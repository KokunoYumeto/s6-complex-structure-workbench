#!/usr/bin/env python3
"""Stable continuation-3 metadata proposals 149–151; no shared writes."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation3_provenance'
main=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
now=datetime.now(timezone.utc).isoformat()

def tsv(name,rows):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,list(rows[0]),delimiter='\t',lineterminator='\n')
        w.writeheader();w.writerows(rows)

a=main.index(r'\bibitem[Dloussky and Teleman(2012)]{DlousskyTeleman2012}')
b=main.index(r'\bibitem',a+1)
old=main[a:b].rstrip()
new=old.replace(r'\newblock URL \url{https://arxiv.org/pdf/1012.5247}.',
    r'\newblock Cited preprint edition: arXiv:1012.5247v2, 5 October 2011;'
    '\n'+r'page and remark locators refer to this edition.'+'\n'
    +r'\newblock URL \url{https://arxiv.org/pdf/1012.5247v2}.')
assert old!=new
rows=[dict(change_id='II-C3-PROV-149',type='D18',statement_id='bib:DlousskyTeleman2012',
    old_location='DlousskyTeleman2012 bibliography entry',old_page='source; final page pending',
    new_location='same entry',new_page='integrated build pending',old_text=old,new_text=new,
    reason='The opened PDF title-page margin identifies arXiv v2 dated 5 October 2011; Remark 2.7 is on printed p.9. Keep the published journal and DOI and pin the body-citation layout.',
    review_status='Title page and complete Remark 2.7 read from the conductor cached primary PDF; exact old/new entry compared; parent admission pending.')]
old=r'''The final spanning step in \cite[Theorem~3.1, proof, p.~85]{CDP98}
reaches the whole target exactly when the indicated invariant lattice'''
new=r'''The final spanning step in \cite[Theorem~3.1, proof, final paragraph, p.~86]{CDP98}
reaches the whole target exactly when the indicated invariant lattice'''
assert main.count(old)==1
rows.append(dict(change_id='II-C3-PROV-150',type='D18',statement_id='cdp:st:D.1.10',
    old_location='D.1.10 final statement sentence',old_page='source; final page pending',
    new_location='same sentence',new_page='integrated build pending',old_text=old,new_text=new,
    reason='The proof diagram starts on printed p.85, but its finite-index and complex-span conclusion is the final paragraph on printed p.86. Read the complete Theorem 3.1 setup, preparatory lemmas and proof on pp.84–86.',
    review_status='Complete earlier D.1.10 owner and primary theorem proof read; locator-only correction, with mathematical content unchanged.'))
tsv('S6_SERIES_PUBLISH_c3_provenance_bibliography_dt_edits.tsv',rows)

pdf=Path('/tmp/S6_SERIES_PUBLISH_c3_conductor_primary/DT2012_v2.pdf')
tsv('S6_SERIES_PUBLISH_c3_provenance_bibliography_dt_sources.tsv',[dict(
    source_id='II-C3-BIB-DlousskyTeleman2012',url='https://arxiv.org/pdf/1012.5247v2',
    version='arXiv:1012.5247v2, 5 October 2011; Mathematische Annalen353 (2012),1283–1314',
    exact_locus='Remark 2.7, printed p.9; complete remark and preceding classification attribution',
    sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),bytes=pdf.stat().st_size,
    own_paraphrase='For a minimal class VII surface with a nonempty homologically trivial effective divisor, the listed possibilities are Hopf elliptic curves or an Enoki rational cycle; the remark attributes its classification input to its reference7. The bibliography proposal pins this layout and does not add a new classification claim.',
    reader='Conductor: complete cited mathematical context. Provenance: title-page version/date and complete Remark2.7, then old/new bibliography.',
    date_utc=now,online_status='Conductor fresh primary download; provenance web reopen returned DisabledError, so the exact cached primary PDF was read.',
    storage='Primary PDF and extracted text remain outside checkpoint; no source content copied into deliverables.')])

old='Lemma 1.5 asserts local freeness of all higher direct images after lower direct images vanish on a base curve.'
new='Lemma 1.5 asserts local freeness of every higher direct image of a locally free sheaf under a surjective holomorphic map from a smooth compact complex threefold to a smooth curve; it imposes no vanishing hypothesis on the lower direct images.'
targets=[
    'agents/continuation3_provenance/S6_SERIES_PUBLISH_c3_provenance_literature_claims.tsv',
    'agents/continuation3_provenance/S6_SERIES_PUBLISH_c3_provenance_claim_rows.tsv',
    'agents/continuation3_provenance/S6_SERIES_PUBLISH_c3_provenance_report.md',
    'S6_SERIES_PUBLISH_provenance_checks.tsv',
]
occurrences={p:(ROOT/p).read_text().count(old) for p in targets}
assert all(occurrences.values()),occurrences
tsv('S6_SERIES_PUBLISH_c3_provenance_A2_correction.tsv',[dict(
    change_id='II-C3-PROV-151',type='D25',statement_id='II-C3-LIT-A2',
    old_location='Admitted provenance paraphrase, not manuscript mathematics',
    old_page='record field; not applicable',new_location='same field in each identified record',
    new_page='record field; not applicable',old_text=old,new_text=new,
    reason='Fresh complete reading of CDP98 Lemma1.5 pp.79–80 found that the recorded established-scope sentence had inserted a hypothesis absent from the published statement. The lemma itself asserts local freeness for every higher direct image. The concrete Poincaré-product counterexample additionally has vanishing zeroth and first direct images; that property belongs to the example, not to the source hypotheses. The counterexample is not changed.',
    review_status='Correction proposed as a new stable row; admitted earlier IDs and shared records are untouched.',
    targets='; '.join(f'{p} ({occurrences[p]} occurrence)' for p in targets),
    source_url='https://www.cambridge.org/core/services/aop-cambridge-core/content/view/79BEA1EB6CF23BB9AEBCF4677C82B108/S0010437X98000360a.pdf/the-algebraic-dimension-of-compact-complex-threefolds-with-vanishing-second-betti-number.pdf',
    source_sha256='7e97396a1bea596bd086f6f1fb948ac418a2455a4562b24ad37e38227f512b7e',date_utc=now)])
print('Prepared stable source proposals149–150 and record-only correction151. Shared files unchanged.')
