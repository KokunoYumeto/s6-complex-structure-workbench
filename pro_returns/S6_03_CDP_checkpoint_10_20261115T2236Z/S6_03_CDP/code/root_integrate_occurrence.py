"""Record the completed equivariant occurrence proof and exact comparison maps."""
from pathlib import Path
from datetime import datetime, timezone

root = Path(__file__).resolve().parents[1]
stamp = datetime.now(timezone.utc).isoformat()
record = f'''# Exact component occurrence: root audit

UTC: {stamp}

The root has read the complete UN34 and UN35 constructions, the independent
rank-two torus H1 proof, and the executed exact-chart outputs. A separately
read both constructions and passed their full comparison maps. These results
settle occurrence of all nonnegative-Kodaira-dimension minimal normalization
classes. They do not assert a classification of all whole reducible supports.

## UN34: retaining the specified elliptic surface

The normalized multiple-root charts are connected by Stein factorization and
are etale over the smooth surface. Their finite inertia acts on the connected
central elliptic curve by a translation of the exact root order. Finite
averaging makes that translation constant in a local trivialization. The
canonical root-line sections give the actual lift to the root curve, retaining
the full original torsor cocycle, including its degree-zero parameters.

For a specified lattice basis lambda1,lambda2, the written homomorphism from
(C*)^2 to C/(Z lambda1+Z lambda2) has kernel the closed injective additive map
w -> (exp(2pi i lambda2 w),exp(-2pi i lambda1 w)). Its sheaf sequence is exact.
The root-curve additive H2 vanishes by finite averaging and the coarse curve.
Thus a pair of actual orbifold line bundles lifts the specified elliptic
torsor. Each line decomposes into an ordinary line and the stated root
characters; the remaining trivial-inertia line descends. Ordinary lines have
signed divisors avoiding the finite prohibited set by the stated RR argument.

The auxiliary blowups replace those exact divisor points by vertical
exceptional curves, with O(Tp)|B=O(p), including the canonical sections.
The root divisors extend the original root lines. Pushing this exact pair
through the same homomorphism retains the original torsor class, so the
selected component is the given surface, unchanged and of multiplicity one.
Every local inertia quotient is free through its exact-order elliptic
translation. The whole threefold is smooth and compact. Away from zero the
vertical canonical sections give an actual product of the fixed two-torus
and the punctured base. Every central component has Euler zero and every
double curve is elliptic; the auxiliary curve tree has no triple points.
Consequently the reduced support already has Euler zero. Root audit: PASS.

## UN35: retaining the specified cyclic action

The basis-free torus is (Lambda tensor C)/Lambda. The elliptic linear action
acts integrally on Lambda, hence by actual monomial transformations on this
torus; its one-dimensional additive kernel has the inverse elliptic
character. On the quotient orbicurve the resulting exact sheaf sequence has
an additive line-bundle kernel. Finite stabilizer averaging and the
one-dimensional coarse base give H2=0, so the original equivariant elliptic
torsor lifts with its full descent cocycle to the torus torsor.

Faithfulness on the base identifies the generic torsor with an actual
algebraic torus torsor over the invariant curve function field. The independent
H1 proof is complete: Riemann--Roch produces the C1 inequality, which gives
surjectivity of every finite field norm. The orders1,2,3,4,6 integral elliptic
lattices are identified with the displayed split, quadratic norm-one, cubic
norm-one and induced quadratic lattices. In order6 restriction to the
degree-two and degree-three intermediate extensions kills H1, and the
explicit transfer cocycle kills the original class by both2 and3. The
coprime relation then kills it. Every integral matrix and conjugating matrix
was checked exactly in A_equivariant_torus.py and its output. Hilbert90 is
applied only to the explicit multiplicative restrictions of scalars.

The independent primary check agrees: the root opened Steinberg's original
1965 Numdam PDF, printedp51, Theorem1.9. Its hypothesis is a perfect field of
cohomological dimension at most one and its conclusion applies to every
connected linear group. The C1 and norm argument here supplies the field
hypothesis as well as an independent proof for the exact tori being used.

The rational point gives an equivariant meromorphic frame of the actual
torsor. Its character divisors form an additive, equivariant homomorphism to
orbifold divisors. The identifications (Lchi,schi)=(O(Dchi),1) preserve both
tensor products and the cyclic action; there is no discarded scalar cocycle.
The auxiliary surface realizes the prescribed base action. For P1 this is
the exceptional coordinate z=x/t with the inverse normal character, exactly
as computed. Blowing up invariant point orbits and replacing each point
divisor by its exceptional divisor preserves the character-divisor map,
including at a double-curve node. The canonical sections therefore extend
the full torus action and the original equivariant torsor simultaneously.

Free root translations give a smooth compact threefold. Choices of root
lifts differ by precisely the inertia action and induce the same coarse
action. The canonical vertical sections trivialize the entire construction
off zero, so the remaining cyclic action there is exactly its given torus
linear action and a faithful normal rotation. The quotient has connected
general two-torus fibres, and its resolved distinguished component is
birational to the prescribed cyclic quotient. The previously proved
modification blocks balance Euler number without changing its minimal class.

Necessity follows from the actual cyclic component cover. The intrinsic
Iitaka, algebraic-reduction or Aut0-orbit pencil is preserved in its specified
case. For a bielliptic cover the Aut0-orbit pencil, not an arbitrary chosen
pencil, has base P1 and identity integral fibre monodromy. The subgroup acting
trivially on the base acts by fibre translations; a nontrivial fibre linear
part would give rational generic quotient and contradict the retained
nonnegative Kodaira dimension. Factoring this subgroup changes multiple
orders by the exact free-translation/reflection charts of UN33. The residual
base action is faithful, giving precisely the input just constructed.
The torus alternative is handled by the actual diagonal quotient of UN24.
Both directions are therefore proved with the specified comparison maps.
Root audit: PASS. Independent A full-source audit: PASS.

Executed certificates read by the root: E_equivariant_occurrence.out reports
233 point-to-exceptional divisor intertwinings and2375 faithful root-translation
charts, with all tests passed. A_equivariant_torus.out checks all five integral
actions, the exact norm-one lattices, the order6 restriction indices and the
quotient/kernel characters, with all tests passed. These are exact finite
checks of the displayed algebra; the written proofs handle all parameters.

## Remaining Hopf and gluing work; rejected routes retained

For a diagonal algebraic-dimension-zero Hopf contraction (alpha u,beta y),
the tentative ambient quotient with a reciprocal v-coordinate and map uv
has a nearby elliptic curve with normal flat line beta. That local model
cannot be placed in a two-torus when that line is nontrivial: the normal of
an elliptic subtorus translate in a two-torus is trivial. The proposed model
is therefore not used as a torus filling. The tentative Tate-family quotient
instead gives an elliptic ruled normalization (P1 times C*)/(alpha x,beta y),
as its exact central map shows. It does not give the desired Hopf component.
Plumbing axes with inverse flat normals supplies local data but currently
has no proved global smoothing comparison. An axis-deformation obstruction
is being checked separately. None of these exploratory routes is stated as
a theorem. A full whole-support gluing and realization classification is
still required by C.2.
'''
(root / 'records/root_research_occurrence.md').write_text(record)
p = root / 'S6_03_CDP_report.md'
s = p.read_text().replace('C.2.UN.1–33; A.5.18–21','C.2.UN.1–35; A.5.18–21')
needle = 'The remaining unresolved clause is the unrestricted geometric classification of all reducible zero-Euler supports;'
s = s.replace(needle, 'UN34 realizes every specified fixed-modulus, identity-monodromy elliptic quasibundle over P1 or an elliptic curve unchanged in a compact zero-Euler support. UN35 retains every specified cyclic action and gives an exact occurrence criterion for all nonnegative-Kodaira-dimension normalization classes. '+needle)
s += '''
## Exact occurrence of all components of nonnegative Kodaira dimension

UN34 realizes every specified identity-monodromy elliptic quasibundle with
fixed elliptic modulus, only smooth multiple fibres, and base P1 or an
elliptic curve. The component is unchanged and has multiplicity one. The
construction uses its actual torsor class, lifted to two root-curve line
bundles through a precise additive-kernel sequence, then extended through
vertical divisors on a compact auxiliary surface. Its reduced support already
has Euler number zero and its punctured family is the specified product.

UN35 retains the prescribed finite cyclic action. An equivariant meromorphic
torus frame gives exact character divisors; their blowup extensions preserve
the full action and all torsor gluing. This proves that the nonnegative-
Kodaira-dimension minimal normalization classes occurring in torus fibres
are exactly the nonnegative-Kodaira cyclic quotients of two-tori or of the
quasibundles just described. Every such class occurs in a compact zero-Euler
support. The generic torus-torsor vanishing is proved explicitly for all five
elliptic integral actions, independently checked against Steinberg's original
Theorem1.9. The exact construction certificates have233 divisor-action checks
and2375 free inertia charts, all passed.

These are necessary and sufficient component occurrence criteria. The
remaining main work is the Hopf component range and the compatibility and
realization of whole reducible supports. The earlier statements of partial
K3 and elliptic restrictions remain in the record and are sharpened by the
subsequent exact results. The report remains INCOMPLETE.
'''
p.write_text(s)
print('UN34 and UN35 full comparison-map audits: PASS.')
print('Exact torus H1 proof and all233+2375 construction certificates read: PASS.')
print('Report updated through UN35; whole-support classification remains INCOMPLETE.')
