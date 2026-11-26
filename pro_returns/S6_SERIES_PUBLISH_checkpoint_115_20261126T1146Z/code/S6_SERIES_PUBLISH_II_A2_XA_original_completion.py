#!/usr/bin/env python3
"""Recompute every displayed algebraic step in the retained 02XA proof.

This program was written after the target was released.  It uses formal
coefficient expansion of bilinear products, not an enumeration of Kato
configurations or a claimed analytic classification certificate.
"""
import json
import sympy as s


def main():
    K,V,R,Z=s.symbols('K V R Z')
    n,k,z0,z1=s.symbols('n k z0 z1')
    KK,KV,VV,KR,KZ,VR,VZ,RR,RZ,ZZ=s.symbols('KK KV VV KR KZ VR VZ RR RZ ZZ')
    products={K*K:KK,K*V:KV,V*V:VV,K*R:KR,K*Z:KZ,
              V*R:VR,V*Z:VZ,R*R:RR,R*Z:RZ,Z*Z:ZZ}
    def intersect(expr):
        poly=s.Poly(s.expand(expr),K,V,R,Z)
        result=0
        for powers,coefficient in poly.terms():
            monomial=K**powers[0]*V**powers[1]*R**powers[2]*Z**powers[3]
            result+=coefficient*products[monomial]
        return s.expand(result)
    ell=-K+V+Z
    jj=R-V-Z
    jj1=K-R
    chern=intersect(ell*ell-jj*jj1)
    B=RR-KR-VR-RZ-KZ+2*VZ+ZZ
    assert s.expand(chern.subs({KK:-n-k,KV:VV})-(B-n-k))==0

    c,d,eps=s.symbols('c d epsilon',integer=True)
    changed={KR:KR-c,VR:VR-eps*c,RZ:RZ-c*d,
             KZ:KZ-d,VZ:VZ-eps*d,RR:RR-c*c,ZZ:ZZ-d*d}
    delta=s.expand(B.subs(changed,simultaneous=True)-B)
    u,v=s.symbols('u v')
    Q=u*u-u*v+v*v
    assert s.expand(2*Q-(u*u+v*v+(u-v)**2))==0
    equality=[]
    for a in [0,1]:
        shifted=s.expand(delta.subs({eps:a,c:1+u,d:1-a+v}))
        assert s.expand(shifted-(1-Q))==0
        equality.append({'epsilon':a,'maximum':1,'unique_maximizer':[1,1-a]})
    invariant_change=s.expand((KV-eps)-(VV-eps*eps)-(KV-VV))
    assert invariant_change==eps*eps-eps
    assert all(invariant_change.subs(eps,a)==0 for a in [0,1])

    D,A,r,z=s.symbols('D A R0 Z0')
    # Multiplication is formal symmetric intersection; expansion is universal.
    B0=r*r+D*r+A*r-z*r+D*z-2*A*z+z*z
    X=r+D
    Y=z+D-A
    q=X*X-X*Y+Y*Y
    completion_remainder=s.expand(n+q-B0)
    assert completion_remainder==A*A-A*D+D*D+n
    assert s.expand(completion_remainder.subs(A*D,A*A).subs(D*D,-n))==0
    xx,yy=s.symbols('X Y')
    assert s.expand(xx*xx-xx*yy+yy*yy-(xx*xx+yy*yy+(xx-yy)**2)/2)==0
    # Adjunction on the cycle-with-trees curve gives K.A=-A.A, V=-A.
    KA,AA=s.symbols('KA AA')
    initial_invariant=-KA-AA
    assert initial_invariant.subs(KA,-AA)==0
    components,nodes=s.symbols('components nodes',integer=True)
    chi=components-nodes
    assert chi.subs({components:n,nodes:n})==0
    gap=s.symbols('gap',positive=True)
    final_upper=s.expand(n-gap+k)
    exact_chern=n+k+z0+z1
    contradiction_gap=s.expand(exact_chern-final_upper)
    assert contradiction_gap==gap+z0+z1

    print(json.dumps({
        'tag':'02XA','phase':'after target-proof release',
        'retained_original_proof_items':7,
        'chern_expansion':str(chern),
        'chern_identity':'B(R,Z)=n+k+z0+z1',
        'blowup_increment':str(delta),
        'complete_blowup_maxima':equality,
        'twice_positive_quadratic':'u^2+v^2+(u-v)^2',
        'K_V_minus_V_square_increment':str(invariant_change),
        'initial_K_V_minus_V_square':0,
        'normalization_chi_of_n_components_and_n_nodes':0,
        'initial_B_expression':str(s.expand(B0)),
        'completion_arguments':[str(X),str(Y)],
        'completion_remainder_before_D_square_and_D_A_relations':str(completion_remainder),
        'completion_remainder_after_D_square_minus_n_and_D_A_A_square':0,
        'negative_form_identity':'q(X,Y)=(X^2+Y^2+(X-Y)^2)/2',
        'strict_initial_gap_propagation':str(contradiction_gap),
        'limitations':'No source theorem, independence of curve classes, effectiveness, saturation, conormal line, curve graph, or holomorphic local first integral is inferred from these polynomial calculations. Each such premise is separately verified in the comparison.',
        'all_assertions_passed':True,
    },indent=2))


if __name__=='__main__':
    main()
