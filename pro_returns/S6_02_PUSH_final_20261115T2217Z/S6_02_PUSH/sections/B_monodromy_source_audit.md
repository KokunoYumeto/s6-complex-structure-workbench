# Primary-source audit for B.4.17

Owner: boundary_d. 15 November 2026, 18:43 UTC.

## Exact access record

**Opened in full:** Honda, N., & Viaclovsky, J. (2025), *Some remarks
on fibrations in complex geometry*, arXiv:2504.14420v1 (19 April 2025).
Primary URL: <https://arxiv.org/pdf/2504.14420>.
The tool returned the explicitly versioned 19-page original PDF.
Relevant locations read: Theorem1.2 p.1; Theorem3.2 pp.8–9;
equations(3.3)–(3.9); Theorem3.5 p.10; Corollary3.7 p.11.
Retrieval references: turn449view0, turn450view0, turn451view0.

**Published metadata opened:** *Journal of Mathematical Study*, 58(4),
552–574, DOI <https://doi.org/10.4208/jms.v58n4.25.11>.
Publisher landing page:
<https://www.global-sci.com/jms/article/view/23902>.
The issue and author publication page independently match this metadata.
The publisher site lists 27 December 2025; the original PDF's front-page
excerpt lists online publication 15 December 2025. The bibliographic year,
volume, issue, pages and DOI agree, and no day-specific claim is needed.
References: turn452view0, turn452view1, turn453view0, turn454view0.

**Original published statement retrieved as a primary PDF excerpt:**
<https://www.global-sci.com/jms/article/download/23902/37287>.
The indexed original-PDF extraction identifies printed p.553, Theorem1.1,
and retains the same equality converse as the preprint. This was obtained
by the exact domain query for the phrase `Equality holds`; reference
turn453search0. It is sufficient to identify the published statement,
but it is not recorded as a full published-PDF read. Direct web-open of
the PDF URL redirected to the landing page; a standard urllib request
returned HTTP403. The publisher preview on ResearchGate contains only
the first printed page and was not used to infer the second page's theorem.

**Independent root check:** root subsequently opened the original
retrieval reference turn453search0 directly and used `find` for
Theorem1.1. Its independent retrievals turn476view0 and turn476view1
expose the original publisher PDF's printed pp.552–553, with the
equality converse at lines41–48. Root confirmed the published statement
from that two-page indexed original-PDF excerpt. The distinction from
a complete published-PDF read remains in force.

The main proof of B.4.17 is independent of this paper. It is a direct
compact-base realization of the fully checked Cartier cocycle in B.4.7.

## Logical issue and what remains valid

The proof gives

`b1(F0) <= dim H1(F)^T <= b1(F)`.

Trivial T gives equality in the right-hand inequality. It provides no
equality in the left-hand inequality when F0 is reducible. Our compact
principal-elliptic example has values `0 < 1 = 1`. No Kähler hypothesis
is imposed in the source theorem, and our compact smooth threefold
satisfies all its actual stated hypotheses.

The topological inequality itself and the forward implication from
equality of the endpoint Betti numbers to trivial monodromy are not
refuted. The irreducible-fibre Corollary3.7 is also unaffected: the relevant
top homology target has rank one and its fibre-class image is nonzero.
The exact compact counterexample has two components.

## Additional preprint issue, not needed for B.4.17

The version1 proof of Theorem3.5 also equates trivial monodromy around
every singular value with trivial global monodromy for an arbitrary
base curve. That implication fails for positive-genus bases. For example,
take elliptic curves E1,E2, a nonzero two-torsion point a in E1, and the
free involution `(x,y) -> (x+a,-y)` of E1 times E2. Its quotient is a smooth
projective surface fibred over E1/<a>, all fibres E2. Its Euler number is
zero, equal to the product of the two fibre/base Euler numbers, whereas
one global monodromy acts as minus identity on H1(E2). This separate
explicit example does not require any classification theorem. I have not
checked the complete published proof of Theorem3.5, and do not attribute
its precise proof wording to that unavailable full published version.

No claim of novelty is made for either elementary construction or the
underlying Cartier logarithmic-transformation method.
