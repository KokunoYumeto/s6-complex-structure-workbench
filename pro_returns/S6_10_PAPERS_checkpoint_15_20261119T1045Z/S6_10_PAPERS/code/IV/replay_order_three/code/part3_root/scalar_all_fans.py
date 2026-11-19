"""Exact physical scalar returns on every two-triangle lattice-basis fan.

The proof is P3K.73. The supplied data are from actual constructed families;
effective H and chi are rational characteristic quotients on an explicitly
identified shorter parameter cover. No division in Theta_7 is performed.
"""
from collections import deque
from datetime import datetime, timezone
from fractions import Fraction as F
from pathlib import Path
import json
from source_all_fans import (mul, inv, edges, word_from_vertical, Q0, Q1, Q2)

ROOT = Path(__file__).resolve().parents[2]

def integer(x):
    x = F(x)
    assert x.denominator == 1, x
    return x.numerator

def local(P, J):
    Pi = inv(P)
    B = tuple(2*J*x for x in mul(mul(Pi, (0,0,0,1)), P))
    l = (B[3]-B[2], B[0]-B[1], B[3])
    x,y = Pi[1], Pi[3]
    w = (x,y,-x-y)
    d = (-x-2*y,-2*x-y,x-y)
    I = tuple(J*w[i]+d[i]*(l[i]-J) for i in range(3))
    W = tuple(J*w[i]-d[i]*(l[i]-J) for i in range(3))
    return B,l,w,d,I,W

def check_trace(P, V, D, J):
    _,_,w,_,I,W = local(P,J)
    for j in (1,2):
        for k in range(3):
            assert w[j]*V[k][j]-w[0]*V[k][0] == (I[j] if k==j else 0)-(I[0] if k==0 else 0)
        assert w[j]*D[j]-w[0]*D[0] == W[j]-W[0]
    assert all(V[i][j] == V[j][i] for i in range(3) for j in range(3))

def vertical_seed(n,J,H,chi):
    H,chi = F(H),F(chi)
    P = (1,0,n,1)
    h = 6*J*n*(n-1)
    V = ((2*J-6*H+h,2*J*(1-2*n),2*J*(2*n-1)),
         (2*J*(1-2*n),2*J,0),(2*J*(2*n-1),0,2*J))
    D = (2*J+6*H-24*chi-h,2*J*(2*n-1),2*J*(1-2*n))
    V = tuple(tuple(integer(x) for x in row) for row in V)
    D = tuple(integer(x) for x in D)
    S = integer(H/2-chi-F(J*n*(n-1),2))
    check_trace(P,V,D,J)
    assert integer(F(D[0]-V[0][0],4)) == integer(3*H-6*chi-3*J*n*(n-1))
    return P,V,D,S

def child(P,V,D,S,i,J):
    assert i in (0,1)
    target = mul(P,(Q0,Q1)[i])
    a,b = V[i][i],D[i]
    _,_,w,_,I,W = local(target,J)
    assert all(w)
    c = w[2]**2*a-w[2]*I[2]
    e = w[2]*(2*a-b)-W[2]
    Vn = tuple(tuple(integer((F(I[j],w[j]) if j==k else 0)+F(c,w[j]*w[k]))
                     for k in range(3)) for j in range(3))
    Dn = tuple(integer(F(W[j]+e,w[j])) for j in range(3))
    increment = integer(F(b-a,4))
    check_trace(target,Vn,Dn,J)
    assert Vn[2][2] == a and Dn[2] == 2*a-b
    assert integer(F(Dn[2]-Vn[2][2],4)) == -increment
    return target,Vn,Dn,S+increment

def calculate(P,J,H,chi,history=False):
    n,word,target = word_from_vertical(P)
    cursor,V,D,S = vertical_seed(n,J,H,chi)
    steps = []
    for i in word:
        increment = integer(F(D[i]-V[i][i],4))
        cursor,V,D,S = child(cursor,V,D,S,i,J)
        if history:
            steps.append({'edge':i,'target':cursor,'actual_single_native_right':increment,
                          'integer_path_sum':S})
    assert cursor == target
    result = {'input_basis':tuple(P),'canonical_basis':target,'vertical_index':n,
              'word':word,'double_variation':V,'double_stable_derivative':D,
              'integer_path_sum':S,'physical_class_mod28':S%28}
    if history: result['steps'] = steps
    return result

def independent_traversal(J,H,chi,depth=7):
    P,V,D,S = vertical_seed(0,J,H,chi)
    todo = deque([(P,V,D,S,0)]); seen=set(); checked=skipped=0
    while todo:
        P,V,D,S,level = todo.popleft()
        key = (P,V,D,S%28)
        if key in seen: continue
        seen.add(key)
        assert calculate(P,J,H,chi)['physical_class_mod28'] == S%28
        checked += 1
        if level == depth: continue
        for i,Q in enumerate((Q0,Q1,Q2)):
            T=mul(P,Q); selected=(2,2,0)[i]
            a,b=V[i][i],2*V[i][i]-D[i]
            _,_,w,_,I,W=local(T,J)
            zeros=[j for j in range(3) if w[j]==0]
            if not zeros:
                c=w[selected]**2*a-w[selected]*I[selected]
                e=w[selected]*b-W[selected]
                Vn=tuple(tuple(integer((F(I[j],w[j]) if j==k else 0)+F(c,w[j]*w[k]))
                                  for k in range(3)) for j in range(3))
                Dn=tuple(integer(F(W[j]+e,w[j])) for j in range(3))
            elif zeros==[selected]:
                r=selected; A=[[0]*3 for _ in range(3)]; ds=[0]*3
                A[r][r]=a; ds[r]=b
                for j in range(3):
                    if j==r: continue
                    A[j][j]=integer(F(I[j],w[j]))
                    A[r][j]=A[j][r]=integer(F(-I[r],w[j]))
                    ds[j]=integer(F(W[j]-W[r],w[j]))
                Vn=tuple(tuple(row) for row in A); Dn=tuple(ds)
            else:
                skipped+=1; continue
            check_trace(T,Vn,Dn,J)
            todo.append((T,Vn,Dn,S+integer(F(D[i]-V[i][i],4)),level+1))
    return {'depth':depth,'independent_states':checked,'separate_fixed_target_skips':skipped}

def bounded_inputs(bound):
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
            if abs(d)<=bound: yield (a,b,c,d)

def main():
    # Primitive source entry of discriminant d has (J,H,chi)=(1,d,1).
    # Original coprime shorter family: J=2KL,H=KL/3,chi=KL/6.
    families=[('OS45_d8',1,F(8),F(1)),('OS47_d14',1,F(14),F(1)),
              ('OS55_d20',1,F(20),F(1)),('OS56_d30',1,F(30),F(1)),
              ('original_K1_L1_shorter',2,F(1,3),F(1,6)),
              ('original_K1_L5_shorter',10,F(5,3),F(5,6))]
    bound=18; inputs=list(bounded_inputs(bound)); records=[]
    witnesses={}
    for name,J,H,chi in families:
        fans={}; max_word=0
        for P in inputs:
            result=calculate(P,J,H,chi)
            max_word=max(max_word,len(result['word']))
            key=edges(P)
            if key in fans: assert fans[key]==result['physical_class_mod28']
            fans[key]=result['physical_class_mod28']
            if name=='original_K1_L1_shorter':
                residue=result['physical_class_mod28']; C=result['canonical_basis']
                score=(max(map(abs,C)),sum(map(abs,C)),len(result['word']),C)
                if residue not in witnesses or score<witnesses[residue][0]:
                    witnesses[residue]=(score,{'residue':residue,'basis':C,
                        'vertical_index':result['vertical_index'],'word':result['word'],
                        'integer_path_sum':result['integer_path_sum']})
        for n in range(-30,31):
            expected=integer(H/2-chi-F(J*n*(n-1),2))%28
            assert calculate((1,0,n,1),J,H,chi)['physical_class_mod28']==expected
        examples=[calculate(P,J,H,chi,True) for P in
                  [(2,-1,-1,1),(3,-2,2,-1),(5,-3,-3,2),(1,0,4,1),(4,-7,-1,2)]]
        records.append({'actual_family':name,'J':J,'H_effective':str(H),'chi_effective':str(chi),
                        'unimodular_inputs':len(inputs),'distinct_fans':len(fans),
                        'maximum_word_length':max_word,'observed_residues':sorted(set(fans.values())),
                        'vertical_formula_checks':61,'independent':independent_traversal(J,H,chi),
                        'examples':examples})
    assert records[0]['examples'][0]['physical_class_mod28']==11
    assert [s['actual_single_native_right'] for s in records[0]['examples'][0]['steps']]==[18,102]
    assert set(witnesses)==set(range(28))
    for _,witness in witnesses.values():
        full=calculate(witness['basis'],2,F(1,3),F(1,6),True)
        witness['single_native_increments']=[s['actual_single_native_right'] for s in full['steps']]
        assert full['physical_class_mod28']==witness['residue']
    # Exact free-invariant pullback: the actual b=6 original shorter endpoint.
    cover_checks=0
    for P in inputs[::31]:
        short=calculate(P,2,F(1,3),F(1,6))
        whole=calculate(P,12,F(2),F(1))
        assert whole['double_variation']==tuple(tuple(6*x for x in row) for row in short['double_variation'])
        assert whole['double_stable_derivative']==tuple(6*x for x in short['double_stable_derivative'])
        assert whole['integer_path_sum']==6*short['integer_path_sum']
        cover_checks+=1
    result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','entry_bound':bound,
            'actual_family_count':len(records),'total_unimodular_executions':len(inputs)*len(records),
            'full_free_invariant_cover_checks':cover_checks,'families':records,
            'original_shorter_all_28_witnesses':[witnesses[j][1] for j in range(28)],
            'scope':'Finite exact checks support the unrestricted-input geometric proof. All28 original-shorter target elements have explicit verified fan witnesses, proving that image equals Theta7. Other printed residue lists are finite observed images.'}
    (ROOT/'code/part3_root/scalar_all_fans.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
