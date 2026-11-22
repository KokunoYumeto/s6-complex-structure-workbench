from pathlib import Path
import hashlib,json,datetime as dt
R=Path(__file__).resolve().parents[1]
def bind(p):return {'path':p,'sha256':hashlib.sha256((R/p).read_bytes()).hexdigest()}
def read(p):return json.loads((R/p).read_text())
p='agents/continuation2_root/S6_SERIES_PUBLISH_II_033P_admission_proposal.json'
d=read(p)
assert d['final_proposed_reading_pending'] is False
source=(R/'S6_SERIES_PUBLISH_II.tex').read_text()
original=(R/d['original']['path']).read_text();proposed=(R/d['proposed']['path']).read_text()
replay=original
for g in d['guards']:
 assert replay.count(g['old'])==1
 replay=replay.replace(g['old'],g['new'],1)
assert replay==proposed
assert r'multiplication by the lattice automorphism $-\alpha A^{-1}$ gives' in proposed
table_start=source.index('\\caption{Programs and their mathematical scope.}')
table_end=source.index('\\end{longtable}',table_start)
last_row=source[:table_end].splitlines(True)[-1]
assert source.count(last_row)==1
def row(scope,name):
 return scope+r' (\cref{push:src:E.5.3}) & \href{https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/\SsixRepositoryCommit/code/'+name+r'}{\nolinkurl{'+name+r'}} \\[3pt]'+'\n'
rows=row('Rational centralizer, norm lattice and cross-ratio derivative','S6_SERIES_PUBLISH_II_033P_prereading_exact.py')
rows+=row('Period covariance, integral collar relations and cubic discriminant','S6_SERIES_PUBLISH_II_033P_postrelease_exact.py')
review='records/S6_SERIES_PUBLISH_II_root_continuation2_batch36_review.json'
assert not (R/review).exists()
(R/review).write_text(json.dumps(dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
 checker='GPT-6 Astra (OpenAI), ChatGPT Pro mode, root, second continuation',
 actual_reading='The complete original nine-item proof, full immediately preceding period definition, complete proposed nine-item proof and all displayed computations were read. The exact norm transport was corrected in the proposed explanatory sentence before admission and then reread.',
 complete_comparison=d['comparison'],bounded_geometric_review=d['geometric_review'],
 primary_reading=bind('agents/continuation2_root/S6_SERIES_PUBLISH_II_033P_primary_reading.json'),
 computation=bind('agents/continuation2_root/S6_SERIES_PUBLISH_II_033P_execution_receipt.json'),
 correction=bind('agents/continuation2_root/S6_SERIES_PUBLISH_II_033P_root_reading_correction.json'),
 mathematical_statement_changed=False,downstream_statement_change_gate_triggered=False,
 prior_independence='Targeted derivation frozen before target release; the precise postrelease correction to its marking is disclosed, and the new geometric sufficiency argument is kept in the check record. Comparative work and the bounded review create no additional independent group.',
 mathematical_scope='All nine items and the full original conclusion. No page-image credit.'),indent=2)+'\n')
cfg=dict(batch=36,root_review_complete=True,source_before_sha256=bind('S6_SERIES_PUBLISH_II.tex')['sha256'],
 ledger_before_sha256=bind('CHECK_EVENTS.tsv')['sha256'],review_evidence=[bind(review),bind(p),d['comparison'],d['geometric_review']],
 targets=[dict(owner=d['owner'],tag=d['tag'],old_page='351',original=d['original'],proposed=d['proposed'],freeze=d['freeze'],release=d['release'],events=d['events'],
  who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, root, second continuation',guards=d['guards'],
  scope='Full classification on the stated small-mu half-plane: uniform family, intrinsic pencil, local cross-ratio rigidity, exact period and oriented-meridian necessity, all-four-fibre sufficiency and original-bidisc injectivity. The independent geometric half-translation and its corrected marking are fully recorded.',
  event_note='The immutable prereading convention mismatch is explicitly settled by an integral change of basis and corrected sign. No theorem statement is weakened or changed; no independent credit is assigned to the comparative or bounded review.')],
 additional_source_edits=[dict(old=last_row,new=last_row+rows,type='D09',reason='Add the two exact-arithmetic programs once to the Programs table. The first program retains its immutable prereading output; the check record and second program explicitly correct its convention-dependent final gluing label. No claim is made that the new code paths already exist at the pinned remote commit.')],
 mathematical_repairs=[],
 scope='E.5.3 is admitted after a frozen statement-led derivation, a full nine-item comparison and a separate bounded review of the geometric even-shift map. A marking/sign error in the new check derivation is corrected explicitly using Pi_p=Pi_f S, H_f=S H_p S^-1 and ell_f=S ell_p; its immutable record is retained. The printed classification statement and all its conclusions remain unchanged, so the statement-change trigger for the III–IV–V dependency chain is not activated. All printed algebra was recomputed by different exact methods, including the complete sphere relation and four period covariance identities. The independent geometric proof stays in the check record, while the paper retains its original proof route with explicit maps and source locators.')
out='records/S6_SERIES_PUBLISH_II_continuation2_batch36_config.json'
assert not (R/out).exists();(R/out).write_text(json.dumps(cfg,indent=2)+'\n')
print(json.dumps(bind(out),indent=2))
