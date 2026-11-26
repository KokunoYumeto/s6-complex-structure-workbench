#!/usr/bin/env python3
"""Prepare two exact author-layout bibliography guards; no central writes."""
from pathlib import Path
from datetime import datetime,timezone
import csv,re
root=Path(__file__).resolve().parents[1]
out=root/'agents/continuation3_conductor'
prefix='S6_SERIES_PUBLISH_c3_conductor_bib155_156'
s=(root/'S6_SERIES_PUBLISH_II.tex').read_text()
def entry(key):
    m=re.search(r'\\bibitem\[[^\]]+\]\{'+re.escape(key)+r'\}',s)
    assert m,key
    end=s.find(r'\bibitem',m.end())
    return s[m.start():end].rstrip()
old155=entry('HuybrechtsK3Draft')
anchor155=r'\newblock Cambridge University Press, 2016.'
new155=old155.replace(anchor155,anchor155+r'''

\newblock The cited page numbers refer to the author's 449-page
  pre-publication draft (copyright 2015).''',1)
assert old155!=new155 and old155.count(anchor155)==1
old156=entry('Peters1990')
anchor156=r'\newblock Compact complex surfaces, 1990.'
new156=old156.replace(anchor156,anchor156+r'''

\newblock Author's 35-page notes for the Special Session of the
  Canadian Mathematical Society Summer Meeting, June 1990,
  \emph{Differential Geometry, Global Analysis, and Topology};
  citations use the pagination of this author PDF.''',1)
assert old156!=new156 and old156.count(anchor156)==1
def tsv(suffix,fields,data):
    with (out/(prefix+suffix)).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(data)
with (root/'S6_SERIES_PUBLISH_defects_II.tsv').open() as f:fields=next(csv.reader(f,delimiter='\t'))
rows=[]
for n,key,old,new,reason in [
(155,'HuybrechtsK3Draft',old155,new155,'The linked 449-page author PDF identifies itself on PDF page2 as a pre-publication draft and prints copyright2015. Chapter1 Proposition3.5 p.17 was opened with its complete proof in that layout. Preserve the published CUP2016 data and key while explicitly identifying the draft pagination used by the body. The PDF creation metadata is not treated as an edition date.'),
(156,'Peters1990',old156,new156,'The current author PDF title identifies the Canadian Mathematical Society Special Session/Summer Meeting of June1990 and Differential Geometry, Global Analysis, and Topology. Name this 35-page author-note layout so the cited Chapter1 pp.5–9 have an explicit version. Preserve the existing year, author, title, key and author URL; no unverified publisher or proceedings year is added.')]:
    rows.append(dict(change_id=f'II-C3-PROV-{n}',type='D18',statement_id='bib:'+key,old_location=key+' bibliography entry',old_page='source; exact final page pending',new_location='same entry',new_page='integrated final PDF pending',old_text=old,new_text=new,reason=reason,review_status='Complete exact old/new bibliography entries compared with the opened author PDF title/version pages. Mathematical readings are recorded in conductor09; this event adds version-metadata comparison only. Parent admission pending.'))
tsv('_edits.tsv',fields,rows)
now=datetime.now(timezone.utc)
sources=[
dict(source_id='II-C3-BIB-HuybrechtsK3Draft-155',url='https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf',version='449-page author pre-publication draft; copyright2015 stated on PDF p.2; CUP2016 publication data retained separately',exact_locus='Complete title page and pre-publication/copyright notice on PDF pp.1–2; Chapter1 Proposition3.5 p.17 mathematical reading belongs to conductor09',sha256='59da72d5807fd05d08ce28ceaf30a030cfc7e52b92e27778d824ac86cb1dd287',bytes='3256284',own_paraphrase='The source identifies the online copy as the draft and distinguishes the published CUP work. The guarded addition names the exact online pagination without changing the publication year or treating metadata creation as an edition.',reader='continuation3 conductor; exposed source metadata reading',date_utc=now.isoformat(),storage='/tmp/S6_SERIES_PUBLISH_c3_conductor_primary/HuybrechtsK3Global.pdf; outside checkpoint'),
dict(source_id='II-C3-BIB-Peters1990-156',url='https://cpeters1.win.tue.nl/ConfsAndSchools/Canada/surface.pdf',version='35-page author notes; title identifies June1990 Canadian Mathematical Society proceedings session',exact_locus='Complete PDF title page; Chapter1 pp.5–6,8–9 mathematical reading belongs to conductor09',sha256='51f9c99621b3819aa85894a8cdee4a528b0894364fc22b40a651f1bae55ceed3',bytes='255331',own_paraphrase='The title gives the session, meeting date and collection title. The guard identifies this author-note pagination, retaining the existing1990 entry and adding no unverified final publication data.',reader='continuation3 conductor; exposed source metadata reading',date_utc=now.isoformat(),storage='/tmp/S6_SERIES_PUBLISH_c3_conductor_primary/Peters1990.pdf; outside checkpoint')]
tsv('_sources.tsv',['source_id','url','version','exact_locus','sha256','bytes','own_paraphrase','reader','date_utc','storage'],sources)
with (root/'CHECK_EVENTS.tsv').open() as f:fields=next(csv.reader(f,delimiter='\t'))
events=[]
for row,n in zip(rows,[155,156]):
    e={k:'' for k in fields}
    e.update(statement_id=row['statement_id'],date=now.date().isoformat(),date_utc=now.isoformat(),who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 conductor agent',type='used and rechecked in this run',outcome=row['reason']+' Complete old and receiving entries read and compared. Exposed version-metadata check only; conductor09 owns the full mathematical-locus readings.',event_id=f'publish:c3:conductor:bib{n}',phase='publication source metadata comparison',source_file='agents/continuation3_conductor/'+prefix+'_edits.tsv',source_event_type='used and rechecked in this run',evidence_group=f'publish:c3:conductor:bib{n}',where='S6_SERIES_PUBLISH_II.tex: '+row['statement_id'])
    events.append(e)
tsv('_CHECK_EVENTS.tsv',fields,events)
assert all('\r' not in r[k] for r in rows for k in ['old_text','new_text'])
print('II-C3-PROV-155 and156: two exact bibliography version guards, two source rows, two exposed metadata events; LF; no central writes.')
