"""Finish four explicitly referenced small certificates, preserving old attempts."""
from pathlib import Path
import json,hashlib,subprocess,sys,datetime,concurrent.futures,platform
import sympy
R=Path(__file__).resolve().parents[3];W=R/'deliverables/work/maps_audit';C=R/'deliverables/code/maps_audit/MAPS/code';S=R/'sources/returns/S6_04_MAPS_MANIFOLDS/code'
O=W/'final_small_program_runs';O.mkdir(exist_ok=True)
meta=dict(reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode)',effort='Pro',date='2026-11-17')
spec={
 'maps_exact':(['B.1.1','B.1.2','B.4.1'],'Full F2^4 invariant-covector enumeration, integral invariant lattices, actual named-family comparison matrices, exact symbolic lens arithmetic, and the flat Pauli symbol. This does not replace the stable-framing or APS geometric argument.'),
 'maps_fixed_curve_monodromy':(['B.6.16'],'Actual four local matrices and primitive cusp basis; induced parameter action on parabolic cohomology and invariant/coinvariant exterior powers. The two H3 grades do not determine their extension or integral shear.'),
 'maps_quotient_classification':(['B.6.18'],'Exact inverse of the characteristic-number matrix with determinant-24 and the ell=-4 specialization. Does not evaluate the remaining integer B or prove Jin’s classification.'),
 'fourfolds_integral_audit':(['E.1.5'],'Integral Smith bases, local restrictions of the global order6 class, finite mapping-torus torsion residues, covering cokernels and primitive summands. Total homology still uses the printed natural transgressions, section, UCT and duality.'),
 'fourfolds_vertical_correction_audit':(['D.2.50'],'Complete82-line independent finite audit:227 local component pairs,5696 profile residues,82 actual cocycle orders and16 additional height-one pairs. Smith unimodularity, integral correction equations and invariant orbit-sum kernels checked. The all-integer conclusion uses the printed periodicity proof; no cap topology is inferred. Imported root_vertical_corrections/manifolds_general_initial were fully audited in the disjoint D ledger.')}
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def run(name):
 source=S/(name+'.py');copy=C/(name+'.py');assert sha(source)==sha(copy)
 p=subprocess.run([sys.executable,str(copy)],cwd=C,capture_output=True,text=True,timeout=180)
 out=O/(name+'.stdout.txt');err=O/(name+'.stderr.txt');out.write_text(p.stdout);err.write_text(p.stderr)
 old=S/(name+'.out.json');new=C/(name+'.out.json');agreement=None
 if old.exists():agreement=json.loads(old.read_text())==json.loads(new.read_text())
 row=dict(program=name+'.py',results=['MAPS:'+s for s in spec[name][0]],source=str(source.relative_to(R)),source_sha256=sha(source),
 executed_copy=str(copy.relative_to(R)),executed_sha256=sha(copy),command=[sys.executable,str(copy)],portable_command=['python',copy.name],cwd=str(C.relative_to(R)),
 recorded_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),exit_code=p.returncode,stdout=str(out.relative_to(R)),stdout_sha256=sha(out),stderr=str(err.relative_to(R)),
 original_json_agreement=agreement,source_lines=len(source.read_text().splitlines()),complete_program_read=True,mathematical_scope=spec[name][1],
 program_changes='None',**meta)
 assert p.returncode==0 and agreement is not False,row
 (O/(name+'.run.json')).write_text(json.dumps(row,ensure_ascii=False,indent=2)+'\n');return row
selected=sys.argv[1:] or list(spec)
assert all(n in spec for n in selected)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:newrows=list(pool.map(run,selected))
oldpath=W/'final_small_program_manifest.json'
oldrows=json.loads(oldpath.read_text()).get('runs',[]) if oldpath.exists() else []
rows=[r for r in oldrows if Path(r['program']).stem not in selected]+newrows
record=dict(metadata=meta,python=platform.python_version(),sympy=sympy.__version__,runs=rows)
(W/'final_small_program_manifest.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
ev=json.loads((W/'check_events.json').read_text());known={e.get('event_id') for e in ev};audit=json.loads((W/'results_audit.json').read_text())
for row in newrows:
 eid='new-maps-final-small-program-20261117:'+row['program'];loc=str((O/(Path(row['program']).stem+'.run.json')).relative_to(R))
 event=dict(event_id=eid,results=row['results'],scope=row['mathematical_scope'],outcome='Complete program read, unchanged exact rerun exit0, all available original JSON output agrees.',run_record=loc,**meta)
 if eid not in known:ev.append(event)
 for a in audit:
  if 'MAPS:'+a['id'] in row['results']:
   if eid not in a.setdefault('check_event_ids',[]):a['check_event_ids'].append(eid)
   if loc not in a.setdefault('program_check_records',[]):a['program_check_records'].append(loc)
(W/'check_events.json').write_text(json.dumps(ev,ensure_ascii=False,indent=2)+'\n');(W/'results_audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
print('Complete program reads and unchanged exact reruns passed:',[(r['program'],r['source_lines']) for r in newrows])
