"""Fresh exact audit code, written from the printed formulas, 19 Nov 2026.

No earlier S6 verification program is read, imported, or executed here.
The fan update is solved from its linear prism equations by rational Gaussian
elimination, then compared with the displayed closed reconstruction formula.
This certifies those algebraic consequences, not their geometric derivation.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from math import gcd
import json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

HERE = Path(__file__).resolve().parent
checks = []
def check(name, value, expected=True):
    if value != expected:
        raise AssertionError((name, value, expected))
    checks.append(name)

def mul(a,b):
    return [[sum(F(x)*F(y) for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def inv2(a):
    d=a[0][0]*a[1][1]-a[0][1]*a[1][0]
    check('unimodular matrix',abs(d),1)
    return [[F(a[1][1],d),F(-a[0][1],d)],[F(-a[1][0],d),F(a[0][0],d)]]
def flat(a): return [x for row in a for x in row]
def add(a,b): return [x+y for x,y in zip(a,b)]
def scale(c,a): return [c*x for x in a]
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def solve_linear(equations, rhs, count):
    """Rational row reduction, including consistency and uniqueness checks."""
    m=[[F(x) for x in row]+[F(y)] for row,y in zip(equations,rhs)]
    pivots=[];r=0
    for c in range(count):
        p=next((i for i in range(r,len(m)) if m[i][c]),None)
        if p is None:continue
        m[r],m[p]=m[p],m[r]
        z=m[r][c];m[r]=[v/z for v in m[r]]
        for i in range(len(m)):
            if i!=r and m[i][c]:
                q=m[i][c];m[i]=[u-q*v for u,v in zip(m[i],m[r])]
        pivots.append(c);r+=1
    check('consistent prism system',all(any(row[:count]) or row[-1]==0 for row in m))
    check('unique prism solution',len(pivots),count)
    result=[F(0)]*count
    for i,c in enumerate(pivots):result[c]=m[i][-1]
    return result

# All 33 correction statements: exact arithmetic and the explicit dual pairing.
H,chi,j,k,l,p,n=sp.symbols('H chi j k l p n', integer=True)
check('physical reference index',sp.simplify((4*3*H-24*chi)/24-(H/2-chi)),0)
check('fixed edge factor seven',sp.simplify(H/2-chi+3*H-6*chi-7*(H/2-chi)),0)
check('weighted OS47 physical class',F(-72-12*(-14),24),4)
check('primitive profile classes',[d//2-1 for d in [8,14,20,30]],[3,6,9,14])
check('primitive profile flops',[7*(d//2-1)%28 for d in [8,14,20,30]],[21,14,7,14])
check('positive OS45 covers',sorted({3*r%28 for r in range(1,29)}),list(range(28)))
check('reduced III covers',sorted({(3*r+2)%28 for r in range(28)}),list(range(28)))
L=sp.Matrix([[-1,2,2],[0,1,0],[0,0,1]])
D=sp.Matrix([[-1,0,0],[2,1,0],[2,0,1]])
check('exterior basis pairing',L*D.T,sp.eye(3))
check('historical vertical fan transport',sp.expand((-j)*(-j-1)-j*(j+1)),0)
check('selected-cusp vertical image',sorted({(-1-3*r*(r-1))%28 for r in range(28)}),[5,7,9,13,19,21,23,27])
check('selected-cusp full period certificate',sp.expand((-1-3*(j+28)*(j+27))-(-1-3*j*(j-1))+28*(6*j+81)),0)
seq=lambda q:(-7-24*q*(q+1))%28
check('mutation exact image',sorted({seq(q) for q in range(7)}),[1,13,17,21])
check('mutation least period',next(h for h in range(1,29) if all(seq(q+h)==seq(q) for q in range(28))),7)
for a in [1,2]:
    for scalar in range(28):
        for mult in range(28):
            values=[(x,y) for x in range(28) for y in range(28)
                    if (y-x-a)%28==0 and (x+y-a-2*mult*scalar)%28==0]
            expected=sorted({((mult*scalar+14*e)%28,(a+mult*scalar+14*e)%28) for e in [0,1]})
            check('source-zero two equations',values,expected)

# Integral normalization and nearby monodromy, recomputed as exterior powers.
C0=sp.Matrix([[1,-1,1],[-1,1,-1]])
C2=sp.Matrix([[-1,1,-1,1],[1,-1,1,-1],[-1,1,-1,1]])
check('normalization C0 Smith diagonal',smith_normal_form(C0,domain=ZZ),sp.Matrix([[1,0,0],[0,0,0]]))
check('normalization C2 rank',C2.rank(),1)
check('normalization C2 primitive image',abs(smith_normal_form(C2,domain=ZZ)[0,0]),1)
rays=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
for i,r in enumerate(rays):
    prev,nxt=rays[(i-1)%6],rays[(i+1)%6]
    check('toric smooth adjacency',r[0]*nxt[1]-r[1]*nxt[0],1)
    check('toric self intersection',tuple(x+y for x,y in zip(prev,nxt)),r)
# Coefficients of divisor with a0=a1=0, and opposite-curve restrictions.
aa=sp.Matrix([0,0,*sp.symbols('a2:6')])
degrees=[aa[(i-1)%6]+aa[(i+1)%6]-aa[i] for i in range(6)]
opposites=[sp.expand(degrees[i]-degrees[i+3]) for i in range(3)]
check('full restriction matrix',sp.Matrix([[v.coeff(a) for a in aa[2:]] for v in opposites]),C2)
# Ordered basis a1,b1,a2,b2; pullback b_i -> b_i+a_i.
T=sp.Matrix([[1,1,0,0],[0,1,0,0],[0,0,1,1],[0,0,0,1]])
invariant_ranks=[];invariant_checks=[]
for degree in range(5):
    inds=list(combinations(range(4),degree))
    E=sp.Matrix([[T.extract(i,j).det() for j in inds] for i in inds])
    A=E-sp.eye(len(inds));rank=len(inds)-A.rank()
    invariant_ranks.append(rank)
    sn=smith_normal_form(A,domain=ZZ)
    # Every nonzero invariant factor of T-I is 1 in this local model.
    check('nearby monodromy saturated constraints',all(abs(sn[i,i]) in [0,1] for i in range(min(sn.shape))))
    invariant_checks.append({'degree':degree,'basis':inds,'T':str(E),'rank':rank})
check('nearby invariant ranks',invariant_ranks,[1,2,4,2,1])
u1,u2,v1,v2=sp.symbols('u1 u2 v1 v2',integer=True)
phi=lambda x,y:x*y
check('cross line cocycle',sp.expand(phi(u1,u2)+phi(v1,v2)+u1*v2+u2*v1-phi(u1+v1,u2+v2)),0)
check('normalization total ranks',[1,3-C0.rank(),(4-C2.rank())+(2-C0.rank()),3-C2.rank(),1],[1,2,4,2,1])

# K108 actual algebraic source and cap arrows, independent symbolic substitutions.
s,t,x,y,r,v,z=sp.symbols('s t x y r v z')
disc=sp.discriminant(x**3+r*x**2+t*x+t**2,x)
check('original source discriminant',sp.factor(disc+t*t*(4*r**3-r**2-18*r*t+27*t**2+4*t)),0)
quad=27*t**2+(18*s-sp.Rational(1,2))*t-4*s*(sp.Rational(1,4)-s)**2
tc=(1-36*s-(1+12*s)**sp.Rational(3,2))/108
to=(1-36*s+(1+12*s)**sp.Rational(3,2))/108
check('selected root polynomial',sp.simplify(quad.subs(t,tc)),0)
check('other root polynomial',sp.simplify(quad.subs(t,to)),0)
sv=v*(v+4)/(4*(v-2)**2); tv=v/(v-2)**3
check('full rational selected height',sp.factor(quad.subs({s:sv,t:tv})),0)
check('source coordinate local degree',sp.diff(sv,v).subs(v,0),sp.Rational(1,4))
X,Y=sp.symbols('X Y')
for cap_l in range(9):
    m=3*cap_l+2;kcap=2*cap_l+1
    eq=y*y-x**3-r*x*x-t*x-t*t
    pulled=sp.expand(eq.subs({t:z**(-m),x:z**(-2*(cap_l+1))*X,y:z**(-3*(cap_l+1))*Y})*z**(6*(cap_l+1)))
    expected=Y*Y-X**3-r*z**(2*cap_l+2)*X*X-z**(cap_l+2)*X-z*z
    check('actual root-source substitution',sp.expand(pulled-expected),0)
    check('deck exponent identity l-2k',cap_l-2*kcap,-m)
    check('deck exponent identity 3k',3*kcap,2*m-1)
    for norm in [-1,1]:
        C=sp.Matrix([[m,1],[norm,0]])
        Ci=sp.Matrix([[0,norm],[1,-m*norm]])
        transport=sp.Matrix([[norm,0],[2-m*norm,1]])
        check('signed cap inverse',C*Ci,sp.eye(2))
        check('signed cap target morphism',C*transport,sp.Matrix([[2,1],[1,0]]))
a,b=sp.symbols('a b')
for XX,U,V in [(a*b,a*a*b,a*b*b),(a*b,a,a*a*b**3),(a*b,a*a*b**3,a)]:
    check('resolved A2 chart',sp.expand(U*V-XX**3),0)
# Entire formal doubling coefficient: compute G+G, then +G, then double anew.
s,q=sp.symbols('s q');r=sp.Rational(1,4)-s;t=1/q
def plus(P,Q):
    x1,y1=P;x2,y2=Q
    slope=(3*x1*x1+2*r*x1+t)/(2*y1) if P==Q else (y2-y1)/(x2-x1)
    xx=sp.cancel(slope*slope-r-x1-x2)
    yy=sp.cancel(-y1+slope*(x1-xx))
    return xx,yy
G=(sp.Integer(0),t)
G2=plus(G,G);G3=plus(G2,G);G6=plus(G3,G3)
L=sp.cancel(-G6[0]/(q*G6[1]));unit=sp.cancel(L/s)
num,den=sp.fraction(unit)
check('formal sixfold point leading unit',unit.subs({s:0,q:0}),-1)
check('formal sixfold point initial q value',sp.cancel(L.subs(q,0)),-s)
check('formal sixfold point numerator nonzero',num.subs({s:0,q:0})!=0)
check('formal sixfold point denominator nonzero',den.subs({s:0,q:0})!=0)
# Initial/root normalization retains the entire rational function in output.
formal={'L_over_s_numerator':str(num),'L_over_s_denominator':str(den),
        'value_at_origin':str(unit.subs({s:0,q:0}))}
# Full middle-chart +G x-coordinate, reduced by the actual c-square equation.
a,b,B,C,c=sp.symbols('a b B C c')
z= a*b*(b-a)/(2*c);X=a*b;Y=a*b*(a+b)/2
K=1+b*(b-a)*(B+C*a*b)/(2*c*(c+1))
FF=1-a*b*(B+C*a*b)*(K+1)/(2*c*(c+1))-C*a*b*b*(a-b)/(4*c*c)
slope=(Y-z)/X
chord_x=slope*slope-C*z*z-X
residual=sp.fraction(sp.cancel(chord_x-a*(a-b)*FF))[0]
relation=c*c-(1+B*a*b+C*a*a*b*b)
check('complete +G middle chart x arrow',sp.rem(residual,relation,c),0)
# Reflection acts on actual periodic fans through the stated identical-fan maps.
j=sp.symbols('j',integer=True)
J=sp.diag(-1,1);Tj=sp.Matrix([[1,0],[j,1]])
R0=sp.Matrix([[-1,-1],[1,0]]);swap=sp.Matrix([[0,1],[1,0]])
check('signed reflection exact fan adapter',-J*Tj*(R0**2)*swap,sp.Matrix([[1,0],[1-j,1]]))
kj=47-2*j**3+18*j**2-52*j
Sj=8-j*(j*j-9*j+26)/3
check('K108 characteristic/index identity',sp.expand((4*kj+4)/24-Sj),0)
for jj in range(-100,101):
    check('K108 signed polynomial integral',F(jj*(jj*jj-9*jj+26),3).denominator,1)

# Fan recurrence solved from prism constraints, with complete exact witness words.
Q=[[[1,-1],[0,1]],[[1,0],[-1,1]]]
symidx={(0,0):0,(0,1):1,(0,2):2,(1,1):3,(1,2):4,(2,2):5}
def seed(kind,n=0):
    if kind=='K106':
        S=F(8)-F(n*(n*n-9*n+26),3);I0=4*n*n-24*n+34
        V=[[-12*S,-I0,I0],[-I0,2*n-8,0],[I0,0,2*n-6]]
        delta=[12*S,4*n*n-26*n+40,-4*n*n+22*n-30]
        mat=[[4,-2],[12,-6]];tt=-1;denom=4
    elif kind=='K71':
        S=-1-3*n*(n-1)
        V=[[18*n*(n-1),6-12*n,12*n-6],[6-12*n,0,0],[12*n-6,0,0]]
        delta=[-12-18*n*(n-1),12*n-12,-12*n]
        mat=[[-6,0],[0,0]];tt=-3;denom=2
    elif kind in ['K73_original','K73_OS45']:
        J,H,chi=(2,F(1,3),F(1,6)) if kind=='K73_original' else (1,F(8),F(1))
        S=H/2-chi-F(J*n*(n-1),2)
        V=[[2*J-6*H+6*J*n*(n-1),2*J*(1-2*n),2*J*(2*n-1)],
           [2*J*(1-2*n),2*J,0],[2*J*(2*n-1),0,2*J]]
        delta=[2*J+6*H-24*chi-6*J*n*(n-1),2*J*(2*n-1),2*J*(1-2*n)]
        mat=[[0,0],[0,2*J]];tt=J;denom=4
    elif kind=='K77':
        S=-(n-1)**2
        V=[[12*(n-1)**2,8*(1-n),8*(n-1)],[8*(1-n),4,0],[8*(n-1),0,4]]
        delta=[-12*(n-1)**2,8*(n-1),8*(1-n)]
        mat=[[0,0],[-2,4]];tt=2;denom=4
    return {'P':[[F(1),F(0)],[F(n),F(1)]],'V':[[F(x) for x in row] for row in V],
            'delta':list(map(F,delta)),'S':F(S),'B0':mat,'t':F(tt),'denom':denom,
            'word':'','steps':[]}
def step(state,edge):
    P=mul(state['P'],Q[edge]);R=inv2(P);w=[R[0][1],R[1][1],-R[0][1]-R[1][1]]
    check('nonzero canonical target weights',all(w))
    x,y=w[:2];d=[-x-2*y,-2*x-y,x-y]
    M=mul(mul(R,state['B0']),P);ll=[M[1][1]-M[1][0],M[0][0]-M[0][1],M[1][1]]
    tt=state['t'];I=[tt*ww+dd*(lll-tt) for ww,dd,lll in zip(w,d,ll)]
    W=[tt*ww-dd*(lll-tt) for ww,dd,lll in zip(w,d,ll)]
    aa=state['V'][edge][edge];bb=state['delta'][edge]
    eq=[];rr=[]
    for vj in [1,2]:
        vec=[F(0)]*3;vec[0]=-w[0];vec[vj]=w[vj]
        for row in range(3):
            co=[F(0)]*6
            for col in range(3):co[symidx[tuple(sorted((row,col)))]]+=vec[col]
            eq.append(co);rr.append((I[vj] if row==vj else 0)-(I[0] if row==0 else 0))
    eq.append([0,0,0,0,0,1]);rr.append(aa)
    vs=solve_linear(eq,rr,6)
    V=[[vs[symidx[tuple(sorted((r,c)))]] for c in range(3)] for r in range(3)]
    deq=[[-w[0],w[1],0],[-w[0],0,w[2]],[0,0,1]]
    delta=solve_linear(deq,[W[1]-W[0],W[2]-W[0],2*aa-bb],3)
    cc=w[2]*w[2]*aa-w[2]*I[2];ee=w[2]*(2*aa-bb)-W[2]
    formula=[[ (I[r]/w[r] if r==c else 0)+cc/(w[r]*w[c]) for c in range(3)] for r in range(3)]
    check('linear solve versus printed variation formula',V,formula)
    check('linear solve versus printed derivative formula',delta,[(u+ee)/ww for u,ww in zip(W,w)])
    increment=(bb-aa)/state['denom']
    check('integral target invariants',all(v.denominator==1 for v in flat(V)+delta+[increment]))
    record={'edge':edge,'P':P,'native_increment':increment,'V':V,'delta':delta,
            'B':M,'weights':w,'I':I,'W':W}
    return {**state,'P':P,'V':V,'delta':delta,'S':state['S']+increment,
            'word':state['word']+str(edge),'steps':state['steps']+[record]}

witnesses={};example_checks={}
for kind in ['K106','K71','K73_original','K73_OS45','K77']:
    initial=seed(kind);seen={int(initial['S'])%28:initial};states=[initial]
    # Canonical nonvertical words start with Q0; further Q0,Q1 are allowed.
    for depth in range(1,9):
        nextstates=[]
        for st in states:
            for edge in ([0] if depth==1 else [0,1]):
                ns=step(st,edge);nextstates.append(ns)
                seen.setdefault(int(ns['S'])%28,ns)
        states=nextstates
        if kind=='K106' and depth==7:check('K106 all classes by depth seven',sorted(seen),list(range(28)))
    witnesses[kind]=seen
    spec=step(step(initial,0),1)
    example_checks[kind]={'residue':int(spec['S'])%28,'integer':spec['S'],
                          'increments':[r['native_increment'] for r in spec['steps']]}
check('K106 two-flop example',example_checks['K106']['increments'],[48,300])
check('K106 two-flop return',example_checks['K106']['integer'],356)
check('K71 two-flop return',example_checks['K71']['residue'],1)
check('K73 OS45 two-flop return',example_checks['K73_OS45']['residue'],11)
check('K77 two-flop return',example_checks['K77']['residue'],7)
check('original K73 first repeated flop return',int(step(step(seed('K73_original'),0),0)['S'])%28,3)
for kind in ['K73_original','K77']:check('actual all-fan witness coverage '+kind,sorted(witnesses[kind]),list(range(28)))
check('K71 witnessed image',sorted(witnesses['K71']),list(range(1,28,2)))

# Exact closed-form images: every primitive residue vector mod112 lifts to a
# primitive integer pair (fix one coordinate and avoid its remaining primes).
# The two output polynomials are unchanged modulo28 under S -> S+112.
images={100:set(),107:set()};primitive_moduli=0
S=sp.symbols('S',integer=True)
f100=-4+sp.Rational(3,2)*(S-1)-sp.Rational(27,8)*(S*S-1)
f107=-sp.Rational(3,8)*(S-1)*(S-3)
for pol in [f100,f107]:
    delta=sp.Poly(sp.expand((pol.subs(S,S+112)-pol)/28),S)
    check('closed fan formula period112',all(a.q==1 for a in delta.all_coeffs()))
for xx in range(112):
    for yy in range(112):
        if gcd(gcd(xx,yy),112)!=1:continue
        primitive_moduli+=1;ss=xx*xx+xx*yy+yy*yy
        a100=-4+F(3*(ss-1),2)-F(27*(ss*ss-1),8)
        a107=-F(3*(ss-1)*(ss-3),8)
        check('primitive norm formula integrality',a100.denominator==a107.denominator==1)
        images[100].add(int(a100)%28);images[107].add(int(a107)%28)
expected=[0,3,4,5,7,10,11,12,14,17,18,19,21,24,25,26]
for label in images:check('K'+str(label)+' complete primitive image',sorted(images[label]),expected)

def serialize(x):
    if isinstance(x,F):return int(x) if x.denominator==1 else str(x)
    if isinstance(x,sp.Basic):return str(x)
    if isinstance(x,set):return sorted(x)
    raise TypeError(type(x).__name__)
result={'scope':'Exact algebra, integral lattices, complete primitive residue images, and actual finite fan-word witnesses. The geometry of the input maps is audited separately.',
        'checks_passed':len(checks),'normalization_invariant_ranks':invariant_ranks,
        'monodromy_details':invariant_checks,'formal_sixfold_point':formal,
        'fan_examples':example_checks,'fan_witnesses':witnesses,
        'primitive_residue_vectors_mod112':primitive_moduli,'closed_images':images,
        'check_names':checks}
(HERE/'independent_IV_checks.json').write_text(json.dumps(result,default=serialize,indent=2)+'\n')
lines=['# Fresh actual fan-word witnesses','',
       'Computed by solving the integral prism equations over the rationals, then comparing the printed reconstruction formulas. No prior code was imported.','',
       '| Residue | K106 word from T0 | Integer sum | Basis |','|---:|---|---:|---|']
for residue,st in sorted(witnesses['K106'].items()):
    lines.append(f"| {residue} | {st['word'] or 'empty'} | {st['S']} | {st['P']} |")
(HERE/'independent_K106_witnesses.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({'checks_passed':len(checks),'rank_two_ranks':invariant_ranks,
                  'fan_images':{k:sorted(v) for k,v in witnesses.items()},
                  'examples':example_checks,'primitive_mod112':primitive_moduli,
                  'closed_images':images},default=serialize,indent=2))
