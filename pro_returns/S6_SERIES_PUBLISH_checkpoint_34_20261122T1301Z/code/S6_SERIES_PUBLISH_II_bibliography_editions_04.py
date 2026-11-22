from pathlib import Path
import csv, datetime as dt, difflib, hashlib, io, json, re

R=Path(__file__).resolve().parents[1]
def sha(b):return hashlib.sha256(b).hexdigest()
def bind(p):
 b=(R/p).read_bytes();return dict(path=p,sha256=sha(b),bytes=len(b))
src=R/'S6_SERIES_PUBLISH_II.tex';bib=R/'S6_SERIES_PUBLISH_references.bib'
sb,bb=src.read_bytes(),bib.read_bytes();s,bs=sb.decode(),bb.decode()
assert sha(sb)=='7479f18411be8c59f79cfedd89a079b089c6742a81faed216b7b26e5d8ae1874'
assert sha(bb)=='3a4d5cd2c3124e5645a6f262c0d8ee1c8b4239accde43b66e25aa934b82c224c'
out=R/'records/S6_SERIES_PUBLISH_II_bibliography_editions_04';assert not out.exists()
a=s.index('\\begin{thebibliography}');z=s.index('\\end{thebibliography}',a)
parts=re.split(r'(?=\\bibitem)',s[a:z]);prefix=parts[0];entries={}
for e in parts[1:]:
 m=re.match(r'\\bibitem\[([\s\S]*?)\]\{([^{}]+)\}',e);assert m
 key=m.group(2);assert key not in entries;entries[key]=e
assert len(entries)==126
oldentries=dict(entries)
updates={
'Albanese2020':r'''\bibitem[Albanese(2021)]{Albanese2020}
Michael Albanese.

\newblock The {Yamabe} invariants of {Inoue} surfaces, {Kodaira} surfaces, and
  their blowups.

\newblock \emph{Annals of Global Analysis and Geometry}, 59\penalty0
  (2):\penalty0 179--195, 2021.
\newblock \doi{10.1007/s10455-020-09744-3}.
\newblock Citations refer to arXiv:2005.09494v2, 6 November 2020.
\newblock URL \url{https://arxiv.org/pdf/2005.09494v2}.


''',
'Catanese2002':r'''\bibitem[Catanese(2002)]{Catanese2002}
Fabrizio Catanese.

\newblock Deformation types of real and complex manifolds.

\newblock In \emph{Contemporary Trends in Algebraic Geometry and Algebraic
  Topology}, volume~5 of \emph{Nankai Tracts in Mathematics}, pages 195--238.
  World Scientific, River Edge, NJ, 2002.
\newblock \doi{10.1142/9789812777416_0009}.
\newblock Citations refer to arXiv:math/0111245v2, 30 January 2002.
\newblock URL \url{https://arxiv.org/pdf/math/0111245v2}.


''',
'LRS2019':r'''\bibitem[Lehn et~al.(2019)Lehn, Rollenske, and Schinko]{LRS2019}
Christian Lehn, S{\"o}nke Rollenske, and Caren Schinko.

\newblock The complex geometry of a hypothetical complex structure on {$S^6$}.

\newblock Revised version, arXiv:1912.09719v1, 20 December 2019.
\newblock Journal version: \emph{Differential Geometry and its Applications},
  57:\penalty0 121--137, 2018.
\newblock \doi{10.1016/j.difgeo.2017.10.015}.
\newblock Citations refer to the revised arXiv version.
\newblock URL \url{https://arxiv.org/abs/1912.09719v1}.


''',
'Steenbrink1999':r'''\bibitem[Steenbrink(1999)]{Steenbrink1999}
J.~H.~M. Steenbrink.

\newblock Cup products and mixed {Hodge} structures.

\newblock arXiv:math/9902134v1, 23 February 1999.
\newblock URL \url{https://arxiv.org/pdf/math/9902134v1}.


''',
'SchuttShioda2010':r'''\bibitem[Sch{\"u}tt and Shioda(2010)]{SchuttShioda2010}
Matthias Sch{\"u}tt and Tetsuji Shioda.

\newblock Elliptic surfaces.

\newblock In \emph{Algebraic Geometry in East Asia---Seoul 2008}, volume~60
  of \emph{Advanced Studies in Pure Mathematics}, pages 51--160.
  Mathematical Society of Japan, 2010.
\newblock \doi{10.2969/aspm/06010051}.
\newblock Section and page citations refer to arXiv:0907.0298v3,
  9 July 2010.
\newblock URL \url{https://arxiv.org/pdf/0907.0298v3}.


''',
'Greb2011':r'''\bibitem[Greb(2011)]{Greb2011}
Daniel Greb.

\newblock Rational singularities and quotients by holomorphic group actions.

\newblock \emph{Annali della Scuola Normale Superiore di Pisa, Classe di
  Scienze}, ser.~5, 10\penalty0 (2):\penalty0 413--426, 2011.
\newblock \doi{10.2422/2036-2145.2011.2.07}.
\newblock URL \url{https://www.numdam.org/item/ASNSP_2011_5_10_2_413_0.pdf}.


'''
}
for k,v in updates.items():
 assert k in entries and entries[k]!=v
 entries[k]=v

def letters(x):
 x=x.replace('\\L','L').replace('\\l','l')
 x=re.sub(r'\\[\'"^`~=.]\s*\{?([A-Za-z])\}?',r'\1',x)
 x=re.sub(r'\\[uvHckbdtr]\s*\{?([A-Za-z])\}?',r'\1',x)
 x=x.replace("'",'').replace('~',' ').replace('{','').replace('}','')
 return re.sub(r'[^a-z0-9]+',' ',x.lower()).strip()
sortkeys={}
for key,e in entries.items():
 label=re.match(r'\\bibitem\[([\s\S]*?)\]\{([^{}]+)\}',e).group(1)
 first,rest=label.split('(',1);date,tail=rest.split(')',1);full=tail.strip() or first
 authors=[letters(x) for x in re.split(r',\s*(?:and\s+)?|\s+and\s+',full)];assert all(authors)
 year=re.search(r'\d{4}',date);suffix=re.search(r'\\natexlab\{([a-z])\}',date)
 sortkeys[key]=(tuple(authors),int(year.group()) if year else 9999,suffix.group(1) if suffix else '',key)
order=sorted(entries,key=lambda k:sortkeys[k]);newbib=prefix+''.join(entries[k] for k in order)
sa=(s[:a]+newbib+s[z:]).encode()
assert sa.decode()[:a]==s[:a] and sa.decode().endswith(s[z:])
assert set(order)==set(oldentries)
assert prefix+''.join(oldentries.values())==s[a:z]
assert order.index('GrauertRemmert1984')<order.index('GrauertRiemenschneider1970') if 'GrauertRemmert1984' in order else True
recovered={}
for e in re.split(r'(?=\\bibitem)',newbib)[1:]:
 key=re.match(r'\\bibitem\[([\s\S]*?)\]\{([^{}]+)\}',e).group(2)
 assert e==entries[key]
 recovered[key]=oldentries[key] if key in updates else e
assert (s[:a]+prefix+''.join(recovered[k] for k in oldentries)+s[z:]).encode()==sb

def master_entry(key):
 m=re.search(r'(?m)^@\w+\{'+re.escape(key)+r',',bs);assert m,key
 n=bs.find('\n@',m.end());return bs[m.start():n if n>=0 else None]
master_guards=[]
def change_master(key,replacements,fields='',kind=None):
 global bs
 old=master_entry(key);new=old
 if kind:new=re.sub(r'^@\w+', '@'+kind,new,count=1)
 for oldtext,newtext in replacements:
  assert new.count(oldtext)==1,(key,oldtext)
  new=new.replace(oldtext,newtext,1)
 if fields:
  close=new.rfind('}');assert close>=0
  body=new[:close].rstrip()
  if not body.endswith(','):body+=','
  new=body+'\n'+fields+'\n'+new[close:]
 assert bs.count(old)==1
 bs=bs.replace(old,new,1)
 master_guards.append(dict(key=key,old=old,new=new))

change_master('Albanese2020',[
 ('year = {2020}','year = {2021}'),('eprint = {2005.09494}','eprint = {2005.09494v2}'),
 ('https://arxiv.org/pdf/2005.09494','https://arxiv.org/pdf/2005.09494v2')],
 '  journal = {Annals of Global Analysis and Geometry},\n  volume = {59},\n  number = {2},\n  pages = {179--195},\n  doi = {10.1007/s10455-020-09744-3},\n  citation_edition = {arXiv:2005.09494v2, 6 November 2020; exact supplied-source identity verified 22 November 2026},',kind='article')
change_master('Catanese2002',[
 ('eprint = {math/0111245}','eprint = {math/0111245v2}'),('https://arxiv.org/pdf/math/0111245','https://arxiv.org/pdf/math/0111245v2')],
 '  booktitle = {Contemporary Trends in Algebraic Geometry and Algebraic Topology},\n  series = {Nankai Tracts in Mathematics},\n  volume = {5},\n  pages = {195--238},\n  publisher = {World Scientific},\n  address = {River Edge, NJ},\n  doi = {10.1142/9789812777416_0009},\n  citation_edition = {arXiv:math/0111245v2, 30 January 2002; exact supplied-source identity verified 22 November 2026},',kind='incollection')
change_master('LRS2019',[
 ('eprint = {1912.09719}','eprint = {1912.09719v1}'),('https://arxiv.org/abs/1912.09719','https://arxiv.org/abs/1912.09719v1')],
 '  howpublished = {Revised version, arXiv:1912.09719v1, 20 December 2019},\n  publication_note = {Journal version: Differential Geometry and its Applications 57 (2018), 121--137; citations use the revised 2019 arXiv version},\n  doi = {10.1016/j.difgeo.2017.10.015},\n  citation_edition = {arXiv:1912.09719v1; exact supplied-source identity verified 22 November 2026},')
change_master('Steenbrink1999',[
 ('eprint = {math/9902134}','eprint = {math/9902134v1}'),('https://arxiv.org/pdf/math/9902134','https://arxiv.org/pdf/math/9902134v1')],
 '  howpublished = {arXiv:math/9902134v1, 23 February 1999},\n  citation_edition = {arXiv:math/9902134v1; exact supplied-source identity verified 22 November 2026},')
change_master('SchuttShioda2010',[
 ('journal = {Algebraic Geometry in East Asia---Seoul 2008}','booktitle = {Algebraic Geometry in East Asia---Seoul 2008}'),
 ('eprint = {0907.0298}','eprint = {0907.0298v3}'),('https://arxiv.org/pdf/0907.0298','https://arxiv.org/pdf/0907.0298v3')],
 '  publisher = {Mathematical Society of Japan},\n  doi = {10.2969/aspm/06010051},\n  citation_edition = {Section and page citations use arXiv:0907.0298v3, 9 July 2010; exact supplied-source identity verified 22 November 2026},',kind='incollection')
change_master('Greb2011',[], '  doi = {10.2422/2036-2145.2011.2.07},')
gr=r'''@article{GrauertRiemenschneider1970,
  author = {Grauert, Hans and Riemenschneider, Oswald},
  title = {Verschwindungss\"atze f\"ur analytische Kohomologiegruppen auf komplexen R\"aumen},
  journal = {Inventiones Mathematicae},
  volume = {11},
  number = {4},
  pages = {263--292},
  year = {1970},
  doi = {10.1007/BF01403182},
  url = {https://www.math.uni-hamburg.de/home/riemenschneider/OR1970c.pdf},
  verification = {verified at listed scope},
  source_note = {Actually read 22 November 2026: Satz 2.3 and its complete proof, printed pp.274--276; Satz 2.4 and its proof, p.277; canonical-sheaf definition and Satz 3.1 statement, p.278. The root did not read the continuation of Satz 3.1 on p.279. The exact vanishing application and proper/local duality maps are recorded in the CL comparative review. Author-hosted article PDF SHA256 610f6f5c4856bb035e497fca1e16dea77bce4e39b79dd0a01d4d8f5be8fbd03a. DOI metadata separately checked through Crossref; the primary article controls the accented title.}
}
'''
assert 'GrauertRiemenschneider1970,' not in bs
addition='\n'+gr
bs+=addition
ba=bs.encode()
undo=bs[:-len(addition)]
for g in reversed(master_guards):
 assert undo.count(g['new'])==1
 undo=undo.replace(g['new'],g['old'],1)
assert undo.encode()==bb

dp=R/'S6_SERIES_PUBLISH_defects_II.tsv';db=dp.read_bytes()
reader=csv.DictReader(io.StringIO(db.decode(),newline=''),delimiter='\t');prior=list(reader);fields=reader.fieldnames
rows=[]
def row(cid,owner,old,new,reason,loc='Bibliography'):
 q={f:'' for f in fields};q.update(change_id=cid,type='D18',statement_id=owner,old_location=loc,new_location=loc,
 old_page='pending integrated locator',new_page='pending integrated PDF',old_text=old,new_text=new,reason=reason,
 review_status='Root read exact primary metadata and preserved existing verification notes; exact inverse source/master reconstruction verified. No new proof reading or completion credit.')
 rows.append(q)
for k in updates:
 row('II-BIB04-ENTRY-'+k,'Bibliography:'+k,oldentries[k],entries[k],
     'Supply verified publication metadata and bind citations to the exact actually read arXiv edition. The five source files were byte-compared with their versioned arXiv sources. Journal pagination is not substituted for preprint locators; the revised LRS2019 edition remains explicit.')
oldpos={k:i+1 for i,k in enumerate(oldentries)}
for i,k in enumerate(order,1):
 if i!=oldpos[k]:
  row('II-BIB04-ORDER-'+k,'Bibliography:'+k,str(oldpos[k]),str(i),
      'Place all126 entries in ordered-author, year and suffix order after insertion of the verified Grauert--Riemenschneider entry. The full entry-byte permutation and its inverse are recorded.')
for g in master_guards:
 row('II-BIB04-MASTER-'+g['key'],'Bibliography:'+g['key'],g['old'],g['new'],
     'Synchronize the shared master metadata and exact cited edition while retaining every existing source_note, verification and historical note.',loc='S6_SERIES_PUBLISH_references.bib')
row('II-BIB04-MASTER-GR1970','Bibliography:GrauertRiemenschneider1970','',gr,
    'Add the exact original article, actual reading scope and verified DOI already admitted in the printed PaperII bibliography.',loc='S6_SERIES_PUBLISH_references.bib')
assert len({x['change_id'] for x in prior+rows})==len(prior)+len(rows)
buf=io.StringIO(newline='');w=csv.DictWriter(buf,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writerows(rows);append=buf.getvalue().encode()
out.mkdir()
(out/'source.diff').write_text(''.join(difflib.unified_diff(s.splitlines(True),sa.decode().splitlines(True),fromfile='II.before',tofile='II.after')))
(out/'master.diff').write_text(''.join(difflib.unified_diff(bb.decode().splitlines(True),bs.splitlines(True),fromfile='master.before',tofile='master.after')))
(out/'entry_map.json').write_text(json.dumps(dict(old_order=list(oldentries),new_order=order,sort_keys=sortkeys,
 entry_guards=[dict(key=k,old=oldentries[k],new=entries[k]) for k in updates],master_guards=master_guards,master_appended_bytes=addition,
 all_unchanged_entry_sha256={k:sha(entries[k].encode()) for k in entries if k not in updates}),indent=2)+'\n')
buf=io.StringIO(newline='');w=csv.DictWriter(buf,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);(out/'defect_rows.tsv').write_text(buf.getvalue())
record=dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),source_before_sha256=sha(sb),source_after_sha256=sha(sa),
 master_before_sha256=sha(bb),master_after_sha256=sha(ba),entry_count=126,printed_entries_edited=list(updates),
 complete_nonbibliography_source_unchanged=True,all_citation_commands_and_locators_unchanged=True,master_inverse_exact=True,source_inverse_exact=True,
 old_source_reconstruction='Undo entry permutation, then replace each new entry with the recorded exact old entry; all outer bytes are unchanged.',
 evidence=[bind('records/S6_SERIES_PUBLISH_II_bibliography_primary_03.json'),bind('records/S6_SERIES_PUBLISH_II_bibliography_primary_04.json'),
           bind('agents/continuation2_B/01CL/S6_SERIES_PUBLISH_II_B2_CL_GR_Crossref_metadata.json'),bind('records/S6_SERIES_PUBLISH_II_root_continuation2_batch79_review.json')],
 specific_scope='Existing cited preprint loci remain explicitly assigned to the same exact arXiv editions. Papikian2004Tate remains the actually read13June2004 notes, with its correct original URL and locator. No later published edition or its pagination is silently substituted. Steenbrink is identified by the actual arXivv1; the separately found institute report catalogue has not been treated as a byte-verified replacement.',
 execution_history='Initial syntax-only compilation found a missing space between else and9999 in the sort-key expression; it stopped before program execution or writes. The syntax was corrected before this run.',
 defect_rows=len(rows),defect_before_sha256=sha(db),defect_after_sha256=sha(db+append),events_added=0,required_rows_completed=0,global_D18_closed=False)
(out/'manifest.json').write_text(json.dumps(record,indent=2)+'\n')
src.write_bytes(sa);bib.write_bytes(ba)
with dp.open('ab') as f:f.write(append)
assert dp.read_bytes()==db+append
print(json.dumps(dict(manifest=bind(str((out/'manifest.json').relative_to(R))),source_sha256=sha(sa),master_sha256=sha(ba),defect_rows=len(rows),
 printed_entries={k:entries[k] for k in updates},GR_position=order.index('GrauertRiemenschneider1970')+1),indent=2))
