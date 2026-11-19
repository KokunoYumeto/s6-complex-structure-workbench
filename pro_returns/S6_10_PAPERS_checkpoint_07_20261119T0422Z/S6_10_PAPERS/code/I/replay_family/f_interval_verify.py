"""Independent exact-rational verification that the saved boxes cover.

This does not re-use the search queue. It reconstructs the deterministic
binary partition from its root and consumes the saved certified/omitted
leaves. It also checks all reported strict interval acceptance inequalities.
"""
from pathlib import Path
from fractions import Fraction as F
import json

base=Path(__file__).parent
data=json.loads((base/'f_interval_parallel_certificate.json').read_text())
assert data['summary']['result']=='PASS', 'the analytic cover is unfinished'
assert not data['pending'] and not data['summary']['undecided_boxes']
local=F(1,10000)
root=(F(0),F(1,2),F(17,20),F(2))

def box(s): return tuple(F(v) for v in s)
def iv_upper(s): return F(s.rstrip(']').split(',')[-1].strip())

leaves={}
max_bound=F(0)
for record in data['certified']:
    b=box(record['box'])
    assert b not in leaves
    c=record['certificate']
    assert c['reason']=='norm bound'
    norm=iv_upper(c['norm_squared_upper'])
    assert norm<2
    assert iv_upper(c['operator_norm_upper'])<1
    assert iv_upper(c['radius'])>0
    max_bound=max(max_bound,norm)
    leaves[b]='certified'
for row in data['omitted']:
    b=box(row)
    assert b not in leaves
    assert 0<=b[0]<=b[1]<=local
    assert 1-local<=b[2]<=b[3]<=1+local
    leaves[b]='omitted'
for row in data.get('outside_modular_domain',[]):
    b=box(row)
    assert b not in leaves
    assert b[1]**2+b[3]**2<1
    leaves[b]='outside modular domain'

for b in leaves:
    assert root[0]<=b[0]<b[1]<=root[1]
    assert root[2]<=b[2]<b[3]<=root[3]

original_count=len(leaves)
area=sum((b[1]-b[0])*(b[3]-b[2]) for b in leaves)
assert area==F(23,40)
max_depth=0

def reconstruct(b,depth=0):
    global max_depth
    max_depth=max(max_depth,depth)
    if b in leaves:
        del leaves[b]
        return
    assert depth<60, 'a hole or a nonconforming rectangle remains'
    x0,x1,y0,y1=b
    if x1-x0>=y1-y0:
        mid=(x0+x1)/2
        reconstruct((x0,mid,y0,y1),depth+1)
        reconstruct((mid,x1,y0,y1),depth+1)
    else:
        mid=(y0+y1)/2
        reconstruct((x0,x1,y0,mid),depth+1)
        reconstruct((x0,x1,mid,y1),depth+1)

reconstruct(root)
assert not leaves, 'overlapping or extraneous leaves remain'
text='\n'.join([
    'PASS: independent exact-rational cover reconstruction.',
    f'Consumed leaves: {original_count}',
    f'Certified norm boxes: {len(data["certified"])}',
    f'Local analytic squares: {len(data["omitted"])}',
    f'Boxes strictly inside the unit circle: {len(data.get("outside_modular_domain",[]))}',
    f'Exact covered area: {area}',
    f'Maximum partition depth: {max_depth}',
    f'Largest reported squared-norm upper bound, exact decimal rational: {max_bound}',
    'Every certified norm upper bound is strictly below 2.',
    'Every omitted box lies in the explicitly certified local square.',
    'Every domain-excluded box satisfies x_upper^2+y_upper^2<1 exactly.',
])+'\n'
print(text,end='')
(base/'f_interval_verify.out.txt').write_text(text)
