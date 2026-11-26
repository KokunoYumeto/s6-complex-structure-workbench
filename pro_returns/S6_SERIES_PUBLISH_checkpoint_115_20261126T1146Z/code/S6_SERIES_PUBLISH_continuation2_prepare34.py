from pathlib import Path
import datetime as dt
import hashlib
import json

R=Path(__file__).resolve().parents[1]
def read(p): return json.loads((R/p).read_text())
def bind(p): return {'path':p,'sha256':hashlib.sha256((R/p).read_bytes()).hexdigest()}

yp='agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_YJ_admission_recommendation.json'
bp='agents/continuation2_B/01BF/S6_SERIES_PUBLISH_II_B2_BF_admission_proposal.json'
y,b=read(yp),read(bp)
ye=read(y['prior_editorial_proposals']['path'])
yt,bt=y['targets'][0],b['targets'][0]
review='records/S6_SERIES_PUBLISH_II_root_continuation2_batch34_review.json'
assert not (R/review).exists()
(R/review).write_text(json.dumps(dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
    checker='GPT-6 Astra (OpenAI), ChatGPT Pro mode, root, second continuation',
    actual_reading='Complete original and proposed blocks for 01BF and 02YJ; both continuation reviews; exact event proposals; BF computation-method comparison and invariant output; YJ program-table insertion and comparison record.',
    owners=['cdp:st:A.5.5','night:P4R.7'],
    mathematical_review=[
      'BF: finite-duality conductor line and determinant identify degree det N=2g-2+c. Separate factor lifts change the radical cubic by A1 ell^2+2a ell L2, whose restriction to R^3 is zero. Arbitrary whole-quadratic lifts fail for f=y^2+x^3. Conductor denominator bounds 2Xi and 4Xi give precisely the recorded degree inequalities. The tacnode d=1 reconstruction removes conductor poles after the Hessian is zero-free. The binary-cubic discriminant weight gives g=1,c=0; local root coordinates have nonzero Jacobian.',
      'YJ: a coefficient-one horizontal component contradicts the adjunction and Riemann-Hurwitz inequalities over genus at least two, so horizontal degree two is twice a section. Reverse blowups with coefficient mu-1 preserve the section with rational trees. Inclusion and tree collapse give inverse fundamental-group maps. The proper pushout uses the complete inverse image of the singular curve, including exceptional components mapped to points; the explicit inverse of the amalgam map identifies pi1(S) with pi1(C). The stated virtually abelian free-product cases and Euler formula give e(C)>=0, and the checked smooth-locus input completes e(S)>=0.'
    ],
    repairs=[dict(owner='cdp:st:A.5.5',type='D25',scope='Incorrect intermediate arbitrary-lift assertion',
                  corrected='Choose factor lifts separately; statement unchanged')],
    inherited_independence='Prior frozen derivations retain their dates/checkers. Root and continuation-agent reviews are comparative and generate no extra targeted event.',
    added_page_reading_credit=0, reviewed_evidence=[bind(yp),bind(bp)]),indent=2)+'\n')

targets=[]
targets.append(dict(owner='night:P4R.7',tag='02YJ',old_page='227',original=yt['full_original_block'],
    proposed=yt['proposed_full_block'],freeze=yt['freeze_receipt'],release=yt['release_receipt'],
    events=y['prior_event_proposals'],who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, checker ii_check_a',
    guards=[dict(old=g['literal_old'],new=g['literal_new'],type=','.join(g['defect_types']),
                 reason=g['reason']+' '+g.get('mathematical_transport','')) for g in ye['guards']],
    scope='Complete inherited statement-led derivation, exact affine/chain computation and two-item proof comparison; singular normalization and proper pushout retained.',
    event_note='Admitted in second continuation after full comparative review; original checker and event date retained. No extra independent event for continuation review.'))
targets.append(dict(owner='cdp:st:A.5.5',tag='01BF',old_page='84',original=bt['original_full_block'],
    proposed=bt['proposed_full_block'],freeze=bt['freeze_receipt'],release=bt['release_receipt'],
    events=bind('agents/ii_checks_provenance/recovery_20261121T2000Z/clean_group14/S6_SERIES_PUBLISH_II_clean_group14_BF_event_proposals.json'),
    who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, checker i_provenance_recovery, first continuation',
    guards=[dict(old=g['old'],new=g['new'],type=g['defect_type'],reason=g['reason'],
                 occurrences=g['expected_occurrences_in_owning_block']) for g in bt['guards']],
    scope='Complete inherited statement-led conductor-cleared jet derivation and universal algebra certificate; all eleven proof items compared. Arbitrary quadratic lift corrected to separate factor lifts.',
    event_note='Admitted in second continuation after full comparative review. Guard 14 is recorded as D25,D13: arbitrary whole-quadratic lifts fail for f=y^2+x^3; separate factor lifts give cubic difference A1 ell^2+2a ell L2. The statement and displayed conclusions remain unchanged.'))
pg=ye['program_table_guard']
row=b['program_table_entry_proposal']['exact_row'].replace('\\\\','\\')
table=pg['literal_new']
assert table.endswith('\\end{longtable}')
newtable=table[:-len('\\end{longtable}')]+row+'\n\\end{longtable}'
copies=[]
for k in ('code','output','execution_receipt'):
    f=b['program_table_entry_proposal'][k]
    copies.append({'from':f,'to':'code/'+Path(f['path']).name})
cfg=dict(batch=34,root_review_complete=True,
    source_before_sha256=bind('S6_SERIES_PUBLISH_II.tex')['sha256'],
    ledger_before_sha256=bind('CHECK_EVENTS.tsv')['sha256'],
    review_evidence=[bind(review),bind(yp),bind(bp)],targets=targets,
    additional_source_edits=[dict(old=pg['literal_old'],new=pg['literal_new'],type='D09',
        reason='Append the exact reviewed YJ program row; all 25 existing rows remain.'),
        dict(old=table,new=newtable,type='D09,D23',
        reason='Append BF program with its mathematical scope; decode the proposed doubled TeX command escapes once (two backslashes to one, four to two for row termination). All existing rows remain.')],
    code_copies=copies, mathematical_repairs=b['mathematical_repairs'],
    scope='Two prepared checks are admitted after complete root and continuation comparisons. The ruled-resolution Euler proof now supplies its proper pushout and inverse group map explicitly. The conductor-jet proof corrects an intermediate arbitrary-quadratic-lift assertion: for f=y^2+x^3, lifts y^2 and y^2+x^3 produce different radical cubics; choosing lifts of a and ell separately makes their cubic difference vanish on the radical. Its original theorem statement, hypotheses and displayed conclusions remain. Both computation packets retain their true earlier independence and chronology. All original labels and tags are preserved. Two Programs rows are added, with no claim that the newly written repository paths are already publicly available.')
out=R/'records/S6_SERIES_PUBLISH_II_continuation2_batch34_config.json'
assert not out.exists()
out.write_text(json.dumps(cfg,indent=2)+'\n')
print(json.dumps(bind(str(out.relative_to(R))),indent=2))
