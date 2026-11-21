from pathlib import Path
import json,hashlib,datetime
from S6_SERIES_PUBLISH_editing import Editor
r=Path(__file__).resolve().parents[1]
p=r/'agents/i_topology/editorial/S6_SERIES_PUBLISH_I_boundary_batch3_guarded.json'
d=json.loads(p.read_text());ed=Editor('I')
for x in d['patches']:
 ed.replace(x['old'],x['new'],x.get('type','D12'),x['reason'],x['id'],count=x.get('expected_count',1))
ed.replace('''On the core the same conclusion is immediate from
flatness of $S\\to B$.''','''On the core the total space is an open subset of $L\\times\\Delta_u$
and is smooth; joint flatness follows from that of $S\\to B$.''',
 'D25','Specify separately the smooth total-space chart and the joint flatness input; both were part of the same plumbing construction.','push:src:A.1.2')
ed.replace('''the usual small resolution of $xy=uzv$ for $u\\ne0$. For $u\\ne0$, put $Y=y/u$, so the equation is $xY=zv$.''',
 '''the small resolution of $xy=uzv$ for $u\\ne0$. Put $Y=y/u$, so the equation is $xY=zv$.''',
 'D08','Remove a repeated local-domain phrase after the exact chart correction.','push:src:A.1.2')
ed.replace('''curve intrinsically in the selected toric model. It is not the
$e_2$-direction curve fixed by $\\operatorname{Aut}^0$.''',
 '''curve in the selected toric model. The fixed double curve of
Proposition~\\ref{mapsI:src:A.1.2} has direction $e_2$ in the same
marked lattice; the two primitive directions satisfy
$\\det(e_1-e_2,e_2)=1$.''',
 'D02','State the exact common-lattice direction comparison and its unimodular determinant.','push:src:A.1.2')
ed.save()
(r/'records/S6_SERIES_PUBLISH_I_boundary3_integration.json').write_text(json.dumps({
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'guard_path':str(p.relative_to(r)),
 'guard_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
 'root_review':'Read full batch3 comparison and every proposed new passage, including complete combined compact/local plumbing and selected-diagonal correction, normalization algorithm, and modified-pinch topology. Read provenance complete strict A1.1/A1.2 comparison and exact correction guard. Agent records complete old/new comparisons; root does not claim a fresh independent plumbing derivation.',
 'mathematical_correction':'Old small-resolution coordinate choice selected the other diagonal. The exact corrected charts and transition are supplied by the frozen provenance derivation and its fresh calculation, with unchanged theorem. The separate error record gives the common Segre resolution and both projection maps.',
 'root_variations':['State smoothness of the core from its open total-line-bundle chart and flatness from the surface fibration separately.','Remove repeated phrase.','Give explicit determinant for the two marked curve directions.'],
 'scope':'Integration creates no additional independent proof event.'},indent=2)+'\n')
