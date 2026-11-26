from pathlib import Path
import csv,datetime as dt,difflib,hashlib,io,json,re

R=Path(__file__).resolve().parents[1]
def sha(b):return hashlib.sha256(b).hexdigest()
def bind(p):
 b=(R/p).read_bytes();return dict(path=p,sha256=sha(b),bytes=len(b))
src=R/'S6_SERIES_PUBLISH_II.tex';before=src.read_bytes();s=before.decode()
assert sha(before)=='fabbb3c55cd5c15301712eeac140a9e016a1548a58a8d3eb3c14d8fc5c45e361'
a=s.index('\\begin{thebibliography}');b=s.index('\\end{thebibliography}',a)
chunks=re.split(r'(?=\\bibitem)',s[a:b]);prefix=chunks[0];entries=chunks[1:]
assert len(entries)==125
old={};meta={}
for i,e in enumerate(entries):
 m=re.match(r'\\bibitem\[([\s\S]*?)\]\{([^{}]+)\}',e);assert m
 label,key=m.groups();assert key not in old
 old[key]=e;meta[key]=dict(old_position=i+1,citation_label=label)
new=dict(old);reasons={k:[] for k in old};guards=[]
def edit(key,x,y,reason):
 assert new[key].count(x)==1,(key,x)
 guards.append(dict(key=key,old=x,new=y,reason=reason))
 new[key]=new[key].replace(x,y,1);reasons[key].append(reason)
marker='\\newblock \\emph{Verified}.\n'
assert sum(e.count(marker) for e in entries)==73
for key in new:
 if marker in new[key]:edit(key,marker,'','Remove the production verification annotation; the historical verification records remain unchanged.')
edit('AKMW2002','\\newblock URL \\url{https://arxiv.org/pdf/math/9904135}.',
 '\\newblock \\doi{10.1090/S0894-0347-02-00396-X}.',
 'Use the official publisher-deposited DOI for the stated2002 journal edition; verified title, authors, volume15(3) and pp531--572 in Crossref.')
edit('Fujimoto1988Log','\\newblock URL\n  \\url{https://scispace.com/pdf/logarithmic-transformations-on-elliptic-fiber-spaces-1uinrvp8jj.pdf}.',
 '\\newblock \\doi{10.1215/kjm/1250520560}.',
 'Replace the third-party copy with the official publisher-deposited DOI, matching author, title, volume28(1), year1988 and pp91--110. Retain the historical journal title printed in that edition.')
edit('Lagrange1770','\\newblock URL\n  \\url{https://yuvalfilmus.cs.technion.ac.il/Manuscripts/Lagrange%20four%20square%20theorem.pdf}.\n','',
 'Remove the third-party copy link; retain the complete1868 collected-works edition, volumeIII and pp189--201.')
edit('Siersma1991Variation','\\newblock URL \\url{https://www.maths.ed.ac.uk/~v1ranick/papers/siersma.pdf}.\n','',
 'Remove the third-party course copy; retain the complete journal data and DOI.')
edit('Hatcher2002','Hatcher(2002{\\natexlab{a}})','Hatcher(2002)',
 'Remove the obsolete year suffix from the citation label of the sole Hatcher2002 entry.')
edit('Hatcher2002','Cambridge University Press, 2002{\\natexlab{a}}.','Cambridge University Press, 2002.',
 'Match the publisher year to the sole Hatcher2002 citation label.')
edit('BHPV2004E','Springer, Berlin, Heidelberg, 2 edition, 2004.','Springer, Berlin, Heidelberg, second edition, 2004.',
 'Write the existing edition number in standard bibliographic English.')
edit('Bingener1980','analytische funktoren.','analytische Funktoren.',
 'Restore German noun capitalization in the existing title.')
edit('Grauert1962E','modifikationen und exzeptionelle analytische mengen.','Modifikationen und exzeptionelle analytische Mengen.',
 'Restore German noun capitalization in the existing title.')
edit('CDP98','second betti number.','second Betti number.',
 'Restore the proper name in the existing title.')
edit('Kulikov1977','surfaces and enriques surfaces.','surfaces and Enriques surfaces.',
 'Restore the proper name in the existing title.')
edit('DemaillyHodgeAuthor2002','$l^2$ hodge theory and vanishing theorems.','$L^2$ Hodge theory and vanishing theorems.',
 'Restore the conventional L2 notation and proper name in the existing title.')
edit('DemaillyHodgeAuthor2002',
 '\\newblock Author-hosted PDF body: Theorem 3.15, p. 15 (physical PDF p. 27), and\n  Theorems 7.1--7.2, p. 32 (physical PDF p. 44);\\allowbreak{} opened 19 November 2026.\n  Scope: classical Green and Hodge inputs. The receiving finite-kernel\n  analytic-minor argument is derived separately.',
 "\\newblock Author's version; cited page numbers refer to the chapter\n  pagination of this PDF.",
 'Remove the reading date and production description while preserving the exact author-version pagination convention used by the citations.')
edit('Papikian2004Tate','Author notes, 13 June 2004, 2004.','Author notes, 13 June 2004.',
 'Remove the duplicated year while preserving the exact dated notes edition.')
edit('LiuRollenske2012SLC','doi:\\href{https://doi.org/10.4418/2012.67.2.14}{10.4418/2012.67.2.14}.',
 '\\doi{10.4418/2012.67.2.14}.','Use the existing common DOI macro without changing the identifier.')
edit('Remmert1957Mappings','DOI \\href{https://doi.org/10.1007/BF01342886}{10.1007/BF01342886}.',
 '\\doi{10.1007/BF01342886}.','Use the existing common DOI macro without changing the identifier.')

# Sorting keys affect only the entry permutation. Every old and new entry is
# retained verbatim in the inverse map below; no citation identifier changes.
def alphabet_key(x):
 x=x.replace('\\L','L').replace('\\l','l')
 x=re.sub(r'\\[\'"^`~=.]\s*\{?([A-Za-z])\}?',r'\1',x)
 x=re.sub(r'\\[uvHckbdtr]\s*\{?([A-Za-z])\}?',r'\1',x)
 x=x.replace('~',' ').replace('{','').replace('}','')
 return re.sub(r'[^a-z0-9]+',' ',x.lower()).strip()
def sortkey(key):
 label=meta[key]['citation_label'];author,rest=label.split('(',1)
 date,tail=rest.split(')',1)
 full=tail.strip() or author
 year=re.search(r'\d{4}',date)
 title=re.search(r'\\newblock ([\s\S]*?)\n\n',new[key])
 value=(alphabet_key(full),int(year.group()) if year else 9999,alphabet_key(title.group(1) if title else key),key)
 meta[key]['author_sort_key']=value[0];meta[key]['sort_key']=list(value)
 return value
ordered=sorted(new,key=sortkey)
newbib=prefix+''.join(new[k] for k in ordered)
assert len(ordered)==125 and set(ordered)==set(old)
assert prefix+''.join(old[k] for k in old)==s[a:b]
inverse=dict(new); 
for g in reversed(guards):
 assert inverse[g['key']].count(g['new'])==1 if g['new'] else True
 # The exact old entry binding supplies the unambiguous inverse of deletion.
inverse=old
assert prefix+''.join(inverse[k] for k in sorted(old,key=lambda k:meta[k]['old_position']))==s[a:b]
after=(s[:a]+newbib+s[b:]).encode()
assert s[:a]==after.decode()[:a]
assert after.decode().endswith(s[b:])
for pat in [r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}',r'\\tag\{([^}]+)\}']:
 assert re.findall(pat,s)==re.findall(pat,after.decode())
assert not re.search(r'scispace\.com|yuvalfilmus\.cs|v1ranick/papers/siersma',newbib)
assert marker not in newbib
now=dt.datetime.now(dt.timezone.utc).isoformat();out=R/'records/S6_SERIES_PUBLISH_II_bibliography_style_02';assert not out.exists()
defects_path=R/'S6_SERIES_PUBLISH_defects_II.tsv';db=defects_path.read_bytes()
rd=csv.DictReader(io.StringIO(db.decode(),newline=''),delimiter='\t');prior=list(rd);fields=rd.fieldnames
rows=[];entrymap=[]
for pos,key in enumerate(ordered,1):
 beforepos=meta[key]['old_position'];why=reasons[key].copy()
 if pos!=beforepos:why.append('Move entry from position'+str(beforepos)+' to position'+str(pos)+' by the recorded author/year/title order.')
 entrymap.append(dict(key=key,**meta[key],new_position=pos,old_sha256=sha(old[key].encode()),new_sha256=sha(new[key].encode()),old_entry=old[key],new_entry=new[key],reasons=why))
 if not why:continue
 row={k:'' for k in fields};row.update(change_id='II-BIB02-'+key,type='D18'+(',D08' if marker in old[key] else ''),statement_id='Bibliography:'+key,
  old_location='Bibliography entry '+key+'; position '+str(beforepos),old_page='pending integrated locator',new_location='Bibliography entry '+key+'; position '+str(pos),new_page='pending integrated PDF',
  old_text=old[key],new_text=new[key],reason=' '.join(why),review_status='Root read all125 original entries, every changed passage and exact entry permutation; edition-specific citation keys preserved.')
 rows.append(row)
assert len({r['change_id'] for r in prior+rows})==len(prior)+len(rows)
buf=io.StringIO(newline='');w=csv.DictWriter(buf,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writerows(rows);append=buf.getvalue().encode()
out.mkdir()
(out/'entry_map.json').write_text(json.dumps(dict(created_utc=now,old_order=list(old),new_order=ordered,entries=entrymap,guards=guards),indent=2)+'\n')
(out/'source.diff').write_text(''.join(difflib.unified_diff(s.splitlines(True),after.decode().splitlines(True),fromfile='II.before',tofile='II.after')))
buf=io.StringIO(newline='');w=csv.DictWriter(buf,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);(out/'defect_rows.tsv').write_text(buf.getvalue())
manifest=dict(created_utc=now,source_before_sha256=sha(before),source_after_sha256=sha(after),source_bytes_before=len(before),source_bytes_after=len(after),
 bibliography_entries=125,removed_production_markers=73,literal_guards=len(guards),defect_rows=len(rows),
 old_bibliography_sha256=sha(s[a:b].encode()),new_bibliography_sha256=sha(newbib.encode()),exact_original_entry_reconstruction=True,
 entry_map=bind(str((out/'entry_map.json').relative_to(R))),source_diff=bind(str((out/'source.diff').relative_to(R))),
 primary_metadata=bind('records/S6_SERIES_PUBLISH_II_bibliography_crossref_02.json'),
 defect_before_sha256=sha(db),defect_after_sha256=sha(db+append),
 reading='All125 original entries were completely read in the preceding bounded bibliography reads; changed entries and every literal change were read again before this application. The explicit old/new entry map preserves the edition and citation identity of every entry. Root read both exact Crossref metadata records. No article reading credit follows from a DOI lookup.',
 mathematical_source_outside_bibliography_unchanged=True,all_labels_and_targets_unchanged=True,events_added=0,required_rows_completed=0,global_D18_closed=False,publication_page_credit=0,
 scope='Author/year/title bibliography order, explicit reversible entry edits, DOI identity repairs, removal of three third-party copies and73 production annotations. Broader citation/edition audit and final page review remain open.')
(out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
src.write_bytes(after)
with defects_path.open('ab') as f:f.write(append)
assert defects_path.read_bytes()==db+append
print(json.dumps(dict(manifest=bind(str((out/'manifest.json').relative_to(R))),source_sha256=sha(after),defect_rows=len(rows),entries=len(ordered),new_order=ordered)))
