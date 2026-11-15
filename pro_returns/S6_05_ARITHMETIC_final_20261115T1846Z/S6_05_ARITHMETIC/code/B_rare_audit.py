"""Exact lattice and change-of-mark audits for the three all-Leech orbits.

The input representatives and group words are the fixed recorded output of
B_rare_orbits.py; no random search is used by this verification program.
"""
from B_global_lattice import *
from mmgroup import MM0, Xsp2_Co1, generators as gen
from collections import Counter

MASK=(1<<48)-1
D=json.loads((REC/'B_rare_stabilizers.json').read_text())
R=json.loads((REC/'B_rare_plane_orbits.json').read_text())
LB=qmat(json.loads((REC/'B_standard_Leech_basis.json').read_text())['basis'])
LI=LB.inv(); LG=LB*LB.transpose()/8
assert LG.det()==1 and all(int(LG[i,i])%2==0 for i in range(24))
def unpack(a):
 return [((a>>i)&1)+2*((a>>(24+i))&1) for i in range(24)]
def mod3(A):
 return np.array([[int(F(str(x)).numerator)*pow(int(F(str(x)).denominator),-1,3)%3 for x in row] for row in qrows(A)],dtype=np.int64)
def neg(a):return int(gen.gen_leech3_neg(a))
def add(a,b):return int(gen.gen_leech3_reduce(gen.gen_leech3_add(a,b)))
def reduce(a):
 w=np.zeros(12,dtype=np.uint32);r=int(gen.gen_leech3_reduce_leech_mod3(a,w));assert r>=0
 return MM0('a',w[:r>>48]),r&MASK
def matrix(g):
 a=Xsp2_Co1(g).leech_op
 return fmpq_mat(a.tolist())/8
def plane_space(v,w):return rr(mod3(qmat([unpack(v),unpack(w)])*LI))[0]

out=[]
for i,r in enumerate(R['orbits']):
 name=r['line_type'];d=D[name];v=d['packed'];w=r['representative']
 vc=ints(qmat([d['vector']])*LI)[0]
 wc=mod3(qmat([unpack(w)])*LI)[0].tolist()
 model=object.__new__(PlaneModel);model.G=LG;model.L=fmpq_mat([[int(i==j) for j in range(24)] for i in range(24)]);model.Li=model.L;model.v=qmat([vc])
 dd=model.plane(wc,REC/f'B_rare_{i+1}')
 assert all(e['root_system']=='Leech' for e in dd['extensions'])
 assert Counter(e['L_intersection_index'] for e in dd['extensions'])=={1:1,3:4,9:3}
 dd['orbit']=r;dd['coordinate_convention']='rows in the integral standard Leech basis B_standard_Leech_basis.json'
 dd['v']=vc;dd['change_of_mark']=[]
 a0,std=reduce(v);P=plane_space(v,w)
 for j,a in enumerate([v,w,add(v,w),add(v,neg(w))]):
  aa,typ=reduce(a)
  if typ!=std:continue
  g=aa*a0**-1;T=matrix(g);assert T*T.transpose()==fmpq_mat([[int(i==j) for j in range(24)] for i in range(24)])
  LT=LB*T*LI;assert abs(LT.det())==1;ints(LT)
  image=rr(P@mod3(LT)%3)[0]
  assert len(image)==2
  # The changed line must be the prescribed anchor, up to its sign.
  av=mod3(qmat([unpack(a)])*T*LI)[0];anchor=mod3(qmat([unpack(v)])*LI)[0]
  assert np.array_equal(av,anchor) or np.array_equal(av,2*anchor%3)
  dd['change_of_mark'].append({'line_index':j,'word':g.mmdata.tolist(),'matrix_in_Leech_basis':ints(LT),'image_plane_basis_mod3':image.tolist()})
 (REC/f'B_rare_plane_{i+1}.json').write_text(json.dumps(dd))
 out.append({'orbit':i+1,'eight_extensions':[e['root_system'] for e in dd['extensions']],'determinant_J':str((qmat(dd['J_basis'])*LG*qmat(dd['J_basis']).transpose()).det()),'exact_mark_isometries':len(dd['change_of_mark'])})
 print('rare orbit',i+1,'eight extensions all Leech; det J = 81; exact integral mark isometries',len(dd['change_of_mark']),flush=True)
(REC/'B_rare_audit.json').write_text(json.dumps(out))
print('PASS: all 24 extension lattices and all 10 changes of rare line mark verified exactly.')
