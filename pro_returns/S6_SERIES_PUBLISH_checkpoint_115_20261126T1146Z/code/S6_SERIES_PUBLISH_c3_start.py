from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
START = '2026-11-22T16:56:58+00:00'
FIELDS = ['paper', 'unit_id', 'unit_title', 'row_kind', 'defect_type', 'status', 'date_utc', 'evidence', 'detail']


def units(text):
    body = text.split('\\begin{document}', 1)[1]
    headings = list(re.finditer(r'^\\(section|subsection)\{([^\n]*)', body, re.M))
    for i, match in enumerate(headings):
        kind = match.group(1)
        end = headings[i + 1].start() if i + 1 < len(headings) else len(body)
        if kind == 'section' and i + 1 < len(headings) and headings[i + 1].group(1) == 'subsection':
            continue
        title = match.group(2).split('}\\hypertarget', 1)[0].split('}\\label', 1)[0]
        if title.endswith('}'):
            title = title[:-1]
        labels = re.findall(r'\\label\{([^}]+)\}', body[match.start():end])
        ident = labels[0] if labels else re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
        yield ident, title


def main():
    target = ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv'
    if target.exists():
        raise SystemExit('Continuation already initialized; existing rows preserved.')
    rows = []
    totals = {}
    for paper in ['II', 'III', 'IV']:
        paper_units = list(units((ROOT / f'S6_SERIES_PUBLISH_{paper}.tex').read_text()))
        totals[paper] = len(paper_units)
        for ident, title in paper_units:
            for number in range(1, 26):
                defect = f'D{number:02}'
                done = paper == 'II' and defect in ['D10', 'D16']
                rows.append(dict(zip(FIELDS, [paper, ident, title, 'defect', defect,
                    'done' if done else 'open', START, 'checkpoint 35; controlling prompt section 0.4',
                    'Inherited completed class; reopen only on an observed instance.' if done else
                    'Complete unit reading and per-instance edits still required.'])))
            rows.append(dict(zip(FIELDS, [paper, ident, title, 'structure', '', 'open', START,
                'controlling prompt section 3.4', 'Final placement and single ownership require unit review.'])))
    with target.open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)
    addition = f'''\n\n## Third continuation started — {START}

All 11,270 base files verified with `python restore_cp35.py`: zero size or SHA-256 mismatches. The merged checkpoint-35 folder is the working directory. Its Paper II source is the recorded `558e587c...` version. The controlling prompt dated 22 November supersedes prior restoration, link, record and checkpoint rules.

Paper II remains first. Its 198 required checks are resolved; D10 and D16 remain done. The other 23 classes, restructuring, provenance, integrated build and final-page reading remain open. Papers III and IV retain 128 and 66 required checks respectively. Papers I and V retain their completed gates until the five-together step, which starts from their attached posted sources.

`S6_SERIES_PUBLISH_unit_progress.tsv` gives the current unit-by-unit text rows required by section 0.4: II {totals['II']} units, III {totals['III']} units, IV {totals['IV']} units. The previously recorded required-check and provenance rows remain in their existing records. New edits are recorded only in the defects table and actual proof comparisons in `CHECK_EVENTS.tsv`; derived deliverables wait until the text is final.

The initial parallel text assignments cover the consecutive foundations and conductor sections; a third track completes Paper II provenance and records-path verification. Root integrates text in body order and handles the remaining sections. No new check or completed text row is asserted by this initialization.

Next checkpoint: 2026-11-22T17:41:58+00:00 (36). Next hourly progress review: 2026-11-22T17:56:58+00:00 (24). Consecutive reviews without movement: 0.
'''
    for name in ['PROGRESS_LEDGER.md', 'S6_SERIES_PUBLISH_report.md']:
        with (ROOT / name).open('a', newline='\n') as f:
            f.write(addition)
    print(f'Started {START}; {len(rows)} unit rows; unit counts {totals}.')


if __name__ == '__main__':
    main()
