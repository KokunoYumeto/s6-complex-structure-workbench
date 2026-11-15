"""Full stabilizer generators for the three rootless-extension plane classes.

Schreier words are reconstructed from the saved exhaustive flag orbit
trees. Their faithful class-stabilizer permutation orders give the full
flag group. Exact changes of mark then give the full plane group; its
order is checked by the orbit of the anchor among the four plane lines.
"""
from B_global_lattice import *
from mmgroup import generators as gen
from sympy.combinatorics import Permutation,PermutationGroup
import time
I=fmpq_mat([[int(i==j) for j in range(24)] for i in range(24)])
D=json.loads((REC/'B_rare_stabilizers.json').read_text());rows=json.loads((REC/'B_all_129_plane_orbits.json').read_text());rrs=json.loads((REC/'B_rare_plane_orbits.json').read_text())['orbits'];LB=qmat(json.loads((REC/'B_standard_Leech_basis.json').read_text())['basis']);LI=LB.inv();G=LB*LB.transpose()/8
def neg(a):return int(gen.gen_leech3_neg(a))
def add(a,b):return int(gen.gen_leech3_reduce(gen.gen_leech3_add(a,b)))
def act(a,w):return int(gen.gen_leech3_reduce(gen.gen_leech3_op_vector_word(a,w,len(w))))
def mod3(A):return np.array([[x.numerator*pow(x.denominator,-1,3)%3 for x in row] for row in qrows(A)],dtype=np.int64)
def canline(a):
 j=next(i for i,x in enumerate(a) if x);return tuple((a*pow(int(a[j]),-1,3)%3).tolist())
folder=REC/'B_plane_groups';folder.mkdir(exist_ok=True);started=time.time()
for ri,r in enumerate(rrs):
 name=r['line_type'];d=D[name];fid=r['flag_ids'][0];assert len(r['flag_ids'])==1
 data=np.load(REC/f'B_rare_{name}_flag_{fid}.npz');points=data['points'];parents=data['parents'];pgen=data['parent_generator'];index={int(x):i for i,x in enumerate(points)}
 v=d['packed'];pivot=next(i for i in range(24) if ((v>>i)&1) or ((v>>(24+i))&1));vp=((v>>pivot)&1)+2*((v>>(24+pivot))&1)
 def project(w):
  x=((w>>pivot)&1)+2*((w>>(24+pivot))&1);k=x*vp%3
  if k:w=add(w,v if k==2 else neg(v))
  return min(w,neg(w))
 words=[np.array(g['word'],dtype=np.uint32) for g in d['generators']];perms=[Permutation(g['permutation']) for g in d['generators']];mats=[fmpq_mat(g['matrix_times8'])/8 for g in d['generators']]
 degree=d['permutation_degree'];identity=Permutation(list(range(degree)));tp={0:identity};tm={0:I}
 def word(i):
  w=[]
  while i:w.append(int(pgen[i]));i=int(parents[i])
  return list(reversed(w))
 def perm(i):
  if i not in tp:
   p=identity
   for j in word(i):p=p*perms[j]
   tp[i]=p
  return tp[i]
 def matrix(i):
  if i not in tm:
   a=I
   for j in word(i):a=a*mats[j]
   tm[i]=a
  return tm[i]
 assert len(index)==len(points) and int(points[0])==r['representative']
 edges=[]
 for i,x in enumerate(points):
  if i:assert int(parents[i])<i and project(act(int(points[int(parents[i])]),words[int(pgen[i])]))==int(x)
  edges.append([index[project(act(int(x),w))] for w in words])
 target=d['order_vector_stabilizer']//len(points);assert target*len(points)==d['order_vector_stabilizer']
 pp=[];pg=PermutationGroup([identity]);gg=[];sch=[]
 for i,ee in enumerate(edges):
  for j,k in enumerate(ee):
   p=perm(i)*perms[j]*perm(k)**-1
   if pg.contains(p):continue
   pp.append(p);pg=PermutationGroup(pp);h=matrix(i)*mats[j]*matrix(k).inv();gg.append(LB*h*LI);sch.append({'from_point':i,'generator':j,'to_point':k,'from_word':word(i),'to_word':word(k)})
   assert target%int(pg.order())==0
   if int(pg.order())==target:break
  if int(pg.order())==target:break
 assert int(pg.order())==target
 gg.append(-I)
 audit=json.loads((REC/f'B_rare_plane_{ri+1}.json').read_text());mark=[]
 for z in audit['change_of_mark']:
  b=r['representative'] if z['line_index']==0 else v;w=np.array(z['word'],dtype=np.uint32);k=index[project(act(b,w))]
  T=qmat(z['matrix_in_Leech_basis'])*(LB*matrix(k)*LI).inv();gg.append(T);mark.append({'line_index':z['line_index'],'mark_word':z['word'],'inverse_flag_transversal_point':k,'inverse_flag_transversal_word':word(k)})
 P=np.array(rows[126+ri]['plane_basis_standard_mod3'],dtype=np.int64);P0=rr(P)[0];linevec=[P[0],P[1],(P[0]+P[1])%3,(P[0]-P[1])%3];linekeys=[canline(x) for x in linevec];anchor=canline(mod3(qmat([d['vector']])*LI)[0]);ai=linekeys.index(anchor);lineperms=[]
 for T in gg:
  ints(T);assert abs(T.det())==1 and T*G*T.transpose()==G and np.array_equal(rr(P@mod3(T)%3)[0],P0)
  lineperms.append(Permutation([linekeys.index(canline(x@mod3(T)%3)) for x in linevec]))
 LP=PermutationGroup(lineperms);anchor_orbit=len(LP.orbit(ai));order=2*target*anchor_orbit;assert order==r['stabilizer_order']
 out={'orbit_id':127+ri,'order':order,'flag_stabilizer_order':2*target,'faithful_class_flag_order':target,'class_permutation_degree':degree,'Schreier_words':sch,'Schreier_permutations':[p.array_form for p in pp],'change_of_mark_words':mark,'anchor_orbit_size':anchor_orbit,'permutations_on_four_plane_lines':[p.array_form for p in lineperms],'generators_in_standard_Leech_basis':[ints(T) for T in gg],'complete_flag_orbit_size':len(points),'complete_flag_edges_rechecked':len(edges)*len(words)}
 (folder/f'{127+ri:03d}.json').write_text(json.dumps(out))
 print('Full rare plane group',127+ri,'order',order,'integral generators',len(gg),'full flag group',2*target,'anchor orbit',anchor_orbit,'closed flag orbit',len(points),'elapsed',round(time.time()-started,2),flush=True)
print('PASS: all three rare full plane stabilizers have exact integral generators and full-order certificates.')
