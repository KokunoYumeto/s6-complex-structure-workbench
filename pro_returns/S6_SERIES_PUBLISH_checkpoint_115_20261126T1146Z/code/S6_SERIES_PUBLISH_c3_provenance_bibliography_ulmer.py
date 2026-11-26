#!/usr/bin/env python3
"""Exact Ulmer–Urzúa edition proposal152; no shared writes."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation3_provenance'
s=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
a=s.index(r"\bibitem[Ulmer and Urz{\'u}a(2021)]{UlmerUrzua2021}")
b=s.index(r'\bibitem',a+1)
old=s[a:b].rstrip()
new=old.replace(r'\newblock URL \url{https://dlulmer.github.io/research/papers/2021a.pdf}.',
    r'\newblock Cited preprint edition: arXiv:2002.01906v2, 26 May 2020;'
    '\n'+r'the author date on its title page is 27 May 2020. Page locators refer'
    '\n'+r'to this preprint.'+'\n'+r'\newblock URL \url{https://arxiv.org/pdf/2002.01906v2}.')
assert old!=new
def tsv(name,rows):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,list(rows[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
tsv('S6_SERIES_PUBLISH_c3_provenance_bibliography_ulmer_edits.tsv',[dict(
    change_id='II-C3-PROV-152',type='D18',statement_id='bib:UlmerUrzua2021',
    old_location='UlmerUrzua2021 bibliography entry',old_page='source; final page pending',
    new_location='same entry',new_page='integrated build pending',old_text=old,new_text=new,
    reason='The receiving body uses §2.3 pp.5–6 of the exact24-page arXiv v2, freshly opened by conductor. The title-page margin is26May2020 and its author Date line is27May2020. Preserve the published IMRN journal data and DOI, identify the actual citation layout and replace the different author-site PDF URL.',
    review_status='Provenance read the complete title page and compared the full old/new bibliography entry; conductor read the full stated mathematical loci and monodromy table. Parent admission pending.')])
pdf=Path('/tmp/S6_SERIES_PUBLISH_c3_conductor_primary/UlmerUrzua2021_arxiv_v2.pdf')
tsv('S6_SERIES_PUBLISH_c3_provenance_bibliography_ulmer_sources.tsv',[dict(
    source_id='II-C3-BIB-UlmerUrzua2021',url='https://arxiv.org/pdf/2002.01906v2',
    version='arXiv:2002.01906v2, margin26May2020; author Date27May2020;24pages',
    exact_locus='§2 setup and uniformization pp.3–4; §2.2 p.5; §2.3 pp.5–6 including the complete local monodromy table',
    sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),bytes=pdf.stat().st_size,
    own_paraphrase='The source supplies the stated elliptic-surface setup and positive-loop local monodromy matrices. Conductor uses that exact table with the separate Kodaira fibre classification and the explicit root-family comparison; the bibliography edit adds no assertion beyond the opened edition identity.',
    reader='Conductor: complete listed mathematical loci and table. Provenance: full first page, both dates, title/authors and exact old/new metadata.',
    date_utc=datetime.now(timezone.utc).isoformat(),storage='Source bytes remain outside checkpoint.')])
print('Prepared stable bibliography proposal152 and exact source record. Shared files unchanged.')
