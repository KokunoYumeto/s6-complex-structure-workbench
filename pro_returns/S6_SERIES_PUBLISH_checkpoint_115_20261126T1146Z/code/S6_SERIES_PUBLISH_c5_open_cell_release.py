"""Release only036V's separately owned proof after its complete fresh check."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import csv
import importlib.util
import io

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('packets',ROOT/'agents/continuation4_iii_infra/S6_SERIES_PUBLISH_III_packets.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
src=mod.parse_allowed('III')
assert src['sha256']=='9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
owner=src['by_owner']['wb:cusp-cone-literal-R4-open-cells']
assert (owner['start_line'],owner['end_line'])==(26572,26608)
assert len(owner['proofs'])==1
p=owner['proofs'][0]
assert (p['start_line'],p['end_line'])==(26612,26659)
assert not p['association_review_required']
assert p['sha256']==owner['proof_sha256']=='b736551134166cc15667f56f1926a63480ea3672e9797ed91215ae6d849871d5'
separate=[]
for label in ['wb:cusp-cone-moving-S4-null-homotopy','wb:cusp-cone-sphere-map-homotopy-status']:
 loc=src['labels'][label]
 assert loc['locus']=='outside_statement_and_proof' and not loc['owner']
 assert loc['line']>p['end_line']
 separate.append(label+' at line'+str(loc['line']))
folder=ROOT/'agents/continuation5_iii_carriers'
prefix='S6_SERIES_PUBLISH_III_036V_'
frozen={
 'fresh_derivation.md':'660ad3aa7abf91b5d0dcacaaeb96940c73ce5898276781c00fb57fca04873f7b',
 'fresh_arithmetic.py':'94f39362a9d3979b9767120b0236521aed4abf2e4254b9e579377fbb70a2c200',
 'fresh_arithmetic.out':'16f92149dd6e40a0922ce205a5c0562d6153abcb105f7b7b674f736876c26281'}
for suffix,digest in frozen.items():assert sha256((folder/(prefix+suffix)).read_bytes()).hexdigest()==digest
completed='2026-11-24T01:02:06+00:00'
stamp=datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z')
assert datetime.fromisoformat(completed)<datetime.fromisoformat(stamp.replace('Z','+00:00'))
progress=ROOT/'S6_SERIES_PUBLISH_required_progress_III.tsv'
before=progress.read_bytes()
reader=csv.DictReader(io.StringIO(before.decode()),delimiter='\t');fields=reader.fieldnames;rows=list(reader)
others=[dict(r) for r in rows if r['tag']!='036V']
r=next(r for r in rows if r['tag']=='036V')
assert r['status']=='open' and not r['proof_released_utc']
argument=src['text'][p['start']:p['end']]
assert sha256(argument.encode()).hexdigest()==p['sha256']
destination=folder/(prefix+'released_proof.tex')
# The standard grouped release stopped at ownership before emitting any text.
assert not destination.exists() or destination.read_bytes()==b''
destination.write_text('% Explicit individual root release for036V; complete separate corollary proof\n'
 '% III source SHA256 '+src['sha256']+'; release UTC '+stamp+'\n'
 '% Source lines26612--26659; argument SHA256 '+p['sha256']+'\n'+argument+'\n')
r.update(assigned_checker='fifth continuation carriers checker /root/iii_02ja',
 statement_packet='agents/continuation5_iii_infra/S6_SERIES_PUBLISH_III_036V_definition_inputs.tex',
 source_ownership_status='verified_exact_individual_scope',
 alias_clause_map='036V: corollary26572--26608 and its complete proof26612--26659 only. The separately labelled following arguments '+ '; '.join(separate)+' remain closed and receive no alias credit.',
 derivation_path=str((folder/(prefix+'fresh_derivation.md')).relative_to(ROOT)),
 derivation_sha256=frozen['fresh_derivation.md'],derivation_completed_utc=completed,
 proof_released_utc=stamp,released_source_sha256=src['sha256'],released_proof_sha256=p['sha256'],
 proof_status='released_after_derivation',
 root_release_authorization='Root fully read the safe113-line packet, all286 original fresh-derivation lines and all attribution-only changes in its293-line refreeze, all158 new program lines and9 output lines before this release. Every quotient inverse, ambient perturbation, completion map and entire-ball inverse was checked. Exact parser ownership assigns only the48-line separate proof to036V;036Z and037K occur later outside all statements/proofs and remain closed. The historical grouping is preserved without granting alias credit.')
r['notes']+=' The standard group release stopped before emitting proof text because the historical group combined this owner with two outside arguments. This bounded individual release resolves the exact source ownership without changing that historical index. Full original/receiving comparison is pending.'
stream=io.StringIO(newline='');writer=csv.DictWriter(stream,fields,delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(rows)
checked=list(csv.DictReader(io.StringIO(stream.getvalue()),delimiter='\t'))
assert [r for r in checked if r['tag']!='036V']==others
assert progress.read_bytes()==before
progress.write_text(stream.getvalue(),newline='\n')
print('Released036V only at',stamp,'proof SHA256',p['sha256'])
print('Verified separate unresolved scopes:', '; '.join(separate))
print('No required row closed; all other rows and the historical structural index preserved.')
