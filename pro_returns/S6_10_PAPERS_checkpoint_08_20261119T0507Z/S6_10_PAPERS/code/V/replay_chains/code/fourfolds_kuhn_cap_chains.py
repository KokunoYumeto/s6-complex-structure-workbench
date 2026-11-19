"""Finite integral Kuhn cusp and boundary chains from strict torus diagrams.

The entire category is enumerated: the 26 simplex orbits in the Kuhn
triangulation of T3, every translated face incidence, and every strict
flag (length at most3).  Torus bar contractions retain all integral
coherence corrections.  Unit cancellation is integral chain equivalence.
"""
from itertools import permutations,combinations
from functools import lru_cache
from collections import deque
import json
from pathlib import Path
import sympy as S
from fourfolds_bar_koszul import AbelianBar,add
from fourfolds_survivor_test import kernel,snf,factors

zero=(0,0,0)
def plus(a,b):return tuple(x+y for x,y in zip(a,b))
def minus(a,b):return tuple(x-y for x,y in zip(a,b))
def normalize(vertices):
    vertices=tuple(sorted(vertices));v=vertices[0]
    return tuple(minus(x,v) for x in vertices),v
def matvec(M,v):return tuple(int(sum(M[i,j]*v[j] for j in range(M.cols))) for i in range(M.rows))

class KuhnCategory:
    def __init__(self):
        cells=set()
        for p in permutations(range(3)):
            vertices=[zero]
            for i in p:vertices.append(plus(vertices[-1],tuple(int(j==i) for j in range(3))))
            for q in range(1,5):
                for sub in combinations(vertices,q):cells.add(normalize(sub)[0])
        self.objects=sorted(cells,key=lambda a:(len(a),a));self.index={a:i for i,a in enumerate(self.objects)}
        assert [sum(len(a)==q for a in self.objects) for q in range(1,5)]==[1,7,12,6]
        self.morphisms=[]
        for j,sigma in enumerate(self.objects):
            for q in range(1,len(sigma)):
                for sub in combinations(sigma,q):
                    tau,w=normalize(sub)
                    self.morphisms.append((self.index[tau],j,w))
        self.mindex={m:i for i,m in enumerate(self.morphisms)}
        self.outgoing={i:[] for i in range(len(self.objects))}
        for i,(s,t,w) in enumerate(self.morphisms):self.outgoing[s].append(i)
        self.chains=[(i,()) for i in range(len(self.objects))]
        old=list(self.chains)
        for p in range(3):
            new=[]
            for start,arrows in old:
                end=self.morphisms[arrows[-1]][1] if arrows else start
                for a in self.outgoing[end]:new.append((start,arrows+(a,)))
            self.chains.extend(new);old=new
        assert not any(self.outgoing[self.morphisms[a[-1]][1]] for s,a in old)
        self.Q=[];self.R=[]
        for tau in self.objects:
            L=S.Matrix.hstack(*(S.Matrix(v) for v in tau[1:])) if len(tau)>1 else S.zeros(3,0)
            Q=kernel(L.T).T
            if Q.rows:
                D,U,V=snf(Q)
                assert [abs(D[j,j]) for j in range(Q.rows)]==[1]*Q.rows
                R=V[:,:Q.rows]*S.diag(*(1/D[j,j] for j in range(Q.rows)))*U
                assert Q*R==S.eye(Q.rows)
            else:R=S.zeros(3,0)
            self.Q.append(Q);self.R.append(R)

    def compose(self,a,b):
        s,t,w=self.morphisms[a];u,v,z=self.morphisms[b]
        assert t==u
        return self.mindex[s,v,plus(w,z)]

class TorusDiagram:
    def __init__(self,category,boundary=False):
        self.C=category;self.boundary=boundary
        self.ranks=[4 if boundary else Q.rows for Q in category.Q]
        self.bars={r:AbelianBar(r) for r in set(self.ranks)}
        self.maps=[]
        for s,t,w in category.morphisms:
            if boundary:
                M=S.eye(4);M[1:,0]=S.Matrix(w)
            else:
                M=category.Q[t]*category.R[s]
                assert M*category.Q[s]==category.Q[t]
            assert all(S.denom(x)==1 for x in M)
            self.maps.append(M)
        for a,(s,t,w) in enumerate(category.morphisms):
            for b in category.outgoing[t]:
                assert self.maps[b]*self.maps[a]==self.maps[category.compose(a,b)]

    def map_bar(self,a,chain):
        M=self.maps[a];out={};z=(0,)*M.rows
        for simplex,c in chain.items():
            image=tuple(matvec(M,g) for g in simplex)
            if not any(g==z for g in image):add(out,{image:c})
        return out

    def delta(self,chain):
        out={}
        for ((start,arrows),simplex),c in chain.items():
            p=len(arrows);q=len(simplex)
            if not p:continue
            a=arrows[0];nstart=self.C.morphisms[a][1]
            for ss,v in self.map_bar(a,{simplex:1}).items():
                add(out,{((nstart,arrows[1:]),ss):c*v*(-1)**q})
            for j in range(1,p):
                aa=arrows[:j-1]+(self.C.compose(arrows[j-1],arrows[j]),)+arrows[j+1:]
                add(out,{((start,aa),simplex):c*(-1)**(q+j)})
            add(out,{((start,arrows[:-1]),simplex):c*(-1)**(q+p)})
        return out

    def h(self,chain):
        out={};groups={}
        for (base,simplex),c in chain.items():add(groups.setdefault(base,{}),{simplex:c})
        for base,simplices in groups.items():
            B=self.bars[self.ranks[base[0]]]
            for s,v in B.ordinary_homotopy(simplices).items():add(out,{(base,s):v})
        return out

    def p(self,chain):
        out={}
        for (base,simplex),c in chain.items():
            B=self.bars[self.ranks[base[0]]]
            for I,v in B.ordinary_project({simplex:1}).items():add(out,{(base,I):c*v})
        return out

    @lru_cache(None)
    def lift(self,base,I):
        B=self.bars[self.ranks[base[0]]]
        term={(base,s):v for s,v in B.ordinary_include({I:1}).items()}
        out=dict(term)
        for j in range(len(base[1])):
            term=self.h(self.delta(term));term={k:-v for k,v in term.items()};add(out,term)
        assert self.h(self.delta(term))=={}
        return out

    def project(self,chain):
        term=dict(chain);out=self.p(term)
        for j in range(3):
            term=self.delta(self.h(term));term={k:-v for k,v in term.items()};add(out,self.p(term))
            if not term:break
        assert all(not base[1] for base,simplex in term)
        return out

    @lru_cache(None)
    def d_basis(self,base,I):return self.p(self.delta(self.lift(base,I)))

    def d(self,chain):
        out={}
        for (base,I),c in chain.items():add(out,self.d_basis(base,I),c)
        return out

    def bases(self):
        out={}
        for base in self.C.chains:
            for q in range(self.ranks[base[0]]+1):
                for I in combinations(range(self.ranks[base[0]]),q):
                    out.setdefault(len(base[1])+q,[]).append((base,I))
        return out

    def complex(self):
        B=self.bases();D={}
        index={n:{b:i for i,b in enumerate(bs)} for n,bs in B.items()}
        for n,bs in sorted(B.items()):
            print('diagram',('boundary' if self.boundary else 'central'),'degree',n,'cells',len(bs),flush=True)
            D[n]={}
            for j,b in enumerate(bs):
                out=self.d_basis(*b)
                assert self.d(out)=={}
                D[n][j]={index[n-1][t]:c for t,c in out.items()} if n else {}
        return B,D

class Collapse:
    def __init__(self,source,target):
        self.source=source;self.target=target
        self.maps=[S.Matrix.hstack(S.zeros(Q.rows,1),Q) for Q in target.C.Q]
        for a,(s,t,w) in enumerate(source.C.morphisms):
            assert self.maps[t]*source.maps[a]==target.maps[a]*self.maps[s]

    @lru_cache(None)
    def basis(self,base,I):
        chain=self.source.lift(base,I);out={}
        for (b,s),c in chain.items():
            M=self.maps[b[0]];z=(0,)*M.rows
            ss=tuple(matvec(M,g) for g in s)
            if not any(g==z for g in ss):add(out,{(b,ss):c})
        return self.target.project(out)

    def apply(self,chain):
        out={}
        for (b,I),c in chain.items():add(out,self.basis(b,I),c)
        return out

    def matrices(self,BY,BW):
        out={}
        for n,bs in BY.items():
            ix={b:i for i,b in enumerate(BW.get(n,[]))};out[n]={}
            for j,b in enumerate(bs):
                image=self.basis(*b)
                assert self.target.d(image)==self.apply(self.source.d_basis(*b))
                out[n][j]={ix[t]:c for t,c in image.items()}
        return out

def unit_reduce(dimensions,differentials):
    bases={n:set(range(k)) for n,k in dimensions.items()}
    D={n:{c:dict(v) for c,v in differentials.get(n,{}).items()} for n in bases}
    rows={n:{} for n in bases};queue=deque()
    for n,columns in D.items():
        for c,col in columns.items():
            for r,v in col.items():
                rows[n].setdefault(r,{})[c]=v
                if abs(v)==1:queue.append((n,c,r))
    count=0
    def erase_col(n,c):
        col=D.get(n,{}).pop(c,{})
        for r in col:
            rows[n][r].pop(c,None)
            if not rows[n][r]:rows[n].pop(r)
    while queue:
        n,a,b=queue.popleft()
        if a not in bases.get(n,set()) or b not in bases.get(n-1,set()):continue
        u=D[n][a].get(b,0)
        if abs(u)!=1:continue
        pivot=dict(D[n][a])
        affected=list(rows[n].get(b,{}))
        for c in affected:
            if c==a:continue
            scale=D[n][c][b]//u
            for r,v in pivot.items():
                old=D[n][c].get(r,0);new=old-scale*v
                if new:
                    D[n][c][r]=new;rows[n].setdefault(r,{})[c]=new
                    if abs(new)==1:queue.append((n,c,r))
                else:
                    D[n][c].pop(r,None)
                    if r in rows[n]:
                        rows[n][r].pop(c,None)
                        if not rows[n][r]:rows[n].pop(r)
        erase_col(n,a)
        for c in list(rows.get(n+1,{}).get(a,{})):
            D[n+1][c].pop(a,None)
        rows.get(n+1,{}).pop(a,None)
        erase_col(n-1,b)
        bases[n].remove(a);bases[n-1].remove(b);count+=1
    matrices={}
    for n in sorted(bases):
        cols=sorted(bases[n]);rr=sorted(bases.get(n-1,set()));ix={r:i for i,r in enumerate(rr)}
        M=S.zeros(len(rr),len(cols))
        for j,c in enumerate(cols):
            for r,v in D[n].get(c,{}).items():M[ix[r],j]=v
        matrices[n]=M
        if n and n-1 in matrices:assert matrices[n-1]*M==S.zeros(matrices[n-1].rows,M.cols)
    return matrices,count

def homology_all(matrices):
    out={}
    for n,D in matrices.items():
        E=matrices.get(n+1,S.zeros(D.cols,0));K=kernel(D)
        assert D*E==S.zeros(D.rows,E.cols)
        assert K.cols==D.cols-D.rank()
        print('reduced degree',n,'boundary',D.shape,'next',E.shape,'kernel',K.shape,flush=True)
        X=K.gauss_jordan_solve(E)[0] if E.cols else S.zeros(K.cols,0)
        assert all(S.denom(x)==1 for x in X)
        out[n]={'rank':K.cols-E.rank(),'torsion':[d for d in factors(X) if d>1]}
    return out

if __name__=='__main__':
    C=KuhnCategory()
    print('objects',len(C.objects),'morphisms',len(C.morphisms),
          'flags',[sum(len(a)==p for s,a in C.chains) for p in range(4)],flush=True)
    W=TorusDiagram(C);Y=TorusDiagram(C,True)
    BW,DW=W.complex();MW,cw=unit_reduce({n:len(b) for n,b in BW.items()},DW)
    HW=homology_all(MW);print('CENTRAL',HW,'unit cancellations',cw,flush=True)
    assert [HW[n]['rank'] for n in range(7)]==[1,3,9,9,10,3,1]
    assert all(not H['torsion'] for H in HW.values())
    BY,DY=Y.complex();MY,cy=unit_reduce({n:len(b) for n,b in BY.items()},DY)
    HY=homology_all(MY);print('BOUNDARY',HY,'unit cancellations',cy,flush=True)
    assert [HY[n]['rank'] for n in range(8)]==[1,4,12,18,18,12,4,1]
    assert [HY[n]['torsion'] for n in range(8)]==[[],[],[],[2],[],[],[],[]]
    F=Collapse(Y,W).matrices(BY,BW)
    dims={n:len(BW.get(n,[]))+len(BY.get(n-1,[])) for n in range(9)}
    DC={}
    for n in range(9):
        nw=len(BW.get(n,[]));nwm=len(BW.get(n-1,[]));DC[n]={}
        for c,col in DW.get(n,{}).items():DC[n][c]=dict(col)
        for c,col in DY.get(n-1,{}).items():
            new=dict(F.get(n-1,{}).get(c,{}))
            for r,v in col.items():new[nwm+r]=-v
            DC[n][nw+c]=new
    MC,cc=unit_reduce(dims,DC);HC=homology_all(MC)
    print('RELATIVE',HC,'unit cancellations',cc,flush=True)
    assert [HC[n]['rank'] for n in range(9)]==[0,0,1,3,10,9,9,3,1]
    assert all(not H['torsion'] for H in HC.values())
    result={'objects':len(C.objects),'morphisms':len(C.morphisms),
            'flags':[sum(len(a)==p for s,a in C.chains) for p in range(4)],
            'central':HW,'boundary':HY,'relative':HC,
            'cancellations':[cw,cy,cc],
            'reduced_matrices':{label:{n:M.tolist() for n,M in mats.items()}
                                for label,mats in [('central',MW),('boundary',MY),('relative',MC)]}}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2,default=int))
    print('ALL KUHN CAP, BOUNDARY, AND COLLAPSE-CHAIN CERTIFICATES PASSED',flush=True)
