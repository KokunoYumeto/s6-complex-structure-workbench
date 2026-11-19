# Intake of S6_06_BLIND cp36 (Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8, 19 Nov 2026).
# For each night-run row, compares the statement in the register (cp36) with the text the papers (S6_10_PAPERS cp15)
# print under the same label, after normalizing whitespace and dropping TeX layout commands.
# Usage: python -I -B compare_text.py <night results.csv> <papers dir>
import csv, os, re, sys, difflib
rows = {r['id']: r for r in csv.DictReader(open(sys.argv[1], encoding='utf-8'))}
def norm(s):
    s = re.sub(r'\\(par|noindent|medskip|nopagebreak\[\d\]|textbf\{Statement\.\}|bigskip|smallskip)', ' ', s)
    s = re.sub(r'%[^\n]*', ' ', s)
    s = re.sub(r'\s+', '', s)
    return s
texts = {}
for root, _, files in os.walk(sys.argv[2]):
    if 'revisions' in root:
        continue
    for f in files:
        if not f.endswith('.tex') or 'source' in f:
            continue
        t = open(os.path.join(root, f), encoding='utf-8', errors='replace').read()
        for m in re.finditer(r'\\label\{night:([A-Z0-9.]+)\}', t):
            i = m.group(1)
            seg = t[m.end(): m.end() + 20000]
            seg = re.sub(r'\\StatementRecord\{[^}]*\}\{[^}]*\}\{', '', seg, count=1)
            end = re.search(r'\\end\{(theorem|refuted|proposition|lemma|corollary|definition|known|openproblem|remark)\}', seg)
            body = seg[:end.start()] if end else seg[:4000]
            texts.setdefault(i, []).append(body)
res = []
for i, r in rows.items():
    a = norm(r['statement'])
    best = 0.0
    for b in texts.get(i, []):
        nb = norm(b)
        # the paper body starts with the record text: test containment first, then similarity of the tail
        if a and a in nb:
            best = 1.0; break
        best = max(best, difflib.SequenceMatcher(None, a, nb[-len(a) - 200:] if len(nb) > len(a) + 200 else nb, autojunk=False).ratio())
    res.append((best, i))
res.sort()
full = sum(1 for b, _ in res if b == 1.0)
print('rows', len(res), '; statement contained verbatim in the papers:', full)
for b, i in res[:25]:
    print('%.3f %s' % (b, i))
