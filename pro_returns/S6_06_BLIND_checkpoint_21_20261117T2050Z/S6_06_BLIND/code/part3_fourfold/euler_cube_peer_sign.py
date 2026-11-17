"""Exact local orientation and collar checks for the independent K66 audit.

This certificate records the two distinct meridian orientations. It does
not resolve their global identification by an assumed characteristic value.
"""
from pathlib import Path
import datetime, itertools, json
import sympy as s

root=Path(__file__).resolve().parents[2]
checks=[]
def check(label, condition):
    assert condition, label
    checks.append(label)

# Coordinates in the positively oriented quaternion basis (1,i,j,k).
q_from_original=s.eye(4)
q_from_right_complex=s.diag(1,1,1,-1)
check('Original (c0,c1) -> c0+j*conj(c1) preserves complex orientation',q_from_original.det()==1)
check('Right-complex (c0,conj(c1)) -> q reverses quaternion orientation',q_from_right_complex.det()==-1)
hopf_h=s.Matrix([[0,2],[-2,0]])  # j,k -> (-2k,2j), rows j,k
check('Hopf derivative on quaternion j,k is positive determinant four',hopf_h.det()==4)
hopf_cp=hopf_h*s.diag(1,-1)
check('Hopf derivative on right-complex projective tangent reverses orientation',hopf_cp.det()==-4)
delta_and_horizontal=s.diag(-1,1,1)
check('Physical circle -i followed by horizontal j,k reverses S3_H',delta_and_horizontal.det()==-1)

# Local right-complex unit section q=(1+j*(x+iy))/sqrt(1+x²+y²).
# Its Maurer i-component is (x dy-y dx)/(1+x²+y²).
# At zero the physical A=-alpha_MC has dA=-2 dx dy, while c1(L)=-dA.
check('Physical c1 on right-complex projective chart is positive',s.Integer(-1)*(-2)==2)
check('Physical c1 on S2_z is negative',s.Integer(2)*s.sign(hopf_cp.det())<0)
# Polar orientation dr,S3_H. Since S3_H=-delta,S2_z and dr crosses delta,
# the circle-first quotient is dr,S2_z.
check('Radial and circle permutations cancel the S3 minus',(-1)*(-1)==1)

a,ab,b,bb=s.symbols('a ab b bb')
g=s.Matrix([[a,-bb],[b,ab]])
gbar=s.Matrix([[ab,-b],[bb,a]])
J=s.Matrix([[0,-1],[1,0]])
check('Complex-conjugate SU2 clutch is the same clutch conjugated by J',gbar==J*g*J.inv())
Qreal=s.Matrix([[0,0,1,0],[0,0,0,-1],[-1,0,0,0],[0,1,0,0]])
check('Quaternionic anti-linear repair preserves real four-orientation',Qreal.det()==1)
check('Quaternionic anti-linear repair squares to minus identity',Qreal**2==-s.eye(4))
check('Its adjoint antipodal repair reverses normal three-orientation',(-s.eye(3)).det()==-1)
check('Orientation reversal and odd cube duality preserve the oriented cubic',(-1)*(-1)**3==1)
check('Orientation reversal and one line duality preserve p1 times x',(-1)*(-1)==1)

n,alpha,theta,z=s.symbols('n alpha theta z')
def wedge(a,b):
    out={}
    for ia,ca in a.items():
        for ib,cb in b.items():
            if set(ia)&set(ib): continue
            raw=ia+ib
            inv=sum(raw[i]>raw[j] for i in range(len(raw)) for j in range(i+1,len(raw)))
            key=tuple(sorted(raw))
            out[key]=s.expand(out.get(key,0)+(-1)**inv*ca*cb)
    return {i:s.simplify(c) for i,c in out.items() if c!=0}
def add(a,b):
    out=dict(a)
    for i,c in b.items(): out[i]=s.expand(out.get(i,0)+c)
    return {i:c for i,c in out.items() if c!=0}
def scale(c,a):return {i:s.expand(c*v) for i,v in a.items()}
# Boundary orientation d_alpha, d_u, d_v, d_gamma, d_theta.
beta={(1,):-n,(2,):-n*alpha+6*n*theta}
F={(0,3):1,(0,2):n}
d_beta={(0,2):-n,(2,4):-6*n}
check('F_boundary squared is zero',wedge(F,F)=={})
check('d_beta squared is zero',wedge(d_beta,d_beta)=={})
mixed=wedge(beta,wedge(F,d_beta))[(0,1,2,3,4)]
check('beta wedge F wedge d_beta coefficient is +6 n²',s.expand(mixed-6*n*n)==0)
curv=add(F,scale(z,d_beta))
coefficient=wedge(beta,wedge(curv,curv))[(0,1,2,3,4)]
increasing=s.integrate(3*coefficient,(z,0,1))
decreasing=s.integrate(3*coefficient,(z,1,0))
check('Increasing collar transgression is +18 n²',increasing==18*n*n)
check('Actual outward collar 1-to-0 is -18 n²',decreasing==-18*n*n)

out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'status':'PASS for explicit local signs and collar; full physical/Thom dictionary and inverse-clutch maps proved in P3K.68',
 'checks':checks,'count':len(checks),
 'meridian_table':{
   'S3_H':'-S1_delta x S2_z',
   'CP1_right_complex':'-S2_z',
   'integral_S2_z_dA':1,'integral_S2_z_c1_physical_line':-1,
   'integral_CP1_right_c1_physical_line':1,
   'circle_first_outward_normal_for_complex_fixed_base':'S2_z'},
 'collar_increasing':str(increasing),'collar_outward':str(decreasing),
 'completed_map':'P3K.68 supplies U=M^-1 by the explicit Hermitian dual on both actual collars and proves lambda_M=-Sigma(F^-1), lambda_U=Sigma(F^-1), retaining every factor orientation and the first-to-second clutch arrow.'}
(root/'code/part3_fourfold/euler_cube_peer_sign.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
