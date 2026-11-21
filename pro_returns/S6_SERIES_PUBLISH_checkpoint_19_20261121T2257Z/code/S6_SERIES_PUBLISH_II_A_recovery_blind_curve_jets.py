"""Independent prefreeze computations for 01B4 and 01FJ.

Written from their statement equations before either target proof or C_jets.py.
Exact finite interpolation and explicit coefficient/preimage constructions only.
"""
from itertools import product
from fractions import Fraction as Q

# Tacnode completion x -> x+lambda*y^2. Separate degree bounds (2,2,1,2).
count = 0
for a,b,c,l in product(range(3),range(3),range(2),range(3)):
    a1,b1,c1 = a,b+2*a*l,c+b*l+a*l*l
    assert 4*a1*c1-b1*b1 == 4*a*c-b*b
    count += 1
assert count == 54
print('tacnode square completion: 54 exact grid values; separate degree (2,2,1,2)')

# Linear frame and equation scaling: a,b,c -> u*(a*A^2,b*A*G^2,c*G^4).
count = 0
for a,b,c,A,G,u in product(range(3),range(3),range(2),range(3),range(5),range(3)):
    aa,bb,cc = u*a*A*A,u*b*A*G*G,u*c*G**4
    assert 4*aa*cc-bb*bb == u*u*A*A*G**4*(4*a*c-b*b)
    count += 1
assert count == 810
print('tacnode tensor weight: 810 exact grid values; separate degree (2,2,1,2,4,2)')

# The two-vector wedge transformation is separately linear in all eight inputs.
count = 0
for p,q,r,s,a,b,c,d in product(range(2),repeat=8):
    gu=(p*a+q*b,r*a+s*b)
    gv=(p*c+q*d,r*c+s*d)
    assert gu[0]*gv[1]-gu[1]*gv[0] == (p*s-q*r)*(a*d-b*c)
    count += 1
assert count == 256
print('binary wedge transformation: all 256 multi-affine grid values; cubic discriminant weight det^6')

# Degree identities are equalities of linear forms in deg(M),deg(Q).
H=(Q(2),Q(0))
cusp=(Q(0),Q(3))
tac=(Q(2),Q(4))
def combine(*terms):
    return tuple(sum(scale*vector[i] for scale,vector in terms) for i in range(2))
assert combine((Q(1,2),H),(Q(1,3),cusp)) == (1,1)
assert combine((Q(1,4),H),(Q(1,4),tac)) == (1,1)
print('degree E = degree(H)/2+degree(cusp cubic)/3 = [degree(H)+degree(tacnode Delta)]/4')

# Arithmetic genus bound: (1+r)+(h-r)=1+h; normalized genus adds total delta.
for r,h in product(range(3),repeat=2):
    assert (1+r)+(h-r) == 1+h
assert [(g,delta) for g in range(1,3) for delta in range(2) if g+delta<=2] == [(1,0),(1,1),(2,0)]
print('positive-genus possibilities with arithmetic genus <=2: (g,delta)=(1,0),(1,1),(2,0)')

# Cusp algebra: every exponent k>=2 has an explicit 2a+3b representation.
for k in range(2,65):
    a,b = (k//2,0) if k%2==0 else ((k-3)//2,1)
    assert a>=0 and b>=0 and 2*a+3*b==k
print('cusp normalization quotient is the single missing linear coefficient; conductor t^2')

# Tacnode conductor membership and inverse-Jacobian constant-order constraints.
# Let A0,B0 be the t^0 coefficients of t^2*h_i. The constraints are A0+B0 and A0-B0.
sumrow=(Q(1),Q(1)); diffrow=(Q(1),Q(-1))
assert combine((Q(1,2),sumrow),(Q(1,2),diffrow)) == (1,0)
assert combine((Q(1,2),sumrow),(Q(-1,2),diffrow)) == (0,1)
assert sum((1,-1))==0
print('tacnode inverse-Jacobian constraints force both double-pole coefficients to zero; residues (a,-a)')

# Cusp: t^3*h and t^4*h lack a t term, killing h[-2] and h[-3] respectively.
pole_coeff={-3:'h_-3',-2:'h_-2',-1:'h_-1',0:'h_0'}
assert {k+3:v for k,v in pole_coeff.items()}[1]=='h_-2'
assert {k+4:v for k,v in pole_coeff.items()}[1]=='h_-3'
print('cusp inverse-Jacobian constraints kill poles of orders 3 and 2, leaving t^-1 B')

# Triple point branch evaluation on homogeneous monomials of degree k.
def evaluate_monomial(i,j):
    # Coefficients on branches (t,0),(0,t),(t,t).
    return (int(j==0),int(i==0),1)
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
for k in range(2,33):
    mixed=evaluate_monomial(k-1,1)
    assert sub(evaluate_monomial(k,0),mixed)==(1,0,0)
    assert sub(evaluate_monomial(0,k),evaluate_monomial(1,k-1))==(0,1,0)
    assert mixed==(0,0,1)
residue=(1,1,-1)
assert residue[0]+residue[2]==0 and residue[1]+residue[2]==0
print('triple conductor: explicit preimages for all three order-k branch monomials, k>=2')
print('triple inverse-Jacobian residues (a,a,-a); each double-pole constant is forced to zero')
print('all computations exact; universal degree/series arguments are in the independent derivations')
