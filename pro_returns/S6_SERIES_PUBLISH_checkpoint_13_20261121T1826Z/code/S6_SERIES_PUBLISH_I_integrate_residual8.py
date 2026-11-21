from pathlib import Path
import datetime, hashlib, json
from S6_SERIES_PUBLISH_editing import Editor

r = Path(__file__).resolve().parents[1]
p = r / 'agents/i_topology/editorial/S6_SERIES_PUBLISH_I_residual_batch8_guarded.json'
d = json.loads(p.read_text())
ed = Editor('I')
before_sha = hashlib.sha256(ed.text.encode()).hexdigest()
for i, g in enumerate(d['patches']):
    kind = ('D12' if i < 4 else
            'D16' if i in {4, 7, 8, 9, 11} else
            'D04' if i in {5, 6, 64} else
            'D23' if i == 10 else
            'D09' if i == 38 else
            'D11' if i == 90 else
            'D01' if i in {67, 70, 71, 76, 77, 78, 79} else
            'D08' if i >= 92 or i in {15, 16, 17, 21, 28, 59, 60, 68} else
            'D02')
    ed.replace(g['old'], g['new'], kind, g['reason'],
               ', '.join(g.get('statement_ids', [])))
ed.save()
receipt = {
    'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'before_sha256': before_sha,
    'after_sha256': hashlib.sha256(ed.text.encode()).hexdigest(),
    'guard_path': str(p.relative_to(r)),
    'guard_sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
    'guards': len(d['patches']),
    'root_read_scope': 'Every old/new guard, the complete B4.2 statement and both proofs, the complete removed A4.5 statement/proof, the exact replacement summary, and the complete agent comparison/inspection receipt were read. The agent compared the full downstream target results. The gradient retraction remains the specialization map used downstream. Every unchanged named object in epithet deletions retains its identical definition, marking and maps.',
    'check_credit': 'Two exposed rereads in the agent event bundle; no extra root event or fresh mathematical independence credit.',
    'remaining_gates': 'Equation numbering, final build, actual page reading and final provenance/deposit synchronization.'
}
(r / 'records/S6_SERIES_PUBLISH_I_residual8_integration.json').write_text(json.dumps(receipt, indent=2) + '\n')
