import json,gzip,sys,io,re,collections
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8',errors='replace')
fn=sys.argv[1]; pat=re.compile(sys.argv[2]); n=int(sys.argv[3]); maxp=int(sys.argv[4]) if len(sys.argv)>4 else 10
cnt=0; keys=collections.Counter(); tot=0; mem=collections.Counter()
with gzip.open(fn,'rt',encoding='utf-8') as f:
    for line in f:
        if not line.strip(): continue
        r=json.loads(line); tot+=1; keys.update(r.keys())
        s=json.dumps(r,ensure_ascii=False)
        if pat.search(s):
            cnt+=1
            mem[str(r.get('member') or r.get('path') or r.get('raw_member'))[-120:]]+=1
            if cnt<=maxp:
                print({k:(v if not isinstance(v,str) or len(v)<=n else v[:n]+'...[%d]'%len(v)) for k,v in r.items()})
                print()
print('total',tot,'matches',cnt,'keys',dict(keys))
for k,v in mem.most_common(20): print(v,k)
