"""Portable copies of nine completely read stable-provider checkers.

Only output/source paths and present-reader metadata change. Original bytes
are retained separately. The original historical scope strings remain intact.
"""
from pathlib import Path
import ast
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / 'sources/codex_workspace/courses/CG-S6'
OUT = ROOT / 'deliverables/code/maps_audit/course/stable'
OLD = OUT / 'original_context'
OLD.mkdir(parents=True, exist_ok=True)
SPECS = [
    ('verify_integral_stable_comparison.py', 'the-original-integral-stable-group-and-its-completion-maps.md'),
    ('verify_arithmetic_completion.py', 'the-original-adams-tower-and-arithmetic-completion.md'),
    ('verify_adams_tower.py', 'the-adams-tower-and-exact-inverse-limits.md'),
    ('verify_finite_cocycle_model.py', 'the-adams-tower-and-exact-inverse-limits.md'),
    ('verify_formal_two_series.py', 'the-exact-characteristic-two-coordinate-calculation.md'),
    ('verify_projective_cooperation.py', 'the-original-projective-coordinate-and-actual-cooperations.md'),
    ('verify_actual_degree_eight.py', 'the-actual-mod-two-cooperation-comparison-through-degree-eight.md'),
    ('verify_actual_cooperation.py', 'the-actual-mod-two-adams-resolution-and-cooperation-maps.md'),
    ('verify_odd_prime_bar.py', 'the-original-odd-prime-cooperations-and-degree-six-adams-calculation.md'),
]
records = []
for filename, chapter in SPECS:
    source = SRC / 'checks' / filename
    original = source.read_text()
    shutil.copyfile(source, OLD / filename)
    chapter_hash = hashlib.sha256((SRC / 'src' / chapter).read_bytes()).hexdigest()
    prefix = (
        'W=Path(__file__).resolve().parent\n'
        'import sys\n'
        'SOURCE_ARG=Path(sys.argv[1]) if len(sys.argv)>1 else None\n'
        'SOURCE_HASH_RECOMPUTED=bool(SOURCE_ARG and SOURCE_ARG.is_file())\n'
        'SOURCE_SHA256=hashlib.sha256(SOURCE_ARG.read_bytes()).hexdigest() if SOURCE_HASH_RECOMPUTED else '
        + repr(chapter_hash)
    )
    assert original.count('W=Path(__file__).resolve().parents[1]') == 1
    text = original.replace('W=Path(__file__).resolve().parents[1]', prefix)
    hash_occurrences = sum(text.count(f'hashlib.sha256({name}.read_bytes()).hexdigest()') for name in ['src', 'p'])
    assert hash_occurrences == 1, (filename, hash_occurrences)
    for name in ['src', 'p']:
        text = text.replace(f'hashlib.sha256({name}.read_bytes()).hexdigest()', 'SOURCE_SHA256')
    text = text.replace("W/'checks/", "W/'").replace("str(R/'checks')", 'str(R)')
    assert text.count('dict(passed=len(checks)') >= 1
    # Only the first such dictionary is the persisted report. In several
    # checkers the later dictionary is a deliberately short stdout summary.
    text = text.replace(
        'dict(passed=len(checks)',
        "dict(reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode)', effort='Pro', date='2026-11-17', source_hash_recomputed=SOURCE_HASH_RECOMPUTED, retained_original_scope=True, passed=len(checks)",
        1,
    )
    ast.parse(text)
    (OUT / filename).write_text(text)
    records.append(dict(
        program=filename,
        source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
        portable_sha256=hashlib.sha256((OUT / filename).read_bytes()).hexdigest(),
        source_chapter=chapter,
        recorded_original_source_sha256=chapter_hash,
        source_line_count=len(original.splitlines()),
        full_code_read=True,
        mathematical_checks_unchanged=True,
        changes='Output beside __file__; sibling helper path; optional first source-path argument recomputes only the provenance hash, otherwise original hash with source_hash_recomputed=false; added exact current-reader metadata. All mathematical code, ranges, assertions, check names and historical scope strings retained.',
        reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode)', effort='Pro', date='2026-11-17',
    ))
(OUT / 'remaining_portable_preparation.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'prepared': len(records), 'complete_program_lines_read': sum(r['source_line_count'] for r in records)}))
