#!/usr/bin/env python3
"""Independent validation of saved partitions, domains, signs and finite maps.
This does not replace running the interval ODE program; it independently
checks the exact finite coverage and the serialized certified inequalities.
"""
import os,sys,json,hashlib
from fractions import Fraction as Q
from pathlib import Path
HERE=Path(__file__).resolve().parent
for candidate in [os.environ.get('PAPER_V_VENDOR'),str(HERE/'vendor'),str(HERE.parent/'vendor'),str(HERE.parents[1]/'vendor')]:
    if candidate and Path(candidate).exists():sys.path.insert(0,candidate)
from flint import arb,acb,acb_mat,ctx
ctx.dps=120
OUT=Path(os.environ.get('PAPER_V_OUTPUT_DIR',str((HERE.parent if HERE.name=='code' else HERE)/'output')))
def cb(text):
    if not text.endswith('j'):return acb(arb(text))
    text=text[:-1]
    if ' + ' in text:
        re,im=text.rsplit(' + ',1);return acb(arb(re),arb(im))
    if ' - ' in text:
        re,im=text.rsplit(' - ',1);return acb(arb(re),-arb(im))
    return acb(0,arb(text))
def rb(q):q=Q(q);return arb(q.numerator)/q.denominator
def child(b,k):
    x0,x1,y0,y1=b;xm=(x0+x1)/2;ym=(y0+y1)/2
    return [(x0,xm,y0,ym),(xm,x1,y0,ym),(x0,xm,ym,y1),(xm,x1,ym,y1)][k]
def rr(b):
    x0,x1,y0,y1=b
    near=lambda a,b:Q(0)if a<=0<=b else min(abs(a),abs(b))
    return near(x0,x1)**2+near(y0,y1)**2,max(x0*x0,x1*x1)+max(y0*y0,y1*y1)
def zb(b):
    x0,x1,y0,y1=b
    return acb(arb(rb((x0+x1)/2),rb((x1-x0)/2)),arb(rb((y0+y1)/2),rb((y1-y0)/2)))
U=arb('-1.0945402503114027801162682630549457037')
endpoint=json.loads((OUT/'fresh_frobenius.json').read_text())
assert U>arb(endpoint['h_b']['infinity'])
summary={};total=0;positive=0;geometric=0
for kind in ['infinity','zero','cusp','collar']:
    meta=json.loads((OUT/f'fresh_cover_{kind}.json').read_text());seed=tuple(map(Q,meta['initial_closed_rectangle']))
    records=[json.loads(line)for line in (OUT/f'fresh_cover_{kind}.jsonl').read_text().splitlines()]
    paths={r['path']for r in records};assert len(paths)==len(records)
    mass=Q(0);area=Q(0);counts={'positive':0,'geometric':0}
    for rec in records:
        key=rec['path'];assert all(k in '0123'for k in key)
        assert all(key[:i]not in paths for i in range(len(key)))
        box=seed
        for k in key:box=child(box,int(k))
        assert box==tuple(map(Q,rec['box']))
        mass+=Q(1,4**len(key));area+=(box[1]-box[0])*(box[3]-box[2]);lo,hi=rr(box);reason=rec['reason']
        if reason=='strict_height_bound':
            assert arb(rec['height_lower']).lower()>U.upper()
            assert len(set(rec['selected_rows']))==4 and set(rec['selected_rows'])<=set(range(5))
            counts['positive']+=1
        else:
            counts['geometric']+=1
            if reason=='outside_root_disc':assert kind in ['infinity','zero']and lo>Q(49,50)**2
            elif reason=='central_hessian_square':assert kind=='infinity'and max(map(abs,box))<=Q(1,10)
            elif reason=='outside_collar_outer_disc':assert kind=='collar'and lo>Q(103,100)**2
            elif reason=='inside_collar_inner_disc':assert kind=='collar'and hi<Q(49,50)**2
            elif reason=='covered_by_cusp_disc':assert kind=='collar'and(-zb(box)**(-5)-1).abs_upper()<=rb(Q(1,4))
            elif reason=='outside_cusp_disc':assert kind=='cusp'and lo>Q(1,4)**2
            elif reason=='inner_cusp_certificate':assert kind=='cusp'and hi<=Q(1,100)**2
            else:raise AssertionError(reason)
    assert mass==1 and area==(seed[1]-seed[0])*(seed[3]-seed[2])
    assert counts['positive']==meta['counts']['positive'] and counts['geometric']==meta['counts']['geometric']
    summary[kind]={'leaves':len(records),'kraft_mass':str(mass),'rational_area':str(area),**counts}
    total+=len(records);positive+=counts['positive'];geometric+=counts['geometric']
assert total==1600 and positive==1088 and geometric==512
assert Q(49,50)**4>=Q(100,103)**5
local=json.loads((OUT/'fresh_local_domains.json').read_text())
assert len(local['central_closed_leaves'])==4
central_area=Q(0)
for rec in local['central_closed_leaves']:
    b=tuple(map(Q,rec['box']));central_area+=(b[1]-b[0])*(b[3]-b[2])
    assert arb(rec['hessian_lower']).lower()>rb(Q(1,4))
    xx,xy,yy=map(arb,[rec['hxx'],rec['hxy'],rec['hyy']])
    assert xx.lower()-xy.abs_upper()>rb(Q(1,4))and yy.lower()-xy.abs_upper()>rb(Q(1,4))
assert central_area==Q(1,25)
assert not cb(local['cusp_lower_block_det']).contains(0)
for c in local['cusp_shifted_det_coefficients']:assert arb(c['lower']).lower()>0
assert arb(local['cusp_anchor']['height'])>arb(endpoint['h_b']['infinity'])
# Recover the point equations from serialized interval matrices independently.
def M(key):return acb_mat([[cb(z)for z in row]for row in endpoint[key]])
X=M('X');U0=M('zero_root_to_base');UI=M('infinity_root_to_base')
assert not X.det().contains(0)
z4=acb(0,1);z5=(acb(0,2)*arb.pi()/5).exp()
def diag(z,exps):return acb_mat([[z**(-exps[i])if i==j else 0 for j in range(6)]for i in range(6)])
T0=diag(z4,[0,6,3,0,-3,-6]);TI=diag(z5,[0,-8,-4,0,4,8])
A=acb_mat([[1,0,0,1,-1,1],[0,1,-1,-1,1,0],[0,1,0,-1,0,0],[0,2,-1,-1,0,1],[0,2,0,-1,0,0],[0,1,1,-1,0,0]])
B=acb_mat([[1,0,0,0,0,0],[0,0,-1,0,1,0],[0,0,-1,0,0,1],[0,0,-1,0,0,0],[0,1,-1,0,0,0],[0,0,-1,1,0,0]])
for res in [X*U0.inv()*T0*U0-B*X,X*UI.inv()*TI*UI-A*X]:assert all(res[i,j].contains(0)for i in range(6)for j in range(6))
c0=96/(625*arb.pi())
for key,Uroot in [('zero',U0),('infinity',UI)]:assert(-c0*(X*Uroot.inv())[0,3].real).overlaps(arb(endpoint['h_b'][key]))
files=list(HERE.glob('*.py'))+list(OUT.glob('fresh*.json'))+list(OUT.glob('fresh_cover_*.jsonl'))
hashes={str(p.relative_to(HERE.parent if HERE.name=='code'else HERE)):hashlib.sha256(p.read_bytes()).hexdigest()for p in files}
result={'checker':'GPT-6 Astra, ChatGPT Pro mode, inherited effort; same model family','verification':'independent saved-data coverage, geometric exclusion and serialized-sign validation; normalized finite maps checked again from saved matrices','domains':summary,'positive_leaves':positive,'geometric_leaves':geometric,'total_outer_leaves':total,'central_hessian_leaves':4,'central_area':'1/25','all_partitions_complete':True,'all_inequalities_strict':True,'cusp_positive_coefficients':True,'normalized_intertwiner_saved_residuals_contain_zero':True,'input_sha256':hashes}
(OUT/'saved_certificate_validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items()if k!='input_sha256'},indent=2))
