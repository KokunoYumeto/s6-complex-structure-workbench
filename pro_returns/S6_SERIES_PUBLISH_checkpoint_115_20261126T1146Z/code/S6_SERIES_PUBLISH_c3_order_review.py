"""Read-only candidates for the paper-wide mathematical order review.

This does not update an inventory, ledger, citation list or derived file.
Every printed edge still needs a reading of its mathematical context.
"""
from pathlib import Path
import re
import sys
from bisect import bisect_right

root = Path(__file__).resolve().parents[1]
text = (root / 'S6_SERIES_PUBLISH_II.tex').read_text()
labels = {m[1]: m.start() for m in re.finditer(r'\\label\{([^}]+)\}', text)}
sections = list(re.finditer(r'^\\section\*?\{([^\n]+)', text, re.M))
section_starts = [m.start() for m in sections]
environment_names = re.findall(r'\\newtheorem\{([^}]+)\}', text)
environments = list(re.finditer(
    r'\\begin\{(' + '|'.join(re.escape(x) for x in environment_names) + r')\}', text))
environment_starts = [m.start() for m in environments]

def owner(pos):
    i = bisect_right(environment_starts, pos) - 1
    if i < 0:
        return 'front'
    start = environments[i].start()
    stop = environment_starts[i + 1] if i + 1 < len(environments) else len(text)
    m = re.search(r'\\label\{([^}]+)\}', text[start:stop])
    return m[1] if m else environments[i][1]

def section(pos):
    return bisect_right(section_starts, pos) - 1

def line(pos):
    return text.count('\n', 0, pos) + 1

body = text.index(r'\section{Common conventions}')
ending = text.index(r'\part{The remaining splitting problem}')
seen = set()
all_owners = '--all-owners' in sys.argv
for proof in re.finditer(r'\\begin\{proof\}[\s\S]*?\\end\{proof\}', text):
    if not body <= proof.start() < ending:
        continue
    source = owner(proof.start())
    targets = []
    for ref in re.finditer(r'\\(?:[Cc]ref|[Ee]qref|ref|SeriesRef)\*?\{([^}]+)\}|\\hyperref\[([^]]+)\]', proof[0]):
        for target in (ref[1] or ref[2]).split(','):
            target = target.strip()
            pos = labels.get(target)
            if pos is None:
                continue
            if all_owners and (pos < proof.end() or owner(pos) == source):
                continue
            if not all_owners and section(pos) <= section(proof.start()):
                continue
            key = (source, target)
            if key in seen:
                continue
            seen.add(key)
            print(f'{line(proof.start()+ref.start())}: {source} -> {target} '
                  f'(target line {line(pos)}, owner {owner(pos)})')
