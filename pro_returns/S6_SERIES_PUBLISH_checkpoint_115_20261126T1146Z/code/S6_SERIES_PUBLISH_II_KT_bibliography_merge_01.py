#!/usr/bin/env python3
"""Merge two bibliography keys while preserving each exact edition and locus."""
from pathlib import Path
import csv,datetime as dt,difflib,hashlib,io,json,re
from S6_SERIES_PUBLISH_II_title_census import fingerprint as titlefp
from S6_SERIES_PUBLISH_II_D10_census import valid as d10valid,fingerprint as d10fp
R=Path(__file__).resolve().parents[1];O=R/'records/S6_SERIES_PUBLISH_II_KT_bibliography_merge_01'
csv.field_size_limit(100_000_000);sha=lambda b:hashlib.sha256(b).hexdigest()
def enc(x):return (json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode()
def bind(p):
 b=p.read_bytes();return dict(path=str(p.relative_to(R)),bytes=len(b),sha256=sha(b))
assert not O.exists();before=(R/'S6_SERIES_PUBLISH_II.tex').read_bytes();s=before.decode()
assert sha(before)=='040555937272b4892edcf2629c7ff5bd53637d0acc2062f90f8ad033156b85f1'
prior=R/'records/S6_SERIES_PUBLISH_II_bibliography_census_05.json';p=json.loads(prior.read_text())
assert sha(s[s.index(r'\begin{thebibliography}'):s.index(r'\end{thebibliography}')+len(r'\end{thebibliography}')].encode())==p['full_printed_bibliography_reading']['bibliography_sha256']
binding=R/p['exact_preprint_binding']['prior_receipt'];assert sha(binding.read_bytes())==p['exact_preprint_binding']['prior_receipt_sha256']
attached=R.parent/'S6_PUBLISH_literature_arxiv/2406.15158/ClassificationInoue-article-new.tex'
assert sha(attached.read_bytes())==p['exact_preprint_binding']['attached_source_sha256']
start=s.index(r'\bibitem[Khaled and Teleman(');end=s.index(r'\bibitem[Kodaira(',start);oldentry=s[start:end]
assert re.findall(r'\\bibitem\[[^\n]+\]\{([^}]+)\}',oldentry)==['KhaledTeleman2026','KhaledTeleman2026Journal']
entry=r'''\bibitem[Khaled and Teleman(2026)]{KhaledTeleman2026}
Zahraa Khaled and Andrei Teleman.
\newblock On the classification of {Inoue} surfaces.
\newblock \emph{Journal of Mathematical Sciences, The University of Tokyo},
  33\penalty0 (3):\penalty0 283--357, 2026.
\newblock Journal edition:
  \url{https://www.ms.u-tokyo.ac.jp/journal/33-3-1.pdf}.
\newblock Cited preprint edition: arXiv:2406.15158v4, 13 July 2026,
  \url{https://arxiv.org/pdf/2406.15158v4}.


'''
edits=[dict(start=start,end=end,old=oldentry,new=entry,edition='Both exact edition URLs retained',locus='bibliography',scope='Two entries merged')]
pairs=[(r'\cite[Sections 2.1--2.3]{KhaledTeleman2026}',r'\cite[arXiv version~4, Sections 2.1--2.3]{KhaledTeleman2026}','arXiv2406.15158v4','Sections2.1--2.3',2),
 (r'\cite[Theorem~3.1, p.~303]{KhaledTeleman2026Journal}',r'\cite[journal edition, Theorem~3.1, p.~303]{KhaledTeleman2026}','journal','Theorem3.1,p303',2),
 (r'\cite[proof of Remark~3.5, p.~305]{KhaledTeleman2026Journal}',r'\cite[journal edition, proof of Remark~3.5, p.~305]{KhaledTeleman2026}','journal','proof of Remark3.5,p305',1)]
for old,new,edition,locus,count in pairs:
 matches=list(re.finditer(re.escape(old),s));assert len(matches)==count
 for m in matches:
  a=s.rfind('\n\n',0,m.start())+2;b=s.find('\n\n',m.start())
  edits.append(dict(start=m.start(),end=m.end(),old=old,new=new,edition=edition,locus=locus,scope='Citation identity and postnote',original_paragraph=s[a:b],original_line=s.count('\n',0,m.start())+1))
new=s;inverse=[]
for g in sorted(edits,key=lambda g:g['start'],reverse=True):
 a=g['start'];assert new[a:g['end']]==g['old'];new=new[:a]+g['new']+new[g['end']:];inverse.append(dict(offset=a,old=g['old'],new=g['new']))
back=new
for g in reversed(inverse):
 a=g['offset'];assert back[a:a+len(g['new'])]==g['new'];back=back[:a]+g['old']+back[a+len(g['new']):]
assert back==s and 'KhaledTeleman2026Journal' not in new
assert len(re.findall(r'\\bibitem\[',s))==126 and len(re.findall(r'\\bibitem\[',new))==125
assert titlefp(s)==titlefp(new) and d10valid(new) and d10fp(s)==d10fp(new)
for pat in [r'\\label\{[^}]+\}',r'\\hypertarget\{[^}]+\}',r'\\tag\{[^}]+\}']:assert re.findall(pat,s)==re.findall(pat,new)
db=(R/'S6_SERIES_PUBLISH_defects_II.tsv').read_bytes();rd=csv.DictReader(io.StringIO(db.decode()),delimiter='\t');defs=list(rd);fields=rd.fieldnames;rows=[]
for i,g in enumerate(edits,1):
 row={k:'' for k in fields};row.update(change_id=f'II-KT-BIB-01-{i:03}',type='D18',statement_id='KhaledTeleman2026',old_location=g['scope']+' / '+g['locus'],old_page='journal303/305 or arXivv4sections2.1--2.3 as explicitly retained',new_location='KhaledTeleman2026 / '+g['edition']+' / '+g['locus'],new_page='same cited external locus; integrated paper page pending',old_text=g['old'],new_text=g['new'],reason='Map (old key,edition,locus) to (single key,same edition,same locus). Journal and arXiv locators remain explicit. No assertion of equality of their full contents or numbering.',review_status='Both full bibliography entries and every complete citation paragraph read; journal metadata and cited loci reopened, exact attachedv4 source binding verified. Header occurrence is inert supporting metadata. No fresh whole-proof reading or mathematical event.');rows.append(row)
def tab(rs,header=True):
 out=io.StringIO(newline='');w=csv.DictWriter(out,fieldnames=fields,delimiter='\t',lineterminator='\n')
 if header:w.writeheader()
 w.writerows(rs);return out.getvalue().encode()
now=dt.datetime.now(dt.timezone.utc).isoformat();O.mkdir();(O/'exact_edits.json').write_bytes(enc(edits));(O/'inverse.json').write_bytes(enc(inverse));(O/'defect_rows.tsv').write_bytes(tab(rows));(O/'source.diff').write_text(''.join(difflib.unified_diff(s.splitlines(True),new.splitlines(True),fromfile='II before KT bibliography merge',tofile='II after KT bibliography merge')))
primary=dict(recorded_utc=now,prior_full_bibliography_census=bind(prior),exact_preprint_binding=bind(binding),attached_source_sha256=sha(attached.read_bytes()),reopened_primary=[dict(url='https://www.ms.u-tokyo.ac.jp/journal/33-3-1.pdf',refs=['turn750514745view0','turn438689920view0','turn438689920view1'],scope='Journal title, authors,volume33(2026),pages283--357; Theorem3.1,p303; complete proof of Remark3.5,p305, as text. No whole-paper proof credit.'),dict(url='https://arxiv.org/abs/2406.15158',ref='turn750514745view1',scope='Exact version4 metadata,13July2026; title/authors and explicit preprint-version link.')],map='(oldkey,edition,locus)->(KhaledTeleman2026,sameedition,samelocus)',web_download_bytes='No primary publication downloaded by this code; web openings have no separately computed file hash.',global_master_bibliography='Unchanged: its aliases remain available for held papers and will be reconciled during five-paper integration.')
(O/'primary_reading.json').write_bytes(enc(primary))
changes=[('S6_SERIES_PUBLISH_II.tex',before,new.encode()),('S6_SERIES_PUBLISH_defects_II.tsv',db,db+tab(rows,False))]
manifest=dict(created_utc=now,source_before_sha256=sha(before),source_after_sha256=sha(new.encode()),bibliography_entries_before=126,bibliography_entries_after=125,exact_citation_transports=5,duplicate_entry_pair_merged=1,defect_rows_added=6,defect_rows_after=len(defs)+6,exact_inverse=True,mathematical_events_added=0,required_rows_closed=0,global_classes_closed=0,final_pdf_page_credit=0,D10_and_D16_fingerprints_unchanged=True,canonical_changes=[dict(path=n,before_sha256=sha(b),after_sha256=sha(a)) for n,b,a in changes],evidence=[bind(q) for q in sorted(O.iterdir())],code=bind(Path(__file__)))
mp=O/'manifest.json';mp.write_bytes(enc(manifest));mb=bind(mp)
for n,b,a in changes:assert (R/n).read_bytes()==b,n
for n,b,a in changes:(R/n).write_bytes(a)
note=f'\n\n## Paper II: one bibliography entry with explicit edition locators — {now}\n\nThe two Khaled--Teleman bibliography keys are merged into one entry containing both original edition URLs. Each of the five citations retains its exact edition and locus through explicit postnotes. The map changes only the key and makes the existing edition explicit; no equality of the two editions or their numbering is asserted. All126 original bibliography entries were read in census05; the current bibliography was byte-identical before this merge. Journal metadata and the two cited journal loci were reopened, and the exact attached arXivv4 binding was reverified.\n\nManifest `{mb["path"]}` (SHA-256 `{mb["sha256"]}`) binds six D18 records and the complete inverse. Source SHA-256 `{sha(new.encode())}`. No mathematical event, required row, global class or final-page credit is added. The shared master bibliography and held papers remain unchanged.\n'
for n in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
 with (R/n).open('ab') as f:f.write(note.encode())
print(json.dumps(dict(source_after_sha256=sha(new.encode()),manifest_sha256=mb['sha256'],defect_rows_after=len(defs)+6),indent=2))
