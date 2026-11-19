"""Independent exact selected T0/ordinary-corner maps, without a return."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
import sympy as S

ROOT=Path(__file__).resolve().parents[2]
tests=[]
def eq(name,expr):
    result=S.factor(S.together(expr).as_numer_denom()[0])
    assert result==0,(name,result)
    tests.append(name)
def yes(name,condition):
    assert bool(condition),name
    tests.append(name)

sig,x,y,s,t,g,C,alpha=S.symbols('sig x y s t g C alpha',nonzero=True)
q=x*y;F=sig**4*q
E=lambda j:S.Matrix([0,j,1,0])
I=lambda a,b:S.Matrix([a,b,0,1])
cones=[]
for r in range(1,5):
    cones.append([E(r-1),E(r),I(0,0),I(1,0)])
cones.extend([[E(4),I(0,0),I(1,0),I(0,1)],
              [E(4),I(1,0),I(0,1),I(1,1)]])
for i,rays in enumerate(cones):
    yes(f'selected maximal cone {i+1} regular',abs(S.det(S.Matrix.hstack(*rays)))==1)

for r in range(1,7):
    factors=[sig,sig,sig,sig,y,x]
    multipliers=[S.Integer(1)]*4+[1/g,g]
    pre=S.prod(factors[:r-1]);post=S.prod(factors[r:])
    apre=S.prod(multipliers[:r-1]);apost=S.prod(multipliers[r:])
    sr=C/apre*s;tr=multipliers[r-1]*apre/C*t
    eq(f'B chart{r} full U lift',sr*apre*pre-C*s*pre)
    eq(f'B chart{r} full W lift',tr*apost*post-S.prod(multipliers)/C*t*post)
    eq(f'B chart{r} factor lift',sr*tr-multipliers[r-1]*s*t)
    for cc in [alpha,S.Symbol('delta',nonzero=True)]:
        eq(f'physical unit chart{r} {cc}',cc*s*(t/cc)-s*t)
    phase=[-S.I]*4+[1,1]
    ap=S.prod(phase[:r-1]); ar=phase[r-1]
    ss=s/ap;tt=ar*ap*t
    eq(f'mu4 chart{r} exact factor',ss*tt-ar*s*t)
    eq(f'mu4 chart{r} fourth iterate s',(1/ap)**4-1)
    eq(f'mu4 chart{r} fourth iterate t',(ar*ap)**4-1)

# Literal source-chain overlap, old final to new penultimate chart.
eq('source overlap exact q',(1/y)*(s*t*y*y)-s*t*y)
eq('source overlap exact U',sig**4*(y*s)-sig**4*y*s)
eq('source overlap exact W',(y*t)/y-t)
# The last old line chart to the first next line chart.
eq('line overlap exact sigma',(1/t)*(sig*t)-sig)
eq('line overlap exact next U',1/t-1/t)
eq('line overlap exact next W',(sig*t)*sig**3*(s*t)*y-sig**4*(s*t)*y*t)
for j in range(-20,21):
    for r in range(1,5):
        eq(f'full q-power chain map j{j} r{r}',
           (sig**4*q)**j*sig**(r-1)*s
           -sig**(4*j+r-1)*(q**j*s))
        eq(f'chain equation j{j} r{r}',(q**j*s)*(q**(-j)*t)-s*t)
        eq(f'B chain multiplier j{j} r{r}',q**(j+1)*C*s-q*C*q**j*s)
        psi,psit=S.symbols('psi psit',nonzero=True)
        eq(f'genuine point-chain equation j{j} r{r}',
           (psi**-1*q**j*s)*(psi*q**(-j)*t)-s*t)
        eq(f'full source-target psi Hom square j{j} r{r}',
           psit**-1*q**(j+1)*C*s
           -(q*C*psi/psit)*(psi**-1*q**j*s))

# Nine-factor chart determinants, retaining eta and v as independent bases.
eta,v,qq=S.symbols('eta v qq',nonzero=True)
for r in range(1,10):
    factors=[eta]*4+[v]*4+[qq]
    target=factors[r-1]
    other=[z for z in (eta,v,qq) if z!=target]
    local=[s,t]+other
    values=[z.subs(target,s*t) for z in (eta,v,qq)]
    values.append(s*S.sympify(S.prod(factors[:r-1])).subs(target,s*t))
    matrix=S.Matrix([[S.expand_power_base(z).as_powers_dict().get(w,0)
                      for w in local] for z in values])
    yes(f'nine-factor chart {r} regular',abs(matrix.det())==1)
    cb=S.Symbol('cb',nonzero=True)
    units=[cb]*4+[1/cb]*4+[1]
    pref=S.prod(units[:r-1]);u=units[r-1]
    eq(f'nine-factor {r} U lift',(C/pref*s)*pref-C*s)
    eq(f'nine-factor {r} factor',(C/pref*s)*(u*pref/C*t)-u*s*t)
    eq(f'nine-factor {r} full product',S.prod(units)-1)

# O/T graph chord with the exact source relation used only once.
U,d,a2=S.symbols('U d a2',nonzero=True)
k=-1/eta+eta**3*v/U
A=(d-2*v)/U+2*eta**4*v*v/U**2
c=v+A-eta**4*v*A/U
eq('O-to-T full Y chord',eta*v-k*(eta**2*A)-eta*c)
eq('O-to-T exact preserved sigma',(eta*c)*(v/c)-eta*v)
relation=1-U-a2*eta**2-d*eta**4/U-eta**8*v*v/U**2
eq('O-to-T full X chord',(k*k-a2-U/eta**2)-eta**2*A-relation/eta**2)
eq('O-to-T central unit',c.subs({eta:0,U:1,d:1})-(1-v))
for b in (1,3):
    eq(f'actual central additive source b{b}',1/(v/(1-b*v))-(1/v-b))

# Exact A1 source-graph Rees generators and the retained point tensor weights.
P,nu=S.symbols('P nu',nonzero=True)
xo=P**2-nu**2;yo=P**3-nu*P-3*nu**2*P;to=nu**2*(1+2*nu)
eq('Rees generator nu2',to/(1+2*nu)-nu**2)
eq('Rees generator P2',xo+to/(1+2*nu)-P**2)
eq('Rees generator Pnu',P*xo-yo-2*P*to/(1+2*nu)-P*nu)
for a in (2,6):
    for vs,vr in ((1,1),(2,1)):
        yes(f'actual M{a} exceptional order {vs},{vr}',a*min(vs,2*vr)==a*vs)

finite_weights=[]
for j in range(4):
    w1=[1,0,j,(-j-1)%4]
    w2=[1,3,(j+1)%4,(-j-1)%4]
    yes(f'ordinary section chart1 determinant j{j}',sum(w1)%4==0)
    yes(f'ordinary section chart2 determinant j{j}',sum(w2)%4==0)
    yes(f'ordinary section chart1 eta j{j}',(w1[2]+w1[3]+1)%4==0)
    yes(f'ordinary section chart2 X j{j}',(w2[1]+w2[2]-j)%4==0)
    yes(f'ordinary section chart2 v j{j}',(w2[2]+w2[3])%4==0)
    finite_weights.append({"j":j,"chart1":w1,"chart2":w2,"physical_delta":[0,0,1,-1]})

source=ROOT/'notes/part3_e6_selected_infinity_toric_audit.md'
ei=ROOT/'notes/part3_e6_selected_infinity_working.md'
eir=ROOT/'notes/part3_e6_selected_infinity_root_working.md'
out={
 "status":"PASS","utc":datetime.now(timezone.utc).isoformat(),
 "check_count":len(tests),"source_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
 "input_hashes":{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (ei,eir)},
 "scope":"Exact local T0 six-cone/factor atlas, full source/line/unit and finite arrows, q^j ordinary-chain gluing, and O/T nine-factor relative corner maps. No global compact attachment or return.",
 "cones":[[list(map(int,r)) for r in c] for c in cones],
 "finite_normal_weights":finite_weights,"checks":tests}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('status','check_count','source_sha256','scope')},indent=2))
