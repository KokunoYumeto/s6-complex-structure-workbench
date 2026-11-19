# F2.37: two exact auxiliary routes before target exposure

Inputs are solely the clean definitions/assertions in `analysis/continuation_V/F2_37_auxiliary_statement_packet.md`, read before any corresponding printed proof excerpt. No original producing code or target argument has been opened. The present scope is the specified free-lift construction and the marked identity deletion/reinsertion operation; it does not claim the rest of F2.37.

## 1. The specified free affine lift, including its actual order

Let M∈GL_n(Z) have finite order d>1 and let u be a primitive vector in its actual integral fixed kernel. Define g on R^n/Z^n by g(x)=Mx+u/d². Since Mu=u, the exact lifted j-th iterate is

g^j(x)=M^j x+j u/d².

Put S=I+M+⋯+M^(d−1), an integer matrix. The identity SM^j=S follows by cycling the d summands modulo d. Also Su=d u. A fixed point of g^j on the torus has a real lift x and an integer vector lambda satisfying

(M^j−I)x+j u/d²=lambda.

Applying this actual integer map S gives j u/d=S lambda∈Z^n. Primitivity means there are integers c_i with sum c_i u_i=1. Applying that exact integer row to j u/d proves d divides j. Write j=d r. Then M^j=I and the original fixed-point equation is r u/d=lambda. The same integer row proves d divides r. Thus every fixed-point power is a multiple of d². Conversely g^(d²)(x)=x+u, so it is the identity on the torus. Its actual order is exactly d², and every nonidentity power of its cyclic group has no fixed point.

For M=I, translation by u/2 for any primitive u has square equal to the integer translation u and has no fixed point itself, because u/2∉Z^n. Its actual order is2. These constructions require no alteration of the fixed lattice.

To establish necessity, a matrix with zero fixed kernel makes I−M invertible over R. For an arbitrary affine lift x↦Mx+a, the explicit real vector x=(I−M)⁻¹a is fixed already in R^n, and therefore its torus class is fixed. Such an action cannot be free for a nontrivial cyclic group. Conversely, a nonzero real kernel of the integer matrix M−I has a nonzero rational basis vector by rational row reduction. Clearing that vector's denominators produces an integral fixed vector; dividing its entries by their integer gcd gives a primitive fixed vector in the same actual kernel. This specifies the exact maps yielding the vector used above. It proves both directions at the requested free-finite-lift scope.

## 2. At most one identity finite slot

In the specified ordered tuple (M1,M2,M3,M0), two identity finite matrices would leave M0 equal to the inverse of the remaining finite-order matrix. It would have finite order d. With N=M0−I and N²=0, direct binomial multiplication gives M0^d=I+dN. Equality to I over Z forces N=0, contrary to its stated rank3. Thus at most one finite slot is the identity.

## 3. The exact deletion and reinsertion maps

Fix the identity position i. Let D_i delete that finite slot and leave the other finite labels in their displayed order, with M0 still last. Let I_i insert I6 at the same fixed position. The product defining M0 is unchanged, and D_i I_i and I_i D_i are the identity on their respective sets of tuples. For every P∈GL6(Z),

D_i(P M_j P⁻¹)_j=(P (D_i M)_j P⁻¹)_j,
I_i(P A_j P⁻¹)_j=(P (I_i A)_j P⁻¹)_j.

The inserted entry is exactly P I6 P⁻¹=I6. These equations are the actual equivariance maps, so they induce inverse bijections on simultaneous integral-conjugacy orbits in that fixed marked sector. The identity position is itself invariant under simultaneous conjugation and is not relabelled. If a returned convention writes C=P⁻¹ M P instead, the same equations hold with the explicitly inverse matrix P⁻¹; no unidentified conjugator is substituted.

Every remaining matrix is an invertible integer matrix and has at least one entry of absolute value≥1. Hence the maximum entry height of the reduced tuple is at least1, and inserting I6 does not change that height. For two reduced tuples of equal height, their first differing row-major entry is still the first differing entry after the same constant I6 block is inserted: all entries of that block agree. Thus height-first/lex comparison is preserved exactly by D_i and I_i. The least-height/lex representative of the full sector is I_i applied to the least-height/lex representative of its reduced pair, and the very same returned P conjugates every retained matrix and the inserted identity.

The separately specified two-involution branch uses its F2.38 canonical convention. Deletion, that canonical map, and reinsertion still give a canonical representative: equal reduced orbits have equal canonical outputs, and equality of the reinserted outputs implies equality after applying D_i. Its returned unimodular witness works by the same displayed conjugation identities. No assertion that this separate convention equals a height/lex minimum is required or made.

All these operations act on the ordered linear tuple. The supplied affine action and its actual order at position i remain recorded in the gluing input; D_i on the linear tuple performs no operation on that affine datum. The exact linear conjugator P transports its numerator v_i to P v_i along with the other marked vectors whenever the full datum is transported.

## Fresh verification scope

`code/root/F2_37_auxiliary_fresh.py` is authored from these definitions. It verifies the actual S-map and all nonidentity powers for explicit finite integral matrices, including a fixed vector which is not a coordinate summand; checks the exact real fixed-point formula in zero-kernel examples; and checks deletion/reinsertion, height/lex order, and the same unimodular conjugator on an explicit primitive rank-three cusp tuple under many integral changes of basis. It reads no original producer or receiving proof. The finite computations witness the displayed maps; the arguments above prove their stated universal scopes.
