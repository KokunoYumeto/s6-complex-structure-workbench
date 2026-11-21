from pathlib import Path
import json,hashlib,datetime
from S6_SERIES_PUBLISH_editing import Editor
r=Path(__file__).resolve().parents[1]
p=r/'agents/i_topology/editorial/S6_SERIES_PUBLISH_I_boundary_batch1_guarded.json'
d=json.loads(p.read_text());ed=Editor('I')
for x in d['patches']:
 ed.replace(x['old'],x['new'],x.get('type','D12'),x['reason'],x['id'],count=x.get('expected_count',1))
ed.replace(r'$p=-1$, $a=1$,.',r'$p=-1$, $a=1$.','D08',
 'Remove a punctuation artifact at the preserved standard specialization.','night:P2.3')
old='''and its second projection is the required holomorphic marked map.
\\end{enumerate}'''
new='''and its second projection is the required holomorphic marked map.
Resolve this reduced graph isomorphically over the smooth punctured
family by the same analytic resolution theorem. Composing its
holomorphic marked map with the resolution gives the asserted
smooth proper modification.
\\end{enumerate}'''
ed.replace(old,new,'D25',
 'Make the final graph resolution explicit in the general smooth-modification conclusion, using precisely the already verified analytic resolution theorem; the graph construction and scope remain unchanged.',
 'night:P2.4')
ed.save()
(r/'records/S6_SERIES_PUBLISH_I_boundary1_integration.json').write_text(json.dumps({
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'guard_path':str(p.relative_to(r)),'guard_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
 'root_review':'Complete agent comparison report and changed partial-filling, marked-extension, nonfilling, base-change and virtual-Euler passages read. The two long unchanged movement spans were not reread in full by root during integration; the agent records its complete affected-proof comparison. Final rendered reading remains open.',
 'scope':'No additional independent proof event from guard application or movement.',
 'root_changes':['Repair one punctuation artifact.','State explicitly the final resolution of the marked-map graph using the already cited analytic resolution input.']
},indent=2)+'\n')
