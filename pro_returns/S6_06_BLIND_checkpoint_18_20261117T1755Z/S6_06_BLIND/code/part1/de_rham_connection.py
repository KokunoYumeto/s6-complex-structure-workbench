"""Exact algebraic Gauss--Manin and candidate rank-six extension connection.

Columns are the de Rham forms omega_k=x^k dx/y, k=0..3.  The output
is a right connection matrix: derivative of the frame equals frame*Gamma.
The rank-five quotient is by 3 omega_0^omega_3 + omega_1^omega_2.
This script constructs regular root-chart extension forms and verifies the
square-zero cusp residue.  Identifying its real/integral extension is a
separate numerical monodromy comparison, not assumed here.
"""
from pathlib import Path
import sympy as s
from itertools import combinations
import json
x,l=s.symbols('x l');a=-s.Rational(256,3125)
f=x**5+l**3*x+l**4
g=s.symbols('g0:4');r=s.symbols('r0:5')
R=sum(r[j]*x**j for j in range(5))
common=f*sum(g[j]*x**j for j in range(4))+s.diff(R,x)*f-R*s.diff(f,x)/2
coefmat,_=s.linear_eq_to_matrix(s.Poly(common,x).all_coeffs(),list(g)+list(r))
rows=[]
for k in range(4):
    target=s.Poly(-x**k*s.diff(f,l)/2,x)
    rhs=s.Matrix([target.coeff_monomial(x**j) for j in range(8,-1,-1)])
    sol=coefmat.inv()*rhs
    rows.append([s.factor(v) for v in sol[:4]])
G=s.Matrix(rows);Gamma=G.T
J=s.zeros(4);J[0,3]=s.Rational(4,3);J[3,0]=-s.Rational(4,3);J[1,2]=4;J[2,1]=-4
assert s.simplify(G*J+J*G.T)==s.zeros(4)
inds=list(combinations(range(4),2));E=s.zeros(6)
for col,(i,j) in enumerate(inds):
    for z in range(4):
        if z!=j:E[inds.index(tuple(sorted((z,j)))),col]+=Gamma[z,i]*(1 if z<j else -1)
        if i!=z:E[inds.index(tuple(sorted((i,z)))),col]+=Gamma[z,j]*(1 if i<z else -1)
omega=s.Matrix([0,0,3,1,0,0]);assert s.simplify(E*omega)==s.zeros(6,1)
keep=[0,1,2,4,5];Q=s.zeros(5,6)
for z,i in enumerate(keep):Q[z,i]=1
Q[2,3]=-3
Sect=s.eye(6)[:,keep]
GW=(Q*E*Sect).applyfunc(s.factor)
res=GW.applyfunc(lambda v:s.factor(s.limit((l-a)*v,l,a)))
assert res**2==s.zeros(5)
bb=s.symbols('b2 b1 bm1 bm2')
b=s.Matrix([[bb[0]/l**2,bb[1]/l,0,bb[2],bb[3]*l]])/(l-a)
br=b.applyfunc(lambda v:s.limit((l-a)*v,l,a))
eq=s.Matrix(list(br*res)).jacobian(bb)
ns=eq.nullspace()
print('G_rows',G)
print('GammaW',GW)
print('cusp_residue',res,'rank',res.rank())
print('squarezero_extension_parameter_equations',eq,'nullspace',ns)
print('gauge_form',GW[2,:])
forms=[]
for v in ns:
    form=b.subs(dict(zip(bb,v)))
    R6=s.zeros(6);R6[1:,1:]=res;R6[0,1:]=form.applyfunc(lambda z:s.limit((l-a)*z,l,a))
    print('extension',v,'form',form,'residue_rank',R6.rank(),'squarezero',R6**2==s.zeros(6))
    forms.append(form)
out={'Gamma4':[[str(v) for v in row] for row in Gamma.tolist()],
     'Gamma5':[[str(v) for v in row] for row in GW.tolist()],
     'extension_forms':[[str(v) for v in form] for form in forms],
     'root_orders':[5,4],'cusp':str(a)}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))

# N=2*pi*i*R6 in the algebraic canonical frame.  The coefficient below
# uses F=(w0+z*(4/3)e,w1,w2), G=(e,w_minus1,w_minus2).
z=s.symbols('z')
R6=s.zeros(6);R6[1:,1:]=res
R6[0,1:]=forms[0].applyfunc(lambda t:s.limit((l-a)*t,l,a))
F=s.zeros(6,3);F[3,0]=1;F[0,0]=s.Rational(4,3)*z;F[2,1]=1;F[1,2]=1
quot=s.zeros(3,6);quot[0,0]=1;quot[0,3]=-s.Rational(4,3)*z;quot[1,4]=1;quot[2,5]=1
NF=(quot*R6*F).applyfunc(s.factor)
print('cusp_R6_algebraic_frame',R6)
print('residue_F_to_G_order_O_L_L2',NF,'det',s.factor(NF.det()))
extra={'R6':[[str(v) for v in row] for row in R6.tolist()],
       'F_to_G':[[str(v) for v in row] for row in NF.tolist()],
       'F_order':['O','L','L2'],'G_order':['O','L-1','L-2'],
       'N_factor':'2*pi*i','parameter':'F0=w0+(4/3)*z*e',
       'extension_scale':'first nullspace direction; integral real normalization not yet matched'}
Path(__file__).with_name('cusp_residue_weight_bases.json').write_text(json.dumps(extra,indent=2))
