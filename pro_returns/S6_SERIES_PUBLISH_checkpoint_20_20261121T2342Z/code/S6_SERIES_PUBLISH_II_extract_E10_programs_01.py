"""Expose only the two E10 routines after its genuine derivation freeze."""
from pathlib import Path
import datetime,hashlib,json
R=Path(__file__).resolve().parents[1]
O=R/'agents/ii_checks_provenance/recovery_20261121T2000Z';rows=[]
specs=[('records/S6_SERIES_PUBLISH_II_opened_programs_recovery_01/E_checks.py','w=s.exp','mu,e1,e2,bb,x,y,r=',"import sympy as s\nt=s.symbols('t')\n\n",'hesse'),
 ('records/S6_SERIES_PUBLISH_II_E_counterexamples_01/E_counterexamples.py','# C is the genus-two double cover','# In the normalized lattice basis','', 'cohomology')]
for path,start,end,prefix,name in specs:
 p=R/path;s=p.read_text();a=s.index(start);b=s.index(end,a);body=prefix+s[a:b]
 out=O/f'S6_SERIES_PUBLISH_II_E10_prior_{name}_slice.py';assert not out.exists();out.write_text(body)
 rows.append(dict(source_path=path,source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),start_line=s[:a].count('\n')+1,end_line=s[:b].count('\n'),added_setup=prefix,slice_path=str(out.relative_to(R)),slice_sha256=hashlib.sha256(out.read_bytes()).hexdigest()))
record=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),slices=rows,scope='Exactly E10 Hesse critical values and negative-degree cohomology routine; E14 and all other shared routines remain closed to the checker.',check_events_added=0)
out=O/'S6_SERIES_PUBLISH_II_E10_prior_program_slices.json';assert not out.exists();out.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
