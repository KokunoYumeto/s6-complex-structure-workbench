"""Apply six reviewed guards and one precisely scoped primary reference."""
from pathlib import Path
import datetime, hashlib, json, re

R = Path(__file__).resolve().parents[1]
sources = [
    'audit_p119_fresh/receiving_convention_guard_08.json',
    'audit_sign/UN24_UN39_source_code_guards_08.json',
]
before = {}; after = {}; receipts = []
for source in sources:
    packet = json.loads((R/source).read_text())
    target = packet.get('target', packet.get('path'))
    if target not in before:
        before[target] = (R/target).read_text(); after[target] = before[target]
    for guard in packet['guards']:
        old = guard.get('old_text', guard.get('old'))
        new = guard.get('new_text', guard.get('new'))
        assert after[target].count(old) == 1, (source, guard)
        after[target] = after[target].replace(old, new, 1)
    receipts.append({'source': source, 'sha256': hashlib.sha256((R/source).read_bytes()).hexdigest(),
                     'guards': packet['guards']})

packet = json.loads((R/sources[1]).read_text())
reference = packet['bibliography_additions'][0]
key = reference['key']
extra = R/'analysis/additional_references.bib'
old_extra = extra.read_text()
assert '{'+key+',' not in old_extra
bib_path = R/'analysis/source_bibliography_entries.json'
bib = json.loads(bib_path.read_text())
assert key not in bib
bib[key] = [{'paper': 'II', 'text': r'''\bibitem[Roulleau(2019)]{Roulleau2019GeneralizedKummer}
Xavier Roulleau.
\newblock On generalized Kummer surfaces and the orbifold Bogomolov--Miyaoka--Yau inequality.
\newblock \emph{Transactions of the American Mathematical Society}, 371(11):7651--7668, 2019.
\newblock \doi{10.1090/tran/7507}.
\newblock Verified in this writing on 20 November 2026 at these loci only.
Author-hosted original journal offprint: section 3.1, p.7659, complete ADE table and cyclic-source attribution;
section 4.1, Theorem 27 and its attribution, p.7663. Applied through the actual translation conjugacy,
quotient map, and local invariant maps. No opening of the cited Nikulin or Bertin originals is claimed.'''}]

for target, text in after.items():
    assert re.findall(r'\\(?:tag|label)\{[^}]+\}', before[target]) == re.findall(r'\\(?:tag|label)\{[^}]+\}', text)
    (R/target).write_text(text)
extra.write_text(old_extra.rstrip()+'\n\n'+reference['bibtex']+'\n')
bib_path.write_text(json.dumps(bib, indent=2, ensure_ascii=False)+'\n')
record = {
    'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'guards': 6, 'receipts': receipts, 'bibliography_key': key,
    'hashes': {p: {'before': hashlib.sha256(before[p].encode()).hexdigest(),
                   'after': hashlib.sha256(after[p].encode()).hexdigest()} for p in before},
    'scope': 'The P1.19 saved matrices use the plus cusp convention; the exact -I cap map relates the minus cone. UN24 and UN39 now cite the executed 607-check certificate with its exact determinant identification and opened primary inputs. No earlier proof-reading chronology is changed.',
    'pending': 'Assembly, build30 all five papers, current reference audit and changed-page actual visual inspection.'
}
(R/'analysis/convention_and_UN24_UN39_integration_08.json').write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps({'guards': 6, 'files': list(after), 'bibliography_key': key}))
