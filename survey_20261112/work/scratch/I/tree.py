import json, sys, io, os, collections, datetime
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
base = r"C:\Users\user\Documents\math\research\s6_recent_results_main\custody"

def short(v, n=300):
    s = json.dumps(v, ensure_ascii=False) if not isinstance(v, str) else v
    return s if len(s) <= n else s[:n] + '...[%d]' % len(s)

mode = sys.argv[1]
if mode == 'goal':
    for line in open(os.path.join(base, 'inherited_goal_state.jsonl'), encoding='utf-8'):
        if line.strip():
            r = json.loads(line)
            print({k: short(v, 3000) for k, v in r.items()})
            print()
else:
    d = json.load(open(os.path.join(base, 'source_task_tree.json'), encoding='utf-8'))
    if mode == 'schema':
        def walk(x, depth=0, name='root'):
            pad = '  ' * depth
            if isinstance(x, dict):
                print(pad, name, 'dict', len(x), list(x.keys())[:40])
                if depth < 2:
                    for k, v in list(x.items())[:40]:
                        walk(v, depth + 1, k)
            elif isinstance(x, list):
                print(pad, name, 'list', len(x))
                if x and depth < 3:
                    walk(x[0], depth + 1, name + '[0]')
            else:
                print(pad, name, short(x, 300))
        walk(d)
    else:
        # find list of task records
        recs = None
        for k, v in (d.items() if isinstance(d, dict) else []):
            if isinstance(v, list) and v and isinstance(v[0], dict):
                recs = v
                print('using list', k, len(v))
                break
        if recs is None and isinstance(d, list):
            recs = d
        if mode == 'fields':
            keys = collections.Counter()
            for r in recs:
                keys.update(r.keys())
            print(keys)
            for k in keys:
                vals = collections.Counter(short(r.get(k), 70) for r in recs)
                if len(vals) <= 30:
                    print(k, vals.most_common(30))
                else:
                    print(k, 'distinct', len(vals), vals.most_common(4))
        elif mode == 'dump':
            import pickle
            json.dump(recs, open(os.path.join(os.path.dirname(__file__), 'tree_recs.json'), 'w', encoding='utf-8'))
            print('dumped', len(recs))
