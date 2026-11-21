#!/usr/bin/env python3
"""Preview current PDF-bound tags, inventory and check files in isolation.

Runs the unchanged historical metadata program in a temporary shadow tree.
The generated outputs persist with an exact input-hash receipt. Canonical
files are copied back only with --apply. This creates no check event.
"""
from pathlib import Path
import argparse
import datetime as dt
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def sha(path):
    return path and hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('paper', choices=['I','II','III','IV','V'])
    p.add_argument('--build', type=Path, required=True)
    p.add_argument('--apply', action='store_true')
    p.add_argument('--certified', action='store_true')
    a = p.parse_args()
    build = a.build.resolve()
    source_name = f'S6_SERIES_PUBLISH_{a.paper}.tex'
    input_names = [source_name, 'S6_SERIES_PUBLISH_tags.tsv', 'S6_SERIES_PUBLISH_inventory.csv', 'CHECK_EVENTS.tsv']
    input_sha = {n:sha(ROOT/n) for n in input_names}
    summary = json.loads((build/'build_summary.json').read_text())
    assert input_sha[source_name] == summary['source_sha256']
    assert sha(build/f'S6_SERIES_PUBLISH_{a.paper}.pdf') == summary['pdf_sha256']
    if a.certified:
        receipt = json.loads((ROOT/f'records/S6_SERIES_PUBLISH_{a.paper}_final_pdf_receipt.json').read_text())
        assert receipt['all_pages_read'] and receipt['source_sha256'] == input_sha[source_name]
        assert receipt['pdf_sha256'] == summary['pdf_sha256']
    outputs = ['S6_SERIES_PUBLISH_tags.tsv', 'S6_SERIES_PUBLISH_inventory.csv',
               f'S6_SERIES_PUBLISH_checks_{a.paper}.md',
               f'records/S6_SERIES_PUBLISH_{a.paper}_current_metadata.json',
               f'records/S6_SERIES_PUBLISH_{a.paper}_current_statements.json']
    stamp = dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    run = ROOT/'agents/continuation_infra'/f'metadata_{a.paper}_{stamp}'
    generated = run/'generated'
    generated.mkdir(parents=True)
    program = ROOT/'code/S6_SERIES_PUBLISH_current_metadata.py'
    with tempfile.TemporaryDirectory(prefix='s6_metadata_', dir=ROOT.parent) as temp:
        shadow = Path(temp)
        (shadow/'code').mkdir()
        (shadow/'records').mkdir()
        for name in input_names:
            shutil.copyfile(ROOT/name, shadow/name)
        shadow_program = shadow/'code'/program.name
        shutil.copyfile(program, shadow_program)
        assert sha(shadow_program) == sha(program)
        cmd = [sys.executable, str(shadow_program), a.paper, '--build', str(build)]
        if a.certified:
            cmd.append('--certified')
        result = subprocess.run(cmd, capture_output=True, text=True)
        (run/'metadata.out').write_text(result.stdout)
        (run/'metadata.err').write_text(result.stderr)
        assert result.returncode == 0, result.stderr[-3000:]
        for name in outputs:
            target = generated/name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(shadow/name, target)
    assert input_sha == {n:sha(ROOT/n) for n in input_names}, 'A canonical input changed during the isolated metadata run.'
    before = {n:sha(ROOT/n) if (ROOT/n).exists() else None for n in outputs}
    if a.apply:
        for name in outputs:
            shutil.copyfile(generated/name, ROOT/name)
    receipt = dict(recorded_utc=dt.datetime.now(dt.timezone.utc).isoformat(), paper=a.paper,
                   applied=a.apply, certified_flag=a.certified, mathematical_events_added=0,
                   historical_program=str(program.relative_to(ROOT)), historical_program_sha256=sha(program),
                   build=str(build), build_summary_sha256=sha(build/'build_summary.json'),
                   input_sha256=input_sha, output_sha256={n:sha(generated/n) for n in outputs},
                   before_canonical_output_sha256=before,
                   metadata=json.loads((generated/f'records/S6_SERIES_PUBLISH_{a.paper}_current_metadata.json').read_text()),
                   scope='Exact input/output binding for the unchanged metadata extractor, run in isolation before an explicitly requested copy into canonical records. No mathematical or page-reading event.')
    (run/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(dict(receipt=str(run/'receipt.json'), applied=a.apply, metadata=receipt['metadata']),indent=2))


if __name__ == '__main__':
    main()
