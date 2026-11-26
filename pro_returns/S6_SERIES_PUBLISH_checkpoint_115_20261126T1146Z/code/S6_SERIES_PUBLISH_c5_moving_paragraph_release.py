"""Release the individually owned moving-sphere paragraph after root review."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import csv,io,importlib.util

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('packets',ROOT/'agents/continuation4_iii_infra/S6_SERIES_PUBLISH_III_packets.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
source=mod.parse_allowed('III')
SOURCE='9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
assert source['sha256']==SOURCE
tag='036Z'; label='wb:cusp-cone-moving-S4-null-homotopy'
loc=source['labels'][label]
assert loc['line']==26663 and loc['locus']=='outside_statement_and_proof' and not loc['owner']
lines=source['text'].splitlines()
assert lines[26661].startswith(r'\paragraph{') and lines[26680].startswith(r'\paragraph{')
assert all(not x.strip() for x in lines[26674:26680])
argument='\n'.join(lines[26661:26674])
ARGUMENT='f43e992e3806617dfb946a7aae24078d40b0bd41f7925080da5582688490a30a'
assert sha256(argument.encode()).hexdigest()==ARGUMENT
assert argument.count(r'\label{')==1 and r'\label{'+label+'}' in argument
assert r'\begin{proof}' not in argument and r'\end{proof}' not in argument
assert sha256(('\n'.join(lines[26661:26680])+'\n').encode()).hexdigest()=='73c5e5cdc399531f2014d8764867611ead233b68ea6c97d0cbb6b105809893ff'
folder=ROOT/'agents/continuation5_iii_carriers'
prefix='S6_SERIES_PUBLISH_III_036Z_'
frozen={
 'fresh_derivation.md':'3dbb12cd1637c0983999e780ee35bb776b9a258e300fe49a7e922e52e91c50c3',
 'fresh_arithmetic.py':'1e9ddcc5b0d981fbde5c24c60af1eb9bc1099b92f8fae5a07debb91452ae080f',
 'fresh_arithmetic.out':'62510b8ddcc16b4822979e3568822fc585a73c591d21da017fb0138ee0ac892b'}
for suffix,digest in frozen.items():
 assert sha256((folder/(prefix+suffix)).read_bytes()).hexdigest()==digest
packet=ROOT/'agents/continuation5_iii_infra/S6_SERIES_PUBLISH_III_036Z_definition_inputs.tex'
assert sha256(packet.read_bytes()).hexdigest()=='48cbbe45d1a1063354951bd209c39e9bca0bad5563857742f528383edd3f2120'
completed='2026-11-24T01:32:31+00:00'
now=datetime.now(timezone.utc)
assert datetime.fromisoformat(completed)<now
stamp=now.isoformat(timespec='seconds').replace('+00:00','Z')
progress=ROOT/'S6_SERIES_PUBLISH_required_progress_III.tsv'
before=progress.read_bytes()
reader=csv.DictReader(io.StringIO(before.decode()),delimiter='\t')
fields=reader.fieldnames; rows=list(reader)
others=[dict(r) for r in rows if r['tag']!=tag]
r=next(r for r in rows if r['tag']==tag)
assert r['status']=='open' and not r['proof_released_utc']
dest=folder/(prefix+'released_argument.tex')
assert not dest.exists()
dest.write_text('% Root-authorized individual outside-paragraph argument release for036Z\n'
 '% III SHA256 '+SOURCE+'; release UTC '+stamp+'\n'
 '% Exact substantive scope26662--26674; argument SHA256 '+ARGUMENT+'\n'
 +argument+'\n',newline='\n')
r.update(source_owner=label,source_ownership_status='verified_exact_individual_scope',
 assigned_checker='fifth continuation carriers checker /root/iii_02ja',
 statement_packet=str(packet.relative_to(ROOT)),statement_status='bare_claims_reviewed',
 packet_status='fresh_written_original_comparison_pending',
 alias_clause_map='036Z owns only the complete outside paragraph26662--26674, label26663. Lines26675--26680 are blank. The separately owned036V proof ends26659;037K begins26681 and remains closed. The historical group is preserved; no other identity receives credit.',
 derivation_path=str((folder/(prefix+'fresh_derivation.md')).relative_to(ROOT)),
 derivation_sha256=frozen['fresh_derivation.md'],derivation_completed_utc=completed,
 proof_released_utc=stamp,released_source_sha256=SOURCE,released_proof_sha256=ARGUMENT,
 proof_status='released_after_derivation',
 root_release_authorization='Root fully read all91 safe-input lines, all294 frozen fresh-derivation lines, all135 new arithmetic lines and all11 output lines before this individual release. Exact quotient homotopies, endpoint/basepoint continuity, all native parameters, integer prism/fundamental-class maps and the restricted auxiliary metric scope were reviewed. Parser ownership and exact heading/blank boundaries prove the single13-line outside paragraph scope; the historical grouping grants no alias credit.',
 checker_exposure_note='Complete fresh derivation and genuinely new computation frozen before individual original paragraph exposure; exact original comparison remains pending.')
r['notes']+=' Individually released after root full fresh review; no required row closed. Exact outside-paragraph ownership was verified without altering the historical structural index.'
out=io.StringIO(newline='')
w=csv.DictWriter(out,fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
check=list(csv.DictReader(io.StringIO(out.getvalue()),delimiter='\t'))
assert [x for x in check if x['tag']!=tag]==others
assert progress.read_bytes()==before
progress.write_text(out.getvalue(),newline='\n')
print('Released036Z only at',stamp,'argument SHA256',ARGUMENT)
print('Exact13-line paragraph; all other rows, manuscript and historical index preserved.')
