"""Integral lattice calculation for the untwisted semistable neck.

The geometric identification of these maps is proved in AB_push.tex.
All calculations here are exact in Z or Q.
"""
from pathlib import Path
import json
import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

half=s.Rational(1,2)
roots=[s.Matrix([half,-half,-half,-half,-half,-half,-half,half]),
       s.Matrix([1,1,0,0,0,0,0,0]),s.Matrix([-1,1,0,0,0,0,0,0]),
       s.Matrix([0,-1,1,0,0,0,0,0]),s.Matrix([0,0,-1,1,0,0,0,0]),
       s.Matrix([0,0,0,-1,1,0,0,0]),s.Matrix([0,0,0,0,-1,1,0,0]),
       s.Matrix([0,0,0,0,0,-1,1,0])]
B=s.Matrix.hstack(*roots)
G8=B.T*B
assert G8.det()==1
m8=B.inv()*s.Matrix([1,-1,0,0,0,0,0,0])
v8=B.inv()*s.Matrix([1,0,2,1,0,0,0,0])
assert all(x.q==1 for x in list(m8)+list(v8))
G=s.diag(s.Matrix([[0,1],[1,-1]]),-G8)
F=s.Matrix([1,0]+[0]*8)
O=s.Matrix([0,1]+[0]*8)
m=s.Matrix([1,0]+list(m8))
v=s.Matrix([0,0]+list(v8))
I=s.eye(10)
T=I+v*(F.T*G)-F*(v.T*G)+3*F*(F.T*G)
assert T.T*G*T==G
assert T.det()==1
assert (T.T*G*m)==G*(m-F)
C=s.Matrix.vstack(F.T*G,v.T*G,m.T*G)
dom=DomainMatrix.from_Matrix(C).convert_to(ZZ)
D,U,V=smith_normal_decomp(dom)
D=D.to_Matrix();U=U.to_Matrix();V=V.to_Matrix()
assert U*C*V==D
K=V[:,3:]
assert C*K==s.zeros(3,7)
assert V.det() in [1,-1]
M=s.Matrix.hstack(F,v,m)
D2,U2,V2=smith_normal_decomp(DomainMatrix.from_Matrix(M).convert_to(ZZ))
D2=D2.to_Matrix();U2=U2.to_Matrix();V2=V2.to_Matrix()
assert U2*M*V2==D2
assert all(abs(D2[i,i])==1 for i in range(3))
quotient=U2[3:,:]
Cmon=quotient*K
SNF=smith_normal_form(Cmon,domain=ZZ)
assert Cmon.rank()==6
smith=[abs(int(SNF[i,i])) for i in range(7)]
assert smith==[1,1,1,1,1,11,0]
mon=s.eye(14)
mon[:7,7:]=Cmon
assert (mon-s.eye(14))**2==s.zeros(14)
out={
 'intersection_matrix':G.tolist(),'F':list(F),'O':list(O),'m':list(m),'v':list(v),
 'gram_F_v_m':(M.T*G*M).tolist(),'T':T.tolist(),
 'constraint_matrix':C.tolist(),'kernel_basis':K.tolist(),
 'quotient_projection':quotient.tolist(),'neck_N_block':Cmon.tolist(),
 'neck_N_smith':smith,'N_rank':6,'N_square_zero':True,
 'betti_untwisted':[1,1,8,14,8,1,1],
 'euler_untwisted':sum((-1)**i*b for i,b in enumerate([1,1,8,14,8,1,1]))}
print(json.dumps(out,indent=2,default=str))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2,default=str)+'\n')
