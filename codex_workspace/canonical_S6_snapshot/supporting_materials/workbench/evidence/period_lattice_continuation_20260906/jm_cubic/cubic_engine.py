"""Exact cubic pullback and finite value modules; no floating arithmetic."""
from fractions import Fraction as Q
from itertools import combinations, product
from functools import reduce
from math import gcd, lcm
import json


def check(condition, message):
    if not condition:
        raise ArithmeticError(message)


def add(x,y): return tuple(a+b for a,b in zip(x,y))
def neg(x): return tuple(-a for a in x)
def sub(x,y): return add(x,neg(y))
def scale(x,c): return tuple(c*a for a in x)
def dot(x,y): return sum(a*b for a,b in zip(x,y))


TRIPLES=((1,2,3),(1,4,5),(1,7,6),(2,4,6),(2,5,7),(3,4,7),(3,6,5))
def cross(x,y):
    out=[Q(0)]*7
    for a,b,c in TRIPLES:
        a,b,c=a-1,b-1,c-1
        out[c]+=x[a]*y[b]-x[b]*y[a]
        out[a]+=x[b]*y[c]-x[c]*y[b]
        out[b]+=x[c]*y[a]-x[a]*y[c]
    return tuple(out)


def residual_data(X):
    A,B,S=[],[],[]
    for i in range(4):
        part=X[6*i:6*i+6]
        S.append(sum((-1)**j*part[j] for j in range(6)))
        for p in (0,1):
            m=sum(part[p+2*j] for j in range(3))/3
            A.append(part[p]-m)
            B.append(part[p+2]-m)
    return tuple(A),tuple(B),tuple(S),X[24:]


def cubic(X):
    """Return coefficients of 1, sqrt(2), sqrt(3), exactly."""
    A,B,S,d=residual_data(X)
    a,b=A[0],B[0]
    u,v=A[1:],B[1:]
    uu,uv,vv=dot(u,u),dot(u,v),dot(v,v)
    P0=-a*b*(a+b)+b*uu+a*vv+2*(a+b)*uv
    D=a*a+a*b+b*b-uu-uv-vv
    Z=sub(add(scale(u,2*a+b),scale(v,a+2*b)),scale(cross(u,v),3))
    P2=(-S[0]*D+dot(S[1:],Z[:3]))/6
    P2+=S[0]*(4*S[0]**2-3*dot(S,S))/108-S[0]*dot(d,d)/6
    P3=dot(d,Z[3:])/3
    return P0,P2,P3


# Independent direct Cayley-Dickson evaluation in Q(sqrt(2),sqrt(3)).
FZERO=(Q(0),)*4
def field(q=0): return (Q(q),Q(0),Q(0),Q(0))
def fm(x,y):
    out=[Q(0)]*4
    for i,a in enumerate(x):
        if not a: continue
        for j,b in enumerate(y):
            if b:
                out[i^j]+=a*b*(2 if i&j&1 else 1)*(3 if i&j&2 else 1)
    return tuple(out)
def qa(x,y): return tuple(add(a,b) for a,b in zip(x,y))
def qn(x): return tuple(neg(a) for a in x)
def qc(x): return (x[0],)+qn(x[1:])
def qm(x,y):
    a,b,c,d=x; e,f,g,h=y
    return (sub(sub(sub(fm(a,e),fm(b,f)),fm(c,g)),fm(d,h)),
            add(add(sub(fm(a,f),fm(d,g)),fm(b,e)),fm(c,h)),
            add(add(sub(fm(a,g),fm(b,h)),fm(c,e)),fm(d,f)),
            add(add(sub(fm(a,h),fm(c,f)),fm(b,g)),fm(d,e)))
def om(x,y):
    a,b=x[:4],x[4:];c,d=y[:4],y[4:]
    return qa(qm(a,c),qn(qm(qc(d),b)))+qa(qm(d,a),qm(b,qc(c)))
def direct_cubic(X):
    A,B,S,d=residual_data(X)
    M=[(Q(0),S[a]/6,Q(0),Q(0)) for a in range(4)]
    M.extend((Q(0),Q(0),d[a]/3,Q(0)) for a in range(4))
    q=[tuple(add(field(value),M[a]) for a,value in enumerate(Y))
       for Y in (A,B,neg(add(A,B)))]
    return om(om(q[0],q[1]),q[2])[0]


def basis(k,n=28): return tuple(Q(int(i==k)) for i in range(n))
root=[]
for i in range(4):
    root.extend(sub(basis(6*i+j),basis(6*i+j+1)) for j in range(5))
root.extend([sub(basis(24),basis(25)),sub(basis(25),basis(26)),
             sub(basis(26),basis(27)),add(basis(26),basis(27))])
lam=tuple(Q(n,6) for n in (5,-1,-1,-1,-1,-1))
zero4=(Q(0),)*4
def glue_lift(k,d=zero4):
    return tuple(x for n in k for x in scale(lam,n))+tuple(map(Q,d))
G=root+[glue_lift((3,3,3,3)),glue_lift((3,3,0,0),(1,0,0,0)),
        glue_lift((3,0,3,0),(Q(1,2),)*4),glue_lift((2,2,2,0)),
        glue_lift((2,4,0,2))]
alpha=G[0]
rho=tuple(Q(5-2*j,2) for i in range(4) for j in range(6))+tuple(map(Q,(3,2,1,0)))
height=[dot(rho,g) for g in G]
check(height==[1]*24+[30,18,18,15,20], 'exact generator heights')
K=[scale(alpha,6)]+[sub(g,scale(alpha,h)) for g,h in zip(G[1:],height[1:])]
v=sub(scale(rho,Q(1,6)),alpha)
LG=K+[v]
check(len(G)==29 and len(LG)==30, 'generator counts')


def finite_value_generators(gens):
    singles=[cubic(g) for g in gens]
    out=[(f'F(g{i+1})',v) for i,v in enumerate(singles)]
    pair_values={}
    for i,j in combinations(range(len(gens)),2):
        plus=cubic(add(gens[i],gens[j]))
        minus=cubic(sub(gens[i],gens[j]))
        pair_values[i,j]=plus
        out.append((f'Dplus({i+1},{j+1})',sub(sub(plus,singles[i]),singles[j])))
        out.append((f'Dminus({i+1},{j+1})',add(sub(minus,singles[i]),singles[j])))
    for i,j,k in combinations(range(len(gens)),3):
        tri=cubic(add(add(gens[i],gens[j]),gens[k]))
        for pair in ((i,j),(i,k),(j,k)):
            tri=sub(tri,pair_values[pair])
        tri=add(tri,add(add(singles[i],singles[j]),singles[k]))
        out.append((f'D3({i+1},{j+1},{k+1})',tri))
    return out


def det3(columns):
    a,b,c=columns
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -b[0]*(a[1]*c[2]-a[2]*c[1])
            +c[0]*(a[1]*b[2]-a[2]*b[1]))


def value_module(gens,name):
    finite=finite_value_generators(gens)
    denom=lcm(*(q.denominator for _,v in finite for q in v))
    target_denominators=(27,54,18) if name=='N' else (27,216,54)
    coords={label:tuple(v[i]*target_denominators[i] for i in range(3))
            for label,v in finite}
    check(all(q.denominator==1 for col in coords.values() for q in col),
          'all finite values in stated module '+name)
    if name=='N':
        selected=['F(g1)','F(g2)','F(g7)','F(g28)','Dplus(21,28)',
                  'Dplus(2,27)','Dplus(2,25)']
        triples=((0,3,4),(1,2,5),(1,6,5))
        expected=(1792,-270,-1647)
    else:
        selected=['F(g2)','F(g4)','F(g28)','F(g30)','Dplus(2,27)']
        triples=((0,2,3),(0,3,4),(1,3,4))
        expected=(-5405504,2315394,1281267)
    minors=tuple(det3([coords[selected[i]] for i in triple]) for triple in triples)
    check(minors==expected,'displayed determinant values '+name)
    check(reduce(gcd,(int(v) for v in minors))==1,'gcd of displayed determinants')
    return {'finite_generator_count':len(finite),'common_denominator':denom,
            'basis_columns_in_1_sqrt2_sqrt3':
               [[str(Q(int(i==j),target_denominators[i])) for i in range(3)] for j in range(3)],
            'primitive_certificate':[
                {'generator':label,'coordinates':[int(x) for x in coords[label]]}
                for label in selected],
            'determinants':[int(v) for v in minors]},finite


def transform_shift(X,shift):
    return tuple(X[6*i+(j-shift)%6] for i in range(4) for j in range(6))+X[24:]
def transform_swap01(X):
    x=list(X);x[0],x[1]=x[1],x[0];return tuple(x)
def Rhat(X):
    x=X[6:12]+X[:6]+X[12:18]+neg(X[18:24])
    d=(-X[24],)+X[25:]
    return x+d
def Hhat(X):
    x=X[:6]+X[12:18]+X[6:12]+neg(X[18:24])
    d=X[24:]
    h=((1,1,1,1),(1,1,-1,-1),(1,-1,1,-1),(1,-1,-1,1))
    return x+tuple(dot(row,d)/2 for row in h)


if __name__=='__main__':
    results={}
    for name,gens in [('N',G),('Lambda',LG)]:
        results[name],finite=value_module(gens,name)
        results[name]['denominator_lcm_by_type']={
            prefix:[lcm(*(v[k].denominator for label,v in finite if label.startswith(prefix)))
                    for k in range(3)] for prefix in ('F(','Dplus(','Dminus(','D3(')}
        expected_table=([(27,27,1),(9,18,18),(9,18,18),(9,18,18)] if name=='N'
                        else [(27,216,27),(27,108,54),(27,108,54),(9,36,54)])
        check(list(results[name]['denominator_lcm_by_type'].values())
              ==[list(x) for x in expected_table],'displayed denominator table '+name)
    witnesses={}
    candidates=G+[add(g,h) for g,h in combinations(G,2)]+[v,rho]
    for name,T in [('six_cycle',lambda X:transform_shift(X,1)),
                   ('Weyl_swap_e0_e1_first_fibre',transform_swap01),
                   ('Rhat',Rhat),('Hhat',Hhat),('negation',neg)]:
        for i,X in enumerate(candidates):
            f,g=cubic(X),cubic(T(X))
            if f!=g:
                witnesses[name]={'candidate_index':i,'X':[str(x) for x in X],
                                 'F_X':[str(x) for x in f],'F_TX':[str(x) for x in g]}
                break
        check(name in witnesses,'find concrete nonpreserver '+name)
    for X in candidates:
        check(cubic(X)==cubic(transform_shift(X,2)), 'cyclic arithmetic check')
    direct_cases=G+LG+[rho]+[
        tuple(sum(Q(((i+3)*(j+2))%7-3)*G[j][k] for j in range(29))
              for k in range(28)) for i in range(5)]
    for X in direct_cases:
        check(direct_cubic(X)==cubic(X)+(Q(0),), 'independent direct octonion cubic')
    results['independent_direct_Cayley_Dickson_checks']=len(direct_cases)
    results['nonpreserver_witnesses']=witnesses
    results['special_values']={'rho':[str(x) for x in cubic(rho)],
                               'v':[str(x) for x in cubic(v)],
                               'alpha':[str(x) for x in cubic(alpha)]}
    print(json.dumps({'status':'PASS','results':results},indent=2))
