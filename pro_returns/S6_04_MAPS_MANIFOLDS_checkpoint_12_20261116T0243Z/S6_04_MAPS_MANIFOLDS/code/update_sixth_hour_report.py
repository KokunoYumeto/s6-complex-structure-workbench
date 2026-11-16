"""Update current scope after the independently audited sixth-hour advances."""
from pathlib import Path

root=Path(__file__).resolve().parents[1]
p=root/'S6_04_MAPS_MANIFOLDS_report.md'
s=p.read_text()
lines=s.splitlines()
for i,line in enumerate(lines):
 if line.startswith('| B.5 |'):
  lines[i]='| B.5 | B.5.1–B.5.2 | (a): explicit topological CW attachment maps and integral homotopy-sphere computation; B.6.19 and B.6.25 supply the parametrized spin trace and a spin filling |'
 elif line.startswith('| B.6 |'):
  lines[i]='| B.6 | B.6.1–B.6.25 | (a)/(b): every requested monodromy class is zero in Θ7, including every admissible higher fixed-data sphere pair; the marked ordinary scalar-shear isotopy is refuted, the actual fixed-circle quotient and spin trace are computed, and the K7 residue is0 |'
 elif line.startswith('| D.2 |'):
  lines[i]=line.replace('D.2.20','D.2.21').replace('remaining choices and smooth classifications are not exhausted','five further mixed original/log families are classified at all allowed orders; remaining choices and smooth classifications are not exhausted')
 elif line.startswith('| F.2 |'):
  lines[i]=line.replace('F.2.23','F.2.24').replace('exhaustive integral affine classification remains','the entire explicit unbounded family now has its complete survivor list across all lattices, multiplicities and twists; the full integral affine classification remains')
s='\n'.join(lines)+'\n'
s=s.replace("Lead8's ordinary scalar-shear assertion is refuted, while its checked twist and symmetry assertions remain separated from the uncomputed Θ7 value.","Lead8's ordinary scalar-shear assertion is refuted. The actual numerical Θ7 value is now computed as zero for every requested sphere family, using the marked fixed-circle replacement and parametrized spin trace.")
old='For B.6, scalar logarithms cannot be patched by treating fractional lattice translations as global gauges. The even-shift maps now extend across the conifold smoothing, whose monodromy acts identically on H3. The normal-framing calculation in B.6.4 reduces that mapping class further to the central Θ7 subgroup. The reverse surgery trace now proves equality of the original and smoothed central classes. The argument extends to every sphere family X_(3k,4l), with h=2kl; their numerical residues remain uncomputed. A moving-zero braid calculation gives exact actions on parabolic cohomology, but affine-sheet continuation and the change of marked linearization degree prevent identifying its word with the smooth scale monodromy.'
new='B.6 is settled by B.6.16–B.6.25. For multiplicities (3k,4l), the actual fixed-circle replacement has quotient invariants k_cup=−kl and ell=−4kl. The integral change of lifted parameter generator removes the cusp power by an actual long-period deck transformation before the deformation. The collar cup calculation retains all finite and nodal markings. The parametrized spin trace has p1 coefficient ell−2k_cup=2k_cup and rank-one form (k_cup); its sign is forced by the marked boundary linking form, with the order-one and order-two cases handled separately. Its correction equals the free-circle disc invariant, so the original mapping-torus invariant and every requested Θ7 class are zero. The earlier fractional scalar-gauge and direct one-component filling routes remain recorded as failed approaches, and neither is used in this computation.'
s=s.replace(old,new)
header='## Sixth-hour independently checked advances'
if header not in s:
 s+='''\n\n## Sixth-hour independently checked advances

B.6.22–B.6.25 complete B.6 for every admissible coprime pair (3k,4l) and every fixed twist datum. The positive parameter generator is2kl, the complex orientation is retained, and the generator of Θ7 has Eells–Kuiper invariant1/28. The answer is zero. The boundary linking comparison uses the same primitive degree-four class on the disc bundle and the actual surgery trace, so it determines the trace sign whenever the torsion order exceeds two. At order two the opposite sign would give invariant±1/112, outside the mapping-torus range (1/28)Z/Z; at order one both possible corrections are zero. The resulting zero class also supplies a spin filling D7×S1 with one zero-handle and one one-handle and with p1-square and signature both zero. That filling is explicitly a consequence of the preceding calculation, not its premise. Root and both topology agents independently checked the higher computation; its symbolic code was rerun exactly.

D.2.21 proves five additional families in which one additive filling is retained and the other is replaced by a finite-good logarithmic cap. For every allowed multiplicity and twist its group is Z/|n| and its middle free ranks are b,2b with b=1,6,5,7,7 in the five displayed rows. All simply connected members are #b(S2×S4)#b(S3×S3), so none is a six-sphere. The symbolic remaining two-row presentation is unimodular for all admissible integers; root additionally reran1068 complete Smith matrices. This is an all-parameter theorem for the five stated rows, not an exhaustive D.2 classification.

F.2.24 completes the survivor classification for the whole unbounded rational family introduced in F.2.16. Across every stable lattice, actual finite multiplicity and affine twist, the only survivors are the two rational parameters v=0,1 in their unique eligible integral classes, with exact multiplicities5,4 and20κ+4r1+5r2=±1. Every vertical twist is removed by an actual cap translation whose obstruction vanishes in the full integral relative group H2(P,∂P;Λ)=ΛΓ=Z. The cusp marking is held fixed during that step. The remaining numerator changes are removed precisely by the determinant relation; fibre inversion preserves the Kuhn fan and total orientation. All resulting manifolds have the already identified smooth type3HP2#(−HP2). Other rational points and other surviving spectral loci remain in F.2's open scope.

These independent proof checks and exact reruns are recorded in records/root_audit_checkpoint06_progress.json. Current unresolved prompt items are D.2, E.2 and F.2. Historical checkpoint narratives below and in topic records retain the state at the time they were written; the opening table and this section supersede their former open-status claims.
'''
p.write_text(s)
print('Updated current B.5/B.6/D.2/F.2 scope; retained historical records.')
