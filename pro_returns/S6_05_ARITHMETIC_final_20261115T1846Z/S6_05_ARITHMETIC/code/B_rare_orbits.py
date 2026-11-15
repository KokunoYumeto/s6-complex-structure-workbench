"""Close the all-Leech residual by certified stabilizer orbits and exact mass.

Candidate discovery is seeded sampling; proof of completeness is NOT sampling:
all retained group orbits are exhausted, distinctness is certified by changes
of line mark, and their total size must equal the exact residual mass.
"""
from B_global_lattice import *
from mmgroup import MM0,generators as gen
import random,time,gzip,struct
MASK=(1<<24)-1;VMASK=(1<<48)-1;CO0=8315553613086720000;TARGET=916269354000
D=json.loads((REC/'B_rare_stabilizers.json').read_text());ROOTS=np.load(REC/'B_standard_Leech_minimal.npz')['vectors'].astype(np.int64)
TYPES={0x1fe|(1<<24):'3',0xe:'622',0x111111:'623',0xeee000:'933'}
def pack(v):
 a=b=0
 for i,x in enumerate(v):
  if x%3==1:a|=1<<i
  elif x%3==2:b|=1<<i
 return a|(b<<24)
def unpack(a):return np.array([((a>>i)&1)+2*((a>>(24+i))&1) for i in range(24)],dtype=np.int64)
def neg(a):return int(gen.gen_leech3_neg(a))
def add(a,b):return int(gen.gen_leech3_reduce(gen.gen_leech3_add(a,b)))
def reduce(a):
 g=np.zeros(12,dtype=np.uint32);r=int(gen.gen_leech3_reduce_leech_mod3(a,g));assert r>=0;return g[:r>>48],r&VMASK
def typ(a):
 _,r=reduce(a);return TYPES.get(r,'other')
def act(a,w):return int(gen.gen_leech3_reduce(gen.gen_leech3_op_vector_word(a,w,len(w))))
class Context:
 def __init__(self,name):
  d=D[name];self.name=name;self.v=d['packed'];self.vv=np.array(d['vector'],dtype=np.int64);self.order=d['order_vector_stabilizer'];self.words=[np.array(g['word'],dtype=np.uint32) for g in d['generators']];self.invwords=[(MM0('a',w)**-1).mmdata for w in self.words];self.pivot=next(i for i in range(24) if ((self.v>>i)&1) or ((self.v>>(24+i))&1));self.vpivot=((self.v>>self.pivot)&1)+2*((self.v>>(24+self.pivot))&1);self.redword,self.red=reduce(self.v);self.redinv=(MM0('a',self.redword)**-1).mmdata;self.lookup={};self.flags=[]
 def project(self,w):
  x=((w>>self.pivot)&1)+2*((w>>(24+self.pivot))&1);k=x*self.vpivot%3
  if k:w=add(w,self.v if k==2 else neg(self.v))
  return min(w,neg(w))
 def lines(self,w):return [self.v,w,add(self.v,w),add(self.v,neg(w))]
 def orbit(self,key):
  fid=len(self.flags);queue=[key];idx={key:0};parents=[0];pgen=[0];self.lookup[key]=fid
  for i,x in enumerate(queue):
   for gi,w in enumerate(self.words):
    y=self.project(act(x,w))
    if y not in idx:
     assert y not in self.lookup;idx[y]=len(queue);queue.append(y);parents.append(i);pgen.append(gi);self.lookup[y]=fid
   assert len(queue)<=1000000
  size=len(queue);assert self.order%size==0
  rec={'id':fid,'representative':key,'size':size,'vector_stabilizer_order':self.order//size}
  self.flags.append(rec);np.savez_compressed(REC/f'B_rare_{self.name}_flag_{fid}.npz',points=np.array(queue,dtype=np.uint64),parents=np.array(parents,dtype=np.uint32),parent_generator=np.array(pgen,dtype=np.uint8))
  print('rare flag',self.name,fid,'size',size,'vector stabilizer',self.order//size,flush=True)
  return fid
 def change(self,a,b):
  w,r=reduce(a);assert r==self.red
  return self.project(act(act(b,w),self.redinv))
 def close_plane(self,key):
  first=self.orbit(key);ids=[first];seen={first};links=[]
  for fid in ids:
   w=self.flags[fid]['representative'];lines=self.lines(w);types=[typ(x) for x in lines];assert all(t in ['3','622'] for t in types)
   if self.name=='622':assert all(t=='622' for t in types)
   marks=[]
   for i,(a,t) in enumerate(zip(lines,types)):
    if t!=self.name:continue
    b=w if i==0 else self.v;k=self.change(a,b)
    f=self.lookup[k] if k in self.lookup else self.orbit(k)
    if f not in seen:seen.add(f);ids.append(f)
    marks.append(f)
   links.append({'flag':fid,'types':types,'mark_flags':marks})
  t=links[0]['types'].count(self.name);S=sum(self.flags[i]['size'] for i in ids);assert 2*self.order*t%S==0;stab=2*self.order*t//S;assert CO0%stab==0;size=CO0//stab
  return {'line_type':self.name,'representative':self.flags[first]['representative'],'flag_ids':ids,'stabilizer_order':stab,'plane_orbit_size':size,'line_types':links[0]['types'],'links':links}
contexts={x:Context(x) for x in ['3','622']};rng=random.Random(20261115);out=[];total=0;started=time.time();attempts=0
while total<TARGET:
 attempts+=1;name='3' if attempts%2 else '622';ct=contexts[name]
 i=rng.randrange(len(ROOTS));j=rng.randrange(len(ROOTS));x=ROOTS[i];y=ROOTS[j];ip=int(x@y)
 if name=='622':
  if ip!=-16:continue
  w=y-x
 else:
  if ip==-8:w=x+y
  elif ip==-16:w=y-x
  else:continue
 if int(ct.vv@w)%3:continue
 k=ct.project(pack(w))
 if k==0 or k in ct.lookup:continue
 tt=[typ(a) for a in ct.lines(k)]
 if any(t not in ['3','622'] for t in tt):continue
 if name=='622' and any(t=='3' for t in tt):continue
 r=ct.close_plane(k);out.append(r);total+=r['plane_orbit_size'];assert total<=TARGET
 print('NEW RARE PLANE',len(out),r,'covered',total,'residual',TARGET-total,'attempts',attempts,'seconds',time.time()-started,flush=True)
 (REC/'B_rare_plane_orbits.json').write_text(json.dumps({'orbits':out,'covered':total,'target':TARGET,'attempts':attempts,'flags':{x:c.flags for x,c in contexts.items()}}))
 if attempts>10000000:raise RuntimeError('candidate discovery stalled')
print('COMPLETE rare plane orbits',len(out),'mass',total,'attempts',attempts,'seconds',time.time()-started,flush=True)
