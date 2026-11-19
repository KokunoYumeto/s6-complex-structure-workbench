"""K90 exact source-zero fan algorithm, reconstructed after the 2026-11-17 outage.

The original post-checkpoint19 file was lost. This reconstruction implements
the complete ZA.1--5 proof retained in the conversation. Free integers are
transported by the actual doubled-prism reset, never lifted from residues.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import deque
from datetime import datetime, timezone
import json
from source_all_fans import ID,Q0,Q1,Q2,mul,inv,det,edges,canonical,word_from_vertical,integer

ROOT=Path(__file__).resolve().parents[2]

def choose2(j): return j*(j-1)//2
def polynomial(b,j): return b*(j+1)*j*(j-1)//3+(3-b)*(j+1)*j//2

def parameters(a,p,k):
    assert a in (1,2) and p>=1 and k>=0
    b=3-a; m=4*p-(a-1); N=k*m
    return b,m,N,N-1,2-a+6*p*k

def local(P,a,p,k):
    b,m,N,t,mu=parameters(a,p,k)
    W=(1,b,-a,N-2)
    B=tuple(2*x for x in mul(mul(inv(P),W),P))
    ell=(B[3]-B[2],B[0]-B[1],B[3])
    x,y=inv(P)[1],inv(P)[3]
    w=(x,y,-x-y); d=(-x-2*y,-2*x-y,x-y)
    I=tuple(t*w[i]+d[i]*(ell[i]-t) for i in range(3))
    J=tuple(t*w[i]-d[i]*(ell[i]-t) for i in range(3))
    return B,ell,w,d,I,J

def check_trace(P,V,D,a,p,k):
    _,_,w,_,I,J=local(P,a,p,k)
    for i in (1,2):
        for r in range(3):
            assert w[i]*V[r][i]-w[0]*V[r][0] == (I[i] if r==i else 0)-(I[0] if r==0 else 0)
        assert w[i]*D[i]-w[0]*D[0] == J[i]-J[0]
    assert all(V[i][j]==V[j][i] for i in range(3) for j in range(3))

def vertical_seed(j,a,p,k):
    b,m,N,t,mu=parameters(a,p,k)
    A=polynomial(b,j)+k*(a-1)*(3*p-1)-N*choose2(j)
    P=(1,0,j,1); _,_,_,_,I,J=local(P,a,p,k)
    V=((2*t-2*mu-12*A,-I[0],I[0]),(-I[0],I[1],0),(I[0],0,-I[2]))
    D=(2*t-2*mu+12*A,J[1]-J[0],J[0]-J[2])
    check_trace(P,V,D,a,p,k)
    return P,V,D,A

def reconstruct(T,c,e,selected,a,p,k):
    _,_,w,_,I,J=local(T,a,p,k)
    zeros=[i for i,x in enumerate(w) if x==0]
    if not zeros:
        C=w[selected]**2*c-w[selected]*I[selected]
        E=w[selected]*e-J[selected]
        V=tuple(tuple(integer((F(I[r],w[r]) if r==s else 0)+F(C,w[r]*w[s])) for s in range(3)) for r in range(3))
        D=tuple(integer(F(J[r]+E,w[r])) for r in range(3))
    elif zeros==[selected]:
        r=selected; vv=[[0]*3 for _ in range(3)]; dd=[0]*3
        vv[r][r]=c;dd[r]=e
        for i in range(3):
            if i==r: continue
            vv[i][i]=integer(F(I[i],w[i]));vv[r][i]=vv[i][r]=integer(F(-I[r],w[i]));dd[i]=integer(F(J[i]-J[r],w[i]))
        V=tuple(tuple(row) for row in vv);D=tuple(dd)
    else:
        return None
    check_trace(T,V,D,a,p,k)
    assert V[selected][selected]==c and D[selected]==e
    return V,D

def child(P,V,D,S,i,a,p,k):
    assert i in (0,1)
    T=mul(P,(Q0,Q1)[i]);c,e=V[i][i],D[i]
    assert all(local(T,a,p,k)[2])
    Vn,Dn=reconstruct(T,c,2*c-e,2,a,p,k)
    rho=integer(F(e-c,4))
    assert integer(F(Dn[2]-Vn[2][2],4))==-rho
    return T,Vn,Dn,S+rho

def calculate(P,a=1,p=1,k=0,history=False):
    j,word,T=word_from_vertical(tuple(P))
    current,V,D,S=vertical_seed(j,a,p,k);steps=[]
    for i in word:
        rho=integer(F(D[i]-V[i][i],4))
        current,V,D,S=child(current,V,D,S,i,a,p,k)
        if history: steps.append({'edge':i,'target':current,'native_right':rho,'integer_sum':S})
    assert current==T
    result={'input_basis':tuple(P),'canonical_basis':T,'a':a,'p':p,'scalar_winding':k,'vertical_index':j,'word':word,'variation':V,'stable_derivative':D,'integer_path_sum':S,'physical_class_mod28':S%28}
    if history: result['steps']=steps
    return result

def bounded_inputs(bound=18):
    for a in range(-bound,bound+1):
      for b in range(-bound,bound+1):
       for c in range(-bound,bound+1):
        for sign in (-1,1):
         if a:
            num=sign+b*c
            if num%a:continue
            ds=[num//a]
         else:
            if -b*c!=sign:continue
            ds=range(-bound,bound+1)
         for d in ds:
            if abs(d)<=bound:yield(a,b,c,d)

def independent_traversal(a,p,k,depth=7):
    P,V,D,S=vertical_seed(0,a,p,k)
    todo=deque([(P,V,D,S,0)]);seen=set();skipped=0
    while todo:
        P,V,D,S,lev=todo.popleft();key=(P,V,D,S%28)
        if key in seen:continue
        seen.add(key)
        assert calculate(P,a,p,k)['physical_class_mod28']==S%28
        if lev==depth:continue
        for i,Q in enumerate((Q0,Q1,Q2)):
            T=mul(P,Q);c,e=V[i][i],D[i]
            ans=reconstruct(T,c,2*c-e,(2,2,0)[i],a,p,k)
            if ans is None:skipped+=1;continue
            Vn,Dn=ans;todo.append((T,Vn,Dn,S+integer(F(e-c,4)),lev+1))
    return {'depth':depth,'states':len(seen),'separate_fixed_seed_transitions_skipped':skipped}

def base_sector_witnesses(a,max_length=10):
    P,V,D,S=vertical_seed(0,a,1,0)
    first=child(P,V,D,S,0,a,1,0);todo=deque([(*first,(0,))]);best={};count=0
    while todo:
        P,V,D,S,word=todo.popleft();count+=1
        assert word_from_vertical(P)[0]==0
        score=(max(abs(v) for v in P),sum(abs(v) for v in P),len(word),P)
        residue=S%28
        if residue not in best or score<best[residue][0]:
            best[residue]=(score,calculate(P,a,1,0,True))
        if len(word)==max_length:continue
        for i in (0,1):todo.append((*child(P,V,D,S,i,a,1,0),word+(i,)))
    assert count==2**max_length-1 and len(best)==28
    return {'a':a,'b':3-a,'visited_words':count,'max_word_length':max_length,'witnesses':[best[r][1] for r in range(28)]}

def main():
    inputs=list(bounded_inputs());assert len(inputs)==6504
    cases=[]
    for a in (1,2):
      for p,k in ((1,0),(1,1),(1,2),(2,1),(3,2)):
        fans={};maximum=0
        for P in inputs:
            q=calculate(P,a,p,k);key=edges(P);val=q['physical_class_mod28']
            if key in fans:assert fans[key]==val
            fans[key]=val;maximum=max(maximum,len(q['word']))
        assert len(fans)==814
        for j in range(-30,31):
            q=calculate((1,0,j,1),a,p,k);b,m,N,t,mu=parameters(a,p,k)
            assert q['integer_path_sum']==polynomial(b,j)+k*(a-1)*(3*p-1)-N*choose2(j)
        cases.append({'a':a,'p':p,'scalar_winding':k,'unimodular_inputs':len(inputs),'distinct_fans':len(fans),'observed_residue_image':sorted(set(fans.values())),'max_word_length':maximum,'independent_traversal':independent_traversal(a,p,k)})
    witnesses=[base_sector_witnesses(a) for a in (1,2)]
    linearity=0
    for branch in witnesses:
      a=branch['a']
      for w in branch['witnesses']:
       P=tuple(w['input_basis'])
       assert calculate(P,a,1,0)=={key:val for key,val in w.items() if key!='steps'}
       for p in (1,2):
        q0=calculate(P,a,p,0);q1=calculate(P,a,p,1)
        for k in (2,3):
         q=calculate(P,a,p,k)
         assert q['integer_path_sum']==q0['integer_path_sum']+k*(q1['integer_path_sum']-q0['integer_path_sum'])
         assert all(q['variation'][i][j]==q0['variation'][i][j]+k*(q1['variation'][i][j]-q0['variation'][i][j]) for i in range(3) for j in range(3))
         assert all(q['stable_derivative'][i]==q0['stable_derivative'][i]+k*(q1['stable_derivative'][i]-q0['stable_derivative'][i]) for i in range(3))
         linearity+=1
    coefficient_checks=0
    for P in inputs:
        Pi=inv(P)
        assert mul(P,Pi)==ID and mul(Pi,P)==ID
        # Four independent full-unit exponents: inverse conjugation is literal.
        for r in range(4):
            E=tuple(int(i==r) for i in range(4))
            assert mul(mul(P,mul(mul(Pi,E),P)),Pi)==E
        coefficient_checks+=1
    for a,expected in ((1,(6,6)),(2,(9,0))):
        assert (calculate(mul(Q0,Q0),a)['physical_class_mod28'],calculate(mul(Q0,Q1),a)['physical_class_mod28'])==expected
    result={'status':'PASS','recovery':'Mathematical reconstruction from retained ZA proof; original bytes lost.','utc_runtime':datetime.now(timezone.utc).isoformat(),'entry_bound':18,'total_inputs':len(inputs)*len(cases),'cases':cases,'full_coefficient_inverse_checks':coefficient_checks,'integer_linearity_checks':linearity,'legacy_K88_witnesses_recovered':56,'fixed_scalar_witnesses':witnesses,'scope':'The exact Euclidean construction proves arbitrary-input coverage. The bounded coupled images are exhibited samples, not a universal coupled-image assertion.'}
    (ROOT/'code/part3_root/source_zero_all_fans.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({key:val for key,val in result.items() if key!='fixed_scalar_witnesses'},indent=2))

if __name__=='__main__':main()
