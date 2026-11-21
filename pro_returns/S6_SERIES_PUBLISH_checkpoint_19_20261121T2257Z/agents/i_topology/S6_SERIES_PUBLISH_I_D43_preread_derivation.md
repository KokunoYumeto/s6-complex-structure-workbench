# Preread derivation — push:src:D.4.3 [032L]

The target proof has not been opened. Inputs are the target's exact real-linear map A:R4→C2 of rank3 and normalized kernel Rk, k1=1. No period-specific analytic claim is used.

Let q:R4→T4=R4/Z4. The annihilator in the character lattice Z4 of the one-parameter subgroup q(Rk) is exactly L_k={m:m·k=0}. Characters separate closed subgroups of a torus, so the closure of q(Rk) is the connected subtorus with Lie algebra V_k=intersection ker(m), m∈L_k. This character statement can also be proved by averaging a character along the line: nonzero frequencies average to zero, while exactly L_k survive; Fourier approximation separates a point outside the asserted subtorus. Thus
closure(Z4+Rk)=Z4+V_k.

The map A factors as the open quotient R4→R4/Rk followed by a real-linear isomorphism onto W=imA. For any subset S of W, openness implies A^(-1)(closure S)=closure(A^(-1)S). Apply this to S=A Z4: its preimage is Z4+Rk. Therefore
closure(A Z4)=A(Z4+V_k).
This is the actual quotient-map derivation of the closure formula.

L_k is a saturated sublattice of Z4: if N m lies in it for a nonzero integer N, then m·k=0. A basis m1,...,mr of L_k therefore extends to an integral basis of Z4. Define
Phi:W→(S1)^r, Phi(Ax)=(exp(2πi m1·x),...,exp(2πi mr·x)).
It is well defined because every mi kills k. Its kernel is exactly A(Z4+V_k): extend the mi to an integral basis to see that all integral coordinates in the first r slots can be subtracted by an actual Z4 vector, leaving V_k. It is surjective by solving the r independent real linear equations. Choose a real normal vector n to W. Then the map
Psi: C2→R×(S1)^r, Psi(Ax+t n)=(t,Phi(Ax))
is a continuous open surjective homomorphism with that same kernel. It induces the asserted Hausdorff quotient, including its exact topology.

r=3 holds exactly when Rk is a rational line: the common kernel of three independent rational rows has dimension1 and a rational generator; conversely a primitive integral generator has a rank-three integer annihilator. Since k1=1, a rational line is equivalent to k∈Q4. In that case A Z4 is a rank-three lattice in W, so its translations are discrete and the complex quotient is a Hausdorff complex Lie group. If r<3, A V_k has dimension3−r>0; closure(A Z4) contains this uncountable connected subgroup, while A Z4 is countable, so A Z4 is not closed. The quotient is non-Hausdorff. This gives the exact obstruction, not only an irrationality slogan.

For A_j→A with A_j invertible and L_j=A_j Z4, every fixed integer v gives A_j v→Av. If a subsequence of L_j has a Chabauty limit L, the defining limit-point property puts Av in L. Since L is closed, closure(AZ4)⊂L. Equality need not hold: take A_epsilon=diag(epsilon,1,1,1), with the standard real identification R4=C2 and epsilon>0. Then A0 has kernel Re1; A0Z4={0}×Z3, whereas the Chabauty limit of epsilon Z×Z3 is R×Z3. For every real x, choosing nearest integers n_epsilon to x/epsilon constructs epsilon n_epsilon→x, proving the extra R explicitly. The induced map C2/(A0Z4)→C2/(R×Z3) has kernel R, so the two quotient spaces are related by this nontrivial quotient map rather than being silently identified.

All of these arguments are independent of the target proof. The only background theorem is the elementary character description of closed subgroups of a torus, with the Fourier proof supplied above. The target has no nontrivial numerical constant to certify; a new exact example program will verify the rational annihilator ranks and the displayed degeneration model.

Saved UTC: 2026-11-21T01:15:36.200585+00:00
