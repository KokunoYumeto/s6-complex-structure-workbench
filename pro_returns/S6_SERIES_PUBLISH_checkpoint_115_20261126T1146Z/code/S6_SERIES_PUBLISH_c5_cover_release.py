#!/usr/bin/env python3
"""Release three individually reviewed, precisely bounded cusp-cover arguments.

The historical metadata group is retained unchanged. Its theorem-proof owner
does not describe the two subsequent outside-environment argument paragraphs.
This root-reviewed release binds each actual argument separately in live rows.
"""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import csv
import importlib.util

ROOT=Path(__file__).resolve().parents[1]
PACK=ROOT/'agents/continuation4_iii_infra/S6_SERIES_PUBLISH_III_packets.py'
spec=importlib.util.spec_from_file_location('reviewed_packets',PACK)
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
src=mod.parse_allowed('III')
assert src['sha256']=='9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
folder=ROOT/'agents/continuation5_iii_carriers'
specs={
 '037X':('c8541a57cb1ab5d2c6225cba13d2a6374c6d5c51ae63c80ea198fb6ab59c0e0e',23788,24094,'complete separate theorem proof'),
 '037Y':('2d6536d547a39e4d340913fc4be108b1caafd6079dd4d6ca790cc31fca2307cd',24117,24131,'complete outside-environment Exact scope paragraph'),
 '0382':('7609b0506fca1d615912362e9beead7782cec65cc1dc5702458916707834e246',24097,24110,'complete outside-environment action-comparison paragraph'),
}
progress=ROOT/'S6_SERIES_PUBLISH_required_progress_III.tsv'
before=progress.read_bytes()
with progress.open(newline='') as stream:
    reader=csv.DictReader(stream,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
stamp=datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z')
lines=src['text'].splitlines(keepends=True)
for tag,(expected,first,last,scope) in specs.items():
    row=next(r for r in rows if r['tag']==tag)
    assert row['status']=='open' and not row['proof_released_utc']
    derivation=folder/f'S6_SERIES_PUBLISH_III_{tag}_fresh_derivation.md'
    assert sha256(derivation.read_bytes()).hexdigest()==expected
    assert '2026-11-23T21:14:04Z' in derivation.read_text()
    program=folder/f'S6_SERIES_PUBLISH_III_{tag}_fresh_arithmetic.py'
    output=program.with_suffix('.out')
    assert program.is_file() and 'ALL FRESH '+tag+' ARITHMETIC PASSED' in output.read_text()
    assert datetime.fromisoformat('2026-11-23T21:14:04+00:00')<datetime.fromisoformat(stamp.replace('Z','+00:00'))
    if tag=='037X':
        owner=src['by_owner'][row['label']]
        assert len(owner['proofs'])==1
        proof=owner['proofs'][0]
        assert (proof['start_line'],proof['end_line'])==(first,last)
        argument=src['text'][proof['start']:proof['end']]
        assert sha256(argument.encode()).hexdigest()==owner['proof_sha256']
    else:
        argument=''.join(lines[first-1:last])
        assert '\\label{'+row['label']+'}' in argument
        assert argument.startswith('\\paragraph{')
        assert '\\begin{proof}' not in argument and '\\end{proof}' not in argument
    argument_hash=sha256(argument.encode()).hexdigest()
    destination=folder/f'S6_SERIES_PUBLISH_III_{tag}_released_proof.tex'
    assert not destination.exists()
    destination.write_text('% Explicit individual root release: '+tag+'; '+scope+'\n'
        +'% III source SHA256 '+src['sha256']+'; release UTC '+stamp+'\n'
        +f'% Exact source lines {first}--{last}; argument SHA256 {argument_hash}\n'+argument+'\n')
    row.update(derivation_path=str(derivation.relative_to(ROOT)),derivation_sha256=expected,
        derivation_completed_utc='2026-11-23T21:14:04Z',proof_released_utc=stamp,
        released_source_sha256=src['sha256'],released_proof_sha256=argument_hash,
        proof_status='released_after_derivation',
        source_ownership_status='verified_exact_individual_scope',
        root_release_authorization=('Root read all 366, 111 and 138 lines of the three frozen derivations and every line of all three new arithmetic programs and outputs before this release. The complete fan-chart, invariant-ring, local-length, compatible-disc, period/clutch, original-base monodromy and holomorphic-character arguments have been reviewed. Each tag is bound only to its own '+scope+f' at current source lines {first}--{last}; historical metadata grouping gives no alias credit. Root was previously exposed; fresh credit belongs to the unexposed carriers checker.'))
    row['notes']+=' Individual bounded argument release; original structural index preserved. Complete old/new comparison and receiving-proof review still pending.'
    print(tag,scope,'lines',first,last,'argument SHA256',argument_hash,'release UTC',stamp)
assert progress.read_bytes()==before
with progress.open('w',newline='') as stream:
    writer=csv.DictWriter(stream,fields,delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(rows)
print('All three rows remain open. Each completed fresh derivation predates its individual argument release.')
