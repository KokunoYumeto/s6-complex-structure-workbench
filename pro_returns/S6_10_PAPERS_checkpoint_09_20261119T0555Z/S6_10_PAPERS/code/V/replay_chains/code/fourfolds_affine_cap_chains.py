"""Finite integral chains for a free cyclic affine torus quotient.

The construction uses two finite homological perturbation series.
First the torus fundamental groupoid bar complex contracts to Koszul
chains; then the cyclic group bar resolution contracts to its periodic
resolution.  Affine translations enter the strict groupoid action.
No equivariant-formality assumption is made.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations,product
import sympy as S
from fourfolds_bar_koszul import AbelianBar,CyclicBar,add
from fourfolds_survivor_test import factors,kernel
from fourfolds_vankampen import affine_certificate

def matvec(M,v):return tuple(sum(M[i][j]*v[j] for j in range(len(v))) for i in range(len(M)))
def plus(a,b):return tuple(x+y for x,y in zip(a,b))
def minus(a,b):return tuple(x-y for x,y in zip(a,b))
def floor(x):return x.numerator//x.denominator

class OrbitGroupoid:
    def __init__(self,M,numerator,order):
        self.M=S.Matrix(M);self.r=self.M.rows;self.m=order
        assert self.M**order==S.eye(self.r)
        assert affine_certificate(self.M,S.Matrix(numerator),order)['free']
        self.bar=AbelianBar(self.r);self.zero=self.bar.zero
        self.powers=[tuple(tuple(int(x) for x in row) for row in (self.M**j).tolist()) for j in range(order)]
        b=tuple(Fraction(int(x),order) for x in numerator)
        raw=[tuple(Fraction(0) for _ in range(self.r))]
        for j in range(order):raw.append(plus(raw[-1],matvec(self.powers[j],b)))
        assert all(x.denominator==1 for x in raw[-1])
        self.raw=raw
        self.points=[tuple(x-floor(x) for x in a) for a in raw[:-1]]
        assert len(set(self.points))==order,"the orbit of zero is not free"
        self.z={}
        for s in range(order):
            for a in range(order):
                v=minus(plus(matvec(self.powers[s],self.points[a]),raw[s]),self.points[(a+s)%order])
                assert all(x.denominator==1 for x in v)
                self.z[s,a]=tuple(int(x) for x in v)

    def term(self,objects,arrows,c=1):
        objects=tuple(objects);arrows=tuple(arrows)
        assert len(objects)==len(arrows)+1
        return {} if any(objects[i]==objects[i+1] and g==self.zero for i,g in enumerate(arrows)) else {(objects,arrows):c}

    def d(self,chain):
        out={}
        for (o,a),c in chain.items():
            q=len(a)
            if not q:continue
            add(out,self.term(o[1:],a[1:],c))
            for j in range(1,q):
                add(out,self.term(o[:j]+o[j+1:],a[:j-1]+(plus(a[j-1],a[j]),)+a[j+1:],c*(-1)**j))
            add(out,self.term(o[:-1],a[:-1],c*(-1)**q))
        return out

    def act(self,s,chain):
        out={}
        for (o,a),c in chain.items():
            oo=tuple((j+s)%self.m for j in o)
            aa=tuple(plus(matvec(self.powers[s],g),minus(self.z[s,o[j+1]],self.z[s,o[j]])) for j,g in enumerate(a))
            add(out,self.term(oo,aa,c))
        return out

    def forget(self,chain):
        out={}
        for (o,a),c in chain.items():
            if not any(g==self.zero for g in a):add(out,{a:c})
        return out

    def include_bar(self,chain):
        out={}
        for a,c in chain.items():add(out,self.term((0,)*(len(a)+1),a,c))
        return out

    def prism(self,chain):
        out={}
        for (o,a),c in chain.items():
            q=len(a)
            for j in range(q+1):
                oo=o[:j+1]+(0,)*(q-j+1)
                aa=a[:j]+(self.zero,)+a[j:]
                add(out,self.term(oo,aa,-c*(-1)**j))
        return out

    def project(self,chain):return self.bar.ordinary_project(self.forget(chain))
    def include(self,chain):return self.include_bar(self.bar.ordinary_include(chain))

    @lru_cache(None)
    def h_basis(self,simplex):
        chain={simplex:1}
        out=self.prism(chain)
        add(out,self.include_bar(self.bar.ordinary_homotopy(self.forget(chain))))
        return out

    def h(self,chain):
        out=self.prism(chain)
        add(out,self.include_bar(self.bar.ordinary_homotopy(self.forget(chain))))
        return out

class AffineCap:
    def __init__(self,M,numerator,order):
        self.groupoid=OrbitGroupoid(M,numerator,order)
        self.r=self.groupoid.r;self.m=order
        self.cyclic=CyclicBar(order)
        self.M=S.Matrix(M)

    @lru_cache(None)
    def exterior_action(self,a,I):
        q=len(I);M=self.M**(a%self.m)
        return {J:int(M.extract(J,I).det()) for J in combinations(range(self.r),q) if M.extract(J,I).det()!=0}

    def big_h(self,chain):
        out={};groups={}
        for (s,z),c in chain.items():add(groups.setdefault(s,{}),{z:c})
        for s,z in groups.items():
            for t,v in self.groupoid.h(z).items():add(out,{(s,t):v})
        return out

    def big_p(self,chain):
        out={}
        for (s,z),c in chain.items():
            for I,v in self.groupoid.project({z:1}).items():add(out,{(s,I):c*v})
        return out

    def vertical_project(self,chain):
        term=dict(chain);out=self.big_p(term)
        bound=max((len(s) for s,z in term),default=0)
        for j in range(bound):
            work={k:v for k,v in term.items() if len(k[1][1])<self.r}
            if not work:term={};break
            term=self.big_delta(self.big_h(work))
            term={k:-v for k,v in term.items()}
            add(out,self.big_p(term))
            if not term:break
        assert all(not s for s,z in term)
        return out

    def big_delta(self,chain):
        out={}
        for (s,z),c in chain.items():
            p=len(s);q=len(z[1])
            if not p:continue
            sign=c*(-1)**q
            for zz,v in self.groupoid.act(s[0],{z:1}).items():add(out,{(s[1:],zz):sign*v})
            for j in range(1,p):
                t=s[:j-1]+((s[j-1]+s[j])%self.m,)+s[j+1:]
                if 0 not in t:add(out,{(t,z):sign*(-1)**j})
            add(out,{(s[:-1],z):sign*(-1)**p})
        return out

    @lru_cache(None)
    def vertical_lift(self,s,I):
        term={(s,z):v for z,v in self.groupoid.include({I:1}).items()}
        out=dict(term)
        for j in range(len(s)):
            term=self.big_h(self.big_delta(term))
            term={k:-v for k,v in term.items()}
            add(out,term)
        assert self.big_h(self.big_delta(term))=={}
        return out

    @lru_cache(None)
    def bar_d_basis(self,s,I):
        return self.big_p(self.big_delta(self.vertical_lift(s,I)))

    def bar_d(self,chain):
        out={}
        for (s,I),c in chain.items():add(out,self.bar_d_basis(s,I),c)
        return out

    def first_d(self,chain):
        out={}
        for (s,I),c in chain.items():
            p=len(s);q=len(I)
            if not p:continue
            sign=c*(-1)**q
            for J,v in self.exterior_action(s[0],I).items():add(out,{(s[1:],J):sign*v})
            for j in range(1,p):
                t=s[:j-1]+((s[j-1]+s[j])%self.m,)+s[j+1:]
                if 0 not in t:add(out,{(t,I):sign*(-1)**j})
            add(out,{(s[:-1],I):sign*(-1)**p})
        return out

    def higher_d(self,chain):
        out=self.bar_d(chain);add(out,self.first_d(chain),-1)
        return out

    def horizontal_p(self,chain):
        out={}
        for (s,I),c in chain.items():
            for a,v in self.cyclic.p_basis(s).items():
                for J,w in self.exterior_action(a,I).items():add(out,{(len(s),J):c*v*w})
        return out

    def horizontal_i(self,chain):
        out={}
        for (p,I),c in chain.items():
            for (a,s),v in self.cyclic.i_basis(p).items():
                for J,w in self.exterior_action(a,I).items():add(out,{(s,J):c*v*w})
        return out

    def horizontal_h(self,chain):
        out={}
        for (s,I),c in chain.items():
            for (a,t),v in self.cyclic.h_basis(s).items():
                for J,w in self.exterior_action(a,I).items():add(out,{(t,J):c*v*w*(-1)**len(I)})
        return out

    def periodic_project(self,chain):
        term=dict(chain);out=self.horizontal_p(term)
        bound=max((len(s) for s,I in term),default=0)
        for j in range(bound):
            work={k:v for k,v in term.items() if len(k[1])<self.r}
            if not work:term={};break
            term=self.higher_d(self.horizontal_h(work))
            term={k:-v for k,v in term.items()}
            add(out,self.horizontal_p(term))
            if not term:break
        assert self.higher_d(self.horizontal_h(term))=={}
        return out

    def total_lift(self,chain):
        out={}
        for (p,I),c in chain.items():
            for (s,J),v in self.periodic_lift(p,I).items():
                add(out,self.vertical_lift(s,J),c*v)
        return out

    def total_project(self,chain):
        return self.periodic_project(self.vertical_project(chain))

    def periodic_d(self,chain):
        out={}
        for (p,I),c in chain.items():
            if not p:continue
            for a,v in self.cyclic.period_d(p,{0:1}).items():
                for J,w in self.exterior_action(a,I).items():add(out,{(p-1,J):c*v*w*(-1)**len(I)})
        return out

    @lru_cache(None)
    def periodic_lift(self,p,I):
        term=self.horizontal_i({(p,I):1});out=dict(term)
        for j in range(p):
            term=self.horizontal_h(self.higher_d(term))
            term={k:-v for k,v in term.items()}
            add(out,term)
            if not term:break
        assert self.horizontal_h(self.higher_d(term))=={}
        return out

    @lru_cache(None)
    def d_basis(self,p,I):
        out=self.periodic_d({(p,I):1})
        add(out,self.horizontal_p(self.higher_d(self.periodic_lift(p,I))))
        assert all(a+len(J)==p+len(I)-1 for a,J in out)
        return out

    def d(self,chain):
        out={}
        for (p,I),c in chain.items():add(out,self.d_basis(p,I),c)
        return out

    def bases(self,n):
        return [(n-q,I) for q in range(min(n,self.r)+1) for I in combinations(range(self.r),q)]

    def clear_intermediates(self):
        # A total-degree calculation never needs bar differentials from a
        # different total degree. Keep only the small final integer maps.
        self.vertical_lift.cache_clear()
        self.periodic_lift.cache_clear()
        self.bar_d_basis.cache_clear()
        self.groupoid.h_basis.cache_clear()
        self.groupoid.bar.h_basis.cache_clear()
        self.groupoid.bar.p_basis.cache_clear()
        self.cyclic.h_basis.cache_clear()
        self.cyclic.p_basis.cache_clear()

    def matrices(self,degree,progress=False):
        matrices={0:S.zeros(0,1)}
        for n in range(1,degree+2):
            if progress:print('building differential',n,flush=True)
            source=self.bases(n);target=self.bases(n-1);indices={b:i for i,b in enumerate(target)}
            D=S.zeros(len(target),len(source))
            for j,b in enumerate(source):
                chain=self.d_basis(*b)
                assert self.d(chain)=={}
                for t,c in chain.items():D[indices[t],j]=c
                if n>=7 and j%8==7:self.clear_intermediates()
            assert matrices[n-1]*D==S.zeros(matrices[n-1].rows,D.cols)
            matrices[n]=D
            self.clear_intermediates()
        return matrices

def homology(matrices,n):
    D=matrices[n];E=matrices[n+1];K=kernel(D)
    coordinates=K.gauss_jordan_solve(E)[0] if E.cols else S.zeros(K.cols,0)
    assert all(S.denom(x)==1 for x in coordinates)
    fs=factors(coordinates)
    return {'rank':K.cols-E.rank(),'torsion':[d for d in fs if d>1]}

class CapMap:
    """A strict equivariant integral torus map, transferred to finite chains."""
    def __init__(self,source,target,L):
        assert source.m==target.m
        self.source=source;self.target=target;self.L=S.Matrix(L)
        assert self.L*source.M==target.M*self.L
        self.matrix=tuple(tuple(int(x) for x in row) for row in self.L.tolist())
        self.offsets=[]
        for a in range(source.m):
            k=minus(matvec(self.matrix,source.groupoid.points[a]),target.groupoid.points[a])
            assert all(x.denominator==1 for x in k)
            self.offsets.append(tuple(int(x) for x in k))

    def big_map(self,chain):
        out={};G=self.target.groupoid
        for (s,(o,a)),c in chain.items():
            aa=tuple(plus(matvec(self.matrix,g),minus(self.offsets[o[j+1]],self.offsets[o[j]]))
                     for j,g in enumerate(a))
            for z,v in G.term(o,aa,c).items():add(out,{(s,z):v})
        return out

    @lru_cache(None)
    def basis(self,p,I):
        chain=self.source.total_lift({(p,I):1})
        return self.target.total_project(self.big_map(chain))

    def apply(self,chain):
        out={}
        for (p,I),c in chain.items():add(out,self.basis(p,I),c)
        return out

    def matrix_degree(self,n):
        src=self.source.bases(n);dst=self.target.bases(n);ix={b:i for i,b in enumerate(dst)}
        F=S.zeros(len(dst),len(src))
        for j,b in enumerate(src):
            out=self.basis(*b)
            assert self.target.d(out)==self.apply(self.source.d_basis(*b))
            for t,c in out.items():F[ix[t],j]=c
        return F

if __name__=='__main__':
    cases=[('circle2',[[1]],[1],2,3,[1,1,0,0],[[],[],[],[]]),
           ('circle3',[[1]],[1],3,3,[1,1,0,0],[[],[],[],[]]),
           ('Klein',[[1,0],[0,-1]],[1,0],2,3,[1,1,0,0],[[],[2],[],[]]),
           ('Klein_nonfixed',[[1,0],[0,-1]],[1,1],2,3,[1,1,0,0],[[],[2],[],[]]),
           ('halfturn3',[[1,0,0],[0,-1,0],[0,0,-1]],[1,0,0],2,4,
             [1,1,1,1,0],[[],[2,2],[],[],[]])]
    for name,M,v,m,degree,ranks,torsion in cases:
        print('CASE',name,flush=True)
        cap=AffineCap(M,v,m)
        G=cap.groupoid
        # All objects, and all two-arrow simplices from this small alphabet.
        alphabet=G.bar.units+(tuple(-1 for _ in range(G.r)),)
        for o in product(range(m),repeat=3):
            for a in product(alphabet,repeat=2):
                chain=G.term(o,a)
                lhs=G.d(G.h(chain));add(lhs,G.h(G.d(chain)))
                rhs=dict(chain);add(rhs,G.include(G.project(chain)),-1)
                assert lhs==rhs
                assert G.project(G.h(chain))=={} and G.h(G.h(chain))=={}
                for s in range(m):
                    assert G.d(G.act(s,chain))==G.act(s,G.d(chain))
        mats=cap.matrices(degree)
        for n in range(degree+1):
            H=homology(mats,n);print('H',n,H,flush=True)
            assert H=={'rank':ranks[n],'torsion':torsion[n]}
    print('ALL FIVE AFFINE-CAP CHAIN TESTS PASSED',flush=True)
