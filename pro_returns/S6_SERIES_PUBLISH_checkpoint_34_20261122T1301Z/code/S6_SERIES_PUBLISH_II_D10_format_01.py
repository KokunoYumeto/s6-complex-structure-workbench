#!/usr/bin/env python3
"""Remove depth-label glyphs with an exact item-tree identity; six read proof pairs."""
from pathlib import Path
import collections,csv,datetime as dt,difflib,hashlib,io,json,re
from S6_SERIES_PUBLISH_II_title_census import headers,fingerprint
R=Path(__file__).resolve().parents[1];O=R/'records/S6_SERIES_PUBLISH_II_D10_format_01';Q=R/'records/S6_SERIES_PUBLISH_II_D10_step_reading_01'
csv.field_size_limit(100_000_000);sha=lambda b:hashlib.sha256(b).hexdigest()
def enc(x):return (json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode()
def bind(p):
 b=p.read_bytes();return dict(path=str(p.relative_to(R)),bytes=len(b),sha256=sha(b))
def rd(n):
 b=(R/n).read_bytes();r=csv.DictReader(io.StringIO(b.decode()),delimiter='\t');return b,list(r),r.fieldnames
def tab(rows,fields,header=True):
 o=io.StringIO(newline='');w=csv.DictWriter(o,fieldnames=fields,delimiter='\t',lineterminator='\n')
 if header:w.writeheader()
 w.writerows(rows);return o.getvalue().encode()
assert not O.exists();old=(R/'S6_SERIES_PUBLISH_II.tex').read_bytes();s=old.decode()
assert sha(old)=='83a729acc0dbd5de32e7186b91c1c2eb3f4b8d302c6098628e94cf454393f028'
pair_index=json.loads((Q/'index.json').read_text());pairs=pair_index['proof_pairs']
for pair in pairs:
 for kind in ['before','after']:
  b=(R/pair[kind]['path']).read_bytes();assert sha(b)==pair[kind]['sha256'] and len(b)==pair[kind]['bytes']
 assert s.count((R/pair['before']['path']).read_text())==1,pair['owner']
envs,hs=headers(s)
def owner(pos):
 line=s.count('\n',0,pos)+1;h=[h for h in hs if h['source_line']<=line][-1]
 return (h['labels'][0] if h['labels'] else 'II:section'),h['tags'],line
fmt={r'label={$\langle1\rangle$\arabic*.}':r'label=\arabic*.',r'label={$\langle2\rangle$\arabic*.}':r'label=(\arabic*)'}
enum=re.compile(r'\\begin\{enumerate\}(\[[^\n]*\])?|\\end\{enumerate\}')
depth=0;spans=[];counts=collections.Counter()
for m in enum.finditer(s):
 if m.group().startswith(r'\end'):depth-=1;assert depth>=0;continue
 depth+=1
 if r'\langle' not in m.group():continue
 d=int(re.search(r'\\langle(\d+)\\rangle',m.group())[1]);assert depth==d
 token=next(k for k in fmt if k in m.group());a=m.start()+m.group().index(token);own,tags,line=owner(a)
 spans.append(dict(start=a,end=a+len(token),old=token,new=fmt[token],kind='enumeration label representation',owner=own,tags=tags,line=line,depth=d,reason='The ordered item tree and integer counter are unchanged. The old displayed (depth,n) glyph maps to n at depth1 and (n) at depth2; every other option and body byte is retained.'));counts[d]+=1
assert depth==0 and len(spans)==306 and counts=={1:194,2:112}
assert len(re.findall(r'\\langle[12]\\rangle',s))==len(spans)
step=re.compile(r'\\item\s*(?:\\noindent\s*)?\\textbf\{Step\s*1\.\}')
for m in step.finditer(s):
 own,tags,line=owner(m.start());spans.append(dict(start=m.start(),end=m.end(),old=m.group(),new=r'\item',kind='duplicate first-item marker',owner=own,tags=tags,line=line,reason='The proof contains one item. Its enumerated first item and immediately repeated bold Step1 name the same tree node; retain the item and remove its second printed marker. The full original/revised proof pair was read.'))
assert len(spans)==312;spans.sort(key=lambda x:x['start'])
for a,b in zip(spans,spans[1:]):assert a['end']<=b['start']
new=s;inverse=[];delta=0
for g in spans:
 a=g['start']+delta;assert new[a:a+len(g['old'])]==g['old'];inverse.append(dict(offset=a,old=g['old'],new=g['new']))
 new=new[:a]+g['new']+new[a+len(g['old']):];delta+=len(g['new'])-len(g['old'])
back=new
for g in reversed(inverse):
 a=g['offset'];assert back[a:a+len(g['new'])]==g['new'];back=back[:a]+g['old']+back[a+len(g['new']):]
assert back==s and fingerprint(s)==fingerprint(new)
assert re.findall(r'\\(?:begin\{enumerate\}|end\{enumerate\}|item\b)',s)==re.findall(r'\\(?:begin\{enumerate\}|end\{enumerate\}|item\b)',new)
for pair in pairs:assert new.count((R/pair['after']['path']).read_text())==1,pair['owner']
for pat in [r'\\label\{[^}]+\}',r'\\hypertarget\{[^}]+\}',r'\\tag\{[^}]+\}',r'\\StatementRecord\{[^}]+\}\{[^}]+\}\{[^}]+\}']:assert re.findall(pat,s)==re.findall(pat,new)
assert not re.search(r'\\langle[12]\\rangle',new) and not step.search(new)
now=dt.datetime.now(dt.timezone.utc).isoformat();db,defects,df=rd('S6_SERIES_PUBLISH_defects_II.tsv');dr=[]
for g in spans:
 row={k:'' for k in df};row.update(change_id=f'II-D10-FORMAT-01-{len(dr)+1:03}',type='D10',statement_id=g['owner'],old_location=f"source line{g['line']}; "+g['kind'],old_page='exact pre-edit source locus bound',new_location=g['owner'],new_page='pending integrated build',old_text=g['old'],new_text=g['new'],reason=g['reason'],review_status='Exact source-span inverse, unchanged mathematical body bytes and unchanged ordered item tree verified. Six complete proof pairs read for the duplicate markers. Final PDF page inspection pending.');dr.append(row)
eb,events,ef=rd('CHECK_EVENTS.tsv');ev=[]
for i,pair in enumerate(pairs,1):
 e={k:'' for k in ef};e.update(statement_id=pair['owner'],date='2026-11-22',date_utc=now,who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; S6_SERIES_PUBLISH continuation2 root',type='used and rechecked in this run',outcome='Read the complete original and revised proof pair before admission. The one-item proof retains every mathematical byte; its depth1 glyph prefix and duplicate bold Step1 marker are removed by the exact item-node identity. The pair still matches the current source after Picard admission. All mathematical statements, displays, labels and proof order are unchanged. No independent derivation, required-row closure or final-page credit.',event_id=f'publish:D10-format01:proof{i:02}',phase='publication editorial comparison',source_file=pair['before']['path'],source_row='1',source_event_type='used and rechecked in this run',evidence_group='publish:D10-format01:six-first-item-proofs',publish_input_file='records/S6_SERIES_PUBLISH_II_D10_format_01/manifest.json',where='Complete proof pair; '+pair['owner']);assert e['event_id'] not in {x['event_id'] for x in events};ev.append(e)
rb=(R/'records/S6_SERIES_PUBLISH_additional_event_bundles.json').read_bytes();reg=json.loads(rb);bundle=tab(ev,ef)
reg['bundles'].append(dict(path='records/S6_SERIES_PUBLISH_II_D10_format_01/event_rows.tsv',bytes=len(bundle),sha256=sha(bundle),admission_manifest='records/S6_SERIES_PUBLISH_II_D10_format_01/manifest.json'))
O.mkdir();(O/'instance_map.json').write_bytes(enc(spans));(O/'inverse.json').write_bytes(enc(inverse));(O/'defect_rows.tsv').write_bytes(tab(dr,df));(O/'event_rows.tsv').write_bytes(bundle)
(O/'source.diff').write_text(''.join(difflib.unified_diff(s.splitlines(True),new.splitlines(True),fromfile='II before D10format01',tofile='II after D10format01')))
sty=Path('/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty');sb=sty.read_bytes()
reading=dict(recorded_utc=now,complete_proof_pairs_actually_read=pairs,reading_scope='All twelve complete before/after files were actually displayed and read before Picard admission. Their full hashes are preserved, and all six old/new pairs replay byte-identically on this admission. The global306 label-option changes are a representation operation with every remaining proof byte and the complete item-tree token sequence preserved; they claim no306 new proof readings.',implementation_source=dict(path=str(sty),bytes=len(sb),sha256=sha(sb),actual_loci_read='enumitem.sty lines513–561,905–938,1392–1404: label sets itemlabel/ref representation; normlabel uses the existing depth counter; usecounter unchanged.'),exact_map='Each intrinsic enumeration-tree address is sent to itself, and its integer counter n to the same n. Only its rendered label changes: depth1 prefix<1>n. -> n.; depth2 prefix<2>n. -> (n). The duplicate Step1 names the same first and only item. Labels, counter choice, item order, all other options and mathematical bodies remain exact.',integrated_verification='Any item-reference glyph change follows this same label representation in enumitem. Final integrated auxiliary and page inspection remain open.',independent_credit=0,final_pdf_page_credit=0)
(O/'reading_and_map.json').write_bytes(enc(reading))
changes=[('S6_SERIES_PUBLISH_II.tex',old,new.encode()),('S6_SERIES_PUBLISH_defects_II.tsv',db,db+tab(dr,df,False)),('CHECK_EVENTS.tsv',eb,eb+tab(ev,ef,False)),('records/S6_SERIES_PUBLISH_additional_event_bundles.json',rb,enc(reg))]
manifest=dict(created_utc=now,source_before_sha256=sha(old),source_after_sha256=sha(new.encode()),format_instances=306,depth_counts=dict(counts),duplicate_markers=6,defect_rows_added=len(dr),defect_rows_after=len(defects)+len(dr),events_added=6,event_groups=1,ledger_rows_after=len(events)+6,exact_inverse=True,all_other_source_bytes_unchanged=True,ordered_item_tree_unchanged=True,D16_header_fingerprint=fingerprint(new),D16_projection_unchanged=True,mathematical_events_type='used and rechecked in this run',required_rows_closed=0,global_defect_classes_closed=0,remaining_D10_gate='The source-wide header/navigation log coverage and the front-matter description require explicit completion; this formatting packet alone does not close D10.',final_pdf_page_credit=0,canonical_changes=[dict(path=n,before_sha256=sha(b),after_sha256=sha(a)) for n,b,a in changes],evidence=[bind(p) for p in sorted(O.iterdir())],code=bind(Path(__file__)))
mp=O/'manifest.json';mp.write_bytes(enc(manifest));mb=bind(mp)
for n,b,a in changes:assert (R/n).read_bytes()==b
for n,b,a in changes:(R/n).write_bytes(a)
note=f'''\n\n## Paper II: proof-list representation — {now}\n\nThe306 depth-prefixed proof-list formats are now ordinary numbered lists:194 outer lists use n.,112 inner lists use (n). The exact map fixes every intrinsic item-tree address and integer counter. All other list options, all mathematical body bytes, every label and every display are unchanged. Six one-item proofs also lose a duplicated bold Step1 marker; all six complete old/new pairs were actually read and their exact hashes remain valid after the Picard consolidation.\n\nThe312 individual D10 edits and six exposed-reread events in one evidence group are bound in `{mb['path']}` (SHA-256 `{mb['sha256']}`). The ledger has {len(events)+6} rows. Source SHA-256 is `{sha(new.encode())}`. This has no independent-check or final-page credit, and D10 remains open pending its complete source-wide log audit and the front-matter correction.\n'''
for n in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
 with (R/n).open('ab') as f:f.write(note.encode())
(O/'admission_receipt.json').write_bytes(enc(dict(recorded_utc=dt.datetime.now(dt.timezone.utc).isoformat(),manifest=mb,canonical_after=[bind(R/n) for n,_,_ in changes])))
print(json.dumps({k:manifest[k] for k in ['created_utc','source_after_sha256','format_instances','duplicate_markers','defect_rows_added','defect_rows_after','ledger_rows_after']},indent=2));print('Manifest',mb['sha256'])
