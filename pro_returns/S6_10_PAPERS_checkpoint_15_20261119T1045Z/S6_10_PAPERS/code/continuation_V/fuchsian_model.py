"""New exact gauge and root-chart checks for the stated rank-six model."""
from pathlib import Path
import json
import sympy as S
l,t,u=S.symbols('lambda t u');a=-S.Rational(256,3125)
d=json.loads(Path(__file__).with_name('gauss_manin_and_residue.json').read_text())
W=S.Matrix([[S.sympify(x.replace('lambda','lam'),locals={'lam':l}) for x in r] for r in d['Gamma_W']])
G=S.zeros(6);G[1:,1:]=W;G[0,1:]=S.Matrix([[-S.Rational(25,6)/l**2,-S.Rational(125,48)/l,0,1,0]])/(l-a)
D=S.diag(1,l**2,l,1,l**-1,l**-2)
F=(D.inv()*G*D+D.inv()*S.diff(D,l)).applyfunc(S.cancel)
R0=F.applyfunc(lambda x:S.limit(l*x,l,0));Ra=F.applyfunc(lambda x:S.limit((l-a)*x,l,a));Rinf=-R0-Ra
assert all(S.cancel(x)==0 for x in F-R0/l-Ra/(l-a))
Rc=G.applyfunc(lambda x:S.limit((l-a)*x,l,a));assert Rc.rank()==3 and Rc*Rc==S.zeros(6)
roots={}
for name,q,spec in [('zero',t,[1,t**6,t**3,1,t**-3,t**-6]),('infinity',u,[1,u**-8,u**-4,1,u**4,u**8])]:
 lam=q**4 if name=='zero' else q**-5;gauge=S.diag(*spec)
 C=(gauge.inv()*G.subs(l,lam)*S.diff(lam,q)*gauge+gauge.inv()*S.diff(gauge,q)).applyfunc(S.cancel)
 roots[name]=[[str(x) for x in C.row(i)] for i in range(6)]
 for x in C:
  den=S.fraction(x)[1];assert den.subs(q,0)!=0

def mat(M):return [[str(M[i,j]) for j in range(M.cols)] for i in range(M.rows)]
out={'R0':mat(R0),'Rcusp':mat(Ra),'Rinfinity':mat(Rinf),'gauge_exponents':[0,2,1,0,-1,-2],'root_connection_matrices':roots,'cusp_residue_rank':Rc.rank(),'cusp_residue_square_zero':True,'status':'PASS'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'R0':out['R0'],'Rcusp':out['Rcusp'],'root_regularity':True,'cusp_rank':Rc.rank(),'status':'PASS'},indent=2))
