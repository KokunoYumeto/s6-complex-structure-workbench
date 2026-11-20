"""Independent statement-input upper-extension classification.
No earlier checker/proof/producing residue output imported.
"""
from pathlib import Path
import hashlib,json,time
import sympy as s
Aroot=Path(__file__).resolve().parents[1]
input_path=Aroot.parent/'audit_corrections/V_P115_isolated_statement_inputs_06.tex'
assert hashlib.sha256(input_path.read_bytes()).hexdigest()=='ace3b9abf8cd0e79f95eef8228dd08b917ec61338cdfe44d83034a8f09519165'
start=time.time();checks=0

def ck(test):
 global checks
 assert test
 checks+=1

def enc(x):
 if isinstance(x,s.MatrixBase):return [[str(x[i,j]) for j in range(x.cols)] for i in range(x.rows)]
 if isinstance(x,dict):return {str(k):enc(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [enc(v) for v in x]
 if isinstance(x,(s.Basic,)):return str(x)
 return x
l=s.symbols('lambda');a=-s.Rational(256,3125)
M=s.Matrix([
 [-8*(625*l+48)/l,-8,10*l,s.Rational(75,2)*l**2,0],
 [-s.Rational(125,2)/l,-4*(625*l+48)/l,8,0,s.Rational(75,2)*l**2],
 [300/l**2,-375/l,0,-48,60*l],
 [120/l**3,0,s.Rational(125,2)/l,4*(625*l+48)/l,-8],
 [0,120/l**3,50/l**2,-s.Rational(125,2)/l,8*(625*l+48)/l]])
GW=M/(3125*l+256)
R=M.subs(l,a)/3125
ck(R**2==s.zeros(5));ck(R.rank()==2)
js=[2,1,0,-1,-2]
deg=[s.floor(s.Rational(4*j,5))+s.floor(-s.Rational(3*j,4)) for j in [-2,-1,0,1,2]]
ck(deg==[-1,-1,0,-1,-1])
lo=[s.ceiling(-s.Rational(3+3*j,4)) for j in js]
hi=[s.ceiling(s.Rational(6+4*j,5)) for j in js]
ck(lo==[-2,-1,0,0,1]);ck(hi==[3,2,2,1,0])
# Each rational coefficient has divisor lower bounds at0,infinity,a.
dim=[max(0,2-z-i) for z,i in zip(lo,hi)]
ck(dim==[1,1,0,1,1])
AA,BB,CC,DD=s.symbols('A B C D');params=s.Matrix([AA,BB,CC,DD])
beta=s.Matrix([[AA/(l*l*(l-a)),BB/(l*(l-a)),0,CC/(l-a),DD*l/(l-a)]])
r=s.Matrix([[AA/(a*a),BB/a,0,CC,DD*a]])
K,_=s.linear_eq_to_matrix(list(r*R),[AA,BB,CC,DD])
ck(K.rank()==2)
sol=s.linsolve((K,s.zeros(K.rows,1)),[AA,BB,CC,DD]);solution=list(sol)[0]
ck(solution==(-s.Rational(25,6)*CC+s.Rational(5,3)*DD,-s.Rational(125,48)*CC-s.Rational(25,3)*DD,CC,DD))
gauge=s.Matrix([s.Rational(300,3125),-s.Rational(375,3125),-s.Rational(48,3125),s.Rational(60,3125)])
ck(K*gauge==s.zeros(K.rows,1))
gauge_beta=beta.subs(dict(zip(params,gauge)))
ck(s.simplify(gauge_beta-GW[2,:])==s.zeros(1,5))
target=s.Matrix([-s.Rational(25,6),-s.Rational(125,48),1,0]);bt=beta.subs(dict(zip(params,target)))
ck(K*target==s.zeros(K.rows,1));ck(s.Matrix.hstack(gauge,target).rank()==2)
class_function=s.Matrix([[0,0,1,s.Rational(4,5)]])
ck((class_function*gauge)[0]==0);ck((class_function*target)[0]==1)
# Explicit decomposition, hence actual quotient and reciprocal gauge map.
sp=CC+s.Rational(4,5)*DD
factor=s.Rational(3125,60)*DD
ck(s.Matrix(solution)==sp*target+factor*gauge)
rt=r.subs(dict(zip(params,target)))
N=s.zeros(6);N[0,1:]=rt;N[1:,1:]=R
ck(N**2==s.zeros(6));ck(N.rank()==3)
Nexact=s.zeros(6);Nexact[0,1:]=r.subs(dict(zip(params,gauge)));Nexact[1:,1:]=R
ck(Nexact.rank()==2)
ker=R[:,:3].nullspace();ck(len(ker)==1);vp=ker[0]/ker[0][2];v=vp.col_join(s.zeros(2,1))
ck(R*v==s.zeros(5,1));ck(v[2]==1)
contraction=(rt*v)[0];alg=s.Rational(4,3)*v[2];ratio=s.simplify(contraction/alg)
ck(ratio==s.Rational(625,256))
ck((GW[2,:].applyfunc(lambda x:s.limit((l-a)*x,l,a))*v)[0]==0)
# All complete upper coefficient rows transformed by the given actual root frames.
u,vv=s.symbols('u v')
rootzero=[];rootinfty=[]
for j,jc in enumerate(js):
 z=s.cancel(4*u**(3+3*jc)*bt[j].subs(l,u**4))
 q=s.cancel(-5*vv**(-6-4*jc)*bt[j].subs(l,vv**-5))
 rootzero.append(z);rootinfty.append(q)
 ck(s.denom(z).subs(u,0)!=0);ck(s.denom(q).subs(vv,0)!=0)
# Integral matrices are copied from the isolated statement.
MA=s.Matrix([[1,0,0,1,-1,1],[0,1,-1,-1,1,0],[0,1,0,-1,0,0],[0,2,-1,-1,0,1],[0,2,0,-1,0,0],[0,1,1,-1,0,0]])
MB=s.Matrix([[1,0,0,0,0,0],[0,0,-1,0,1,0],[0,0,-1,0,0,1],[0,0,-1,0,0,0],[0,1,-1,0,0,0],[0,0,-1,1,0,0]])
inv=s.Matrix.vstack(MA-s.eye(6),MB-s.eye(6)).nullspace();dual=s.Matrix.vstack(MA.T-s.eye(6),MB.T-s.eye(6)).nullspace()
e0=s.eye(6)[:,0]
ck(len(inv)==1);ck(inv[0]==e0);ck(len(dual)==0)
zsym=s.symbols('z:36');Z=s.Matrix(6,6,zsym)
central,_=s.linear_eq_to_matrix(list(Z*MA-MA*Z)+list(Z*MB-MB*Z),zsym)
cn=central.nullspace();ck(central.rank()==35);ck(len(cn)==1)
CZ=s.Matrix(6,6,list(cn[0]));ck(CZ==s.eye(6))
# No nonzero normalized centralizer infinitesimal remains afterZ e0=0.
normal,_=s.linear_eq_to_matrix(list(Z*MA-MA*Z)+list(Z*MB-MB*Z)+list(Z*e0),zsym)
ck(normal.rank()==36)
res=dict(status='PASS',assertions=checks,elapsed_seconds=time.time()-start,input_sha256=hashlib.sha256(input_path.read_bytes()).hexdigest(),frozen_derivation_sha256=hashlib.sha256((Aroot/'V_P115_statement_derivation_06.md').read_bytes()).hexdigest(),method='Fresh exact rational SymPy linear systems from isolated root-frame and integral-matrix inputs; no existing checker imported.',quotient_Gamma=GW,residue=R,root_lower_bounds=lo,infinity_lower_bounds=hi,upper_dimensions=dim,parameter_constraint_matrix=K,parameter_solution=solution,gauge_parameter=gauge,target_parameter=target,class_function=class_function,exact_decomposition={'class':sp,'gauge_coefficient':factor},full_target_residue=N,kernel_in_P=v,contraction_residue=contraction,alpha_alg=alg,ratio_before_2pi_i=ratio,alpha_factor='625*pi*i/128',target_zero_root_coefficients=rootzero,target_infinity_root_coefficients=rootinfty,common_invariants=inv,common_dual_invariants=dual,centralizer_rank=central.rank(),centralizer_basis=[CZ],normalized_centralizer_kernel_rank=normal.rank(),scope='Exact upper-extension quotient, nonsplit target and supplied local system, existence of a connection isomorphism fixing invariant line, contraction normalization and uniqueness of the common monodromy intertwiner. No numerical period computation; supplied quotient local-system identification remains named input. Prior visual exposure explicitly recorded.')
(Aroot/'V_P115_extension_independent_06.json').write_text(json.dumps(enc(res),indent=2)+'\n')
print(json.dumps({'status':'PASS','assertions':checks,'residue_rank':R.rank(),'upper_solution':enc(solution),'kernel_in_P':enc(v),'contraction_residue':str(contraction),'alpha_ratio_before_2pi_i':str(ratio),'centralizer_dimension':len(cn),'elapsed_seconds':time.time()-start},indent=2))
