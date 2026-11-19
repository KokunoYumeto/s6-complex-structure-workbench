#!/usr/bin/env python3
"""Fresh exact extension-residue classification and alpha normalization."""
from pathlib import Path
import json
import sympy as s
l=s.symbols('lambda');a=-s.Rational(256,3125);data=json.loads(Path(__file__).with_name('gauss_manin_and_residue.json').read_text())
W=s.Matrix([[s.sympify(v.replace('lambda','lam'),locals={'lam':l}) for v in row] for row in data['Gamma_W']]);R=W.applyfunc(lambda x:s.limit((l-a)*x,l,a));aa,bb,cc,dd=s.symbols('a b c d');generic=s.Matrix([[aa/l**2,bb/l,0,cc,dd*l]])/(l-a);br=generic.applyfunc(lambda x:s.limit((l-a)*x,l,a));eq,_=s.linear_eq_to_matrix(list(br*R),[aa,bb,cc,dd]);space=eq.nullspace();assert len(space)==2
v1=s.Matrix([-s.Rational(25,6),-s.Rational(125,48),1,0]);v2=s.Matrix([s.Rational(5,3),-s.Rational(25,3),0,1]);assert eq*v1==s.zeros(eq.rows,1) and eq*v2==s.zeros(eq.rows,1)
def row(v):return s.Matrix([[v[0]/l**2,v[1]/l,0,v[2],v[3]*l]])/(l-a)
b1,b2=row(v1),row(v2);assert (W[2,:]-(-48*b1+60*b2)/3125).applyfunc(s.cancel)==s.zeros(1,5)
Rp=R[:,:3];ker=Rp.nullspace();assert len(ker)==1;v=ker[0]/ker[0][2];bres=b1.applyfunc(lambda x:s.limit((l-a)*x,l,a));evaluation=(bres[:,:3]*v)[0];alpha_algebraic=s.Rational(4,3)*v[2];ratio=s.cancel(evaluation/alpha_algebraic);assert ratio==s.Rational(625,256)
Gamma=s.zeros(6);Gamma[0,1:]=b1;Gamma[1:,1:]=W;RR=Gamma.applyfunc(lambda x:s.limit((l-a)*x,l,a));assert RR**2==s.zeros(6) and RR.rank()==3
# Residue of a formal primitive of omega_i times omega_j at infinity.
J=s.zeros(4)
for i in range(4):
 for j in range(4):
  if i+j==3:J[i,j]=s.Rational(4,3-2*i)
assert J+J.T==s.zeros(4) and J[0,3]==s.Rational(4,3) and J[1,2]==4
out={'status':'PASS','extension_constraint_matrix':eq.tolist(),'extension_parameter_basis':[v1.tolist(),v2.tolist()],'holomorphic_coboundary_coefficients':['-48/3125','60/3125'],'positive_cusp_kernel_vector':v.tolist(),'extension_residue_on_kernel':str(evaluation),'algebraic_contraction_on_kernel':str(alpha_algebraic),'ratio_before_2pii':str(ratio),'alpha_factor':'625*pi*i/128','residue_rank':RR.rank(),'deRham_pairing':J.tolist(),'scope':'Exact displayed meromorphic-extension classification, its holomorphic coboundary direction and scalar normalization. Integral geometric existence is the separate extension-class argument of P1.15.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2,default=str)+'\n');print(json.dumps(out,indent=2,default=str))
