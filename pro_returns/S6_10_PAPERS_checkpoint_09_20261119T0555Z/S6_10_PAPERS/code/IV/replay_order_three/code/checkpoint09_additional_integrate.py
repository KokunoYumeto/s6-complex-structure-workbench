"""Integrate the remaining audited cap and common-exterior statements."""
from pathlib import Path
from datetime import datetime,timezone
import json
R=Path(__file__).resolve().parents[1];now=datetime.now(timezone.utc).isoformat()
p=R/'notes/part3.tex';s=p.read_text()
fnew=['part3_weighted_extra_sites','part3_os50_affine_conjugacy']
for name in fnew:
 line='\\input{notes/'+name+'.tex}\n'
 if line not in s:s=s.replace('\\input{notes/part3_fourfold.tex}',line+'\\input{notes/part3_fourfold.tex}')
for name in ['part3_joint_additive_returns','part3_common_exterior_meridians']:
 line='\\input{notes/'+name+'.tex}\n'
 if line not in s:s+=line
p.write_text(s)
audits={
 'part3_iii_star_ii_joint_final_audit':{
  'statements':['P3F.47'],'independent_auditors':['checks'],
  'checks':['Both E7 source pairs and every actual reduced/good star/II substitution and marked section.',
   'The starred good deck is (-X,-iY), checked from exponents and corrected before promotion.',
   'Exact E7 toric Cartier correction and good II coefficient-one cancellation; both actual translation and norm diagrams retained.',
   'Full source and boundary cones, every integral Smith representative, raw torsion rows and marked degree-one/three cycles.',
   'Both mixed degree-two maps are isomorphisms for every cap coefficient; symbolic D1/D3 determinant and1681 supplementary Smith cases.',
   'Remaining nodal cycle and its starred conjugate form an elliptic basis, so the actual group is cyclic of the exact determinant.',
   'All D=0 groups, exact global scalar closing and every gluing degree included.'],
  'certificate':'code/part3_root/iii_star_ii_joint.py',
  'history':'The free-lift determinant assertion before reducing the actual Z/2 target row is archived in code/part3_root/attempts/. The corrected certificate retains both raw and reduced mixed-group maps.'},
 'part3_weighted_extra_sites_final_audit':{
  'statements':['P3F.48'],'independent_auditors':['root'],
  'checks':['Exact rational source inversion with only the verified Z/b torsion removed by localization.',
   'Actual old N and generic Fgamma representatives give the required H3 surjection after all new tubes are removed.',
   'The ordinary H2 connecting map vanishes in a free even meridian group; the full localized rim extension is exact.',
   'Both free ends are odd; squaring the extension involution gives 2C=0, hence C=0 without inverting2.',
   'The old additive boundary isomorphism eliminates as its actual graph and leaves independent smooth/multiplicative blocks.',
   'The retained base-framing Seifert relation forces pairwise coprime effective orders and hence p not dividing b.',
   'The exact local product uses the signed translation g_-=-bG and p=a+b tau-t g_-.'],
  'certificate':'code/part3/weighted_extra_sites.py'},
 'part3_os50_affine_final_audit':{
  'statements':['P3F.49'],'independent_auditors':['root','blind_control'],
  'checks':['Both transitive quadratic-root actions have odd component, so their difference lies in the central identity C*.',
   'The exact squaring map solves the central (1-D) equation; the residual formal logarithm is solved by finite cyclic averaging.',
   'The literal Tate-unit solution has even quotient and conjugating even square root.',
   'The actual translation transports all four blowup centres and their Cartier comparison, without claiming it fixes the original centres.',
   'Extending degree-zero line lifts commute with B, and the target-scalar ratio is removed by the displayed coboundary with its arrow fixed.',
   'The remaining finite delta character and complete outer collar are retained.'],
  'certificate':'code/part3/os50_affine_conjugacy.py'},
 'part3_joint_additive_returns_final_audit':{
  'statements':['P3K.28'],'independent_auditors':['root','fourfold','checks'],
  'checks':['The actual positive parameter is one r-loop with lambda=r^(m_infinity*m_0); its cusp coefficient is the signed sphere determinant.',
   'Both root solid-torus maps have literal inverse cut identification and agree on the marked ordinary annulus.',
   'The actual weighted complex page has degree product, the displayed three branch divisors and exact genus.',
   'All root-sheet orbits have the stated length; the actual norm identity removes every residual stabilizer.',
   'Every good/reduced line correction is carried to the actual page, including the full I1star E0+E1 correction and central character -1.',
   'Two lifted conjugate nodal monodromies have primitive transverse vanishing cycles, giving integral coinvariants zero on the branched page.',
   'The relative translation and rigidified Hom comparisons retain the binding and all vertical/odd gauge ambiguities.',
   'Positive physical parameter equals the positive weighted Hopf angle for both determinant signs; the exact Thom comparison gives kappa=+1.',
   'All nine joint return polynomials and both single-I1star values A=-2 rechecked independently; all seven standalone pages visually reviewed.'],
  'certificate':'code/part3/joint_additive_returns.py'},
 'part3_common_exterior_final_audit':{
  'statements':['P3K.29'],'independent_auditors':['root'],
  'checks':['The normalized reciprocal section of O(1,1) has oriented boundary T[a]+T[c] minus the four actual positive strict-curve meridians.',
   'The actual common-exterior map is m0_new=-m0+2m1+2m2 and its integral relative dual is the inverse transpose.',
   'The return is the same actual map relative to the closed Cox cusp product; the common-exterior variation is symmetric.',
   'Integral Gysin and Poincare-Lefschetz maps identify the circle-trace image with the primitive span of the two nonfixed dual cycles.',
   'Equivariance kills variation on that span; the fixed coefficient uses the complex-meridian dual convention v=k_Jin.',
   'The stable derivative is a quotient pullback and vanishes on those trace cycles; its exact change of frame pairs with variation, which is zero there.',
   'No post-fixed-flop relative Pontryagin correction or further finite-isotropy return is inferred in this statement.'],
  'certificate':'code/part3_fourfold/common_exterior_meridians.py'}
}
for name,obj in audits.items():
 obj.update(status='PASS',audited_utc=now)
 (R/'records'/(name+'.json')).write_text(json.dumps(obj,indent=2)+'\n')
p=R/'code/update_report.py';s=p.read_text()
s=s.replace('P3F.16–P3F.47, P3K.6–P3K.27','P3F.16–P3F.49, P3K.6–P3K.29')
old='Joint additive return pages, the remaining weighted extra-site exclusions, global order-one parameter cochains and finite-isotropy fan return branches remain under proof.'
new=('P3F.48 excludes every added smooth or multiplicative effective order above one on all the computed weighted additive cores, including the prime2 case. '
 'P3F.49 exhausts the actual OS50 affine source and line lifts by explicit conjugations and transported blowup diagrams. '
 'P3K.28 computes all nine joint additive return rows and the two one-I1star source returns A=-2, with both determinant signs and the actual corrected line. '
 'P3K.29 gives the exact common-exterior meridian and relative-cycle maps, the full variation after the fixed-edge flop, and integer-zero derivative coordinates on the original nonfixed edges. '
 'Global order-one parameter cochains, the general page/Cox individual framing pair and the subsequent finite-isotropy fan frame recurrence remain under proof.')
s=s.replace(old,new);p.write_text(s)
print(json.dumps({'time':now,'audits':list(audits),'included':fnew+['part3_joint_additive_returns','part3_common_exterior_meridians']}))
