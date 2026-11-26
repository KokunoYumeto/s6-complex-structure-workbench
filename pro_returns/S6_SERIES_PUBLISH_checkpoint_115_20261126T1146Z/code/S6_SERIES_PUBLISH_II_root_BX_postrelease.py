"""Compare the printed double-cover ranks via closed-cover Euler strata.

The input is the geometric stratification and exceptional intersection rank
proved in the comparison record. This arithmetic computes b2 of the resolved
closed surface first, then subtracts the boundary span. It separately checks
the printed open-pair formula, including disconnected branch support.
"""
import json
import sympy as s

c,g,nu,n,lam,B1,r,b0=s.symbols('c g nu n lambda B1 r b0',integer=True)
e_base=4
e_branch=2*c-2*g-nu
e_closed_singular=3*(e_base-e_branch)+e_branch
e_closed_resolved=e_closed_singular+n-lam
b2_closed=e_closed_resolved-2+2*B1
boundary_rank=n+r
closed_pair_rank=s.expand(b2_closed-boundary_rank)
e_open=3*(e_base-e_branch)
boundary_b1=2*g+nu-c+b0+lam
relations=c-r
open_pair_rank=s.expand(e_open+b0-2+2*B1-boundary_b1+relations)
assert s.expand(closed_pair_rank-open_pair_rank)==0
expected=10-4*c+4*g+2*nu-lam+2*B1-r
assert s.expand(closed_pair_rank-expected)==0
assert not closed_pair_rank.has(n,b0)

checks=[]
def record(name,actual,expected_value):
    assert s.expand(actual-expected_value)==0,(name,actual,expected_value)
    checks.append(dict(name=name,value=str(s.expand(actual))))

record('v0 lower rank',closed_pair_rank.subs({c:2,lam:2,B1:0}),4*g+2*nu-r)
record('v1 lower rank',closed_pair_rank.subs({c:3,r:2,lam:2,B1:0}),4*g+2*nu-6)
record('two simple zeros Euler',e_open.subs({c:4,g:1}),3*nu-6)
record('two simple zeros boundary b1',boundary_b1.subs({c:4,g:1,b0:1,lam:0}),nu-1)
record('two simple zeros pairing',closed_pair_rank.subs({c:4,g:1,r:2,lam:0,B1:0}),2*nu-4)
record('double zero Euler',e_open.subs({c:3,g:1}),3*nu)
record('double zero boundary b1',boundary_b1.subs({c:3,g:1,b0:1,lam:0}),nu)
record('double zero pairing',closed_pair_rank.subs({c:3,g:1,r:2,lam:0,B1:0}),2*nu)

# Every unbounded positive-genus/branch-count variable enters with a positive
# coefficient. Evaluating the minimum endpoint proves these printed bounds.
minima={
 'v0_rank':int((4*g+2*nu-r).subs({g:1,nu:0,r:2})),
 'v1_rank':int((4*g+2*nu-6).subs({g:1,nu:2})),
 'two_simple_rank':min(2*k-4 for k in (4,5,6)),
 'double_rank':min(2*k for k in (2,3)),
}
assert minima==dict(v0_rank=2,v1_rank=2,two_simple_rank=4,double_rank=4)
first_betti=dict(v0=max(2+2-k for k in (1,2)),v1=2+3-2,two_simple=0+4-2,double=0+3-2)
assert first_betti==dict(v0=3,v1=3,two_simple=2,double=1)

# The line-subbundle coordinate change to the printed two splitting charts.
ell,v,a,d=s.symbols('ell v a d',integer=True)
pa=3+ell-v
meet=2-ell-v
record('balanced arithmetic genus under ell=-1-d',pa.subs(ell,-1-d),2-v-d)
record('unbalanced intersection under ell=a',meet.subs(ell,a),2-a-v)
root_square=-2-2*ell
record('root section square in trivial summand',root_square.subs(ell,0),-2)

print(json.dumps(dict(status='PASS',method='Closed-cover Euler strata and resolved b2, compared symbolically with the printed open-pair sequence',general_closed_pair_rank=str(closed_pair_rank),open_pair_identity=True,disconnected_b0_cancels=True,checks=checks,rank_minima=minima,first_betti_maxima=first_betti,scope='Postrelease comparison of the original stronger formulas; no additional independent evidence group and no proof of geometric existence from code'),indent=2))
