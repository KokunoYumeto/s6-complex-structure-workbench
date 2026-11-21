from pathlib import Path
import json,hashlib,datetime
from S6_SERIES_PUBLISH_editing import Editor
r=Path(__file__).resolve().parents[1]
ed=Editor('I')
g=json.loads((r/'agents/i_provenance/S6_SERIES_PUBLISH_I_primary_citation_guards_02.json').read_text())
for x in g['changes']:
 ed.replace(x['old'],x['new'],'D18',x['reason'],x['id'],count=x.get('expected_count',1))
ed.replace(r'\citep{AC26,E26}',r'\citep{AC2026,Engel2026}','D18',
 'The shared prose referred to Paper V bibliography keys. AC26 maps exactly to AC2026 and E26 to Engel2026, the same two primary works in Paper I; change only the lookup keys, preserving the shared rendered wording.','series:I:series')
g=json.loads((r/'agents/i_analytic/S6_SERIES_PUBLISH_I_nine_correction_guards.json').read_text())
for x in g['guards']:
 ed.replace(x['old'],x['new'],'D25',x['reason'],'ari:C.8.12' if 'C8.12' in x['id'] else 'ari:C.7.1',count=x.get('expected_count',1))
ed.save()
g=json.loads((r/'agents/i_provenance/S6_SERIES_PUBLISH_I_shared_bib_guards_02.json').read_text())
p=r/'S6_SERIES_PUBLISH_references.bib';s=p.read_text();old=s
for x in g['changes']:
 assert s.count(x['old'])==x.get('expected_count',1),x['id']
 s=s.replace(x['old'],x['new'])
p.write_text(s)
(r/'records/S6_SERIES_PUBLISH_I_bibliography_guard_receipt_02.json').write_text(json.dumps({
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'before_sha256':hashlib.sha256(old.encode()).hexdigest(),'after_sha256':hashlib.sha256(s.encode()).hexdigest(),
 'source_guard':'agents/i_provenance/S6_SERIES_PUBLISH_I_shared_bib_guards_02.json'},indent=2)+'\n')
p=r/'S6_SERIES_PUBLISH_report.md';s=p.read_text()
s+='''
### Paper I: two further exact corrections

The branch clause of ari:C.7.1 was false when read as covering changes of the elliptic logarithm. For u=omega_2/3 and a shift by 2 omega_1, the change is 4 pi i/3 modulo 4 pi i, by Legendre's relation. The refined statement retains the original label/tag and adds ari:C.7.1:lift-transport (tag IA01): with u fixed, log-sigma branches change the expression by 4 pi i integers, while elliptic-logarithm translations follow the exact displayed semicharacter formula. Its real part and the norm identity are unchanged. A scoped refutation event and the refined id are being merged from the analytic comparison ledger.

In the proof of ari:C.8.12, the ratio (t-1)/t'_tau omitted one factor of E4 in its denominator. The corrected expression is -E6/(2 pi i E4^2), derived directly from t=E4^3/(E4^3-E6^2) and t'=-2 pi i t E6/E4. The radial theorem agrees with the independent derivation and is unchanged. The analytic check also disclosed and corrected its own preread sigma-theta constant slip; that constant step is excluded from preread check credit.

The first intermediate Paper I build has zero overflows, undefined references, missing characters/fonts and duplicate labels; its two undefined citations were the shared-introduction keys AC26/E26, now mapped to this paper's entries AC2026/Engel2026. A later build and the complete final page reading are still required.
'''
p.write_text(s)
print(json.dumps({'new_math_refinement':'ari:C.7.1:lift-transport','intermediate_proof_correction':'ari:C.8.12','bibliography_updated':True}))
