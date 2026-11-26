"""T1: retain exact display-label aliases without changing AMS/kernel label hooks.

The seven secondary labels are moved immediately after their enclosing display.
Their complete ordinary and cleveref aux records are copied from their primary
labels on the next LaTeX pass. No equation counter or printed formula changes.
"""
from pathlib import Path
from collections import Counter
import argparse
import csv
import hashlib
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'S6_SERIES_PUBLISH_III.tex'
WORK = ROOT / 'agents/continuation9_tex_runtime/aliases'
PAIRS = [
    ('wb:h24:ret:eq:M', 'maps:eq:B.3.2'),
    ('wb:h24:ret:eq:derivative-on-M', 'maps:eq:B.3.3'),
    ('wb:h24:ret:eq:normal-u', 'maps:eq:B.3.4'),
    ('maps:eq:D.OF1', 'maps:eq:D.OL1'),
    ('maps:eq:D.OF11', 'maps:eq:D.OL2'),
    ('maps:eq:D.OF16', 'maps:eq:D.OL12'),
    ('maps:eq:D.OF18', 'maps:eq:D.OL3'),
]
BLOCK = r'''\makeatletter
\newcommand{\SsixDisplayAliases}[2]{%
  \begingroup
  \def\label##1{%
    \@ifundefined{r@#1}{}{%
      \protected@write\@auxout{}{%
        \string\newlabel{##1}{\csname r@#1\endcsname}}%
    }%
    \@ifundefined{r@#1@cref}{}{%
      \protected@write\@auxout{}{%
        \string\newlabel{##1@cref}{\csname r@#1@cref\endcsname}}%
    }%
  }%
  #2%
  \endgroup
}
\makeatother'''

def identities(s):
    return Counter(re.findall(r'\\(?:label|hypertarget)\{[^{}]*\}', s))

def candidate(s):
    start = s.index('\\makeatletter\n\\AtBeginDocument{%')
    end = s.index('\\makeatother', start) + len('\\makeatother')
    old = s[start:end]
    assert '\\Ssix@dispatch' in old and '\\cref@old@label@in@display' in old
    t = s[:start] + BLOCK + s[end:]
    pattern = re.compile(r'\\begin\{(equation|align)\}(.*?)\\end\{\1\}', re.S)
    changes = []
    for primary, alias in PAIRS:
        token = '\\label{' + alias + '}'
        assert t.count(token) == 1, alias
        matches = [m for m in pattern.finditer(t) if token in m.group()]
        assert len(matches) == 1, alias
        m = matches[0]
        assert '\\label{' + primary + '}' in m.group()
        replacement = m.group().replace(token, '') + '\n\\SsixDisplayAliases{' + primary + '}{' + token + '}'
        changes.append((primary, alias, m.group(), replacement))
        t = t[:m.start()] + replacement + t[m.end():]
    assert identities(s) == identities(t)
    # Explicit inverse reconstructs the original bytes; the only changes are
    # the preamble mechanism and the seven local moves of literal label calls.
    inverse = t
    for _, _, before, after in reversed(changes):
        assert inverse.count(after) == 1
        inverse = inverse.replace(after, before, 1)
    inverse = inverse.replace(BLOCK, old, 1)
    assert inverse == s
    return t, old, changes

def mwe(s):
    t, _, _ = candidate(s)
    pre = t.split('\\begin{document}', 1)[0]
    displays = []
    for m in re.finditer(r'\\begin\{(equation|align)\}(.*?)\\end\{\1\}', t, re.S):
        if any('\\label{' + p + '}' in m.group() for p, _ in PAIRS):
            tail = t[m.end():]
            a = re.match(r'\n\\SsixDisplayAliases\{[^{}]+\}\{\\label\{[^{}]+\}\}', tail)
            assert a
            displays.append(m.group() + a.group())
    assert len(displays) == 7
    body = '\\begin{document}\n\\section{Equation aliases}\n'
    body += '\\begin{equation}a=1\\label{c9:ordinary-before}\\end{equation}\n'
    body += '\n'.join(displays)
    body += '\n\\begin{equation}b=2\\label[equation]{c9:ordinary-after}\\end{equation}\n'
    for p, a in PAIRS:
        body += '\\noindent Primary: \\eqref{' + p + '}; alias: \\eqref{' + a + '}; type: \\cref{' + a + '}.\\par\n'
    body += '\\section{Counter reset}\n\\begin{equation}c=3\\label{c9:reset}\\end{equation}\n'
    body += 'Before: \\eqref{c9:ordinary-before}; after: \\eqref{c9:ordinary-after}; reset: \\eqref{c9:reset}.\n\\end{document}\n'
    return pre + body

def run_mwe():
    WORK.mkdir(parents=True, exist_ok=True)
    tex = WORK / 'S6_SERIES_PUBLISH_c9_display_aliases.tex'
    tex.write_text(mwe(SOURCE.read_text()), newline='\n')
    wrapper = ROOT / 'code/S6_SERIES_PUBLISH_c9_tex_runtime.py'
    last = None
    for n in range(1, 5):
        result = subprocess.run([sys.executable, str(wrapper), '-interaction=nonstopmode', '-halt-on-error', tex.name], cwd=WORK, capture_output=True, text=True)
        prefix = ROOT / f'code/S6_SERIES_PUBLISH_c9_alias_pass{n:02d}'
        prefix.with_suffix('.out').write_text(result.stdout, newline='\n')
        prefix.with_suffix('.err').write_text(result.stderr, newline='\n')
        log = tex.with_suffix('.log').read_text() if tex.with_suffix('.log').exists() else ''
        prefix.with_suffix('.log').write_text(log, newline='\n')
        print('pass', n, 'exit', result.returncode)
        if result.returncode:
            print(result.stdout[-5000:], result.stderr[-2000:])
            return result.returncode
        aux = tex.with_suffix('.aux').read_text()
        warnings = [x for x in log.splitlines() if any(y in x for y in ('Warning:', 'Overfull', 'Missing character', 'undefined'))]
        print('\n'.join(warnings))
        if aux == last and not any('undefined' in x or 'Rerun' in x for x in warnings):
            records = dict(re.findall(r'^\\newlabel\{([^{}]+)\}(.*)$', aux, re.M))
            for p, a in PAIRS:
                assert records[p] == records[a], (p, a)
                assert records[p + '@cref'] == records[a + '@cref'], (p, a)
                print(p, '=', a, records[p])
            print('All seven complete label and cleveref records match; auxiliary data converged.')
            return 0
        last = aux
    raise RuntimeError('Alias diagnostic did not converge within four passes')

def apply():
    original = SOURCE.read_text()
    revised, old, changes = candidate(original)
    path = ROOT / 'S6_SERIES_PUBLISH_defects_III.tsv'
    csv.field_size_limit(100000000)
    with path.open(newline='') as f:
        reader = csv.DictReader(f, delimiter='\t'); rows = list(reader); fields = reader.fieldnames
    assert not any(x['change_id'] == 'CLAUDE-III-T1' for x in rows)
    row = dict.fromkeys(fields, '')
    row.update(change_id='CLAUDE-III-T1', type='D18;D23', statement_id='preamble;seven display alias pairs', old_location='cp100 preamble lines 19–52 and seven multiply labelled displays', new_location='preamble SsixDisplayAliases; each alias immediately after its display', old_text=old, new_text=BLOCK, reason='Remove the incompatible changes to ltx@label and cref@old@label@in@display. Each display keeps one AMS label; seven literal secondary labels are retained and copy the complete primary and cleveref auxiliary records without changing their number, page, title or destination. The exact inverse in the application program reconstructs every source byte before this edit. All explicit hypertargets remain in the original displays. Legacy-kernel MWE has converged with all seven record pairs equal; current-kernel full build remains required.', review_status='source repair applied; two-kernel full build and final page review pending')
    rows.append(row)
    SOURCE.write_text(revised, newline='\n')
    with path.open('w', newline='') as f:
        w = csv.DictWriter(f, fields, delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(rows)
    print('Applied T1 source repair; preserved', sum(identities(original).values()), 'literal label/target occurrences.')
    print('Source SHA-256', hashlib.sha256(SOURCE.read_bytes()).hexdigest())
    print('No mathematical statement or proof body changed. Current-kernel/full-build gate remains open.')

if __name__ == '__main__':
    p = argparse.ArgumentParser(); p.add_argument('action', choices=('mwe', 'apply')); a = p.parse_args()
    sys.exit(run_mwe() if a.action == 'mwe' else apply())
