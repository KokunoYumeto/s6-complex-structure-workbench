"""Fresh bookkeeping certificate; no target proof or producing code imported."""
import json
from pathlib import Path
import sympy as s

a, rank, extra, defect = s.symbols('a rank extra defect', integer=True)
h1S = 1 + a
h0Q = h1S-rank
h0LC = a+extra
h1LC = h0Q-defect
chi = s.expand(h0LC-h1LC)
assert chi == rank+extra+defect-1
assert s.expand(chi.subs(rank,0)+1) == extra+defect
assert s.expand(chi.subs(rank,1)) == extra+defect
checks=0
for aa in (0,1):
    for rr in range(aa+2):
        for ee in range(8):
            for dd in range(2+aa-rr):
                value=int(chi.subs({a:aa,rank:rr,extra:ee,defect:dd}))
                assert value >= -1
                if rr>=1: assert value>=0
                checks+=1

r, delta, branches, gap = s.symbols('r delta branches gap', nonnegative=True)
chiC = r-delta
eC = 2*r-branches
assert s.expand((delta-branches)+chiC) == r-branches
# With e=0, delta>=branches and chi>=0 force 0<=-r.
assert s.expand(((delta-branches)+chiC).subs(branches,2*r)) == -r
graph_checks=0
for rr in range(21):
    for dd in range(41):
        for bb in range(41):
            if dd>=bb and rr-dd>=0 and 2*rr-bb==0:
                assert (rr,dd,bb)==(0,0,0)
            graph_checks+=1
out={'status':'PASS','dimension_identity':str(chi),
     'dimension_cases':checks,'normalization_cases':graph_checks,
     'scope':'exact dimension/Euler bookkeeping, not finite verification of the sheaf-duality argument'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
