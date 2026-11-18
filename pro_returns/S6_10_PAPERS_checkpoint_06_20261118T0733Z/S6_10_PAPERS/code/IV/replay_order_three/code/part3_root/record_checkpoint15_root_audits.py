"""Record scoped root audits of the newly completed map calculations."""
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json

root=Path(__file__).resolve().parents[2]
def record(name,sections,files,points,scope):
    data={'utc':datetime.now(timezone.utc).isoformat(),
          'reviewer':'root','status':'PASS','audited_sections':sections,
          'verified_points':points,
          'files':{f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in files},
          'scope':scope}
    out=root/'records'/name
    assert not out.exists(),out
    out.write_text(json.dumps(data,indent=2)+'\n')

record('root_audit_source_infinity_corrected_norm.json',['IF.9'],
 ['notes/part3_source_infinity_fourfold_working.md'],
 [
  'The A kernel is g and its V multiplier is C epsilon^N q_* q_B^-2 u_X^-2. The B kernel is g h^-b and its Y=Z^a V multiplier is C epsilon^N q_* q_A^-2 u_Q^-2 u_P^-4 u_X^-2.',
  'On strict B, epsilon is comparable to q_A, the line multiplier is (QP)^a of order a, the metric ratio loses at most a powers, and the source reindex loses at most ab powers. Strict A gives the same bound using P^a and Q=O(q_B^2).',
  'The complete losses are a(1+b)=3 for (a,b)=(1,2) and 4 for (2,1). The actual operator bounds are C|lambda_0||epsilon|^(N-5) and C|lambda_0||epsilon|^(N-6).',
  'The executed geometric orders N=8 and N=6 lie in those bounds; the latter contracts after a uniform small choice of lambda_0. Smaller N=3,N=4 fan certificates establish arithmetic identities only.',
  'The two strict-face regions are disjoint. Their middle and H overlaps use the full-rank logarithmic period matrix, whose least singular value is bounded below by a positive multiple of the H logarithmic radius.',
  'Both node charts use the same interpolated endpoint line metric; the proof does not add an uncounted overlap loss. The actual E chain and nonzero H images of the face kernels remain retained.',
  'The prior raw-multiplier wording and short norm-shell attempt are preserved in immutable checkpoint14, and the working proof explicitly records the correction.'
 ],
 'Narrow audit of the corrected analytic norm budget. The separate full excision and residue audits remain in their own records; no smaller-order filling is inferred.')

record('root_audit_source_cusp_shear_typed_cartier.json',['SFIX.4'],
 ['notes/part3_source_cusp_shear_fixed_pair_working.md'],
 [
  'The new spinor is E tensor O(n(D_+-D_-)); its generators are x^(-n-1)y^n and x^-n y^(n+1).',
  'Multiplication by Z^n is a map from that typed Cartier bundle to E and sends those actual generators to 1/x and y. Its inverse is Z^-n with the opposite bundle types.',
  'The determinant generators and trivialization are Z^(-2n-1) and Z^(2n+1); the Hom normal line remains O(-D_+-D_-).',
  'After the typed map the standard-frame arrow is diag(1/y,y), so its Hermitian normalization and the fixed summand swap recover the displayed local SP.9 matrix.',
  'The branch SU(2) contractions have axis degrees +n and -n. Their Cartier eigenline transitions are retained in the new Hopf line.',
  'The outer Cox collar, actual source/line B^n reindex and completed quotient/graph comparison remain required. This local calculation does not assign a global characteristic value.'
 ],
 'Only the typed local bundle morphism and its normal/axis data are audited. No ell=0 result or full shear characteristic pair is inferred.')

record('root_audit_source_zero_native_square.json',['DZ.1','DZ.2','DZ.3','DZ.4','DZ.5'],
 ['notes/part3_source_zero_double_loop_product_working.md',
  'code/part3/source_zero_double_loop_product.py',
  'code/part3/source_zero_double_loop_product.json'],
 [
  'The actual forward arrow q^(nk) is reindexed by the full period B^(-nk), leaving the varying-unit seam E_v=(g^(-nk)Z,eta^(-nk)V). The cut logarithms supply C_end E_v=1 as a full collar identity, including all derivatives.',
  'The seam maps preserve q, commute with both periods and the physical circle, and have the literal T+ and T- chart maps. Direct substitution retains every coefficient in the three edge transitions.',
  'The single C2 native star has the literal transition z prime=1/z and normal prime=z normal. The doubled closed product is defined by C2_(j+tau)=C1_tau E_v^(-j), which matches on full collars and is precisely its pullback to the degree-two parameter cover.',
  'The original global cap and overlap square remain unchanged. A cutoff extension of the prescribed boundary product velocity in the existing compact family constructs a compatible complete family connection.',
  'The doubled determinant winding 2(N-1) gives the displayed based quaternion contractions. The retained logarithmic units, nonlinear normal rescaling and vertex collars construct the actual ordinary product.',
  'The moved Hopf representative, Maurer product boundary caps and stable GL+ universal-cover chain rule give I_i=t w_i+d_i(l_i-t) and W_i=t w_i-d_i(l_i-t). The actual trace prism then gives V22=2N-4 and delta2=2N+4a-4.',
  'The carried ambient-to-single-star frame has absolute third class e2. Its exact frame-change pairing gives the ordinary pair (-2N+4-2a,2a). The explicit native boundary change is pure left with endpoint degree -2t, giving native pair (2-2a,2a).',
  'The Cox lift (a0,a1,c0,c1) maps to (a0,(AD)^-1 a1,A c0,D c1), preserves q=a0 a1 c0 c1, and extends to both resolutions with a literal inverse at the same q.',
  'The pulled-back native boundary product and pulled-back connection have relative return f squared. Interpolation with that boundary fixed identifies the ordinary calculation, after its actual boundary correction, with the same relative square.',
  'The free-coordinate homomorphism of the K23 relative group sends f squared to twice the two integer coordinates. Injectivity of multiplication by two on Z squared gives the single pair (1-a,a).',
  'Applying the actual single-loop K23 conjugation gives Z_(J T)-Z_T=a in Z/28. The proof takes no inverse of multiplication by two on Theta7 and assigns no individual source-zero class.'
 ],
 'The initial and reflected source-zero fan objects with the exact RG scalar/cap data only. The separate C1 scalar diagnostic is outside this audited C2 comparison.')
print('PASS: corrected IF.9, typed local SFIX.4, and actual DZ native-square audits saved.')
