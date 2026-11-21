from pathlib import Path
import datetime, hashlib, json
from S6_SERIES_PUBLISH_editing import Editor

r = Path(__file__).resolve().parents[1]
ed = Editor('I')
initial_sha = hashlib.sha256(ed.text.encode()).hexdigest()
sources = []

p = r / 'agents/i_topology/editorial/S6_SERIES_PUBLISH_I_residual_batch9_guarded.json'
data = json.loads(p.read_text())
types = ['D02', 'D22', 'D02', 'D02', 'D02', 'D08', 'D02', 'D08', 'D02', 'D02', 'D11']
for g, kind in zip(data['patches'], types, strict=True):
    ed.replace(g['old'], g['new'], kind, g['reason'], ', '.join(g['statement_ids']))
sources.append({'path': str(p.relative_to(r)), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest(), 'applied': len(data['patches'])})

p = r / 'agents/i_analytic/S6_SERIES_PUBLISH_I_final_residual_guards.json'
data = json.loads(p.read_text())
for i, g in enumerate(data['guards']):
    kind = ('D23' if i == 42 else 'D04' if i in {19, 46, 52} else
            'D01' if i == 9 else 'D02' if i in {0, 1, 3, 7, 10, 11, 47, 50, 54, 56, 58, 60} else 'D08')
    ed.replace(g['old'], g['new'], kind, g['reason'], ', '.join(g['statement_ids']))
sources.append({'path': str(p.relative_to(r)), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest(), 'applied': len(data['guards'])})

p = r / 'agents/i_provenance/S6_SERIES_PUBLISH_I_residual_prebuild_guards.json'
data = json.loads(p.read_text())
skipped = []
for g in data['changes']:
    if g['id'] == 'I-residue-provenance-2':
        assert 'This proves descent under the specified period identifications.' in ed.text
        skipped.append({'id': g['id'], 'reason': 'The same epithet was removed in the already applied IA-FRES-006 guard, which retains the specified marked period identifications. Both agents read the complete affected proof; no extra event is created for this overlap.'})
        continue
    kind = 'D02/D08' if g['id'] == 'I-residue-provenance-6' else 'D08'
    ed.replace(g['old'], g['new'], kind, g['reason'], g['id'])
sources.append({'path': str(p.relative_to(r)), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest(), 'applied': len(data['changes'])-len(skipped), 'covered_by_other_guard': skipped})
ed.save()
(r / 'records/S6_SERIES_PUBLISH_I_final_residual_integration.json').write_text(json.dumps({
    'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'before_sha256': initial_sha, 'after_sha256': hashlib.sha256(ed.text.encode()).hexdigest(),
    'sources': sources,
    'root_review': 'Every guard or its complete changed-line diff and every accompanying comparison was read. All substantive equations and morphisms retain their exact content. In B4.18, summing gamma(s+k)=gamma(s)-k*delta gives gamma-11*delta/2, and the twelve constant terms give -delta/2, recovering the existing gamma-6*delta iterate. The full old/current/proposed proof comparisons belong to the supplying agent records.',
    'scope': 'No new root check event. Analytic exposed rereads are recorded by their own 28-row bundle; topology uses the same three existing exposed groups and provenance wording QA adds no mathematical credit.'
}, indent=2)+'\n')
