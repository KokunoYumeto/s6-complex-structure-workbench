"""Record the independently audited eighth-hour additions and scope."""
from pathlib import Path
from datetime import datetime,timezone
import json

ROOT=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
audits={
 'part3_reduced_iii_final_audit':{
  'statements':['P3F.37','P3K.24'],
  'scope':'Both explicit E7 source profiles; reduced III root m=4l+3, actual positive r-loop.',
  'checks':['Exact Weierstrass substitutions and resolved III chart; nonidentity G and identity 2G.',
   'Actual root-line descent, retained deck character, commuting contracting norm and directed ordinary-to-cap gluing.',
   'Primitive E7 complement, exact relative-Wang second column, arbitrary cap coefficient, all D0 through D4 maps and van Kampen.',
   'Weighted-S3 inverse, actual regular-binding cover t=t_*+a^(-m), complete root-slice graph and boundary-relative Neron torsor comparison.',
   'Rigidified universal Hom evaluation gives the actual line comparison before pulling back along smooth translations.',
   'Physical V=exp(2pi i zeta_2), gamma_out=B^(-1), inverse closing q_infinity and positive cusp deck (t-t_c).',
   'Circle-first orbit reversal and normal Thom reversal both retained; actual page boundary arg(a) and positive loop give kappa=+1.',
   'Exact chi=l+1, M^2=-2m, A=-(3l+2); all 28 residues executed.'],
  'independent_auditors':['root','fourfold'],
  'history':'The inward-origin attempt and the intermediate incomplete ambient-orientation inference are retained; neither was promoted. The final exact arrow and Thom calculation decide the sign.'},
 'part3_i1star_joint_final_audit':{
  'statements':['P3F.38','P3F.39'],
  'scope':'Actual good/reduced IV partners on I1star+IV+I1, and exclusion of added smooth effective orders above one on the three computed additive cores.',
  'checks':['Exact good and reduced root equations and component characters.',
   'Good-root blowup/quotient/contraction line comparison with E2-E0, including order-three Euler character.',
   'One translation lift chosen before its n-th power; invariant base-unit norm and commuting A,B.',
   'Source complement fundamental group from the primitive starred/nodal vanishing-cycle intersection.',
   'All source-cone, primitive torsion, degree-one and degree-three path columns rerun by root.',
   'Arbitrary-kappa degree-two matrices are integral isomorphisms for b2 and b6; determinant m*n_star+2*n_IV in degrees one and three.',
   'Smooth-cap proof uses inversion only on the original exterior; Thom maps vanish by actual intersection parity; the odd rim extension is split over F_p.',
   'Additive image eliminates a graph over the original H2 and leaves independent rim summands; p|m leaves two classes.',
   'P3F.35 actual common blowup/flop chain transfers sphere topology to all permitted fans.'],
  'independent_auditors':['root','blind_control']},
 'part3_multiplicative_cap_final_audit':{
  'statements':['P3F.40'],
  'scope':'One multiplicative-site actual cap for the ten primitive-translation sources; simultaneous modifications not yet claimed.',
  'checks':['Actual outward gamma gives c=-c_G in the integral boundary commutators.',
   'Ordinary cap and primitive full-source Wang maps give the exact H2 boundary isomorphism and torsion-free H2 exterior.',
   'Tate-unit boundary frame and actual Hom lift have zero graph winding; their sole base winding gives (T-I)K=+/-F by the relative Chern connecting map and Poincare-Lefschetz duality.',
   'Boundary isotropy first kills the exterior L coefficient and then its R coefficient by self-intersection.',
   'Actual meridian mu=m alpha+j b+n gamma, signed affine root displacement -A, A=Nj-cn, and transitivity gcd(m,A)=1.',
   'Cap isotropy forces r=-A and m*t=A*s. The integral target change retains k and leaves diag(m,m).',
   'The full symbolic matrix and seven marked exterior-square complexes execute; sampled cap H1 quotients and Smith forms are exact.',
   'All corrections and the failed pre-isotropy assertion are preserved under code/part3_root/attempts/.'],
  'independent_auditors':['root','checks']},
 'part3_whole_i1_shear_final_audit':{
  'statements':['P3K.25'],
  'scope':'The ten K22 scalar families, all fans retaining the physical delta edge; finite-isotropy branches remain under proof.',
  'checks':['Literal height-one ray map and monomial local coordinates fix physical delta.',
   'Actual period labels generate Z^2; returning the shifted representative leaves one common physical-delta parameter factor in the Cox lift.',
   'The directed parameter deck and the retained source double-root origin gauge give the same endpoint scalar.',
   'Both charged cap boundaries and the full fixed-locus normal sphere are retained as in K17; their actual lines and characteristic corrections vanish.',
   'The endpoint characteristic expressions are equal independently of their original numerical index.'],
  'independent_auditors':['root']}
}
for name,record in audits.items():
 record.update(status='PASS',audited_utc=now)
 (ROOT/'records'/f'{name}.json').write_text(json.dumps(record,indent=2)+'\n')

(ROOT/'notes/part3_multiplicative_cap_working.md').write_text('''# Multiplicative-cap derivation: completed one-site proof

The completed and independently audited derivation is P3F.40 in
`notes/part3_multiplicative_cap.tex`. Its complete boundary certificate is
`code/part3_root/multiplicative_cap_boundary.py`, with JSON and recorded output.

The exact one-site degree-two cokernel is (Z/m)^2. The actual sphere
sector is m=1,n=+/-1. This does not assert the classification of
simultaneous multiplicative-site replacements or their parameter returns.

The first draft left an exterior coefficient e and two cap coefficients
s,t arbitrary. The executable isotropy check showed the additional
self-pairing condition: e=0 and m*t=A*s. Transitivity gives gcd(m,A)=1,
so s=m*k,t=A*k; the exact integral target basis change retains k and
reduces the full degree-two quotient to diag(m,m). The signed full
four-by-four determinant is -m^2 and the reduced determinant is m^2.

The earlier draft and failed script are preserved under
`code/part3_root/attempts/multiplicative_cap_before_isotropy.md` and
`code/part3_root/attempts/multiplicative_cap_boundary_before_isotropy.py`.
They were never promoted. The final orientation uses c=-c_G because
physical outward gamma covers +G; its affine-root displacement is -A.

The relative Chern-frame argument was independently checked by the checks
agent: the translated Tate-unit boundary frame has no elliptic winding;
dividing the actual Hom section by its sole base zero adds exactly one
signed alpha winding. Its Poincare--Lefschetz dual is +/-F with no rim term.
''')

p=ROOT/'code/update_report.py'
s=p.read_text()
s=s.replace('P3F.16–P3F.35, P3K.6–P3K.23','P3F.16–P3F.40, P3K.6–P3K.25')
addition=(' P3F.36–40 prove the corrected-line I1star sphere sectors, the two-cap I1star/IV determinant m*n_star+2*n_IV, the reduced-III actual cap, extra smooth-order exclusion on the additive cores, and the exact (Z/m)^2 one-multiplicative-cap obstruction for primitive sources. P3K.24 gives the reduced-III positive return A=−(3l+2), m=4l+3, on both explicit E7 profiles, with the physical closing arrow and signed Thom comparison. P3K.25 proves equality of the K22 returns across every fan retaining the physical delta edge. Simultaneous cap tuples, the remaining additive partners and return indices on finite-isotropy fan branches remain under proof.')
s=s.replace('Remaining singular-source cap tuples and return indices for general nonfixed-edge fans remain under proof.',addition.strip())
s=s.replace('Exhaustive singular-source cap verification and return indices for general nonfixed-edge fans and logarithmic sites permitted by Remark8.5 remain under proof.',addition.strip())
marker="def expanded_ids(text):"
new="""# Exact corrected-line I1star comparisons; supplied narrow qualifiers remain undefined.
put('S6_04','D.2.27','The actual corrected-line weighted I1star constructions in P3F.36/38 give spheres. The supplied natural-profile qualifier is not defined, so its narrower scope remains undecided.','P3F.36; P3F.38','undetermined')
put('S6_04','D.2.49','The actual primitive boundary torsion cancels in the corrected-line weighted sphere construction. The supplied canonical qualifier does not identify its exact tuple.','P3F.36','undetermined')
put('S6_04','D.2.50','The exact line O(aG-O-L0) produces the proved sphere tuples; the supplied sixteen corrected-line tuples are not identified in the row.','P3F.36; P3F.38','undetermined')

"""
if '# Exact corrected-line I1star comparisons' not in s:s=s.replace(marker,new+marker)
p.write_text(s)
print(json.dumps({'audits':list(audits),'updated_utc':now}))
