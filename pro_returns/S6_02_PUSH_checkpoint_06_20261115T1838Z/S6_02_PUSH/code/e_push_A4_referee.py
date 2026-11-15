"""Independent integral checks for A.4, using the odd blow-up lattice I_(1,9).

This does not import any AB program or its E8 basis.  Geometry and the
identification of the maps are checked separately in E_A4_referee.md.
"""
from pathlib import Path
from itertools import combinations
import json
import math
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

G=s.diag(1,*([-1]*9))
F=s.Matrix([3]+[-1]*9)
O=s.eye(10)[:,9]
m=s.eye(10)[:,8]-O
v=s.Matrix([0,1,1,-1,-1,-1,0,0,1,0])
n=m-F
pair=lambda a,b:(a.T*G*b)[0]
assert [pair(F,F),pair(F,m),pair(F,v),pair(m,m),pair(v,v),pair(m,v)]==[0,0,0,-2,-6,-1]
assert [pair(O,F),pair(O,m),pair(O,v),pair(O,O)]==[1,1,0,-1]
T=s.eye(10)+v*(F.T*G)-F*(v.T*G)+3*F*(F.T*G)
assert T.T*G*T==G
assert T.T*G*m==G*n

def factors(M):
    D=smith_normal_form(M,domain=ZZ)
    return [abs(int(D[i,i])) for i in range(min(M.shape))]

def quotient_projection(M):
    """Explicit split quotient when a unimodular maximal minor is present."""
    r=M.cols
    for rows in combinations(range(M.rows),r):
        minor=M[list(rows),:]
        if abs(minor.det())==1:
            other=[i for i in range(M.rows) if i not in rows]
            P=s.zeros(len(other),M.rows)
            for j,i in enumerate(other):
                P[j,i]=1
            correction=-M[other,:]*minor.inv()
            for j,i in enumerate(rows):
                P[:,i]=correction[:,j]
            assert P*M==s.zeros(len(other),r)
            assert all(x.q==1 for x in P)
            assert P[:,other]==s.eye(len(other))
            return P,list(rows)
    raise AssertionError('No unimodular coordinate minor found')

def primitive_row_kernel(row):
    pivot=next(i for i,x in enumerate(row) if abs(x)==1)
    others=[i for i in range(row.cols) if i!=pivot]
    K=s.zeros(row.cols,len(others))
    for j,i in enumerate(others):
        K[i,j]=1
        K[pivot,j]=-row[i]/row[pivot]
    assert row*K==s.zeros(1,len(others))
    return K

C=s.Matrix.vstack(F.T*G,v.T*G,m.T*G)
assert factors(C)==[1,1,1]

# Solve the three kernel equations over Z with seven freely chosen variables.
p=s.Matrix(s.symbols('h a2 a3 a4 a5 a6 a7'))
h,a2,a3,a4,a5,a6,a7=p
a8=-3*h-2*a3-2*a4-2*a5-a6-a7
a1=3*h-a2+3*a3+3*a4+3*a5+a6+a7
a=s.Matrix([h,a1,a2,a3,a4,a5,a6,a7,a8,a8])
K=a.jacobian(p)
assert C*K==s.zeros(3,7)
assert K[[0,2,3,4,5,6,7],:]==s.eye(7)

M=s.Matrix.hstack(F,v,m)
P,pivots=quotient_projection(M)
N=P*K
assert factors(N)==[1,1,1,1,1,11,0]
assert N.rank()==6
fullN=s.zeros(14)
fullN[:7,7:]=N
assert fullN**2==s.zeros(14)

# Integral Thom restriction map H^2(R+) -> H^2(S) + H^2(S).
restriction=s.Matrix.vstack(s.Matrix.hstack(s.eye(10),s.zeros(10,1),F),
                           s.Matrix.hstack(s.eye(10),-m,s.zeros(10,1)))
assert restriction.rank()==12
assert factors(restriction)==[1]*12

# Divisor evaluations on H_2(R+), with coordinates (a, lambda, eta).
section_intersections=s.Matrix.vstack(
    s.Matrix.hstack(m.T*G,s.Matrix([[1,-1]])),
    s.Matrix([[0]*10+[1,0]]))
assert factors(section_intersections)==[1,1]
Z2=s.Matrix.vstack(s.eye(10),s.zeros(1,10),m.T*G)
assert section_intersections*Z2==s.zeros(2,10)

# Normalization map and its restriction to the primitive boundary bundle.
d2=s.Matrix.vstack(s.eye(10)-T,n.T*G,F.T*G)
assert d2.rank()==3
assert [x for x in factors(d2) if x]==[1,1,1]
En2=primitive_row_kernel(n.T*G)
restricted=d2*En2
base_map=(s.eye(10)-T)*En2
assert restricted==Z2*base_map
assert base_map.rank()==2
assert [x for x in factors(base_map) if x]==[1,1]

Pfm,_=quotient_projection(s.Matrix.hstack(F,m))
vbar=Pfm*v
assert math.gcd(*[int(x) for x in vbar])==1
assert Pfm*(T-s.eye(10))==vbar*(F.T*G)

gram=s.Matrix.hstack(n,v).T*G*s.Matrix.hstack(n,v)
assert gram==s.Matrix([[-2,-1],[-1,-6]])
assert gram.det()==11
out={
 'independent_lattice':'I_(1,9), basis h,e1,...,e9',
 'intersection_matrix':G.tolist(),'F':list(F),'O':list(O),'m':list(m),'v':list(v),
 'constraint_smith':factors(C),'kernel_basis':K.tolist(),
 'quotient_pivot_rows':pivots,'quotient_projection':P.tolist(),
 'N_block':N.tolist(),'N_smith':factors(N),'N_rank':int(N.rank()),
 'N_square_zero':True,'root_gram':gram.tolist(),'root_discriminant':int(gram.det()),
 'Thom_restriction_smith':factors(restriction),
 'section_intersection_smith':factors(section_intersections),
 'normalization_d2_smith':factors(d2),
 'restricted_MV_d2_smith':factors(base_map),
 'v_mod_F_m':list(vbar),
 'node_generization_matrix':[[1,0],[1,1]],
 'node_generization_determinant':1,
 'note':'The node generization and orbit-trace identifications are proved geometrically in the separate referee note, not inferred from this code.'
}
print(json.dumps(out,indent=2,default=str))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2,default=str)+'\n')
