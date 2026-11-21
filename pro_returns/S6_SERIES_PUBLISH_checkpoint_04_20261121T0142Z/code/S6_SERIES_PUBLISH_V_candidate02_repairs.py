#!/usr/bin/env python3
"""Apply the exact, reviewed findings of the second complete Paper V page pass."""
from pathlib import Path
import json
from S6_SERIES_PUBLISH_editing import Editor

ROOT = Path(__file__).resolve().parents[1]
ed = Editor('V')
sources = [
    ('agents/v_topology/S6_SERIES_PUBLISH_V_candidate02_topology_guarded_patch.json', 'D23'),
    ('agents/v_topology/S6_SERIES_PUBLISH_V_Stacks_locator_guarded_patch.json', 'D18'),
    ('agents/provenance/S6_SERIES_PUBLISH_V_final_candidate02_guards.json', 'D06'),
    ('agents/provenance/S6_SERIES_PUBLISH_V_remaining_locator_guards.json', 'D18'),
    ('agents/v_analytic/S6_SERIES_PUBLISH_V_final_citation_locator_guards.json', 'D18'),
]

def changes(d):
    if isinstance(d, list):
        return d
    return next(d[k] for k in ('patches', 'changes', 'edits') if k in d)

integrated = []
for relative, kind in sources:
    data = json.loads((ROOT / relative).read_text())
    for row in changes(data):
        old, new = row.get('old', row.get('old_text')), row.get('new', row.get('new_text'))
        reason = row.get('reason') or (data.get('instruction') if isinstance(data, dict) else None) or 'Apply verified page-reading correction.'
        ed.replace(old, new, kind, reason,
                   row.get('statement', row.get('statement_id', row.get('id', ''))),
                   count=row.get('expected_count', 1))
        integrated.append({'file': relative, 'id': row.get('id'), 'kind': kind})

ed.replace('\\crefname{corollary}{corollary}{corollarys}',
           '\\crefname{corollary}{corollary}{corollaries}',
           'D23', 'Correct the plural reference name in the preamble; no theorem or proof changes.', 'preamble')

bibpath = ROOT / 'S6_SERIES_PUBLISH_references.bib'
bib = bibpath.read_text()
relative = 'agents/provenance/S6_SERIES_PUBLISH_V_remaining_locator_bibliography_guards.json'
for row in changes(json.loads((ROOT / relative).read_text())):
    old, new = row.get('old', row.get('old_text')), row.get('new', row.get('new_text'))
    assert bib.count(old) == 1, row.get('id')
    bib = bib.replace(old, new)
    ed.record('D18', old, new, row.get('reason', 'Record the exact newly opened primary-source pages.'),
              row.get('bibkey', row.get('id', '')), 'shared bibliography entry', 'shared bibliography entry')
    integrated.append({'file': relative, 'id': row.get('id'), 'kind': 'D18 shared bibliography'})

ed.save()
bibpath.write_text(bib)
(ROOT / 'records/S6_SERIES_PUBLISH_V_candidate02_repairs_receipt.json').write_text(
    json.dumps({'integrated': integrated, 'mathematical_events_added': 0,
                'scope': 'Exact guarded references, primary locators and layout repairs; each mathematical formula remains unchanged.'}, indent=2) + '\n')
