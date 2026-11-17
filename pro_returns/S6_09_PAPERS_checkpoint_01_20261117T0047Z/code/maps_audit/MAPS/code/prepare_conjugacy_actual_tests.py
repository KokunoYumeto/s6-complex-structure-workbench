"""Export exact admissible order-(5,4) tuples for the Julia conjugacy tests."""
from pathlib import Path
import json
import sympy as S
from fourfolds_family_survivors import family
from fourfolds_survivor_test import factors

root=Path(__file__).resolve().parents[1]
tuples=[]
for v in (0,1,2):
    A,B=family(v)
    A,B=A.T,B.T
    C=(A*B).inv()
    assert A**5==S.eye(6) and B**4==S.eye(6)
    assert (C-S.eye(6))**2==S.zeros(6)
    assert factors(C-S.eye(6))==[1,1,1]
    assert all(x.q==1 for M in (A,B,C) for x in M)
    tuples.append([[[str(int(x)) for x in row] for row in M.tolist()]
                   for M in (A,B,C)])
    print('Actual parameter',v,'orders5,4; primitive square-zero rank3 cusp: PASS;',
          'trace(M1*M2^3)=',int((A*B**3).trace()))
dest=root/'records/fourfolds_conjugacy_actual_inputs.toml'
dest.write_text('tuples = '+json.dumps(tuples)+'\n')
print('Exported3 actual admissible tuples.')
