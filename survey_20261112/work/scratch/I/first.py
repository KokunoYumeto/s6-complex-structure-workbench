import json,gzip,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8',errors='replace')
fn=r"C:/Users/user/Documents/math/research/s6_recent_results_main/ledgers/unfinished_and_nonclaim_routes.jsonl.gz"
n=0
with gzip.open(fn,'rt',encoding='utf-8') as f:
    for line in f:
        r=json.loads(line)
        if r['source_task_id'].startswith('01a03492') and str(r['raw_line'])=='9':
            print(r['exact_text'])
            n+=1
            break
print('found',n)
