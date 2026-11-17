"""Independent exact derivation of the actual cusp/ordinary origin differences.

The identification of the two origins is analytic (printed proof); this program
checks the polynomial cocycle algebra after that identification, not the existence
of a filling. Symbols C and mu are single-valued in the cusp parameter.
"""
import sympy as s
from pathlib import Path
import json

x,v,n,h,C,mu,kappa,c=s.symbols('s v n h C mu kappa c')
delta=s.Matrix([0,1])
gamma=s.Matrix([6*mu,C-x-12*v])
F=s.Matrix([mu*(x+12*v)/2,C*(x+12*v)/12-(x+12*v)**2/24+6*v])
b=gamma/12-delta/24
zero=s.zeros(2,1)
assert s.simplify(F.subs(x,x+1)-F-b)==zero
assert s.simplify(F.subs(x,x+12)-F-(gamma-6*delta))==zero
assert s.simplify(F.subs(v,v+n)-F-(n*gamma-6*n*(n-1)*delta))==zero
D=C-12*kappa
sigma=s.Matrix([-c*mu/2,-c*c/24-c*D/12])
bbar=s.Matrix([-h*mu/2,-h*(c+D)/12-h*h/24])
assert s.simplify(sigma.subs(c,c+h)-sigma-bbar)==zero
G=s.Matrix([mu*x/2,C*x/12-x*x/24])
k=-x+12*kappa
assert s.simplify(F-sigma.subs(c,-12*v)-k*v*delta-G-6*v*delta)==zero
A1=s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
U1=A1[:3,:3];U2=A2[:3,:3]
assert s.Matrix.vstack(U1-s.eye(3),U2-s.eye(3)).rank()==3
fixed1=(U1-s.eye(3)).nullspace();fixed2=(U2-s.eye(3)).nullspace()
out={'status':'PASS','q_step':str(b),'q_12_step':str(gamma-6*delta),
 'r_n_step':str(n*gamma-6*n*(n-1)*delta),'cusp_closing':str(bbar),
 'ordinary_cusp_origin_identity':'F-sigma = k*v*delta+G(s)+6*v*delta',
 'fixed_lines_in_Lambda_Q_mod_delta':[str(fixed1),str(fixed2)],
 'common_fixed_space_dimension':0,
 'scope':'Exact cocycle, closing, and linear-invariant arithmetic; analytic origin identification and extension arguments are separate proofs.'}
text=json.dumps(out,indent=2)+'\n'
Path(__file__).with_suffix('.output.json').write_text(text)
print(text)
