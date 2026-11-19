"""Keep opening mechanisms explicit at the already reviewed proof scope.

This editorial pass changes no theorem or proof. Exact old/new text and the
corresponding lower-rung reasons are preserved in its receipt.
"""
from pathlib import Path
import hashlib
import json

OUT = Path(__file__).resolve().parents[1]
EDITS = []


def edit(paper, old, new, reason):
    EDITS.append({'paper': paper, 'old': old, 'new': new, 'reason': reason})


edit('I', r'''The six papers start from the compact complex six-spheres
constructed by Claude and L.~Alp\"oge and from Engel's elliptic-surface
description. In Paper~I, the theta transformation law and the integral
root norms determine the periods and moduli, while the corner meridians
and the Albanese nome obstruct extension at the two ends. In Paper~II,
the torsion term in the differential sequence identifies the missing
step in the cited vanishing argument and gives the exact replacement
criterion. In Paper~III, actual fibre framings and integral attaching
maps determine the homotopy classes and the resulting manifolds.
In Paper~IV, the full cusp charts, the tensor-frame return and the
relative Pontryagin calculation determine the smooth monodromy on
every retained fan; an explicit family gives a generator of $\Theta_7$.
In Paper~V, rank-six lattice data and their period extension give the
complex fourfold on $3\mathbb H\mathbb P^2\#(-\mathbb H\mathbb P^2)$.
In Paper~VI, normalization, local Milnor fibres and compact-stratum
cohomology give the Euler sign for all degenerations in its stated
torus-fibration class. Each numbered result below supplies the precise
scope and the morphisms used in these mechanisms.''',
r'''We start from the compact complex six-spheres constructed by Claude
and L.~Alp\"oge and Engel's elliptic-surface description: in Paper~I,
theta transformations and integral root norms determine the periods
and moduli, while corner meridians and the Albanese nome obstruct
extension at the two ends; in Paper~II, the torsion term in the
differential sequence identifies the missing vanishing step and gives
the exact replacement criterion; in Paper~III, actual fibre framings
and integral attaching maps determine the homotopy classes and
resulting manifolds. In Paper~IV, the full cusp charts, tensor-frame
return and relative Pontryagin calculation determine the smooth
monodromy on every retained fan, with an explicit family giving a
generator of $\Theta_7$; in Paper~V, rank-six lattice data and their
period extension give the complex fourfold on
$3\mathbb H\mathbb P^2\#(-\mathbb H\mathbb P^2)$; in Paper~VI,
normalization, local Milnor fibres and compact-stratum cohomology
give the Euler sign for all degenerations in its stated
torus-fibration class.''',
'Retain all six previously stated results and their exact mechanisms in the requested two-sentence series rung zero.')

edit('I', r'''On the null locus of $\psi(d,Jd)$ there is a dense set
of points with infinite monodromy stabilizer. On either nonzero
locus the stabilizer in the real parabolic is compact, and the
family period map embeds the $t$-line properly in the relevant
quotient (\ref{fam:src:F.2.2}, \ref{fam:src:F.2.3},
\ref{fam:src:F.3.1}).''',
r'''On the null locus of $\psi(d,Jd)$ there is a dense set of points
with infinite monodromy stabilizer, because the rational parabolic
conjugates of the explicit unipotent stabilizer are dense there.
On either nonzero locus the real parabolic stabilizer is compact,
and the family period map embeds the $t$-line properly in the
quotient: the modular quotient $j/1728$ is its left inverse and
controls the inverse images of compact sets
(\ref{fam:src:F.2.2}, \ref{fam:src:F.2.3}, \ref{fam:src:F.3.1}).''',
'The adjacent five-step proof gives the actual rational conjugation maps, homogeneous-space stabilizer and j/1728 left inverse.')

edit('I', r'''For the standard data,
$h^q(T_X)=(1,1,1,0)$, the Kuranishi germ is a smooth
one-dimensional germ, and $\operatorname{Aut}(X)=\C^*$.
These are credited results of DGKX version~1, re-derived
here through the root-curve Koszul complex and the integral
translation sheaf. The same root calculation gives
$(1,1,1,0)$ for every coprime $(3k,4l)$ sphere family
(\ref{fam:st:A.5.2}, \ref{fam:src:B.4.1},
\ref{push:src:E.2.1}).''',
r'''For the standard data, $h^q(T_X)=(1,1,1,0)$, the Kuranishi germ
is smooth of dimension one, and $\operatorname{Aut}(X)=\C^*$:
these credited results of DGKX version~1 are re-derived here through
the root-curve Koszul complex and the integral translation sheaf.
The same root calculation gives $(1,1,1,0)$ for every coprime
$(3k,4l)$ sphere family (\ref{fam:st:A.5.2},
\ref{fam:src:B.4.1}, \ref{push:src:E.2.1}).''',
'Retain the exact credit and re-derivation scope while using two sentences.')

edit('I', r'''No flat proper filling exists at $w=0$, after any
finite cover, for any admissible twist or any coprime
$(3k,4l)$ family. Commuting meridians propagate one ratio
along a connected corner fibre, while its two ends have
the incompatible values $0$ and $-p$
(\ref{push:src:B.4.33}, \ref{night:P2.7}, \ref{night:P2.9}).''',
r'''No flat proper filling exists at $w=0$, after any finite cover,
for any admissible twist or any coprime $(3k,4l)$ family.
The actual cusp deck map has $\gamma$-coefficient $-pn$;
commuting meridians propagate the corresponding ratio along the
connected corner fibre, whose two ends give $0$ and $-p\ne0$
(\ref{push:src:B.4.33}, \ref{night:P2.7}, \ref{night:P2.9}).''',
'The adjacent steps retain Delta_R F=an gamma-6an(n-1)d with a=-p and the exact commuting-meridian ratio equation; make the requested -pn corner coefficient visible at rung zero.')

edit('III', r'''The quotient of the regular family extends across the cusp
through the explicit target solid torus constructed in Paper~I.
Agreement outside the cusp alone leaves all twelve elements of
$\pi_6(S^3)$ available: pinching a small interior six-ball adds any
chosen element.  The target and collar conditions of the repaired map
specify the extension used in the subsequent calculations
(\cref{mapsI:src:A.2.1,maps:src:A.2.2}).''',
r'''The quotient of the regular family extends across the cusp through
the explicit target solid torus constructed in Paper~I, with the
target and collar conditions fixing the extension used here.
Agreement only on the exterior permits all twelve elements of
$\pi_6(S^3)$, because the relative pinch of an interior six-ball
adds any chosen element (\cref{mapsI:src:A.2.1,maps:src:A.2.2}).''',
'The full four-step lower rung constructs the relative pinch and the prescribed solid-torus extension; retain both exact scopes in two sentences.')

edit('III', r'''The prescribed degree-$N^2$ relative Kummer cover of the
cusp, for $N>1$, has no extension to a smooth finite cover of the
whole threefold.  Monodromy continues its marked lattice to one
whose primitive ray indices cannot occur in a smooth cover of the
entire periodic fan.  A finite flat normal completion exists and
is described separately (\cref{maps:src:C.1.1,maps:src:C.1.2,maps:src:C.1.3,maps:src:C.1.4,maps:src:C.1.5}).''',
r'''The prescribed degree-$N^2$ relative Kummer cover of the cusp,
for $N>1$, has no extension to a smooth finite cover of the whole
threefold, because its marked monodromy continuation has primitive
ray indices that violate the full-fan smoothness equations.
The explicit semidirect cover and its normal monomial completion
give the finite flat normal completion
(\cref{maps:src:C.1.1,maps:src:C.1.2,maps:src:C.1.3,maps:src:C.1.4,maps:src:C.1.5}).''',
'The five lower steps give both the primitive-ray obstruction and the semidirect-cover/monomial-completion construction; name each mechanism in two sentences.')

edit('III', r'''The natural-line construction has a complete marked sphere
classification on the twenty-one rank-one Mordell--Weil profiles:
$59$ sphere patterns on $50$ initial rows.  Twelve profiles have
unbounded sphere multiplicities, four have only logarithmic order
one, and five have no sphere output.  The integral refinements
identify the minimal simply connected nonspherical outputs and
the weight-$d$ Engel manifolds.  For OS49 the latest free-cap
calculation retains the extra torsion present outside the coprime
sector (\cref{maps:src:D.2.28,maps:src:D.2.44,maps:src:D.2.45,maps:src:D.2.46,maps:src:D.2.47,maps:src:D.2.48,night:P3F.34}).''',
r'''The primitive specialization lattices and actual normal-circle-torus
maps classify the marked natural-line sphere outputs on all
twenty-one rank-one Mordell--Weil profiles: $59$ patterns on $50$
initial rows, with twelve profiles of unbounded sphere multiplicity,
four of logarithmic order one and five with no sphere output.
Their integral cokernels and full characteristic evaluations also
identify the minimal simply connected nonspherical outputs and
weight-$d$ Engel manifolds, and the free OS49 Gysin lattice retains
the extra torsion outside the coprime sector
(\cref{maps:src:D.2.28,maps:src:D.2.44,maps:src:D.2.45,maps:src:D.2.46,maps:src:D.2.47,maps:src:D.2.48,night:P3F.34}).''',
'The seven-step lower rung gives the primitive specialization, actual boundary/Gysin maps, full finite-coefficient invariants and noncoprime OS49 Smith groups; expose these mechanisms without changing any count.')

edit('III', r'''Moving the zero of the line-bundle linearization gives a
proper analytic family with one ordinary double point.  Its two
smooth sides are the original six-sphere and $S^3\times S^3$;
the latter carries a complex structure with algebraic dimension
one (\cref{maps:src:D.3.1,maps:src:D.3.2,maps:src:D.3.3}).''',
r'''Moving the zero of the line-bundle linearization gives the local
equation $xy=u(zv-s)$ and a proper analytic family with one ordinary
double point. The actual replacement of $S^2\times D^4$ by
$D^3\times S^3$ and its primitive boundary maps identify its two
smooth sides as the original six-sphere and $S^3\times S^3$,
the latter with algebraic dimension one
(\cref{maps:src:D.3.1,maps:src:D.3.2,maps:src:D.3.3}).''',
'The full lower rung gives this exact collision equation, the actual surgery and primitive boundary maps before applying the known smooth classification.')

edit('III', r'''The transverse fibre product with the specified elliptic
surface, with its explicit small resolution, is a compact complex
fourfold with $K=\Pi^*L^{-5}$, algebraic dimension two, and
signature two.  Its degree-four intersection form is
$\langle1\rangle\oplus\langle1\rangle$; its Hodge data exclude
membership in Fujiki's class $\mathcal C$
(\cref{maps:src:E.1.2,maps:src:E.2.1}).''',
r'''The explicit crepant small resolution of the transverse elliptic
fibre product gives a compact complex fourfold with
$K=\Pi^*L^{-5}$ and algebraic dimension two; its Todd and
Pontryagin calculations give signature two and middle form
$\langle1\rangle\oplus\langle1\rangle$.
The computed values $b_1=0$ and $h^{0,1}=1$, preserved by a
K\"ahler modification, obstruct membership in Fujiki's class
$\mathcal C$ through the K\"ahler equality $b_1=2h^{0,1}$
(\cref{maps:src:E.1.2,maps:src:E.2.1}).''',
'The lower five steps give the actual small resolution, root canonical map, exact characteristic values and explicit modification-invariant obstruction.')


def main():
    receipt = {'scope': 'Opening wording and one-to-two-sentence presentation; all claims and maps already in the reviewed lower rungs; no new proof credit.', 'files': []}
    for paper in sorted(set(x['paper'] for x in EDITS)):
        path = OUT / 'papers' / paper / 'opening.tex'
        old = path.read_text()
        new = old
        applied = []
        for row in [x for x in EDITS if x['paper'] == paper]:
            assert new.count(row['old']) == 1, (paper, row['reason'])
            new = new.replace(row['old'], row['new'])
            applied.append(row)
        path.write_text(new)
        receipt['files'].append({'path': str(path.relative_to(OUT)),
                                  'old_sha256': hashlib.sha256(old.encode()).hexdigest(),
                                  'new_sha256': hashlib.sha256(new.encode()).hexdigest(),
                                  'edits': applied})
    dest = OUT / 'analysis/opening_mechanism_refinements.json'
    dest.write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps({'receipt': str(dest), 'edits': len(EDITS)}))


if __name__ == '__main__':
    main()
