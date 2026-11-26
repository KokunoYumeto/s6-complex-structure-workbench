"""Record source-finding admissions and complete T1's exact local edit record."""
from pathlib import Path
from datetime import datetime, timezone
from zipfile import ZipFile
import csv
import importlib.util

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)

def read_table(path):
    with path.open(newline='') as stream:
        reader = csv.DictReader(stream, delimiter='\t')
        return reader.fieldnames, list(reader)

def write_table(path, fields, rows):
    with path.open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)

spec = importlib.util.spec_from_file_location('alias_repair', ROOT / 'code/S6_SERIES_PUBLISH_c9_display_aliases.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
archive = ROOT.parents[1] / 'upload/S6_SERIES_PUBLISH_continue_cp100.zip'
with ZipFile(archive) as z:
    original = z.read('S6_SERIES_PUBLISH_checkpoint_100/S6_SERIES_PUBLISH_III.tex').decode()
repaired, old_preamble, changes = module.candidate(original)
assert len(changes) == 7
old = [old_preamble]
new = [module.BLOCK]
for primary, alias, before, after in changes:
    heading = '\n\n% Exact display fragment: ' + primary + ' / ' + alias + '\n'
    old.append(heading + before)
    new.append(heading + after)
df, defects = read_table(ROOT / 'S6_SERIES_PUBLISH_defects_III.tsv')
matches = [r for r in defects if r['change_id'] == 'CLAUDE-III-T1']
assert len(matches) == 1
row = matches[0]
assert row['old_text'] == old_preamble and row['new_text'] == module.BLOCK
row['old_text'] = ''.join(old)
row['new_text'] = ''.join(new)
row['reason'] += (' The exact old/new fields now include each of the seven display fragments, '
    'recovered directly from the attached checkpoint source without changing the current manuscript. '
    'Both legacy and current-kernel isolated diagnostics establish complete ordinary/@cref '
    'record equality; current-kernel PDF annotations and destinations are retained in '
    'code/S6_SERIES_PUBLISH_c9_current_alias_evidence.json.')
write_table(ROOT / 'S6_SERIES_PUBLISH_defects_III.tsv', df, defects)

now = datetime.now(timezone.utc).isoformat()
ff, findings = read_table(ROOT / 'S6_SERIES_PUBLISH_findings_III.tsv')
resolutions = {
    'P1': 'Abstract names the elliptic fibre configurations; first main-text use defines the Oguiso–Shioda table convention and distinguishes its entry numbers from inverse heights.',
    'P3': 'Open problems uses an unnumbered part heading with its own table-of-contents entry.',
    'P5': 'Zhubr locators agree: Theorems 3 and 5, pages 795–796, and section 4.1, page 809.',
    'P6': 'The conjunction and parenthesized alternative in the exact freeness condition are explicit.',
    'P7': 'The publication work has one GPT-6 Astra/OpenAI/ChatGPT Pro setup description with its actual continuation dates and the Claude reading dates.',
    'P8': 'The general twists, period vectors, finite actions and clutch integers are defined before use, with the existing conventions retained.',
    'P9': 'Hatcher Additional Topics has its author-PDF date/version and exact theorem/page locator.',
    'P10': 'The covering-space lift cites Hatcher Proposition 1.33, page 61.',
    'P12': 'The two references address the displayed equation; the q2 deduction stands in the corollary that states it.',
    'P13': 'The two incorrect literal Theorem references now use the target-aware reference to the lemma.',
    'P16': 'The IV-star monodromy uses the IV-star subscript throughout the matrix definition and dependent Hurwitz comparison; entries unchanged.',
    'P17': 'The all-positive-weight representative is M_d^w; the coprime-to-six comparison with the cyclic representative retains its explicit oriented identification and marked H2 map.',
}
for row in findings:
    key = row['id']
    if key in resolutions:
        assert row['status'] == 'open', key
        row.update(status='done', date_utc=now, source_resolution=resolutions[key],
            remaining_gate='Final rendered-page reading is tracked separately by the paper PDF gate.',
            evidence='code/S6_SERIES_PUBLISH_c9_admit_findings.py/.out; CLAUDE-III-' + key + ' defect rows; agents/continuation9_findings/S6_SERIES_PUBLISH_c9_named_findings_review.md')
    elif key == 'T1':
        row.update(date_utc=now,
            source_resolution='The seven display aliases now copy complete primary auxiliary records. Legacy and current-kernel isolated diagnostics pass; all current-kernel ordinary/@cref pairs, destinations and 21 links match.',
            remaining_gate='Full manuscript builds on both kernels and final PDF alias checks.',
            evidence='CLAUDE-III-T1; code/S6_SERIES_PUBLISH_c9_current_alias_evidence.json; agents/continuation9_defect_records/S6_SERIES_PUBLISH_III_current_kernel_alias_review.md')
    elif key in ('P2','P11','P15'):
        row.update(date_utc=now,
            source_resolution='The named-locus edits are admitted with exact old/new records and inverse-checked substitutions; the wider contextual sweep is in progress.',
            remaining_gate='Whole-paper contextual disposition followed by final rendered-page reading.',
            evidence='code/S6_SERIES_PUBLISH_c9_admit_findings.py/.out; code/S6_SERIES_PUBLISH_c9_admit_notation.py/.out; code/S6_SERIES_PUBLISH_c9_admit_wording.py/.out')
write_table(ROOT / 'S6_SERIES_PUBLISH_findings_III.tsv', ff, findings)
print('Completed exact T1 record: preamble plus all seven before/after display fragments.')
print('Marked twelve supplied source findings done under prompt section 0.4.')
print('T1, P2, P11, P14 and P15 remain open; P4 remains deferred to the joint phase.')
print('No final-PDF, required-check or whole-unit credit added.')
