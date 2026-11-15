"""Construct full integral stabilizer generators for every rooted plane.

This is an executable, exact version of the conjugation/Schreier recipe
in Statement B.9.  A2 uses its normal rotation group of order 729 and
enumerates only the 190080 monomial code automorphisms; A1 uses the full
colored Golay graph.  Mark-changing isometries then give the full plane
group, whose order is independently checked on its intrinsic root union.

Usage: python B_plane_stabilizer_recipe.py [--orbit ID]
With no ID, construct all 126 rooted-plane stabilizers. The remaining
three are handled by B_rare_plane_groups.py using the saved Schreier trees.
"""
from B_global_lattice import *
from B_A2_fusion import MODEL as A2,mark_isometry,key_from_Nrow
from B_A1_fusion import MODEL as A1,markA1,keyA1,Cf,graph
from sympy.combinatorics import Permutation,PermutationGroup
import pynauty,argparse,time

I=fmpq_mat([[int(i==j) for j in range(24)] for i in range(24)])
RG=[[2 if i==j else -1 if i//2==j//2 else 0 for j in range(24)] for i in range(24)]
rootrows=[]
for i in range(12):
 for a,b in [(1,0),(0,1),(1,1),(-1,0),(0,-1),(-1,-1)]:
  v=[0]*24;v[2*i:2*i+2]=[a,b];rootrows.append(v)
rootindex={tuple(v):i for i,v in enumerate(rootrows)}
NEG=Permutation([6*(i//6)+(i%6+3)%6 for i in range(72)])
def matrix_from_rootperm(p):return fmpq_mat([rootrows[p(6*i+j)] for i in range(12) for j in range(2)])
def rotor(z):
 out=I*1;r=fmpq_mat([[0,1],[-1,-1]])
 for i,k in enumerate(z):
  a=r**int(k)
  for j in range(2):
   for l in range(2):out[2*i+j,2*i+l]=a[j,l]
 return out
def rotperm(z):
 a=np.array(ints(rotor(z)),dtype=np.int64)
 return Permutation([rootindex[tuple(x)] for x in np.array(rootrows)@a])
def monoperm(p,sgn=1):
 swap=[1,0,2,4,3,5];out=[]
 for i in range(12):
  j=int(p[2*i])//2;sw=int(p[2*i])%2
  for k in range(6):
   l=swap[k] if sw else k
   if sgn<0:l=(l+3)%6
   out.append(6*j+l)
 return Permutation(out)
def mod3(a):return np.array([[x.numerator*pow(x.denominator,-1,3)%3 for x in row] for row in qrows(a)],dtype=np.int64)

class A2Engine:
 def __init__(self):
  self.d=json.loads((REC/'B_A2_strata_setup.json').read_text());C=np.array(self.d['C'],dtype=np.int64)
  self.codes=np.array(list(product(range(3),repeat=6)))@C%3
  pg=PermutationGroup([Permutation(p) for p in self.d['monomial_generators']]);assert pg.order()==190080
  self.perms=np.array([p.array_form for p in pg.generate_schreier_sims()],dtype=np.uint8);self.ip=np.argsort(self.perms,axis=1)
  self.R=np.array(ints(A2.R),dtype=np.int64)%9;self.Ri=A2.R.inv();self.rho=np.array(self.d['rho_N_mod3'],dtype=np.int64);self.j=next(i for i,x in enumerate(self.rho) if x);self.ri=pow(int(self.rho[self.j]),-1,3);self.pows=3**np.arange(24,dtype=np.int64)
  self.rotperms=[rotperm(z) for z in self.codes];self.cache={}
 def scaled(self,y):return np.array(ints(3*y*self.Ri)[0],dtype=np.int64)%9
 def keys(self,a):
  n=a@self.R%9;assert np.all(n%3==0);n=n//3;n=(n-n[:,self.j,None]*self.ri*self.rho[None,:])%3
  return n@self.pows
 def rotations(self,y):
  a=self.scaled(y);out=np.tile(a,(729,1));x=a[::2];b=a[1::2]
  for i,z in enumerate(self.codes):
   out[i,::2]=np.where(z==0,x,np.where(z==1,-b,b-x));out[i,1::2]=np.where(z==0,b,np.where(z==1,x-b,-x))
  keys=self.keys(out%9);lookup={}
  for i,k in enumerate(keys):lookup.setdefault(int(k),i)
  return lookup,[i for i,k in enumerate(keys) if k==keys[0]],int(keys[0])
 def candidates(self,source,target_c):
  a=self.scaled(source);cc=a[self.ip[:,1::2]]%3
  for sign in [1,-1]:
   good=np.flatnonzero(np.all(sign*cc%3==target_c,axis=1))
   rows=sign*a[self.ip[good]]%9
   yield sign,good,self.keys(rows)
 def flag_group(self,s,oid,y,expected):
  key=(s,oid)
  if key in self.cache:return self.cache[key]
  lookup,kernel,_=self.rotations(y);target_c=self.scaled(y)[1::2]%3
  gens=[NEG];PG=PermutationGroup(gens)
  zbase,_=rr(self.codes[kernel])
  for z in zbase:
   p=rotperm(z)
   if not PG.contains(p):gens.append(p);PG=PermutationGroup(gens)
  if PG.order()!=expected:
   done=False
   for sign,ii,keys in self.candidates(y,target_c):
    matches=np.flatnonzero(np.isin(keys,np.array(list(lookup),dtype=np.int64)))
    for m in matches:
     j=int(ii[m]);r=lookup[int(keys[m])];p=monoperm(self.perms[j],sign)*self.rotperms[r]**-1
     if PG.contains(p):continue
     gens.append(p);PG=PermutationGroup(gens)
     assert expected%int(PG.order())==0
     if int(PG.order())==expected:done=True;break
    if done:break
  assert int(PG.order())==expected
  out=[self.Ri*matrix_from_rootperm(p)*A2.R for p in gens]
  self.cache[key]=out
  return out
 def transport(self,source,target):
  lookup,_,_=self.rotations(target);target_c=self.scaled(target)[1::2]%3
  for sign,ii,keys in self.candidates(source,target_c):
   for m in np.flatnonzero(np.isin(keys,np.array(list(lookup),dtype=np.int64))):
    j=int(ii[m]);r=lookup[int(keys[m])];p=monoperm(self.perms[j],sign)*self.rotperms[r]**-1
    T=self.Ri*matrix_from_rootperm(p)*A2.R
    assert self.keys(self.scaled(source*T)[None,:])[0]==self.keys(self.scaled(target)[None,:])[0]
    return T
  raise AssertionError('No A2 flag transporter')

CODE=[tuple((np.array([(x>>i)&1 for i in range(12)])@Cf%2).tolist()) for x in range(4096)]
OCT=[c for c in CODE if sum(c)==8];CSET=set(CODE)
def A1parts(y):
 a=mod3(y*A1.R.inv())[0]
 return [tuple(i for i,x in enumerate(a) if x==k) for k in range(3)]
def A1graph(parts):
 adj={i:[] for i in range(24)}
 for c in OCT:
  k=len(adj);adj[k]=[i for i,x in enumerate(c) if x]
  for i in adj[k]:adj[i].append(k)
 first=len(adj)
 for part in parts:
  k=len(adj);adj[k]=list(part)
  for i in part:adj[i].append(k)
 return pynauty.Graph(len(adj),adjacency_dict=adj,vertex_coloring=[set(range(24)),set(range(24,first)),set(range(first,len(adj)))])
def checkperm(p):
 assert set(p)==set(range(24))
 for c in OCT:
  d=[0]*24
  for i,x in enumerate(c):d[p[i]]=x
  assert tuple(d) in CSET
def A1matrix(p):return A1.R.inv()*fmpq_mat([[int(j==p[i]) for j in range(24)] for i in range(24)])*A1.R
def A1group(y,expected):
 parts=A1parts(y);gg,_,_,_,_=pynauty.autgrp(A1graph(parts));pp=[p[:24] for p in gg];PG=PermutationGroup([Permutation(p) for p in pp]);assert 2*int(PG.order())==expected
 for p in pp:
  checkperm(p);assert {tuple(sorted(p[i] for i in a)) for a in parts}=={tuple(a) for a in parts}
 return [-I]+[A1matrix(p) for p in pp]
def A1transport(source,target):
 a=A1parts(source);b=A1parts(target);la=pynauty.canon_label(A1graph(a));lb=pynauty.canon_label(A1graph(b));p=[0]*len(la)
 for i,j in zip(la,lb):p[i]=j
 p=p[:24];checkperm(p);assert {tuple(sorted(p[i] for i in x)) for x in a}=={tuple(x) for x in b}
 return A1matrix(p)

def plane_equal(P,Q):return np.array_equal(rr(P)[0],rr(Q)[0])
def construct(r,engine):
 typ=r['type'];s,oid=r['representative'];M=A2 if typ=='A2' else A1;dat=json.loads((REC/f'B_{typ}_flags'/f'{s}_{oid}.json').read_text());y=qmat([dat['y']]);flags=json.loads((REC/f'B_{typ}_flags.json').read_text());flag=next(f for f in flags if (f['stratum'],f['orbit_id'])==(s,oid));expected=flag['flag_stabilizer']
 gens=engine.flag_group(s,oid,y,expected) if typ=='A2' else A1group(y,expected)
 P=mod3(qmat(qrows(M.v)+qrows(y))*M.Li);P0=rr(P)[0];marktype='12A2' if typ=='A2' else '24A1';markgens=[]
 for ext in dat['extensions']:
  if ext['root_system']!=marktype or ext['L_intersection_index']!=3:continue
  T=mark_isometry(ext) if typ=='A2' else markA1(ext)
  for x in [M.v,y]:
   xx=x*T
   if typ=='A2':
    a=mod3(xx)[0];rho=engine.rho;j=engine.j;a=(a-a[j]*engine.ri*rho)%3
    if any(a):break
   else:
    v=mod3(xx*M.R.inv())[0]
    if len(set(v))>1:break
  key=key_from_Nrow(xx) if typ=='A2' else keyA1(xx)
  if key!=(s,oid):continue
  U=engine.transport(xx,y) if typ=='A2' else A1transport(xx,y);markgens.append(T*U)
 gens+=markgens
 # Faithful finite representation: the roots in all eight extensions.
 allroots=set()
 for ext in dat['extensions']:
  if ext['roots']:
   for row in qrows(fmpq_mat(ext['roots'])*qmat(ext['basis'])):allroots.add(tuple(row))
 roots=sorted(allroots);R=qmat(roots);ri={v:i for i,v in enumerate(roots)};pp=[];gg=[];PG=PermutationGroup([Permutation(list(range(len(roots))))])
 for T in gens:
  assert T*M.G*T.transpose()==M.G;LT=M.L*T*M.Li;ints(LT);assert abs(LT.det())==1 and plane_equal(P0@mod3(LT)%3,P0)
  im=qrows(R*T);p=Permutation([ri[tuple(x)] for x in im])
  if PG.contains(p):continue
  pp.append(p);PG=PermutationGroup(pp);gg.append(T)
 assert int(PG.order())==r['stabilizer_order']
 iso=json.loads((REC/'B_global_model_isometries.json').read_text());S=qmat(iso[f'standard_to_{typ}_N_coordinates']);SI=S.inv();standard=[ints(S*T*SI) for T in gg]
 G=qmat(iso['standard_Gram']);P=np.array(r['plane_basis_standard_mod3'],dtype=np.int64)
 for T in standard:
  t=fmpq_mat(T);assert t*G*t.transpose()==G and abs(t.det())==1 and plane_equal(P@np.array(T,dtype=np.int64)%3,P)
 return {'orbit_id':r['orbit_id'],'order':int(PG.order()),'flag_stabilizer_order':expected,'intrinsic_root_union_size':len(roots),'intrinsic_roots_in_N_coordinates':[[str(x) for x in row] for row in roots],'generators_in_standard_Leech_basis':standard,'permutations_on_intrinsic_root_union':[p.array_form for p in pp],'number_of_anchor_changing_generators_examined':len(markgens)}

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--orbit',type=int);a=parser.parse_args();rows=json.loads((REC/'B_all_129_plane_orbits.json').read_text());engine=A2Engine();folder=REC/'B_plane_groups';folder.mkdir(exist_ok=True);started=time.time();count=0
 for r in rows[:126]:
  if a.orbit is not None and r['orbit_id']!=a.orbit:continue
  d=construct(r,engine);(folder/f"{r['orbit_id']:03d}.json").write_text(json.dumps(d));count+=1
  print('full plane group',r['orbit_id'],'order',d['order'],'integral generators',len(d['generators_in_standard_Leech_basis']),'faithful root degree',d['intrinsic_root_union_size'],'elapsed',round(time.time()-started,2),flush=True)
 print('PASS exact full generators, lattice identities, plane preservation and independent permutation orders for',count,'rooted plane classes.',flush=True)
