"""Restore the attached state, verify every manifest, and initialize the run.

No mathematical verification is awarded by this script.
"""
from pathlib import Path
import csv, hashlib, json, shutil, sys
from collections import Counter
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT.parent / 'S6_SERIES_GRIND_source'
CP = BASE / 'S6_GRIND_1_papers_cp15'
csv.field_size_limit(10**9)

def main():
    (ROOT / 'analysis').mkdir(exist_ok=True)
    (ROOT / 'code' / 'outputs').mkdir(exist_ok=True)
    verified, mismatches = [], []
    for manifest in sorted(BASE.glob('*_MANIFEST.tsv')):
        directory = BASE / manifest.name.removesuffix('_MANIFEST.tsv')
        with manifest.open() as stream:
            for row in csv.DictReader(stream, delimiter='\t'):
                path = directory / row['path']
                digest = hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None
                actual_size = path.stat().st_size if path.exists() else None
                result = dict(row, manifest=manifest.name, actual_size=actual_size, actual_sha256=digest)
                if str(actual_size) != row['size'] or digest != row['sha256']:
                    mismatches.append(result)
                verified.append(result)
    report = {'verified_count':len(verified), 'mismatches':mismatches}
    (ROOT/'code/outputs/source_verification.json').write_text(json.dumps(report,indent=2))
    if mismatches:
        raise RuntimeError(f'{len(mismatches)} source mismatches')
    with (CP/'S6_10_PAPERS_inventory.csv').open() as stream:
        rows=list(csv.DictReader(stream))
    for n,row in enumerate(rows,1):
        row.update(source_inventory_row=str(n), source_paper=row['paper'], tag='',
                   check_summary='Historical evidence retained; current-run assessment pending.',
                   confidence_line='Unassessed in this run; no completion inferred from inherited status.',
                   placement_state='pending migration', writing_state='pending standardization',
                   confidence_state='pending assessment', completion_state='pending',
                   literature_searches='')
        if row['paper']=='VI': row['paper']='II'
        if row['paper']=='III' and row['label'].startswith(('maps:src:E.1.','maps:src:E.2.')):
            row['paper']='V'
    with (ROOT/'S6_SERIES_GRIND_inventory.csv').open('w',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    for old,new in [('S6_10_PAPERS_notation_sheet.md','S6_SERIES_GRIND_notation_sheet.md'),
                    ('S6_10_PAPERS_references.bib','S6_SERIES_GRIND_references.bib'),
                    ('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv')]:
        shutil.copyfile(CP/old,ROOT/new)
    meta={'first_clock_observation_utc':'2026-11-19T18:40:01+00:00',
          'initialized_utc':datetime.now(timezone.utc).isoformat(),
          'base_zip':'S6_SERIES_GRIND.zip','base_zip_sha256':hashlib.sha256((ROOT.parent/'upload/S6_SERIES_GRIND.zip').read_bytes()).hexdigest(),
          'continuation':False,'next_checkpoint':1,'source_rows':len(rows),
          'source_statuses':dict(Counter(r['status'] for r in rows)),
          'model':'GPT-6 Astra (OpenAI), ChatGPT Pro mode',
          'effort':'Pro mode; no separate numeric effort setting is exposed'}
    (ROOT/'analysis/run.json').write_text(json.dumps(meta,indent=2))
    (ROOT/'S6_SERIES_GRIND_report.md').write_text('INCOMPLETE\n\n# S6_SERIES_GRIND report\n\n'
        '## Start and authority\n\nFresh run from the attached base archive and prompt only. '
        'The first clock observation was 19 November 2026, 18:40:01 UTC (19:40:01 Europe/Berlin). '
        'No earlier conversation or Library content was used.\n\n'
        f'All {len(verified)} payload entries in the six top-level manifests match their supplied sizes and SHA-256 values. '
        'The attached archive and source files are preserved without edits.\n\n'
        '## Completion standard\n\nMathematical status, placement, writing, and confidence are tracked separately. '
        'An inherited proved status, imported check event, source move, or successful build confers no new proof verification. '
        'The five-paper deliverable remains incomplete until all stated gates have been closed.\n\n'
        '## Current work\n\nInventory initialized; correction audit, high-risk sign-theorem audit, and Paper I audit in progress.\n')
    (ROOT/'PROGRESS_LEDGER.md').write_text('# Progress ledger\n\n'
        '## 2026-11-19 18:40 UTC — fresh run\n\n'
        'Main question: five complete papers in the requested standardized form, with every inventory row placed and checked.\n\n'
        'Initial gate: 1,524 inventory rows require placement, standardization and evidence assessment; '
        'the source has six papers and the deliverable has five. Mathematical statuses are retained as received.\n\n'
        'The first three-hour review is due approximately 21:40 UTC; subsequent reviews are hourly. '
        'Checkpoint 01 is due approximately 19:25 UTC, then every 45 minutes.\n\n'
        'Open mathematical rows are listed in analysis/open_rows_initial.tsv; every inventory row has separate completion fields.\n')
    openrows=[r for r in rows if r['status'] in ['open','proved under hypotheses H']]
    with (ROOT/'analysis/open_rows_initial.tsv').open('w',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=['source_inventory_row','paper','label','source_id','status'],delimiter='\t',extrasaction='ignore')
        writer.writeheader();writer.writerows(openrows)
    shutil.copyfile(ROOT.parent/'upload/PROMPT(20261119-183848).md',ROOT/'S6_SERIES_GRIND_PROMPT.md')
    print(json.dumps({'manifest_entries':len(verified),'mismatches':len(mismatches),'inventory_rows':len(rows),'open_mathematical_rows':len(openrows)}))

if __name__=='__main__': main()
