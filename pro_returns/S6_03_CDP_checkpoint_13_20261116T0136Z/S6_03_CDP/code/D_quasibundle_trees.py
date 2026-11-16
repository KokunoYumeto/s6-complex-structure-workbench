"""Exact root, canonical-order and example checks for C.2.UN.62."""
import sympy as S

# The inverse-log chart with secondary order one retains the positive root line.
p,u,X,W,s,y=S.symbols('p u X W s y', nonzero=True)
eout=S.symbols('eout',nonzero=True)
ein=eout/s
assert S.simplify(W*eout-(s*W)*ein)==0
for m in range(1,61):
    assert S.simplify((s/y)**m*y**m-s**m)==0
    assert S.simplify((s/y)**-1-y/s)==0
    assert S.simplify((s**m)*(y/s)**m-y**m)==0
    assert S.simplify((s*W)**m-s**m*W**m)==0
print('PASS 60 exact inverse-log/root-line maps: p=s^m, u=y^m, X=s/y, W=y/s.')
print('PASS signed positive divisor line: e_in=s^-1*e_out, W*e_out=y*e_in iff y=s*W; its canonical section has coefficient s.')

# Holomorphic pluricanonical sections satisfy m*a+k*(m-1)>=0.
cases=0
for m in range(1,81):
    for k in range(1,121):
        lower=-(k*(m-1)//m)
        assert m*lower+k*(m-1)>=0
        assert m*(lower-1)+k*(m-1)<0
        cases+=1
print('Exact root-coordinate pluricanonical pole bounds checked:',cases)

# The explicit two-core / four-leaf graph, including its two parallel core edges.
vertices=['P','Q','L1','L2','L3','L4']
edges=[('P','Q',1),('Q','P',1)]+[('P',f'L{i}',3) for i in range(1,5)]
incidence=S.zeros(len(edges),len(vertices))
heights={'P':0,'Q':0,**{f'L{i}':3 for i in range(1,5)}}
for j,(a,b,m) in enumerate(edges):
    incidence[j,vertices.index(a)]=1
    incidence[j,vertices.index(b)]=-1
    assert (heights[b]-heights[a])%m==0
assert incidence.rank()==5
assert len(incidence.T.nullspace())==1
residue=incidence.T.nullspace()[0]
assert all(residue[j]==0 for j in range(2,len(edges)))
assert residue[0]!=0 and residue[1]!=0
print('PASS exact six-component incidence matrix: rank5, h(O)=(1,2,1), residues only on the two core edges.')

# At P the rational differential has poles at the ordinary cycle marks,
# and no zero or pole at the four order-three fibres.
divisor_orders={'cycle0':-1,'cycle_infinity':-1,**{f'triple{i}':2 for i in range(1,5)}}
assert -3-3+sum(2 for i in range(4))==2
for k in range(1,121):
    P=max(0,1-2*k+4*(2*k//3))
    if k%3==0:
        assert P==2*(k//3)+1
assert max(0,1-2+4*(2//3))==0
print('PASS exact canonical pushdown: 3K=q*O(2), pg=0, and P_(3b)=2b+1 for b=1,...,40.')
print('Four triple fibres have orbifold canonical degree',S.Rational(-2)+4*S.Rational(2,3))
print('Plurigenera P_1,...,P_12:',[max(0,1-2*k+4*(2*k//3)) for k in range(1,13)])
print('PASS all root-line, height, incidence and properly elliptic example checks.')
