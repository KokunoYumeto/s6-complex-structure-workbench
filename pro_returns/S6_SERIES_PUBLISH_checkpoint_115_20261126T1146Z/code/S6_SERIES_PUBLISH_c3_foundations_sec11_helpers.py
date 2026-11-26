from pathlib import Path
import csv
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation3_foundations/sec11'
OUT.mkdir(parents=True, exist_ok=True)
with (ROOT / 'agents/continuation2_B/D19/S6_SERIES_PUBLISH_II_B2_D19_v1_equation_map.tsv').open(newline='') as f:
    EQUATION_DICTIONARY = {r['old_tag']: r['target_label'] for r in csv.DictReader(f, delimiter='\t') if r['old_tag']}


def block(text, key):
    p = text.index(r'\label{' + key + '}')
    a = text.rfind(r'\begin{', 0, p)
    b = text.index(r'\end{proof}', p) + len(r'\end{proof}')
    return text[a:b]


class Package:
    def __init__(self, name, unit):
        self.name = name
        self.unit = unit
        self.rows = []
        self.guards = []
        self.equations = []

    def record(self, kinds, owner, old, new, reason):
        for kind in kinds.split(','):
            self.rows.append(dict(change_id=f'II-C3-S11-{self.name.upper()}-{len(self.rows)+1:03}', type=kind, statement_id=owner, old_location='sec:II:11 / ' + owner, old_page='cp35; page concordance pending', new_location=self.unit + ' / ' + owner, new_page='integrated build pending', old_text=old, new_text=new, reason=reason, review_status='Complete original read; receiving comparison pending.'))

    def edit(self, text, old, new, kinds, owner, reason):
        assert old in text, (owner, old[:150])
        for i in range(text.count(old)):
            self.record(kinds, owner, old, new, reason + f' [Occurrence {i+1}.]')
        return text.replace(old, new)

    def guard(self, key, old, new, reason):
        self.guards.append(dict(key=key, old=old, new=new, reason=reason))

    def clean(self, text, owner, prose=True):
        for m in list(re.finditer(r'(?:Proposition~|Theorem~)?\\SeriesRef\{([^{}]+)\}', text)):
            old = m.group(0)
            label = m.group(1)
            if old not in text:
                continue
            new = ('\\eqref{' if ':eq:' in label or label.startswith('eq:') else '\\cref{') + label + '}'
            text = self.edit(text, old, new, 'D04', owner, 'Use the current paper statement or equation number and preserve its stable label.')
        for oldtag, label in EQUATION_DICTIONARY.items():
            if len(oldtag) == 1:
                continue
            old = '(' + oldtag + ')'
            if old in text:
                text = self.edit(text, old, r'\eqref{' + label + '}', 'D04,D19', owner, 'The prepared D19 map identifies this literal citation with its existing exact target.')
        for word, replacement in ([('actual ', ''), ('actual\n', ''), ('Kahler', r'K\"ahler'), ('etale', r"\'etale")] if prose else []):
            pattern = r'(?<![A-Za-z\\\x27])' + re.escape(word)
            def replace_word(m):
                old = m.group(0)
                self.record('D23' if word in ('Kahler', 'etale') else 'D08', owner, old, replacement, 'Use mathematical wording and the conventional accent; all named maps, equations and multiplicities remain.')
                return replacement
            text = re.sub(pattern, replace_word, text)

        def eq(m):
            body = m.group(1)
            tag = re.search(r'\\tag\{([^{}]+)\}', body)
            if not tag:
                return m.group(0)
            labels = re.findall(r'\\label\{([^{}]+)\}', body)
            label = EQUATION_DICTIONARY.get(tag.group(1), labels[0] if labels else 'eq:II:manual:' + tag.group(1))
            newbody = re.sub(r'\\tag\{[^{}]+\}', '', body)
            if not labels:
                newbody += '\\label{' + label + '}\n'
            newbody = '\n' + '\n'.join(line for line in newbody.splitlines() if line.strip()) + '\n'
            new = '\\begin{equation}' + newbody + '\\end{equation}'
            self.equations.append(dict(old_tag=tag.group(1), label=label, owner=owner))
            self.record('D19', owner, m.group(0), new, 'Use the section equation counter, preserving every permanent identifier; convert the tagged bracket display to equation without an internal paragraph.')
            return new

        text = re.sub(r'\\\[([\s\S]*?)\\\]', eq, text)
        return re.sub(r'\n{3,}', '\n\n', text).strip() + '\n'

    def write(self, fragment):
        prefix = 'S6_SERIES_PUBLISH_sec11_' + self.name
        (OUT / ('S6_SERIES_PUBLISH_II_sec11_' + self.name + '.tex')).write_text(fragment, newline='\n')
        (OUT / (prefix + '_guards.json')).write_text(json.dumps(self.guards, ensure_ascii=False, indent=2) + '\n', newline='\n')
        for suffix, data, fields in [('defects', self.rows, list(self.rows[0])), ('equation_map', self.equations, ['old_tag', 'label', 'owner'])]:
            with (OUT / (prefix + '_' + suffix + '.tsv')).open('w', newline='') as f:
                w = csv.DictWriter(f, fieldnames=fields, delimiter='\t', lineterminator='\n')
                w.writeheader()
                w.writerows(data)
        print(f'{self.name}: {len(fragment.splitlines())} receiving lines, {len(self.guards)} guards, {len(self.rows)} defect rows; full receiving read pending.')
