"""Complete identity-insertion branch and a genuine order-one gluing input."""
from pathlib import Path
import json
import sympy as S
from fourfolds_tuple_classification import canonical_tuple
from fourfolds_classify_gluing import genuine_data

root=Path(__file__).resolve().parents[1]
data=json.loads((root/'records/fourfolds_involution_classes.json').read_text())
P=S.eye(6)
for i,j,a in ((0,4,11),(2,5,-7),(4,1,3)):
    E=S.eye(6);E[i,j]=a;P=E*P
count=0
for row in data['classes']:
    for position in range(3):
        T=[S.Matrix(M) for M in row['matrices']]
        T.insert(position,S.eye(6))
        result=canonical_tuple([P*M*P.inv() for M in T])
        assert result['identity_site']==position
        expected=list(row['matrices']);expected.insert(position,S.eye(6).tolist())
        assert result['representative']==expected
        R=S.Matrix(result['conjugator'])
        assert abs(R.det())==1 and all(R*(P*M*P.inv())==S.Matrix(N)*R
                                      for M,N in zip(T,expected))
        count+=1
print('ALL168 CONJUGATED IDENTITY-INSERTION INPUTS NORMALIZED EXACTLY',flush=True)
original=json.loads((root/'records/fourfolds_marked_involution_input.json').read_text())
sample=dict(original);w=S.Matrix([0,1,0,1,0,0]);suffix=S.Matrix(original['matrices'][1])
sample['matrices']=original['matrices'][:1]+[S.eye(6).tolist()]+original['matrices'][1:]
sample['numerators']=original['numerators'][:1]+[[int(x) for x in w]]+original['numerators'][1:]
sample['orders']=[4,1,4]
sample['local_bases']=original['local_bases'][:1]+[S.eye(6).tolist()]+original['local_bases'][1:]
sample['clutch']=[int(x) for x in -suffix.inv()*w]
reduced=genuine_data(sample)
for name in ('matrices','numerators','orders','clutch','cusp_marking','local_bases'):
    assert reduced[name]==original[name],name
(root/'records/fourfolds_marked_order_one_input.json').write_text(json.dumps(sample,indent=2,default=int)+'\n')
(root/'records/fourfolds_identity_classification_tests.json').write_text(json.dumps(
    {'normalizations':count,'identity_positions':[0,1,2],
     'order_one_nonzero_numerator':sample['numerators'][1],
     'original_clutch':sample['clutch'],'reduced_clutch':reduced['clutch']},indent=2)+'\n')
print('NONZERO ORDER-ONE NUMERATOR/SUFFIX CLUTCH COMPARISON PASSED',flush=True)
