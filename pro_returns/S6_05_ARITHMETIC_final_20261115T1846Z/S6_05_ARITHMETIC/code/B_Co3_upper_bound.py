"""Independent exact upper bound for the norm-six vector stabilizer.

The 552 minimal vectors meeting v in 3 span R^24. Their Gram graph has
automorphism group 2.Co3; a displayed graph automorphism does not preserve
the Leech lattice.  The already verified Co3 subgroup has index two, so
the full lattice stabilizer has exactly the claimed order.
"""
from B_global_lattice import *
from sympy.combinatorics import Permutation,PermutationGroup
import pynauty
v=np.array([5]+[1]*23,dtype=np.int64)
roots=np.load(REC/'B_standard_Leech_minimal.npz')['vectors'].astype(np.int64)
S=roots[(roots@v)==24];assert S.shape==(552,24)
G=S@S.T//8;assert set(G.flat)=={-1,1,2,4}
# Encode the exceptional -1 matching with 276 extra vertices.  Edges of
# inner product one and edges to matching vertices have separate colors.
adj={i:np.flatnonzero(G[i]==1).tolist() for i in range(552)}
for i in range(552):
 j=int(np.flatnonzero(G[i]==-1)[0])
 if i<j:
  k=len(adj);adj[k]=[i,j];adj[i].append(k);adj[j].append(k)
graph=pynauty.Graph(len(adj),adjacency_dict=adj,vertex_coloring=[set(range(552)),set(range(552,len(adj)))])
gg,ma,ex,_,_=pynauty.autgrp(graph)
PG=PermutationGroup([Permutation(g[:552]) for g in gg]);order=int(PG.order())
print('Gram graph vertices',len(adj),'exact permutation group order',order,flush=True)
assert order==2*495766656000
_,piv=rr(S.T,1000003);assert len(piv)==24
A=fmpq_mat(S[piv].tolist());AI=A.inv();LB=qmat(json.loads((REC/'B_standard_Leech_basis.json').read_text())['basis']);LI=LB.inv()
outside=[];saved=[]
for p in gg:
 T=AI*fmpq_mat(S[[p[i] for i in piv]].tolist());assert fmpq_mat(S.tolist())*T==fmpq_mat(S[p[:552]].tolist())
 assert T*T.transpose()==fmpq_mat([[int(i==j) for j in range(24)] for i in range(24)])
 LT=LB*T*LI;integral=all(x.denominator==1 for row in qrows(LT) for x in row)
 if not integral:outside.append(len(saved))
 saved.append({'permutation':p[:552],'matrix_physical':qjson(T),'preserves_Leech':integral})
assert outside
(REC/'B_Co3_upper_bound.json').write_text(json.dumps({'graph_order':order,'full_vector_stabilizer_order':order//2,'outside_generator_indices':outside,'graph_generators':saved}))
print('Graph automorphisms failing lattice preservation:',outside,flush=True)
print('PASS full norm-six vector stabilizer = 495766656000; full line stabilizer = 991533312000.',flush=True)
