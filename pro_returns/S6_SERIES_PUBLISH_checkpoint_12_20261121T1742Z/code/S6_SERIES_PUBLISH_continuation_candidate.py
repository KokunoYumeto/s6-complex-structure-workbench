#!/usr/bin/env python3
"""Build a frozen Paper I candidate and preserve exact page-equality evidence.

Runs the unchanged build, render, and reading-coverage helpers. It never marks
the candidate certified and never supplies an actual reading or math event.
"""
from pathlib import Path
import argparse
import csv
import datetime as dt
import hashlib
import json
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
csv.field_size_limit(100_000_000)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_text())


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('candidate',type=int)
    p.add_argument('--previous',type=int,required=True)
    p.add_argument('--expected-source-sha256',required=True)
    p.add_argument('--expected-defect-rows',type=int,required=True)
    a=p.parse_args()
    source=ROOT/'S6_SERIES_PUBLISH_I.tex'
    defects=ROOT/'S6_SERIES_PUBLISH_defects_I.tsv'
    assert sha(source)==a.expected_source_sha256,'Source differs from the frozen handback.'
    assert len(list(csv.DictReader(defects.open(),delimiter='\t')))==a.expected_defect_rows
    source_sha,defect_sha=sha(source),sha(defects)
    prior=ROOT/f'records/S6_SERIES_PUBLISH_I_candidate{a.previous}_complete_coverage_snapshot.json'
    previous=load(prior)
    assert previous['all_pages_read'] and previous['missing_pages']==[]
    build=ROOT/f'build/I_candidate{a.candidate}'
    render=ROOT/f'render/I_candidate{a.candidate}'
    comparison=ROOT/f'agents/continuation_infra/S6_SERIES_PUBLISH_I_candidate{a.candidate}_image_comparison.json'
    progress=ROOT/f'records/S6_SERIES_PUBLISH_continuation_I_candidate{a.candidate}_progress.json'
    assert not any(x.exists() for x in [build,render,comparison,progress]),'Candidate output already exists.'
    stamp=dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    operation=ROOT/f'agents/continuation_infra/candidate{a.candidate}_operation_{stamp}'
    operation.mkdir()
    for src,suffix in [(source,'source_for_mapping.tex'),(defects,'defects_for_mapping.tsv')]:
        target=ROOT/f'agents/continuation_infra/S6_SERIES_PUBLISH_I_candidate{a.candidate}_{suffix}'
        if target.exists():
            assert sha(target)==sha(src)
        else:
            with target.open('xb') as f:f.write(src.read_bytes())
    operations=[]
    def run(name,program,*args):
        command=[sys.executable,str(ROOT/'code'/program),*map(str,args)]
        with (operation/(name+'.out')).open('w') as out,(operation/(name+'.err')).open('w') as err:
            result=subprocess.run(command,cwd=ROOT,stdout=out,stderr=err)
        operations.append(dict(name=name,command=command,returncode=result.returncode))
        assert result.returncode==0,(name,'See '+str(operation/(name+'.err')))
    run('build','S6_SERIES_PUBLISH_build.py',source,'--output-dir',build)
    summary=load(build/'build_summary.json')
    assert summary['source_sha256']==source_sha
    assert sha(source)==source_sha and sha(defects)==defect_sha,'Canonical inputs changed during build.'
    run('render','S6_SERIES_PUBLISH_render.py',build/'S6_SERIES_PUBLISH_I.pdf','--output-dir',render,'--scale','1.6')
    run('compare','S6_SERIES_PUBLISH_compare_page_images.py',prior,render/'manifest.json','--output',comparison)
    assert sha(source)==source_sha and sha(defects)==defect_sha,'Canonical inputs changed during render.'
    run('coverage','S6_SERIES_PUBLISH_reading_coverage.py','I','--render',render)
    run('progress','S6_SERIES_PUBLISH_continuation_tools.py','snapshot','--render','I='+str(render),'--output',progress)
    comp=load(comparison)
    coverage=load(ROOT/'records/S6_SERIES_PUBLISH_I_page_coverage.json')
    assert not coverage['certified']
    receipt=dict(recorded_utc=dt.datetime.now(dt.timezone.utc).isoformat(),paper='I',candidate=a.candidate,
                 previous_candidate=a.previous,source_sha256=source_sha,defect_log_sha256=defect_sha,
                 defect_rows=a.expected_defect_rows,pdf_sha256=summary['pdf_sha256'],build_summary=summary,
                 render_manifest_sha256=sha(render/'manifest.json'),comparison_sha256=sha(comparison),
                 pages=comp['pages'],identical_entire_png_pages=comp['identical_entire_png_pages'],
                 different_pages=comp['different_pages'],covered_pages=coverage['covered_pages'],
                 certified=False,mathematical_events_added=0,page_reading_events_added=0,
                 operations=operations,scope='Build, render, exact image comparison, and existing reading-evidence collection only.')
    (operation/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(dict(operation=str(operation),source_sha256=source_sha,pdf_sha256=summary['pdf_sha256'],
                         pages=comp['pages'],identical=len(comp['identical_entire_png_pages']),changed=len(comp['different_pages']),
                         different_pages=comp['different_pages'],covered_pages=coverage['covered_pages'],certified=False),indent=2))


if __name__=='__main__':main()
