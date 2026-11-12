import json, sys, io, os, collections, datetime
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
base = r"C:\Users\user\Documents\math\research\s6_recent_results_main\custody"
d = json.load(open(os.path.join(base, 'source_task_tree.json'), encoding='utf-8'))
T = d['threads']
E = d['edges']

def ts(ms):
    if ms is None:
        return 'None'
    return datetime.datetime.fromtimestamp(int(ms) / 1000, datetime.timezone.utc).strftime('%Y-%m-%d %H:%M')

def short(v, n=300):
    s = json.dumps(v, ensure_ascii=False) if not isinstance(v, str) else v
    s = ' '.join(s.split())
    return s if len(s) <= n else s[:n] + '...[%d]' % len(s)

mode = sys.argv[1]
if mode == 'fields':
    for k in ['model', 'reasoning_effort', 'model_provider', 'source', 'agent_role', 'thread_source', 'originator', 'cli_version', 'archived', 'history_mode']:
        vals = collections.Counter(short(r.get(k), 80) for r in T)
        print(k, vals.most_common(25))
    print('edges sample', E[:3])
    print('edge kinds', collections.Counter(short(e[2], 60) for e in E).most_common(10))
    root = [r for r in T if r['id'] == d['source_id']][0]
    print({k: short(v, 600) for k, v in root.items()})
    cm = [r['created_at_ms'] for r in T if r.get('created_at_ms')]
    print('created range', ts(min(cm)), ts(max(cm)))
elif mode == 'bymodelday':
    c = collections.Counter()
    for r in T:
        day = ts(r.get('created_at_ms'))[:10]
        c[(day, r.get('model'), r.get('reasoning_effort'))] += 1
    for k in sorted(c, key=str):
        print(k, c[k])
elif mode == 'first':
    n = int(sys.argv[2])
    rs = sorted(T, key=lambda r: int(r.get("created_at_ms") or 0))
    par = {}
    for e in E:
        par.setdefault(e[1], e[0])
    for r in rs[:n]:
        print(ts(r.get('created_at_ms')), r['id'][:13], 'parent', (par.get(r['id']) or '')[:13], '|', r.get('model'), r.get('reasoning_effort'), '|', r.get('agent_role'), r.get('agent_nickname'), '| tok', r.get('tokens_used'), '|', short(r.get('title'), 90), '||', short(r.get('first_user_message'), int(sys.argv[3]) if len(sys.argv) > 3 else 200))
elif mode == 'depth1':
    kids = [e[1] for e in E if e[0] == d['source_id']]
    byid = {r['id']: r for r in T}
    ks = sorted(set(kids), key=lambda i: byid[i].get('created_at_ms') or 0 if i in byid else 0)
    print('direct children', len(ks))
    c = collections.Counter()
    for i in ks:
        r = byid.get(i)
        if r:
            c[(ts(r.get('created_at_ms'))[:10], r.get('model'), r.get('reasoning_effort'))] += 1
    for k in sorted(c, key=str):
        print(k, c[k])
