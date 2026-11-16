"""Record full audits of UN49--54 and the inspected preceding PDF."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json

root = Path(__file__).resolve().parents[1]
stamp = datetime.now(timezone.utc).isoformat()
audit = '''# Whole-support branches through UN54

## Exact nonlinear stars and their full secondary characters

UN49 has full independent root, A and D source audits. The actual inverse
logarithmic transform retains the central analytic torsor, not only its
rational Chern data. Its determinant-one boundary matrix identifies every
Hopf core with the same ordinary elliptic fibre class. The canonical-order
and nonzero core-period calculation forces a common resonance. The compact
twistor lattice, weighted insertion, polynomial norm bound and closed-graph
replacement prove proper compact occurrence of every specified support.

UN50 has full independent root, A and D audits. The coarse maps
u=z^n, X=x z^k, p=X^r u^(-l), W=X^(-n)u^k, with rk-nl=1, are mutually
inverse on the actual punctured products. The primitive meridian is
r delta-n e; the full integer n is retained in the framing and Chern
vector. The root fibre character and the 1/n core-period factor agree.
The compact O(nR) insertion is free on its nonzero coarse line and has
the stated smooth quotient. Its stated multiplier is explicitly the
normal-line multiplier; the nonlinear higher terms are retained in the
actual contraction and in the smooth-pair comparison. Exact code checks
255 coprime cases.

## Mixed reduced cycles and arbitrary Hopf-cycle multiplicities

UN51 has full independent root and D source audits. Every rank-three
complement, affine edge map, actual smooth collar comparison and period
product is retained. The ruled component has a separate moving frame,
because its consecutive normal meridians coincide. Two Hopf normal
directions supply the independent constants for the compact comparison.
The all-ruled local criterion and its horizontal gluing translation are
included; compact globalization in that branch is not asserted in UN51.
Its 169 exact mixed-cycle examples and all-ruled affine comparison pass.

UN52 has full independent root, A and E source audits. The weighted
normal sections give actual smooth plumbing maps. The finite root neck
normalization uv=s^h, x=u^B, y=v^A is birational and normal with the
specified gcd data. Coordinate-power maps identify the strict covers
with the actual diagonal Hopf surfaces. The original normalization map
fixes the two marked axis branches, forcing oriented deck rotations.
This comparison precedes the proof Ru=u. The non-torsion degree-zero
line then forces R=I. The finite affine equations give u/N in the
actual integral lattice. Rational left-kernel relations and independence
of its three lattice generators prove holomorphic finite transport.
Two distinct edge orbits provide the needed independent normal constants.
The local invariant ring is exactly C{u^B,v^A}; it proves the quotient
smooth with the original multiplicities. The punctured translation torsor
has an actual holomorphic section, giving the compact I_q replacement.
The support is preserved, while the construction chooses normal-product
constants. Exact code checks 3456 root/inertia cases, 300 toric charts,
60 secondary indices and all three triangle equivariance maps. Compact
examples with multiplicities(1,n) and(1,2,2) are given independently.

## Arbitrary central surfaces in mixed Hopf stars

UN53 has full independent E and D source audits. Every primary and
secondary Hopf leaf is forced by the exact canonical character to the
specified resonant diagonal or nonlinear cyclic quotient. The scalar
two-line orbit has the non-descending minus-one logarithmic-form character.
An orbit of weight-r curves, including the axis z=0, is treated with
its full total weight mr; triangular permutations have not been omitted.
The central surface is minimal with pg1. Its multiplicity-one strict
root cover has degree one, so the proved component theorem applies to
the central surface itself. This forces the stated elliptic quasibundle
over an elliptic base and all boundary curves to be its fibres.

The exact inverse torsor has integral Chern vector zero. A common period
has order R: every nonlinear resonance equals R and every diagonal
resonance is smaller. When all leaves are diagonal the existence proof
chooses R larger than all their resonances without asserting a nonzero
period in an arbitrary prior smoothing. The weighted twistor maps
preserve s=xw, send p to p+d s^R, and give each prescribed leaf and the
entire central torsor. The properness and cluster comparisons retain
all marked elliptic gluing maps. Exact code checks15470 generic-curve
degree cases,50 axis divisibilities,40 weighted maps and315 finite
secondary period cases.

## Full reduced all-Hopf incidence and canonical minimum

UN54 has full independent root and A source audits. The additive
primary deck cocycle is pulled to the actual stabilizer F^d of a lifted
curve branch, becoming d. Its Laurent constant coefficient proves
restriction nonzero even when F permutes branches. Finite unramified
trace maps give the secondary comparison. The actual H1(O) matrix,
flat upper semicontinuity and the proved fundamental-group quotient
force one cycle and exact coherent holonomy one. The coherent dimensions
are(1,2,1). The transpose residue map identifies the unique dualizing
form, nonzero precisely on the cycle. The local xy=t adjunction
calculation identifies exactly those components with the minimum
canonical-evaluation order. In algebraic dimension zero the curve
counts force the whole graph to be a diagonal cycle, so UN46/48 give
the complete compact occurrence criterion for that entire branch.
Exact graph computations check35 cycle/tree cases and the branched
residue vector, plus the symbolic two-component holonomy determinant.

## Packaging continuity

The original checkpoint09, frozen at21:36:02UTC, exceeded the512MiB
upload limit. The upload error and both failed prepare attempts are
recorded. The same frozen snapshot was repackaged without changing any
current authored file or omitting any historical file version. All nine
original ZIPs were reconstructed and their exact byte hashes verified.
The saved compact package is209550608bytes, SHA256
03930e4fd1c785f477b217c8c7cd5597a1fe96228bfafbb7400cfa68f5bc4923,
with1704 distinct historical versions. Its save receipt succeeds.
Future hourly packages use the same lossless file-version method and
retain exact recipes for both the legacy and compact archives. No
earlier checkpoint is overwritten, renamed or deleted.

## Remaining main question

The unrestricted geometric assembly and realization classification of
reducible zero-Euler supports remains INCOMPLETE. The results above
complete additional entire specified support branches. Current work
addresses all-ruled compact cycles, weighted mixed cycles, and the
all-Hopf configurations with algebraic-dimension-one vertices and
attached trees. No classification of all unrestricted supports is
inferred from the completed component range or these branch criteria.
'''
(root / 'records/root_research_2211.md').write_text(
    f'Recorded at {stamp}.\n\n'+audit)
report = root / 'S6_03_CDP_report.md'
s = report.read_text().replace('C.2.UN.1–48; A.5.18–21',
                               'C.2.UN.1–54; A.5.18–21')
needle = 'The remaining unresolved clause is the unrestricted geometric classification of all reducible zero-Euler supports;'
addition = ('UN49/50 classify full nonlinear Hopf stars with every primary/secondary leaf. '
            'UN53 extends the exact criterion and compact realization to mixed diagonal/nonlinear Hopf stars with an arbitrary smooth central surface. '
            'UN51 gives the exact local mixed Hopf/ruled cycle criterion and compact occurrence with Hopf vertices. '
            'UN52 completes the weighted diagonal a0 Hopf cycle branch, with exact root/inertia maps and arbitrary original multiplicities. '
            'UN54 computes the actual all-Hopf coherent incidence map and canonical minimum and reduces the entire reduced a0 Hopf branch to the completed cycle criterion. ')
s=s.replace(needle,addition+needle)
s+='\n'+audit
report.write_text(s)

p=root/'records/root_results.csv'
with p.open(newline='') as f:
    reader=csv.DictReader(f)
    fields=reader.fieldnames
    rows=list(reader)
for row in rows:
    if row['id']=='C.2.UN.53':
        row['notes']=row['notes'].replace('Full independent audit requested; exact code completed.',
            'Exact code completed. E and D independently read the complete source and passed every canonical character, root-cover degree, core period and compact weighted comparison. D\'s weight-r orbit wording precision is incorporated explicitly.')
with p.open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields)
    writer.writeheader();writer.writerows(rows)

with (root/'records/visual_qa.md').open('a') as f:
    f.write(f'\n## Root actual visual inspection at {stamp}\n\n'
            'The367-page203-statement PDF from root_build_2146.out was rendered '
            'and root opened current pages222,225,266. These cover the exact '
            'primary boundary matrix, twistor period frame and weighted map, '
            'and the secondary coarse inverse and primitive boundary matrix. '
            'All text and formulas fit with no clipping or overlap. The build '
            'had four successful passes and zero errors, overflows, undefined '
            'references or missing glyphs.\n'
            'The first207-statement build (root_build_2210.out, filename label '
            'chosen before its actual finish) exposed sixteen TeX errors '
            'caused solely by unbraced math-letter macro subscripts in UN51/52. '
            'All six source subscripts were braced. The replacement build '
            'root_build_2209.out completes all four passes with zero errors, '
            'overflows, unresolved references and missing glyphs. Actual '
            'inspection of that new PDF is recorded separately after rendering.\n')
print(json.dumps({'utc':stamp,'full_audits':'UN49–54',
                  'report_status':'INCOMPLETE','completed_branches_integrated':6},indent=2))
