"""Independent replay, quotient-ring and marked-volume audit of all 52 charts."""
from pathlib import Path
from fractions import Fraction
from itertools import product,combinations
from collections import Counter
from datetime import datetime,timezone
from math import gcd,floor,ceil
import hashlib,json
import sympy as s

ROOT=Path(__file__).resolve().parents[2]
IN=ROOT/'code/part3_root/e6_selected_infinity_mu4_fan.json'
data=json.loads(IN.read_text())
tests=[]
def yes(name,p):
    assert bool(p),name
    tests.append(name)
def eq(name,p):
    num=s.factor(s.together(p).as_numer_denom()[0])
    assert num==0,(name,num)
    tests.append(name)
def mat(r):
    return s.Matrix.hstack(*[s.Matrix(v) for v in r])
def key(r):
    return tuple(sorted(tuple(v) for v in r))
def shift(v,k):
    return tuple(s.Matrix(data['B_cocharacter_matrix'])**k*s.Matrix(v))
def primitive(v):
    return gcd(*[abs(int(a)) for a in v])==1

# Actual quotient torus, including the primitive physical cocharacter.
K=s.Matrix(data['cover_to_quotient_character_matrix'])
Q=s.Matrix([[s.Rational(*a) for a in row] for row in data['quotient_cocharacter_basis_in_cover']])
yes('character and cocharacter matrices are inverse',K*Q==s.eye(4))
S=s.Matrix(data['B_cocharacter_matrix'])
yes('actual B integral automorphism',S.det()==1)
yes('B fixes physical delta',S*s.Matrix([0,0,0,1])==s.Matrix([0,0,0,1]))
for pk,p in data['parents'].items():
    P=mat(p['rays'])
    yes(f'{pk} actual quotient index',abs(P.det())==4)
    w=s.Matrix(p['mu4_weights'])
    residue=4*P.inv()*s.Matrix([1,0,0,0])-w
    yes(f'{pk} actual cover weights',all(a.q==1 and int(a)%4==0 for a in residue))
    expected={u for u in product(range(5),repeat=4)
              if 1<=sum(u)<=4 and sum(a*b for a,b in zip(u,p['mu4_weights']))%4==0}
    yes(f'{pk} complete degree-four invariant list',
        expected==set(tuple(u) for u in p['invariant_monomial_generators']))

# Replay every simultaneous star from the raw eight cones, without using
# the parent's residue selector or its mutation loop.
fan={key(p['rays']):{'rays':tuple(map(tuple,p['rays'])),'parent':pk}
     for pk,p in data['parents'].items()}
inserted=[]
for hidx,h in enumerate(data['stellar_history']):
    ray=tuple(h['ray'])
    yes(f'star{hidx} primitive actual lattice point',primitive(ray))
    width=-ray[0]+4*ray[1]+4*ray[2]
    yes(f'star{hidx} positive period width',width>0)
    lifts=[shift(ray,k) for k in range(ceil(Fraction(-ray[3],width)),
                                     floor(Fraction(width-ray[3],width))+1)]
    yes(f'star{hidx} all period images',lifts==list(map(tuple,h['period_images'])))
    nextfan={};removed=added=0
    for ck,c in fan.items():
        P=mat(c['rays']);inv=P.inv()
        centres=[]
        for r in lifts:
            a=inv*s.Matrix(r)
            if all(v>=0 for v in a) and sum(bool(v>0) for v in a)>1:
                centres.append((r,a))
        yes(f'star{hidx} cone{ck} orbit separation',len(centres)<=1)
        if not centres:
            nextfan[ck]=c
            continue
        removed+=1
        r,a=centres[0]
        yes(f'star{hidx} strict coefficient decrease {ck}',all(0<=v<1 for v in a))
        for i,val in enumerate(a):
            if val==0:continue
            child=list(c['rays']);child[i]=r
            C=mat(child)
            yes(f'star{hidx} child volume {ck}:{i}',
                abs(C.det())==val*abs(P.det()) and 0<abs(C.det())<abs(P.det()))
            nk=key(child)
            yes(f'star{hidx} distinct child {nk}',nk not in nextfan)
            nextfan[nk]={'rays':tuple(child),'parent':c['parent']}
            added+=1
    yes(f'star{hidx} exact removed count',removed==h['removed'])
    yes(f'star{hidx} exact added count',added==h['added'])
    fan=nextfan;inserted+=lifts
yes('complete replay matches all 52 charts',set(fan)==set(key(c['rays']) for c in data['cones']))
yes('all14 stars and52 cones',len(data['stellar_history'])==14 and len(fan)==52)

# Every local and periodic facet, with actual strip boundary equations.
facets=Counter(tuple(sorted(f)) for c in fan.values() for f in combinations(c['rays'],3))
boundary_rows=[(1,0,0,0),(-1,4,0,0),(0,0,1,0),(0,0,0,1),(-1,4,4,-1)]
for f,count in facets.items():
    yes(f'facet multiplicity {f}',count in (1,2))
    if count==1:
        yes(f'no missing interior facet {f}',
            any(all(sum(a*b for a,b in zip(row,r))==0 for r in f) for row in boundary_rows))
lower={f for f in facets if all(r[3]==0 for r in f)}
upper={f for f in facets if all(-r[0]+4*r[1]+4*r[2]-r[3]==0 for r in f)}
yes('all four period facets exactly paired',
    {tuple(sorted(shift(r,1) for r in f)) for f in lower}==upper and len(lower)==4)

for cidx,c in enumerate(data['cones']):
    N=mat(c['rays']);P=mat(data['parents'][c['parent']]['rays'])
    yes(f'cone{cidx} smooth in actual quotient lattice',N.det()==1)
    yes(f'cone{cidx} primitive rays',all(primitive(r) for r in c['rays']))
    A=P.inv()*N
    yes(f'cone{cidx} in actual parent',all(a>=0 for a in A))
    gens=data['parents'][c['parent']]['invariant_monomial_generators']
    for gi,(g,recorded) in enumerate(zip(gens,c['quotient_invariant_monomial_matrix'])):
        exponent=s.Matrix([g])*A
        yes(f'cone{cidx} invariant{gi} full arrow',
            list(exponent)==recorded and all(a.q==1 and a>=0 for a in exponent))
    physical=N.inv()*s.Matrix([0,0,0,1])
    yes(f'cone{cidx} full primitive physical weights',
        list(physical)==c['physical_weights'] and gcd(*map(abs,map(int,physical)))==1)
    for label,row,field in [
        ('epsilon',[0,1,1,0],'epsilon_exponents'),
        ('qnew',[1,0,0,0],'q_new_exponents'),
        ('sigma4',[-1,4,4,0],'sigma_fourth_exponents')]:
        ex=s.Matrix([row])*N
        yes(f'cone{cidx} actual {label}',list(ex)==c[field] and all(a>=0 for a in ex))
    local=list(s.Matrix([[0,1,1,0]])*N-s.ones(1,4))
    old=list(s.Matrix([[-1,5,4,0]])*N-s.ones(1,4))
    delta=list(s.Matrix([[-1,4,3,0]])*N)
    yes(f'cone{cidx} local divisor',local==c['canonical_orders'])
    yes(f'cone{cidx} marked-family divisor',old==c['original_marked_family_volume_orders'])
    yes(f'cone{cidx} full frame monomial',delta==c['original_to_local_frame_exponents'] and old==[x+y for x,y in zip(local,delta)])
    target=S*N
    yes(f'cone{cidx} actual B target',target==mat(c['B_target_rays']))
    su=s.Matrix(c['B_source_unit_exponents']);hu=s.Matrix(c['B_full_Hom_unit_exponents'])
    yes(f'cone{cidx} full source-unit reconstruction',target*su==s.Matrix([0,1,-1,0]))
    yes(f'cone{cidx} full Hom-unit reconstruction',target*hu==s.Matrix([0,0,0,1]))
    yes(f'cone{cidx} B monomial square',target.inv()*S*N==s.eye(4))

# Full original volume wedge, with its actual varying base unit.
chi,sig,X,Y=s.symbols('chi sig X Y',nonzero=True)
e=chi*sig;d=1-3*e**2
xo=sig**2*X/d**2;to=sig**4/d**3;yo=sig**3*Y/d**3
J=s.Matrix([xo,to,e]).jacobian([chi,X,sig]).det()
eq('positive eight in exact original wedge',J/yo-8*sig**3/d**2/(2*Y))

# Exact O-unit and primitive O/T source derivative square.
eta,v,U,dd,a2=s.symbols('eta v U dd a2',nonzero=True)
F=1-U-a2*eta**2-dd*eta**4/U-eta**8*v*v/U**2
Du=-(eta*s.diff(F,eta)-v*s.diff(F,v))/s.diff(F,U)
uO=U**2/(U**3-dd*U*eta**4-2*eta**8*v*v)
a2eq=(1-U-dd*eta**4/U-eta**8*v*v/U**2)/eta**2
eq('exact O differential unit',
   (1-Du/(2*U)-uO).subs(a2,a2eq))
AA=(dd-2*v)/U+2*eta**4*v*v/U**2
cb=v+AA-eta**4*v*AA/U
Dcb=eta*s.diff(cb,eta)-v*s.diff(cb,v)+s.diff(cb,U)*Du
uT=1/(dd+2*a2*eta**2*AA+3*eta**4*AA**2)
eq('complete primitive chord Jacobian-unit identity',
   (uO-uT*(cb+Dcb)).subs(a2,a2eq))
us,ut,c,jac=s.symbols('us ut c jac',nonzero=True)
eq('full marked determinant-frame reset',
   ((eta*c)**4*(v/c)**3*ut*jac-eta**4*v**3*us).subs(us,ut*c*jac))
yes('actual marked character retained',data['original_marked_family_canonical_character']==[-1,5,4,0])

note=ROOT/'notes/part3_e6_selected_infinity_mu4_root_working.md'
out={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),
     'input_json_sha256':hashlib.sha256(IN.read_bytes()).hexdigest(),
     'input_note_sha256':hashlib.sha256(note.read_bytes()).hexdigest(),
     'check_count':len(tests),'regular_cones':len(fan),'stellar_steps':len(data['stellar_history']),
     'paired_period_facets':len(lower),
     'scope':'All52 actual quotient charts; independently replayed simultaneous stars, complete boundary/period facets, invariant-ring generators and monomial arrows, original marked-volume character and full primitive source derivative/unit square. No compact global count or Spin assumption.',
     'checks':tests}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('status','input_json_sha256','input_note_sha256','check_count','regular_cones','stellar_steps','paired_period_facets','scope')},indent=2))
