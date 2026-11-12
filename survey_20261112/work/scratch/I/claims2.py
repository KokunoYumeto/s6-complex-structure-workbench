import json,gzip,sys,io,collections,re,hashlib
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8',errors='replace')
fn=r"C:/Users/user/Documents/math/research/s6_recent_results_main/ledgers/source_claim_locators.jsonl.gz"
mem=collections.Counter(); base=collections.Counter(); conj={}; uniq=set(); uniqstmt=collections.Counter()
with gzip.open(fn,'rt',encoding='utf-8') as f:
    for line in f:
        r=json.loads(line)
        m=r['member']
        parts=m.split('/')
        mem['/'.join(parts[:4])]+=1
        base[parts[-1].split('!')[-1].split('/')[-1]]+=1
        h=hashlib.sha1(r['exact_source_block'].encode()).hexdigest()
        if h not in uniq:
            uniq.add(h); uniqstmt[r['environment']]+=1
        if r['environment'] in ('conjecture','claim'):
            conj.setdefault(h,(r['environment'],m,r['line'],r['exact_source_block']))
print('distinct blocks',len(uniq)); print(uniqstmt.most_common())
print('--- member prefixes'); 
for k,v in mem.most_common(25): print(v,k)
print('--- basenames');
for k,v in base.most_common(45): print(v,k)
print('--- conjecture/claim blocks',len(conj))
for h,(e,m,l,b) in conj.items():
    print('##',e,m[-110:],l); print(re.sub(r'\s+',' ',b)[:900]); print()
