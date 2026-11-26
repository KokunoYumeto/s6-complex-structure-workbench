"""Clean theorem-only intakes for the four remaining unopened III targets.

Read neither their old argument-bearing packets nor any original proof.
This prepares inputs only and grants no completion or release credit.
"""
from pathlib import Path
from hashlib import sha256
import re

ROOT = Path(__file__).resolve().parents[1]
raw = (ROOT / 'S6_SERIES_PUBLISH_III.tex').read_bytes()
assert sha256(raw).hexdigest() == '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
text = raw.decode()
targets = [('02LQ', 'maps:src:D.2.49'), ('02LS', 'maps:src:D.2.50'),
           ('02LU', 'maps:src:D.2.52'), ('02LG', 'maps:src:D.2.4')]
prepared = []
for tag, label in targets:
    marker = '\\label{' + label + '}'
    assert text.count(marker) == 1
    position = text.index(marker)
    starts = list(re.finditer(r'\\begin\{(theorem|proposition|lemma|corollary)\}', text[:position]))
    match = starts[-1]
    start = match.start()
    environment = match.group(1)
    end_marker = '\\end{' + environment + '}'
    end = text.index(end_marker, position) + len(end_marker)
    statement = text[start:end]
    assert r'\begin{proof}' not in statement and r'\end{proof}' not in statement
    assert 'tag-' + tag in statement
    folder = ROOT / ('agents/continuation7_iii_' + tag[2:].lower() + '_statement')
    path = folder / ('S6_SERIES_PUBLISH_III_' + tag + '_statement_only.tex')
    assert not path.exists()
    prepared.append((tag, start, end, statement, folder, path))

for tag, start, end, statement, folder, path in prepared:
    folder.mkdir(exist_ok=True)
    header = ('% Clean exact canonical statement-only intake for ' + tag + '.\n'
              '% Original proof, old packet and historical target programs remain closed.\n'
              '% Stated dependency names are retained without exposing their proof bodies.\n')
    path.write_text(header + statement + '\n', newline='\n')
    print(tag, 'canonical lines', text[:start].count('\n') + 1,
          'through', text[:end].count('\n') + 1, flush=True)
    print('Statement', len(statement.splitlines()), 'lines; SHA256',
          sha256(statement.encode()).hexdigest(), flush=True)
    print('Intake', path.relative_to(ROOT), 'SHA256',
          sha256(path.read_bytes()).hexdigest(), flush=True)
assert (ROOT / 'S6_SERIES_PUBLISH_III.tex').read_bytes() == raw
print('Canonical unchanged. No target proof, old packet or historical program was exposed; no global row was changed.', flush=True)
