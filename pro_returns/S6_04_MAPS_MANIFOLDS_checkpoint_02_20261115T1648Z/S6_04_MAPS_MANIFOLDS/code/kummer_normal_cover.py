"""Finite quotient used to globalize a Kummer cusp with normal source.

Exact arithmetic throughout. Search all elements of G_N for N=2,3,4;
the proof works for every N without this finite check.
"""
from collections import deque
from pathlib import Path
import json
A1=((1,0,0,0),(6,0,1,0),(-6,-1,-1,0),(-2,1,0,1))
A2=((1,0,0,0),(0,0,-1,0),(-6,1,0,0),(3,0,1,1))
I=tuple(int(i==j) for i in range(4) for j in range(4))
def mul(a,b,n):
 return tuple(sum(a[4*i+k]*b[4*k+j] for k in range(4))%n
              for i in range(4) for j in range(4))
results=[]
for n in (2,3,4):
 generators=[(tuple(x%n for row in A1 for x in row),(-1)%n),
             (tuple(x%n for row in A2 for x in row),0)]
 seen={(I,0)};todo=deque(seen)
 while todo:
  a,k=todo.popleft()
  for b,l in generators:
   c=(mul(a,b,n),(k+l)%n)
   if c not in seen:seen.add(c);todo.append(c)
 result={'N':n,'G_N_order':len(seen),'global_degree':n*n*len(seen),
         'specified_cusp_component_degree':n**3}
 assert len(seen)%n==0
 results.append(result);print(result,flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(results,indent=2))
