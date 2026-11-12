import json, gzip, collections, sys, io, os, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
base = r"C:\Users\user\Documents\math\research\s6_recent_results_main\ledgers"
fn = os.path.join(base, 'unfinished_and_nonclaim_routes.jsonl.gz')
geo = re.compile(r"Dolbeault|Hodge|Fr[oö]licher|Picard|deformation|Kuranishi|Kodaira|automorphism|Bott|Aeppli|canonical bundle|K_X|nearby|Leray|homolog|cohomolog|tangent|T_X|Campana|CDP|algebraic dimension|a\(X\)|conormal|torsion|bielliptic|del Pezzo|toric|logarithmic|multiple fibre|multiple fiber|period|monodromy|moduli|h\^\{|vanishing|Serre|residue|gluing|atlas|diffeomorph|h-cobord|Smale|sphere|cusp", re.I)
unf = re.compile(r"\bopen\b|unresolved|remain|not (yet )?(proved|established|verified|complete)|gap|unfinished|still|missing|unknown|not claim|no claim|does not|cannot|incomplete|next", re.I)
mode = sys.argv[1]
rows = []
with gzip.open(fn, 'rt', encoding='utf-8') as f:
    for line in f:
        if line.strip():
            rows.append(json.loads(line))
if mode == 'stats':
    root = [r for r in rows if r['source_task_id'].startswith('01a03492')]
    print('root records', len(root), collections.Counter(r['role'] for r in root))
    lens = [len(r['exact_text']) for r in rows]
    print('total chars', sum(lens), 'max', max(lens))
    a = [r for r in rows if r['role'] == 'assistant']
    g = [r for r in a if geo.search(r['exact_text']) and unf.search(r['exact_text'])]
    print('assistant', len(a), 'assistant geo+unf', len(g), 'chars', sum(len(r['exact_text']) for r in g))
    gr = [r for r in g if r['source_task_id'].startswith('01a03492')]
    print('root assistant geo+unf', len(gr), 'chars', sum(len(r['exact_text']) for r in gr))
    lines = sorted(int(r['raw_line']) for r in root)
    print('root raw_line range', lines[0], lines[-1])
elif mode == 'root':
    lo = int(sys.argv[2]); hi = int(sys.argv[3]); n = int(sys.argv[4])
    for r in rows:
        if not r['source_task_id'].startswith('01a03492'):
            continue
        if r['role'] != 'assistant':
            continue
        ln = int(r['raw_line'])
        if ln < lo or ln > hi:
            continue
        t = r['exact_text']
        if not (geo.search(t) and unf.search(t)):
            continue
        t = re.sub(r'\s+', ' ', t)
        print('[%d] %s' % (ln, t[:n]))
        print()
elif mode == 'children':
    n = int(sys.argv[2])
    kw = re.compile(sys.argv[3], re.I) if len(sys.argv) > 3 else None
    for r in rows:
        if r['source_task_id'].startswith('01a03492') or r['role'] != 'assistant':
            continue
        t = r['exact_text']
        if not (geo.search(t) and unf.search(t)):
            continue
        if kw and not kw.search(t):
            continue
        t = re.sub(r'\s+', ' ', t)
        print('[%s:%s] %s' % (r['source_task_id'][:13], r['raw_line'], t[:n]))
        print()
