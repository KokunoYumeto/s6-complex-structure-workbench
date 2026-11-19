#!/usr/bin/env python3
"""Independent finite check of the complete Q03 hierarchy construction.

Uses exact finite search to choose normalized schedules. It then constructs the
lists, runs, cutoff extensions, switches, separator walks, global formulas and
relative formulas directly from their definitions. It checks I1, I2, and every
possible full replacement schedule in I3 for each nonroot node. The latter
enumeration is exact, not a random selection of replacements. Finite results do
not substitute for the accompanying arbitrary-size proof audit.

Run: python3 code/B_hierarchy_check.py > code/B_hierarchy_check_output.json
No third-party package is needed. Cases and a pseudorandom seed are printed.
"""
from dataclasses import dataclass, replace
from functools import lru_cache
from itertools import combinations
from collections import Counter
from random import Random
import json
import sys


def bits(x):
    while x:
        b=x&-x
        yield b.bit_length()-1
        x-=b

@dataclass(frozen=True)
class Formula:
    mask:int
    leaves:int=1
    def meet(self,other):return Formula(self.mask&other.mask,self.leaves+other.leaves)
    def join(self,other):return Formula(self.mask|other.mask,self.leaves+other.leaves)
    def comp(self,allmask):return Formula(allmask^self.mask,self.leaves)

@dataclass(frozen=True)
class Entry:
    base:Formula
    suffix:object
    kind:str
    ident:int

@dataclass(frozen=True)
class Boundary:
    mask:int
    virtual:int=0  # -1 = original before, +1 = original after, 0 = real

class Checker:
    def __init__(self,m,n,arcs,counters):
        self.m,self.n,self.all=m,n,(1<<n)-1
        self.arcs=arcs
        self.c=counters
        p=[0]*n
        for u,v in arcs:
            assert u<v
            p[v]|=1<<u
        for v in range(n):
            for u in list(bits(p[v])):p[v]|=p[u]
        s=[0]*n
        for v in range(n):
            for u in bits(p[v]):s[u]|=1<<v
        self.pred={1:p,-1:s}
        self.succ={1:s,-1:p}
        self.serial=0
        self.history=[]

    def rank(self,x,f):return x+1 if f==1 else self.n-x
    def threshold(self,r,f,lower=True):
        return Formula(sum(1<<x for x in range(self.n)
                           if (self.rank(x,f)>=r if lower else self.rank(x,f)<=r)))
    def val(self,e,f):
        return e.base.mask if e.suffix is None else e.base.mask&self.threshold(e.suffix,f).mask
    def formula(self,e,f):
        return e.base if e.suffix is None else e.base.meet(self.threshold(e.suffix,f))
    def create(self,base,kind,suffix=None):
        self.serial+=1
        return Entry(base,suffix,kind,self.serial)
    def trim(self,e,r):return replace(e,suffix=r if e.suffix is None else max(r,e.suffix))
    def qual(self,entries,f):
        out=0
        for e in entries:out|=self.val(e,f)
        return out
    def unionformula(self,entries,f):
        if not entries:return Formula(0)
        z=self.formula(entries[0],f)
        for e in entries[1:]:z=z.join(self.formula(e,f))
        return z
    def key(self,x,entries,f):
        ids=[i for i,e in enumerate(entries) if self.val(e,f)>>x&1]
        assert ids
        return max(ids),self.rank(x,f)
    def cone(self,b,f,which,weak=False):
        if b.virtual:
            isbefore=(b.virtual*f==-1)
            return Formula(self.all if (isbefore==(which=='D')) else 0)
        out=0
        for x in bits(b.mask):
            out|=self.succ[f][x] if which=='D' else self.pred[f][x]
        return Formula(out|b.mask if weak else out)
    def upset(self,mask,f):
        return all(not(self.succ[f][x]&~mask) for x in bits(mask))
    def downset(self,mask,f):return self.upset(mask,-f)
    def feasible(self,sched,domain=None,f=1):
        domain=self.all if domain is None else domain
        done=0
        for slot in sched:
            if slot.bit_count()!=self.m or done&slot:return False
            if any(self.pred[f][x]&domain&~done for x in bits(slot)):return False
            done|=slot
        return done==domain
    def schedules(self,domain,f,priority):
        # All full schedules in lexicographic slot-priority order.
        index={x:i for i,x in enumerate(priority)}
        def rec(rem):
            if not rem:
                yield ()
                return
            avail=[x for x in priority if (rem>>x&1) and not(self.pred[f][x]&rem)]
            for comb in combinations(avail,self.m):
                slot=sum(1<<x for x in comb)
                for tail in rec(rem^slot):yield (slot,)+tail
        return rec(domain)
    def normalized(self,domain,f,priority):
        @lru_cache(None)
        def rec(rem):
            if not rem:return ()
            avail=[x for x in priority if rem>>x&1 and not(self.pred[f][x]&rem)]
            for comb in combinations(avail,self.m):
                slot=sum(1<<x for x in comb)
                tail=rec(rem^slot)
                if tail is not None:return (slot,)+tail
            return None
        ans=rec(domain)
        self.c['normalizations']+=1
        assert ans is not None
        return ans
    def separator(self,slotidx,S,work,f):
        before=0
        after=0
        for x in work[:slotidx]:before|=x
        for x in work[slotidx+1:]:after|=x
        b=Boundary(work[slotidx])
        return not((before&~S)&~self.cone(b,f,'P').mask) and not((after&S)&~self.cone(b,f,'D').mask)
    def carry(self,entries,O,S,f):
        rem=O&~S
        if not rem:return []
        x=min(bits(rem),key=lambda x:self.key(x,entries,f))
        d,r=self.key(x,entries,f)
        return [self.trim(entries[d],r)]+entries[d+1:]
    def check_invariants(self,sched,l,r,f,entries):
        W=0
        for sl in sched[l:r]:W|=sl
        orig_a=Boundary(sched[l-1]) if l else Boundary(0,-1)
        orig_b=Boundary(sched[r]) if r<len(sched) else Boundary(0,1)
        a,b=(orig_a,orig_b) if f==1 else (orig_b,orig_a)
        D=self.cone(a,f,'D').mask
        P=self.cone(b,f,'P').mask
        Q=self.qual(entries,f)
        assert all(self.upset(self.val(e,f),f) for e in entries)
        assert not((W&Q)&~P) and not((W&~Q)&~D),('I1',self.history)
        atbefore=(sched[:l] if f==1 else sched[r:])
        ext=0
        for sl in atbefore:ext|=sl
        assert not((ext&Q)&~self.cone(a,f,'P',True).mask),('I2',self.history)
        self.c['I1_checks']+=1
        self.c['I2_checks']+=1
        self.c['I2_qualifiers_at_boundary']+=(a.mask&Q).bit_count()
        self.c['I2_qualifiers_strictly_before_boundary']+=(ext&~a.mask&Q).bit_count()
        self.c['max_pruned_entries']=max(self.c['max_pruned_entries'],len(entries))
        self.c['max_injections']=max(self.c['max_injections'],sum(e.kind=='injection' for e in entries))
        assert len(entries)<=self.m+2
        assert sum(e.kind=='injection' for e in entries)<=self.m
        assert all(self.formula(e,f).leaves<=3*self.m+7 for e in entries)
        assert self.unionformula(entries,f).leaves<=6*self.m+9
        if a.virtual:return
        pairs=[(x,y) for x in bits(W&~D) for y in bits(a.mask&Q)
               if self.key(x,entries,f)<self.key(y,entries,f)]
        self.c['I3_nonvacuous_pairs']+=len(pairs)
        if not pairs:return
        for new in self.schedules(W,1,tuple(bits(W))):
            self.c['I3_full_replacements']+=1
            trial=list(sched)
            trial[l:r]=new
            for x,y in pairs:
                changed=list(trial)
                ix=next(i for i,sl in enumerate(changed) if sl>>x&1)
                iy=next(i for i,sl in enumerate(changed) if sl>>y&1)
                changed[ix]^=(1<<x)|(1<<y)
                changed[iy]^=(1<<x)|(1<<y)
                self.c['I3_exchange_checks']+=1
                assert not self.feasible(changed),('I3',self.history,x,y)
    def short_extension(self,U,a,b,f,entries,O,S,same,car,run):
        if not same:
            r=max([self.rank(x,f) for x in bits(S)]+[0])
            H=self.cone(a,f,'D').comp(self.all).meet(self.threshold(r,f,False))
        else:
            initial=[e for e in car if e.kind!='injection']
            inject=[self.formula(e,f) for e in car if e.kind=='injection']
            if run['type']=='root':
                init=[self.threshold(e.suffix,f) if e.suffix is not None else Formula(self.all) for e in initial]
            else:
                first=next((e for e in initial if e.kind=='first'),None)
                if first:
                    init=[run['second_base'].join(self.threshold(first.suffix,f))]
                    original=0
                    for e in initial:original|=self.val(e,f)
                    assert U&original==U&init[0].mask,('6.1',self.history)
                    self.c['flattenings']+=1
                else:init=[self.formula(e,f) for e in initial]
            fs=inject+init
            Phi=Formula(0) if not fs else fs[0]
            for ff in fs[1:]:Phi=Phi.join(ff)
            assert Phi.leaves<=3*self.m+2
            assert U&Phi.mask==U&self.qual(car,f)
            H=self.cone(b,f,'P').meet(Phi.comp(self.all))
        assert H.leaves<=3*self.m+3
        assert U&H.mask==S and self.downset(H.mask,f),('6.2',self.history)
        self.c['low_extensions']+=1
        return H
    def node(self,sched,l,r,f,entries,oldedge,run,depth=0):
        self.c['nodes']+=1
        self.c['max_depth']=max(self.c['max_depth'],depth)
        self.history.append((l,r,f))
        W=0
        for sl in sched[l:r]:W|=sl
        assert W and self.feasible(sched)
        self.check_invariants(sched,l,r,f,entries)
        oa=Boundary(sched[l-1]) if l else Boundary(0,-1)
        ob=Boundary(sched[r]) if r<len(sched) else Boundary(0,1)
        a,b=(oa,ob) if f==1 else (ob,oa)
        if oldedge is None:
            center=r-1
        else:
            C=W&self.cone(b,f,'P').mask
            priority=tuple(sorted(bits(C),key=lambda x:self.rank(x,f))+sorted(bits(W&~C),key=lambda x:self.rank(x,f)))
            norm=self.normalized(W,f,priority)
            work=norm
            ci=next(i for i in range(len(work)) if self.separator(i,C,work,f))
            # Any separator suffices; use the first and record the actual resulting witness.
            sched=list(sched)
            sched[l:r]=work if f==1 else work[::-1]
            center=l+ci if f==1 else r-1-ci
        v=Boundary(sched[center])
        center_original=center
        self.c['centers']+=1
        # Normalize each open side in its working frame. Sides have disjoint jobs.
        for same in (True,False):
            g=f if same else -f
            aa,bb=(oa,ob) if g==1 else (ob,oa)
            el,er=(l,center) if g==1 else (center+1,r)
            E=0
            for sl in sched[el:er]:E|=sl
            O=W&self.qual(entries,f)
            if same:
                S0=(W&~O)&self.cone(bb,g,'P').mask
                promotions=sorted(bits(O),key=lambda x:self.key(x,entries,g))
                Y=W&~self.cone(bb,g,'P').mask
                priority=sorted(bits(S0),key=lambda x:self.rank(x,g))+promotions+sorted(bits(Y),key=lambda x:self.rank(x,g))
            else:
                S0=0
                X=W&~self.cone(aa,g,'D').mask
                promotions=sorted(bits(X),key=lambda x:self.rank(x,g))
                priority=promotions+sorted(bits(W&~X),key=lambda x:self.rank(x,g))
            assert len(priority)==W.bit_count() and len(set(priority))==len(priority)
            norms=self.normalized(E,g,tuple(x for x in priority if E>>x&1))
            sched=list(sched)
            sched[el:er]=norms if g==1 else norms[::-1]
        # Both normalized sides now live in this one parent witness.
        for same in (True,False):
            g=f if same else -f
            aa,bb=(oa,ob) if g==1 else (ob,oa)
            el,er=(l,center) if g==1 else (center+1,r)
            E=0
            for sl in sched[el:er]:E|=sl
            work=list(sched[el:er]) if g==1 else list(sched[el:er][::-1])
            O=W&self.qual(entries,f)
            if same:
                S0=(W&~O)&self.cone(bb,g,'P').mask
                promotions=sorted(bits(O),key=lambda x:self.key(x,entries,g))
                Sstar=W&self.cone(bb,g,'P').mask
            else:
                S0=0
                X=W&~self.cone(aa,g,'D').mask
                promotions=sorted(bits(X),key=lambda x:self.rank(x,g))
                Sstar=X
            cuts=[S0]
            positions=[-1]
            pos=-1
            S=S0
            for x in promotions:
                S|=1<<x
                while True:
                    bound=aa if pos==-1 else Boundary(work[pos])
                    exceptions=[j for j in range(pos+1,len(work)) if work[j]&S&~self.cone(bound,g,'D').mask]
                    if not exceptions:break
                    pos=exceptions[0]
                    self.c['walk_advances']+=1
                cuts.append(S)
                positions.append(pos)
            assert S==Sstar
            positions.append(len(work))
            Hstar_center=self.cone(bb,g,'P') if same else self.cone(aa,g,'D').comp(self.all)
            Fv=self.cone(v,g,'P').join(Hstar_center.meet(self.cone(v,g,'D',True).comp(self.all)))
            assert W&Fv.mask==E
            self.c['center_formula_checks']+=1
            for i,S in enumerate(cuts):
                car=self.carry(entries,O,S,g) if same else []
                if same:
                    tilde=self.cone(bb,g,'P').meet(self.unionformula(car,g).comp(self.all))
                else:
                    rr=max([self.rank(x,g) for x in bits(S)]+[0])
                    tilde=self.cone(aa,g,'D').comp(self.all).meet(self.threshold(rr,g,False))
                assert W&tilde.mask==S
                assert tilde.leaves<=6*self.m+10
                self.c['cutoff_predicate_checks']+=1
                p,q=positions[i:i+2]
                if p>=0:
                    z=Boundary(work[p])
                    Fz=Fv.meet(self.cone(z,g,'P').join(tilde.meet(self.cone(z,g,'D',True).comp(self.all))))
                    before=0
                    for sl in work[:p]:before|=sl
                    assert W&Fz.mask==before
                    original=Fz if g==1 else Fz.comp(self.all).meet(Formula(self.all^z.mask))
                    oi=next(j for j,sl in enumerate(sched) if sl==z.mask)
                    actual=0
                    for sl in sched[l:oi]:actual|=sl
                    assert W&original.mask==actual
                    assert original.leaves<=6*self.m+16
                    self.c['relative_formula_checks']+=1
                if q-p<=1:continue
                childmask=0
                for sl in work[p+1:q]:childmask|=sl
                ap=aa if p==-1 else Boundary(work[p])
                bp=v if q==len(work) else Boundary(work[q])
                assert not((childmask&S)&~(self.cone(ap,g,'D').mask&self.cone(bb,g,'P').mask))
                assert not((childmask&~S)&~self.cone(bp,g,'P').mask)
                Hext=self.short_extension(W,aa,bb,g,entries,O,S,same,car,run)
                if same:
                    injection=self.cone(aa,g,'D').meet(self.cone(bb,g,'P').comp(self.all))
                    pre=car+[self.create(injection,'injection')]
                    childrun=run
                else:
                    assert oldedge is not None
                    a_minus=oldedge['b']
                    v_minus=oldedge['v']
                    G=self.cone(a_minus,g,'D').meet(self.cone(aa,g,'P',True).comp(self.all)).meet(self.cone(v_minus,g,'P',True).comp(self.all)).meet(oldedge['Hext'])
                    assert self.upset(G.mask,g)
                    assert not(X&~G.mask)
                    external=0
                    for sl in (sched[:l] if g==1 else sched[r:]):external|=sl
                    assert not(G.mask&external)
                    h=min([self.rank(x,g) for x in bits(X&~S)]+[self.n+1])
                    second=self.cone(aa,g,'D')
                    pre=[self.create(G,'first',h),self.create(second,'second')]
                    childrun={'type':'switched','second_base':second}
                    self.c['switches']+=1
                assert W&self.qual(pre,g)==W&~S
                kept=[e for e in pre if self.val(e,g)&childmask]
                assert childmask&self.qual(kept,g)==childmask&~S
                injections=[e for e in kept if e.kind=='injection']
                witnesses=[]
                for k,e in enumerate(injections):
                    for ee in injections[k+1:]:assert not(W&self.val(e,g)&self.val(ee,g))
                    x=min(bits(childmask&self.val(e,g)),key=lambda x:self.rank(x,g))
                    ys=[y for y in bits(bp.mask) if self.succ[g][x]>>y&1]
                    assert ys
                    y=min(ys,key=lambda y:self.rank(y,g))
                    assert self.val(e,g)>>y&1
                    witnesses.append(y)
                assert len(set(witnesses))==len(witnesses)<=self.m
                self.c['capacity_witness_checks']+=1
                high=self.unionformula(kept,g).meet(self.cone(bp,g,'P')).meet(self.cone(ap,g,'P',True).comp(self.all))
                low=self.cone(ap,g,'D').meet(self.cone(bb,g,'P')).meet(self.cone(bp,g,'D',True).comp(self.all)).meet(self.cone(v,g,'D',True).comp(self.all)).meet(tilde)
                assert high.mask==childmask&~S,('8.4',self.history)
                assert low.mask==childmask&S,('8.5',self.history)
                whole=high.join(low)
                assert whole.mask==childmask and whole.leaves<=12*self.m+25
                self.c['global_formula_checks']+=1
                self.c['max_global_formula_leaves']=max(self.c['max_global_formula_leaves'],whole.leaves)
                slots=work[p+1:q]
                origindices=[j for j,sl in enumerate(sched) if sl in slots]
                cl,cr=min(origindices),max(origindices)+1
                assert cr-cl==len(slots)
                edge={'a':aa,'b':bb,'v':v,'Hext':Hext,'parent':W}
                self.node(list(sched),cl,cr,g,kept,edge,childrun,depth+1)
        self.history.pop()

    def run(self):
        priority=tuple(range(self.n))
        norm=self.normalized(self.all,1,priority)
        self.node(list(norm),0,len(norm),1,[self.create(Formula(self.all),'root')],None,{'type':'root'})
        self.c['instances']+=1


def main():
    seed=20261115
    rng=Random(seed)
    c=Counter({'flattenings':0, 'I2_qualifiers_at_boundary':0, 'I2_qualifiers_strictly_before_boundary':0})
    records=[]
    # Fixed feasible layers: arcs are independently chosen only between
    # distinct layers; the original layer schedule proves initial feasibility.
    specs=[(3,3,30),(3,4,50),(3,5,30),(3,6,20),
           (4,3,30),(4,4,40),(4,5,20),(5,3,20),(5,4,15)]
    for m,slots,count in specs:
        for j in range(count):
            density=(0.06,0.12,0.2,0.35,0.55)[j%5]
            n=m*slots
            arcs=[(u,v) for u in range(n) for v in range(u+1,n)
                  if u//m<v//m and rng.random()<density]
            before=dict(c)
            checker=Checker(m,n,arcs,c)
            try:checker.run()
            except Exception:
                print(json.dumps({'failed_case':{'m':m,'n':n,'arcs':arcs},'counts':dict(c)},indent=2))
                raise
            if c['switches']>before.get('switches',0) or c['flattenings']>before.get('flattenings',0) or c['I3_nonvacuous_pairs']>before.get('I3_nonvacuous_pairs',0):
                records.append({'m':m,'n':n,'arcs':arcs,
                                'switches':c['switches']-before.get('switches',0),
                                'flattenings':c['flattenings']-before.get('flattenings',0),
                                'I3_pairs':c['I3_nonvacuous_pairs']-before.get('I3_nonvacuous_pairs',0)})
    print(json.dumps({'date':'2026-11-15','seed':seed,
                      'coverage':'Seeded layered feasible DAGs; exact normalization and all replacements for every tested I3 pair; no exhaustiveness claim for all DAGs.',
                      'case_specifications':[{'m':m,'slots':s,'cases':k} for m,s,k in specs],
                      'counts':dict(sorted(c.items())),
                      'cases_exercising_switch_flatten_or_I3':records,
                      'verdict':'All asserted checks passed.'},indent=2))

if __name__=='__main__':main()
