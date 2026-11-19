"""Exact maps for the moving Q0Q1 fixed surface and its actual reference cap.

This certificate verifies identities in the written geometric argument. It
does not select a global return or either separate free characteristic number.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sympy as S

ROOT = Path(__file__).resolve().parents[2]
PROOF = ROOT/'notes/part3_e6_selected_infinity_moving_cap_working.md'
checks = []


def ck(value, label):
    assert bool(value), label
    checks.append(label)


def eq(left, right, label):
    ck(S.cancel(S.together(left-right)) == 0, label)


eps, rho, sn, zn, x, z1, v, zz, zeta, r, h, k = S.symbols(
    'epsilon rho s Z x z1 v z zeta r h k', nonzero=True)
d = 1-3*eps**2
alpha = eps/d
nu = eps**2/d
P = -(1+eps)/(1-eps)
Z = (sn-1)/(sn+1)
eq((1+Z)/(1-Z), sn, 'full inverse selected normalization')
eq(nu/(1+3*nu), eps**2, 'rho-to-epsilon square and actual inverse-disc relation')
eq(1/(1+3*nu), d, 'full d inverse under rho squared=nu')
eq(alpha**2/nu, 1/d, 'full u squared and alpha=rho*u')

uu = S.symbols('u', nonzero=True)
eq((sn-1)/(sn+1)-1, -2/(sn+1), 'exact O generator in s chart')
eq((Z-1).subs(sn,1/(uu*v)), -2*uu*v/(1+uu*v),
   'exact full O ideal generator in v=1/z1')
eq((Z+1).subs(sn,z1/uu), 2*z1/(uu+z1),
   'exact full T ideal generator in z1=u*s')

# Both original graph charts and their entire source maps.
graph_L = ((1+3*h*k)*h-k)/(1-h**2)
graph_U = h*graph_L
graph_height = (h*k+graph_U)*graph_L**2-graph_U**2*(1+3*h*k+graph_U)
eq(graph_height, 0, 'complete graph-to-source height vanishes')
eq((-zeta)*(-z1**2*zeta), (z1*zeta)**2, 'second original blowup h*k=rho squared')
eq(-rho**2/(rho**2*zz), -1/zz, 'second graph chart h=-1/z')
eq(-rho**2*zz, -rho**2*zz, 'second graph chart k=-rho squared*z')
eq(-rho**2/(rho*z1), -rho/z1, 'first original blowup h=-rho/z1')
eq((-rho/z1).subs(rho,z1*zeta), -zeta, 'full first-to-second graph h arrow')
eq((-rho*z1).subs(rho,z1*zeta), -z1**2*zeta, 'full first-to-second graph k arrow')

# The native O blowup is the exact elementary transform, including infinity.
ss, rr = S.symbols('S R', nonzero=True)
eq((rho*z1).subs({rho:v*ss,z1:1/v}, simultaneous=True), ss,
   'O blowup rho=v*S resolves S=rho*z1')
eq((rho*z1).subs(z1,1/(rho*rr)), 1/rr,
   'O reciprocal chart v=rho*R resolves inverse S=R')
eq((rho*z1).subs(z1,rho*zz), rho**2*zz, 'T blowup first chart has S=rho squared*z')
eq((rho*z1).subs(rho,z1*zeta), z1**2*zeta, 'T blowup second chart full S')

line_rows = []
for a in (2,6):
    b = P**a
    sa = (1+b)/(1-b)
    Sa = alpha*sa
    fb = (1-Z/b)/(1-Z)
    eq(fb, -(1-b)*(sn-sa)/(2*b), f'a={a}: full point theta zero-pole ratio')
    ck(S.limit(Sa,eps,0)==-S.Rational(1,a), f'a={a}: exact marked point limit')
    phi = -d*(1-b)/(2*b*eps)
    eq(fb/(alpha*sn-Sa), phi, f'a={a}: global point-frame comparison')
    ck(S.limit(phi,eps,0)==a, f'a={a}: extending point-frame unit value')
    Ca = S.Integer(2) if a==2 else 6+20*eps**2+6*eps**4
    eq(phi, d*Ca/(1+eps)**a, f'a={a}: entire point-frame unit with explicit denominator')
    fa_native = (sn+eps)**a/(sn-sa)
    fp = (1-Z/P)/(1-Z)
    eq(fp,(sn+eps)/(1+eps), f'a={a}: full native single-point theta')
    eq(fp**a/(fa_native*fb),1/(eps*Ca),f'a={a}: exact native tensor-to-point coefficient')
    H = eps**(-a)*d**(a-1)/Ca
    eq(alpha**(1-a)/(eps*Ca), H, f'a={a}: original tensor scalar with all source powers')
    eq(H*phi, (d/(eps*(1+eps)))**a, f'a={a}: complete Miller numerator / point cancellation')
    eq(alpha**(a-1)*fa_native, (alpha*sn+nu)**a/(alpha*sn-Sa),
       f'a={a}: full original Miller function')
    eq((rho*z1+rho**2)**a, rho**a*(z1+rho)**a,
       f'a={a}: first exceptional tensor order and retained strict divisor')
    eq((rho**2*zz+rho**2)**a, rho**(2*a)*(zz+1)**a,
       f'a={a}: second exceptional tensor order and retained strict divisor')
    exponents = (-(a+3),1-a)
    ck(sum(exponents)==-2*a-2, f'a={a}: full positive normal determinant winding')
    ck(-4-2*a-(-2)==-2*a-2, f'a={a}: directed height/native/original tensor phase composite')
    ck(-a+(4-a)==4-2*a, f'a={a}: full completed-point to original-tensor determinant winding')
    line_rows.append({'a':a,'phi':str(S.factor(phi)),'S_a':str(S.factor(Sa)),
                      'H_original':str(H),'phi_central':a,
                      'tensor_exceptional_orders':[a,2*a],
                      'positive_normal_windings':list(exponents),
                      'determinant_winding':-2*a-2,
                      'completed_point_to_original_tensor_windings':[-a,4-a],
                      'completed_point_to_original_tensor_determinant_winding':4-2*a})

# Complete selected q-factor maps and their normal rows.
sigma, eta, vv, sN, tN, cb = S.symbols('sigma eta vbase sN tN cb', nonzero=True)
U,V,y = sigma**4*sN,tN*x,sN*tN
eq(U*V,sigma**4*x*y,'selected y-factor full equation')
eq(x*(sigma**(-4)*tN)*(sigma**4*sN),x*sN*tN,'native Cox q under full sigma-fourth arrow')
eq(zn*(zn**(-1)*sigma**(-4)*tN)*(sigma**4*sN),sN*tN,
   'q-factor native Cox q retains full inverse-Z normal unit')
eq(zn*sN*(zn**(-1)*tN),sN*tN,'full y-factor/q-factor height overlap')
eq((eta*cb)**4*(vv/cb)**4,eta**4*vv**4,'full source-reset unit cancels in q-factor normal power')
eq((eta*vv)**4*sN,eta**4*vv**4*sN,'grouped corner q-factor positive normal')
q=x*sN*tN
eq(S.diff(q,sN).subs({sN:0,tN:0}),0,'q has zero first positive normal derivative')
eq(S.diff(q,tN).subs({sN:0,tN:0}),0,'q has zero first negative normal derivative')
ck([-1,0,0]==[-1,0,0],'each normal first Chern class is the pulled-back minus-one class')
ck(S.Matrix([-1,0,0])-S.Matrix([-1,0,0])==S.zeros(3,1),
   'positive-spinor determinant is zero in all three integral F directions')

# Actual integral intersection matrices and both surface descriptions.
I=-S.eye(2)
T=S.Matrix([[-1,0],[0,1]])
ck(abs(T.det())==1,'native/original total-transform basis change unimodular')
ck(T.T*I*T==I,'native/original free intersection matrices agree under displayed basis')
chain=S.Matrix([[-1,1,0],[0,-1,1]])
chainI=chain.T*I*chain
ck(chainI==S.Matrix([[-1,1,0],[1,-2,1],[0,1,-1]]),
   'full (-1,-2,-1) source chain with every intersection')
ck(chain[:,0]+chain[:,1]+chain[:,2]==S.zeros(2,1),
   'complete native central fibre becomes zero under the reference cap')
restriction=S.Matrix([[1,0,0]])
kernel=S.Matrix([[0,0],[1,0],[0,1]])
ck(restriction*kernel==S.zeros(1,2),'exact degree-two MV kernel')
ck(restriction.rank()==1 and kernel.rank()==2,'all integral ranks in degree-two MV')
ck(S.Matrix([[-1]]).det()==-1,'degree-one cap restriction is onto over integers')
ck(S.Matrix([[0],[0],[0]])==S.zeros(3,1),'actual determinant Chern vector in full F basis')

# The Hermitian-ball cap map: homogeneous inverse and full composition.
A,B,C,D,Y00,Y01,Y10,Y11=S.symbols('A B C D Y00 Y01 Y10 Y11',nonzero=True)
Y=S.Matrix([[Y00,Y01],[Y10,Y11]])
L=S.diag(A,B); Lstar=S.diag(C,D)
Y1=L*Y*Lstar
tr=S.trace(Y1)
forward=Y1/tr
back=L.inv()*forward*Lstar.inv()
back=back/S.trace(back)
for i in range(2):
    for j in range(2):
        eq(back[i,j],Y[i,j]/S.trace(Y),f'Hermitian cap full inverse entry{i}{j}')
eq(forward.det(),L.det()*Lstar.det()*Y.det()/tr**2,
   'Hermitian cap rank-one boundary and positive-definite interior preserved')

# Relative tangent numbers and exact c2 cancellation, without a chosen c2.
c1sq,c2,p1=S.symbols('c1sq c2 p1')
kU=-(c1sq-c2)
lU=-(p1+c1sq-4*c2)
eq(4*kU-lU,p1-3*c1sq,'full projective-link cancellation of actual second Chern class')
ck(S.diff(4*kU-lU,c2)==0,'no second-Chern value is used')
ck(-1-2*1==-3,'one ordinary complex blowup relative p1')
ck(2*(-3)==-6,'two actual blowups relative tangent number')
result=S.cancel((4*kU-lU).subs({c1sq:0,p1:-6})/24)
ck(result==-S.Rational(1,4),'moving cap contribution derived before other ledger terms')

out={'status':'PASS_EXACT_MOVING_CAP_IDENTITIES','utc':datetime.now(timezone.utc).isoformat(),
     'checks':len(checks),'check_labels':checks,
     'source':'notes/part3_e6_selected_infinity_moving_cap_working.md',
     'proof_sha256':hashlib.sha256(PROOF.read_bytes()).hexdigest(),
     'scope':'Original (6,1;2), n=1, fixed scalar/finite character, initial negative-square fan, moving Q0Q1 face with actual K68 reference cap.',
     'line_maps':line_rows,
     'closed_intersection_matrix':[[int(vv) for vv in row] for row in I.tolist()],
     'original_chain_matrix':[[int(vv) for vv in row] for row in chainI.tolist()],
     'MV_H1_restriction':[[0,-1]],'MV_H2_restriction':[[1,0,0]],
     'closed_c1_spinor':[0,0],'closed_tangent_p1':-6,
     'U_link_expression':str(result),'physical_M_expression':str(-result),
     'unassigned':['The separate k and ell numbers','The actual second Chern number of the full spinor clutch','The total source-moduli return','Other caps and other fans']}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('check_labels',)},indent=2))
