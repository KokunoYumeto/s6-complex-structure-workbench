from pathlib import Path
import csv,datetime as dt,hashlib,json
R=Path(__file__).resolve().parents[1]
def bind(p):return {'path':p,'sha256':hashlib.sha256((R/p).read_bytes()).hexdigest()}
def read(p):return json.loads((R/p).read_text())
review='records/S6_SERIES_PUBLISH_II_root_continuation2_batch42_review.json'
assert not (R/review).exists()
indices={t:f'agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_{t}_final_v1_index.json' for t in ['033F','0339']}
assert bind(indices['033F'])['sha256']=='0fab5b3d36e1992d3b98887f4c62b949b867b9ae49732068f2ea6682b8a3b40b'
assert bind(indices['0339'])['sha256']=='7bf687d98b136584e582156fe37f49c9b459c9b6876a1f7604285e9b195e4207'
for p in indices.values():
 for b in read(p)['artifacts']:assert bind(b['path'])['sha256']==b['sha256'],b['path']
review_data=dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),checker='GPT-6 Astra (OpenAI), ChatGPT Pro mode, root, second continuation; reasoning effort not separately exposed',
 actual_reading='Complete original and proposed ten-item033F and seven-item0339 proofs, both frozen derivations and complete comparisons read. Both033F programs and outputs were read in full; the exact old matrix slice and missing named-program disposition were read. The final0339 block was reread after the exact Demailly page-locator guard. Final033F proposed bytes equal the already fully read final block.',
 mathematical_review=[
 '033F: the finite cover z=exp(-pi i c/(kl)), u=z^(2kl), extended marked critical sections and a regular central target yield the precise loop comparison. Identity H1 monodromy of the proper smooth torus family over the parameter disc is compared with ordinary or peripheral powers. In the primary basis, T=I+E14, the finite peripheral matrices have orders3/4, and Ainf=I+E23+E14. The cusp product is I+pE23+(p+N)E14, so p=N=0; the finite-order cases likewise force N=0. The maximum principle excludes an outer boundary limit. All ten analytic and integral-lattice items agree.',
 '033F: the explicit integral matrix P with rows (0,-1,0,-1),(6,0,1,0),(0,1,0,0),(1,0,0,0), determinant-1, intertwines both printed finite matrices and the cusp matrix with the primary basis. It carries the printed E41 to -E14, so the printed parameter S(-N) corresponds exactly to T^N. The postrelease invariant-subspace/cyclotomic remainder computation is compared with the bounded historical direct-power computation through these exact maps, without asserting a second independent group.',
 '0339: the fixed-pair locus is open by the cited local miniversal comparison. Disc propagation makes it closed on each connected Riemann surface. At a closure point b, a finite generic projection rho:T->Delta^d with singleton central fibre and the inverse image of the line through rho(a),0 give an irreducible curve C containing both a and b: d-1 equations give dimension at least1, finiteness gives at most1, and proper image equals the connected line disc. Finite normalization gives a connected smooth curve, and the pulled-back family carries a to b by disc propagation. Reduction preserves fibres, proper smooth base change and underlying connected topology. Finite chains preserve the pair; the E1.2/E1.3 holomorphic comparisons and connected half-plane/period quotient give the converse. No E2.4 circular input occurs.'
 ],primary_readings=[
 {'url':'https://arxiv.org/html/2610.39102v1','locus':'Lemma2.1, equations(2.1),(2.2), primary matrices and basis; PDF printedp3','web_refs':['turn449640180view1','turn885715014view3']},
 {'url':'https://people.math.harvard.edu/~demarco/Math274/Demailly_ComplexAnalyticDiffGeom.pdf','version':'21June2012','locus':'ChapterII Theorem4.19 p95, conical bound and proof pp96-97; Theorem7.6 and Corollary7.7 p113; Theorem7.12 pp114-115','web_refs':['turn550604340view0','turn582897450view2','turn885715014view2']}],
 historical_program_limit='The specifically named e_push_E_zero_end.py was not recovered in the bounded attachment lookup or the two failed pinned online requests. No reading or rerun of it is claimed. The actual read/run matrix slice and complete new computations cover every displayed calculation. Unavailable base assets do not reopen completed gates.',
 statement_changed=False,page_reading_credit=0,evidence=[bind(x) for x in indices.values()])
(R/review).write_text(json.dumps(review_data,indent=2)+'\n')
with (R.parent/'S6_SERIES_GRIND_tags.tsv').open() as f:pages={x['tag']:x['page'] for x in csv.DictReader(f,delimiter='\t')}
targets=[];evidence=[bind(review)]
for tag,ip in indices.items():
 prefix=f'agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_{tag}_final_v1'
 prop=prefix+'_proposals.json';p=read(prop);t=next(x for x in p['blocks'] if x['tag']==tag);idx=read(ip)
 evidence.extend([bind(ip),bind(prop),idx['comparison']])
 targets.append(dict(owner=t['statement_owner'],tag=tag,old_page=pages[tag],original=t['original_full_block'],proposed=t['proposed_full_block'],freeze=idx['freeze_receipt'],release=idx['release_receipt'],events=bind(prefix+'_event_proposals.json'),who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, continuation2_C; reasoning effort not separately exposed',guards=[dict(old=g['old'],new=g['new'],type=g['defect_type'],reason=g['reason'],occurrences=g['expected_occurrences_in_owning_block']) for g in t['guards']],scope=('Complete interior-period exclusion by exact parameter/peripheral monodromy and all10proof items.' if tag=='033F' else 'Complete fixed-pair separation for arbitrary smooth deformation chains, including singular and nonreduced bases, all7proof items.'),event_note='Root full comparison complete; exact final versioned evidence retained. No extra independence from packet versioning, no page-reading credit, and no admission of the separate0330 domain correction in this batch.'))
programs='agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_033F_final_v1_programs_table_proposal.json';pr=read(programs);evidence.append(bind(programs))
copies=[]
for c in pr['program_copy_proposals']:
 copies.extend([{'from':{'path':c['from'],'sha256':c['sha256']},'to':c['to']},{'from':{'path':c['output_from'],'sha256':c['output_sha256']},'to':c['output_to']}])
extra=[dict(old=g['old'],new=g['new'],type=g['defect_type'],reason=g['reason']) for g in pr['guards']]
cfg=dict(batch=42,root_review_complete=True,source_before_sha256=bind('S6_SERIES_PUBLISH_II.tex')['sha256'],ledger_before_sha256=bind('CHECK_EVENTS.tsv')['sha256'],review_evidence=evidence,targets=targets,code_copies=copies,additional_source_edits=extra,mathematical_repairs=[],scope='033F and0339 are admitted after complete frozen/printed comparisons. Exact integral basis and sign transport settles the monodromy comparison, and normalized finite curve pullbacks settle deformation propagation over arbitrary connected analytic bases. Eleven body guards and one Programs-table guard preserve both statements and all displayed mathematics. Historical named-program retrieval limitation remains explicit. The separate0330 statement-domain correction is not admitted here.')
out='records/S6_SERIES_PUBLISH_II_continuation2_batch42_config.json';assert not (R/out).exists();(R/out).write_text(json.dumps(cfg,indent=2)+'\n');print(json.dumps(bind(out),indent=2))
