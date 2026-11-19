# Fresh reviews of F.3.8 and C.2.UN.5

19 November 2026, GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro.

## Paper V: maps:src:F.3.8

The complete derivation in `D3_spanning_tube_before_read.md` was written
before the printed proof was opened. It supplies a uniform spanning
tube through a base-point-free Pluecker extension across the compact
projective closures of nine lines. Every point is reached by the actual
oriented real change-of-basis action. The construction proves the full
stated tube domination and applies the opened LSAP/Oka-1 criterion.

The printed four-step proof was then read in full. It uses real graph
coordinates and a different explicit nine-matrix basis, whose transverse
singular values have a uniform lower bound. The coordinate morphism
between the two arguments is explicit: in C6=E plus conjugate(E), with
E={(iv,v)}, a graph y=W x becomes the real-coordinate graph

    Z=i(I-W)(I+W)^{-1},
    W=(Z+iI)^{-1}(iI-Z)

on their common chart. Both maps extend as the same planes in the
Grassmannian; the compact-closure argument uses its Pluecker embedding
where a graph chart changes. Thus both arguments dominate the specified
component of the same domain.

`D3_tube_fresh.py` was first written before the target proof and gives
nine independent directions with determinant -27i/4, each rank two and
each with complementary conjugate infinite limit. After the printed
proof was opened, the same fresh program was extended to compare all
its displayed arithmetic, without reading its producing program. It
reproduces determinant -16, the exact completed-square identity and
the bounds 1/2 or 1/3 for the six transverse squared singular values.
The printed perturbation radius 1/4 is below 1/sqrt(3), so the actual
normal-operator perturbation preserves invertibility for every complex
line parameter. The printed proof has no remaining tube-thickness gap.

Known input opened in the supplied arXiv:2303.15855v5 text: Definition
2.1 p.4, Theorem 2.2 p.5, and the paragraph before Proposition 7.13,
parts(a),(b), p.23, continuing on p.24. The attempted direct web opening
of the exact v5 PDF returned DisabledError; no successful web-PDF
reading is claimed by that request. The actual supplied exact-edition
text was read and matches the definitions used above.

## Paper VI: cdp:st:C.2.UN.5

`UN5_before_read.md` was written from the statement-only packet before
this checker opened any of the target proof. The full seven-step proof
was subsequently read. Every step matches the prereading derivation:
the isolated vanishing-sphere exclusion, the normalized cyclic base
change and its connected central fibre, the actual degree-one Albanese
map, the affine deck action and its eigenvalues, canonical-order
divisibility, the diagonal compact quotient, and primitive lifts of the
Albanese character for every allowed multiplicity.

The receiving proof's positive-area argument excludes contracted curves
directly using the H2 pullback isomorphism; the prereading derivation
used the equivalent surface exceptional-curve obstruction. Both concern
the same period-integration Albanese morphism. The unit-root charts
identify the actual degree-m unramified cover, and the character-kernel
inclusion identifies its factorization through the canonical torus cover.

Primary PDFs opened: Buchdahl, *On compact Kaehler surfaces*, Theorem11,
published p.297 (PDF page12 with cover), giving the metric for even b1;
Catanese, arXiv:math/0111245v2, Definition3.1 and Theorems3.2–3.3 on
p.9, including all seven finite product presentations, and Theorem4.6
on p.13 with proof on p.14. In particular, the quoted presentation makes
the canonical character factor through the elliptic Albanese base.

`UN5_characters_fresh.py` is new code using exact CRT lifts. It checks
all 47 surjective residue characters for orders 2,3,4,6, obtaining in
every case an integral pair of gcd one. That exact gcd gives a surjection
modulo every multiple m, without extrapolating a finite test in m. The
five possible integral traces of a finite elliptic unit give exactly
orders 2,3,4,6,1 by exact matrix powers. No producing code was read or
reused. The full prereading and computation gates for this row are
closed; its paper owner retains the remaining credit/source accounting.
