"""Record the complete Hopf-cycle and finite-cover support audits."""
from pathlib import Path
from datetime import datetime, timezone

root = Path(__file__).resolve().parents[1]
stamp = datetime.now(timezone.utc).isoformat()
record = f'''# Whole-support gluing and finite-cover audit

UTC: {stamp}

UN46: root read every line of the full proof. The actual a0 Hopf curve
list and UN40 make the SNC incidence graph a cycle. For primary and
secondary diagonal Hopf surfaces, deleting the other axis gives the
entire normal line bundle, not just a formal neighbourhood. Its finite
diagonal quotient remains a line bundle because the base action is free.
The full inverse-image lattice under exponentiation is discrete of rank
three and spans the complex two-space. A base elliptic isomorphism lifts
affinely; the derivative of the logarithm of the normal multiplier is
elliptic-periodic, hence constant. This proves the stated affine edge
matrix and its exact integral lattice map.

Compatible flat metrics give bounded necks and disjoint open overlaps.
The relative closedness of their graphs, and the nested compact cores
and closed smaller necks, prove Hausdorffness and properness of the finite
plumbing. Each core and neck retracts onto the specified three-torus;
the actual collar inclusions induce its full rank-three group. Van Kampen
therefore gives the injected semidirect-product presentation.

For an arbitrary actual smoothing, the canonical branch divisor sections,
a smooth base retraction and product-preserving line-bundle identifications
give a genuine tubular diffeomorphism with f=xy. Its radial isotopy fixes
the induced collar group maps. Thus the same group calculation applies
to that actual smoothing. Its torus group forces identity cycle product.
Conversely the explicit plumbing with identity product has a global closed
holomorphic coframe; the dual complete commuting fields give the exact
transitive C2 quotient and all periods, including the cycle translation.
No assertion of holomorphic normal linearization for an arbitrary given
smoothing is inserted.

For two components, exact multiplication of the two matrices forces both
to be minus coordinate exchange. Equality of the entire exponential
preimage lattices identifies the complete primary/secondary deck groups.
The two actual diagonal automorphisms remove both elliptic translation
constants. UN41/43 therefore realize the entire prescribed reduced support
compactly. The general-cycle part at this stage gives an exact local
plumbing and necessary condition for any actual smoothing. Its compact
globalization is being written separately as UN48 and is not assumed here.
Root full-source audit: PASS. Independent A full-source audit: PASS.

UN47: root read every line, including the later chiO1 restriction.
Every finite quotient of the actual support group gives a connected finite
etale complex cover of the whole small tube. The punctured cover is
connected because its group map is onto. Its Stein base is the normal
completion of a cyclic punctured-disc cover, so has exactly one point
over zero and coordinate t=s^a. Its connected nearby fibres are actual
finite etale covers of a two-torus. Thus UN28 applies to the whole covered
central support.

The actual pullback of a chosen normalization resolution has exactly
[Q:H_Q] connected components, each of degree |H_Q|. Removing proper
analytic curves leaves each connected; the dense-open base-change
isomorphism proves that these are resolutions of distinct normalization
components, retaining every degree. Pullback of a nonzero holomorphic
two-form then forces H_Q=Q. The written finite-index abelian subgroup
argument proves subgroup separability directly and retains the actual
component image, hence gives surjectivity on the whole support group.
Common point blowups identify this image with that of every resolved
strict-transform vertex. Its surjectivity kills the whole dual-complex
group. K3 and chiO2 components force the support group trivial.

For chiO1, etale Riemann--Roch gives the exact inequality
1 >= N-N/e. A detected nontrivial component image requires N=e=2.
Residual finiteness and a product quotient then force the entire support
group to be Z/2. The induced connected double cover has chi2,pg1,q0.
Two different chi1 components with nontrivial image would violate UN28
in that same cover. These arguments work for arbitrary finite quotient
order and do not replace the proof by bounded enumeration.
Root full-source audit: PASS. Independent D full-source audit: PASS.

The latest compiled manuscript contains200 numbered statements and356
pages throughUN47. build/root_build_2120.out records four successful
passes, zero TeX errors, zero overfull boxes, zero unresolved references
and zero missing glyphs. Its filename is only a run label; its actual
start was21:17UTC. The preceding failed build had one14.71288pt overflow
in C.HC.2, repaired in the source by shortening the display text. The
earlier8.02008pt Tate-series display was split in C.DH.14a. All earlier
logs are retained. Root actually inspected current pages98,131,167,180,
215,252, including both repaired displays, the cover inequality, exact
root cover, weighted nonlinear bound and secondary finite quotient.
All text and equations on those images are within the page boundaries.

The remaining task remains the unrestricted whole-support geometric
assembly/realization classification. Current work attacks general compact
Hopf cycles and the exact inverse-log-transform criterion for nonlinear
Hopf stars. These are direct branches of that task. No statement of
completion is inferred from the full component range or numerical zero
test alone.
'''
(root / 'records/root_research_support_groups.md').write_text(record)
p = root / 'S6_03_CDP_report.md'
s = p.read_text().replace('C.2.UN.1–45; A.5.18–21',
                         'C.2.UN.1–47; A.5.18–21')
needle = 'The remaining unresolved clause is the unrestricted geometric classification of all reducible zero-Euler supports;'
s = s.replace(needle,
    'UN46 gives the exact local lattice criterion for all unblown diagonal Hopf cycles and the complete compact two-component support classification. UN47 proves that every pg1 normalization component surjects onto the support group; K3 or chiO2 components force that group trivial, and chiO1 component images vanish except for the specified whole-group Z/2 case. '
    + needle)
s += '''
## Exact Hopf-cycle and finite-cover support constraints

UN46 computes every diagonal Hopf cycle transition from the actual elliptic
gluing and dual-normal isomorphisms. The cycle product on the integral
rank-three complement lattice is the exact torus criterion for the finite
proper local plumbing. The actual smooth tubular comparison proves its
necessity for every given smoothing in this branch. For two components,
the entire reduced support consists of two copies of the same primary or
secondary diagonal Hopf surface, with both elliptic curves joined by
inversion; the compact constructions UN41/43 realize every such support.
General-cycle compact globalization is being developed separately.

UN47 links each component to the whole support through every finite etale
tube cover and its exact Stein disc. A positive geometric genus component
has pg1 and surjects onto the support fundamental group. Every resolved
dual complex is then simply connected. A K3 component, or any component
with chiO2, makes the whole support simply connected. A chiO1 component
has trivial image except for the exact possible whole-group Z/2
configuration; at most one chiO1 component can surject in that case.
Both proofs have complete root and independent agent audits.

The clean manuscript now has200 statements and356 pages throughUN47.
The preceding14.71288pt Hopf-cycle display overflow was repaired; the
earlier8.02008pt Tate display was also repaired. The final build has zero
errors, overfull boxes, unresolved references and missing glyphs. Root
actually inspected pages98,131,167,180,215,252 of this current rendering,
including the repaired displays and the main new comparison formulas.
The complete assembly/realization classification remains INCOMPLETE.
'''
p.write_text(s)
with (root / 'records/visual_qa.md').open('a') as f:
    f.write(f'\n## Root inspection at {stamp}\n\n'
            'Current356-page200-statement PDF throughUN47: all four passes '
            'successful; zero errors, overflows, undefined references or '
            'missing glyphs. Previous overflows8.02008pt and14.71288pt '
            'were repaired in C.DH.14a and C.HC.2. Root opened and visually '
            'inspected current pages98,131,167,180,215,252; formulas, text '
            'and page boundaries are readable with no clipping or overlap.\n')
print('Full UN46/47 audits and report throughUN47 recorded.')
print('Current clean cutoff:200 statements,356 pages; six actual QA pages.')
