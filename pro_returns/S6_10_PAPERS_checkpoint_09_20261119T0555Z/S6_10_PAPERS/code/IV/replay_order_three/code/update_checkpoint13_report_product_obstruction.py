"""Register K47 and clarify the proved scope of K29's product argument."""
from datetime import datetime, timezone
from pathlib import Path
import ast
import json
import shutil

root=Path(__file__).resolve().parents[1]
p=root/'code/update_report.py'
s=p.read_text().replace('P3K.40–P3K.46','P3K.40–P3K.47')
old=('The separate nonfixed-edge integer and the general source-loop fan '
     'formula remain under proof.')
new=('P3K.47 proves that the entire labelled three-curve plumbing has no '
     'periodic smooth product intertwining the physical delta action: the '
     'actual endpoint winding equations leave the determinant obstruction '
     'wind(kappa)+2wind(alpha)-wind(eta)=-6, even for arbitrary GL(2,C) '
     'normal derivatives. This identifies the failed hypothesis in the '
     'attempted direct use of the scalar-loop simultaneous product. The '
     'separate nonfixed-edge integer and the general source-loop fan '
     'formula remain under proof.')
assert s.count(old)==2
s=s.replace(old,new)
ast.parse(s)
p.write_text(s)

path=root/'notes/part3_common_exterior_meridians.tex'
original=path.read_text()
old=('In a fan retaining the physical delta edge, the actual relative\n'
     'return has variation')
new=('For the scalar-parameter families and the extending cusp products\n'
     'of K22--27, in a fan retaining the physical delta edge the actual\n'
     'relative return has variation')
assert original.count(old)==1
preserved=root/'code/part3_root/attempts/K29_scalar_product_scope'
preserved.mkdir(parents=True,exist_ok=True)
assert not (preserved/path.name).exists()
shutil.copy2(path,preserved/path.name)
path.write_text(original.replace(old,new))
record={
 'utc':datetime.now(timezone.utc).isoformat(),
 'included':'P3K.47',
 'root_audit':'records/root_audit_P3K_47.json',
 'peer_audits':'records/k47_peer_audits.json',
 'standalone_qa':'records/k47_standalone_visual_qa.json',
 'scope_clarification': 'K29 statement now explicitly names the scalar-parameter families and cusp products of K22-27 used in its proof. Its common-exterior meridian maps are unchanged; K31 already states its precise scalar-family scope.',
 'preserved_K29':'code/part3_root/attempts/K29_scalar_product_scope/part3_common_exterior_meridians.tex',
 'numerical_returns_changed':False
}
(root/'records/checkpoint13_product_obstruction_inclusion.json').write_text(json.dumps(record,indent=2)+'\n')
print('Registered K47 and made the existing K29 product scope explicit.')
