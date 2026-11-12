import json,gzip,sys,io,re
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8',errors='replace')
fn=r"C:/Users/user/Documents/math/research/s6_recent_results_main/ledgers/source_files.jsonl.gz"
pat=re.compile(sys.argv[1], re.I)
seen=set()
with gzip.open(fn,'rt',encoding='utf-8') as f:
    for line in f:
        r=json.loads(line)
        if pat.search(r['member']):
            k=(r['member'],r['sha256'])
            if k in seen: continue
            seen.add(k)
            print(r['bytes'], r['sha256'][:12], r['member'][-150:])
print(len(seen))
