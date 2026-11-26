from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation3_foundations/sec07'
OUT.mkdir(parents=True, exist_ok=True)
text = (ROOT / 'S6_SERIES_PUBLISH_II.tex').read_text()
start = text.index(r'\section{Irreducible and reducible torus-fibre Euler criteria}')
end = text.index(r'\section{Local torus fillings and canonical-flat component geometry}', start)
fragment = text[start:end]
destination = OUT / 'S6_SERIES_PUBLISH_II_sec07_input.tex'
if not destination.exists():
    destination.write_text(fragment, newline='\n')
else:
    assert destination.read_text() == fragment, 'The assigned source changed; do not overwrite the input.'
print(f'Section input: {len(fragment.splitlines())} lines; starts at source line {text[:start].count(chr(10))+1}')
for number, line in enumerate(fragment.splitlines(), 1):
    if re.match(r'\\(?:begin\{(?:theorem|proposition|lemma|corollary|definition|remark)\}|subsection\{)', line):
        print(f'{number}: {line}')
