"""Finite exact cross-checks of the complete coefficient comparison proof."""
from pathlib import Path
from math import comb
import hashlib,json
W=Path(__file__).resolve().parents[1]
rows=[]
def check(name,truth):
    assert truth,name
    rows.append(name)
def relation(a,b):
    return {(a+b-c,c):(int(a%2==0 and b%2==0 and c%2==1))
            for c in range(a//2+1) if comb(b-1-c,a-2*c)%2}
check('Q2 Q2 retains one coefficient on Q3 Q1',relation(2,2)=={(3,1):1})
check('Q1 Q2 equals Q3 with coefficient one',relation(1,2)=={(3,0):0})
check('Q3 Q2 is zero including both zero binomial terms',relation(3,2)=={})
check('Q4 Q4 retains two differently weighted summands',relation(4,4)=={(7,1):1,(6,2):0})
for b in range(1,17):
    for a in range(1,2*b):
        for c in range(a//2+1):
            coef=comb(b-1-c,a-2*c)%2
            e=int(a%2==0 and b%2==0 and c%2==1)
            check(f'Adem original weights a={a},b={b},c={c}',
                  coef==0 or e+(a+b-c)//2+c//2==a//2+b//2)
for i in range(1,9):
    wh=2**(i-1)-1
    check(f'dual generator {i} keeps weight',-wh+wh==0)
    for k in range(1,i):
        exp=(2**(i-1)-1)+2**(k-1)*(1-2**(i-k))+(1-2**(k-1))
        check(f'full coproduct coefficient i={i},k={k}',exp==0)
        source_weight=2**k*(2**(i-k-1)-1)+(2**(k-1)-1)-(2**(i-1)-1)
        check(f'DI full interior coefficient i={i},k={k}',source_weight==-2**(k-1))
    for r in range(17):
        check(f'full original basis coefficient i={i},r={r}',
              r*wh+r//2==(r*(2**i-1))//2)
# Counterexamples distinguish the source's inconsistent convention, not just the corrected formula.
check('negative cohomological power for Q2 has wrong weight',-1!=1)
check('source odd-index formula maps Q1 to nonzero coefficient weight',-1!=0)

import runpy
ns=runpy.run_path(str(W/'checks/calculate_original_coefficient_h28.py'))
for row in ns['rows']:
    key='weight '+str(row['weight'])
    d1=row['d1_columns_binary'];d2=row['d2_columns_binary']
    c1=row['d1_rank_witness'];c2=row['d2_rank_witness'];j=row['cycle_column']
    ell=row['nonboundary_functional_binary']
    check(key+' first nonzero original minor',ns['determinant_mod2'](c1['minor_rows_binary'])==1)
    check(key+' second nonzero original minor',ns['determinant_mod2'](c2['minor_rows_binary'])==1)
    check(key+' full differential composition',all(ns['apply'](d2,c)==0 for c in d1))
    check(key+' exact original cycle',d2[j]==0)
    check(key+' nonboundary functional on image',all((ell&c).bit_count()%2==0 for c in d1))
    check(key+' nonboundary functional on cycle',(ell>>j)&1==1)
    check(key+' exact rank dimension sum',row['dimensions']['2']==c1['rank_lower_bound']+c2['rank_lower_bound']+1)
check('Exercise 7.2 complete first matrix',ns['rows'][4]['d1_columns_binary']==[29,0])
check('Exercise 7.2 complete second matrix',ns['rows'][4]['d2_columns_binary']==[2,3,0,4,6])

note=W/'src/coefficient-rings-and-the-original-degree-six-class.md'
report=dict(passed=len(rows),source_sha256=hashlib.sha256(note.read_bytes()).hexdigest(),
            checks=rows,scope='Finite integer/binomial cross-checks. Complete all-index parity, presentation, inverse, coproduct, grading and original coefficient proofs are in the chapter; the full matrix certificate and both exercise matrices are included. No topological-operation or Adams-convergence certification.')
(W/'checks/COEFFICIENT_RING_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='checks'}))
