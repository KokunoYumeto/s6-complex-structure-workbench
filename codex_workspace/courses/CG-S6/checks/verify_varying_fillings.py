"""Exact symbolic checks for the original varying periods. CC0-1.0."""
from pathlib import Path
import hashlib,json
import sympy as s

root=Path(__file__).resolve().parents[1]
T,M,B,q=s.symbols('T M B q')
z,u=s.symbols('z u')
rho=(1+s.sqrt(3)*s.I)/2
As=[s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]]),s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])]
vs=[s.Matrix([1,2,-4,0]),s.Matrix([-1,-3,3,0])]
checks=[]
def zero(value):
    return all(s.simplify(s.together(v))==0 for v in value) if isinstance(value,s.MatrixBase) else s.simplify(s.together(value))==0
def check(name,value):
    assert zero(value),name
    checks.append(name)
def Pi(t,m,b):return s.Matrix([[6*m,t,1,0],[b,m,0,1]])
for j,degree,center,phase,d,e,c in [(1,3,rho,(-1-s.sqrt(3)*s.I)/2,1,2,-1),(2,4,s.I,-s.I,2,1,1)]:
    label=f'case_{j}:'
    if j==1:
        tr=lambda t,m:((t-1)/t,(1-m)/t)
        phi=lambda t,m:2-6*(1-m)**2/t
        R=lambda t,m:s.Matrix([[-1/t,0],[(1-m)/t,1]])
        particular=lambda t:(2-t)/3
        roots=[1,(-1+s.sqrt(3)*s.I)/2,(-1-s.sqrt(3)*s.I)/2]
    else:
        tr=lambda t,m:(-1/t,1+m/t)
        phi=lambda t,m:-3-6*m*m/t
        R=lambda t,m:s.Matrix([[1/t,0],[-m/t,1]])
        particular=lambda t:(1-t)/2
        roots=[1,s.I,-1,-s.I]
    t1,m1=tr(T,M)
    check(label+'full_period_covariance',R(T,M)*Pi(T,M,B)-Pi(t1,m1,B+phi(T,M))*As[j-1])
    check(label+'central_additive_term',phi(center,particular(center)))
    phase_q=s.conjugate(center)/center
    check(label+'base_phase',phase**d-phase_q)
    check(label+'correction_phase',phase**e-c/center)
    cayley=lambda t:(t-center)/(t-s.conjugate(center))
    inv=lambda q:(center-s.conjugate(center)*q)/(1-q)
    check(label+'cayley_inverse',cayley(inv(q))-q)
    check(label+'original_period_inverse',inv(cayley(T))-T)
    check(label+'period_rotation',cayley(t1)-phase_q*cayley(T))
    check(label+'full_correction_multiplier',c/T-(c/center)*(1-cayley(T))/(1-phase_q*cayley(T)))
    check(label+'particular_mu',tr(T,particular(T))[1]-particular(t1))
    orbit=[];t,m=T,M;matrix=s.eye(2)
    for k in range(degree):
        orbit.append(s.factor(phi(t,m)))
        matrix=(R(t,m)*matrix).applyfunc(s.factor)
        t,m=map(s.factor,tr(t,m))
    check(label+'tau_returns',t-T)
    check(label+'mu_returns',m-M)
    check(label+'full_linear_covariance_returns',matrix-s.eye(2))
    check(label+'all_additive_terms_sum_to_zero',sum(orbit))
    weighted=sum(k*orbit[k] for k in range(degree))/degree
    shifted=sum(k*orbit[(k+1)%degree] for k in range(degree))/degree
    check(label+'weighted_sum_exact_difference',shifted-weighted-orbit[0])
    check(label+'affine_power_translation',sum((As[j-1]**k*vs[j-1]/degree for k in range(degree)),s.zeros(4,1))-vs[j-1])
    check(label+'all_branch_factors',s.prod(z-a*u for a in roots)-(z**degree-u**degree))
    idempotents=[]
    for a,ca in enumerate(roots):
        ea=s.prod(z-cb*u for b,cb in enumerate(roots) if b!=a)/(u**(degree-1)*s.prod(ca-cb for b,cb in enumerate(roots) if b!=a))
        idempotents.append(ea)
        for b,cb in enumerate(roots):
            check(label+f'branch_{a}_on_{b}',ea.subs(z,cb*u)-(1 if a==b else 0))
    check(label+'all_branch_idempotents_sum_to_one',sum(idempotents)-1)
    for a,ca in enumerate(roots):
        check(label+f'cyclic_branch_phase_{a}',roots[(a+1)%degree]*phase-ca)
    w=s.symbols('w')
    check(label+'logarithm_conjugacy_translation',-w+s.Rational(1,degree)+(w-s.Rational(1,degree)))

tr,ti,mr,mi,br,bi=s.symbols('tr ti mr mi br bi',real=True)
a,b,c,d=s.symbols('a b c d',real=True)
z1=6*(mr+s.I*mi)*a+(tr+s.I*ti)*b+c
z2=(br+s.I*bi)*a+(mr+s.I*mi)*b+d
D=bi-6*mi**2/ti
aa=(s.im(z2)-mi*s.im(z1)/ti)/D
bb=(s.im(z1)-6*mi*aa)/ti
cc=s.re(z1)-6*mr*aa-tr*bb
dd=s.re(z2)-br*aa-mr*bb
for name,actual,expected in [('a',aa,a),('b',bb,b),('c',cc,c),('d',dd,d)]:
    check('full_real_inverse_'+name,actual-expected)
receipt={'lesson':'CG-S6-03','passed':len(checks),'checks':checks,'source_sha256':hashlib.sha256((root/'src/varying-finite-fillings.md').read_bytes()).hexdigest(),'scope':'Exact symbolic covariance, full cyclic cocycles, inverse period maps, real marking and every branch idempotent. Convergence, properness and integral closure are proved in the lesson; symbolic checks do not replace those proofs.'}
(root/'checks/VARYING_FILLING_CHECKS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':len(checks),'lesson':'CG-S6-03'}))
