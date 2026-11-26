#!/usr/bin/env python3
"""Prepare bounded Yoshihara publisher/DOI correction; no central edits."""
from pathlib import Path
from datetime import datetime, timezone
import csv

root=Path(__file__).resolve().parents[1]
out=root/'agents/continuation3_conductor'
prefix='S6_SERIES_PUBLISH_c3_conductor_bib153'
s=(root/'S6_SERIES_PUBLISH_II.tex').read_text()
a=s.index(r'\bibitem[Yoshihara(1995)]{Yoshihara1995}')
b=s.index(r'\end{thebibliography}',a)
old=s[a:b].rstrip()
old_url=r'''\newblock URL
  \url{https://www.jstage.jst.go.jp/article/kyotoms1969/31/1/31_1_135/_pdf}.'''
new_url=r'''\newblock \doi{10.2977/PRIMS/1195164795}.

\newblock URL \url{https://ems.press/journals/prims/articles/3766}.'''
assert old.count(old_url)==1
new=old.replace(old_url,new_url,1)
def tsv(suffix,fields,rows):
    with (out/(prefix+suffix)).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
with (root/'S6_SERIES_PUBLISH_defects_II.tsv').open() as f:fields=next(csv.reader(f,delimiter='\t'))
row=dict(change_id='II-C3-PROV-153',type='D18',statement_id='bib:Yoshihara1995',old_location='Yoshihara1995 bibliography entry',old_page='source; final page pending',new_location='same entry',new_page='integrated build pending',old_text=old,new_text=new,reason='The complete primary title page and EMS publisher article record confirm the existing Publications RIMS 31(1), 135–143, 1995 data. The J-STAGE path prompted a metadata conflict but its opened PDF is the same published article. Add the verified DOI 10.2977/PRIMS/1195164795 and use the unambiguous publisher article URL. Keep the bibliography key, journal, year, volume, issue and pages.',review_status='Conductor read the full primary title page, the complete publisher metadata record and both exact old/new bibliography entries. Mathematical source-locus readings are already recorded in package07; this correction adds metadata comparison only. Parent admission pending.')
tsv('_edits.tsv',fields,[row])
now=datetime.now(timezone.utc)
sf=['source_id','url','version','exact_locus','sha256','bytes','own_paraphrase','reader','date_utc','storage']
sources=[dict(source_id='II-C3-BIB-Yoshihara1995-EMS-record',url='https://ems.press/journals/prims/articles/3766',version='Published article record; Publications RIMS 31(1), 1995, 135–143',exact_locus='Complete article metadata record: title, author, citation, DOI and submitted/published dates',sha256='',bytes='',own_paraphrase='The publisher confirms Hisao Yoshihara, Quotients of Abelian Surfaces, Publications RIMS31(1),135–143,1995, DOI10.2977/PRIMS/1195164795; submitted18April1994 and published28February1995. This agrees with the original PDF title page.',reader='GPT-6 Astra (OpenAI), ChatGPT Pro mode; continuation3 conductor; inherited effort not separately exposed',date_utc=now.isoformat(),storage='No saved webpage or published passages in checkpoint.'),dict(source_id='II-C3-BIB-Yoshihara1995-EMS-PDF',url='https://ems.press/content/serial-article-files/40556',version='Original published paper, 1995;10 PDF pages',exact_locus='Complete first/title page and published journal/date header; comparison with the previously opened J-STAGE PDF',sha256='dd1296b0493064f00cd9a9658e823c603a4781586d61a2572616808616165d3c',bytes='986713',own_paraphrase='The title page identifies Publications RIMS31(1995),135–143 and the communicated date18April1994. The package07 mathematical-locus readings are of this same published article through its J-STAGE reproduction; no new complete mathematical-proof reading is credited by this metadata check.',reader='GPT-6 Astra (OpenAI), ChatGPT Pro mode; continuation3 conductor; inherited effort not separately exposed',date_utc=now.isoformat(),storage='PDF outside checkpoint in temporary primary-source directory.')]
tsv('_sources.tsv',sf,sources)
with (root/'CHECK_EVENTS.tsv').open() as f:ef=next(csv.reader(f,delimiter='\t'))
event={k:'' for k in ef};event.update(statement_id='bib:Yoshihara1995',date=now.date().isoformat(),date_utc=now.isoformat(),who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 conductor agent',type='used and rechecked in this run',outcome='Read the complete primary title page, publisher article metadata and exact old/new bibliography entries. Confirmed the existing Publications RIMS31(1),135–143,1995 data; added DOI10.2977/PRIMS/1195164795 and replaced the J-STAGE path with the EMS article URL. The DOI and publisher record resolve the observed path/journal concern. No mathematical statement or source-locus conclusion changes; package07 retains the mathematical readings. Exposed metadata check only.',event_id='publish:c3:conductor:bib153',phase='publication source metadata comparison',source_file='agents/continuation3_conductor/'+prefix+'_edits.tsv',source_event_type='used and rechecked in this run',evidence_group='publish:c3:conductor:bib153',where='S6_SERIES_PUBLISH_II.tex: Yoshihara1995 bibliography entry')
tsv('_CHECK_EVENTS.tsv',ef,[event])
print('II-C3-PROV-153: one exact bibliography guard; journal/year/key unchanged; DOI and publisher URL verified.')
print('Two source records and one exposed metadata event. No central file changed; LF.')
