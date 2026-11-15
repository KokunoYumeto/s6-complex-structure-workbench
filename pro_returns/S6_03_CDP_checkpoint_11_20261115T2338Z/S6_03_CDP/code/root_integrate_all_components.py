"""Record full occurrence and whole-support comparison audits through UN45."""
from pathlib import Path
from datetime import datetime, timezone
import csv

root=Path(__file__).resolve().parents[1]
stamp=datetime.now(timezone.utc).isoformat()
record=f'''# Complete component range and whole-support constraints

UTC: {stamp}

UN39: root read the whole proof and all nineteen exact outputs. The average
is taken over a common multiple of every resolved component multiplicity,
so it includes all components before cancellations. A'Campo's exact trace
formula then makes the open-surface Euler sum equal to j(T). Counting the
three double-curve incidences at each triple point gives the displayed
genus/triple correction. The actual full inverse image under a point or
curve blowup has projective fibres, giving exactly2 or2−2g independently
of the scheme multiplicity along the centre. Thus e(S)=j(T)−2I holds for
every actual support and makes I resolution independent. The constants
are0,4,6,8; the point/quartic example checks both correction signs. Root PASS.

UN40: root read the complete integral adjunction and point-blowdown proof.
Clearing the original component multiplicity gives the stated exact
divisor-class identity. Its push is through the common meromorphic field,
not an unjustified coherent direct-image identification. The pushed
boundary is reduced because a strict curve has one generic SNC neighbour.
The actual finite unramified primary cover retains all these coefficients.
The contracting-unit/eigenfunction proof gives the full axis list, and
Hartogs applied to a trivializing function and its inverse makes the
automorphy-factor map injective. Independent diagonal axis classes force
both boundaries and equal canonical ratios; the nonlinear infinite-order
axis class forces the exact strict decrease. A shared elliptic curve cannot
be a point-blowdown exceptional curve on the other component, so the
nonlinear-versus-a0-Hopf adjacency exclusion follows. Root PASS.

UN41: root read the entire construction, including the final exact Tate
chart, and every executed output. Inversion identifies each actual Hopf
axis normal with the inverse normal on the second copy. The gluing uses
explicit open collars; at either boundary of an overlap one of the two
points is absent, so the identification graphs are relatively closed.
The two core overlaps are disjoint by |t|<r². Nested compact cores and
bounded line-bundle necks cover every closed inverse image, proving
properness. The actual core/neck coordinate maps give a local isomorphism
to the stated C*² lattice quotient. The height intervals cover one period
circle with exactly one preimage at height zero, so its degree is one.
The four additive period vectors have the computed nonzero real determinant.

For compactness, the generic cubic pencil through the specified smooth
nodal points gives the desired I1 fibre and section. K_J=−F makes the
minimal graph argument extend translation by that section through all
fibres. The actual Tate series, central Weierstrass coordinate change and
nodal multiplicative coordinate identify a(0) with the prescribed alpha,
including its sign. The simple q-zero retains a smooth xy=q(t) neck.
The suspension is a compact J-bundle over E_(alpha beta), and z=y,w=u/y
identifies its two periods exactly with the plumbing periods. Gluing these
proper pieces over the compact base therefore gives the claimed compact
threefold. All other supports are bundles over an elliptic curve and have
Euler zero. The primitive integral restriction matrices give free support
ranks(1,2,3,4,2), and the constant-cocycle restrictions give hO(1,2,1).
Root PASS; independent A full-source audit PASS. The exact code also checks
all neck maps, height intervals, Tate signs, q-series and Smith forms.

UN42: root read the entire weighted construction and its executed output.
The explicitly squarefree hyperelliptic curve has the two stated infinity
points and exact order-r translation jets. The weighted blowup stack is
specified by its actual C* chart, and its weight-one nonzero line kills
the finite stabilizer. Gauge ell=1 gives a smooth threefold chart and the
exact nonlinear Hopf restriction. The canonical section norm is comparable
to the weighted elliptic distance on a whole B-times-small-disc chart;
the inverse translation gives the lower bound as well. The uniform
polynomial bound is dominated by every prescribed |beta|^n, proving a free
proper action and a compact annular fundamental set. No stronger smallness
assumption on beta is inserted.

The canonical lifts obey their group laws because they preserve the actual
divisor section. The half-period map squares to the infinite deck map.
At every fixed point of its base involution, comparison of fibre norms
would require |beta|^(1/2)=|beta|^n, so the finite quotient is free. It
exchanges the two Hopf components, retaining either one unchanged over P1.
The exact p=x^r z,s=xw chart gives the second component's one r-fold
elliptic fibre and canonical divisor(r−1)J. The Seifert meridian/longitude
matrix and the radial product comparison give the stated integral and
coherent groups. The primitive restriction maps give support ranks
(1,3,5,5,2) and hO(1,2,1). The local invariant holomorphic three-form
x^r dz wedge dw wedge dx has evaluation orders(r,0), exactly realizing
UN40. The earlier pair(0,−r) is only a meromorphic full-fibre shift and is
not used as holomorphic generator orders. Root PASS; D and A independent
full-source audits PASS. The written polynomial argument covers every r;
the executed algebra checks ten orders, the involution and all Smith maps.

UN43: root read the complete quotient proof and the two requested edits.
The normal core of the primary contraction subgroup is central by the
nonzero determinant-modulus character. Commuting power-series equations
give the full diagonal or nonlinear centralizer, so the actual deck group
is abelian. Its Z-plus-finite-torsion decomposition gives exactly the
cyclic characters in the theorem, with freeness read on the axes. The
nonlinear centralizer is derived directly from its two coordinate equations,
not only quoted. The finite exact-order-n torsion cover contains the
chosen local mu_n section and is unramified at that I1 point, by the
nonzero derivative of multiplication by n on the smooth nodal group.
Thus the actual prescribed section and local model survive the compact
base change. Translation extension, the global suspension action, and
the inverse-weight neck action all commute through the written maps.
The distinguished quotient tube is smooth and retains the given secondary
Hopf surface. The nonlinear scalar action is free in every weighted chart
and remains free modulo the infinite deck group. Other fibres may be
balanced away from the distinguished tube. Root PASS; independent E
full-source audit PASS. The sufficient specified compact-base scope is
retained; the unnecessary optional P1 dependency was removed from UN43.

UN44: root read the entire proof, its rank-two addition and all539 exact
Smith tests. The gradient inequality gives a finite, uniform remaining
length for the normalized negative-gradient flow and hence an actual
strong tube retraction. Root independently opened Kurdyka1998's original
Numdam scan, printedp775 Theorem(LI): its exponent is strictly below one,
exactly as required. General-position discs give the full normal meridian
kernel, and the local f=u z^mi equation gives each actual winding mi.
The gcd quotient has exact index d. The normalized root chart v^d=u,s=vh
is etale everywhere in the smooth total tube, including above singular
support points; its lifted retraction proves the central cover connected.
All lifted meridians are retained, giving the exact integral A presentation
with torsion. Sphere-bundle van Kampen comparisons preserve pi1 through
every actual smooth blowup. The intersection mapping cylinders give a
homotopy comparison with the support and the surjection to its dual complex.

The actual specialization map F->S is a ring map and injects rational H1
because the image of pi1(F) has finite index. Pulling back three independent
dual-complex H1 classes would give a nonzero wedge in H3(T4), whereas the
two-dimensional complex has no H3. Its degree-one exterior algebra therefore
injects and b1<=2. The finite cover belonging to the image of A pulls back
to the precise winding-mod-a cover, which is normalized s^a=f because a|d.
The same comparison on that cover bounds the finite-index abelian subgroup's
rank by two. For no-triple graphs, the elementary finite graph-cover rank
formula gives a tree or a single cycle; a cycle also forces eigenvalue1
in monodromy. Root PASS, including the complete added cover argument.

UN45: root wrote the full all-curve construction and executed fifty exact
plane-branch examples. D independently read every step and ran the code:
PASS. The primitive-element map gives the specified curve as the actual
normalization of a plane model. Each singular-point blowup lowers its
nonnegative total normalization defect by m(m−1)/2, giving a finite
resolution inside successive actual ambient point blowups. The final
curve's generic multiplicity is one. Its blowup produces the precise
projectivized normal bundle, and balancing is performed away from it.
Meromorphic frames identify exactly its ruled birational class; no arbitrary
normal bundle is prescribed. The integral projective-bundle maps and the
coherent Leray maps compute all its groups. The hyperelliptic plane models
verify the genus and balancing formulas through50 without substituting
finite computation for the general adjunction proof.

The complete range of normalization birational classes is now settled:
UN35 gives exactly all nonnegative-Kodaira classes, UN37/41/42/43 realize
every Hopf surface, UN45 gives every ruled class, and UN15/19 exclude the
remaining general-type and class-VII alternatives. The only remaining
classification work is how whole supports fit together and which full
gluing data occur. The universal numerical decision criterion UN39 is
proved for every actual fibre but is kept distinct from a complete
analytic support-type or abstract-smoothability classification. D pursues
the complete diagonal-Hopf cycle branch; E pursues intrinsic data for
nonlinear-Hopf stars. The report remains INCOMPLETE for that whole-support
clause.
'''
(root/'records/root_research_all_components.md').write_text(record)
p=root/'S6_03_CDP_report.md'
s=p.read_text().replace('C.2.UN.1–38; A.5.18–21','C.2.UN.1–45; A.5.18–21')
needle='The remaining unresolved clause is the unrestricted geometric classification of all reducible zero-Euler supports;'
s=s.replace(needle,'UN39 supplies a universal resolution-based zero-Euler decision criterion. UN40 gives exact Hopf adjacency through all point blowups. UN41–43 settle occurrence of every remaining primary and secondary Hopf surface; UN45 realizes every ruled birational class. The normalization birational-class range is therefore complete. UN44 computes the exact meridian group and etale root cover, and bounds every resolved dual-complex group to be virtually abelian of rank at most two; without triple points its graph is a tree or one cycle. '+needle)
s+='''
## Complete normalization-component range and exact whole-support tests

UN37 and UN41–43 now realize every primary and secondary Hopf surface,
unchanged, in a compact zero-Euler torus fibre. The diagonal construction
plumbs two identical Hopf surfaces along both axes and identifies its
nearby lattice exactly. A compact elliptic-surface suspension retains that
punctured family. The nonlinear construction uses an explicit weighted
blowup, a uniformly controlled infinite quotient, and a free half-period
involution over P1. Its full central support is the prescribed Hopf plus
the specified smooth-multiple elliptic component. Every component and
support cohomology map is computed. The finite quotient construction
retains the exact given secondary surface, including all torsion characters.

UN45 constructs every ruled birational class by resolving the specified
curve's actual plane model inside a vertical exceptional plane, then
blowing up that curve and balancing away from the resulting ruled
component. Together with UN35 and the exclusions UN15/19, these results
complete the range of possible normalization birational classes.

UN39 is a necessary and sufficient geometric decision test for Euler
zero of every actual support: the sum of double-curve genera minus their
number, plus triple points and the exact resolution-centre correction,
must equal j(T)/2, where j(T) is explicitly0,4,6,or8 according to the
nineteen-row monodromy table. It eliminates every surface Euler term and
retains all multiplicities through the actual A'Campo comparison.

UN44 gives a further whole-support constraint. The exact meridian group
has an abelian image of Z4 of index the gcd of the full multiplicities;
the corresponding connected etale root cover and its integral group are
explicit. Every resolved dual-complex group is virtually abelian of rank
at most two. With no triple points its graph is a tree or a single cycle,
and a cycle forces monodromy eigenvalue1. These conclusions follow from
actual tube retractions, finite covering maps and specialization ring maps.

The range of components and the universal zero-Euler test are complete.
The exhaustive geometric assembly/realization classification of whole
reducible supports remains the outstanding clause; no abstract smoothing
claim has been inferred from the numerical test or the necessary group
and lattice constraints. The current follow-up addresses complete Hopf
cycle and Hopf-star branches. The report remains INCOMPLETE.
'''
p.write_text(s)
meta=root/'records/root_results.csv'
with meta.open(newline='') as f:rows=list(csv.DictReader(f));fields=list(rows[0])
for row in rows:
    if row['id']=='C.2.UN.45' and 'Independent D' not in row['notes']:
        row['notes']+=' Independent D full-source audit and executed-code check: PASS.'
with meta.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
print('Root full audits UN39,40,41,42,43,44: PASS; D full UN45 audit: PASS.')
print('All normalization birational classes settled; exact whole-support tests recorded.')
print('Report updated throughUN45; whole-support geometric classification remains INCOMPLETE.')
