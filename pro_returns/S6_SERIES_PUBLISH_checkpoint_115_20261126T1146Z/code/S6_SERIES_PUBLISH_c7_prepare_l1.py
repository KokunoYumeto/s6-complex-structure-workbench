"""Resolve the held L1 statement without exposing its original proof."""
import csv
import hashlib
import io
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
source=ROOT/'S6_SERIES_PUBLISH_III.tex'
raw=source.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
index=json.loads((ROOT/'agents/continuation4_iii_infra/S6_SERIES_PUBLISH_III_packet_structure.json').read_text())
g=next(g for g in index['metadata_groups'] if g['candidate_tags']==['02L1'])
assert g['statement_lines']==[12740,12835]
lines=raw.decode().splitlines()
statement='\n'.join(lines[12739:12835])
assert statement.startswith(r'\begin{theorem}') and statement.endswith(r'\end{theorem}')
assert r'\begin{proof}' not in statement
claim='\n'.join(line for line in statement.splitlines() if not line.startswith(r'\StatementRecord'))
folder=ROOT/'agents/continuation7_iii_nonstar'
folder.mkdir(exist_ok=True)
packet=folder/'S6_SERIES_PUBLISH_III_02L1_claim.tex'
assert not packet.exists()
header=('% Complete target statement, manually reviewed as claims to verify.\n'
        '% Canonical III lines12740--12835; only the machine StatementRecord line is omitted.\n'
        '% Original proof lines12838--13019 remain embargoed. No old program or output is an input.\n'
        '% All displayed finite presentations, counts and smooth identifications are target conclusions.\n')
packet.write_text(header+claim+'\n',newline='\n')
progress=ROOT/'S6_SERIES_PUBLISH_required_progress_III.tsv'
with progress.open(newline='') as f:
    reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
row=next(r for r in rows if r['tag']=='02L1')
assert row['status']=='open' and row['proof_status']=='embargoed'
row.update(statement_packet=str(packet.relative_to(ROOT)),
           statement_status='complete_target_claim_statement_manually_reviewed',
           packet_status='target_statement_resolved_inputs_open',
           unresolved_inputs='KX natural necessity/local-defect and L0 many-site proof remain in fresh derivation; exact finite-cap inputs must also be derived')
row['notes']+=' Continuation-seven root read only the full theorem statement at12740--12835. Its presentation and parameter assertions are target claims, not an embedded proof. Complete claim packet staged; no original proof released, no fresh or closure credit.'
b=io.StringIO(newline='');w=csv.DictWriter(b,fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
progress.write_text(b.getvalue(),newline='\n')
assert source.read_bytes()==raw
print('L1 full claim statement staged; original proof remains embargoed; no required row closed.')
print('Target claims include59 patterns/50 initial rows, exact all-order finite/regular presentations, and oriented smooth scope.')
