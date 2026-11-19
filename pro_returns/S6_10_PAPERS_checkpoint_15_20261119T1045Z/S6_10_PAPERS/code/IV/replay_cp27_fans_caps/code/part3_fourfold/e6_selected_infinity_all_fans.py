"""Exact original-height selected-infinity fan algorithm.

Every target is reconstructed by fresh rational row reduction of all circle,
normal-derivative and selected-edge equations.  The optional comparison with
K71 evaluates two already typed algorithms; no free integer is recovered
from a residue.  The initial and vertical geometric proof is in the matching
working note.
"""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from collections import deque
from datetime import datetime, timezone
import hashlib, json, sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'code/part3_root'))
import source_all_fans as k71

ID, Q0, Q1, Q2 = k71.ID, k71.Q0, k71.Q1, k71.Q2
mul, inv, det = k71.mul, k71.inv, k71.det
W = (-4, 0, 0, 0)
T = -4
PAIRS = ((0,0),(0,1),(0,2),(1,1),(1,2),(2,2))
VID = {p:i for i,p in enumerate(PAIRS)}
SOLVE_LOG = {}
ASSERTIONS = 0

def ck(ok, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not ok: raise AssertionError(label)

def integer(v):
    v = F(v)
    ck(v.denominator == 1, ('nonintegral', v))
    return v.numerator

def local(P):
    B = tuple(2*z for z in mul(mul(inv(P), W), P))
    ell = (B[3]-B[2], B[0]-B[1], B[3])
    Pi = inv(P); x,y = Pi[1],Pi[3]
    weights = (x,y,-x-y)
    d = (-x-2*y,-2*x-y,x-y)
    I = tuple(T*weights[i]+d[i]*(ell[i]-T) for i in range(3))
    J = tuple(T*weights[i]-d[i]*(ell[i]-T) for i in range(3))
    return B,ell,weights,d,I,J

def prism_rows(P, c, e, selected):
    _,_,w,_,I,J = local(P)
    rows = []
    for i in (1,2):
        for r in range(3):
            row = [F(0)]*10
            row[VID[tuple(sorted((r,i)))]] += w[i]
            row[VID[tuple(sorted((r,0)))]] -= w[0]
            row[9] = (I[i] if r==i else 0)-(I[0] if r==0 else 0)
            rows.append(row)
        row = [F(0)]*10
        row[6+i] += w[i]; row[6] -= w[0]
        row[9] = J[i]-J[0]
        rows.append(row)
    row = [F(0)]*10; row[VID[(selected,selected)]]=1; row[9]=c
    rows.append(row)
    row = [F(0)]*10; row[6+selected]=1; row[9]=e
    rows.append(row)
    return rows

@lru_cache(maxsize=None)
def solve(P, c, e, selected=2):
    """Ten literal equations for six symmetric + three derivative entries."""
    original = prism_rows(P,c,e,selected)
    A = [list(map(F,row)) for row in original]
    pivots=[]; nextrow=0
    for col in range(9):
        pivot=next((r for r in range(nextrow,len(A)) if A[r][col]),None)
        if pivot is None: continue
        A[nextrow],A[pivot]=A[pivot],A[nextrow]
        scale=A[nextrow][col];A[nextrow]=[v/scale for v in A[nextrow]]
        for r in range(len(A)):
            if r==nextrow:continue
            scale=A[r][col]
            if scale:A[r]=[A[r][j]-scale*A[nextrow][j] for j in range(10)]
        pivots.append(col);nextrow+=1
    ck(all(any(row[:9]) or not row[9] for row in A),('inconsistent',P,c,e))
    if len(pivots)!=9:return None
    vals=[F(0)]*9
    for r,col in enumerate(pivots):vals[col]=A[r][9]
    ck(all(sum(row[i]*vals[i] for i in range(9))==row[9] for row in original),('full equations',P))
    vals=list(map(integer,vals))
    V=tuple(tuple(vals[VID[tuple(sorted((r,s)))]] for s in range(3)) for r in range(3))
    D=tuple(vals[6:9])
    SOLVE_LOG[(P,c,e,selected)]={'basis':P,'selected':selected,'c':c,'e':e,'rank':9,'variation':V,'derivative':D}
    return V,D

def seed(j):
    P=(1,0,j,1)
    mu=2;nu=-6-12*j*(j-1)
    c=2*T-2*mu-2*nu;e=2*T-2*mu+2*nu
    V,D=solve(P,c,e,0)
    ck(V==((24*j*(j-1),8-16*j,16*j-8),(8-16*j,0,0),(16*j-8,0,0)),('verticalV',j))
    ck(D==(-24-24*j*(j-1),16*j-16,-16*j),('verticalD',j))
    return P,V,D,integer(F(nu,6))

def child(P,V,D,S,i):
    target=mul(P,(Q0,Q1,Q2)[i]);selected=(2,2,0)[i]
    c,e=V[i][i],D[i]
    ans=solve(target,c,2*c-e,selected)
    if ans is None:return None
    Vn,Dn=ans;rho=integer(F(e-c,4))
    ck(integer(F(Dn[selected]-Vn[selected][selected],4))==-rho,('right inverse',target))
    return target,Vn,Dn,S+rho

def calculate(P,history=False):
    j,word,target=k71.word_from_vertical(tuple(P))
    current,V,D,S=seed(j);steps=[]
    for i in word:
        rho=integer(F(D[i]-V[i][i],4))
        current,V,D,S=child(current,V,D,S,i)
        if history:steps.append({'edge':i,'basis':current,'native_right':rho,'integer_sum':S,'variation':V,'derivative':D})
    ck(current==target,('reconstruction',P))
    out={'input_basis':tuple(P),'canonical_basis':target,'vertical_index':j,'word':word,'variation':V,'stable_derivative':D,'integer_path_sum':S,'physical_class_mod28':S%28}
    if history:out['steps']=steps
    return out

def inputs(bound):
    for a in range(-bound,bound+1):
      for b in range(-bound,bound+1):
       for c in range(-bound,bound+1):
        for sign in (-1,1):
         ds=([ (sign+b*c)//a ] if a and (sign+b*c)%a==0 else []) if a else (range(-bound,bound+1) if -b*c==sign else [])
         for d in ds:
          if abs(d)<=bound:yield(a,b,c,d)

def prism_comparison(P, ours):
    ref=k71.calculate(P)
    C=tuple(ours['canonical_basis']); x,y=inv(C)[1],inv(C)[3]
    norm=x*x+x*y+y*y;Dprod=x*y*(-x-y)
    ck((ref['integer_path_sum']+1)%3==0,('reference divisibility',C))
    ck(ours['integer_path_sum']==integer(F(2,3)*(ref['integer_path_sum']+1))-norm,('closed integer',C))
    ck(all(F(ours['variation'][r][s])==F(4,3)*ref['variation'][r][s] for r in range(3) for s in range(3)),('full V comparison',C))
    w=(x,y,-x-y)
    dd=[F(ours['stable_derivative'][i])-F(4,3)*ref['stable_derivative'][i] for i in range(3)]
    if x==0:ck(dd==[-8,0,0],('vertical derivative difference',C))
    else:ck(dd==[F(8*Dprod,wi) for wi in w],('all derivative difference',C))
    ck(ours['integer_path_sum']%2==1,('odd',C))
    return norm

def independent_three_edges(depth=7):
    todo=deque([(*seed(0),0)]);seen=set();skips=0
    while todo:
        P,V,D,S,lev=todo.popleft();key=(P,V,D,S%28)
        if key in seen:continue
        seen.add(key)
        ck(calculate(P)['physical_class_mod28']==S%28,('other path',P))
        if lev==depth:continue
        for i in range(3):
            ans=child(P,V,D,S,i)
            if ans is None:skips+=1
            else:todo.append((*ans,lev+1))
    return {'states':len(seen),'depth':depth,'separate_fixed_transitions_left_to_proved_seeds':skips}

def witnesses(depth=10):
    todo=deque([(*child(*seed(0),0),(0,))]);best={};count=0
    while todo:
        P,V,D,S,word=todo.popleft();count+=1
        score=(max(map(abs,P)),sum(map(abs,P)),len(word),P)
        r=S%28
        if r not in best or score<best[r][0]:best[r]=(score,calculate(P,True))
        if len(word)<depth:
            for i in (0,1):todo.append((*child(P,V,D,S,i),word+(i,)))
    ck(set(best)==set(range(1,28,2)),('witness image',sorted(best)))
    return {'visited_words':count,'depth':depth,'witnesses':[best[r][1] for r in sorted(best)]}

def symbolic():
    import sympy as s
    x,y=s.symbols('x y',nonzero=True);N=x*x+x*y+y*y;D=-x*y*(x+y)
    for i,(xp,yp) in enumerate(((x+y,y),(x,x+y))):
        wp=(xp,yp,-xp-yp);dp=wp[0]*wp[1]*wp[2]
        ck(s.cancel(dp/wp[2]+D/(x,y)[i])==0,('D identity',i))
        ck(s.expand(xp*xp+xp*yp+yp*yp-N+2*D/(x,y)[i])==0,('norm increment',i))
    j=s.symbols('j',integer=True)
    P=s.Matrix([[1,0],[j,1]]);Wm=s.diag(-4,0)
    ck(2*P.inv()*Wm*P==s.Matrix([[-8,0],[8*j,0]]),'vertical winding')
    eps,xo,yo,to=s.symbols('eps x y t')
    d=1-3*eps**2;r=eps**2*(3*eps**2-2)/d**2
    X=eps**2/d**2*xo;Y=eps**3/d**3*yo;TT=eps**4/d**3*to
    native=yo**2-xo**3-(3*eps**2-2)*xo**2-d*to*xo-eps**2*to**2
    ck(s.factor(Y**2-X**3-r*X**2-TT*X-TT**2-eps**6/d**6*native)==0,'full source equation')
    ck(s.simplify(r.subs(eps,-eps)-r)==0,'original parameter even')
    ck(s.simplify(TT.subs(eps,-eps)-TT)==0,'original height even')
    # Literal exterior algebra in order (alpha,u,b,gamma,theta).
    alpha,theta,z=s.symbols('alpha theta z')
    def add(*forms):
        out={}
        for f in forms:
            for k,v in f.items():out[k]=s.expand(out.get(k,0)+v)
        return {k:v for k,v in out.items() if v!=0}
    def scale(f,c):return {k:s.expand(c*v) for k,v in f.items() if c*v!=0}
    def wedge(f,g):
        out={}
        for I,a0 in f.items():
          for J,b0 in g.items():
            if set(I)&set(J):continue
            K=I+J;sign=(-1)**sum(K[p]>K[q] for p in range(len(K)) for q in range(p+1,len(K)))
            key=tuple(sorted(K));out[key]=out.get(key,0)+sign*a0*b0
        return {k:s.expand(v) for k,v in out.items() if s.expand(v)!=0}
    beta={(1,):-j,(2,):-j*(alpha-4*theta)}
    Fext={(0,3):1,(0,2):j}
    dbeta={(0,2):-j,(2,4):-4*j}
    Fz=add(Fext,scale(dbeta,z))
    value=wedge(beta,wedge(Fz,Fz))
    ck(set(value)=={(0,1,2,3,4)},'collar orientation support')
    ck(s.integrate(3*value[(0,1,2,3,4)],(z,0,1))==12*j*j,'exact outward primitive')
    ck(not wedge(dbeta,dbeta),'tensor square zero')
    dg=s.symbols('dg')
    J=s.Matrix([[1,dg,-j*dg],[0,1,-j],[0,0,1]])
    ck(J.det()==1,'full source triangular determinant')
    ck(s.expand((-4+12*j-12*j*j)-(-4-12*j*(j-1)))==0,'vertical endpoint calibration')
    return {'generator_D_and_norm_identities':4,'vertical_matrix':True,'full_source_and_even_endpoint':True,'exact_exterior_algebra_collar':True,'source_tangent_matrix':True}

def main():
    symbolic_data=symbolic();fans={};allinputs=list(inputs(18));maxword=0
    for P in allinputs:
        r=calculate(P);prism_comparison(P,r);key=k71.edges(P)
        if key in fans:ck(fans[key]==r['physical_class_mod28'],('identical fan',P))
        fans[key]=r['physical_class_mod28'];maxword=max(maxword,len(r['word']))
        Pi=inv(P)
        for k in range(4):
            U=tuple(int(k==i) for i in range(4))
            ck(mul(mul(P,mul(mul(Pi,U),P)),Pi)==U,('full coefficient inverse',P,k))
    for j in range(-40,41):prism_comparison((1,0,j,1),calculate((1,0,j,1)))
    traversal=independent_three_edges();exhibited=witnesses()
    source=ROOT/'notes/part3_e6_selected_infinity_all_fans_working.md'
    output={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),'input_winding_matrix':[[-4,0],[0,0]],'initial_physical_pair':[-4,8],'initial_native_pair':[2,-6],'checks':ASSERTIONS,'bounded_inputs':len(allinputs),'distinct_fans':len(fans),'observed_and_proved_image':sorted(set(fans.values())),'max_word_length':maxword,'fresh_full_rational_systems':len(SOLVE_LOG),'symbolic':symbolic_data,'independent_three_edges':traversal,'witness_data':exhibited,'full_solutions':list(SOLVE_LOG.values()),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest() if source.exists() else None,'scope':'Exact map proof and terminating construction cover every stated fan; finite checks and explicit witnesses independently audit the equations. No claim about another parameter loop or higher cap is included.'}
    path=ROOT/'code/part3_fourfold/e6_selected_infinity_all_fans.json';path.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({k:v for k,v in output.items() if k not in ('full_solutions','witness_data')},indent=2))
    print('WITNESSES',json.dumps([{'class':w['physical_class_mod28'],'P':w['canonical_basis'],'word':w['word'],'integer':w['integer_path_sum']} for w in exhibited['witnesses']]))

if __name__=='__main__':main()
