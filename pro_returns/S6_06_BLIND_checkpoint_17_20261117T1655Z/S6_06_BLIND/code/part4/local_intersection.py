from pathlib import Path
import json
import sympy as s
a,b,c=s.symbols('a b c')
W=s.Matrix([[1,0,0],[0,1,0],[0,0,1],[a,b,c]])
pairs=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
Q=s.zeros(6)
for i,(p,q) in enumerate(pairs):
 for j,(r,t) in enumerate(pairs):
  if len({p,q,r,t})==4:
   v=[p,q,r,t]
   Q[i,j]=(-1)**sum(v[k]>v[l] for k in range(4) for l in range(k+1,4))
B=s.Matrix([[W.extract([i,j],[k,l]).det() for k,l in [(0,1),(0,2),(1,2)]] for i,j in pairs])
G=s.simplify(B.T*Q*B)
assert G==s.zeros(3)
out={'status':'PASS','basis_H2':['e1e2','e1e3','e1e4','e2e3','e2e4','e3e4'],'torus_intersection':[[int(v) for v in row] for row in Q.tolist()],'exterior_square_columns':[[str(v) for v in row] for row in B.tolist()],'restricted_intersection':[[int(v) for v in row] for row in G.tolist()]}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('Local torus intersection restriction: PASS')
print('Restricted pairing:',G)
