"""Fresh exact F2.1/F3.1/F3.3 checks; written after the proofs were read."""
from pathlib import Path
import hashlib,json,platform,time
import sympy as s

start=time.monotonic(); checks=[]
def check(name, assertion):
    assert assertion,name
    checks.append({'name':name,'pass':True})

I=s.eye(4)
J=s.Matrix([[0,0,-1,0],[0,0,0,-6],[1,0,0,0],[0,s.Rational(1,6),0,0]])
Omega=s.Matrix([[0,0,0,6],[0,0,1,0],[0,-1,0,0],[-6,0,0,0]])
R=s.Matrix([[1,0,0,0],[0,1,72,0],[0,0,1,0],[-12,0,0,1]])
N=R-I
check('F2.1 complex structure',J*J==-I)
check('F2.1 symplectic complex structure',J.T*Omega*J==Omega)
check('F2.1 symmetric metric',Omega*J==(Omega*J).T)
check('F2.1 exact metric eigenvalues',(Omega*J).eigenvals()=={s.Integer(1):1,s.Integer(-1):1,s.Integer(6):1,s.Integer(-6):1})
check('F2.1 null invariant at e', (Omega*J)[3,3]==0)
check('F2.1 symplectic stabilizer',R.T*Omega*R==Omega)
check('F2.1 actual fixed point',R*J==J*R)
check('F2.1 nonzero square-zero nilpotent',N!=s.zeros(4) and N*N==s.zeros(4))
m,n=s.symbols('m n',integer=True)
check('F2.1 universal additive powers',(I+m*N)*(I+n*N)==I+(m+n)*N)
T=s.Matrix([[1,1],[0,1]])
literal=s.diag(1,T**72,1);literal[3,0]=-12
check('F2.1 exact g lift',R==literal)
check('F2.1 integral character membership',72%12==(-12)%12==0)

t=s.symbols('t'); A=-3*t**3*(t-1);B=2*t**4*(t-1)**2
disc=s.factor(-16*(4*A**3+27*B**2))
j=s.cancel(1728*4*A**3/(4*A**3+27*B**2))
check('F3.1 discriminant',disc==1728*t**8*(t-1)**3)
check('F3.1 exact j cancellation',j==1728*t)
check('F3.1 left inverse derivative',s.diff(j/1728,t)==1)

# Fixed-point calculations in Q[rho]/(rho^2-rho+1); no floating root chosen.
rho=s.symbols('rho'); relation=rho**2-rho+1
def red(x):
    num,den=s.fraction(s.cancel(x))
    return s.rem(s.rem(num,relation,rho)*s.invert(den,relation,rho),relation,rho)
mu=(2-rho)/3;kappa=-rho
mu_ratio=-(1-mu)/rho**2/(kappa+1/rho)
beta_ratio=(12*(1-mu)/rho*mu_ratio+6*(1-mu)**2/rho**2)/(kappa-1)
check('F3.3 fixed-point mu derivative',red(mu_ratio)==-s.Rational(1,3))
check('F3.3 fixed-point beta derivative',red(beta_ratio)==s.Rational(2,3))
check('F3.3 actual determinant zero',red(6*mu_ratio**2-beta_ratio)==0)
B0=s.Matrix([[0,1],[-1,0]])
check('F3.3 cusp leading determinant',B0.det()==1)

out={'reviewer':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort; same model family',
     'chronology':'Fresh exact implementation after printed proof reading; no absent f_exact.py replay',
     'python':platform.python_version(),'sympy':s.__version__,'all_pass':True,
     'check_count':len(checks),'checks':checks,
     'matrices':{k:[[str(x) for x in row] for row in M.tolist()] for k,M in [('J0',J),('Omega',Omega),('R',R),('N',N),('OmegaJ0',Omega*J)]},
     'discriminant':str(disc),'j':str(j),'rho_relation':str(relation),
     'mu_derivative_ratio':str(red(mu_ratio)),'beta_derivative_ratio':str(red(beta_ratio)),
     'analytic_boundary':'Cusp holomorphy, quotient properness and finite-disc descent are the stated printed geometric inputs; these exact finite checks do not prove those analytic statements.',
     'elapsed_seconds':round(time.monotonic()-start,6)}
path=Path(__file__).with_suffix('.output.json');path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'all_pass':True,'check_count':len(checks),'output':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()},indent=2))
