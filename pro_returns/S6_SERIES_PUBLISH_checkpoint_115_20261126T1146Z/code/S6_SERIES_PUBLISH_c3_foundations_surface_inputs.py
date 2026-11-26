from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation3_foundations'
source = (ROOT / 'S6_SERIES_PUBLISH_II.tex').read_text()
for label, name in [('night:P4.15', 'P415'), ('night:P4R.2', 'P4R2')]:
    position = source.index(r'\label{' + label + '}')
    start = source.rfind(r'\begin{proposition}', 0, position)
    end = source.index(r'\end{proof}', position) + len(r'\end{proof}')
    text = source[start:end]
    path = OUT / f'S6_SERIES_PUBLISH_II_P244_{name}_input.tex'
    path.write_text(text + '\n')
    print(f'{label}: {len(text.splitlines())} lines; {path.relative_to(ROOT)}')
