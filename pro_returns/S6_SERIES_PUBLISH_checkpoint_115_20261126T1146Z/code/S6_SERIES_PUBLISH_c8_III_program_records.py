"""Derive Paper III's one records-page program table from its final printed paths.

The default is a read-only path/index inspection with no hashes or network.
--write retrieves exact pinned historical bytes into /tmp, hashes the selected
local and historical sources once, and writes only records_III.tsv. It never
imports or executes a mathematical program and changes no manuscript.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
import argparse
import csv
import hashlib
import json
import re
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT.parent
COMMIT = 'a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7'
REMOTE = 'https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/' + COMMIT + '/'
CP12 = 'pro_returns/S6_04_MAPS_MANIFOLDS_checkpoint_12_20261116T0243Z/S6_04_MAPS_MANIFOLDS/'
CP15 = 'pro_returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z/S6_10_PAPERS/'
GRIND10 = 'pro_returns/S6_SERIES_GRIND_checkpoint_10_20261120T0211Z/'
CP12_PATHS = {'code/kummer_normal_cover.py','code/kummer_orbits.py','code/manifolds_semistable.py'}
GRIND10_PATHS = {
    'code/III_invariant_chern_cone_fresh.py',
    'code/III_OS45_core_independent.py',
    'code/III_OS45_primitive_cubic_independent.py',
    'code/III_OS45_annulus_independent.py',
    'code/III_OS45_boundary_prisms_07.py',
    'code/III_weighted_OS45_checks.py',
}

def selected():
    text = (ROOT/'S6_SERIES_PUBLISH_III.tex').read_text(encoding='utf-8')
    start = text.index(r'\section{Programs}')
    end = text.index(r'\begin{thebibliography}', start)
    table = text[start:end]
    printed = re.findall(r'\\nolinkurl\{([^{}]+)\}', table)
    assert len(printed) == len(set(printed)) == 181
    index = set((BASE/'REPOSITORY_PROGRAM_PATHS.txt').read_text(encoding='utf-8').splitlines())
    rows = []
    for path in printed:
        if path.startswith('code/S6_SERIES_PUBLISH'):
            assert (ROOT/path).is_file(), path
            rows.append((path,path,'local'))
            continue
        if path in CP12_PATHS:
            full = CP12 + path
        elif path in GRIND10_PATHS:
            full = GRIND10 + path
        elif path.startswith('code/III/') or path.startswith('code/V/replay_chains/code/'):
            full = CP15 + path
        else:
            raise ValueError('No reviewed exact historical association: '+path)
        assert full in index, full
        rows.append((path,full,'historical'))
    return rows

def historical_bytes(item):
    printed, full, _ = item
    url = REMOTE + full
    request = urllib.request.Request(url, headers={'User-Agent':'S6-publication-source-verification/1.0'})
    with urllib.request.urlopen(request,timeout=40) as response:
        data = response.read()
        status = response.status
        resolved = response.geturl()
        content_type = response.headers.get('Content-Type','')
    assert status == 200 and data, (printed,status)
    assert not data.lstrip().lower().startswith(b'<!doctype html'), printed
    target = Path('/tmp/S6_SERIES_PUBLISH_c8_III_program_sources')/full
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_bytes(data)
    sha = hashlib.sha256(data).hexdigest()
    return printed,full,sha,dict(printed_path=printed,repository_path=full,requested_url=url,resolved_url=resolved,status=status,bytes=len(data),sha256=sha,content_type=content_type,retrieved_utc=datetime.now(timezone.utc).isoformat(),temporary_source=str(target),executed=False)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write',action='store_true')
    args=parser.parse_args()
    rows=selected()
    print('SELECTED',len(rows),'LOCAL',sum(x[2]=='local' for x in rows),'HISTORICAL',sum(x[2]=='historical' for x in rows))
    if not args.write:
        for printed,full,kind in rows:
            if kind=='historical':print(printed,'=>',full)
        print('INSPECT_ONLY; NO_HASHES_NETWORK_OR_WRITES')
        return
    hashes={}
    errors=[]
    for printed,full,kind in rows:
        if kind=='local':
            hashes[printed]=hashlib.sha256((ROOT/full).read_bytes()).hexdigest()
    with ThreadPoolExecutor(max_workers=6) as pool:
        futures={pool.submit(historical_bytes,item):item for item in rows if item[2]=='historical'}
        for future in as_completed(futures):
            item=futures[future]
            try:
                printed,full,sha,record=future.result()
                hashes[printed]=sha
                print(json.dumps(record,sort_keys=True),flush=True)
            except Exception as exc:
                record={'printed_path':item[0],'repository_path':item[1],'error':type(exc).__name__+': '+str(exc)}
                errors.append(record)
                print(json.dumps(record,sort_keys=True),flush=True)
    assert not errors, 'Historical retrieval failed; final table was not written'
    assert len(hashes)==181
    target=ROOT/'S6_SERIES_PUBLISH_records_III.tsv'
    with target.open('w',encoding='utf-8',newline='') as stream:
        writer=csv.DictWriter(stream,['printed_path','repository_path','sha256'],delimiter='\t',lineterminator='\n')
        writer.writeheader()
        writer.writerows(dict(printed_path=printed,repository_path=full,sha256=hashes[printed]) for printed,full,_ in rows)
    print('WROTE',str(target),'ROWS',181,'UTC',datetime.now(timezone.utc).isoformat())
    print('NO_MATHEMATICAL_PROGRAM_EXECUTED; NO_MANUSCRIPT_OR_CHECK_EVENT_MUTATION')

if __name__=='__main__':
    main()
