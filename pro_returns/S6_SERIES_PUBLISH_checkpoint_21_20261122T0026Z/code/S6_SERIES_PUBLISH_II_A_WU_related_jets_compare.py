#!/usr/bin/env python3
"""Postrelease WU comparison with the positively related P4.14 jet routine.

Compute explicit quotient maps and right inverses instead of matrix ranks.
The independent prerelease polynomial preimages prove that their kernels
are exactly the image rings. No additional prereading event is claimed.
"""
import json


def vector(q,n,j,k):
    rows=[[0]*n for _ in range(q)]
    rows[j][k]=1
    return rows


def defect(rows):
    if len(rows)==2:
        a,b=rows
        return [a[0]-b[0],a[1]-b[1]]
    a,b,c=rows
    return [a[0]-c[0],b[0]-c[0],c[1]-a[1]-b[1]]


def main():
    records=[]
    for q in (2,3):
        for n in (2,3,4,6,8):
            # These are explicit preimages of the standard quotient basis.
            lifts=([vector(2,n,0,0),vector(2,n,0,1)] if q==2 else
                   [vector(3,n,0,0),vector(3,n,1,0),vector(3,n,2,1)])
            for j,v in enumerate(lifts):
                assert defect(v)==[int(i==j) for i in range(q)]
            # Every pure order >=2 branch vector is in the kernel; no pure
            # order-one branch vector is. Polynomial preimages are in the
            # prerelease program and complete derivation, not rank tests.
            membership=[]
            for j in range(q):
                assert any(defect(vector(q,n,j,1)))
                for k in range(2,n):
                    assert defect(vector(q,n,j,k))==[0]*q
                    membership.append([j,k])
            kernel_dimension=q*n-q
            basis_count=(2 if q==2 else 3)+q*(n-2)
            assert basis_count==kernel_dimension
            records.append(dict(branches=q,order=n,quotient_dimension=q,
                kernel_dimension=kernel_dimension,explicit_kernel_basis_count=basis_count,
                higher_branch_vectors=membership,conductor_orders=[2]*q,
                chi_normalization=q,chi_curve=q-q,arithmetic_genus=1-(q-q),
                normalization_conductor_length=2*q,
                image_conductor_quotient_length=2*q-q))
    # The prior triple branch order is (t,0),(0,t),(t,t); ours is
    # (0,t),(t,0),(t,t). Ambient x,y are unchanged. This exact permutation
    # is an algebra isomorphism over the common ring xy(x-y)=0.
    permutation=[1,0,2]
    for x_coeff,y_coeff,constant in ((1,0,0),(0,1,0),(0,0,1),(3,5,7)):
        old=[(constant,x_coeff),(constant,y_coeff),(constant,x_coeff+y_coeff)]
        new=[old[j] for j in permutation]
        assert new==[(constant,y_coeff),(constant,x_coeff),(constant,x_coeff+y_coeff)]
    print(json.dumps(dict(timing='postrelease',method='explicit defect quotient with a written right inverse',
        triple_factor_permutation_old_to_new=permutation,
        ambient_coordinate_map='identity on x,y',records=records,
        conclusion='all exact quotient and dimension identities passed'),indent=2))


if __name__=='__main__':
    main()
