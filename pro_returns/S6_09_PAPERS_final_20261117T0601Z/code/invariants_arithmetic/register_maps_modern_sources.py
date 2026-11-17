#!/usr/bin/env python3
"""Register the actually opened modern primary-source scopes (idempotently)."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / 'deliverables/work/invariants_arithmetic'
BASE = json.loads((WORK / 'references_verified.json').read_text())
BY = {x['citation_key']: x for x in BASE}
LEDGER = WORK / 'maps_D_references_verified.json'
entries = json.loads(LEDGER.read_text())
existing = {x['citation_key']: x for x in entries}

scopes = [
 ('manViaclovskyLogs26','ViaclovskyLog2026',
  'Original supplied TeX: lines349–503 (data (2.11)–(2.12), Proposition2.3 and its whole proof), 698–742 (Proposition4.1 and its whole proof), 857–973 (Proposition4.3 and its whole proof), 1065–1137 (Proposition4.5 and Corollary4.6, whole proofs).',
  'D2.5: actual logarithmic filling, integral boundary marking, primitive cusp specialization and original determinant result.',
  'The source Proposition4.1 assumes H1(X)=0. The receiving D2.5 independently proves the arbitrary-determinant/torsion extension and does not attribute that extension to the source. The primary translation data are integral v_i=r_i delta+n_i u_i, with gcd(n_i,m_i)=1; the meridian and section corrections are retained.'),
 ('manViaclovskyTwo26','ViaclovskyTwoParameter2026',
  'Original supplied TeX: lines493–730 (local completions, Proposition3.1, Lemma3.2, complete proofs), 873–958 (Proposition4.2 and complete global monodromy proof).',
  'D2.6: the III-star configuration, rank-one/full-rank-two Mumford specialization, origin-preserving good-reduction model, and exact global monodromy marking.',
  'The original finite filling has order4. The arbitrary4k extension is proved in D2.6. The homology convention is (T^{-1})^t; the r^3 origin correction and the exact invariant vector hat(psi)-hat(u)-hat(w) are included. Source monodromy is not substituted without this marking.'),
 ('manWang26','Wang2026',
  'Original supplied TeX: lines151–193 (surface and section statements); 294–479 (Tate lemma and rank-one filling, complete proofs); 499–755 (rank-two filling, good reduction, logarithmic quotient and boundary-group lemma, complete proofs); 759–1030 (main statement and whole elliptic/section/Jacobi monodromy derivation); 1410–1474 (Theorem7.1 and surface proof); 1590–1853 (end of elliptic factorization proof and complete AppendixB topological argument).',
  'D2.7–D2.8: actual order-three cap and section marking, the primitive (2,1) I2 period, global cohomology matrices, and comparison with the original surgery/cube theorem.',
  'The I2 period is (2,1), changed by (x,y)=(v,v^2/z) to primitive (1,0). A zero-weight I2 archival API cap is a different construction. The quotient group has m_*^3=t_{-ell} in the source positive-meridian convention, with ell=hat(psi)-2hat(u)-4hat(w). D2.8 gives its own all-odd-twist cube argument and uses the independently opened Zhubr classification; no unverified Andrus thesis theorem is relied on in the receiving proof.'),
 ('manLR26','LiuRollenske2026',
  'Original supplied TeX: lines891–1014 (Lemma3.10 and Proposition3.11, complete proofs); 1112–1245 (Proposition3.13 and full global basis-comparison proof); earlier opening1702–1728 (main theorem and proof).',
  'D2.9 and D2.11: product type-II cap, marked specialization, positive angular/radial circles, and the original global torus monodromy.',
  'The type-II line bundle is topologically trivial over the retracting S2, the mapping torus is contracted through an isotopy extending over the disc, and specialization is primitive by degree-one sections. Original order is T_inf*T_1*T_0=I; the cyclic order in D2.9 preserves this relation. The 3P Type-C variant in D2.11 is rederived there and is not asserted as an original LR theorem. Commented source text after1732 is excluded.'),
 ('manYang26','Yang2026',
  'Original supplied TeX: lines708–1078 (Propositions3.1,3.4,3.6 and intervening lemmas, complete modular-coordinate and affine-period proofs); 1375–1568 (Lemmas4.1,4.3, Proposition4.4 and complete proofs); 3340–3695 (Whitney/Thom lemma, compatible level-tube retraction, ordered-branch normalization resolution, Theorem7.8 and complete proofs); 3851–3983 (Lemma7.10 and full sweep-chain proof); 4077–4154 (Theorem7.13 and whole homology proof); 5340–5461 (AppendixB.4, exact forward-return matrices, cut cylinders, signs, and finite sweep squares).',
  'D2.10–D2.11: holomorphic root-disc quotient/collar, finite-power relation, primitive integral cusp sweeps, original homology, Type-C modular map and normalized first/second affine coordinates.',
  'The source uses clockwise meridians with left-to-right path traversal; conjugation deck matrix A and forward-return matrix A^{-1} differ. The integral Mayer–Vietoris connecting class is -(u+w), and the delta sweep is one coarse meridian with coefficient1/m. The receiving proofs retain these signs, independently prove the all-R saturation and arbitrary twist extension, and do not infer it from the original k=l=1 statement. The torsor under O(-1) has unique first coordinate; the second coordinate is an affine C-line.'),
]

source_bib = (ROOT/'sources/returns/S6_04_MAPS_MANIFOLDS/S6_04_MAPS_MANIFOLDS_references.bib').read_text()
bibpath = WORK/'maps_D_checked_references.bib'
bib = bibpath.read_text()
for key,old,loc,use,hyp in scopes:
    rec = {k:v for k,v in BY[old].items() if k != 'citation_contexts'}
    rec.update(citation_key=key, alias_of=old, opened_locator=loc,
               actual_use=use, hypotheses_and_normalization_check=hyp,
               status='verified_for_stated_use', verified=True,
               extent='Full operative original proof blocks read at the exact listed locators; scope does not claim full-paper rederivation.',
               date='2026-11-17 UTC')
    assert hashlib.sha256((ROOT/rec['local_source']).read_bytes()).hexdigest()==rec['source_sha256']
    existing[key]=rec
    if not re.search(r'@\w+\{'+re.escape(key)+r'\s*,',bib):
        block=re.search(r'(?ms)^@\w+\{'+re.escape(key)+r',.*?^\}',source_bib).group()
        block=re.sub(r'(?ms)^\s*note\s*=.*?(?=^\})','',block)
        block=block[:-1].rstrip().rstrip(',')+',\n  note={Original supplied primary source verified at the scoped locators in maps\\_D\\_references\\_verified.json by GPT-6 Astra (OpenAI, ChatGPT Pro mode), effort Pro, 17 November 2026 UTC.}\n}'
        bib+='\n\n'+block+'\n'

z=existing['manZhubr75']
addition=' Additional opening: printed p805, Lemma3.7 and exact sequence(3.8), original text lines676–760; E-infinity_(6,0)=Ker(alpha) and alpha is dual to Sq2. The surrounding Lemmas3.5–3.6 and statement/proof of(3.9) on pp805–806 were read.'
if 'Lemma3.7 and exact sequence' not in z['opened_locator']:
    z['opened_locator']+=addition
    z['actual_use']+=' D2.48: full mu lies in the Sq2-dual kernel described by Lemma3.7, not merely the detected quotient.'

LEDGER.write_text(json.dumps(list(existing.values()),indent=2,ensure_ascii=False)+'\n')
bibpath.write_text(bib)
print(json.dumps({'references':len(existing),'modern_added':[s[0] for s in scopes],'Zhubr_scope_extended':True},indent=2))
