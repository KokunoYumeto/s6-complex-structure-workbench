"""Parallel execution of the exact-box certificate in f_interval_cert.py.

This changes only scheduling.  Every acceptance uses the same outward
interval proof; rational bisections and omission tests are recorded.
Completed boxes and the remaining frontier are checkpointed regularly.
"""
from concurrent.futures import ProcessPoolExecutor, wait, FIRST_COMPLETED
from fractions import Fraction as F
from pathlib import Path
import json
import sys
import time
from f_interval_cert import certify, box_string, LOCAL

ROOT=(F(0),F(1,2),F(17,20),F(2))

def do_box(box):
    try:
        return certify(box)
    except Exception as e:
        return False,{'reason':str(e)}

def split(box):
    x0,x1,y0,y1=box
    if x1-x0>=y1-y0:
        mid=(x0+x1)/2
        return [(x0,mid,y0,y1),(mid,x1,y0,y1)]
    mid=(y0+y1)/2
    return [(x0,x1,y0,mid),(x0,x1,mid,y1)]

def omitted(box):
    x0,x1,y0,y1=box
    return x1<=LOCAL and y0>=1-LOCAL and y1<=1+LOCAL

def outside_domain(box):
    # The standard modular domain requires |tau|>=1.  Both coordinates
    # are nonnegative, so this exact rational upper-corner test excludes
    # the entire closed box from that domain.
    return box[1]**2+box[3]**2<1

if __name__=='__main__':
    queue=[ROOT]
    pending={}
    done=[];left_out=[];excluded=[];undecided=[]
    start=time.time()
    mark=0
    aborted=False
    base=Path(__file__).parent
    previous_seconds=0
    if '--resume' in sys.argv:
        prior=json.loads((base/'f_interval_parallel_certificate.json').read_text())
        queue=[tuple(F(v) for v in row) for row in prior['pending']]
        done=prior['certified']
        left_out=prior['omitted']
        excluded=prior.get('outside_modular_domain',[])
        undecided=prior['summary']['undecided_boxes']
        previous_seconds=prior['summary']['elapsed_seconds']
        mark=len(done)//200

    def save(result):
        frontier=queue+list(pending.values())
        summary={'result':result,'precision_decimal_digits':30,'rectangle':box_string(ROOT),'modular_restriction':'Re(tau)^2+Im(tau)^2>=1','omitted_square_radius':str(LOCAL),'certified_boxes':len(done),'omitted_boxes':len(left_out),'outside_modular_domain_boxes':len(excluded),'pending_boxes':len(frontier),'undecided_boxes':undecided,'elapsed_seconds':previous_seconds+time.time()-start}
        payload={'summary':summary,'certified':done,'omitted':left_out,'outside_modular_domain':excluded,'pending':[box_string(b) for b in frontier]}
        (base/'f_interval_parallel_certificate.json').write_text(json.dumps(payload,indent=2)+'\n')
        (base/'f_interval_parallel.out.txt').write_text(json.dumps(summary,indent=2)+'\n')
        return summary

    with ProcessPoolExecutor(max_workers=6) as pool:
        while queue or pending:
            while queue and len(pending)<12:
                box=queue.pop()
                if outside_domain(box):
                    excluded.append(box_string(box))
                elif omitted(box):
                    left_out.append(box_string(box))
                else:
                    pending[pool.submit(do_box,box)]=box
            if not pending:
                continue
            finished,_=wait(pending,return_when=FIRST_COMPLETED)
            for future in finished:
                box=pending.pop(future)
                ok,why=future.result()
                if ok:
                    done.append({'box':box_string(box),'certificate':why})
                elif max(box[1]-box[0],box[3]-box[2])<LOCAL/2048:
                    undecided.append({'box':box_string(box),'certificate':why})
                else:
                    queue.extend(split(box))
            if len(done)//200>mark:
                mark=len(done)//200
                summary=save('RUNNING')
                print('progress',len(done),'pending',summary['pending_boxes'],'undecided',len(undecided),'seconds',round(summary['elapsed_seconds'],2),flush=True)
            if len(undecided)>30:
                aborted=True
                break
    summary=save('PASS' if not aborted and not queue and not pending and not undecided else 'UNFINISHED')
    print(json.dumps(summary,indent=2),flush=True)
