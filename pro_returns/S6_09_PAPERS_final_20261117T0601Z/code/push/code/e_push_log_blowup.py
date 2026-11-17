"""Exact audits for B.4.27; the all-length proof is in the TeX source.

Enumerates point-blowup markings through four exceptional curves, including
smooth exceptional points and crossings with either strict boundary axis.
No statement about arbitrary analytic caps is inferred from this code.
"""
from pathlib import Path
import json
import sympy as S

m,n,a,b=S.symbols('m n a b',integer=True,positive=True)
block=S.diag(12*m*a,12*m*a+12*n*b)
assert S.factor(block.det())==144*a*m*(a*m+b*n)

initial={'vals':{'Q':(1,0),'R':(0,1)},'self':{},'edges':{frozenset(('Q','R'))}}

def next_states(state):
    centres=[tuple(sorted(edge)) for edge in sorted(state['edges'],key=lambda x:tuple(sorted(x)))]
    centres += [(key,) for key in sorted(state['self'])]
    for centre in centres:
        vals=dict(state['vals']); selfint=dict(state['self']); edges=set(state['edges'])
        label='E'+str(len(selfint)+1)
        vals[label]=tuple(sum(vals[key][j] for key in centre) for j in (0,1))
        selfint[label]=-1
        for key in centre:
            if key in state['self']: selfint[key]-=1
            edges.add(frozenset((key,label)))
        if len(centre)==2: edges.remove(frozenset(centre))
        yield {'vals':vals,'self':selfint,'edges':edges}

level=[initial]; counts={}; examples=[]
for depth in range(1,5):
    level=[child for parent in level for child in next_states(parent)]
    counts[str(depth)]=len(level)
    for state in level:
        exc=sorted(state['self'])
        mat=S.Matrix([[state['self'][u] if u==v else int(frozenset((u,v)) in state['edges']) for v in exc] for u in exc])
        assert mat.det()==(-1)**depth
        for key in exc:
            av,bv=state['vals'][key]
            assert av>0 and bv>0
            assert S.factor(block.det().subs({a:av,b:bv}))!=0
        if depth==1:
            examples.append({'intersection_matrix':str(mat),'exceptional_valuations':state['vals']['E1'],'period_block_m1_n1':str(block.subs({a:1,b:1,m:1,n:1}))})

result={'status':'PASS','symbolic_exceptional_block':str(block),
        'symbolic_determinant':str(S.factor(block.det())),
        'labelled_blowup_sequences_by_exceptional_count':counts,
        'checked_sequences':sum(counts.values()),'first_blowup':examples[0],
        'bounded_first_character':'strict Q plus every exceptional curve; no strict R',
        'bounded_second_character':'full reduced boundary',
        'scope':'Finite exact audit plus symbolic block. General sheaf and all-length geometric proof is B.4.27; no unrestricted cap nonexistence claim.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
for key,value in result.items(): print(f'{key}: {value}')
