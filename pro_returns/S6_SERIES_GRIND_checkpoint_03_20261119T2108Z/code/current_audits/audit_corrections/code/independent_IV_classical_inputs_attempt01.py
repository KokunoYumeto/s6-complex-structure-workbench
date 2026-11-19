"""Fresh low-F computations; no supplied program or saved certificate is imported.

The permutation search enumerates involutions against a canonical order-three
permutation. SymPy then verifies the independently produced tuples. This file
checks finite mathematical inputs, not the cited classification theorems or the
geometric existence and orientation maps in the paper.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations,product
import json,time,hashlib
import sympy as S
from sympy.combinatorics import Permutation,PermutationGroup

start=time.monotonic(); assertions=0; checks=[]
def check(name,condition):
    global assertions
    assertions+=1
    if not condition: raise AssertionError(name)
    checks.append(name)

def fibre(name):
    records={'III*':(9,0,0,0,1),'IV*':(8,0,1,0,0),
             'I3*':(9,3,0,0,0),'I1*':(7,1,0,0,0),
             'III':(3,0,0,0,1),'IV':(4,0,0,1,0),'II':(2,0,1,0,0)}
    if name in records:return records[name]
    n=int(name[1:]);return(n,n,0,0,0)

root_choices={43:[['III*']],45:[['I8']],46:[['I3*']],
 47:[['I7'],['I2','III']],49:[['IV*'],['I2','III']],
 50:[['I1*'],['I3','IV']],55:[['I5'],['I4']],
 56:[['I5'],['I3','IV'],['I2','III']]}
configs=[]
for row,choices in root_choices.items():
    for red in product(*choices):
        missing=12-sum(fibre(x)[0] for x in red)
        for nII in range(missing//2+1):
            names=list(red)+['I1']*(missing-2*nII)+['II']*nII
            data=[fibre(x) for x in names]
            d=sum(x[1] for x in data);a0=sum(x[2] for x in data)
            b0=sum(x[3] for x in data);a1=sum(x[4] for x in data)
            check('profiles_integral_'+str(row)+'_'+'_'.join(names),
                  (d-a0-2*b0)%3==0 and (d-a1)%2==0)
            p0=[1]*a0+[2]*b0+[3]*((d-a0-2*b0)//3)
            p1=[1]*a1+[2]*((d-a1)//2)
            pinf=[x[1] for x in data if x[1]>0]
            x=2*d-2-sum(d-len(p) for p in (p0,p1,pinf))
            configs.append(dict(row=row,fibres=names,degree=d,
                                profile0=p0,profile1=p1,profile_infinity=pinf,excess=x))
check('twenty_four_Euler_candidates',len(configs)==24)
excluded={tuple(q['fibres']) for q in configs if q['excess']<0}
check('exact_three_Riemann_Hurwitz_exclusions',excluded=={
 ('I8','II','II'),('I7','III','II'),('I5','IV','III')})
valid=[q for q in configs if q['excess']>=0]
check('twenty_one_nonnegative_profiles',len(valid)==21)

def canonical(profile):
    p=list(range(sum(profile)));k=0
    for n in profile:
        for j in range(n):p[k+j]=k+(j+1)%n
        k+=n
    return tuple(p)
def compose(p,q):return tuple(p[q[i]] for i in range(len(p)))
def inverse(p):
    q=[0]*len(p)
    for i,j in enumerate(p):q[j]=i
    return tuple(q)
def cycles(p):
    seen=set();out=[]
    for i in range(len(p)):
        if i in seen:continue
        c=[];j=i
        while j not in seen:c.append(j);seen.add(j);j=p[j]
        out.append(c)
    return out
def cycle_type(p):return sorted(map(len,cycles(p)))
def matchings(xs):
    if not xs:
        yield ();return
    a=xs[0]
    for j in range(1,len(xs)):
        for tail in matchings(xs[1:j]+xs[j+1:]):yield ((a,xs[j]),)+tail
def involutions(n,fixed):
    for chosen in combinations(range(n),fixed):
        remaining=tuple(i for i in range(n) if i not in chosen)
        for pairs in matchings(remaining):
            p=list(range(n))
            for a,b in pairs:p[a]=b;p[b]=a
            yield tuple(p)
def connected(perms):
    seen={0};todo=[0]
    while todo:
        a=todo.pop()
        for p in perms:
            b=p[a]
            if b not in seen:seen.add(b);todo.append(b)
    return len(seen)==len(perms[0])

search_trials=0
for q in valid:
    n=q['degree'];s0=canonical(q['profile0']);ident=tuple(range(n))
    trans=[ident]
    if q['excess']==1:
        trans=[]
        for a,b in combinations(range(n),2):
            t=list(ident);t[a]=b;t[b]=a;trans.append(tuple(t))
    found=None
    for s1 in involutions(n,q['profile1'].count(1)):
        s01=compose(s0,s1)
        for ss in trans:
            search_trials+=1
            pp=compose(s01,ss)
            if cycle_type(pp)!=sorted(q['profile_infinity']):continue
            if not connected((s0,s1,ss)):continue
            found=(s0,s1,ss,inverse(pp));break
        if found:break
    check('new_transitive_tuple_'+str(q['row'])+'_'+'_'.join(q['fibres']),found is not None)
    s0,s1,ss,si=found
    check('tuple_product_identity_'+str(q['fibres']),compose(compose(compose(s0,s1),ss),si)==ident)
    check('Euler_cover_genus_zero_'+str(q['fibres']),sum(n-len(cycles(p)) for p in found)==2*n-2)
    # SymPy multiplication acts in its own convention: use explicit image list
    # for the desired product and independently verify each profile and orbit.
    lib=[Permutation(list(p),size=n) for p in found]
    check('SymPy_transitivity_'+str(q['fibres']),PermutationGroup(lib).is_transitive())
    for i,profile in enumerate((q['profile0'],q['profile1'],
                               [2]+[1]*(n-2) if q['excess']==1 else [1]*n,
                               q['profile_infinity'])):
        actual=sorted(k for k,v in lib[i].cycle_structure.items() for _ in range(v))
        check('SymPy_profile_'+str(i)+'_'+str(q['fibres']),actual==sorted(profile))
    q['permutations_zero_based']=[list(p) for p in found]
    q['cycles_one_based']=[[[i+1 for i in c] for c in cycles(p)] for p in found]

t,X,s,b,c,d=S.symbols('t X s b c d')
R=t*t+s;AA=R**2+b*t;BB=R**3+S.Rational(3,2)*b*t*R+S.Rational(3,8)*b*b
disc=S.expand(4*(-3*AA)**3+27*(2*BB)**2)
check('A7_model_1_discriminant',S.expand(disc.subs({s:1,b:1})-S.Rational(27,16)*(48*t**4+8*t**3+96*t*t+72*t+57))==0)
check('A7_model_2_discriminant',S.expand(disc.subs({s:3,b:48})-186624*(t+3)**2*(3*t*t-10*t+51))==0)
q1=S.Poly(disc.subs({s:1,b:1}),t)
check('A7_model_1_squarefree',S.gcd(q1,q1.diff()).degree()==0)
for name,poly in [('A',AA),('B',BB)]:
    check('A7_model_1_coprime_'+name,S.gcd(q1,S.Poly(poly.subs({s:1,b:1}),t)).degree()==0)
    p=S.Poly(poly.subs({s:3,b:48}),t)
    check('A7_model_2_simple_zero_'+name,p.eval(-3)==0 and p.diff().eval(-3)!=0)
check('A7_model_2_residual_squarefree',S.discriminant(3*t*t-10*t+51,t)!=0)
cubic=X**3+3*(t*t+s)*X**2-3*b*t*X+S.Rational(3,4)*b*b
lin=S.Poly(cubic.subs(X,c*t+d),t)
check('A7_linear_root_forces_slope_zero',lin.coeff_monomial(t**4)==3*c*c)
check('A7_constant_root_forces_zero',lin.coeff_monomial(t**2).subs(c,0)==3*d*d)
check('A7_constant_obstruction',S.simplify(cubic.subs(X,0)-S.Rational(3,4)*b*b)==0)
quad=S.Poly(cubic.subs(X,-3*t*t+c*t+d),t)
check('A7_quadratic_t5',quad.coeff_monomial(t**5)==9*c)
check('A7_quadratic_t4',S.factor(quad.coeff_monomial(t**4).subs(c,0))==9*(d+3*s))
check('A7_quadratic_residual',S.expand(cubic.subs(X,-3*(t*t+s))-(9*b*t*(t*t+s)+S.Rational(3,4)*b*b))==0)

def A(n):return [Q(j*(n-j),n) for j in range(n)]
components={43:[[Q(0),Q(3,2)]],45:[A(8)],46:[[Q(0),Q(1),Q(7,4),Q(7,4)]],
 47:[A(7),A(2)],49:[[Q(0),Q(4,3),Q(4,3)],A(2)],
 50:[[Q(0),Q(1),Q(5,4),Q(5,4)],A(3)],55:[A(5),A(4)],56:[A(5),A(3),A(2)]}
heights={43:Q(1,2),45:Q(1,8),46:Q(1,4),47:Q(1,14),49:Q(1,6),50:Q(1,12),55:Q(1,20),56:Q(1,30)}
height_results=[]
for row,sets in components.items():
    h=heights[row]
    check('max_contribution_bound_'+str(row),sum(max(a) for a in sets)<4-h)
    choices=[]
    for ids in product(*[range(len(a)) for a in sets]):
        contribution=sum(sets[j][i] for j,i in enumerate(ids))
        intersection=(h-2+contribution)/2
        if intersection.denominator==1 and intersection>=0:
            check('height_integral_choice_zero_'+str(row)+'_'+str(ids),intersection==0)
            choices.append(dict(components=ids,contribution=str(contribution)))
    check('primitive_choice_exists_'+str(row),bool(choices))
    height_results.append(dict(row=row,choices=choices))
check('OS49_cubic_positive_correction',(Q(1,2)-2+Q(3,2))/2==0)
check('OS49_wrong_negative_correction',(Q(1,2)-2-Q(3,2))/2==Q(-3,2))

a,bb,dd,xx,p=S.symbols('a b d x p')
D=dd+a+bb
degree6=S.Poly(((D+2*xx)**3-(D+2*xx)*(p+(a+bb)**2))/48,xx)
push=degree6.coeff_monomial(xx)+degree6.coeff_monomial(xx**2)*(a-bb)+degree6.coeff_monomial(xx**3)*(a*a-a*bb+bb*bb)
check('F14_projective_pushforward',S.expand(push-((3*dd*dd-p)/24+(a*a+a*dd)/2))==0)
check('F14_fixed_sheet_index',1+Q(-2,2)==0)
check('F22_Jiang_scalar',Q(6,896)-Q(1,192)==Q(1,672))
check('F22_oriented_generator',-Q(-24,672)==Q(1,28))
check('F22_Davis_positive_Milnor',Q(36-4,896)==Q(1,28))
check('F24_CN_normalization',Q(1,8*4*28)==Q(1,896))

v,theta,G,C,ss=S.symbols('v theta G C s')
origin=S.Matrix([-G*ss/4,-C*ss/4-ss**2/8-ss*v])
sigma=S.Matrix([G*v,C*v+2*v*v-2*v]);F=sigma-origin
gamma=S.Matrix([G,C+ss+4*v]);delta=S.Matrix([0,1])
def zero(mat):return all(S.expand(x)==0 for x in mat)
check('F23_ordinary_parameter_deck',zero(origin.subs(v,v+1)-origin+ss*delta))
check('F23_cusp_parameter_deck',zero(sigma.subs(v,v+1)-sigma+ss*delta-gamma))
check('F23_ordinary_cusp_deck',zero(origin.subs(ss,ss+4)-origin+gamma+2*delta))
check('F23_cusp_cusp_deck',zero(sigma.subs(ss,ss+4)-sigma))
change=F.subs(v,v+theta)-F
check('F23_full_angular_origin_identity',zero(change-theta*gamma-2*theta*(theta-1)*delta))
check('F23_full_fourth_root_winding',zero(change.subs(ss,ss+4)-change-4*theta*delta))
check('F23_both_delta_endpoints',all((2*theta*(theta-1)).subs(theta,j)==0 for j in (0,1)))

z,star=S.symbols('z star');mob=star*z/(z+star-1);inv=(star-1)*t/(star-t)
check('F6_Mobius_exact_inverse',S.cancel(mob.subs(z,inv)-t)==0)
check('F6_three_marked_branch_images',S.simplify(mob.subs(z,0))==0 and S.simplify(mob.subs(z,1))==1 and S.limit(mob,z,S.oo)==star)
check('F6_RH_genus_three',2-24+(4*2+3*3+11)==6)
check('F12_unimodular_coinvariants',(S.Matrix([[1,-1],[-1,2]])-S.eye(2)).det()==-1)

out={'status':'PASS','assertions':assertions,'seconds':round(time.monotonic()-start,3),
     'candidate_count':len(configs),'realized_profiles':len(valid),'search_trials':search_trials,
     'method':'Fresh pure-Python involution enumeration with independent SymPy permutation verification; exact rational and symbolic checks. No supplied code or certificate imported.',
     'excluded':sorted([list(x) for x in excluded]),'new_permutation_certificates':valid,
     'height_component_choices':height_results,'checks':checks,
     'limitations':'The geometric branched-cover construction, Miranda source theorem, normal/Cartier/collar identifications and orientation direction are read proof inputs, not certified by finite arithmetic.',
     'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
path=Path(__file__).with_suffix('.json');path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('status','assertions','seconds','candidate_count','realized_profiles','search_trials','code_sha256')},indent=2))
