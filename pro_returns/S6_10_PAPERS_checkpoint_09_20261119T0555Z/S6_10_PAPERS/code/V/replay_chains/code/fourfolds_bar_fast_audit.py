"""Exact comparison with the original unsimplified recursive contractions.

The finite sample is every declared abelian/cyclic simplex used by the
original281/498 verification program, including both complete universal
group-ring projections and complete universal homotopy chains.
"""
from functools import lru_cache
from itertools import product
from fourfolds_bar_koszul import AbelianBar,CyclicBar,add

class ReferenceAbelian(AbelianBar):
    @lru_cache(None)
    def p_basis(self,s):
        if not s:return {(self.zero,()):1}
        if len(s)>self.rank:return {}
        return self.skoszul(self.project(self.dbar({(self.zero,s):1})))
    @lru_cache(None)
    def h_basis(self,s):
        if not s:return {}
        z={(self.zero,s):1}
        add(z,self.include(self.p_basis(s)),-1)
        add(z,self.homotopy(self.dbar({(self.zero,s):1})),-1)
        return self.sbar(z)

class ReferenceCyclic(CyclicBar):
    @lru_cache(None)
    def p_basis(self,s):
        if not s:return {0:1}
        return self.period_s(len(s)-1,self.project(self.dbar({(0,s):1})))
    @lru_cache(None)
    def h_basis(self,s):
        if not s:return {}
        z={(0,s):1}
        add(z,self.include(len(s),self.p_basis(s)),-1)
        add(z,self.homotopy(self.dbar({(0,s):1})),-1)
        return self.sbar(z)

count=0
for r in (1,2,3):
    fast=AbelianBar(r);old=ReferenceAbelian(r)
    alphabet=fast.units+(tuple(-1 for _ in range(r)),tuple(2 for _ in range(r)))
    for n in range(4):
        for s in product(alphabet,repeat=n):
            assert fast.p_basis(s)==old.p_basis(s)
            assert fast.h_basis(s)==old.h_basis(s)
            count+=1
print('COMPLETE UNIVERSAL ABELIAN MAPS IDENTICAL ON',count,'DECLARED SIMPLICES')
count=0
for m in (2,3,4,5):
    fast=CyclicBar(m);old=ReferenceCyclic(m)
    for n in range(5):
        for s in product(range(1,m),repeat=n):
            assert fast.p_basis(s)==old.p_basis(s)
            assert fast.h_basis(s)==old.h_basis(s)
            count+=1
print('COMPLETE UNIVERSAL CYCLIC MAPS IDENTICAL ON',count,'DECLARED SIMPLICES')
