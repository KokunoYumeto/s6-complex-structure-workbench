"""BY: open-pair ranks, contact partitions and exact character cohomology.

Geometric inputs and all unbounded assertions are proved in the frozen
derivation. This does not certify that an abstract row occurs geometrically.
"""
import itertools
import json
import sympy as s

c,g,nu,lam,B1=s.symbols('c g nu lambda B1',integer=True)
e_branch=2*c-2*g-nu
e_open=3*(4-e_branch)
boundary_h1=2*g+nu-c+1+lam
relations=c-2
pair=s.expand(e_open-1+2*B1-boundary_h1+relations)
assert s.expand(pair-(8-4*c+4*g+2*nu-lam+2*B1))==0
rows=[]
for nu0 in range(1,6):
    for lam0 in (0,1,2):
        for q in (0,1):
            rank=int(pair.subs({c:2,g:0,nu:nu0,lam:lam0,B1:2*q}))
            if rank==0:
                rows.append(dict(nu=nu0,link_b1=lam0,q=q))
assert rows==[dict(nu=1,link_b1=2,q=0)]
# All omitted nu>=6 have rank>=2*nu-2>0 by this symbolic difference.
n=s.symbols('n',integer=True,positive=True)
assert s.expand(pair.subs({c:2,g:0,nu:n,lam:2,B1:0})-(2*n-2))==0

partitions=[(1,1,1),(2,1),(3,)]
contact_rows=[]
survivors=[]
for a,b in itertools.product(partitions,repeat=2):
    t=int(a==(3,))+int(b==(3,))
    q=max(t-1,0)
    branches=len(a)+len(b)
    rank=int(pair.subs({c:3,g:0,nu:branches,lam:2*t,B1:2*q}))
    row=dict(partitions=[a,b],pg_sum=t,q=q,nu=branches,
             first_betti=2*q+1,pair_rank=rank,attachment_excess=branches-2)
    contact_rows.append(row)
    assert row['first_betti']<=3
    if rank==0:
        survivors.append(row)
assert [(x['partitions'],x['attachment_excess']) for x in survivors]==[
    ([(2,1),(3,)],1), ([(3,),(2,1)],1), ([(3,),(3,)],0)]

def line_cohomology(k):
    return max(k+1,0),max(-k-1,0)
def product_cohomology(a,b):
    a0,a1=line_cohomology(a);b0,b1=line_cohomology(b)
    return [a0*b0,a1*b0+a0*b1,a1*b1]
reduced_chars=[(0,0),(-1,-1),(-2,-2)]
double_chars=[(0,0),(-1,-1),(-1,-2)]
reduced_h=[product_cohomology(*x) for x in reduced_chars]
double_h=[product_cohomology(*x) for x in double_chars]
assert reduced_h==[[1,0,0],[0,0,0],[0,0,1]]
assert double_h==[[1,0,0],[0,0,0],[0,0,0]]

# E-exponents: -L'=-sigma*L+E and -2L'+F'=-2sigma*L+sigma*F+E.
root_E=-1
double_component_E=-1
assert -root_E==1 and -2*root_E+double_component_E==1
assert line_cohomology(-1)==(0,0)
double_rows=[]
for p in partitions:
    count=len(p)
    rank=int(pair.subs({c:2,g:0,nu:count,lam:0,B1:0}))
    exceptional_components=sum(1+3*(k-1) for k in p)
    double_rows.append(dict(contact_partition=p,nu=count,first_betti=0,
                            pair_rank=rank,exceptional_tree_components=exceptional_components))
    assert rank==2*count>0

# Bidegree intersection and arithmetic genus, independent of a splitting-coordinate formula.
def intersection(D,E):return D[0]*E[1]+D[1]*E[0]
L=(1,1);F=(1,0);K=(-2,-2)
root_rows=[]
for v in (1,2):
    R=(3-v,3)
    pa=1+(intersection(R,R)+intersection(R,K))//2
    assert pa==4-2*v and intersection(R,F)==3
    root_rows.append(dict(v=v,R=R,pa=pa,intersection_with_fibre=3))

# Hodge class map: pullback of base intersection multiplies by3.
base=s.Matrix([[0,1],[1,0]])
pullback=3*base
assert pullback.det()==-9 and (s.Matrix([[1,1]])*pullback*s.Matrix([1,1]))[0]==6

print(json.dumps(dict(status='PASS',method='Open-pair Euler/Gysin ranks; complete contact-partition enumeration; Kunneth character cohomology; blowup exponent transport',
    general_pair_rank=str(pair),one_simple_zero_solutions=rows,
    two_simple_zero_cases=contact_rows,two_simple_zero_survivors=survivors,
    reduced_character_cohomology=reduced_h,double_character_cohomology=double_h,
    blowup_character_exceptional_exponents=[1,1],double_zero_cases=double_rows,
    root_bidegrees=root_rows,base_pullback_matrix=[[int(x) for x in row] for row in pullback.tolist()],
    scope='Exact arithmetic of the pre-target derivation; no existence claim or independent check group beyond BY'),indent=2))
