"""Different-method recomputation after printed-proof comparison.

Triangulations of Delta_2 x [0,1] are maximal chains in the Boolean lattice:
at generic base barycentric coordinates a tetrahedron gives one vertical
interval, and the three intervals concatenate by adding one coordinate.
This method does not test polyhedral intersections. Lattice regularity is
verified by Smith form; chart maps are recovered from character pairings.
"""
from pathlib import Path
from itertools import permutations,combinations
import datetime,json
import sympy as S
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
B=Path(__file__).parent
lower=('a','b','e');upper=('c','d','f')
rays={'a':(0,0,1,0),'b':(1,0,1,0),'c':(0,1,1,0),
      'd':(1,1,1,0),'e':(0,0,0,1),'f':(0,1,0,1)}
chains=[]
for order in permutations(range(3)):
 # Add coordinates in order to a subset. An interval [sum_S lambda,
 # sum_(S union i) lambda] corresponds to the tetrahedron with upper
 # vertices S union i and lower vertices outside S.
 subset=set();ts=[];intervals=[]
 for i in order:
  t=tuple(sorted([upper[j] for j in subset|{i}]+[lower[j] for j in range(3) if j not in subset]))
  assert len(t)==4
  ts.append(t);intervals.append([sorted(subset),sorted(subset|{i})]);subset.add(i)
 assert subset=={0,1,2}
 chains.append({'order':order,'tetrahedra':sorted(ts),'intervals':intervals})
assert len({tuple(x['tetrahedra']) for x in chains})==6

def faces(ts):
 cnt={}
 for t in ts:
  for f in combinations(t,3):cnt[f]=cnt.get(f,0)+1
 return {f for f,n in cnt.items() if n==1}
bottom={tuple('abc'),tuple('bcd')};G={'a':'b','c':'d','e':'e','f':'f'}
fixed=[];good=[]
for c in chains:
 fs=faces(c['tetrahedra'])
 if {f for f in fs if set(f)<=set('abcd')}!=bottom:continue
 fixed.append(c)
 left={f for f in fs if set(f)<=set('acef')};right={f for f in fs if set(f)<=set('bdef')}
 if {tuple(sorted(G[v] for v in f)) for f in left}==right:good.append(c)
assert len(fixed)==3 and len(good)==2

chars={'x':(0,1,0,0),'y':(0,-1,1,1),'z':(1,0,0,0),
       'v':(-1,0,1,0),'u':(0,0,0,1),'q':(0,0,1,0)}
atlas=[]
for c in good:
 charts=[]
 for t in c['tetrahedra']:
  M=S.Matrix.hstack(*(S.Matrix(rays[v]) for v in t))
  D=smith_normal_form(M,domain=ZZ)
  smith=[int(D[i,i]) for i in range(4)]
  assert all(abs(d)==1 for d in smith)
  # Column vectors of M^(-T) are the four regular chart characters.
  dual=M.inv().T
  assert all(z.q==1 for z in dual)
  exps={k:[int(z) for z in M.T*S.Matrix(m)] for k,m in chars.items()}
  assert all(z>=0 for v in exps.values() for z in v)
  assert [x+y for x,y in zip(exps['x'],exps['y'])]==[
    u+z+v for u,z,v in zip(exps['u'],exps['z'],exps['v'])]
  assert exps['q']==[z+v for z,v in zip(exps['z'],exps['v'])]
  assert all(q*u==0 for q,u in zip(exps['q'],exps['u']))
  assert set(exps['q']+exps['u'])<={0,1}
  assert sum(exps['u']) in (1,2)
  charts.append({'rays':''.join(t),'smith_diagonal':smith,'affine_character_basis':
   [[int(dual[i,j]) for i in range(4)] for j in range(4)],'map_exponents':exps})
 atlas.append(charts)

result={'computed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'timing':'After target proofs were read; this is a new computation, not an unopened-proof derivation.',
 'method':'Boolean maximal chains / vertical barycentric intervals, Smith normal form, character lattice pairings; no halfspace-intersection enumeration.',
 'all_chains':[{'order':list(x['order']),'tetrahedra':[''.join(t) for t in x['tetrahedra']],
   'intervals':x['intervals']} for x in chains],
 'fixed_bottom_count':len(fixed),'period_invariant_count':len(good),'atlas':atlas,
 'scope':'A2.1 finite classification and regularity; A2.2 toric local chart exponents, fixed bottom, q/u flatness and reduced two-branch central charts. Global gluing is the disclosed A1.2 input.'}
(B/'S6_SERIES_PUBLISH_I_push_A2_staircases.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
