"""Explicit integral generators and independent order for the B.5 group."""
from B_global_lattice import *
from B_exact_lattices import J,over,gram
from sympy.combinatorics import Permutation,PermutationGroup
D=json.loads((REC/'B_autJ_data.json').read_text());gg=[fmpq_mat(g) for g in D['AutJ_generators']];pp=D['plane_permutations'];I=fmpq_mat([[int(i==j) for j in range(24)] for i in range(24)])
queue=[5];trans={5:I};tw={5:[]}
for x in queue:
 for i,p in enumerate(pp):
  y=p[x]
  if y not in trans:trans[y]=trans[x]*gg[i];tw[y]=tw[x]+[i];queue.append(y)
assert len(queue)==6
L=qmat(over[5][2]);JB=qmat(J);GJ=qmat(gram(J));C=L*(GJ.inv()*JB).transpose()/144;LC=C.inv();GL=C*GJ*C.transpose()
rootC=qmat(D['J_coordinates_in_root_basis']);rootCi=rootC.inv();roots=[]
for i in range(12):
 for a,b in [(1,0),(0,1),(1,1),(-1,0),(0,-1),(-1,-1)]:
  v=[0]*24;v[2*i:2*i+2]=[a,b];roots.append(v)
index={tuple(r):i for i,r in enumerate(roots)};R=fmpq_mat(roots);PG=PermutationGroup([Permutation(list(range(72)))]);gens=[];perms=[];words=[]
for x in queue:
 for i,g in enumerate(gg):
  y=pp[i][x];h=trans[x]*g*trans[y].inv();T=C*h*LC;assert T*GL*T.transpose()==GL and abs(T.det())==1;mat=ints(T)
  im=ints(R*rootCi*h*rootC);p=Permutation([index[tuple(v)] for v in im])
  if PG.contains(p):continue
  perms.append(p);PG=PermutationGroup(perms);gens.append(mat);words.append({'transversal':tw[x],'generator':i,'inverse_transversal':tw[y]})
assert int(PG.order())==2099520
(REC/'B_specific_plane_group.json').write_text(json.dumps({'order':int(PG.order()),'L0_Gram':ints(GL),'generators_in_L0_basis':gens,'permutations_on_intrinsic_72_roots':[p.array_form for p in perms],'Schreier_words_in_AutJ_generators':words,'extension_orbit':queue}))
print('B.5 full plane stabilizer: integral generators',len(gens),'independent faithful permutation order',PG.order())
print('All determinants, Gram identities, and six-extension Schreier identities verified exactly.')
