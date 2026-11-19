# CR.4 and UN.9: independent full proof and printed-step comparison

19 November 2026. GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro.

The complete written prereading proof is `CR4_UN9_before_read.md`.
The clean statement packet was its only target input. The new exact
local-algebra program passed before the two isolated target proof
blocks were opened. The comparison below preserves the narrower
scope of a different printed transport route.

## Rank loss and actual normal forms

The critical locus is used with its stated reduced-support meaning.
The proof derives f in (x,y)^2 from the actual critical axis; it does
not replace the Jacobian ideal by a reduced ideal. The unit-root
reduction of the full map was also written before reading: critical
components through the point have value zero, so multiplication by a
unit preserves the critical germ after shrinking.

For the cusp, the printed primitive symmetric rank-one factorization
matches the saturated-line factorization in the prereading proof.
The parameter choice a(z)+epsilon with a simple zero and a nonzero
perturbed kernel cubic coefficient is identical. The Weierstrass
and depressed-cubic formulas, including divisibility by X and X^2,
are explicitly computed by the new program. The actual curve
coordinate Z=beta*Y+gamma has nonzero z-derivative at the chosen root.

The printed unit removal scales all three coordinates by a cube
root; the root derivation uses the weights (1/2,1/3,0). These maps
are related exactly: write the unit as r^6. In the root's coordinates
(U,V,W)=(r^3X,r^2Y,Z), the printed map is
(U,V,W) -> (r^-1 U,V,r^2 W), with r pulled back by the first inverse
coordinate map. It preserves V^3+U^2 W exactly and has invertible
Jacobian at the origin. Thus both maps identify the same actual
local levels with the Hirzebruch model.

For the node, the root prereading proof uses the incidence
det(Q(z)+E)=0 with rank one and nonzero determinant derivative. The
printed explicit choice uses a rank-one matrix R. The parameter
change (z,E) -> (z,R=Q(z)+E), inverse E=R-Q(z), identifies those
incidence spaces. In both coordinates the same derivative is
tr(adj(R)Q'(z)). The nonzero symmetric derivative pairs nontrivially
with rank-one adjugates, exactly the fact used in the prereading
incidence argument. The subsequent splitting and substitution
Z=h(y,z) match the written proof. The nonzero-Hessian case was
already treated there by the supplied A.5.17 input.

## Boundary and transport

The root independently wrote the entire uniform boundary argument.
On the compact critical link the transverse quadratic/cubic
coefficients are units; parameter-dependent product charts supply a
curve-direction tangent vector to every level, with nonzero radial
component. A finite chart cover makes this uniform. The remaining
boundary regions are controlled by the original smooth-stratum
transversality and a positive lower bound on |f|. This is exactly the
printed boundary argument in CR.4 step5 and UN.9 step4.

The root then used a path in the joint parameter/regular-value
discriminant complement. The printed proofs use two legs: first move
the level value at fixed perturbation, then move the perturbation to
zero at a fixed value outside all its critical values. That uniform
critical-value estimate was not separately written in the root
prereading file. It was therefore assigned to the fresh V reviewer,
who saved `VI_CR4_transport_factor_before_read.md` before receiving
only CR.4 steps2/6 and UN.9 step5. The V comparison receipt is required
for that particular printed route; the root's alternative path is
not used to infer its chronology.

The root does independently supply the final local-to-global map:
transport by a proper boundary submersion, followed by the open
embedding of the actual reduced level in the original torus fibre.
The spherical cycle's compactly supported Poincare dual extends by
zero, preserving its square. The sphere then lifts to the torus
universal cover C^2 and is null-homotopic, contradicting its square
-4. No injectivity of all local homology into the torus is assumed.

## Additional printed cusp clause

The printed CR.4 step2 separately checks that y^3u has singular
reduced support when u(0,0)=0 and u(0,z) is not identically zero.
The root used the full stated nonzero-Hessian consequence of A.5.17
directly. The explicit reduced-divisor intermediate clause was
included in the V review assignment and written there before target
exposure, rather than credited retroactively to the root.

## Scope

The root has a complete independent alternative proof of both target
statements, with new exact coordinate algebra. The current printed
proofs are covered by the precise union of this derivation and the
separate V derivations after their comparison. No statement change or
proof repair is presently required. The local spherical-class input
and A.5.17 are the supplied cited inputs, not newly proved by this
root event. The newly used proper-image input was opened in Grauert
1960, Section7 Satz1, printed p.60.
