# Independent D.2.45 geometric inputs and relative-class audit

The full parent proof code/root_critical_link_refined_P_proof.tex was
read independently. Its relative-class calculation passes, with the
sphere-selection order now explicit in the source:

1. First form a genuine normal-framed ambient cobordism from the chosen
   three-manifold (or an odd number of copies) to an embedded sphere
   representing the full two-primary generator.
2. Then choose Zhubr's admissible three-frame for that particular sphere.
   Its Spin3 complement can be framed over the trace relative to the
   incoming boundary, since the trace has only one/two-handles.
3. The reference complement frame is spin-compatible because the
   complement of the real-codimension-four critical cycle is simply
   connected. Both induced three-manifold framed classes are even, so
   their Spin6 comparison has even integral degree.
4. Relative stabilization is multiplication by two on the Spin3
   obstruction, and the actual complex critical cycle represents minus
   the relative lambda class. Pairing the identity with a chain bounding
   c times the three-manifold retains the integer ambiguity and proves
   the stated rational linking formula. No division by two in an even
   cyclic group is used.

The local derivative input is code/maps_D2_II_frame_proof.tex.
At the original type-II cap, the map is y²-x³ times the scalar direction,
the critical ideal is (x²,y), and the explicit normalized SU2 clutch has
degree two. The actual critical cycle is 2E_II. At a free good-reduction
logarithmic cap of order m, dividing df by its common (m−1)D factor gives
the target L0(-(m−1)D) and the surjective map m ds on the etale total
cover. The corrected critical cycle is empty. No assumption of
isotriviality or of a free action on an unverified model is made. The
type-II linearization zero is elsewhere. Exact local checks are in
code/maps_D2_II_frame_checks.py/.out.

The actual finite-core reference parity and the preferred full generator
are proved in code/maps_D2_finite_generator_frame.tex. Kaplan's
spin-compatible zero/two-handle filling gives actual tangent-framing
parity 1+b1(N;F2). For the finite-II mapping torus this is zero.
The corrected target line gives the true complex normal direction,
and projection along the transverse delta vector converts the global
vertical reference frame to an actual tangent three-frame.

The preferred primitive character is

    chi(delta)=1, chi(ell)=-sigma*r, chi(g)=-sigma*r*e,
    sigma=n-m*e=±1.

It respects m*g=r*delta+n*ell. Its kernel has order-six elliptic
monodromy B^sigma. More importantly, the D.2.30 reduced Thom columns
have pairings (1,-sigma*r,0), including the nonzero root-loop term
before the column change Kg-e*Kell. Thus b*s bounds with pairing
sigma, so this N is a full H3 generator even when b=20. Root
independently checked these identities; the six-manifolds agent is
replaying the full integral marked matrix with the root-loop term.
The earlier character with chi(g)=0 was valid but needlessly lost
some odd-primary information and is not used in the final input.
