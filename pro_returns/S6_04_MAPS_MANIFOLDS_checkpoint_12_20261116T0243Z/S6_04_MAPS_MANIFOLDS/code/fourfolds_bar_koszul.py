"""Explicit integral bar-to-Koszul contractions.

All chains are finite dictionaries.  Universal-resolution coefficients
are integer group-ring monomials.  The recursive construction terminates
by chain degree; no truncation is used inside a comparison or homotopy.
The executed verification set is stated at the end of this file.
"""
from functools import lru_cache
from itertools import permutations,product,combinations

def add(target,source,scale=1):
    for key,value in source.items():
        z=target.get(key,0)+scale*value
        if z:target[key]=z
        else:target.pop(key,None)
    return target

def parity(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))

class AbelianBar:
    def __init__(self,rank):
        self.rank=rank;self.zero=(0,)*rank
        self.units=tuple(tuple(int(i==j) for i in range(rank)) for j in range(rank))

    def plus(self,a,b):return tuple(x+y for x,y in zip(a,b))

    def bar_term(self,a,s,c=1):
        return {} if any(g==self.zero for g in s) else {(a,s):c}

    def bar_shift(self,chain,a):
        out={}
        for (b,s),c in chain.items():add(out,{(self.plus(a,b),s):c})
        return out

    def koszul_shift(self,chain,a):
        out={}
        for (b,I),c in chain.items():add(out,{(self.plus(a,b),I):c})
        return out

    def dbar(self,chain):
        out={}
        for (a,s),c in chain.items():
            q=len(s)
            if not q:continue
            add(out,self.bar_term(self.plus(a,s[0]),s[1:],c))
            for j in range(1,q):
                t=s[:j-1]+(self.plus(s[j-1],s[j]),)+s[j+1:]
                add(out,self.bar_term(a,t,c*(-1)**j))
            add(out,self.bar_term(a,s[:-1],c*(-1)**q))
        return out

    def dkoszul(self,chain):
        out={}
        for (a,I),c in chain.items():
            for j,i in enumerate(I):
                J=I[:j]+I[j+1:];sgn=c*(-1)**j
                add(out,{(self.plus(a,self.units[i]),J):sgn,(a,J):-sgn})
        return out

    def sbar(self,chain):
        out={}
        for (a,s),c in chain.items():
            add(out,self.bar_term(self.zero,(a,)+s,c))
        return out

    def skoszul(self,chain):
        out={}
        for (a,I),c in chain.items():
            stop=I[0] if I else self.rank
            for j in range(stop):
                aj=a[j]
                terms=range(aj) if aj>=0 else range(aj,0)
                sign=1 if aj>=0 else -1
                for k in terms:
                    b=(0,)*j+(k,)+a[j+1:]
                    add(out,{(b,(j,)+I):c*sign})
        return out

    @lru_cache(None)
    def i_basis(self,I):
        out={}
        for p in permutations(I):
            add(out,self.bar_term(self.zero,tuple(self.units[i] for i in p),parity(p)))
        return out

    def include(self,chain):
        out={}
        for (a,I),c in chain.items():add(out,self.bar_shift(self.i_basis(I),a),c)
        return out

    @lru_cache(None)
    def p_basis(self,s):
        q=len(s)
        if not q:return {(self.zero,()):1}
        if q>self.rank:return {}
        # All non-first faces have p-image in im(s_K), killed by s_K.
        return self.skoszul(self.koszul_shift(self.p_basis(s[1:]),s[0]))

    def project(self,chain):
        out={}
        for (a,s),c in chain.items():add(out,self.koszul_shift(self.p_basis(s),a),c)
        return out

    @lru_cache(None)
    def h_basis(self,s):
        if not s:return {}
        # h on a coefficient-one bar has only coefficient-one terms.
        # Thus s_B kills all non-first faces and the original bar.
        out=self.sbar(self.include(self.p_basis(s)))
        out={k:-v for k,v in out.items()}
        add(out,self.sbar(self.bar_shift(self.h_basis(s[1:]),s[0])),-1)
        return out

    def homotopy(self,chain):
        out={}
        for (a,s),c in chain.items():add(out,self.bar_shift(self.h_basis(s),a),c)
        return out

    def augment_bar(self,chain):
        out={}
        for (a,s),c in chain.items():add(out,{s:c})
        return out

    def augment_koszul(self,chain):
        out={}
        for (a,I),c in chain.items():add(out,{I:c})
        return out

    def ordinary_project(self,chain):
        # Augmentation of the recursive Koszul projection is the ordered
        # cup formula.  It follows by induction from skoszul, and avoids
        # constructing group-ring coefficients which are then discarded.
        out={}
        for s,c in chain.items():
            for I in combinations(range(self.rank),len(s)):
                value=c
                for g,i in zip(s,I):value*=g[i]
                if value:add(out,{I:value})
        return out

    def ordinary_include(self,chain):
        out={}
        for I,c in chain.items():add(out,self.augment_bar(self.i_basis(I)),c)
        return out

    def ordinary_homotopy(self,chain):
        # h i=0, so remove the whole alternating Koszul image before
        # expanding individual bars. This makes exact cancellations occur
        # before, rather than after, potentially large universal chains.
        chain=dict(chain)
        add(chain,self.ordinary_include(self.ordinary_project(chain)),-1)
        out={}
        for s,c in chain.items():add(out,self.augment_bar(self.h_basis(s)),c)
        return out

    def ordinary_d(self,chain):
        return self.augment_bar(self.dbar({(self.zero,s):c for s,c in chain.items()}))

class CyclicBar:
    def __init__(self,order):assert order>=2;self.order=order

    def term(self,a,s,c=1):
        a%=self.order;s=tuple(x%self.order for x in s)
        return {} if any(x==0 for x in s) else {(a,s):c}

    def shift(self,chain,a):
        out={}
        for (b,s),c in chain.items():add(out,{((a+b)%self.order,s):c})
        return out

    def dbar(self,chain):
        out={}
        for (a,s),c in chain.items():
            q=len(s)
            if not q:continue
            add(out,self.term(a+s[0],s[1:],c))
            for j in range(1,q):
                add(out,self.term(a,s[:j-1]+(s[j-1]+s[j],)+s[j+1:],c*(-1)**j))
            add(out,self.term(a,s[:-1],c*(-1)**q))
        return out

    def sbar(self,chain):
        out={}
        for (a,s),c in chain.items():add(out,self.term(0,(a,)+s,c))
        return out

    def period_d(self,q,chain):
        if q==0:return {}
        out={}
        shifts=range(self.order) if q%2==0 else (0,1)
        for a,c in chain.items():
            for j in shifts:add(out,{(a+j)%self.order:c*(1 if q%2==0 or j==1 else -1)})
        return out

    def period_s(self,q,chain):
        out={}
        for a,c in chain.items():
            if q%2==0:
                for j in range(a):add(out,{j:c})
            elif a==self.order-1:add(out,{0:c})
        return out

    @lru_cache(None)
    def i_basis(self,q):
        if q==0:return {(0,()):1}
        out={}
        for a,c in self.period_d(q,{0:1}).items():add(out,self.shift(self.i_basis(q-1),a),c)
        return self.sbar(out)

    def include(self,q,chain):
        out={}
        for a,c in chain.items():add(out,self.shift(self.i_basis(q),a),c)
        return out

    @lru_cache(None)
    def p_basis(self,s):
        q=len(s)
        if not q:return {0:1}
        shifted={(a+s[0])%self.order:v for a,v in self.p_basis(s[1:]).items()}
        return self.period_s(q-1,shifted)

    def project(self,chain):
        out={}
        for (a,s),c in chain.items():
            for b,z in self.p_basis(s).items():add(out,{(a+b)%self.order:c*z})
        return out

    @lru_cache(None)
    def h_basis(self,s):
        if not s:return {}
        out=self.sbar(self.include(len(s),self.p_basis(s)))
        out={k:-v for k,v in out.items()}
        add(out,self.sbar(self.shift(self.h_basis(s[1:]),s[0])),-1)
        return out

    def homotopy(self,chain):
        out={}
        for (a,s),c in chain.items():add(out,self.shift(self.h_basis(s),a),c)
        return out

if __name__=='__main__':
    # Exactly these three ranks, vector alphabets, and degrees are tested.
    abelian_count=0
    for r in (1,2,3):
        K=AbelianBar(r);zero=K.zero
        alphabet=K.units+(tuple(-1 for _ in range(r)),tuple(2 for _ in range(r)))
        for q in range(4):
            for s in product(alphabet,repeat=q):
                chain={(zero,s):1}
                assert K.dbar(K.dbar(chain))=={}
                assert K.project(K.dbar(chain))==K.dkoszul(K.project(chain))
                assert K.ordinary_project({s:1})==K.augment_koszul(K.p_basis(s))
                lhs=K.dbar(K.homotopy(chain))
                add(lhs,K.homotopy(K.dbar(chain)))
                rhs=dict(chain);add(rhs,K.include(K.project(chain)),-1)
                assert lhs==rhs
                abelian_count+=1
        from itertools import combinations
        for q in range(r+1):
            for I in combinations(range(r),q):
                assert K.project(K.i_basis(I))=={(zero,I):1}
        print('ABELIAN RANK',r,'ALL COMPARISON IDENTITIES PASSED',flush=True)
    cyclic_count=0
    for m in (2,3,4,5):
        C=CyclicBar(m)
        for q in range(5):
            assert C.project(C.i_basis(q))=={0:1}
            for s in product(range(1,m),repeat=q):
                chain={(0,s):1}
                assert C.dbar(C.dbar(chain))=={}
                assert C.project(C.dbar(chain))==C.period_d(q,C.project(chain))
                lhs=C.dbar(C.homotopy(chain));add(lhs,C.homotopy(C.dbar(chain)))
                rhs=dict(chain);add(rhs,C.include(q,C.project(chain)),-1)
                assert lhs==rhs
                cyclic_count+=1
        print('CYCLIC ORDER',m,'ALL COMPARISON IDENTITIES PASSED',flush=True)
    print('EXACT TEST COUNTS:',abelian_count,'abelian;',cyclic_count,'cyclic',flush=True)
