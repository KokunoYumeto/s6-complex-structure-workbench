# Intake of S6_06_BLIND cp36 (Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8, 19 Nov 2026).
# Compares the night run's status per row with the status the papers (S6_10_PAPERS cp15) record for the same label.
# Usage: python -I -B compare_status.py <night results.csv> <papers dir>
import csv, os, re, sys, collections
rows = {r['id']: r for r in csv.DictReader(open(sys.argv[1], encoding='utf-8'))}
rec = collections.defaultdict(set)
pat = re.compile(r'\\StatementRecord\{night:([A-Z0-9.]+)\}\{([^}]*)\}')
for root, _, files in os.walk(sys.argv[2]):
    if 'revisions' in root:
        continue
    for f in files:
        if f.endswith('.tex') and 'source' not in f:
            for m in pat.finditer(open(os.path.join(root, f), encoding='utf-8', errors='replace').read()):
                rec[m.group(1)].add(m.group(2).strip())
pairs = collections.Counter()
diff = collections.defaultdict(list)
for i, r in rows.items():
    st = r['status'].strip()
    ps = '; '.join(sorted(rec.get(i, {'(not recorded)'})))
    pairs[(st, ps)] += 1
    diff[(st, ps)].append(i)
for (a, b), n in sorted(pairs.items(), key=lambda x: -x[1]):
    ids = diff[(a, b)]
    print('%-8s | papers: %-40s | %3d | %s' % (a, b[:40], n, ' '.join(ids[:14]) + (' ...' if len(ids) > 14 else '')))
