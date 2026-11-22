"""New recovery computation after target-proof exposure.

The original preproof AV/AX programs and freezes remain separate durable
inputs. This script is newly written after reset and supplies no extra event.
"""
from fractions import Fraction as Q
from itertools import combinations
import json
import sympy as s

# AR: degree-two Hirzebruch--Riemann--Roch coefficient convolution for Omega.
# ch(Omega)=2-c1+(c1^2-2c2)/2, td=1+c1/2+(c1^2+c2)/12.
rr_c1sq=2*Q(1,12)-Q(1,2)+Q(1,2)
rr_c2=2*Q(1,12)-1
assert (rr_c1sq,rr_c2)==(Q(1,6),Q(-5,6))
# On E x P1, c1^2=c2=0. H0(Omega)=1; Serre-dual H2 is H0(T tensor K)=1.
chi=rr_c1sq*0+rr_c2*0
ar_h=[1,int(2-chi),1];assert ar_h==[1,2,1]

# AV: the actual pair quotient S/D is T/C, the one-point compactification
# of (C*)^2 = T^2 x R^2. Its reduced CW counts are the twice-shifted torus
# counts, not an assumption about all attaching maps of the original S.
double_locus_cells={0:2,1:6,2:6}
relative_quotient_reduced_cells={2:1,3:2,4:1}
e_double=sum((-1)**k*n for k,n in double_locus_cells.items())
e_relative=sum((-1)**k*n for k,n in relative_quotient_reduced_cells.items())
assert (e_double,e_relative,e_double+e_relative)==(2,0,2)

# AX: a rank-minor certificate, independent of the printed contraction.
a=s.symbols('a0:4')
bases=[list(combinations(range(4),k)) for k in range(5)]
def wedge_matrix(coeff,k):
    out=s.zeros(len(bases[k+1]),len(bases[k]))
    for col,I in enumerate(bases[k]):
        for j in range(4):
            if j not in I:
                J=tuple(sorted(I+(j,)))
                out[bases[k+1].index(J),col]+=(-1)**sum(i<j for i in I)*coeff[j]
    return out
D=[wedge_matrix(a,k) for k in range(4)]
assert all(D[k+1]*D[k]==s.zeros(len(bases[k+2]),len(bases[k])) for k in range(3))
minors=[]
for k in range(4):
    cols=[i for i,I in enumerate(bases[k]) if 0 not in I]
    rows=[bases[k+1].index((0,)+bases[k][i]) for i in cols]
    minor=s.factor(D[k].extract(rows,cols).det())
    assert minor==a[0]**len(cols)
    minors.append(str(minor))
ranks=[1,3,3,1]
# The displayed nonzero minors give lower bounds. D^2=0 and the dimensions
# inductively give matching upper bounds, hence exactness in every degree.
h=[len(bases[k])-(ranks[k-1] if k else 0)-(ranks[k] if k<4 else 0) for k in range(5)]
assert h==[0]*5

permutations=[]
for j in range(4):
    sigma=list(range(4));sigma[0],sigma[j]=sigma[j],sigma[0]
    P=[]
    for k in range(5):
        mat=s.zeros(len(bases[k]))
        for col,I in enumerate(bases[k]):
            image=[sigma[i] for i in I]
            inversions=sum(image[u]>image[v] for u in range(len(image)) for v in range(u+1,len(image)))
            mat[bases[k].index(tuple(sorted(image))),col]=(-1)**inversions
        assert mat.T*mat==s.eye(len(bases[k]))
        P.append(mat)
    coeff=[a[sigma[i]] for i in range(4)]
    for k in range(4):
        assert D[k]*P[k]==P[k+1]*wedge_matrix(coeff,k)
    permutations.append({'nonzero_original_coordinate':j,'sigma':sigma,'chain_identity_verified_all_degrees':True,
                         'basis_rule':'new wedge e_I maps to sign(sigma|I) times old e_sorted(sigma(I))'})

print(json.dumps({'timing':'new post-reset and after all three target proofs were exposed',
 'new_independent_event_count':0,
 '01AR':{'method':'Hirzebruch--Riemann--Roch and Serre duality',
          'chi_coefficients':{'c1_squared':str(rr_c1sq),'c2':str(rr_c2)},'cohomology':ar_h},
 '01AV':{'method':'actual normalization pair quotient and compact-support Thom cells',
          'double_locus_cells':double_locus_cells,'relative_quotient_reduced_cells':relative_quotient_reduced_cells,
          'relative_euler':e_relative,'rational_normalization_fibre_euler':e_double+e_relative,
          'arbitrary_original_attaching_maps_not_identified':True},
 '01AX':{'method':'nonzero exterior differential minors and square-zero rank bounds',
          'minors_after_pivot_permutation':minors,'ranks':ranks,'cohomology':h,
          'exact_signed_exterior_basis_transports':permutations},
 'all_assertions_passed':True},indent=2,sort_keys=True))
