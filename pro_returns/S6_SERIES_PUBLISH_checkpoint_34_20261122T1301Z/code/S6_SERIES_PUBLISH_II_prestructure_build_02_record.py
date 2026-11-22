from pathlib import Path
import datetime as dt,hashlib,json
R=Path(__file__).resolve().parents[1]
def bind(p):
 b=(R/p).read_bytes();return dict(path=p,sha256=hashlib.sha256(b).hexdigest(),bytes=len(b))
root='build/II_prestructure_20261122T0842/'
s=json.loads((R/(root+'build_summary.json')).read_text())
assert s['source_sha256']=='43a75d6229813cc849de7a520ccf532fa58b9ed18997252706c09a4837489ed1'
assert s['pdf_sha256']=='5b281c433b4201da16e8993ce9e511cd267bc2a09d2dd6afbfef0a781f2850f6'
for k in ('overfull_total','overfull_above_2pt','undefined_references','undefined_citations','missing_characters','missing_fonts','multiply_defined','duplicate_destinations'):
 assert s[k]==0
now=dt.datetime.now(dt.timezone.utc).isoformat()
readings={
204:'Complete page image read. The final part of the preceding simple-elliptic argument and the first three XT items are visible. Grauert1960 section6 p59 and Grauert1963 pp35-36 render as resolved citations. Lines, displayed weights, filtration and quotient maps fit. Manual equation numbering and missing printed small statement tag remain for the global editorial pass.',
261:'Complete page image read. All five C4d proof items are visible, with character, fibre cohomology and twisting formulas. The repaired endpoint reference renders as proposition3.2 and the index reference as proposition3.1. No undefined marker or overflow remains. The remaining bare numeric references are still part of the global reference/style review.',
304:'Complete page image read. The E16 statement ending and proof items1-4 are visible. The two diagonal matrices share the first display line and their conjugation morphism occupies the second. Every exponent and matrix entry agrees with the source; both lines fit. The surrounding root degrees, determinant order and logarithmic formulas remain legible. Inherited E.16 equation numbers remain open globally.',
787:'Complete bibliography page image read. The new Grauert1963 entry has correct accents, volume16, pp35-36 and DOI. The DOI breaks at a legal slash without leaving the margin. The page also visibly retains duplicate1960 Grauert entries, lowercased proper title words and a long production-history note; these are unresolved global D01/D08/D18 instances and this visual inspection does not close them.'}
images=[]
for p,note in readings.items():
 q=R.parent/f'temporary_II_prestructure_pages/II_prestructure02_{p}.png'
 b=q.read_bytes();images.append(dict(pdf_page=p,image_sha256=hashlib.sha256(b).hexdigest(),image_bytes=len(b),dpi=130,actual_reading=note))
receipt=dict(created_utc=now,scope='Second integrated prestructure build after batch71 and the three concrete initial-build fixes. This is not the final publication candidate.',
 source=bind('S6_SERIES_PUBLISH_II.tex'),pdf=bind(root+'S6_SERIES_PUBLISH_II.pdf'),summary=bind(root+'build_summary.json'),
 passes=[bind(root+f'build_pass{i}.out') for i in (1,2,3)],pages=794,engine='pdfLaTeX',shell_escape=False,
 before=dict(overfull_total=1,overfull_above_2pt=1,max_overfull_pt=4.56259,undefined_references=1,undefined_citations=1,missing_fonts=0),
 after={k:s[k] for k in ('overfull_total','overfull_above_2pt','undefined_references','undefined_citations','missing_characters','missing_fonts','multiply_defined','duplicate_destinations')},
 actual_rendered_inspections=images,extra_rendered_but_unread_pages=[352],
 final_publication_page_reading_credit=0,global_defect_rows_closed=0,required_check_rows_closed=0,new_check_events=0,
 clean_typesetting_for_this_exact_build=True,final_publication_typesetting_gate_closed=False)
p=R/'records/S6_SERIES_PUBLISH_II_prestructure_build_02.json';assert not p.exists();p.write_text(json.dumps(receipt,indent=2)+'\n')
msg=f'''\n\n## Paper II second integrated build and affected-page inspection — {now}\n\nThe exact source43a75d6229813cc849de7a520ccf532fa58b9ed18997252706c09a4837489ed1 builds in three pdfLaTeX passes without shell escape to794 pages, PDF SHA2565b281c433b4201da16e8993ce9e511cd267bc2a09d2dd6afbfef0a781f2850f6. Initial counts of one overfull box(4.56259pt), one undefined reference and one undefined citation are now all zero. Missing fonts/characters, duplicate destinations and multiply-defined labels are also zero. Root actually inspected complete130dpi page images204,261,304,787, confirming the resolved citations, exact endpoint proof reference and two-line matrix display. The bibliography page still contains production notes and duplicate entries; manual equation numbering and statement-tag presentation remain globally open. This prestructure build receives no final publication page-reading credit. The source-bound build and image-reading receipt is records/S6_SERIES_PUBLISH_II_prestructure_build_02.json.\n'''
for name in ('PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md'):
 with (R/name).open('a') as f:f.write(msg)
print(json.dumps(bind(str(p.relative_to(R)))))
