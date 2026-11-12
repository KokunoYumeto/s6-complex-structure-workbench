import json, gzip, collections, sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
base = r"C:\Users\user\Documents\math\research\s6_recent_results_main\ledgers"

def short(v, n=300):
    s = json.dumps(v, ensure_ascii=False) if not isinstance(v, str) else v
    return s if len(s) <= n else s[:n] + '...[%d]' % len(s)

what = sys.argv[1]
if what == 'readings':
    rows = [json.loads(l) for l in open(os.path.join(base, 'actual_source_readings.jsonl'), encoding='utf-8') if l.strip()]
    print(len(rows))
    keys = collections.Counter()
    for r in rows:
        keys.update(r.keys())
    print(keys)
    for r in rows[:6]:
        print({k: short(v, 200) for k, v in r.items()})
    print('...')
    for r in rows[-3:]:
        print({k: short(v, 200) for k, v in r.items()})
    for k in keys:
        vals = collections.Counter(short(r.get(k), 80) for r in rows)
        if len(vals) < 25:
            print(k, vals.most_common(25))
elif what == 'use':
    d = json.load(open(os.path.join(base, 'source_reading_use_ledger.json'), encoding='utf-8'))
    def walk(x, depth=0, name='root'):
        pad = '  ' * depth
        if isinstance(x, dict):
            print(pad, name, 'dict', len(x), list(x.keys())[:12])
            if depth < 2:
                for k, v in list(x.items())[:12]:
                    walk(v, depth + 1, k)
        elif isinstance(x, list):
            print(pad, name, 'list', len(x))
            if x and depth < 3:
                walk(x[0], depth + 1, name + '[0]')
        else:
            print(pad, name, short(x, 200))
    walk(d)
elif what in ('unfinished', 'claims'):
    fn = 'unfinished_and_nonclaim_routes.jsonl.gz' if what == 'unfinished' else 'source_claim_locators.jsonl.gz'
    n = 0
    keys = collections.Counter()
    cats = collections.defaultdict(collections.Counter)
    first = []
    with gzip.open(os.path.join(base, fn), 'rt', encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            r = json.loads(line)
            n += 1
            keys.update(r.keys())
            for k, v in r.items():
                if isinstance(v, (str, int, bool)) or v is None:
                    s = str(v)
                    if len(s) < 60:
                        cats[k][s] += 1
            if n <= 3:
                first.append(r)
    print('records', n)
    print('keys', keys)
    for r in first:
        print({k: short(v, 400) for k, v in r.items()})
    for k, c in cats.items():
        if len(c) <= 40:
            print(k, c.most_common(40))
        else:
            print(k, 'distinct', len(c), c.most_common(8))
