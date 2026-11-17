"""Remove observed duplicated kind words around already resolved references."""
from pathlib import Path
import json
import sys

D = Path(__file__).resolve().parents[2]


def transform(text, paper):
    changes = []
    rules = ([('Theorem Paper~I, Theorem~17.4', 'Paper~I, Theorem~17.4'),
              ('Proposition~Paper~I, Proposition~D.6', 'Paper~I, Proposition~D.6'),
              ('Its equation Paper~I, Equation~183', 'Paper~I, Equation~183')]
             if paper == 'III' else
             [('The cusp theorem Paper~I, Theorem~B.6', 'The cusp result in Paper~I, Theorem~B.6')])
    expected = [2, 1, 1] if paper == 'III' else [1]
    for (old, new), count in zip(rules, expected):
        assert text.count(old) == count, (paper, old, text.count(old))
        changes.append({'before': old, 'after': new, 'occurrences': count,
                        'reason': 'Remove the source kind word duplicated by the explicit cross-paper reference; the target and all mathematical content are unchanged.'})
        text = text.replace(old, new)
    (D / f'records/{paper}_external_reference_wording_repairs.json').write_text(json.dumps(changes, indent=2) + '\n')
    return text


if __name__ == '__main__':
    paper = sys.argv[1]
    p = D / f'S6_09_PAPERS_{paper}.tex'
    p.write_text(transform(p.read_text(), paper))
