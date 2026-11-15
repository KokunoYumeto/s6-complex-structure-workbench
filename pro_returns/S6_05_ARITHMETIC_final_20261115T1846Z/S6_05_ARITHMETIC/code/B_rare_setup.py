"""Certified full stabilizers for the two all-Leech isotropic line types."""
from B_global_lattice import *
from mmgroup import mat24,MM0,Xsp2_Co1,generators as gen
from sympy.combinatorics import Permutation,PermutationGroup
from itertools import combinations,product
MASK=(1<<24)-1

def pack(v):
 a=b=0
 for i,x in enumerate(v):
  if x%3==1:a|=1<<i
  elif x%3==2:b|=1<<i
 return a|(b<<24)
def unpack(a):return np.array([((a>>i)&1)+2*((a>>(24+i))&1) for i in range(24)],dtype=np.int64)
def reduce(v):
 a=np.zeros(12,dtype=np.uint32);ret=int(gen.gen_leech3_reduce_leech_mod3(int(v),a));assert ret>=0;return a[:ret>>48],ret&((1<<48)-1)
def apply(v,w):return int(gen.gen_leech3_op_vector_word(int(v),w,len(w)))
def neg(v):return int(gen.gen_leech3_neg(int(v)))

codes=[int(mat24.gcode_to_vect(i)) for i in range(4096)];octads=[c for c in codes if c.bit_count()==8];assert len(octads)==759
roots=[]
for i,j in combinations(range(24),2):
 for a,b in product([-4,4],repeat=2):
  v=[0]*24;v[i]=a;v[j]=b;roots.append(v)
for c in octads:
 inds=[i for i in range(24) if(c>>i)&1]
 for m in range(128):
  signs=[(m>>j)&1 for j in range(7)];signs.append(sum(signs)%2);v=[0]*24
  for i,s in zip(inds,signs):v[i]=-2 if s else 2
  roots.append(v)
for i in range(24):
 for c in codes:
  v=[-1 if(c>>j)&1 else 1 for j in range(24)];v[i]*=-3;roots.append(v)
roots=np.array(roots,dtype=np.int16);assert roots.shape==(196560,24) and np.all(np.sum(roots*roots,axis=1)==32)
np.savez_compressed(REC/'B_standard_Leech_minimal.npz',vectors=roots)
# Complete physical-coordinate lattice basis (the scalar product is /8).
e0=[0]*24;e0[0]=8;bg=[e0]
for i in range(1,24):v=[0]*24;v[i]=4;v[0]=-4;bg.append(v)
for j in range(12):bg.append([2*((codes[1<<j]>>i)&1) for i in range(24)])
bg.append([-3]+[1]*23);LB=fmpq_mat(hnf(bg));LG=LB*LB.transpose()/8;assert LG.det()==1 and all(int(LG[i,i])%2==0 for i in range(24));LBi=LB.inv()

results={}
for typ in ['3','622']:
 if typ=='3':
  v=np.array([5]+[1]*23,dtype=np.int64);v3=pack(v);v2=int(gen.gen_leech3to2(v3))&MASK
  sel=roots[(roots@v)==24];assert len(sel)==552
  pairs=sorted(set(min(int(gen.gen_leech3to2_short(pack(r)))&MASK,(int(gen.gen_leech3to2_short(pack(r)))&MASK)^v2) for r in sel));assert len(pairs)==276
  index={a:i for i,a in enumerate(pairs)};target=495766656000
 else:
  v=np.zeros(24,dtype=np.int64);v[1]=-8;v[2]=v[3]=4;v3=pack(v)
  x=[0]*24;x[1]=-4;x[2]=4;y=[0]*24;y[2]=-4;y[3]=4
  x2=int(gen.gen_leech3to2_short(pack(x)))&MASK;y2=int(gen.gen_leech3to2_short(pack(y)))&MASK
  aa=np.zeros(891,dtype=np.uint32);ret=gen.gen_leech2_u4_2xx(x2,y2,gen.rand_get_seed(),aa);assert ret==891
  pairs=sorted(map(int,aa));index={a:i for i,a in enumerate(pairs)};assert len(index)==891
  assert all(gen.gen_leech2_type(a)==4 and all(gen.gen_leech2_type(a^b)==2 for b in [x2,y2,x2^y2]) for a in pairs)
  target=55180984320
 base,red=reduce(v3);baseg=MM0('a',base);gens=[];pg=[];group=PermutationGroup([Permutation(list(range(len(pairs))))])
 for trial in range(100):
  w=MM0('r','G_x0');im=apply(v3,w.mmdata);t,rr=reduce(im);assert rr==red
  h=w*MM0('a',t)*baseg**-1;word=h.mmdata.copy();vv=apply(v3,word);assert vv in [v3,neg(v3)]
  M=Xsp2_Co1(h).leech_op.astype(np.int64);assert np.array_equal(M@M.T,64*np.eye(24,dtype=np.int64))
  assert np.all((v@M)%8==0)
  vm=v@M//8
  if pack(vm)==neg(v3):M=-M;vm=-vm
  assert pack(vm)==v3
  if typ=='3':assert np.array_equal(vm,v)
  else:assert sorted(vm[1:4])==[-8,4,4] and np.count_nonzero(vm)==3
  T=fmpq_mat(M.tolist())/8;coords=LB*T*LBi;ints(coords);assert coords.det() in [-1,1]
  p=[]
  for a in pairs:
   b=int(gen.gen_leech2_op_word(a,word,len(word)))&MASK
   if typ=='3':b=min(b,b^v2)
   p.append(index[b])
  perm=Permutation(p)
  if group.contains(perm):continue
  pg.append(perm);group=PermutationGroup(pg);gens.append({'word':word.tolist(),'matrix_times8':M.tolist(),'permutation':p});order=int(group.order());print('line',typ,'generators',len(gens),'permutation order',order,flush=True)
  if order==target:break
 assert int(group.order())==target
 results[typ]={'vector':v.tolist(),'packed':v3,'order_vector_stabilizer':target,'permutation_degree':len(pairs),'generators':gens}
(REC/'B_rare_stabilizers.json').write_text(json.dumps(results));(REC/'B_standard_Leech_basis.json').write_text(json.dumps({'basis':ints(LB),'Gram':ints(LG)}))
