"""New root-curve floor arithmetic and characteristic consistency checks."""
from pathlib import Path
from itertools import combinations
from fractions import Fraction
from math import floor
import json
import sympy as s

def line(r):
    d=floor(Fraction(4*r,5))+floor(Fraction(-3*r,4))
    return {'power':r,'coarse_degree':d,'h0':max(d+1,0),'h1':max(-d-1,0)}
def wedge_weights(weights,q):return [sum(x) for x in combinations(weights,q)]
G=[0,-1,-2]
direct=[]
cohom=[0]*5
for q in range(4):
    ws=wedge_weights(G,q);ls=[line(r) for r in ws]
    direct.append({'q':q,'weights':ws,'lines':ls})
    cohom[q]+=sum(t['h0'] for t in ls)
    cohom[q+1]+=sum(t['h1'] for t in ls)
assert cohom==[1,1,0,0,0]
F=[0,1,2];log_e1={}
for p in range(5):
    weights=wedge_weights(F,p)+[11+r for r in wedge_weights(F,p-1)] if p>=1 else [0]
    groups=[0]*5
    for q in range(4):
        for a in weights:
            for b in wedge_weights(G,q):
                L=line(a+b);groups[q]+=L['h0'];groups[q+1]+=L['h1']
    log_e1[p]={'filtration_weights':weights,'associated_graded_H':groups}
H=[[1,1,0,0,0],[0,2,1,0,0],[0,1,6,1,0],[0,0,1,2,0],[0,0,0,1,1]]
chi=[sum((-1)**q*H[p][q] for q in range(5)) for p in range(5)]
assert chi==[0,-1,4,-1,0]
assert all(H[p][q]==H[4-p][4-q] for p in range(5) for q in range(5))
assert sum((-1)**p*chi[p] for p in range(5))==6
assert sum(chi)==2
cc=s.symbols('c2sq');todd=(3*cc-6)/720;sig=(3*cc+84)/45
possible=[k for k in range(-10,11) if abs(2+16*k)<=4]
assert possible==[0]
out={'method':'rational floor pushforward of root line bundles; exterior subset enumeration; exact characteristic identities',
  'line_weights':[line(r) for r in range(-22,23)],'structure_direct_images':direct,
  'structure_cohomology':cohom,'logarithmic_associated_graded_only':log_e1,
  'printed_hodge_table_consistency':{'chi_p':chi,'euler':6,'signature':2,'Serre_duality':True},
  'characteristic_numbers':{'c2sq':2,'c4':6,'p1sq':8,'p2':14,'signature':2,'Todd_genus':0},
  'scope':'Associated-graded dimensions and characteristic consistency do not establish the connecting-map ranks or the full Hodge/tangent tables.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
print(json.dumps({'structure_cohomology':cohom,'hodge_characteristic_checks':'passed','log_associated_graded':log_e1,'scope':out['scope']},indent=2))
