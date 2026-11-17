"""Restore eleven independently approved PUSH wording repairs, exactly once.

The assembler used to filter on an audit status that changed after review.
The failure record, every old/new passage, and source hashes are retained.
This script deliberately edits only the frozen final manuscript; the
corresponding assembler rule was corrected in the same editorial pass.
"""
from pathlib import Path
import hashlib, json, re

D = Path(__file__).resolve().parents[2]
p = D / 'S6_09_PAPERS_III.tex'
before = p.read_text()
record = json.loads((D / 'work/cdp_audit/push_C_retention/current_editorial_regressions.json').read_text())
assert hashlib.sha256(before.encode()).hexdigest() == record['III_tex_sha256']
text = before
for fix in record['regressed_replacements']:
    assert text.count(fix['before']) == 1, (fix['source_id'], fix['before'])
    text = text.replace(fix['before'], fix['after'], 1)
assert re.findall(r'\\label\{([^}]+)\}', before) == re.findall(r'\\label\{([^}]+)\}', text)
assert before.count(r'\begin{proof}') == text.count(r'\begin{proof}')
assert before.count(r'\end{proof}') == text.count(r'\end{proof}')
p.write_text(text)
out = {
    'reader': 'GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026',
    'reason': 'Fresh source-to-print comparison detected eleven exact prior standalone repairs lost because the assembler filtered on a mutable audit-status string. All complete mathematical argument blocks were independently compared before this repair.',
    'before_tex_sha256': hashlib.sha256(before.encode()).hexdigest(),
    'after_tex_sha256': hashlib.sha256(text.encode()).hexdigest(),
    'events': record['regressed_replacements'],
    'unchanged_labels_and_proof_environment_counts': True,
    'preserved_failure_record': 'work/cdp_audit/push_C_retention/current_editorial_regressions.json',
    'assembler_repair': 'Apply the eleven exact prose replacements after the first five separately applied typography/reference replacements, irrespective of audit status.',
}
(D / 'records/III_final_push_prose_restoration.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'restored': len(out['events']), 'tex_sha256': out['after_tex_sha256']}))
