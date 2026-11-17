"""Preserve original course checkers and adjust only paths/provenance metadata."""
from pathlib import Path
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / 'sources/codex_workspace/courses/CG-S6'
OUT = ROOT / 'deliverables/code/maps_audit/course'
OUT.mkdir(parents=True, exist_ok=True)
records = []

for stem, chapter, report_name in [
    ('sphere_twists', 'sphere-twists-and-the-original-smooth-six-sphere-comparison.md', 'SPHERE_TWIST_CHECKS.json'),
    ('almost_complex', 'almost-complex-structures-and-integrability.md', 'ALMOST_COMPLEX_CHECKS.json'),
]:
    original_path = SRC / 'checks' / f'verify_{stem}.py'
    original = original_path.read_text()
    source_path = SRC / 'src' / chapter
    source_hash = hashlib.sha256(source_path.read_bytes()).hexdigest()
    retained = OUT / f'verify_{stem}.original_context.py'
    shutil.copy2(original_path, retained)
    shutil.copy2(SRC / 'checks' / report_name, OUT / report_name.replace('.json', '.original_context.json'))
    prefix = f'''# Path/provenance adaptation only, GPT-6 Astra, Pro, 2026-11-17.
import argparse
from pathlib import Path
_arguments = argparse.ArgumentParser(description="Run the unchanged finite mathematical checks; optionally verify the original chapter.")
_arguments.add_argument('--source', type=Path)
_options = _arguments.parse_args()
AUDIT_OUT = Path(__file__).resolve().parent
source = _options.source
RECORDED_SOURCE_SHA256 = {source_hash!r}
SOURCE_HASH_RECOMPUTED = source is not None
'''
    adapted = original.replace('W=Path(__file__).resolve().parents[1]\n', prefix)
    if stem == 'sphere_twists':
        adapted = adapted.replace("source=W/'src/sphere-twists-and-the-original-smooth-six-sphere-comparison.md'\n", '')
        start = adapted.index("src=source.read_text('utf-8');tags=")
        end = adapted.index("report=dict(status='passed'", start)
        source_checks = adapted[start:end]
        adapted = adapted[:start] + "mathematical_checks_passed=len(checks)\nsrc=None\nif source is not None:\n" + ''.join('    '+line+'\n' for line in source_checks.splitlines()) + adapted[end:]
        adapted = adapted.replace("source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),source=str(source.name),formulas=len(re.findall(r'\\\\\\(.*?\\\\\\)|\\\\\\[.*?\\\\\\]',src,re.S)),", "source_sha256=(hashlib.sha256(source.read_bytes()).hexdigest() if source else RECORDED_SOURCE_SHA256),source=(str(source) if source else None),formulas=(len(re.findall(r'\\\\\\(.*?\\\\\\)|\\\\\\[.*?\\\\\\]',src,re.S)) if src is not None else None),")
        # Keep the original formula-count expression literally while guarding the optional source.
        adapted = adapted.replace("source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),source=str(source.name),", "source_sha256=(hashlib.sha256(source.read_bytes()).hexdigest() if source else RECORDED_SOURCE_SHA256),source=(str(source) if source else None),")
        adapted = adapted.replace(",src,re.S)),checks=checks", ",src,re.S)) if src is not None else None),checks=checks") if 'formulas=(len(' not in adapted else adapted
        if 'formulas=len(' in adapted:
            adapted = adapted.replace('formulas=len(', 'formulas=(len(')
        adapted = adapted.replace("(W/'checks/SPHERE_TWIST_CHECKS.json')", "(AUDIT_OUT/'SPHERE_TWIST_CHECKS.json')")
        adapted = adapted.replace("(AUDIT_OUT/'SPHERE_TWIST_CHECKS.json').write_text", "report.update(source_hash_recomputed=SOURCE_HASH_RECOMPUTED,source_text_checks_executed=source is not None,mathematical_checks_passed=mathematical_checks_passed,reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode)',effort='Pro',date='2026-11-17')\n(AUDIT_OUT/'SPHERE_TWIST_CHECKS.json').write_text")
        original_math = original[original.index('checks=[]'):original.index("src=source.read_text('utf-8');tags=")]
        adapted_math = adapted[adapted.index('checks=[]'):adapted.index('mathematical_checks_passed=len(checks)')]
    else:
        adapted = adapted.replace("source=W/'src/almost-complex-structures-and-integrability.md'\n", '')
        adapted = adapted.replace("source_sha256=hashlib.sha256(source.read_bytes()).hexdigest()", "source_sha256=(hashlib.sha256(source.read_bytes()).hexdigest() if source else RECORDED_SOURCE_SHA256)")
        adapted = adapted.replace("(W/'checks/ALMOST_COMPLEX_CHECKS.json')", "(AUDIT_OUT/'ALMOST_COMPLEX_CHECKS.json')")
        adapted = adapted.replace("(AUDIT_OUT/'ALMOST_COMPLEX_CHECKS.json').write_text", "out.update(source_hash_recomputed=SOURCE_HASH_RECOMPUTED,reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode)',effort='Pro',date='2026-11-17')\n(AUDIT_OUT/'ALMOST_COMPLEX_CHECKS.json').write_text")
        original_math = original[original.index('checks=[]'):original.index("source=W/'src/almost-complex-structures-and-integrability.md'")]
        adapted_math = adapted[adapted.index('checks=[]'):adapted.index('out=dict(source_sha256=')]
    assert original_math == adapted_math, stem
    compile(adapted, str(OUT / f'verify_{stem}.py'), 'exec')
    (OUT / f'verify_{stem}.py').write_text(adapted)
    records.append(dict(
        script=f'deliverables/code/maps_audit/course/verify_{stem}.py',
        original_context_copy=str(retained.relative_to(ROOT)),
        original_sha256=hashlib.sha256(original_path.read_bytes()).hexdigest(),
        adapted_sha256=hashlib.sha256(adapted.encode()).hexdigest(),
        mathematical_body_sha256=hashlib.sha256(original_math.encode()).hexdigest(),
        mathematical_body_unchanged=True,
        source_file=str(source_path.relative_to(ROOT)), source_sha256=source_hash,
        only_changes='Output paths and optional original-source metadata/text checks. Every mathematical assertion and calculation is unchanged.',
        original_producer_header=source_path.read_text().splitlines()[:5],
    ))
(OUT / 'additional_portable_preparation.json').write_text(json.dumps(records, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(records, ensure_ascii=False, indent=2))
