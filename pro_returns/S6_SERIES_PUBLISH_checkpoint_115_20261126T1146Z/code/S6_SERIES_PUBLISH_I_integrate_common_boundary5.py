from pathlib import Path
import json,re,hashlib,datetime
from S6_SERIES_PUBLISH_editing import Editor
r=Path(__file__).resolve().parents[1];ed=Editor('I');sources=[]
for rel,key in [('agents/i_topology/editorial/S6_SERIES_PUBLISH_I_boundary_batch5_guarded.json','patches'),('agents/i_provenance/S6_SERIES_PUBLISH_I_common_family_guards.json','changes')]:
 p=r/rel;d=json.loads(p.read_text())
 for x in d[key]:
  new=x['new']
  new=re.sub(r'(\\hypertarget\{tag-(IP(?:09|10|11))\}\{\}\\label\{([^}]+)\})',lambda m:m[1]+'\n'+r'\StatementRecord{'+m[3]+r'}{proved}{'+m[2]+r'}{}',new)
  ed.replace(x['old'],new,x.get('type','D12'),x['reason'],x['id'],count=x.get('expected_count',1))
 sources.append({'path':rel,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'guards':len(d[key])})
ed.replace(r'''This proves the necessity outside the specified exceptional set; \ref{fam:src:A.2.1} proves the necessity also on that set.''',
 r'''This proves parameter recovery from the two Albanese invariants outside the specified exceptional set. For biholomorphic total spaces, \cref{fam:src:A.2.1} gives the parameter congruence at every point.''',
 'D02','State exactly which hypothesis gives each parameter implication; the centralizer theorem takes a total-space biholomorphism as its input. The generic Albanese-recovery statement is unchanged.','fam:src:A.4.1')
ed.replace(r'$\mathfrak B_{k,l}=\Pp(3k,4l)$ the actual root lift satisfies',
 r'$\mathfrak B_{k,l}=\Pp(3k,4l)$, the vertical root bundle $E$ and the root lift satisfy',
 'D18','Identify the main theorem bundle with the vertical root bundle E in its supplying tangent theorem.','series:I:E')
ed.replace(r' \mathcal E=\mathcal O\oplus\mathcal O(-z_0),\quad',r' E=\mathcal O\oplus\mathcal O(-z_0),\quad',
 'D18','Use the same E as the supplying root tangent theorem; reserve mathcal E for the logarithmic cotangent bundle.','series:I:E')
ed.replace(r'At the value $h=1$ of Proposition~\ref{inv:A3.1},  The totals are',r'At the value $h=1$ of Proposition~\ref{inv:A3.1}, the totals are',
 'D08','Correct the joined sentence.','inv:C2.1')
ed.save()
(r/'records/S6_SERIES_PUBLISH_I_common_boundary5_integration.json').write_text(json.dumps({
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sources':sources,
 'root_review':'Read every complete proposed new passage, boundary5 full comparison, and common full scoped reread receipt. Agents compared all affected old/new proofs. Root integration creates no additional independent mathematical credit.',
 'root_variations':['Print tags IP09--IP11.','Distinguish the exact hypothesis maps in the final Albanese-recovery sentence.','Identify E in main E with the supplying vertical root bundle, by the identity of its definition.','Fix one joined sentence.'],
 'source_sha256':hashlib.sha256(ed.text.encode()).hexdigest()},indent=2)+'\n')
