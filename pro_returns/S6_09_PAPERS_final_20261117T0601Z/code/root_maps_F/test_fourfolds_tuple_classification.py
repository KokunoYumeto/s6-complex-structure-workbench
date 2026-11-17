"""Execute the public canonical-classifier entry point on the finite stratum."""
from pathlib import Path
import json
import sympy as S
from fourfolds_tuple_classification import canonical_tuple,admissible,FREE_LINEAR_ORDERS
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'records/fourfolds_involution_classes.json').read_text())
P=S.eye(6)
for i,j,a in ((0,4,11),(2,5,-7),(4,1,3)):
    E=S.eye(6);E[i,j]=a;P=E*P
keys=[]
for row in data['classes']:
    T=[S.Matrix(M) for M in row['matrices']]
    result=canonical_tuple([P*M*P.inv() for M in T])
    assert result['key']==row['key']
    assert result['representative']==row['matrices']
    keys.append(result['key'])
assert len(keys)==56
print('PUBLIC CANONICAL CLASSIFIER: all56 conjugated inputs returned their exact representatives.')
print('Executed method: complete involution normal form. General height-box fallback was not exhaustively run.')
print('Allowed finite linear orders with a free affine lift:',FREE_LINEAR_ORDERS)
(root/'records/fourfolds_tuple_classification_tests.json').write_text(json.dumps({'checked':56,'keys':keys,'general_height_box_exhausted':False},indent=2)+'\n')
