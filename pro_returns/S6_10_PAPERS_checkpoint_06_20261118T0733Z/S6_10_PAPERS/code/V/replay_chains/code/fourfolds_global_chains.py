"""Exact complement chains and marked cap-to-complement chain maps.

The complement is B(Z^r semidirect F_k).  A bar-to-bisimplicial
Alexander--Whitney map, the integral torus bar contraction, and the
Fox/tree contraction of F_k retain all higher chain-map corrections.
No homology-level substitute is used for a boundary map.
"""
from functools import lru_cache
from itertools import combinations,product
import sympy as S
from fourfolds_bar_koszul import AbelianBar,add
from fourfolds_affine_cap_chains import matvec,plus,minus,CapMap

def word(*parts):
    out=[]
    for part in parts:
        for a in part:
            if out and out[-1]==-a:out.pop()
            else:out.append(a)
    return tuple(out)

def inverse(w):return tuple(-a for a in w[::-1])

class FreeBar:
    def __init__(self,rank):self.rank=rank
    def term(self,a,s,c=1):
        return {} if any(not g for g in s) else {(a,s):c}
    def shift(self,chain,a):
        out={}
        for (b,s),c in chain.items():add(out,{(word(a,b),s):c})
        return out
    def dbar(self,chain):
        out={}
        for (a,s),c in chain.items():
            q=len(s)
            if not q:continue
            add(out,self.term(word(a,s[0]),s[1:],c))
            for j in range(1,q):
                add(out,self.term(a,s[:j-1]+(word(s[j-1],s[j]),)+s[j+1:],c*(-1)**j))
            add(out,self.term(a,s[:-1],c*(-1)**q))
        return out
    def sbar(self,chain):
        out={}
        for (a,s),c in chain.items():add(out,self.term((),(a,)+s,c))
        return out
    def fox(self,w):
        out={};prefix=()
        for a in w:
            if a>0:add(out,{(prefix,a-1):1})
            else:add(out,{(word(prefix,(a,)),-a-1):-1})
            prefix=word(prefix,(a,))
        return out
    def p_basis(self,s):
        if not s:return {((),-1):1}
        if len(s)==1:return self.fox(s[0])
        return {}
    def project(self,chain):
        out={}
        for (a,s),c in chain.items():
            for (b,j),v in self.p_basis(s).items():add(out,{(word(a,b),j):c*v})
        return out
    def i_basis(self,j):return {((),() if j<0 else ((j+1,),)):1}
    def include(self,chain):
        out={}
        for (a,j),c in chain.items():add(out,self.shift(self.i_basis(j),a),c)
        return out
    def dtree(self,chain):
        out={}
        for (a,j),c in chain.items():
            if j>=0:add(out,{(word(a,(j+1,)),-1):c,(a,-1):-c})
        return out
    @lru_cache(None)
    def h_basis(self,s):
        if not s:return {}
        out={((),s):1}
        add(out,self.include(self.p_basis(s)),-1)
        add(out,self.homotopy(self.dbar({((),s):1})),-1)
        return self.sbar(out)
    def homotopy(self,chain):
        out={}
        for (a,s),c in chain.items():add(out,self.shift(self.h_basis(s),a),c)
        return out

class Complement:
    def __init__(self,matrices):
        self.M=tuple(S.Matrix(M) for M in matrices)
        self.k=len(self.M);self.r=self.M[0].rows
        assert all(M.shape==(self.r,self.r) and abs(M.det())==1 for M in self.M)
        self.zero=(0,)*self.r;self.identity=(self.zero,())
        self.bar=AbelianBar(self.r);self.free=FreeBar(self.k)
        self.generators={i+1:M for i,M in enumerate(self.M)}
        self.generators.update({-i-1:M.inv() for i,M in enumerate(self.M)})

    @lru_cache(None)
    def matrix(self,w):
        out=S.eye(self.r)
        for a in w:out=out*self.generators[a]
        return out
    def mv(self,M,v):return tuple(int(x) for x in M*S.Matrix(v))
    def mul(self,a,b):
        x,w=a;y,u=b
        return plus(x,self.mv(self.matrix(w),y)),word(w,u)
    def inv(self,a):
        x,w=a;u=inverse(w)
        return tuple(-v for v in self.mv(self.matrix(u),x)),u
    def power(self,a,n):
        if n<0:return self.power(self.inv(a),-n)
        out=self.identity
        for j in range(n):out=self.mul(out,a)
        return out
    def translate(self,v):return tuple(int(x) for x in v),()
    def peripheral(self,w):return self.zero,tuple(w)
    def group_term(self,s,c=1):
        return {} if any(g==self.identity for g in s) else {tuple(s):c}
    def group_d(self,chain):
        out={}
        for s,c in chain.items():
            n=len(s)
            if not n:continue
            add(out,self.group_term(s[1:],c))
            for j in range(1,n):
                add(out,self.group_term(s[:j-1]+(self.mul(s[j-1],s[j]),)+s[j+1:],c*(-1)**j))
            add(out,self.group_term(s[:-1],c*(-1)**n))
        return out
    def right_action(self,w,v):return self.mv(self.matrix(inverse(w)),v)
    @lru_cache(None)
    def exterior(self,w,I):
        M=self.matrix(inverse(w));q=len(I);out={}
        for J in combinations(range(self.r),q):
            value=M.extract(J,I).det()
            if value:out[J]=int(value)
        return out

    def big_term(self,s,z,c=1):
        if any(not g for g in s) or any(v==self.zero for v in z):return {}
        return {(tuple(s),tuple(z)):c}
    def big_vertical_d(self,chain):
        out={}
        for (s,z),c in chain.items():
            for zz,v in self.bar.ordinary_d({z:1}).items():add(out,{(s,zz):c*v})
        return out
    def big_delta(self,chain):
        out={}
        for (s,z),c in chain.items():
            p=len(s);q=len(z)
            if not p:continue
            sign=c*(-1)**q
            zz=tuple(self.right_action(s[0],a) for a in z)
            add(out,self.big_term(s[1:],zz,sign))
            for j in range(1,p):
                ss=s[:j-1]+(word(s[j-1],s[j]),)+s[j+1:]
                add(out,self.big_term(ss,z,sign*(-1)**j))
            add(out,self.big_term(s[:-1],z,sign*(-1)**p))
        return out
    def big_d(self,chain):
        out=self.big_vertical_d(chain);add(out,self.big_delta(chain));return out
    def aw(self,chain):
        out={}
        for s,c in chain.items():
            prefix=();vectors=[];base=[]
            for x,w in s:
                vectors.append(self.mv(self.matrix(prefix),x))
                base.append(w);prefix=word(prefix,w)
            n=len(s)
            for p in range(n+1):
                add(out,self.big_term(base[:p],vectors[p:],c*(-1)**(p*(n-p))))
        return out
    def big_h(self,chain):
        out={};groups={}
        for (s,z),c in chain.items():add(groups.setdefault(s,{}),{z:c})
        for s,z in groups.items():
            for zz,v in self.bar.ordinary_homotopy(z).items():add(out,{(s,zz):v})
        return out
    def big_p(self,chain):
        out={}
        for (s,z),c in chain.items():
            for I,v in self.bar.ordinary_project({z:1}).items():add(out,{(s,I):c*v})
        return out
    def vertical_project(self,chain):
        term=dict(chain);out=self.big_p(term)
        for j in range(max((len(s) for s,z in chain),default=0)):
            # Every further correction raises vertical degree; once it
            # exceeds r the final exterior projection is identically0.
            work={k:v for k,v in term.items() if len(k[1])<self.r and
                  any(self.matrix(w)!=S.eye(self.r) for w in k[0])}
            if not work:term={};break
            term=self.big_delta(self.big_h(work));term={k:-v for k,v in term.items()}
            add(out,self.big_p(term))
            if not term:break
        assert all(not s for s,z in term)
        return out
    @lru_cache(None)
    def vertical_lift(self,s,I):
        term={(s,z):v for z,v in self.bar.ordinary_include({I:1}).items()}
        out=dict(term)
        for j in range(len(s)):
            term=self.big_h(self.big_delta(term));term={k:-v for k,v in term.items()}
            add(out,term)
            if not term:break
        assert self.big_h(self.big_delta(term))=={}
        return out
    @lru_cache(None)
    def bar_d_basis(self,s,I):return self.big_p(self.big_delta(self.vertical_lift(s,I)))
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
            for J,v in self.exterior(s[0],I).items():add(out,{(s[1:],J):sign*v})
            for j in range(1,p):
                ss=s[:j-1]+(word(s[j-1],s[j]),)+s[j+1:]
                if all(ss):add(out,{(ss,I):sign*(-1)**j})
            add(out,{(s[:-1],I):sign*(-1)**p})
        return out
    def higher_d(self,chain):
        out=self.bar_d(chain);add(out,self.first_d(chain),-1);return out
    def horizontal_p(self,chain):
        out={}
        for (s,I),c in chain.items():
            for (a,j),v in self.free.p_basis(s).items():
                for J,w in self.exterior(a,I).items():add(out,{(j,J):c*v*w})
        return out
    def horizontal_h(self,chain):
        out={}
        for (s,I),c in chain.items():
            for (a,t),v in self.free.h_basis(s).items():
                for J,w in self.exterior(a,I).items():add(out,{(t,J):c*v*w*(-1)**len(I)})
        return out
    def project(self,chain):
        chain=self.vertical_project(chain)
        term=dict(chain);out=self.horizontal_p(term)
        for j in range(max((len(s) for s,I in chain),default=0)):
            work={k:v for k,v in term.items() if len(k[1])<self.r}
            if not work:term={};break
            term=self.higher_d(self.horizontal_h(work));term={k:-v for k,v in term.items()}
            add(out,self.horizontal_p(term))
            if not term:break
        assert self.higher_d(self.horizontal_h(term))=={}
        return out
    def from_group(self,chain):return self.project(self.aw(chain))
    def d(self,chain):
        out={}
        for (j,I),c in chain.items():
            if j<0:continue
            sign=c*(-1)**len(I)
            for J,v in self.exterior((j+1,),I).items():add(out,{(-1,J):sign*v})
            add(out,{(-1,I):-sign})
        return out
    def bases(self,n):
        return [(-1,I) for I in combinations(range(self.r),n)]+[
            (j,I) for j in range(self.k) for I in combinations(range(self.r),n-1)] if n else [(-1,())]
    def matrix_degree(self,n):
        src=self.bases(n);dst=self.bases(n-1) if n else [];ix={b:i for i,b in enumerate(dst)}
        D=S.zeros(len(dst),len(src))
        for j,b in enumerate(src):
            for t,c in self.d({b:1}).items():D[ix[t],j]=c
        return D
    def clear_intermediates(self):
        self.vertical_lift.cache_clear()
        self.bar_d_basis.cache_clear()
        self.bar.h_basis.cache_clear()
        self.bar.p_basis.cache_clear()
        self.free.h_basis.cache_clear()

class FiniteBoundaryToComplement:
    def __init__(self,boundary,target,index):
        self.source=boundary;self.target=target;self.index=index
        r=target.r;m=boundary.m
        assert boundary.r==r+1
        assert boundary.M==S.diag(S.ones(1,1),target.M[index])
        self.w=tuple(int(x) for x in boundary.groupoid.raw[m][1:])
        self.g=target.peripheral((index+1,))
        self.gamma=[]
        for j,raw in enumerate(boundary.groupoid.raw[:-1]):
            floor=tuple(x.numerator//x.denominator for x in raw)
            assert floor[0]==0
            self.gamma.append(target.mul(target.translate(tuple(-x for x in floor[1:])),target.power(self.g,j)))
    def translation(self,v):
        E=self.target;theta=v[0]
        x=tuple(v[j+1]-theta*self.w[j] for j in range(E.r))
        return E.mul(E.translate(x),E.power(self.g,self.source.m*theta))
    def quotient(self,chain):
        out={};E=self.target
        for (base,(objects,arrows)),c in chain.items():
            if base:continue
            s=[]
            for j,a in enumerate(arrows):
                z=E.mul(E.inv(self.gamma[objects[j]]),self.translation(a))
                s.append(E.mul(z,self.gamma[objects[j+1]]))
            add(out,E.group_term(s,c))
        return out
    @lru_cache(None)
    def basis(self,p,I):
        big=self.source.total_lift({(p,I):1})
        return self.target.from_group(self.quotient(big))
    def apply(self,chain):
        out={}
        for (p,I),c in chain.items():add(out,self.basis(p,I),c)
        return out
    def matrix_degree(self,n):
        src=self.source.bases(n);dst=self.target.bases(n);ix={b:i for i,b in enumerate(dst)}
        F=S.zeros(len(dst),len(src))
        for j,b in enumerate(src):
            image=self.basis(*b)
            assert self.target.d(image)==self.apply(self.source.d_basis(*b))
            for t,c in image.items():F[ix[t],j]=c
        return F

class AffineGraphBoundary:
    """The finite cap boundary as a one-edge affine torus bundle.

    Its chain ranks are binomial(r,n)+binomial(r,n-1), so using it
    avoids the unnecessary periodic rank-(r+1) boundary resolution.
    Both maps retain the translation through the orbit groupoid.
    """
    def __init__(self,cap,target,index,lattice=None):
        self.cap=cap;self.target=target;self.index=index
        self.r=cap.r;self.groupoid=cap.groupoid
        self.lattice=S.eye(self.r) if lattice is None else S.Matrix(lattice)
        assert abs(self.lattice.det())==1
        assert target.M[index]*self.lattice==self.lattice*cap.M
        self.g=target.peripheral((index+1,))
    def bases(self,n):
        return [(-1,I) for I in combinations(range(self.r),n)]+[
            (0,I) for I in combinations(range(self.r),n-1)] if n else [(-1,())]
    def d(self,chain):
        out={}
        for (j,I),c in chain.items():
            if j<0:continue
            sign=c*(-1)**len(I)
            for J,v in self.cap.exterior_action(1,I).items():add(out,{(-1,J):sign*v})
            add(out,{(-1,I):-sign})
        return out
    def matrix_degree(self,n):
        src=self.bases(n);dst=self.bases(n-1) if n else [];ix={b:i for i,b in enumerate(dst)}
        D=S.zeros(len(dst),len(src))
        for j,b in enumerate(src):
            for t,c in self.d({b:1}).items():D[ix[t],j]=c
        return D
    def lift(self,j,I):return self.cap.vertical_lift(() if j<0 else (1,),I)
    def big_to_complement(self,chain):
        E=self.target;G=self.groupoid;out={}
        for (base,(objects,arrows)),c in chain.items():
            if not base:
                add(out,E.group_term([E.translate(E.mv(self.lattice,a)) for a in arrows],c));continue
            assert base==(1,)
            q=len(arrows)
            transformed=[]
            for j,a in enumerate(arrows):
                transformed.append(plus(matvec(G.powers[1],a),minus(G.z[1,objects[j+1]],G.z[1,objects[j]])))
            for j in range(q+1):
                eta=E.mul(E.inv(self.g),E.translate(E.mv(self.lattice,G.z[1,objects[j]])))
                s=[E.translate(E.mv(self.lattice,a)) for a in arrows[:j]]+[eta]+[
                    E.translate(E.mv(self.lattice,a)) for a in transformed[j:]]
                add(out,E.group_term(s,c*(-1)**(q+j)))
        return out
    @lru_cache(None)
    def cap_basis(self,j,I):return self.cap.total_project(self.lift(j,I))
    @lru_cache(None)
    def complement_basis(self,j,I):
        return self.target.from_group(self.big_to_complement(self.lift(j,I)))
    def apply(self,chain,to_cap=False):
        method=self.cap_basis if to_cap else self.complement_basis;out={}
        for (j,I),c in chain.items():add(out,method(j,I),c)
        return out
    def map_degree(self,n,to_cap=False):
        target=self.cap if to_cap else self.target
        src=self.bases(n);dst=target.bases(n);ix={b:i for i,b in enumerate(dst)}
        F=S.zeros(len(dst),len(src));method=self.cap_basis if to_cap else self.complement_basis
        for j,b in enumerate(src):
            image=method(*b)
            assert target.d(image)==self.apply(self.d({b:1}),to_cap)
            for t,c in image.items():F[ix[t],j]=c
        return F

class SuspensionBoundaryToCap:
    """Exact shortcut when M=1+D and v=epsilon e0, epsilon=+-1.

    The cap group is Z^(r-1) semidirect_D Z, with root generator g.
    Fibre (u,a) maps to (a,g^(epsilon*m*u)).  This is a geometric
    mapping-torus model, not a cohomology replacement.
    """
    def __init__(self,source,target,epsilon):
        self.source=source;self.target=target;self.epsilon=epsilon
        self.m=source.cap.m;self.G=source.groupoid
        assert epsilon in (-1,1)
        assert source.cap.M==S.diag(1,target.M[0])
        assert self.G.raw[1]==(S.Rational(epsilon,self.m),)+(0,)*(source.r-1)
        self.g=target.peripheral((1,))
    def fibre(self,a):
        E=self.target
        return E.mul(E.translate(a[1:]),E.power(self.g,self.epsilon*self.m*a[0]))
    def big_map(self,chain):
        E=self.target;G=self.G;out={}
        for (base,(objects,arrows)),c in chain.items():
            if not base:
                add(out,E.group_term([self.fibre(a) for a in arrows],c));continue
            assert base==(1,);q=len(arrows);transformed=[]
            for j,a in enumerate(arrows):
                transformed.append(plus(matvec(G.powers[1],a),minus(G.z[1,objects[j+1]],G.z[1,objects[j]])))
            for j in range(q+1):
                eta=E.mul(E.inv(self.g),self.fibre(G.z[1,objects[j]]))
                s=[self.fibre(a) for a in arrows[:j]]+[eta]+[self.fibre(a) for a in transformed[j:]]
                add(out,E.group_term(s,c*(-1)**(q+j)))
        return out
    @lru_cache(None)
    def basis(self,j,I):
        return self.target.from_group(self.big_map(self.source.lift(j,I)))
    def apply(self,chain):
        out={}
        for (j,I),c in chain.items():add(out,self.basis(j,I),c)
        return out
    def matrix_degree(self,n):
        src=self.source.bases(n);dst=self.target.bases(n);ix={b:i for i,b in enumerate(dst)}
        F=S.zeros(len(dst),len(src))
        for j,b in enumerate(src):
            image=self.basis(*b)
            assert self.target.d(image)==self.apply(self.source.d({b:1}))
            for t,c in image.items():F[ix[t],j]=c
        return F

def shuffles(p,q):
    for base_positions in combinations(range(p+q),p):
        bp=set(base_positions)
        steps=tuple('B' if j in bp else 'V' for j in range(p+q))
        sign=(-1)**sum(1 for i in range(p+q) for j in range(i+1,p+q) if steps[i]=='B' and steps[j]=='V')
        yield steps,sign

class CuspBoundaryToComplement:
    def __init__(self,source,target,adapted,clutch=None):
        self.source=source;self.target=target
        assert target.r==6
        P=S.Matrix(adapted);assert abs(P.det())==1
        self.A=P[:,:3];self.B=P[:,3:]
        w=inverse(tuple(range(1,target.k+1)))
        U=target.matrix(w)
        assert U*self.A==self.A and U*self.B==self.B+self.A
        clutch=tuple(clutch) if clutch is not None else target.zero
        self.c=target.mul(target.peripheral(w),target.translate(tuple(-x for x in clutch)))
    def phase(self,z):
        E=self.target
        return E.mul(E.power(self.c,z[0]),E.translate(tuple(self.A*S.Matrix(z[1:]))))
    def big_map(self,chain):
        E=self.target;C=self.source.C;out={}
        for ((start,arrows),simplex),c in chain.items():
            for steps,sign in shuffles(len(arrows),len(simplex)):
                prefix=(0,0,0);i=j=0;s=[]
                for step in steps:
                    if step=='B':
                        w=C.morphisms[arrows[i]][2];i+=1
                        s.append(E.translate(tuple(self.B*S.Matrix(w))))
                        prefix=plus(prefix,w)
                    else:
                        z=simplex[j];j+=1
                        zz=(z[0],)+tuple(z[a+1]+prefix[a]*z[0] for a in range(3))
                        s.append(self.phase(zz))
                add(out,E.group_term(s,c*sign))
        return out
    @lru_cache(None)
    def basis(self,base,I):
        return self.target.from_group(self.big_map(self.source.lift(base,I)))
    def apply(self,chain):
        out={}
        for (base,I),c in chain.items():add(out,self.basis(base,I),c)
        return out
    def matrix_degree(self,n,bases):
        src=bases.get(n,[]);dst=self.target.bases(n);ix={b:i for i,b in enumerate(dst)}
        F=S.zeros(len(dst),len(src))
        for j,b in enumerate(src):
            image=self.basis(*b)
            assert self.target.d(image)==self.apply(self.source.d_basis(*b))
            for t,c in image.items():F[ix[t],j]=c
        return F

if __name__=='__main__':
    F=FreeBar(2);alphabet=((1,),(-1,),(2,),(1,2,-1),(-2,1))
    total=0
    for n in range(4):
        for s in product(alphabet,repeat=n):
            z={((),s):1}
            assert F.dbar(F.dbar(z))=={}
            assert F.project(F.dbar(z))==F.dtree(F.project(z))
            lhs=F.dbar(F.homotopy(z));add(lhs,F.homotopy(F.dbar(z)))
            rhs=dict(z);add(rhs,F.include(F.project(z)),-1)
            assert lhs==rhs
            assert F.project(F.homotopy(z))=={} and F.homotopy(F.homotopy(z))=={}
            total+=1
    print('FREE BAR/Fox CONTRACTION:',total,'SIMPLICES PASSED',flush=True)
    E=Complement([[[1,1],[0,1]],[[0,-1],[1,0]]])
    alphabet=[E.translate((1,0)),E.translate((0,1)),E.peripheral((1,)),E.peripheral((2,)),((1,-1),(1,2))]
    total=0
    for n in range(4):
        for s in product(alphabet,repeat=n):
            z={s:1}
            assert E.big_d(E.aw(z))==E.aw(E.group_d(z))
            assert E.d(E.from_group(z))==E.from_group(E.group_d(z))
            total+=1
    print('NONCOMMUTING SEMIDIRECT AW AND FINITE PROJECTION:',total,'SIMPLICES PASSED',flush=True)
