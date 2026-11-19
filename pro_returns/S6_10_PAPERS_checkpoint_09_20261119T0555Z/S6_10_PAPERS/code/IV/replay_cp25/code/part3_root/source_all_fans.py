"""Exact selected-cusp return on every two-triangle lattice-basis fan.

The complete map proof is notes/part3_source_all_fans_working.md.
All arithmetic is integral or Fraction arithmetic. No residue is used to
recover a free relative invariant.
"""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime, timezone
from collections import deque
import json

ROOT = Path(__file__).resolve().parents[2]
ID = (1,0,0,1)
Q0 = (1,-1,0,1)
Q1 = (1,0,-1,1)
Q2 = (1,1,0,1)
Q1INV = (1,0,1,1)
R = (-1,-1,1,0)
SWAP = (0,1,1,0)

def mul(a,b):
    return (a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],
            a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3])

def det(a):
    return a[0]*a[3]-a[1]*a[2]

def inv(a):
    d=det(a)
    assert d in (-1,1)
    return (d*a[3],-d*a[1],-d*a[2],d*a[0])

def neg(a):
    return tuple(-x for x in a)

GROUP=(ID,R,mul(R,R),neg(ID),neg(R),neg(mul(R,R)))

def edges(P):
    vals=[]
    for a,b in ((P[0],P[2]),(P[1],P[3]),(P[0]-P[1],P[2]-P[3])):
        if a<0 or (a==0 and b<0): a,b=-a,-b
        vals.append((a,b))
    return tuple(sorted(vals))

def canonical(P):
    assert det(P) in (-1,1)
    positive = P if det(P)==1 else mul(P,SWAP)
    candidates=[mul(positive,g) for g in GROUP]
    fixed=[q for q in candidates if q[0]==1 and q[1]==0 and q[3]==1]
    if fixed:
        assert len(fixed)==1
        return fixed[0]
    nonfixed=[q for q in candidates if q[0]>0 and q[1]<0]
    assert len(nonfixed)==1, (P,candidates)
    return nonfixed[0]

def word_from_vertical(P):
    """Return the exact canonical T_n and a finite C0/C1 construction."""
    P=canonical(P)
    cursor=P
    backwards=[]
    while cursor[1]!=0:
        p,r=cursor[0],-cursor[1]
        assert p>0 and r>0
        old=p+r
        if r>=p:
            cursor=mul(cursor,Q2)
            backwards.append(0)
        else:
            cursor=mul(cursor,Q1INV)
            backwards.append(1)
        if cursor[1]!=0:
            assert cursor[0]-cursor[1]<old
    assert cursor==(1,0,cursor[2],1)
    word=tuple(reversed(backwards))
    rebuilt=cursor
    for i in word: rebuilt=mul(rebuilt,(Q0,Q1)[i])
    assert rebuilt==P
    return cursor[2],word,P

def local(P):
    Pi=inv(P)
    B=tuple(-6*x for x in mul(mul(Pi,(1,0,0,0)),P))
    l=(B[3]-B[2],B[0]-B[1],B[3])
    x,y=Pi[1],Pi[3]
    w=(x,y,-x-y)
    d=(-x-2*y,-2*x-y,x-y)
    I=tuple(-3*w[i]+d[i]*(l[i]+3) for i in range(3))
    W=tuple(-3*w[i]-d[i]*(l[i]+3) for i in range(3))
    return B,l,w,d,I,W

def integer(x):
    x=F(x)
    assert x.denominator==1, x
    return x.numerator

def check_trace(P,V,D):
    _,_,w,_,I,W=local(P)
    for j in (1,2):
        for k in range(3):
            assert w[j]*V[k][j]-w[0]*V[k][0] == (I[j] if k==j else 0)-(I[0] if k==0 else 0)
        assert w[j]*D[j]-w[0]*D[0] == W[j]-W[0]
    assert all(V[i][j]==V[j][i] for i in range(3) for j in range(3))

def vertical_seed(n):
    P=(1,0,n,1)
    h=18*n*(n-1)
    V=((h,6-12*n,12*n-6),(6-12*n,0,0),(12*n-6,0,0))
    D=(-12-h,12*n-12,-12*n)
    s=-1-3*n*(n-1)
    check_trace(P,V,D)
    return P,V,D,s

def child(P,V,D,s,i):
    assert i in (0,1)
    target=mul(P,(Q0,Q1)[i])
    a,b=V[i][i],D[i]
    _,_,w,_,I,W=local(target)
    assert all(w)
    c=w[2]**2*a-w[2]*I[2]
    e=w[2]*(2*a-b)-W[2]
    Vnew=tuple(tuple(integer((F(I[j],w[j]) if j==k else 0)+F(c,w[j]*w[k])) for k in range(3)) for j in range(3))
    Dnew=tuple(integer(F(W[j]+e,w[j])) for j in range(3))
    right=integer(F(b-a,2))
    check_trace(target,Vnew,Dnew)
    assert Vnew[2][2]==a and Dnew[2]==2*a-b
    assert integer(F(Dnew[2]-Vnew[2][2],2))==-right
    return target,Vnew,Dnew,s+right

def calculate(P,history=False):
    n,word,target=word_from_vertical(P)
    P0,V,D,s=vertical_seed(n)
    steps=[]
    for i in word:
        right=integer(F(D[i]-V[i][i],2))
        P0,V,D,s=child(P0,V,D,s,i)
        if history: steps.append({'edge':i,'target':P0,'native_right':right,'integer_sum':s})
    assert P0==target
    result={'input_basis':tuple(P),'canonical_basis':target,'vertical_index':n,'word':word,
            'variation':V,'stable_derivative':D,'integer_path_sum':s,'physical_class_mod28':s%28}
    if history: result['steps']=steps
    return result

def existing_single_seed_crosscheck(depth=8):
    """Independent paths: the old three-edge traversal, without fixed resets."""
    P,V,D,s=vertical_seed(0)
    todo=deque([(P,V,D,s,0)])
    seen=set(); checked=0; skipped=0
    while todo:
        P,V,D,s,level=todo.popleft()
        key=(P,V,D,s%28)
        if key in seen: continue
        seen.add(key)
        assert calculate(P)['physical_class_mod28']==s%28, (P,s,calculate(P))
        checked+=1
        if level==depth: continue
        for i,Q in enumerate((Q0,Q1,Q2)):
            T=mul(P,Q); selected=(2,2,0)[i]
            a,b=V[i][i],2*V[i][i]-D[i]
            _,_,w,_,I,W=local(T)
            zeros=[j for j in range(3) if w[j]==0]
            if not zeros:
                c=w[selected]**2*a-w[selected]*I[selected]
                e=w[selected]*b-W[selected]
                Vn=tuple(tuple(integer((F(I[j],w[j]) if j==k else 0)+F(c,w[j]*w[k])) for k in range(3)) for j in range(3))
                Dn=tuple(integer(F(W[j]+e,w[j])) for j in range(3))
            elif zeros==[selected]:
                r=selected; A=[[0]*3 for _ in range(3)]; ds=[0]*3
                A[r][r]=a; ds[r]=b
                for j in range(3):
                    if j==r: continue
                    A[j][j]=integer(F(I[j],w[j])); A[r][j]=A[j][r]=integer(F(-I[r],w[j])); ds[j]=integer(F(W[j]-W[r],w[j]))
                Vn=tuple(tuple(row) for row in A); Dn=tuple(ds)
            else:
                skipped+=1
                continue
            check_trace(T,Vn,Dn)
            todo.append((T,Vn,Dn,s+integer(F(D[i]-V[i][i],2)),level+1))
    return {'depth':depth,'independent_states':checked,'old_traversal_separate_fixed_skips':skipped}

def main():
    bound=18; inputs=0; fans={}; max_word=0
    for a in range(-bound,bound+1):
      for b in range(-bound,bound+1):
       for c in range(-bound,bound+1):
        for sign in (-1,1):
         if a:
            num=sign+b*c
            if num%a: continue
            ds=[num//a]
         else:
            if -b*c!=sign: continue
            ds=range(-bound,bound+1)
         for d in ds:
            if abs(d)>bound: continue
            P=(a,b,c,d)
            result=calculate(P)
            inputs+=1; max_word=max(max_word,len(result['word']))
            fk=edges(P)
            if fk in fans: assert fans[fk]==result['physical_class_mod28']
            fans[fk]=result['physical_class_mod28']
    for j in range(-30,31):
        assert calculate((1,0,j,1))['physical_class_mod28']==(-1-3*j*(j-1))%28
    for j in range(31):
        assert calculate((1,-j,0,1))['physical_class_mod28']==(-1-3*j*(j+1))%28
        assert calculate((j+1,-j,-1,1))['physical_class_mod28']==(-7-24*j*(j+1))%28
    independent=existing_single_seed_crosscheck()
    examples=[calculate(p,True) for p in [(2,-1,-1,1),(3,-2,2,-1),(5,-3,-3,2),(1,0,4,1),(4,-7,-1,2)]]
    output={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','entry_bound':bound,
            'unimodular_inputs':inputs,'distinct_fans':len(fans),'max_word_length':max_word,
            'observed_residue_image':sorted(set(fans.values())),
            'closed_formula_checks':123,'independent_traversal':independent,'examples':examples,
            'scope':'The finite checks support the complete arbitrary-input proof; no claim of an exhaustive residue image is inferred from this bound.'}
    (ROOT/'code/part3_root/source_all_fans.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))

if __name__=='__main__': main()
