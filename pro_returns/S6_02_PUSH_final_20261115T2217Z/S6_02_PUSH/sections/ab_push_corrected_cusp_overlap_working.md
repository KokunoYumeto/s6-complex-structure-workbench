# A corrected cusp over the punctured bidisc

Owner: limits_ab. 15November2026,19:00UTC. **Working proof; independent review requested. No completion over the origin is claimed.**

The intended contribution is an explicit comparison of the rotating central model with the prescribed punctured cusp, not another claim that a multiple cusp already fills the actual family.

## 1. Exact affine data

On the logarithmic cover of U=Δq*×Δr* put

s=log(q)/(2πi), t=log(r)/(2πi), C(q)=βpart(q)+s.

The actual cusp functions μ(q) and C(q) are single-valued and holomorphic at q=0. After the B.4.9 affine gauge, the family is its Jacobian with period

γ(s,t)=(6μ(q), C(q)−s−12t), δ=(0,1).

The other two periods are u=(τ,μ), w=(1,0), with τ increasing by1 under s→s+1. The monodromies send γ toγ−δ under a q loop and toγ−12δ under an r loop. The ambient additive C² coordinate is unchanged; these are integral changes of the period basis.

Define the affine q-deck translation

b(s,t)=γ(s,t)/12−δ/24.

Its twelvefold norm is

sum(k=0..11)b(s+k,t)=γ(s,t)−6δ,

an actual integral period. Further b(s,t+1)−b(s,t)=−δ. Thus on the q-root cover q=z^12 it gives a genuine order12 affine deck action, well-defined around the r loop. Taking −b supplies the opposite component rotation. The half-integral scalar correction is retained; a bare γ/12 would have the wrong twelfth iterate.

The explicit logarithmic-cover function

f(s,t)=( μ(q)(s+12t)/2,
         C(q)(s+12t)/12−(s+12t)^2/24+6t )

satisfies the exact identities

f(s+1,t)−f(s,t)=b(s,t),
f(s,t+1)−f(s,t)=γ(s,t).

The second difference is an integral period. Therefore translation by f gives a holomorphic trivialization of this affine torus torsor on U. Translation by −f treats the desired opposite rotation. Composing with the already proved B.4.9 gauge identifies it with the actual retained affine cusp family, not merely with its unmarked fibrewise periods.

## 2. The rotating model with the wrong q-boundary

For completeness, its compactification can be constructed on the root cover before quotient. In multiplicative coordinates, the periods have valuation shears

G1:(y1,y2,hz,hr)→(y1+12hz,y2,hz,hr),
G2:(y1,y2,hz,hr)→(y1,y2+12hz+12hr,hz,hr).

The fractional affine deck has monomial shear

H:(y1,y2,hz,hr)→(y1,y2+hz+hr,hz,hr),

and rotates z by exp(2πi/12). It has H^12=G2 and commutes with G1. Its unit factors are single-valued in q. In the convention W=exp(−2πiζ2), the positive translation b multiplies W by

r z exp(−2πi C(q)/12) exp(πi/12)

and the first multiplicative coordinate by exp(πi μ(q)). In the twelfth iterate, the z-rotation contributes exp(2πi·66/12)=−1 and the scalar correction contributes exp(πi)=−1; their product is1, so the twelfth iterate is exactly the actual second period, including its unit.

Use the usual unit-square cusp triangulation, with twelve consecutive bottom cells in the y1 direction, and the same bridge choice in every cell. It is invariant under G1 and H, hence under G2. Each of its unit prisms has the three determinant-one cones of A.2.1. The A.1.2 compact-core construction on the I12 elliptic root model, or its explicitly unfolded toric charts, gives the proper rank-one model on the root cover. The finite H action extends because it is an actual torus-unit map preserving the fan. It is free on the r-central divisor: its nontrivial powers rotate the twelve r-component labels, and at most two adjacent r-branches meet. It is also free on the q-central divisor away from r=0, by the nonzero translation of the q-component grid. The same r-branch argument covers their common locus. Off those divisors it is free because the root-base action is free. Consequently its quotient is smooth, proper over (q,r), flat over r, and has reduced NC r-centre.

The component monodromy around q is +1 for b and −1 for −b, in the common convention. Its q-fibre for r≠0 has multiplicity12, exactly as in B.3.3. This is the wrong q-boundary, and is not substituted for the actual Mumford fibre.

## 3. A proper family over the punctured bidisc

Let B^×=(Δq×Δr)\{(0,0)}. On the open subset q≠0 use the preceding rotating model, with the sign giving component shift−1. On the open subset r≠0 use the actual prescribed reduced Mumford cusp family. On their intersection U, glue by translation−f composed with the B.4.9 actual gauge. These are specified holomorphic isomorphisms of the actual period quotients. There is only one overlap, so no additional triple cocycle is being omitted.

The resulting analytic space is Hausdorff and proper over B^×: both properties follow locally over the two base open sets, which are proper Hausdorff models there. It has smooth total space and is flat over r. Its r-central fibre over q≠0 has the required shift−1, whereas its q-fibre over each r≠0 is exactly the prescribed reduced Mumford cusp. This is a partial filling over a punctured bidisc, with the missing set reduced to the single base origin.

The remaining task is a proper analytic completion over that origin with smooth total space and reduced NC r-centre (after any permitted finite base change), and a compatibility proof with the global finite-place data. None is supplied by the exact affine identities. The comparison contains quadratic logarithms, so neither Remmert graph closure nor a meromorphic common modification may be assumed. Indeed a proper birational comparison between the two full q-boundaries for fixed r≠0 is excluded by their multiplicity12 versus reduced multiplicity1, as already proved in B.3.7.

## Verification record

`code/ab_push_corrected_cusp_overlap.py` verifies the two finite differences, twelvefold norm, scalar phase, commuting shears and determinant-one unit cones exactly. The global root-cover fan/gluing and free-action arguments above require independent review before this partial-family proposition is promoted to a numbered result. The earlier288 q-cover Euler calculation is already established in the parent package and is not claimed here as a new result. The auxiliary B.3.7 plumbing's twelvefold circle cover has the same local12-by12 cusp combinatorics, but no global isomorphism of that cover with the actual q-basechanged family is inferred from the numerical match.
