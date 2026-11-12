import json,gzip,sys,io,os,glob,collections,datetime
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8',errors='replace')
base=r"C:/Users/user/Documents/math/research/s6_recent_results_main/related_sources"
def ts(ms): return datetime.datetime.fromtimestamp(int(ms)/1000,datetime.timezone.utc).strftime('%Y-%m-%d %H:%M')
for sid in sorted(os.listdir(base)):
    fs=glob.glob(os.path.join(base,sid,'*state_5.sqlite__threads.jsonl.gz'))
    for fn in fs:
        rows=[json.loads(l) for l in gzip.open(fn,'rt',encoding='utf-8') if l.strip()]
        c=collections.Counter()
        for r in rows:
            r=r.get('row',r)
            c[(r.get('model'),r.get('reasoning_effort'))]+=1
        print(sid[:13],len(rows),dict((str(k),v) for k,v in c.items()))
        for r in rows:
            r=r.get('row',r)
            if r.get('id')==sid or r.get('thread_source')=='user':
                print('   root', r.get('id','')[:13], ts(r['created_at_ms']) if r.get('created_at_ms') else r.get('created_at'), '->', ts(r['updated_at_ms']) if r.get('updated_at_ms') else '', r.get('model'), r.get('reasoning_effort'), '| name:', r.get('name'), '| tok', r.get('tokens_used'))
        if rows: print('   keys', list(rows[0].keys())[:8])
