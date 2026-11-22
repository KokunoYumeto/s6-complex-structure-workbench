from pathlib import Path
import datetime as dt, hashlib, json
R=Path(__file__).resolve().parents[1]
def bind(p):
 b=(R/p).read_bytes()
 return dict(path=p,sha256=hashlib.sha256(b).hexdigest(),bytes=len(b))
idxpath='agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_R13_two_image_review_index_v1.json'
idx=json.loads((R/idxpath).read_text())
assert bind(idxpath)['sha256']=='de07115afeec05692c8d3f4cec396f7b8a2b07ff6001728adb66245710c30ec8'
for b in idx['files']:
 assert bind(b['path'])==b
evidence=[bind(idxpath),*idx['files'],
 bind('agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_Y6_unfinished_scope_20261122.md'),
 bind('agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_Y6_full_fibre_layers_20261122.md')]
record=dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
 source=bind('S6_SERIES_PUBLISH_II.tex'),target='night:P4R.13',tag='02Y6',
 reading='Root read the complete C post-reading report and complete group-presentation program/output, and both complete A pre-release unfinished/layer records. The C hypothesis/callsite JSON is hash-bound but not claimed fully reread here. Root also read the full bounded current D.2.7 and C.3.1 owning blocks. No new independent check is claimed.',
 related_blocks=[dict(owner='cdp:st:D.2.7',bytes=13002,sha256='f427b0ec78b499cbc24429ac08829250c49c9d19b4c81e925d8f2776ec0d8dcc'),dict(owner='cdp:st:C.3.1',bytes=4401,sha256='b1c64f7ab01defecf2a368438124688de5cb8591e6db2fdd4a593dd46b2d971a')],
 findings=[
  'C confirms the exact reduced-horizontal delegation gap and classifies all six direct consumers. Four use the zero-Euler exclusion, and two use the actual doubled-section primary-restriction maps. No blanket one-image consumer was found. The unresolved assertion remains in R13 itself.',
  'The explicit amalgam Lambda1 *_Lambda Lambda2 has a central rank-two lattice and an index-two rank-three abelian subgroup. The two inverse maps in the R4-style meridian presentation are t=a,r=ab and a=t,b=t^{-1}r. The symbolic matrix has determinant1 and realizes those quotient relations. This supplies algebraic compatibility only, not geometric occurrence.',
  'The A layer record retains the full Cartier fibre and its torsion descent line. It identifies necessary multiplicities2 or4 and the canonical negative norm characters, with the single H2 layer at m/2. Root checked the stated conductor-sequence, torsor-connectedness and layer maps on reading, but has not established a smoothing or ambient realization. No completion credit is assigned.',
  'The existing D.2.7 construction has a fixed abelian general fibre and uses holomorphic non-Kahler local fillings to kill global H1 and H2. Its exact clutching and Mayer-Vietoris maps were read. It prevents an exclusion based solely on projectivity of the nearby torus. Its punctured-disc product model does not directly supply a filling with the two-image central support; no such gluing is asserted.',
  'The next scope question is the normalized root family and its finite deck action, with precise total-space Kahler or relative-polarization hypotheses for any invariant-cycle theorem. No classification theorem is applied without those hypotheses.'
 ],
 searches=[
  dict(engine='system2',queries=['degeneration abelian surfaces elliptic ruled normalization multiple fibre two double curves','irreducible degeneration complex tori two elliptic double curves nonnormal'],scope='Discovery only; secondary-host snippets do not support a mathematical conclusion.'),
  dict(engine='system1',queries=['"degenerations" "abelian surfaces" "multiple" "elliptic ruled"','"Degenerations of abelian surfaces and Hodge structures" Hulek Spandaw arxiv'],scope='Primary-author paper located; no completeness claim for the search.')
 ],
 primary_openings=[dict(authors='K. Hulek and J. Spandaw',title='Degenerations of abelian surfaces and Hodge structures',version='arXiv alg-geom/9404006v2,20 April1994',
  metadata_url='https://arxiv.org/abs/alg-geom/9404006',paper_url='https://arxiv.org/pdf/alg-geom/9404006v2',
  actual_opened_pdf_url='https://arxiv.org/pdf/alg-geom/9404006',resolved_version='v2 shown in the PDF header',
  text_read='Web-extracted text through the displayed beginning of section3.1. The relevant scope is section2.1,p.2, and Propositions1 and2,pp.4-5. No all-pages reading claimed.',
  relevant_scope='Section2.1 explicitly assumes a smooth Kahler total space, algebraic central components and relative minimality. Its local-normal-crossing irreducible case glues the two sections to each other; the statement concerns the full reduced fibre. These premises have not been proved for the original arbitrary-multiple support.',
  pdf_downloaded=False,pdf_sha256=None,new_body_citation=False)],
 evidence=evidence,required_row_closed=False,canonical_source_changes=0,check_events_added=0,final_page_credit=0,
 status='The full reduced-horizontal one-image assertion remains unresolved. No counterexample satisfying the compact ambient hypotheses is established.')
p=R/'records/S6_SERIES_PUBLISH_II_R13_root_research_02.json';assert not p.exists()
p.write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n')
text='\n\n## R13 full-fibre and primary-scope review — '+record['created_utc']+'\n\n'
text+='The two-image reduced-horizontal question remains open. Root read both independent unfinished/layer records, the complete comparative downstream audit, and the explicit group-presentation calculation. The full D.2.7 construction was read to retain the possibility of projective nearby tori in a compact ambient threefold with both Betti vanishings. A primary-source search opened Hulek–Spandaw, arXiv alg-geom/9404006v2, with its exact smooth Kahler total-space and full-fibre scope. No geometric occurrence or exclusion has been proved, and no new source assertion, check event or completion row is added. Evidence and search locators: `records/S6_SERIES_PUBLISH_II_R13_root_research_02.json`.\n'
for name in ['S6_SERIES_PUBLISH_report.md','PROGRESS_LEDGER.md']:
 q=R/name;q.write_bytes(q.read_bytes()+text.encode())
print(json.dumps(bind(str(p.relative_to(R)))))
