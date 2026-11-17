"""Record the original AC26 semidirect-product source match and rewording."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'deliverables'
record={
 'keys':['AC2026','AC26'],
 'locator':'AC26, original PDF p.90, section10.5, Lemma10.7 and its complete proof',
 'source':'sources/original/AC26_original_manuscript.pdf',
 'opened_image':'sources/external/root/ac26_pages/page090.png',
 'reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode), effort Pro, 17 November 2026 UTC',
 'status':'verified in the specified scope',
 'verification':'Original page visually opened; full lemma and proof read. For a split group extension, the correct abelianization is the direct sum of Q_ab and the Q-coinvariants of K_ab. The WB lemma is a re-derivation of this known formula, not a new result. The complete quotient proof is independently worded in work/root/semidirect_abelianization_rederivation.tex, with the normal subgroup, induced quotient maps and commutator quotient explicitly justified.',
 'source_proof_sha256':hashlib.sha256((OUT/'work/cdp_audit/extracted/WB_lem_semidirect-abelianization.tex').read_bytes()).hexdigest(),
 'printed_rederivation_sha256':hashlib.sha256((OUT/'work/root/semidirect_abelianization_rederivation.tex').read_bytes()).hexdigest(),
 'retention':'Every mathematical step of the WB quotient method is retained, with explicit AC26 credit. Its original text remains in the extracted provenance file; no AC26 prose is reproduced in the paper.'}
(OUT/'work/root/source_checks_007.json').write_text(json.dumps([record],indent=2)+'\n')
p=OUT/'work/root/references_verified.json';rs=json.loads(p.read_text())
if not any(r.get('locator')==record['locator'] for r in rs):rs.append(record)
p.write_text(json.dumps(rs,ensure_ascii=False,indent=2)+'\n')
p=OUT/'work/root/proof_audit.md';s=p.read_text()
heading='## Semidirect-product credit and complete rewording'
if heading not in s:
 s+='\n'+heading+'\n\n'+record['reader']+'. '+record['verification']+' The original AC26 statement and proof were checked on the rendered page, not only in the searchable transcription. A prose-only 14-word overlap scan of the current I manuscript against the AC26 transcription found no long identical prose run; this is a locator aid, not a mathematical or originality certificate.\n'
 p.write_text(s)
print('AC26 Lemma10.7 credit and quotient re-derivation recorded.')
