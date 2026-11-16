"""Record root audits of UN16 and UN18--21 and the remaining occurrence problem."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json

root = Path(__file__).resolve().parents[1]
stamp = datetime.now(timezone.utc).isoformat()
path = root / 'records/root_results.csv'
with path.open(newline='') as handle:
    reader = csv.DictReader(handle)
    fields = reader.fieldnames
    rows = list(reader)
for row in rows:
    if row['id'] == 'C.2.UN.12':
        row['depends_on'] = ('C.2.UN.5; C.2.UN.7; C.2.UN.19; C.2.VII.1-4; '
                             'A.5.17; exact normalization-complement isomorphism')
        row['notes'] = ('Normal supports are tori or bielliptic; noncontracted irrational ruled '
                        'supports have the four constant elliptic conductor types; rational and '
                        'contracted irrational cases have e>=2. The remaining branch has Hopf '
                        'minimal normalization by UN19, with b2(Z)=r and the exact conductor '
                        'branch patterns. A5.17 removes both old exceptional terms outside '
                        'the conductor. This classifies actual irreducible fibres without '
                        'asserting smoothability of arbitrary abstract gluings.')
with path.open('w', newline='') as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

(root / 'records/root_research_component_descent.md').write_text(f'''# Component fields, exact finite descent and new occurrence examples

UTC: {stamp}

## Root proof audits

UN16: PASS. The adjugate bound M subset L subset s^(-d)M proves finite generation of the saturated relative-translation lattice over C{{s}}. The restriction kernel is exactly sL because the selected component has multiplicity one. Thus the two-dimensional residue space injects into the meromorphic vector fields on the actual component, even when its pointwise rank is one. The ratio in that rank-one branch is a nonconstant meromorphic first integral; equivariant resolution and Stein factorization give the compact fibration. The one-dimensional time-primitive argument excludes poles of the restricted semicomplete field on a general compact fibre. Algebraic dimension zero is preserved under the actual generically finite cover by the symmetric-function field argument. Guillot's theorem, the unique minimal model, and the verified vector-field bounds leave torus or Hopf minimal cover in that case. The root opened and checked the DOT2000 bound in its original journal scan.

UN18: PASS. The two opposite root charts x=a^m b and their dual charts are smooth, the q action is free and proper, and the punctured comparison is the displayed product map. The actual cyclic curve followed by the torsion-trivializing cover gives the finite etale map from a product of two curves to P_m. Its Jacobians at both types of branch point are units. The canonical calculation gives K=(m-1)(J_++J_-), the stated plurigenera, and Kodaira dimension one. The integral M3 and M5 gluing maps have the primitive images claimed; their signs in the negative root chart are retained. The support Mayer--Vietoris maps, the global deck cocycle, and the finite etale projectivity comparison justify every displayed integral and coherent group. A independently audited the full construction. This is an actual projective properly elliptic essential component in a fixed punctured product filling of reduced Euler number zero.

UN19: PASS. The targeted cyclic root has an actual generic torsor, and the stabilizer quotient of a selected component is bimeromorphic to the original normalization. Equivariant resolution and the unique minimal contraction preserve that quotient comparison. A torus minimal cover has even invariant first Betti number, and cyclic quotient resolution does not change H1. On a Hopf cover, log absolute derivative determinant fixes H1; holomorphic finite-order automorphisms consequently have Lefschetz number zero. Fixed curves have genus one and zero Euler number, so there are no isolated fixed points. Cyclic stabilizers are pseudoreflections, and the quotient is smooth. Its b1=1, b2=0, Kodaira dimension -infinity and actual elliptic curve identify it as Hopf by the previously checked surface criterion. Therefore every original classVII component has Hopf minimal model. D and E independently audited this proof. The earlier positive-b2 GSS conclusion of UN17 is retained as a valid necessary reduction and is now excluded by the stronger two-field descent.

UN20: PASS. The cyclic stabilizer acts semilinearly on the relative lattice, preserves its valuation and sL, and acts complex linearly on the residue space. The exact coefficient comparison is h composed with g inverse = (c+dh)/(a+bh). Equivariant graph resolution and the unique Stein factor give the actual base action. A general fibre of the quotient is F/K, where K is the kernel on the base. At its points the stabilizer fixes the base coordinate and acts by a pseudoreflection on the smooth surface, so resolution leaves this general fibre unchanged. The resulting base is already the Stein base because the general fibre is connected. The prior generic torsor identifies the quotient with the original normalization. Nonnegative Kodaira dimension excludes rational general fibre by restricting pluricanonical sections to O_P1(-2m). E independently audited all these steps.

UN21: PASS. The lift preserving the canonical section has eigenvalues plus or minus one at every fixed base point, so multiplying it by q^(1/2) gives a free involution on the elliptic line-bundle quotient. The exact full fibres are 2P+2Q and 2B. The derivative -I at the blown-up centre gives the Hopf contraction -q^(1/2). The canonical-form character on P has exact order two. The invariant unit-circle metric identifies the compact quotient and the component as actual mapping tori. Two lifted invariant base cycles and two circle preimages of anti-invariant elliptic loops give an integral diagonal basis for H2(M5), avoiding any unproved integral splitting. Wang and universal coefficients give the stated (Z/2)^2 torsion. The doubled-fibre calculation keeps the nilpotent coordinate: an eigenframe e of sign plus or minus contributes the invariant e or t e in C[t]/(t^2)e. Each full scheme therefore has h(O)=(1,2,1). Normalization of the actual quadratic fibre product recovers the primary Kodaira cover. The root supplied, and E independently verified, an invariant Seifert surface for the angular fibre over zero; its mapping torus bounds J and fixes the integral support torsion map.

## Current unresolved scope and attempts

The sole unfinished requested clause is the exhaustive geometric classification of unrestricted reducible zero-Euler supports. UN14 transfers all essential-component occurrence questions exactly to every even Euler value. UN15 excludes general type; UN19 excludes every classVII minimal model except Hopf. Explicit essential examples now include primary and secondary Kodaira, Hopf, projective and nonprojective properly elliptic, and Kummer K3 components. These results do not classify all possible K3 or elliptic components or their interface and smoothing data.

The root attempted an Enriques component through the usual free involution on a Kummer surface. On E1 times E2 it is induced by (-x+a,y+b), with nonzero two-torsion a and b, together with the Kummer involution. The torus group is noncyclic. Acting by that involution fibrewise changes the generic fibre to a bielliptic surface. To combine it with the required half-turn on the Kummer-family base would require a torus lift squaring to -I; the displayed linear part squares to I. Thus this exact proposed construction does not produce a torus fibration. No general Enriques exclusion follows from this failed construction. E is now examining the exact cyclic torus quotient obstruction.

A second attempt starts with a rational elliptic surface produced by nine point blowups of a vertical plane component and seeks logarithmic transforms giving an Enriques surface. No elliptic pencil on an ambient neighbourhood has been constructed. The existing pencil on the single component supplies no ambient surgery map, so this is not a construction.

The rank-two commuting fields have a joint maximal local action on their holomorphic locus, by the checked local-flow result. A Hausdorff compact globalization with a comparison to the given filling has not been proved, so no global action classification is used. A and D are developing a direct period calculation instead. The proposed stronger bound kappa<=0 in the elliptic branch was withdrawn: a fibre translation can compensate cyclic-root time monodromy at a multiple smooth elliptic fibre. The retained claim under audit concerns chi(O)=0 and the exact singular-fibre list.

The root also considered lifting the periods of a compact rank-one orbit to periods of the nearby tori. A compact central orbit need not deform as a compact curve, and no period-lifting morphism has been constructed. Consequently neither isotriviality nor a K3 exclusion is inferred in the rank-one branch. UN20's descended rational/elliptic fibration is the proved statement.
''')

path = root / 'S6_03_CDP_report.md'
report = path.read_text()
report = report.replace('C.2.UN.1–15,17; A.5.18–21', 'C.2.UN.1–21; A.5.18–21')
report = report.replace('exact class VII equality data', 'exact Hopf-minimal equality data')
report = report.replace('Universal zero-Euler refinements and essential Kodaira, Hopf, properly elliptic and Kummer K3 components are constructed.',
                        'Universal zero-Euler refinements and essential primary/secondary Kodaira, Hopf, projective/nonprojective properly elliptic and Kummer K3 components are constructed. General-type components are excluded, every class VII component has Hopf minimal model, and the rank-one translation fibration descends to the original normalization.')
marker = '## Two translation fields, cyclic descent and further essential components'
if marker not in report:
    report += '''
## Two translation fields, cyclic descent and further essential components

C.2.UN.16 retains both torus translation fields on the actual multiplicity-one component cover by a finite saturated lattice over C{s}. Its residue is a two-dimensional space of commuting semicomplete meromorphic fields. Rank one gives a rational or elliptic fibration. In algebraic dimension zero, the cover's minimal model is a torus or a Hopf surface. C.2.UN.20 descends that rank-one fibration through the actual cyclic stabilizer quotient to the original normalization, with its exact connected generic fibre and base. No replacement of a quotient by an unspecified cover is made.

C.2.UN.19 proves that every class VII original normalization has Hopf minimal model. The torus-cover alternative is excluded by invariant first cohomology. The Hopf-cover alternative has a smooth cyclic quotient: Lefschetz and adjunction exclude isolated fixed points, leaving pseudoreflection stabilizers. The quotient invariants and its actual elliptic curve identify it as Hopf. UN12's complete irreducible zero criterion has been updated accordingly. The positive-b2 necessary GSS restriction in UN17 is now superseded by this exclusion, while its independent canonical-support identity remains valid.

C.2.UN.18 realizes projective properly elliptic essential components in zero-Euler fillings of a fixed punctured product. The product cover is finite etale, its branch-chart Jacobians are explicit, and the canonical bundle and all integral and coherent cohomology groups are computed. C.2.UN.21 realizes a secondary Kodaira essential component by a free half-period involution. Its special full fibres are 2P+2Q and 2B, with P secondary Kodaira, Q primary Hopf and B bielliptic. The integral torsion is determined through actual mapping tori, and the nilpotent-direction character gives h(O)=(1,2,1) for each full fibre despite h(O)=(1,1,0) on its reduction.

The remaining occurrence questions include the exact K3 and Enriques possibilities and the interface, multiplicity and analytic smoothing conditions for unrestricted reducible supports. The attempted Kummer-to-Enriques quotient and component-only logarithmic transform are recorded with their missing comparison maps. A direct rank-two period argument is in progress; its proposed stronger Kodaira-dimension bound was withdrawn after an explicit multiple-fibre calculation. The report remains INCOMPLETE for C.2 alone.
'''
path.write_text(report)

path = root / 'code/render_qa.py'
source = path.read_text()
source = source.replace("'C.2.UN.17', 'C.2.UN.18', 'C.2.UN.19',", "'C.2.UN.17', 'C.2.UN.18', 'C.2.UN.19',\n         'C.2.UN.20', 'C.2.UN.21', 'C.2.UN.22', 'C.2.UN.23',")
path.write_text(source)
print(json.dumps({'utc': stamp, 'accepted': ['C.2.UN.16', 'C.2.UN.18', 'C.2.UN.19', 'C.2.UN.20', 'C.2.UN.21'],
                  'updated': ['UN12 Hopf minimal branch', 'C2 report', 'root audit record', 'visual QA terms']}, indent=2))
