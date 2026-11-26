"""Record the completed original/receiving ruled-equality proof comparisons."""
from S6_SERIES_PUBLISH_c3_edit import *
import json
import subprocess
import sys

apply_edit(
 r'''and the ruling maps $r_N,s$ satisfying $r_Ns=\operatorname{id}$.''',
 r'''and the ruling maps $r_N:N\to B_0$ and $s=\pi h:B_0\to N$, where $h:B_0\simeq H\hookrightarrow T$, satisfying $r_Ns=\operatorname{id}_{B_0}$.''',
 'II-C3-RULED-TRIPLE-SECTION-NOTATION',['D22'],'night:P4.31',
 'First step of the ordinary-triple equality proof',
 'Make the maps and their common base explicit before the later identity r_N pi h is used; these are exactly the maps of P253.',
 'Complete old and receiving unit read by root; bounded notation change read in full. No independent credit.')
apply_edit(
 r'''and the descended ruling $r_N:N\to B_0$ with section $s=\pi h$.''',
 r'''and the descended ruling $r_N:N\to B_0$ with section $s=\pi h$, where $h:B_0\simeq H\hookrightarrow T$.''',
 'II-C3-RULED-TACNODE-SECTION-NOTATION',['D22'],'night:P4R.11',
 'First step of the tacnodal equality proof',
 'Declare the parametrized section inherited from P253 at its first use, preserving the same ruling and normalization maps.',
 'Complete old and receiving unit read by root; bounded notation change read in full. No independent credit.')

entries=[
 ('subsec:II:zero-euler-ruled-conductor','II-C3-ROOT-RULED-CONDUCTOR-UNIT-READ',
  'The complete original common reductions in P4.29/P4.31/R11/P4.32 and complete receiving P253 were read. The proper pushout includes every contracted curve and gives the inverse on the same pi1(T); R1 applies to the identical full mS. The section identity is exhibited through the exact P4.33 substitution. The Euler graph equality gives an irreducible unibranch image with elliptic normalization, and the local delta/intersection enumeration gives the three full transverse germs and their branch degrees. No original statement scope was reduced. This new unit receives no subdivision or migration movement credit.'),
 ('night:P4.29','II-C3-ROOT-CUSPIDAL-EQUALITY-UNIT-READ',
  'The complete original and receiving cuspidal equality statement and proof were read. P253 supplies exactly the common ruling, conductor and Euler data formerly proved in this unit. The unchanged generic cusp has conductor (v^2); Cohen--Macaulay depth removes the finite-support nilradical. The same conductor-scheme Euler equality forces all delta invariants to vanish; the product-cusp conclusion and minimality use P4.28 and P4.22 on the identical support and normalization. All original hypotheses and the complete conclusion remain.'),
 ('night:P4.30','II-C3-ROOT-TRIPLE-EQUALITY-UNIT-READ',
  'The complete original and receiving P4.30/P4.31 unit was read. P4.30 retains every derivative-lattice step, the embedding-dimension cases, and the symbolic-double exact sequence. P4.31 applies P253 to the same full fibre and double horizontal divisor; the three explicit quadratic branch vectors identify the generic conductor, depth one gives J=P^(2), and the conormal inequality forces g=1 and smooth C. The section map keeps the three preimages distinct. The normal-branch and regular-quotient argument proves all branches smooth before the explicit invertible (x,y,z)->(ax,-by,z) coordinate change. The section parametrization is now declared at first use. No statement or numerical conclusion changed.'),
 ('night:P4R.10','II-C3-ROOT-TACNODE-EQUALITY-UNIT-READ',
  'The complete original and receiving R10/R11 unit was read. R10 retains the full conormal and Hessian lattices, d_p/2+b_p bounds in both embedding dimensions, the descent lengths and equality conclusion; only its conductor-depth input now names the shared duality lemma on the same finite normalization. R11 retains the entire tacnodal local factorization and coordinate-root argument. P253 provides the common ruling data, the same R10 equality makes the curve smooth and Hessian rank one, and Riemann--Hurwitz gives the unchanged degree-two unramified map. The section h is explicitly declared. No full-fibre deformation conclusion is inferred here from a reduced equation.'),
 ('night:P4.32','II-C3-ROOT-ZERO-EULER-CLASSIFICATION-UNIT-READ',
  'The complete original and receiving P4.32 statement and proof were read. Its statement is byte-identical under the guarded rewrite. The normal case specifies the exact cyclic root charts and finite unramified torus cover. The class-VII application uses the identical normalization resolution and full fibre. The ruled alternatives apply P252/R7 or P253 and the three full local equality propositions to the same pole divisor; the converses are retained. The global conclusion keeps the all-supports irreducible-or-normal-crossing hypothesis and the same nonnegative Euler sum. Neither refined R13 nor P4.40 is used.')]
for unit,event,outcome in entries:
    data=dict(unit=unit,event_id=event,complete_original_and_receiving_read=True,
      outcome=outcome,unit_detail='The complete local proofs and exact common-data maps were compared; final placement and rendered-page reading remain open.')
    subprocess.run([sys.executable,str(ROOT/'code/S6_SERIES_PUBLISH_c3_read_unit.py')],
      input=json.dumps(data),text=True,check=True)

set_unit_status('night:P4.33','D12','done',
 'Complete original and receiving P4.33 read. Its duality paragraph now applies the common conductor-duality owner to the identical finite normalization; its full Leray, Serre-duality and Riemann--Roch proof remains. The statement exposes precisely its already-proved Cohen--Macaulay conductor, Euler and ruling-section identities.',
 'CHECK_EVENTS.tsv: II-C3-ROOT-NORMALIZATION-COHOMOLOGY-RECEIVING')
add_event('night:P4.33','II-C3-ROOT-NORMALIZATION-COHOMOLOGY-RECEIVING','used and rechecked in this run',
 'Complete old and receiving statement/proof read. All original cohomology, rational-singularity, Euler and ruling conclusions remain, with the already-proved conductor and section identities stated for exact reuse by P253. The finite normalization in the first step is the one to which P222 applies. The existing whole-unit check is retained; only its reopened D12 row is closed. No independent credit.',
 'S6_SERIES_PUBLISH_II.tex: Normalization cohomology and conductor schemes',
 source='code/S6_SERIES_PUBLISH_c3_ruled_equality_receiving.py')
print('Ruled-equality receiving comparisons complete; final placement and page reading remain open.')
