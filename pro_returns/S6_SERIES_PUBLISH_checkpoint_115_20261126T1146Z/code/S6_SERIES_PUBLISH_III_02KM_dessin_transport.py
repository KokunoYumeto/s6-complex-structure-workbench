#!/usr/bin/env python3
"""Own peripheral-word derivation from the bounded Herfurtner J passports.

Ancillary post-release realization work, not additional check credit.
Inputs are only the peer's exact branch permutations and defining tuples.
The ribbon graph records every deletion, tree path and peripheral word.
"""
from collections import deque
from itertools import permutations,product
from pathlib import Path
from datetime import datetime,timezone
import json
import math
import sympy as S

HERE=Path(__file__).resolve().parent
INPUT_ROOT = Path(__file__).resolve().parents[1] / 'agents/continuation5_iii_d2'
I=(1,0,0,1)
A=(0,1,-1,1)       # positive II lift at J=0
B=(0,1,-1,0)       # positive III lift at J=1

def mul(a,b):return(a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3])
def inv(a):return(a[3],-a[1],-a[2],a[0])
def neg(a):return tuple(-x for x in a)
def tr(a):return a[0]+a[3]
def pw(a,n):
    if n<0:return pw(inv(a),-n)
    z=I
    for _ in range(n):z=mul(z,a)
    return z
def word(w):
    r=[]
    for a in w:
        if r and r[-1]==-a:r.pop()
        else:r.append(a)
    return tuple(r)
def wi(w):return tuple(-a for a in reversed(w))
def cat(*ww):return word(sum((list(w) for w in ww),[]))
def evaluate(w,gens=(A,B)):
    r=I
    for x in w:r=mul(r,gens[x-1] if x>0 else inv(gens[-x-1]))
    return r
def cycles(p):
    seen=set();ans=[]
    for x in sorted(p):
        if x in seen:continue
        c=[];y=x
        while y not in seen:seen.add(y);c.append(y);y=p[y]
        ans.append(c)
    return ans
def perm(n,cc):
    p=list(range(n))
    for c in cc:
        for x,y in zip(c,c[1:]+c[:1]):p[x]=y
    return p
def K(a,b,n=1):return pw((1-a*b,a*a,-b*b,1+a*b),n)

DATA=[
 ('55_II',10,[(0,1,2),(3,4,5),(6,7,8)],[(0,1),(2,3),(4,6),(5,7),(8,9)],
  [K(1,0,5),(5,4,-4,-3),(5,3,-7,-4),K(1,1)]),
 ('56_III',9,[(0,1,2),(3,4,5),(6,7,8)],[(1,3),(2,4),(5,6),(7,8)],
  [K(1,0,5),(7,3,-12,-5),(12,5,-29,-12),K(1,1)]),
 ('56_IV',8,[(0,1,2),(3,4,5),(6,7)],[(0,1),(2,3),(4,6),(5,7)],
  [K(1,0,5),K(1,-1,2),(1,1,-3,-2),K(1,1)])]


def dessin(name,n,c0,c1,target):
    p0,p1=perm(n,c0),perm(n,c1)
    rot={};origin={};edgeletter={}
    for v in range(n):
        ds=[2*v,2*p0.index(v)+1,2*n+2*v,2*n+2*p1.index(v)+1]
        for h,k in zip(ds,ds[1:]+ds[:1]):rot[h]=k;origin[h]=v
    for j in range(2*n):edgeletter[2*j]=1 if j<n else 2;edgeletter[2*j+1]=-edgeletter[2*j]
    def faces():return cycles({h:rot[h^1] for h in rot})
    original=faces();face_of={h:i for i,f in enumerate(original) for h in f}
    parent=list(range(len(original)));tags={};labels={}
    for i,f in enumerate(original):
        ll=[edgeletter[h] for h in f]
        if set(ll)=={-1}:kind='zero';width=len(f);smooth=width==3
        elif set(ll)=={-2}:kind='one';width=len(f);smooth=width==2
        else:kind='infinity';width=len(f)//2;smooth=False
        tags[i]=[] if smooth else [i]
        labels[i]=(kind,width)
    assert n-2*n+len(original)==2 and sum(bool(t) for t in tags.values())==4
    def root(x):
        while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
        return x
    def erase(h):
        for x in (h,h^1):
            prev=next(k for k,v in rot.items() if v==x)
            if prev==x:del rot[x]
            else:rot[prev]=rot[x];del rot[x]
    deletions=[]
    while len(faces())>4:
        fs=faces();idx={h:i for i,f in enumerate(fs) for h in f}
        chosen=None
        for i,f in enumerate(fs):
            r=root(face_of[f[0]])
            assert all(root(face_of[x])==r for x in f)
            if tags[r]:continue
            assert evaluate(wi([edgeletter[x] for x in f])) in (I,neg(I))
            for h in f:
                if idx[h^1]!=i:chosen=(h,r,root(face_of[h^1]));break
            if chosen:break
        assert chosen is not None
        h,r,s=chosen
        deletions.append({'edge_dart':h,'smooth_component':r,'adjacent_component':s})
        parent[r]=s;tags[s]=tags[s]+tags[r]
        erase(h)
    assert len(rot)==2*(n+2)
    # A concrete spanning tree and all paths before contraction.
    adjacency={v:[] for v in range(n)}
    for h in rot:adjacency[origin[h]].append(h)
    paths={0:()};tree=[];queue=[0]
    for v in queue:
        for h in sorted(adjacency[v]):
            dest=origin[h^1]
            if dest not in paths:
                paths[dest]=cat(paths[v],(edgeletter[h],));tree.append(h);queue.append(dest)
    assert len(paths)==n
    tree_edges={h//2 for h in tree}
    loopword={h:cat(paths[origin[h]],(edgeletter[h],),wi(paths[origin[h^1]]))
              for h in rot if h//2 not in tree_edges}
    # Contract a tree edge by splicing its two vertex rotations.
    contractions=[]
    for h in tree:
        q=h^1
        preh=next(k for k,v in rot.items() if v==h)
        preq=next(k for k,v in rot.items() if v==q)
        nh,nq=rot[h],rot[q]
        rot[preh]=nq;rot[preq]=nh
        del rot[h];del rot[q]
        contractions.append(h)
    assert len(rot)==6 and len(cycles(rot))==1
    fs=faces();assert len(fs)==4
    chords=sorted({h//2 for h in rot});chord_index={x:i+1 for i,x in enumerate(chords)}
    def cw(f):return wi([chord_index[h//2]*(1 if h%2==0 else -1) for h in f])
    peripheral=[]
    for f in fs:
        roots={root(face_of[h]) for h in f};assert len(roots)==1
        ids=tags[roots.pop()];assert len(ids)==1
        w=cw(f)
        peripheral.append({'puncture':ids[0],'type':labels[ids[0]],'word':w})
    generators=[loopword[2*x] for x in chords]
    # Locate a complete positive peripheral system by exact free reduction.
    systems=[]
    for order in permutations(range(4)):
        choices=[]
        for i in order:
            w=peripheral[i]['word'];choices.append([w[k:]+w[:k] for k in range(len(w))])
        for ww in product(*choices):
            if cat(*ww):continue
            ff=[cat(*[generators[x-1] if x>0 else wi(generators[-x-1]) for x in w]) for w in ww]
            mats=[evaluate(w) for w in ff]
            typed=[peripheral[i]['type'] for i in order]
            lifted=[]
            for typ,M in zip(typed,mats):
                kind,width=typ
                tracewant=2 if kind=='infinity' else (1 if kind=='zero' and width==1 else (-1 if kind=='zero' else 0))
                if tracewant and tr(M)!=tracewant:M=neg(M)
                assert tr(M)==tracewant
                lifted.append(M)
            result=I
            for M in lifted:result=mul(result,M)
            if result==neg(I):
                ii=[i for i,(kind,width) in enumerate(typed) if kind=='one']
                assert len(ii)==1
                lifted[ii[0]]=neg(lifted[ii[0]])
            assert evaluate((1,2,3,4),lifted)==I
            systems.append({'order':order,'types':typed,'chord_words':ww,'F2_words':ff,'SL_matrices':lifted})
    assert systems
    print(name,'smooth-face deletions',len(deletions),'tree contractions',len(tree),'peripheral systems',len(systems),flush=True)
    print(name,'first system',systems[0],flush=True)
    return {'name':name,'sigma0':p0,'sigma1':p1,'original_face_labels':labels,
            'deleted_edges':deletions,'tree_edges':tree,'tree_paths':paths,
            'contracted_rotation':rot,'chord_F2_words':generators,
            'peripheral_systems':systems,'target':target}


def simultaneous(mats,target):
    x=S.symbols('h0:4');H=S.Matrix(2,2,x)
    eq=[]
    for M,T in zip(mats,target):eq.extend(S.Matrix(2,2,M)*H-H*S.Matrix(2,2,T))
    coeff=S.linear_eq_to_matrix(eq,x)[0]
    ns=coeff.nullspace()
    if len(ns)!=1:return None
    v=ns[0];den=math.lcm(*[int(z.q) for z in v]);v=[int(z*den) for z in v]
    gg=math.gcd(*v);v=[z//gg for z in v];h=tuple(v)
    if h[0]*h[3]-h[1]*h[2]!=1:return None
    assert all(mul(M,h)==mul(h,T) for M,T in zip(mats,target))
    return h
def kind(M):
    if tr(M)==2:return('I',math.gcd(M[0]-1,M[1],M[2],M[3]-1))
    return('A',tr(M))
def character(ms):
    return tuple(kind(M) for M in ms)+tuple(tr(mul(ms[i],ms[j])) for i in range(4) for j in range(i+1,4))
def hurwitz(ms,i,sign):
    a,b=ms[i:i+2]
    pair=(b,mul(mul(inv(b),a),b)) if sign==1 else (mul(mul(a,b),inv(a)),a)
    return ms[:i]+pair+ms[i+2:]
def match(record,limit=10):
    target=tuple(record['target']);tk=character(target)
    queue=deque();seen=set()
    for ii,ss in enumerate(record['peripheral_systems']):
        ms=tuple(ss['SL_matrices']);key=character(ms)
        if key not in seen:seen.add(key);queue.append((ms,ii,()))
    while queue:
        ms,ii,path=queue.popleft()
        if character(ms)==tk:
            h=simultaneous(ms,target)
            if h:
                print(record['name'],'MATCH','system',ii,'moves',path,'H',h,'states',len(seen),flush=True)
                return {'system_index':ii,'hurwitz_moves':path,'H':h,'H_inverse':inv(h),'matched_matrices':ms,'visited_character_states':len(seen)}
        if len(path)>=limit:continue
        for i in range(3):
            for sign in (1,-1):
                mm=hurwitz(ms,i,sign);key=character(mm)
                if key not in seen:
                    seen.add(key);queue.append((mm,ii,path+((i,sign),)))
        if len(seen)>300000:break
    print(record['name'],'NO MATCH within',limit,'moves; states',len(seen),flush=True)
    return None


def main():
    print('Own dessin transport started',datetime.now(timezone.utc).isoformat(),flush=True)
    output=[]
    all_data=list(DATA)
    analytic={r['name']:r for r in json.loads((INPUT_ROOT/'S6_SERIES_PUBLISH_III_02KM_analytic_cover_maps.json').read_text())}
    raw=json.loads((INPUT_ROOT.parent/'continuation5_iii_infra'/'S6_SERIES_PUBLISH_III_02KM_marked_inputs.json').read_text())['rows']
    for name,index in [('45_II',0),('47_II',1),('47_III',2),('49_IVstar',6)]:
        p0,p1=analytic[name]['actual_permutations']
        c0=cycles(dict(enumerate(p0)));c1=cycles(dict(enumerate(p1)))
        target=[tuple(x for rr in A for x in rr) for A in raw[index]['elliptic_matrices']]
        all_data.append((name,len(p0),c0,c1,target))
    for args in all_data:
        record=dessin(*args);record['match']=match(record);output.append(record)
    path=HERE/'S6_SERIES_PUBLISH_III_02KM_dessin_transport_maps.json'
    path.write_text(json.dumps(output,separators=(',',':'))+'\n')
    print('Own dessin transport ended',datetime.now(timezone.utc).isoformat(),flush=True)

if __name__=='__main__':main()
