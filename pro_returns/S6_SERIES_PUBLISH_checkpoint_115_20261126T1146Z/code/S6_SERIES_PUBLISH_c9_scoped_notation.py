"""Helpers for reviewed, bounded, exactly reversible source proposals."""
from pathlib import Path
import csv
import difflib
import json
import re


def math_letters(text, mapping):
    spans = re.compile(r'\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\]|(?<!\\)\$(?:\\.|[^$])*?\$')
    text_commands = {'begin', 'end', 'operatorname', 'text', 'hbox', 'textrm',
                     'mathrm', 'mathbf', 'mathsf', 'mathcal', 'mathfrak',
                     'label', 'hypertarget', 'ref'}
    def span(match):
        value, out, i = match.group(), [], 0
        while i < len(value):
            if value[i] == '\\':
                cmd = re.match(r'\\[A-Za-z]+|\\.', value[i:])
                if cmd:
                    token = cmd.group()
                    out.append(token)
                    i += len(token)
                    if token[1:] in text_commands and i < len(value) and value[i] == '{':
                        depth, j = 1, i + 1
                        while depth:
                            if value[j] == '{': depth += 1
                            elif value[j] == '}': depth -= 1
                            j += 1
                        arg = value[i:j]
                        out.append(arg)
                        i = j
                        if token == r'\begin' and arg in ['{array}', '{tabular}']:
                            assert value[i] == '{'
                            depth, j = 1, i + 1
                            while depth:
                                if value[j] == '{': depth += 1
                                elif value[j] == '}': depth -= 1
                                j += 1
                            out.append(value[i:j])
                            i = j
                    continue
            out.append(mapping.get(value[i], value[i]))
            i += 1
        return ''.join(out)
    return spans.sub(span, text)


class ScopedReview:
    def __init__(self, source, first, last, tag, unit, pages, review_status):
        self.source, self.tag, self.unit, self.pages = source, tag, unit, pages
        self.status = review_status
        self.start = source.index(first)
        self.end = source.index(last, self.start)
        self.old = source[self.start:self.end]
        self.new = self.old
        self.operations = []

    def edit(self, first, last, transform, reason, markers):
        a = self.new.index(first)
        b = self.new.index(last, a) if last else len(self.new)
        old = self.new[a:b]
        new = transform(old)
        assert old != new, ('empty operation', first)
        assert self.new.count(old) == 1
        self.new = self.new[:a] + new + self.new[b:]
        self.operations.append((old, new, reason, markers))

    def exact(self, old, new, reason, markers):
        assert self.new.count(old) == 1, ('exact guard', old)
        self.new = self.new.replace(old, new, 1)
        self.operations.append((old, new, reason, markers))

    def finish(self, output, stem):
        back = self.new
        for old, new, _, _ in reversed(self.operations):
            assert back.count(new) == 1
            back = back.replace(new, old, 1)
        assert back == self.old
        for pat in [r'\\label\{[^}]+\}', r'\\hypertarget\{[^}]+\}', r'\d+']:
            assert re.findall(pat, self.new) == re.findall(pat, self.old), pat
        oldlines, newlines = self.old.splitlines(True), self.new.splitlines(True)
        matcher = difflib.SequenceMatcher(a=oldlines, b=newlines, autojunk=False)
        rows = []
        for number, group in enumerate(matcher.get_grouped_opcodes(n=3), 1):
            a, b = group[0][1], group[-1][2]
            c, d = group[0][3], group[-1][4]
            old, new = ''.join(oldlines[a:b]), ''.join(newlines[c:d])
            assert self.source.count(old) == 1
            reasons = []
            for _, _, reason, markers in self.operations:
                if any(marker in new for marker in markers) and reason not in reasons:
                    reasons.append(reason)
            assert reasons
            rows.append(dict(change_id=f'CLAUDE-III-P15-current02-{self.tag}-{number:03}',
                             type='D20', statement_id=self.unit,
                             old_location=f'Paper III, tag {self.tag}; bounded fragment {number}',
                             old_page='candidate02 '+self.pages,
                             new_location='same permanent result and its explicitly identified surrounding context',
                             new_page='pending changed rendering',
                             old_text=old, new_text=new, reason=' '.join(reasons),
                             review_status=self.status))
        full = self.source
        for row in rows:
            assert full.count(row['old_text']) == 1
            full = full.replace(row['old_text'], row['new_text'], 1)
        for row in reversed(rows):
            assert full.count(row['new_text']) == 1
            full = full.replace(row['new_text'], row['old_text'], 1)
        assert full == self.source
        (output/(stem+'.json')).write_text(json.dumps(rows, ensure_ascii=False, indent=2)+'\n')
        (output/(stem+'.diff')).write_text(''.join(difflib.unified_diff(
            oldlines, newlines, fromfile=self.tag+' before', tofile=self.tag+' proposed', n=5)))
        with (output/(stem+'_defects.tsv')).open('w', newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t',lineterminator='\n')
            w.writeheader()
            w.writerows(rows)
        print(self.tag, len(oldlines), 'scoped lines;', len(self.operations),
              'reversible operations;', len(rows), 'guarded fragments.')
        print('Scoped and complete-source inverses; numeric literals; labels and targets all passed.')
        return rows
