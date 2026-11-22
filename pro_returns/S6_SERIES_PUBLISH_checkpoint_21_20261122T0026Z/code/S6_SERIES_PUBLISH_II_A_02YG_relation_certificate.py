"""02YG prerelease formal relation-matrix and graph-Euler certificates.

Matrices are transformed by explicit mutually inverse matrices over the
Laurent polynomial ring Z[a_ij,lambda_i,m,m^-1].  No sampled monodromy or
pre-existing target routine is used.
"""
import json
from itertools import permutations

N=21
ZERO={}
ONE={(0,)*N:1}


def plus(a,b):
    c=dict(a)
    for e,v in b.items():
        c[e]=c.get(e,0)+v
        if c[e]==0:del c[e]
    return c


def neg(a):return {e:-v for e,v in a.items()}


def times(a,b):
    c={}
    for e,v in a.items():
        for f,w in b.items():
            p=tuple(i+j for i,j in zip(e,f))
            c[p]=c.get(p,0)+v*w
    return {e:v for e,v in c.items() if v}


def variable(i,power=1):
    e=[0]*N;e[i]=power;return {tuple(e):1}


def identity(n):return [[dict(ONE) if i==j else {} for j in range(n)] for i in range(n)]


def matmul(A,B):
    out=[]
    for row in A:
        new=[]
        for j in range(len(B[0])):
            p={}
            for k,a in enumerate(row):p=plus(p,times(a,B[k][j]))
            new.append(p)
        out.append(new)
    return out


def residual(A,B):return [[plus(a,neg(b)) for a,b in zip(x,y)] for x,y in zip(A,B)]


def term_count(A):return sum(len(p) for row in A for p in row)


def det_by_permutations(A):
    total={}
    for p in permutations(range(len(A))):
        inversions=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
        term=dict(ONE)
        for i,j in enumerate(p):term=times(term,A[i][j])
        total=plus(total,neg(term) if inversions%2 else term)
    return total


A=[[variable(4*i+j) for j in range(4)] for i in range(4)]
D=[[plus(A[i][j],neg(ONE) if i==j else {}) for j in range(4)] for i in range(4)]
lam=[variable(16+i) for i in range(4)]
m=variable(20);mi=variable(20,-1)
M=[D[i]+[lam[i]] for i in range(4)]+[[{}, {}, {}, {}, m]]
U=identity(5);V=identity(5)
for i in range(4):U[i][4]=neg(times(lam[i],mi));V[i][4]=lam[i]
U[4][4]=mi;V[4][4]=m
target=[D[i]+[{}] for i in range(4)]+[[{}, {}, {}, {}, ONE]]
checks={
    'U_times_M_minus_diag_D_1':residual(matmul(U,M),target),
    'U_times_V_minus_identity':residual(matmul(U,V),identity(5)),
    'V_times_U_minus_identity':residual(matmul(V,U),identity(5)),
}
for value in checks.values():assert term_count(value)==0

detD=det_by_permutations(D)
minusD=[[neg(x) for x in row] for row in D]
detMinusD=det_by_permutations(minusD)
detDifference=plus(detD,neg(detMinusD));assert not detDifference

# Euler numbers of the graph of spheres: vertices v+p, edges E,
# two-cells v.  A tree has E=v+p-1.
graph_cells_euler={'v':2,'p':1,'E':-1}
tree_substitution={'v':1,'p':1,'one':-1}
after={'v':2,'p':1}
for key,value in tree_substitution.items():after[key]=after.get(key,0)-value
after={k:v for k,v in after.items() if v}
assert after=={'v':1,'one':1}
support_euler=dict(after);support_euler['one']+=1
assert support_euler=={'v':1,'one':2}

print(json.dumps({
    'target':'02YG / night:P4R.4',
    'coefficient_ring':'Z[a_11,...,a_44,lambda_1,...,lambda_4,m,m^-1]',
    'input_relation_matrix':'M=((A-I,lambda),(0,m))',
    'explicit_transform':'U=((I,-lambda/m),(0,1/m)); V=((I,lambda),(0,m))',
    'computed_residual_term_counts':{name:term_count(value) for name,value in checks.items()},
    'diagonalized_matrix':'diag(A-I,1)',
    'rank_consequence_proved_in_derivation':'rank_Q M=rank_Q(A-I)+1, hence b1=4-rank(A-I)',
    'four_by_four_leibniz_terms':24,
    'det_A_minus_I_collected_monomials':len(detD),
    'det_I_minus_A_collected_monomials':len(detMinusD),
    'determinant_difference':len(detDifference),
    'graph_of_spheres_euler_before_tree_substitution':graph_cells_euler,
    'tree_edge_substitution':tree_substitution,
    'curve_euler_after_substitution':after,
    'support_euler_when_e_regular_equals_one':support_euler,
    'limits':'Matrix identities and graph counts are certified algebraically. The exact topological quotient, unimodularity when the group vanishes, and the sign supplied by P4.13 are proved separately.'
},indent=2))
