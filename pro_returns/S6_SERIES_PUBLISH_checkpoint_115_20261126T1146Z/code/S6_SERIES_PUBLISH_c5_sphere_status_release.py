"""Release the individually owned sphere-status paragraph after root review."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import csv, io, importlib.util

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('packets', ROOT/'agents/continuation4_iii_infra/S6_SERIES_PUBLISH_III_packets.py')
mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
source = mod.parse_allowed('III')
SOURCE = '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
assert source['sha256'] == SOURCE
tag = '037K'; label = 'wb:cusp-cone-sphere-map-homotopy-status'
loc = source['labels'][label]
assert loc['line'] == 26682 and loc['locus'] == 'outside_statement_and_proof' and not loc['owner']
lines = source['text'].splitlines()
assert lines[26680].startswith(r'\paragraph{') and lines[26708].startswith(r'\begin{')
assert all(not x.strip() for x in lines[26703:26708])
argument = '\n'.join(lines[26680:26703])
ARGUMENT = '24dfffbb91fc9acc05da778465a31da8fc54f8d28a5d749c8b0acd1ccf7c9fe5'
assert sha256(argument.encode()).hexdigest() == ARGUMENT
assert argument.count(r'\label{') == 1 and r'\label{'+label+'}' in argument
assert r'\begin{proof}' not in argument and r'\end{proof}' not in argument
assert sha256(('\n'.join(lines[26680:26708])+'\n').encode()).hexdigest() == 'db5fa4362db1f34bf1756cc535eb044a67ba99a5a3539cb14ab63e7f2a7e94a8'
folder = ROOT/'agents/continuation5_iii_carriers'
prefix = 'S6_SERIES_PUBLISH_III_037K_'
frozen = {
    'fresh_derivation.md': '13a587f03ed9baaab133652bcd5c4882782fd5fd8fa578cbd722b5cd4600a230',
    'fresh_arithmetic.py': '01b85352ee94e7053a0da8391ee2601f0cf8b4ab2e63646e8bbde5c15a2d41ef',
    'fresh_arithmetic.out': 'fb55c6f934d7a7aa87f4a5e41efdd21c847f904cb81df989170b585c3090fa1c',
}
for suffix, digest in frozen.items():
    assert sha256((folder/(prefix+suffix)).read_bytes()).hexdigest() == digest
packet = ROOT/'agents/continuation5_iii_infra/S6_SERIES_PUBLISH_III_037K_definition_inputs.tex'
assert sha256(packet.read_bytes()).hexdigest() == 'e5d99b9215504f3cad707aaec8366b3d72951bc962cdc0693e56191f39e41154'
completed = '2026-11-24T01:49:28+00:00'
now = datetime.now(timezone.utc)
assert datetime.fromisoformat(completed) < now
stamp = now.isoformat(timespec='seconds').replace('+00:00', 'Z')
progress = ROOT/'S6_SERIES_PUBLISH_required_progress_III.tsv'
before = progress.read_bytes()
reader = csv.DictReader(io.StringIO(before.decode()), delimiter='\t')
fields = reader.fieldnames; rows = list(reader)
others = [dict(r) for r in rows if r['tag'] != tag]
r = next(r for r in rows if r['tag'] == tag)
assert r['status'] == 'open' and not r['proof_released_utc']
dest = folder/(prefix+'released_argument.tex')
assert not dest.exists()
dest.write_text('% Root-authorized individual outside-paragraph argument release for037K\n'
    '% III SHA256 '+SOURCE+'; release UTC '+stamp+'\n'
    '% Exact substantive scope26681--26703; argument SHA256 '+ARGUMENT+'\n'
    +argument+'\n', newline='\n')
r.update(source_owner=label, source_ownership_status='verified_exact_individual_scope',
    assigned_checker='fifth continuation carriers checker /root/iii_02ja',
    statement_packet=str(packet.relative_to(ROOT)), statement_status='bare_claims_reviewed',
    packet_status='fresh_written_original_comparison_pending',
    alias_clause_map='037K owns only the complete outside paragraph26681--26703, label26682. Lines26704--26708 are blank and the next environment starts26709. The separate036V and036Z scopes receive no alias credit. The historical grouping is preserved.',
    derivation_path=str((folder/(prefix+'fresh_derivation.md')).relative_to(ROOT)),
    derivation_sha256=frozen['fresh_derivation.md'], derivation_completed_utc=completed,
    proof_released_utc=stamp, released_source_sha256=SOURCE, released_proof_sha256=ARGUMENT,
    proof_status='released_after_derivation',
    root_release_authorization='Root fully read all86 safe-input lines, all341 frozen fresh-derivation lines, all140 new arithmetic lines and all11 output lines before this individual release. Exact native projection/character and quotient marking inverses identify the one-copy maps with admitted02Q7; the based homotopies descend continuously for every positive smash power. All actual homological/cohomological grades, Hurewicz arrows, equal-dimensional degree definition, singular prism signs and tensor identities were reviewed. Parser ownership and heading/blank boundaries prove the exact23-line individual paragraph. No historical grouping supplies alias credit.',
    checker_exposure_note='Complete fresh derivation and genuinely new computation frozen before either original037K or released036Z paragraph exposure. Root fully reviewed fresh037K before its individual release; the original comparison remains pending.')
r['notes'] += ' Individually released after root full fresh review; no required row closed. Exact outside-paragraph ownership was verified without altering the historical structural index.'
out = io.StringIO(newline='')
w = csv.DictWriter(out, fields, delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(rows)
check = list(csv.DictReader(io.StringIO(out.getvalue()), delimiter='\t'))
assert [x for x in check if x['tag'] != tag] == others
assert progress.read_bytes() == before
progress.write_text(out.getvalue(), newline='\n')
print('Released037K only at', stamp, 'argument SHA256', ARGUMENT)
print('Exact23-line paragraph; all other rows, manuscript and historical index preserved.')
