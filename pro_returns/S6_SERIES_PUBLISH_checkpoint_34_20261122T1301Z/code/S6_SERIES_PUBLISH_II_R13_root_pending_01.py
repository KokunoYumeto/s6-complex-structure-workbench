from pathlib import Path
import datetime,hashlib,json,re
R=Path(__file__).resolve().parents[1]
def bind(p):
 b=(R/p).read_bytes()
 return dict(path=p,sha256=hashlib.sha256(b).hexdigest(),bytes=len(b))
s=(R/'S6_SERIES_PUBLISH_II.tex').read_text()
blocks=[]
for label in ['night:P4R.13','night:P4R.9']:
 p=s.index('\\label{'+label+'}')
 a=s.rfind('\\begin{proposition}',0,p)
 se=s.index('\\end{proposition}',a)+len('\\end{proposition}')
 assert a<p<se
 assert re.match(r'\s*\\begin\{proof\}',s[se:])
 b=s.index('\\end{proof}',se)+len('\\end{proof}')
 block=s[a:b]
 blocks.append(dict(owner=label,sha256=hashlib.sha256(block.encode()).hexdigest(),
                    bytes=len(block.encode()),full_original_block_read=True))
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
r=dict(created_utc=now,
 source=bind('S6_SERIES_PUBLISH_II.tex'),
 checker='GPT-6 Astra (OpenAI), ChatGPT Pro mode, root; comparative scope audit only',
 status='Required row02Y6 remains open; the single-image conclusion in the reduced-horizontal branch is unproved in the current record.',
 blocks=blocks,
 finding='R13 item1 says that the reduced-horizontal case is already proved by R9, then treats only the doubled-horizontal case. R9 proves smooth minimal elliptic-ruled normalization and e(S)=0 for a reduced horizontal boundary consisting of one elliptic bisection or two disjoint elliptic sections. It does not prove that their finite image conductor has only one component.',
 exact_scope='The omitted question concerns two distinct smooth elliptic image curves, each covered by a different coefficient-one elliptic section through an unramified degree-two branch map. The original ambient full fibre has arbitrary multiplicity m; no reduction to a full reduced fibre has been proved for this question.',
 original_error_identified='The assertion that the cited R9 already establishes every conclusion of R13 in this branch is unsupported by its exact statement and complete proof.',
 no_global_counterexample_established=True,
 original_statement_false_not_claimed=True,
 downstream_statement_reading=[
  'MainC gives smooth minimal elliptic-ruled normalization without one-image uniqueness.',
  'P4.32 explicitly restricts its one-image assertion to the doubled-horizontal case.',
  'P4.58 gives smooth minimal elliptic-ruled normalization without one-image uniqueness.'
 ],
 agent_evidence=[
  bind('agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_Y6_unfinished_scope_20261122.md'),
  bind('agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_Y6_full_fibre_layers_20261122.md')
 ],
 agent_boundary='A preserved its own unresolved construction and full-fibre calculations before any target-proof release; the target remains unopened for A. C and root perform disclosed comparative audits. Root has not independently verified every new full-fibre layer calculation and assigns it no new completion credit.',
 remaining_work='Settle the exact one-image assertion in the full ambient scope, preserve the proved numerical/minimality result, and complete the exact downstream inference audit. The organization packet records the unresolved premise explicitly.',
 canonical_source_changes=0,check_events_added=0,required_rows_closed=0,final_page_credit=0)
out='records/S6_SERIES_PUBLISH_II_R13_root_pending_01.json'
assert not (R/out).exists()
(R/out).write_text(json.dumps(r,indent=2)+'\n')
note=f"""

### {now}: R13 reduced-horizontal scope gap remains open

The complete R13 and R9 proofs were read in a root comparative audit.
R13's first step cites R9 for its reduced-horizontal case, but R9 proves
minimal elliptic-ruled normalization and Euler number zero and allows two
disjoint coefficient-one elliptic sections. It supplies no proof that their
finite image conductor has one component. The two-distinct-image case with
degree-two unramified branch maps is therefore still an open gate for required
row02Y6. No global counterexample or falsity of the full statement is claimed.
The full multiplicity m is retained.

Main C and P4.58 have no one-image uniqueness clause. P4.32 explicitly limits
its one-image clause to the doubled-horizontal case. The precise proof-use
audit continues. A's independent unresolved attempt remains uncredited and
its target proof unopened; C and root comparisons remain disclosed as such.
No source, check-event or completion row is changed by this pending record.
Evidence: records/S6_SERIES_PUBLISH_II_R13_root_pending_01.json.
"""
for name in ['S6_SERIES_PUBLISH_report.md','PROGRESS_LEDGER.md']:
 with (R/name).open('a') as f:f.write(note)
print(json.dumps(bind(out),indent=2))
