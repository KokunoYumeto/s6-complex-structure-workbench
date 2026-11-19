"""Execute exact public Threefold Explorer topology computations.

Read-only POST requests evaluate integer data. The response and exact input
are retained together; remote output is independent evidence, not a proof of
the unpublished marked geometric local-model comparison.
"""
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError
import json,time,sys
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'records/manifolds_explorer_runs'
OUT.mkdir(exist_ok=True)
API='https://threefold-explorer-api.onrender.com/api'

def post(path,payload,name):
    target=OUT/(name+'.json')
    if target.exists():
        old=json.loads(target.read_text())
        if 'response' in old:return old['response']
    begin=time.time()
    record={'url':API+path,'input':payload}
    try:
        req=Request(API+path,data=json.dumps(payload).encode(),headers={'Content-Type':'application/json'})
        with urlopen(req,timeout=55) as r:response=json.load(r)
        record['response']=response
    except HTTPError as e:
        record['error']=e.read().decode()
    except Exception as e:record['error']=repr(e)
    record['elapsed_seconds']=round(time.time()-begin,3)
    target.write_text(json.dumps(record,indent=2))
    print(name,record['elapsed_seconds'],
          [g['label'] for g in record.get('response',{}).get('cohomology',[])],
          record.get('response',{}).get('fundamental_group',record.get('error','')),flush=True)
    return record.get('response')

def datum(entry,P,Q,weights,logs=None,profile='default',coordinates='invariant'):
    return dict(os_entry=entry,profile=profile,P=[P],Q=[Q],
                linearization_divisor=weights,log_data=logs,coordinates=coordinates)

checks={
 'original_sphere':datum(49,1,6,[0,0,1],[['0','1/3'],['0','1/4'],None],'III'),
 'untwisted_K13':datum(49,1,6,[0,0,1],[None,None,None],'III'),
 'split_two_parameter':datum(43,1,2,[0,0,0,1],[['0','-1/4'],None,None,None]),
 'cuspidal_43_II':datum(43,1,2,[0,0,1],[['0','-1/4'],None,None],'II'),
 'wang_candidate_49':datum(49,1,6,[0,0,1,0],[None,['0','1/3'],None,None]),
 'wang_second_zero':datum(49,1,6,[0,0,0,1],[None,['0','1/3'],None,None]),
 'wang_second_zero_sign':datum(49,1,6,[0,0,0,1],[None,['0','-1/3'],None,None]),
 'os49_complementary':datum(49,2,3,[0,0,1,0],[None,['0','1/3'],None,None]),
 'os45_II':datum(45,8,1,[0,0,1,0],[None,['0','1/6'],None,None],'II'),
 'os47_II':datum(47,14,1,[0,0,1,0],[None,None,None,['0','1/6']],'II'),
 'os47_III':datum(47,7,2,[0,1,0,0],[None,None,None,['0','1/4']],'III'),
 'os49_III_P2':datum(49,2,3,[0,0,1],[['0','1/3'],None,None],'III'),
 'os55_II':datum(55,20,1,[0,0,0,1],[None,None,['0','1/6'],None],'II'),
 'os56_IV':datum(56,10,3,[0,0,0,1],[None,None,['0','1/3'],None],'IV'),
 'os56_III':datum(56,15,2,[0,0,0,1],[None,None,['0','1/4'],None],'III'),
}
for d in [2,5,7,11]:
    checks['cover_model_'+str(d)]=datum(49,1,6*d,[0,0,d],
                    [['0','1/3'],['0','1/4'],None],'III')
for e,n in [(45,8),(47,14),(55,20),(56,30)]:
    for clutch in [0,1]:
        checks['semistable_%d_clutch%d'%(e,clutch)]=datum(e,n,1,[0,0,0,0,1,0],
                     [None]*5+[[0,0,0,clutch]],coordinates='ambient')
if __name__=='__main__':
    requested=set(sys.argv[1:])
    for name,payload in checks.items():
        if requested and name not in requested:continue
        post('/compute',payload,name)
