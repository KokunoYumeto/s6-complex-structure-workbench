#!/usr/bin/env python3
"""Record the exact Rossi source/version and the exposed resolution comparison."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation3_provenance/final_sources'
source = (ROOT / 'S6_SERIES_PUBLISH_II.tex').read_text()
start = source.index(r'\bibitem[Rossi(2017)]{Rossi2017}')
end = source.index(r'\bibitem[', start + 1)
old = source[start:end]
old_url = r'\newblock URL \url{https://arxiv.org/pdf/1211.6329}.'
assert old.count(old_url) == 1
new = old.replace(old_url,
    '\\newblock Cited preprint: arXiv:1211.6329v3, 31 March 2017.\n'
    '\\newblock URL \\url{https://arxiv.org/pdf/1211.6329v3}.')
pdf = ROOT.parents[1] / 'tmp/c3_provenance_primary/Rossi2017_arxiv_v3.pdf'
content = pdf.read_bytes()
sha = hashlib.sha256(content).hexdigest()
assert len(content) == 336443
assert sha == '000ad2e03b115a872c1d8ab4283e72c81c25216dd5376e549ceedf3e3e1c84bb'
now = datetime.now(timezone.utc).isoformat()

def write(name, rows):
    with (OUT / name).open('w', newline='') as f:
        w = csv.DictWriter(f, list(rows[0]), delimiter='\t', lineterminator='\n')
        w.writeheader()
        w.writerows(rows)

write('S6_SERIES_PUBLISH_rossi_bib161.tsv', [dict(
    change_id='II-C3-PROV-161', type='D18', statement_id='Rossi2017;cdp:st:C.2.UN.8',
    old_location='Bibliography: Rossi2017', old_page='source guard; final concordance pending',
    new_location='Bibliography: Rossi2017 exact preprint version', new_page='integrated build pending',
    old_text=old, new_text=new,
    reason='The receiving numerical locators are in arXiv:1211.6329v3, dated31 March2017: Proposition4 and complete proof pp.10-12; Remark5 p.20. The current unversioned URL does not identify that layout. Preserve the publication key, journal data and DOI and identify the opened preprint version.',
    review_status='Primary arXiv version history and exact PDF title/version checked; complete cited statements/proofs read. Bounded bibliography guard only; no shared writes.')])
write('S6_SERIES_PUBLISH_rossi_sources.tsv', [dict(
    source_key='Rossi2017', url='https://arxiv.org/pdf/1211.6329v3',
    version='arXiv:1211.6329v3,31 March2017; publication Math.Phys.Anal.Geom.20(2017),article15',
    locus_read='Weierstrass convention and Theorem3 statement p.8; complete section3 setup, Proposition3 and proof p.9; complete Proposition4 and proof pp.10-12; complete Remark5 p.20; pages8,11,20 rendered and visually read; title/version and arXiv submission history',
    sha256=sha, bytes=len(content),
    own_paraphrase='The cuspidal self-product has six isolated threefold cusps. Successive blowups of pairs of cyclic images of the diagonal yield six small projective resolutions; each singular point is replaced by two projective lines meeting once. The local proof writes the three graph equations. Remark5 computes the resolved threefold Hodge numbers h11=21 and h12=3.',
    exact_application='UN8 uses the same Weierstrass surface under (x_Rossi,y_Rossi)=(y,x), B=t^6-1. Its actual final graph has R=[u:a], S=[u:ab] and the three equations in the supplied TeX paragraph. The p.11 displayed local index5,epsilon=rho has variables(v,u,c,a). Its graph coordinates are(mu,nu)=(tau_L^-1(swap S),R), with inverse(nu,swap(tau_L mu)). Here tau_L sends a line ell to ell tensor L_b; L=O_B(1). The source p.10 global action with epsilon=rho^2 has fifth/zeroth centres(v,c),(u,a); their graph gives the same equations. These maps commute with blowdown and glue to the identity off the six singularities.',
    read_extent='Complete original UN8 statement/proof and both following/prefacing credit paragraphs were read, together with all specified primary loci and the complete proposed comparison paragraph. The source uses inverse orbit exponents in its p.10 graph parametrization and p.11 local coordinate list; both conventions were compared explicitly rather than silently identifying the indices. No full reading of the entire Rossi paper or independent proof credit is claimed.',
    date_utc=now)])
write('S6_SERIES_PUBLISH_rossi_CHECK_EVENTS.tsv', [dict(
    statement_id='cdp:st:C.2.UN.8', date=now[:10],
    who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; continuation3 provenance',
    type='used and rechecked in this run',
    outcome='Read the full original UN8 owner/proof and exact Rossi version3 Proposition4/proof and Remark5. Compared both cyclic-index conventions and the Weierstrass coordinate interchange. Verified all three receiving graph equations, all three old blowup charts, both inverse projective-bundle maps and gluing over X. The proposed paragraph identifies the actual resolved threefold without changing UN8 scope. No independent derivation or complete receiving root-unit read claimed.',
    event_id='publish:c3:provenance:Rossi-UN8', phase='publication exact primary application',
    source_file='agents/continuation3_provenance/final_sources/S6_SERIES_PUBLISH_rossi_CHECK_EVENTS.tsv',
    source_row='', source_event_type='used and rechecked in this run',
    evidence_group='publish:c3:provenance:Rossi-UN8', publish_input_file='',
    publish_input_row='', date_utc=now,
    where='UN8 complete original owner; Rossi version3 pp.8-12 and20; proposed full resolution comparison')])
print('Prepared Rossi source/application records and bounded bibliography161; shared source unchanged.')
