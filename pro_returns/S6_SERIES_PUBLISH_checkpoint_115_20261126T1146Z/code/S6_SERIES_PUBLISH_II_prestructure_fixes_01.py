from pathlib import Path
import csv, datetime as dt, difflib, hashlib, io, json, re

R = Path(__file__).resolve().parents[1]
def sha(b): return hashlib.sha256(b).hexdigest()
def bind(p):
    b=(R/p).read_bytes()
    return dict(path=p,sha256=sha(b),bytes=len(b))

sp=R/'S6_SERIES_PUBLISH_II.tex'
oldb=sp.read_bytes(); old=oldb.decode()
assert sha(oldb)=='5a3dc240306456d2f948cfc3cb2ae326bb7039aa24ce5ae7c666cc98acefad4d'
dp=R/'S6_SERIES_PUBLISH_defects_II.tsv'
db=dp.read_bytes()
reader=csv.DictReader(io.StringIO(db.decode()),delimiter='\t')
previous=list(reader); fields=reader.fieldnames
edits=[dict(owner='cdp:st:C4d',type='D06,D18',old_page='260',
 old='Intersecting with the endpoint-vanishing loci of\n\\ref{cdp:st:C.1.2} and applying \\ref{cdp:st:C.1.1} gives',
 new='Intersecting with the endpoint-vanishing loci in the proof of\n\\cref{cdp:st:C.1.3} and applying \\cref{cdp:st:C.1.1} gives',
 reason='The batch35 locator named C.1.2, an inherited inventory/compendium entry with no owning statement in the current paper. The complete receiving C4d proof and complete C.1.3 proof were read. C.1.3 explicitly obtains the same two endpoint loci by applying CDP98 Corollary1.3 p79 to T_Y tensor L_P and its Serre-dual bundle, using the maps M->L_P tensor M and M->M inverse. Its smooth compact connected and b1=b2=0 scope follows from C4d integral vanishings, and a full fibre is a nonzero effective Cartier divisor. This corrects the locator without changing an inference or conclusion; existing C4b/C4c use this same precise proof locus.'),
 dict(owner='cdp:st:E16',type='D23',old_page='304',
 old='\\[\n D_3(w)=\\operatorname{diag}(1,1,w,w^2),\\qquad\n D_4(w)=\\operatorname{diag}(1,1,w,w^3),\\qquad\n \\Psi^\\sharp(w)=D_n(w)\\Psi(w^n)D_n(w)^{-1}.\n\\]',
 new='\\[\n \\begin{gathered}\n D_3(w)=\\operatorname{diag}(1,1,w,w^2),\\qquad\n D_4(w)=\\operatorname{diag}(1,1,w,w^3),\\\\\n \\Psi^\\sharp(w)=D_n(w)\\Psi(w^n)D_n(w)^{-1}.\n \\end{gathered}\n\\]',
 reason='The initial three-pass pdfLaTeX log reports this single display extending4.56259pt beyond the margin. Its complete owning statement and proof were read. Put the two diagonal matrices on one line and their conjugation formula on the next, preserving every mathematical token and the exact morphism.'),
 dict(owner='Bibliography:Grauert1963ErratumD',type='D18',old_page='204 citation',
 old='\\bibitem[Grauert(1960{\\natexlab{b}})]{Grauert60}',
 new='\\bibitem[Grauert(1963)]{Grauert1963ErratumD}\nHans Grauert.\n\\newblock Berichtigung: Ein Theorem der analytischen Garbentheorie und die\n  Modulr\\\"aume komplexer Strukturen.\n\\newblock \\emph{Publications Math\\\"ematiques de l\'IH\\\"ES}, 16:35--36, 1963.\n\\newblock \\doi{10.1007/BF02684291}.\n\n\\bibitem[Grauert(1960{\\natexlab{b}})]{Grauert60}',
 reason='The cited key exists in the verified master bibliography but was absent from the self-contained inline bibliography. Numdam primary metadata confirms author, title, journal, volume16, year1963, pages35-36 and DOI10.1007/BF02684291. Root opened the original PDF and visually read both complete article pages35-36. Item1 corrects radius conditions and inductive proof steps; item2 corrects the closedness claim in section7 Satz2. The existing XT citation to proof corrections is unchanged. Global bibliography ordering and removal of production notes remain open.')]
# Use the proper acute accents in the French journal name.
edits[2]['new']=edits[2]['new'].replace('Math\\\"ematiques','Math\\\'ematiques').replace("IH\\\"ES","IH\\\'ES")
new=old; rows=[]
for i,e in enumerate(edits,1):
    assert new.count(e['old'])==1
    new=new.replace(e['old'],e['new'],1)
    rows.append(dict(change_id=f'II-C2-PREFLIGHT01-{i:03d}',type=e['type'],statement_id=e['owner'],
        old_location=e['owner'],old_page=e['old_page'],new_location=e['owner'],new_page='pending rebuilt PDF',
        old_text=e['old'],new_text=e['new'],reason=e['reason'],
        review_status='Complete receiving proofs and exact edits read by root; final rendered review pending'))
for pat in [r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}']:
    assert re.findall(pat,old)==re.findall(pat,new)
assert old.count('\\begin{proof}')==new.count('\\begin{proof}')
assert old.count('\\end{proof}')==new.count('\\end{proof}')

bp=R/'S6_SERIES_PUBLISH_references.bib'; bb=bp.read_bytes(); bt=bb.decode()
start=bt.index('@article{Grauert1963ErratumD,'); end=bt.index('\n@',start+1)
entry=bt[start:end]
needle='  year = {1963},\n'
assert entry.count(needle)==1 and 'doi =' not in entry
entry_new=entry.replace(needle,needle+'  doi = {10.1007/BF02684291},\n',1)
bt_new=bt[:start]+entry_new+bt[end:]
rows.append(dict(change_id='II-C2-PREFLIGHT01-004',type='D18',statement_id='Bibliography:Grauert1963ErratumD',
    old_location='master bibliography',old_page='',new_location='master bibliography',new_page='',
    old_text=entry,new_text=entry_new,reason='Add the exact DOI independently confirmed in the opened primary Numdam metadata; all existing scoped verification history remains.',
    review_status='Primary metadata and both original article pages read by root'))
assert not ({r['change_id'] for r in previous}&{r['change_id'] for r in rows})
out=io.StringIO(newline=''); w=csv.DictWriter(out,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
tail=out.getvalue().split('\n',1)[1].encode()
assert db.endswith(b'\n')
now=dt.datetime.now(dt.timezone.utc).isoformat()
rd=R/'records/S6_SERIES_PUBLISH_II_prestructure_fixes_01'
assert not rd.exists();rd.mkdir()
(rd/'source.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='II.before',tofile='II.after')))
(rd/'bibliography.diff').write_text(''.join(difflib.unified_diff(bt.splitlines(True),bt_new.splitlines(True),fromfile='references.before',tofile='references.after')))
(rd/'defect_rows.tsv').write_text(out.getvalue())
primary=R.parent/'primary_continuation2_root_provenance/Grauert1963Erratum_original.pdf'
assert sha(primary.read_bytes())=='04b24590e8c56e1a05c0cb520843e8160447ebb560d9ca2394b0682d83ed489c'
manifest=dict(created_utc=now,source_before_sha256=sha(oldb),source_after_sha256=sha(new.encode()),
    bibliography_before_sha256=sha(bb),bibliography_after_sha256=sha(bt_new.encode()),
    defects_before_sha256=sha(db),defects_after_sha256=sha(db+tail),defect_rows=4,
    current_ledger=bind('CHECK_EVENTS.tsv'),new_check_events=0,required_rows_closed=0,global_defect_rows_closed=0,
    original_three_issue_receipt=bind('records/S6_SERIES_PUBLISH_II_prestructure_build_01.json'),
    primary_reading=dict(metadata_url='https://www.numdam.org/item/PMIHES_1963__16__35_0/',
        pdf_url='https://www.numdam.org/item/PMIHES_1963__16__35_0.pdf',version='Original1963 journal article, Numdam scan',
        pdf_sha256=sha(primary.read_bytes()),pdf_bytes=primary.stat().st_size,article_pages_read=['35','36'],
        actual_reading='Both full130dpi page images inspected through view_image after reading the complete retrieved text. The web screenshot calls returned text placeholders only and receive no visual-reading credit. The original1960 article was not reread in this step.',
        receiving_locus='night:P4.54 item3; complete current proof read; only absent bibliography entry supplied'),
    current_publication_page_reading_credit=0,typesetting_gate_closed=False,
    residual_scope='Final source organization, all global defect classes, every final PDF page and final provenance checks remain open.')
(rd/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
sp.write_text(new);bp.write_text(bt_new)
with dp.open('ab') as f:f.write(tail)
assert dp.read_bytes()==db+tail
text=f'''\n\n## Paper II initial build fixes — {now}\n\nThe initial pdfLaTeX build's three concrete issues are addressed in source: the missing Grauert1963 corrigendum bibliography entry, the C4d endpoint reference, and the4.56259pt overfull matrix display. The C4d reference had been introduced in batch35 and pointed to a compendium/inventory statement absent from the current paper; it now points exactly to the existing C.1.3 proof of the same endpoint loci. No theorem or proof inference changed. The diagonal matrices and their conjugation map are split over two lines with identical mathematics. Root read both complete Grauert corrigendum pages35–36 in the original scan and confirmed its primary bibliographic metadata. Four exact defect rows and both diffs are in records/S6_SERIES_PUBLISH_II_prestructure_fixes_01. Source SHA256 {manifest['source_after_sha256']}. This edit does not itself close the typesetting, provenance, required-check or page-reading gates; the new integrated build and affected-page images remain to be checked.\n'''
for name in ('PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md'):
    with (R/name).open('a') as f:f.write(text)
print(json.dumps(manifest,indent=2))
