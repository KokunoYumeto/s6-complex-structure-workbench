from pathlib import Path
import csv,datetime as dt,hashlib,json
R=Path(__file__).resolve().parents[1]
def bind(p):return {'path':p,'sha256':hashlib.sha256((R/p).read_bytes()).hexdigest()}
def read(p):return json.loads((R/p).read_text())
proposal='agents/continuation2_B/01FT/S6_SERIES_PUBLISH_II_B2_FT_admission_proposal.json'
p=read(proposal);t=p['targets'][0]
portable='agents/continuation2_B/01FT/S6_SERIES_PUBLISH_II_B2_FT_portable_companion_receipt.json';port=read(portable)
assert port['byte_identical_output'] and port['new_events']==0
review='records/S6_SERIES_PUBLISH_II_root_continuation2_batch40_review.json';assert not (R/review).exists()
(R/review).write_text(json.dumps(dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
 checker='GPT-6 Astra (OpenAI), ChatGPT Pro mode, root, second continuation; reasoning effort not separately exposed',
 actual_reading='Complete ten-part frozen derivation, all six original and proposed proof items, full comparison, both complete programs and successful outputs, portable-path diff receipt and primary-reading locators read.',
 mathematical_review=[
 'The exponential-sequence period-cocycle equation gives the two resonance equations by eliminating its last coordinates. The nonreal central generators ensure unique integers. The relative Dolbeault comparison includes bounded-frequency separation and the large-frequency bound, so its Fourier homotopies preserve smooth series and derivatives. The two finite filtrations and cyclic equivariance prove the coherent-complex comparison.',
 'The regular Picard derivative is the nonzero vector kappa^t(q,r), and the unit determinant gives the simple zero. The displayed cycle bases and relation maps give H1=(R/s)^2 and H2=R/s^2, with explicit inverse generators. At order three, the theta/Ramanujan derivation gives mu_second=3W/(8pi^2), alpha_prime=W/(2pi^2) and aligned transverse coefficient 41W/(24pi^2). Its joint scaled coefficient is 123/64. The independent postrelease cubic calculation gives x(3P)=(512-592t+80t^2)/81 and transports all printed constants through the exact curve isomorphism. The sign g3(rho)=-8/F^6 is explicitly bound.',
 'The Picard/cohomology frame map has inverse (c,d)->(2c-d,-c). Alignment by b/nu, the displayed row subtraction and unit rescalings give the exact order-three complex, rather than inferring it solely from determinant order. The quotient maps in degrees one and two have the stated inverse generators and annihilators s^2,s^3. The affine deck evaluations and the twelve residue classes give the actual coarse skyscrapers.',
 'The cusp triangular and square complexes have exact chain inclusion, projection and homotopy; exp(2pi i z)-1 is nonzero. Base change and the logarithmic/normalization sequences give its degree-two skyscraper and surjective map. The countable-tuple argument produces a vanishing regular fibre; coherence on the compact base gives finite support. The two-column Leray sequence yields the unchanged dimensions and normalization-map surjectivity.'
 ],statement_changed=False,page_reading_credit=0,
 independence='Prior C_twists.py matrix and rational-constant exposure remains disclosed. The frozen geometric theta derivative and constructive quotient method is the targeted check. The two new programs share its one computation event. Root comparison adds no event.',
 program_portability='The frozen program remains untouched. Its separately saved companion replaces only the cwd-dependent dependency lookup by Path(__file__).with_name and produces byte-identical output from /tmp.',
 evidence=[bind(proposal),p['review'],p['primary_reading'],bind(portable)]),indent=2)+'\n')
with (R.parent/'S6_SERIES_GRIND_tags.tsv').open() as f:pages={x['tag']:x['page'] for x in csv.DictReader(f,delimiter='\t')}
target=dict(owner=t['statement_owner'],tag=t['tag'],old_page=pages[t['tag']],original=t['original_full_block'],proposed=t['proposed_full_block'],freeze=t['freeze_receipt'],release=t['release_receipt'],events=bind('agents/continuation2_B/01FT/S6_SERIES_PUBLISH_II_B2_FT_event_proposals.json'),who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, continuation2_B; reasoning effort not separately exposed',guards=[dict(old=g['old'],new=g['new'],type=g['defect_type'],reason=g['reason'],occurrences=g['expected_occurrences_in_owning_block']) for g in t['guards']],scope='All nonintegral twists, regular and finite-point resonance modules, cusp normalization map and every printed order-three coefficient.',event_note='Admitted after complete root comparison of both full proofs and both exact programs. Prior historical program exposure, actual source-reading scope and checker sign correction are retained. All original theorem displays and quantifiers remain.')
edits=[dict(old=g['old'],new=g['new'],type=g['defect_type'],reason=g['reason'],occurrences=g['expected_occurrences_in_source']) for g in p['additional_source_guards']]
source=(R/'S6_SERIES_PUBLISH_II.tex').read_text();st=source.index('\\caption{Programs and their mathematical scope.}');end=source.index('\\end{longtable}',st);last=source[:end].splitlines(True)[-1]
rows=''
for obj,scope in [(p['computations'][0]['program'],'Nonintegral-twist quotient maps, theta derivatives, finite characters and cusp contraction'),(port['portable_companion'],'Tripling-coordinate identity, resonance coefficients and cusp chain homotopy')]:
 name=Path(obj['path']).name
 rows+=scope+r' (\cref{cdp:st:C5c}) & \href{https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/\SsixRepositoryCommit/code/'+name+r'}{\nolinkurl{'+name+r'}} \\[3pt]'+'\n'
edits.append(dict(old=last,new=last+rows,type='D09',reason='Add the two reviewed exact programs with their actual mathematical scopes and common pinned-commit macro. The second is the documented portable companion.'))
copies=[]
for obj in [p['computations'][0]['program'],p['computations'][0]['output'],port['portable_companion'],port['output']]:copies.append({'from':obj,'to':'code/'+Path(obj['path']).name})
cfg=dict(batch=40,root_review_complete=True,source_before_sha256=bind('S6_SERIES_PUBLISH_II.tex')['sha256'],ledger_before_sha256=bind('CHECK_EVENTS.tsv')['sha256'],review_evidence=[bind(review),bind(proposal),bind(portable)],targets=[target],additional_source_edits=edits,code_copies=copies,mathematical_repairs=[],scope='The nonintegral-twist theorem is checked in full, including every local cyclic module, affine character, order-three coefficient and the cusp normalization map. Exact maps replace implicit eliminations; the primary derivative identity and elliptic-curve coordinate change are cited precisely. The immutable freeze discloses historical matrix exposure and the postrelease sign correction is retained. The theorem, all original displayed formulas, labels and tags are unchanged.')
out='records/S6_SERIES_PUBLISH_II_continuation2_batch40_config.json';assert not (R/out).exists();(R/out).write_text(json.dumps(cfg,indent=2)+'\n');print(json.dumps(bind(out),indent=2))
