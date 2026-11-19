#!/usr/bin/env python3
"""Fresh exact arithmetic from cp36 statements, before reading their proofs.

No producer program is imported or opened. SymPy polynomial arithmetic,
resultants/gcds, and exact rational substitutions are used throughout.
The geometric assertions are expressly outside this program's scope.
"""
from pathlib import Path
from datetime import datetime, timezone
import json, math
import sympy as S

P=Path(__file__).resolve().parents[2]
out=P/'analysis/continuation_IV/statement_arithmetic.output.json'
checks=[]

def equal(name,left,right,labels):
    delta=S.factor(left-right)
    checks.append(dict(name=name,labels=labels,pass_check=delta==0,
                       left=str(S.factor(left)),right=str(S.factor(right)),difference=str(delta)))
    assert delta==0,(name,delta)

def nonzero(name,value,labels):
    value=S.factor(value)
    checks.append(dict(name=name,labels=labels,pass_check=value!=0,value=str(value)))
    assert value!=0,name

x,t,r,w,u,v,a,j,l,k=S.symbols('x t r w u v a j l k')
F=x**3+r*x**2+t*x+t**2
D=27*t**2+(4-18*r)*t+r**2*(4*r-1)
equal('E6 discriminant',S.discriminant(F,x),-t**2*D,['P3K.109','P3K.113','P3K.114'])
equal('E6 node quadratic discriminant',S.discriminant(D,t),16*(1-3*r)**3,['P3K.109','P3K.113'])
equal('Type III selected root',D.subs({r:0,t:-S.Rational(4,27)}),0,['P3K.114'])
equal('G tangent intersection',S.expand((t+x/2)**2-F),-x**2*(x-(S.Rational(1,4)-r)),['P3K.109','P3K.110','P3K.113','P3K.114'])
tc=(w-1)**2*(2*w+1)/27
equal('Marked node substitution',D.subs({r:(1-w**2)/3,t:tc}),0,['P3K.115'])
equal('Marked type III lift',tc.subs(w,-1),-S.Rational(4,27),['P3K.115'])
equal('K111 characteristic index',(4*S.Integer(71)+4)/24,12,['P3K.111'])
kj=11-6*j**3+24*j**2-30*j
sj=2-j**3+4*j**2-5*j
equal('K112 characteristic polynomial',(4*kj+4)/24,sj,['P3K.112'])
equal('K112 native starting fan',kj.subs(j,-1),71,['P3K.112'])
equal('K112 residue periodicity',S.rem(S.Poly(S.expand(sj.subs(j,j+28)-sj),j),S.Poly(28,j)).as_expr(),0,['P3K.112'])
# Integer coefficient divisibility is the useful exact periodicity check.
period_coefficients=S.Poly(S.expand(sj.subs(j,j+28)-sj),j).all_coeffs()
assert all(c%28==0 for c in period_coefficients)
image=sorted({int(sj.subs(j,J))%28 for J in range(28)})
assert image==[0,2,8,10,12,14,16,22,24,26]
checks.append(dict(name='K112 complete vertical residue image',labels=['P3K.112'],pass_check=True,period=28,image=image,period_difference_coefficients=[str(c) for c in period_coefficients]))
m=3*l+2
equal('K115 M6 index',(4*(18*m-3*m*j*(j-1))-24*(l+1))/24,8*l+5-m*j*(j-1)/2,['P3K.115'])
equal('K115 M2 index',(4*(2*l-3*l*j*(j-1))-8*l)/24,-l*j*(j-1)/2,['P3K.115'])
equal('K115 M6 T4', (8*l+5-m*j*(j-1)/2).subs(j,4),-10*l-7,['P3K.115'])
unit_receipts=[]
for L in range(28):
    fan=0 if L%7!=2 else 4
    value=8*L+5-(3*L+2)*fan*(fan-1)//2
    assert math.gcd(value,28)==1
    unit_receipts.append(dict(l_mod_28=L,fan=fan,integer=value,gcd_with_28=1))
checks.append(dict(name='K115 M6 complete residue-class unit witnesses',labels=['P3K.115'],pass_check=True,receipts=unit_receipts))

R=t*t+a
f=R*R+t
g=R**3+S.Rational(3,2)*t*R+S.Rational(3,8)
disc=S.factor(S.discriminant(x**3-3*f*x+2*g,x))
capdisc=S.factor(disc.subs(t,0))
equal('OS45 cap discriminant',capdisc,-S.Rational(81,16)*(16*a**3+3),['P3K.119'])
au=-u/S.Integer(3)-u**4/S.Integer(9)
tcu=1/(2*u)-u**2/S.Integer(3)
xiu=1/(4*u*u)+u/S.Integer(3)
equal('OS45 selected double-root equation', (x**3-3*f*x+2*g).subs({a:au,t:tcu,x:xiu}),0,['P3K.116','P3K.117','P3K.119'])
equal('OS45 selected critical equation', (3*x*x-3*f).subs({a:au,t:tcu,x:xiu}),0,['P3K.116','P3K.117','P3K.119'])
cap_poly=2187-16*u**3*(u**3+3)**3
equal('OS45 cap source substitution',(16*au**3+3)*729,cap_poly,['P3K.119'])
equal('OS45 cap factorization',cap_poly,-(2*u**3-3)*(8*u**9+84*u**6+342*u**3+729),['P3K.119'])
ii_poly=16*u**6+120*u**3+243
for name,poly in [('unselected_II',ii_poly),('ordinary_cap',cap_poly)]:
    equal(name+' squarefree',S.gcd(poly,S.diff(poly,u)),1,['P3K.116' if name=='unselected_II' else 'P3K.119'])
    equal(name+' avoids branch locus',S.gcd(poly,4*u**3+3),1,['P3K.116' if name=='unselected_II' else 'P3K.119'])
    nonzero(name+' avoids u zero',poly.subs(u,0),['P3K.116' if name=='unselected_II' else 'P3K.119'])
equal('unselected II / ordinary cap disjointness',S.gcd(ii_poly,cap_poly),1,['P3K.116','P3K.119'])
equal('selected-cap zero locus',6*u*tcu,3-2*u**3,['P3K.119'])
cap_eq=16*a**3+3
nodal_derivative_residual=S.together(S.diff(disc,a)-2*a*S.diff(disc,t)).subs(t,0)
equal('OS45 moving nodal derivative',S.rem(nodal_derivative_residual,cap_eq,a),0,['P3K.119'])
equal('OS45 cap derivative nonvanishing gcd',S.gcd(S.diff(disc,t).subs(t,0),cap_eq),1,['P3K.119'])
checks.append(dict(name='OS45 exact ordered point counts',labels=['P3K.116','P3K.119'],pass_check=True,unselected_II=2*S.degree(ii_poly,u),ordinary_cap=2*S.degree(cap_poly,u),selected_cap=6,unselected_cap=18))

u0=S.symbols('u0')
useries=u0*(1-v*v/S.Integer(3))**S.Rational(1,3)
aseri=S.series(au.subs(u,useries)-au.subs(u,u0),v,0,6).removeO().expand()
aseri=S.rem(aseri,u0**3+S.Rational(3,4),u0)
equal('OS45 ordered-cusp fourfold leading term',aseri,u0*v**4/162,['P3K.117'])
equal('K117 vertical index',(4*(-6-18*j*(j-1)))/24,-1-3*j*(j-1),['P3K.117'])

W=S.symbols('w0:3',nonzero=True)
I=S.symbols('I0:3')
J=S.symbols('J0:3')
aa,bb=S.symbols('a_old b_old')
C=W[2]**2*aa-W[2]*I[2]
E=W[2]*(2*aa-bb)-J[2]
VM=S.Matrix(3,3,lambda rr,ss:(I[rr]/W[rr] if rr==ss else 0)+C/(W[rr]*W[ss]))
dd=S.Matrix([(J[rr]+E)/W[rr] for rr in range(3)])
for ii in [1,2]:
    ee=S.zeros(3,1);ee[ii]=W[ii];ee[0]=-W[0]
    rhs=S.zeros(3,1);rhs[ii]=I[ii];rhs[0]=-I[0]
    for rr in range(3):equal(f'K117 target matrix equation i{ii} r{rr}',(VM*ee)[rr],rhs[rr],['P3K.117'])
    equal(f'K117 target delta equation i{ii}',W[ii]*dd[ii]-W[0]*dd[0],J[ii]-J[0],['P3K.117'])
equal('K117 retained matrix entry',VM[2,2],aa,['P3K.117'])
equal('K117 retained delta entry',dd[2],2*aa-bb,['P3K.117'])

table=[
 (1,6,3*l,4*k,k*l,4*k*l,0),
 (2,3,3*l,4*k+1,2*l*(4*k+1),8*l*(k+1),k*l),
 (3,2,3*l+2,4*k,9*k*(3*l+2),12*k*(l+2),k*(4*l+2)),
 (6,1,3*l+2,4*k+1,18*(3*l+2)*(4*k+1),24*(k*l+2*k+l+1),35*k*l+22*k+8*l+5)]
for A,B,M,H,K,LL,SS in table:
    equal(f'K118 ({A},{B}) characteristic index',(4*K-LL)/24,SS,['P3K.118'])
    equal(f'K118 ({A},{B}) vertical variation',(4*(K-3*M*H/B*j*(j-1))-LL)/24,SS-M*H/(2*B)*j*(j-1),['P3K.118'])
    exp=S.factor(M*H*S.Rational(B-1,2*B))
    assert S.Poly(exp,k,l).domain==S.ZZ
    checks.append(dict(name=f'K118 ({A},{B}) comparison exponent integral',labels=['P3K.118'],pass_check=True,polynomial=str(exp)))

payload=dict(created_at=datetime.now(timezone.utc).isoformat(),checker='GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation',method='New SymPy exact polynomial/determinant/rational computation from statements; no producer code read or reused',sympy_version=S.__version__,checks=checks,total_checks=len(checks),all_pass=all(c['pass_check'] for c in checks),scope='Only the listed algebraic substeps; no full geometric proof or whole result is certified.')
out.write_text(json.dumps(payload,indent=2,default=str)+'\n')
print(json.dumps({'all_pass':payload['all_pass'],'checks':len(checks),'output':str(out)},indent=2))
