#!/usr/bin/env python3
"""Integrate the exact findings from the complete candidate12 rendered reading."""
from pathlib import Path
import datetime, hashlib, json
from S6_SERIES_PUBLISH_editing import Editor, block

R = Path(__file__).resolve().parents[1]
EXPECTED = '38fd3831cb7be2eb60d856024571f9f8ec9105df45b445714251c41932580bbb'
sha = lambda b: hashlib.sha256(b).hexdigest()
ed = Editor('I')
assert sha(ed.before.encode()) == EXPECTED
changes = []

def change(old, new, kind, reason, statement=''):
    ed.replace(old, new, kind, reason, statement)
    changes.append({'old':old,'new':new,'type':kind,'reason':reason,'statement':statement})

anchor = r'\BeforeBeginEnvironment{theorem}{\Needspace{5\baselineskip}}'
hooks = r'''\pretocmd{\section}{\Needspace{14\baselineskip}}{}{\PackageError{S6}{Section spacing hook failed}{}}
\pretocmd{\subsection}{\Needspace{9\baselineskip}}{}{\PackageError{S6}{Subsection spacing hook failed}{}}
'''
change(anchor, hooks + anchor, 'D23',
       'Complete rendered-page reading found subsection headings separated from protected statements, and section/subsection pairs stranded at the page foot. Reserve enough space before the heading for the following statement, including a section followed immediately by a subsection. No mathematical text changes.')

# The repeated printed numbers are aliases of exactly the same entire block.
assert block(ed.before, 'fam:st:A.5.2') == block(ed.before, 'push:src:E.2.1')
assert block(ed.before, 'night:P2.2') == block(ed.before, 'night:P2.3')
old = r'''gives the standard automorphism group
(\hyperref[fam:st:A.5.2]{\ref*{fam:st:A.5.2}},
\hyperref[fam:src:B.4.1]{\ref*{fam:src:B.4.1}},
\hyperref[push:src:E.2.1]{\ref*{push:src:E.2.1}}).'''
new = r'''gives the standard automorphism group
(\hyperref[fam:st:A.5.2]{\ref*{fam:st:A.5.2}},
\hyperref[fam:src:B.4.1]{\ref*{fam:src:B.4.1}}).'''
change(old,new,'D06','Candidate12 page14 repeats B.2 in outline E6. The two source identifiers belong to the byte-identical statement/proof block; retain one printed reference and all original identifiers.','series:I:E')
old = r'''differences
(\hyperref[night:P2.2]{\ref*{night:P2.2}},
\hyperref[night:P2.3]{\ref*{night:P2.3}}).'''
new = r'''differences
(\hyperref[night:P2.3]{\ref*{night:P2.3}}).'''
change(old,new,'D06','Candidate12 page14 repeats18.2 in outline F1. Both source identifiers belong to the byte-identical statement/proof block; retain its primary printed reference and every original identifier.','series:I:F')

change(r'\draw[->,bend left=18,semithick] (TB) to (TG);',
       r'\draw[->,semithick] (TB.east) -- ++(.45,0) |- (TG.east);',
       'D23','Route the B-to-G dependency arrow through the gap to the right of E and below it, keeping the edge clear of all theorem boxes.')
change(r'\draw[->,bend left=18,semithick] (TG) to (TA);',
       r'\draw[->,semithick] (TG.west) -- ++(-.45,0) |- (TA.west);',
       'D23','Candidate12 page17 shows the G-to-A edge crossing the D box. Route it outside the left edges; endpoints and mathematical relation remain unchanged.')

archive_path = R/'agents/i_analytic/S6_SERIES_PUBLISH_I_final_candidate12_visual_archive.json'
archive = json.loads(archive_path.read_text())
assert archive['source_sha256'] == EXPECTED
current = archive['current_complete_statement_and_proof']
replacement = archive['replacement_complete_statement_and_proof']
assert current[current.index(r'\begin{proof}'):] == replacement[replacement.index(r'\begin{proof}'):]
assert current in ed.text
gfile = R/'agents/i_analytic/S6_SERIES_PUBLISH_I_final_candidate12_reading_analytic_guards.json'
for g in json.loads(gfile.read_text())['guards']:
    change(g['old'],g['new'],g['defect'],g['scope']+' Root read the entire original/current/replacement statement and proof archive; current and replacement proofs are byte-identical.',g['statement_id'])

for filename, kind in [
    ('agents/i_provenance/S6_SERIES_PUBLISH_I_candidate12_proof_placement_guards.json','D23'),
    ('agents/i_topology/S6_SERIES_PUBLISH_I_metadata_parser_alias_guards.json','D06')]:
    data=json.loads((R/filename).read_text())
    assert data.get('source_sha256',data.get('target_sha256')) == EXPECTED
    for g in data['guards']:
        change(g['old'],g['new'],kind,g['reason'])

ed.save()
# Exact inverse replacements reconstruct the complete prior source, not just
# a whitespace-normalized approximation.
prior=ed.text
for g in reversed(changes):
    assert prior.count(g['new']) == 1
    prior=prior.replace(g['new'],g['old'],1)
assert prior == ed.before
receipt={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
         'before_source_sha256':EXPECTED,'after_source_sha256':sha(ed.text.encode()),
         'changes':changes,'exact_reverse_reconstruction_verified':True,
         'proof_comparison_archive':str(archive_path.relative_to(R)),
         'proof_comparison_archive_sha256':sha(archive_path.read_bytes()),
         'check_events_added':0,
         'scope':'Layout, alias placement, duplicate outline references and positive presentation of an unchanged explicit counterexample. No mathematical statement is strengthened, no hypothesis or numerical value changes, and no proof step is changed.'}
(R/'records/S6_SERIES_PUBLISH_I_candidate13_visual_finalize_applied.json').write_text(json.dumps(receipt,indent=2)+'\n')
