"""Exact OS49 return on every lattice-basis fan, with actual OR65 endpoints.

The geometric proof is P3K.77. The input j is m=3k on the canonical r
circle and k on the constructed w=r^3 circle. V and D are always the
literal double-circle ordinary invariants; S is the single-circle path sum.
"""
from collections import deque
from datetime import datetime, timezone
from fractions import Fraction as F
from pathlib import Path
import json
from source_all_fans import mul, inv, edges, word_from_vertical, Q0, Q1, Q2
from scalar_all_fans import bounded_inputs

ROOT = Path(__file__).resolve().parents[2]

def integer(x):
    x = F(x)
    assert x.denominator == 1, x
    return x.numerator

def local(P,j):
    Pi = inv(P)
    B = tuple(2*j*x for x in mul(mul(Pi,(0,0,-1,2)),P))
    ell = (B[3]-B[2],B[0]-B[1],B[3])
    t = 2*j
    x,y = Pi[1],Pi[3]
    w = (x,y,-x-y)
    d = (-x-2*y,-2*x-y,x-y)
    I = tuple(t*w[i]+d[i]*(ell[i]-t) for i in range(3))
    W = tuple(t*w[i]-d[i]*(ell[i]-t) for i in range(3))
    return B,ell,w,d,I,W

def check_trace(P,V,D,j):
    _,_,w,_,I,W = local(P,j)
    for a in (1,2):
        for b in range(3):
            assert w[a]*V[b][a]-w[0]*V[b][0] == (I[a] if b==a else 0)-(I[0] if b==0 else 0)
        assert w[a]*D[a]-w[0]*D[0] == W[a]-W[0]
    assert all(V[a][b] == V[b][a] for a in range(3) for b in range(3))

def vertical_seed(n,j):
    P = (1,0,n,1)
    h = 12*j*(n-1)**2
    V = ((h,8*j*(1-n),8*j*(n-1)),
         (8*j*(1-n),4*j,0),(8*j*(n-1),0,4*j))
    D = (-h,8*j*(n-1),8*j*(1-n))
    S = -j*(n-1)**2
    check_trace(P,V,D,j)
    assert integer(F(D[0]-V[0][0],4)) == -6*j*(n-1)**2
    return P,V,D,S

def child(P,V,D,S,i,j):
    assert i in (0,1)
    target = mul(P,(Q0,Q1)[i])
    a,b = V[i][i],D[i]
    _,_,w,_,I,W = local(target,j)
    assert all(w)
    C = w[2]**2*a-w[2]*I[2]
    E = w[2]*(2*a-b)-W[2]
    Vn = tuple(tuple(integer((F(I[h],w[h]) if h==k else 0)+F(C,w[h]*w[k]))
                     for k in range(3)) for h in range(3))
    Dn = tuple(integer(F(W[h]+E,w[h])) for h in range(3))
    increment = integer(F(b-a,4))
    check_trace(target,Vn,Dn,j)
    assert Vn[2][2] == a and Dn[2] == 2*a-b
    assert integer(F(Dn[2]-Vn[2][2],4)) == -increment
    return target,Vn,Dn,S+increment

def calculate(P,j,history=False):
    n,word,target = word_from_vertical(P)
    cursor,V,D,S = vertical_seed(n,j)
    steps = []
    for i in word:
        old_a,old_b = V[i][i],D[i]
        increment = integer(F(old_b-old_a,4))
        cursor,V,D,S = child(cursor,V,D,S,i,j)
        if history:
            steps.append({'selected_curve':i,'target':cursor,
                          'old_double_variation':old_a,'old_double_derivative':old_b,
                          'single_native_right':increment,'integer_path_sum':S,
                          'double_variation':V,'double_stable_derivative':D})
    assert cursor == target
    result = {'input_basis':tuple(P),'canonical_basis':target,
              'vertical_index':n,'word':word,'j':j,
              'double_variation':V,'double_stable_derivative':D,
              'integer_path_sum':S,'physical_class_mod28':S%28}
    if history: result['steps'] = steps
    return result

def independent_traversal(j,depth=8):
    """Traverse all three local curve choices, including actual inverse edges.

    Targets with a separate fixed curve are recorded and left to the proved
    vertical seed; no arbitrary integration constant is chosen at such a target.
    """
    P,V,D,S = vertical_seed(0,j)
    todo = deque([(P,V,D,S,0)]); seen=set(); checked=skipped=0
    while todo:
        P,V,D,S,level = todo.popleft()
        key = (P,V,D,S%28)
        if key in seen: continue
        seen.add(key)
        assert calculate(P,j)['physical_class_mod28'] == S%28
        checked += 1
        if level == depth: continue
        for i,Q in enumerate((Q0,Q1,Q2)):
            T=mul(P,Q); selected=(2,2,0)[i]
            a,b=V[i][i],2*V[i][i]-D[i]
            _,_,w,_,I,W=local(T,j)
            zeros=[h for h in range(3) if w[h]==0]
            if not zeros:
                C=w[selected]**2*a-w[selected]*I[selected]
                E=w[selected]*b-W[selected]
                Vn=tuple(tuple(integer((F(I[h],w[h]) if h==k else 0)+F(C,w[h]*w[k]))
                                   for k in range(3)) for h in range(3))
                Dn=tuple(integer(F(W[h]+E,w[h])) for h in range(3))
            elif zeros==[selected]:
                r=selected; A=[[0]*3 for _ in range(3)]; ds=[0]*3
                A[r][r]=a; ds[r]=b
                for h in range(3):
                    if h==r: continue
                    A[h][h]=integer(F(I[h],w[h]))
                    A[r][h]=A[h][r]=integer(F(-I[r],w[h]))
                    ds[h]=integer(F(W[h]-W[r],w[h]))
                Vn=tuple(tuple(row) for row in A); Dn=tuple(ds)
            else:
                skipped+=1; continue
            check_trace(T,Vn,Dn,j)
            todo.append((T,Vn,Dn,S+integer(F(D[i]-V[i][i],4)),level+1))
    return {'depth':depth,'independent_states':checked,
            'separate_fixed_target_skips':skipped}

def main():
    bound=18; inputs=list(bounded_inputs(bound)); records=[]; witnesses={}
    cover_checks=0
    for k in (1,2,5,7):
        fans={}; max_word=0
        for P in inputs:
            short=calculate(P,k)
            max_word=max(max_word,len(short['word']))
            key=edges(P)
            if key in fans: assert fans[key]==short['physical_class_mod28']
            fans[key]=short['physical_class_mod28']
            whole=calculate(P,3*k)
            assert whole['double_variation']==tuple(tuple(3*x for x in row) for row in short['double_variation'])
            assert whole['double_stable_derivative']==tuple(3*x for x in short['double_stable_derivative'])
            assert whole['integer_path_sum']==3*short['integer_path_sum']
            cover_checks+=1
            if k==1:
                residue=short['physical_class_mod28']; C=short['canonical_basis']
                score=(max(map(abs,C)),sum(map(abs,C)),len(short['word']),C)
                if residue not in witnesses or score<witnesses[residue][0]:
                    witnesses[residue]=(score,calculate(C,1,True))
        for n in range(-40,41):
            assert calculate((1,0,n,1),k)['integer_path_sum']==-k*(n-1)**2
            assert calculate((1,0,n,1),3*k)['integer_path_sum']==-3*k*(n-1)**2
        records.append({'actual_OS49_k':k,'canonical_m':3*k,
                        'shorter_unimodular_inputs':len(inputs),
                        'canonical_unimodular_inputs':len(inputs),
                        'distinct_fans':len(fans),'maximum_word_length':max_word,
                        'observed_shorter_residues':sorted(set(fans.values())),
                        'vertical_checks':162,'independent':independent_traversal(k),
                        'example':calculate((2,-1,-1,1),k,True)})
    example=calculate((2,-1,-1,1),1,True)
    assert example['integer_path_sum']==-49
    assert example['physical_class_mod28']==7
    assert [s['single_native_right'] for s in example['steps']]==[-6,-42]
    result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS',
            'entry_bound':bound,'total_unimodular_executions':8*len(inputs),
            'full_degree_three_cover_checks':cover_checks,'families':records,
            'k1_shorter_witnesses':[witnesses[r][1] for r in sorted(witnesses)],
            'scope':'Exact bounded audit of the unrestricted geometric algorithm in K77. Every full free invariant is computed before reduction modulo28. The explicit witness records state the attained residues; their completeness is checked separately.'}
    (ROOT/'code/part3_root/os49_all_fans.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
