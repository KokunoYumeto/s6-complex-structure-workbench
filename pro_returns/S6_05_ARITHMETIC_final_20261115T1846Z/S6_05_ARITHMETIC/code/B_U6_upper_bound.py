"""Independent full upper bound for the 6_22 isotropic-line stabilizer.

The three shortest representatives of a nonzero 6_22 class form a
triangle.  Their pairwise differences/3 form a minimal-vector triangle.
The 891 minimal vectors with inner products (2,0) with its first two
vectors give a faithful Gram graph for the pointwise stabilizer.  We
test every coset of the known pointwise subgroup in that Gram group for
integrality on the Leech lattice, hence obtain a full upper bound.
"""
from B_global_lattice import *
from sympy.combinatorics import Permutation,PermutationGroup
import pynauty
D=json.loads((REC/'B_rare_stabilizers.json').read_text())['622']
gens=[fmpq_mat(g['matrix_times8'])/8 for g in D['generators']]
I=fmpq_mat([[int(i==j) for j in range(24)] for i in range(24)])
vv=[]
for k in range(3):
 v=[0]*24;v[1:4]=[4,4,4];v[1+k]=-8;vv.append(v)
V=fmpq_mat(vv);vi={tuple(v):i for i,v in enumerate(vv)}
perms=[tuple(vi[tuple(x)] for x in ints(V*g)) for g in gens]
# Exact Schreier generators fixing the three representatives pointwise.
todo=[(0,1,2)];trans={(0,1,2):I};edges=[]
for p in todo:
 for g,q in zip(gens,perms):
  pq=tuple(q[p[i]] for i in range(3))
  if pq not in trans:trans[pq]=trans[p]*g;todo.append(pq)
assert len(todo)==6
kg=[]
for p in todo:
 for g,q in zip(gens,perms):
  pq=tuple(q[p[i]] for i in range(3));h=trans[p]*g*trans[pq].inv();assert V*h==V
  if h!=I:kg.append(h)
roots=np.load(REC/'B_standard_Leech_minimal.npz')['vectors'].astype(np.int64)
a=np.zeros(24,dtype=np.int64);a[1]=-4;a[2]=4
b=np.zeros(24,dtype=np.int64);b[2]=-4;b[3]=4
S=roots[((roots@a)==16)&((roots@b)==0)];assert S.shape==(891,24)
Gram=S@S.T//8;adj={i:np.flatnonzero(Gram[i]==0).tolist() for i in range(891)}
gg,ma,ex,_,_=pynauty.autgrp(pynauty.Graph(891,adjacency_dict=adj))
BG=PermutationGroup([Permutation(g) for g in gg]);Bord=int(BG.order())
assert all(np.array_equal(Gram[np.array(g)[:,None],np.array(g)[None,:]],Gram) for g in gg)
print('891-vector Gram graph group order:',Bord,flush=True)
index={tuple(x):i for i,x in enumerate(S)};kp=[]
for h in kg:
 im=ints(fmpq_mat(S.tolist())*h);kp.append(Permutation([index[tuple(x)] for x in im]))
KG=PermutationGroup(kp);Kord=int(KG.order());assert Kord==9196830720 and BG.is_subgroup(BG)
assert all(BG.contains(p) for p in kp);cosets=BG.coset_transversal(KG)
print('Verified pointwise triangle subgroup:',Kord,'Gram-group cosets:',len(cosets),flush=True)
_,piv=rr(S.T,1000003);assert len(piv)==23
A=fmpq_mat(S[piv].tolist()+[b.tolist()]);AI=A.inv();LB=qmat(json.loads((REC/'B_standard_Leech_basis.json').read_text())['basis']);LI=LB.inv();accepted=[];checks=[]
for j,p in enumerate(cosets):
 T=AI*fmpq_mat(S[[p(i) for i in piv]].tolist()+[b.tolist()]);assert fmpq_mat(S.tolist())*T==fmpq_mat(S[[p(i) for i in range(891)]].tolist()) and V*T==V
 assert T*T.transpose()==I
 LT=LB*T*LI;integral=all(x.denominator==1 for row in qrows(LT) for x in row)
 if integral:accepted.append(j)
 checks.append({'permutation':p.array_form,'matrix_physical':qjson(T),'preserves_Leech':integral})
assert len(accepted)==1
(REC/'B_U6_upper_bound.json').write_text(json.dumps({'Gram_graph_order':Bord,'pointwise_triangle_order':Kord,'coset_checks':checks,'full_class_stabilizer_order':6*Kord,'full_line_stabilizer_order':12*Kord,'kernel_generator_matrices_physical':[qjson(h) for h in kg]}))
print('Cosets preserving the Leech lattice:',accepted,flush=True)
print('PASS full pointwise triangle stabilizer = 9196830720; class stabilizer = 55180984320; line stabilizer = 110361968640.',flush=True)
