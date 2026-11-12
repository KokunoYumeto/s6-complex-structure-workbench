import json, sys, io, os, collections, datetime
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
base = r"C:/Users/user/Documents/math/research/s6_recent_results_main/custody"
d = json.load(open(os.path.join(base, 'source_task_tree.json'), encoding='utf-8'))
T = d['threads']
def day(r):
    return datetime.datetime.fromtimestamp(int(r['created_at_ms'])/1000, datetime.timezone.utc).strftime('%Y-%m-%d')
tok = collections.Counter(); cnt = collections.Counter(); tokm = collections.Counter()
for r in T:
    t = int(r.get('tokens_used') or 0)
    tok[day(r)] += t; cnt[day(r)] += 1; tokm[(r.get('model'), r.get('reasoning_effort'))] += t
for k in sorted(tok): print(k, cnt[k], 'threads', round(tok[k]/1e6,1), 'M tokens')
print({str(k): round(v/1e6,1) for k,v in tokm.items()})
print('total M', round(sum(tok.values())/1e6,1))
gaps = set(json.load(open(r"C:/Users/user/Documents/math/research/s6_recent_results_main/ledgers/source_reading_use_ledger.json", encoding='utf-8'))['raw_history_gaps'])
g = collections.Counter(); 
for r in T:
    if r['id'] in gaps: g[day(r)] += 1
print('missing histories by day', sorted(g.items()))
root=[r for r in T if r['id']==d['source_id']][0]
print('root updated', datetime.datetime.fromtimestamp(int(root['updated_at_ms'])/1000, datetime.timezone.utc))
