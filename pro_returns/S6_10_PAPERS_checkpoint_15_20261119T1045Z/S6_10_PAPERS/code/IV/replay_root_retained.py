"""Run three byte-identical certificates; preserve all withdrawn-field notices."""
from pathlib import Path
import subprocess,hashlib,json,datetime
P=Path(__file__).resolve().parents[2]
S=P.parents[1]/'sources/newer_night/checkpoint29'
R=P/'code/IV/replay_root_retained'
files=['code/part3/order_one_pages.py','code/part3_fourfold/weighted_shorter_loop.py','code/part3_fourfold/os49_shorter_loop.py','code/part3/scalar_dependency_scope.py','code/part3/canonical_scalar_catalogue.json','records/scalar_fan_correction_scope.json']
inputs=[]
for rel in files:
 a=S/rel;b=R/rel;b.parent.mkdir(parents=True,exist_ok=True);raw=a.read_bytes();b.write_bytes(raw)
 assert hashlib.sha256(b.read_bytes()).digest()==hashlib.sha256(raw).digest()
 inputs.append({'path':rel,'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)})
(R/'records/literature_fourfold.md').touch(exist_ok=True)
runs=[]
for rel in files[:3]:
 start=datetime.datetime.now(datetime.timezone.utc).isoformat()
 proc=subprocess.run(['python',str(R/rel)],cwd=R,capture_output=True,text=True)
 out=R/(rel+'.stdout.txt');err=R/(rel+'.stderr.txt');out.write_text(proc.stdout);err.write_text(proc.stderr)
 generated=(R/rel).with_suffix('.json')
 rec={'program':rel,'started_at':start,'exit_code':proc.returncode,'stdout':str(out.relative_to(P)),'stderr':str(err.relative_to(P)),
      'output_sha256':hashlib.sha256(generated.read_bytes()).hexdigest() if generated.exists() else None,
      'scope':'Exact algebraic assertions only. Historical audit prose and withdrawn all-fan polynomial arithmetic in the unmodified output confer no geometric proof or return-value credit.'}
 runs.append(rec);print(rel,'exit',proc.returncode,flush=True)
record={'source_checkpoint':29,'all_pass':all(r['exit_code']==0 for r in runs),'inputs':inputs,'runs':runs,
        'reading_scope':'All three executed programs and their complete imported scalar-scope helper were read. All catalogue fields actually used by the polynomial verification were read; the untouched remainder and correction-ledger bytes were supplied as exact inputs without a whole-source reading claim.'}
(P/'analysis/IV_root_retained/certificate_replays.json').write_text(json.dumps(record,indent=2))
assert record['all_pass']
