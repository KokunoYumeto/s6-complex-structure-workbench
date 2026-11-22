from pathlib import Path
import csv, datetime as dt, difflib, hashlib, io, json, re

R=Path(__file__).resolve().parents[1]
csv.field_size_limit(100_000_000)
def sha(b):return hashlib.sha256(b).hexdigest()
def bind(p):return dict(path=p,sha256=sha((R/p).read_bytes()),bytes=(R/p).stat().st_size)
def rows(b,delimiter='\t'):
 reader=csv.DictReader(io.StringIO(b.decode(),newline=''),delimiter=delimiter)
 return list(reader),reader.fieldnames
def encode(rr,fields,delimiter='\t',header=True):
 f=io.StringIO(newline='');w=csv.DictWriter(f,fields,delimiter=delimiter,lineterminator='\n')
 if header:w.writeheader()
 w.writerows(rr);return f.getvalue().encode()

planpath='agents/continuation2_root/S6_SERIES_PUBLISH_II_RAT6_restore_v2_plan.json'
plan=json.loads((R/planpath).read_text())
assert bind(planpath)['sha256']=='f31a962d0e0f6175c845c151b70f61b49487014944ac36fd2cb95b66c615445a'
output=R/'records/S6_SERIES_PUBLISH_II_RAT6_restore_20261122';assert not output.exists()
sourcepath=R/'S6_SERIES_PUBLISH_II.tex';sourceold=sourcepath.read_bytes();source=sourceold.decode()
assert sha(sourceold)==plan['source_before_sha256']
bibpath=R/'S6_SERIES_PUBLISH_references.bib';bibold=bibpath.read_bytes();bib=bibold.decode()
assert sha(bibold)==plan['bib_before_sha256']
ledgerpath=R/'CHECK_EVENTS.tsv';ledgerold=ledgerpath.read_bytes();ledger,fields=rows(ledgerold)
assert sha(ledgerold)=='f4a01e9df7e09a3997999b8f650ea228f4cf5c8d7619eaaf80dfb353dceeb57f'
defectpath=R/'S6_SERIES_PUBLISH_defects_II.tsv';defectold=defectpath.read_bytes();defects,df=rows(defectold)
completion=bind('records/S6_SERIES_PUBLISH_required_check_completion_manifest.json')
invpath=R/'S6_SERIES_PUBLISH_inventory.csv';invold=invpath.read_bytes();inventory,ivf=rows(invold,',')
now=dt.datetime.now(dt.timezone.utc).isoformat()
for p in ['restored_block','BW_proposed','freeze']:
 assert bind(plan[p]['path'])['sha256']==plan[p]['sha256']
for e in plan['source_edits']:
 assert source.count(e['old'])==1
 source=source.replace(e['old'],e['new'],1)
assert sha(source.encode())==plan['source_after_sha256']
for e in plan['bib_edits']:
 if 'append' in e:bib+=e['append']
 else:
  assert bib.count(e['old'])==1;bib=bib.replace(e['old'],e['new'],1)
assert sha(bib.encode())==plan['bib_after_sha256']
# Preserve all open target blocks; this support edit cannot alter a released target.
bx=(R/'agents/ii_infra/released_proofs/01BX/b168cbeb6186b92e/S6_SERIES_PUBLISH_full_owning_block.tex').read_text()
assert source.count(bx)==1
for pattern in [r'\\hypertarget\{([^}]+)\}',r'\\label\{([^}]+)\}']:
 a=re.findall(pattern,sourceold.decode());b=re.findall(pattern,source)
 for token in set(a):assert a.count(token)==b.count(token),token

review=dict(created_utc=now,checker='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode, root, second continuation; reasoning effort not separately exposed',
 actual_reading='Complete five-section supporting derivation and all19 Koszul output rows read before the original RAT6 proof. Freeze06:35:14.392934UTC. The complete original research proof was subsequently read from its begin-proof to end-proof, including the full branch/Puiseux case analysis, all five displays/tables and the program paragraph. The complete finalRAT6v2 block and complete consolidatedBW block, including all12 proof items, have been read. Primary-page readings are individually stated in the derivation and source records.',
 chronology='Historical inventory proof-summary exposure preceded the RAT6 freeze and is explicitly disclosed. The target proof itself was opened only after that freeze. This support operation claims only used-and-rechecked events, with no extra independent-check or computation credit. BW has its separate admitted batch53 independent check. Source-neighbour inspection also exposed the opening CJ proof items1-4; root claims no independent CJ check from that inspection.',
 comparison=[
 'The original complete low-delta branch/intersection classification and the frozen Arnold-determinator derivation give exactly A1-10,D4-9,E6-8. The primary p95 J2,0 row has Milnor number10 but its three contact-two branches give delta6, so it is excluded by the stated bound. The explicit coordinate/unit-cube-root map and inverse identify each actual suspension.',
 'The original pg lattice formula and its inclusive boundary agree with the frozen graded-Jacobian spectrum formula. All qualifying low weighted degrees precede the least derivative degree, so their monomial classes are independent. The original selected plane Jacobian bases and the fresh Koszul complete-intersection method give the same19 values. Only A5,D4 have link b1=2; all nonzero pg entries cost delta at least3. No arithmetic discrepancy was found.',
 'The original variation/intersection-pair route and the frozen Wang/Alexander-duality route compute the same eigenspace ker(T-I) of the same weighted monodromy. The finite weighted action makes it semisimple. The new printed result retains the original variation/pair route and monomial-basis computation; the alternate Hilbert-series/Wang derivation stays in the check record.',
 'The known-result disposition is preserved. The long classical analytic case analysis is cited at its exact opened Arnold loci, with the short low-delta exclusion and invariant application written in the form needed here, as permitted by prompt3.4 and GRIND4.4 condition2. Its original full proof remains in the attached source at the bound path/hash. No claim of a new theorem or third required check is made.',
 'BW local equations are unchanged w^3=r. Its total-delta-at-most4 inputs are a subset of the restored at-most5 table through the identity map on each germ. The repeated classification/counting paragraphs are consolidated under01CI. BW retains its exact link-to-exceptional-divisor homology map, equationC.D4.7 and every inherited tag/label. All global cyclic-cover, projective-bundle, compact-core, boundary and intersection steps remain byte-identical; twelve enumeration items remain.',
 'RAT6 original isolated-surface hypotheses, every invariant bound, the equality cases and the collection bound are preserved. The publisher metadata verifies Arnold DOI10.1007/BF01390134. Teissier-Merle author order is corrected in both the rendered bibliography and the BibTeX file; existing citation keys remain. The added bibliography entry is limited to the loci actually read.'
 ],
 evidence=[bind(planpath),plan['freeze'],bind('agents/continuation2_root/S6_SERIES_PUBLISH_II_root_RAT6_derivation.md'),plan['restored_block'],plan['BW_proposed'],bind('agents/continuation2_root/01BW/S6_SERIES_PUBLISH_II_root_BW_koszul_spectrum.json')],
 mathematical_errors_found=[],required_rows_closed=0,required_denominator=197,global_defect_classes_closed=0,publication_page_reading_credit=0)

newdefects=[]
for n,e in enumerate(plan['source_edits'],1):
 newdefects.append(dict(change_id=f'II-C2-RAT6-{n:03d}',type=e['type'],statement_id=e['owner'],old_location=e['owner'],old_page='',new_location=e['owner'],new_page='pending integrated PDF',old_text=e['old'],new_text=e['new'],reason=e['reason'],review_status='Exact edit and complete affected owning blocks read by root'))
for n,e in enumerate(plan['bib_edits'],1):
 newdefects.append(dict(change_id=f'II-C2-RAT6-BIB-{n:03d}',type='D18',statement_id='Bibliography',old_location='S6_SERIES_PUBLISH_references.bib',old_page='',new_location='S6_SERIES_PUBLISH_references.bib',new_page='',old_text=e.get('old',''),new_text=e.get('new',e.get('append','')),reason=e['reason'],review_status='Exact bibliographic field changes compared with opened primary sources'))
eventdata=[('cdp:st:C.2.RAT.6','01CI','Known supporting result restored with the unchanged delta-five statement and bounds, exact analytic/unit-root maps, cited normal forms and short invariant application. Full original and final proof read; fresh Koszul arithmetic agrees with the original Jacobian-basis method. Historical summary exposure is disclosed; this is used-and-rechecked credit only, outside the197 required owners.'),('cdp:st:C.2.D4.1','01BW','Full consolidated proof read. The local delta-four calculation uses the same cubic-suspension germs and the restriction of cited result01CI; the exact link-to-exceptional-divisor plumbing map remains. All global mathematical steps and every existing label/tag remain. This editorial consolidation adds no independent check to batch53.')]
events=[]
for n,(owner,tag,outcome) in enumerate(eventdata,1):
 row={k:'' for k in fields};row.update(statement_id=owner,date=now[:10],who=review['checker'],type='used and rechecked in this run',outcome=outcome,event_id=f'S6_SERIES_PUBLISH_II_C2_RAT6_SUPPORT_{tag}_20261122',phase='S6_SERIES_PUBLISH_II',source_file='records/S6_SERIES_PUBLISH_II_RAT6_restore_20261122/review.json',source_row=str(n),source_event_type='used and rechecked in this run',evidence_group='S6_SERIES_PUBLISH_II_C2_RAT6_SUPPORT',publish_input_file='S6_SERIES_PUBLISH_RAT6_support_CHECK_EVENTS.tsv',publish_input_row=str(n+1),date_utc=now,where='records/S6_SERIES_PUBLISH_II_RAT6_restore_20261122/review.json');events.append(row)
assert len({x['event_id'] for x in ledger+events})==len(ledger)+len(events)
assert len({x['change_id'] for x in defects+newdefects})==len(defects)+len(newdefects)
ix=next(i for i,x in enumerate(inventory) if x['label']=='cdp:st:C.2.RAT.6')
oldrow=inventory[ix].copy();newrow=oldrow.copy()
newrow.update(kind='Cited result',in_compendium_only_because='',placement_state='Printed cited result restored at inherited tag01CI',writing_state='Complete original and final source compared; final layout pending',confidence_state='Scoped used-and-rechecked evidence recorded; historical summary exposure disclosed',completion_state='Known supporting result; outside197 required-check rows',current_statement_owner='cdp:st:C.2.RAT.6',publication_review_status='Exact restored form and BW consolidation read; global publication review remains open',current_source_sha256=sha(source.encode()),uses='Arnold1976NormalForms: section1 I.0 and II1 pp92,95; section2 items1-12 pp100-101. MerleTeissier1977: Theorem2.1.1/Corollary2.1.3 pp11-13. Steenbrink1989Spectrum pp165-167. Nemethi1991Join section1/TheoremL1/Example2.4a pp1-3.',literature_searches=json.dumps(dict(queries=plan['online_searches'],publisher=plan['publisher_page'],primary_reading='agents/continuation2_root/S6_SERIES_PUBLISH_II_root_RAT6_derivation.md'),ensure_ascii=False))
notes=json.loads(newrow['notes']);notes['publication_cited_result_restoration']=dict(date_utc=now,record='records/S6_SERIES_PUBLISH_II_RAT6_restore_20261122/review.json',scope='Restore existing known01CI anchor; short application of cited sources in needed form; unchanged hypotheses/conclusions; no required-check credit. Historical disposition is preserved in notes and the original row diff.')
newrow['notes']=json.dumps(notes,ensure_ascii=False);inventory[ix]=newrow
invnew=encode(inventory,ivf,',')
ledgernew=ledgerold+encode(events,fields,header=False);defectnew=defectold+encode(newdefects,df,header=False)

# All exact guards and mathematical review are complete before canonical writes.
output.mkdir()
(output/'review.json').write_text(json.dumps(review,indent=2)+'\n')
for name,old,new in [('source',sourceold.decode(),source),('bibliography',bibold.decode(),bib)]:
 (output/f'{name}.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=name+'.before',tofile=name+'.after')))
(output/'S6_SERIES_PUBLISH_RAT6_support_CHECK_EVENTS.tsv').write_bytes(encode(events,fields))
(output/'defect_rows.tsv').write_bytes(encode(newdefects,df))
(output/'inventory_row_change.json').write_text(json.dumps(dict(old=oldrow,new=newrow),indent=2)+'\n')
sourcepath.write_text(source);bibpath.write_text(bib);invpath.write_bytes(invnew)
with ledgerpath.open('ab') as f:f.write(ledgernew[len(ledgerold):])
with defectpath.open('ab') as f:f.write(defectnew[len(defectold):])
assert ledgerpath.read_bytes()==ledgernew and ledgernew[:len(ledgerold)]==ledgerold
assert defectpath.read_bytes()==defectnew
assert bind(completion['path'])==completion
manifest=dict(created_utc=now,review=bind(str((output/'review.json').relative_to(R))),plan=bind(planpath),source_before_sha256=sha(sourceold),source_after_sha256=sha(source.encode()),bib_before_sha256=sha(bibold),bib_after_sha256=sha(bib.encode()),ledger_before_sha256=sha(ledgerold),ledger_after_sha256=sha(ledgernew),ledger_before_rows=len(ledger),ledger_after_rows=len(ledger)+len(events),ledger_prefix_unchanged=True,defects_before_rows=len(defects),defects_after_rows=len(defects)+len(newdefects),inventory_before_sha256=sha(invold),inventory_after_sha256=sha(invnew),completion_manifest_unchanged=completion,required_rows_closed=0,publication_page_reading_credit=0)
(output/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
text=f'''\n\n## Paper II known-result support restored — {now}\n\nCited result01CI (`cdp:st:C.2.RAT.6`) now appears with its inherited tag, unchanged isolated-surface scope and delta-five bounds. The local table previously repeated in01BW is consolidated there through the identity on each germ and restriction to total delta at most four; BW retains the link-to-exceptional-divisor map and all global steps. The original long known-result derivation remains in the attached research source and is replaced in the publication by exact primary citations and a short application in the required form (prompt3.4; GRIND4.4 condition2). The complete original and final proofs were read. No mathematical error was found. Historical inventory-summary exposure is disclosed; this adds two used-and-rechecked events, no independent-check credit and no new required owner. Paper II remains170/197 resolved,27 open. The missing Arnold reference is restored with publisher DOI10.1007/BF01390134; Teissier-Merle author order is corrected and its rendered entry moved accordingly. Eight exact defect edits are logged, with source/bibliography diffs and inventory-row change in `{output.relative_to(R)}`. Every inherited label/tag and the entire prior event-ledger byte prefix are retained. The new ledger has{len(ledger)+len(events)} rows and SHA-256 `{sha(ledgernew)}`; source SHA-256 `{sha(source.encode())}`. The required-check manifest is byte-identical. No global defect class or final PDF page is closed.\n'''
journal=[]
for name in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
 p=R/name;before=p.read_bytes()
 with p.open('a') as f:f.write(text)
 journal.append(dict(path=name,before_sha256=sha(before),after_sha256=sha(p.read_bytes()),appended_text=text))
(output/'journal_append.json').write_text(json.dumps(journal,indent=2)+'\n')
print(json.dumps(dict(manifest=bind(str((output/'manifest.json').relative_to(R))),source_sha256=sha(source.encode()),ledger_sha256=sha(ledgernew),events_added=len(events),defects_added=len(newdefects),required_rows_closed=0),indent=2))
