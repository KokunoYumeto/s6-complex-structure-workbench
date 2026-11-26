from pathlib import Path
import csv,hashlib,json
R=Path(__file__).resolve().parents[1]
def bind(p):return {'path':p,'sha256':hashlib.sha256((R/p).read_bytes()).hexdigest()}
def read(p):return json.loads((R/p).read_text())
proposal='agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_group03_proposals.json';p=read(proposal)
index='agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_group03_final_index.json'
events='agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_group03_event_proposals.json'
t=next(x for x in p['blocks'] if x['tag']=='032W')
assert t['proposed_full_block']['sha256']=='08832d50712496f2917e6c8a062fefb3534dfad400a9cbaaa3ca00f3a2cd8209'
assert len(t['guards'])==4
es=[e for e in read(events)['events'] if e['statement_id']=='push:src:E.2.11']
assert len(es)==2 and all('For033F' not in e['outcome'] for e in es)
review='records/S6_SERIES_PUBLISH_II_root_continuation2_batch41_review.json'
assert (R/review).exists()
with (R.parent/'S6_SERIES_GRIND_tags.tsv').open() as f:pages={x['tag']:x['page'] for x in csv.DictReader(f,delimiter='\t')}
target=dict(owner=t['statement_owner'],tag='032W',old_page=pages['032W'],original=t['original_full_block'],proposed=t['proposed_full_block'],freeze=bind('agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_032W_freeze.json'),release=bind('agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_032W_release.json'),events=bind(events),who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, continuation2_C; reasoning effort not separately exposed',guards=[dict(old=g['old'],new=g['new'],type=g['defect_type'],reason=g['reason'],occurrences=g['expected_occurrences_in_owning_block']) for g in t['guards']],scope='Complete extension of a torus torsor across a codimension-two fibre with a smooth proper torus Jacobian, including the finite-stabilizer and finite-transversal arguments.',event_note='Full root comparison completed. The frozen covering proof and printed Jacobian-divisor proof use the same finite transverse map. Four wording/production-header guards preserve all mathematical hypotheses, conclusions, displays, labels and tag. The separate 033F check remains outside this admission.')
cfg=dict(batch=41,root_review_complete=True,source_before_sha256=bind('S6_SERIES_PUBLISH_II.tex')['sha256'],ledger_before_sha256=bind('CHECK_EVENTS.tsv')['sha256'],review_evidence=[bind(review),bind(proposal),bind(index)],targets=[target],code_copies=[],additional_source_edits=[],mathematical_repairs=[],scope='The torus-torsor purity statement is independently checked in full. Hartogs extension, complete vertical flows, the exact period quotient, compact-stabilizer representation and finite transverse map prove smoothness and the unique holomorphic torsor extension. The original mathematical statement and all displays remain. No computation, new page reading or completion of the separate pending 033F owner is claimed.')
out='records/S6_SERIES_PUBLISH_II_continuation2_batch41_config.json';assert not (R/out).exists();(R/out).write_text(json.dumps(cfg,indent=2)+'\n');print(json.dumps(bind(out),indent=2))
