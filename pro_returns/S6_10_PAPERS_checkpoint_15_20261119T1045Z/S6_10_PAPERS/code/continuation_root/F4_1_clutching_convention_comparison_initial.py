"""Fresh post-target exact comparison of the two clutching bases."""
from pathlib import Path
import json, datetime
from sympy import Matrix, eye

T=Matrix([[0,-1],[-1,0]])
root=Matrix([[1,-1],[2,2]])
former=Matrix([[1,-1],[-2,-2]])
checks={
    'integral_involution':T*T==eye(2),
    'unimodular_basis_change':T.det()==-1,
    'actual_euler_pontryagin_map':former*T==root,
    'inverse_coordinate_map':T*root.inv()==former.inv(),
}
assert all(checks.values())
result={'timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'chronology':'Written and run after target comparison; no prereading claim.',
 'checks':checks,'status':'passed','T':T.tolist(),'root_map':root.tolist(),
 'former_map':former.tolist()}
dest=Path(__file__).with_suffix('.output.json')
dest.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
