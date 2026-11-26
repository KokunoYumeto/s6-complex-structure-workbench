#!/usr/bin/env python3
"""Retrieve primary inputs outside the checkpoint; write metadata only."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import csv
import hashlib
from pathlib import Path
import subprocess
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
TMP = ROOT.parents[1] / 'tmp' / 'c3_provenance_primary'
OUT = ROOT / 'agents' / 'continuation3_provenance' / 'next_part'
SOURCES = [
 ('AbashevaDeev_v1', 'https://arxiv.org/pdf/2303.10764v1', 'arXiv:2303.10764v1'),
 ('Fujino2021_author', 'https://www.math.kyoto-u.ac.jp/~fujino/surfaces-classC2.pdf', 'author version 0.08, 20 January 2020'),
 ('Meersseman2019', 'https://numdam.org/item/10.5802/jep.108.pdf', 'JEP 6 (2019), pp.879–945'),
 ('Lazzeri1973', 'https://www.numdam.org/item/AST_1973__7-8__269_0.pdf', 'Astérisque 7–8 (1973), pp.269–275'),
 ('HondaViaclovsky_v1', 'https://arxiv.org/pdf/2504.14420v1', 'arXiv:2504.14420v1'),
 ('Grauert1960', 'https://www.numdam.org/item/PMIHES_1960__5__5_0.pdf', 'Publ.Math.IHES 5 (1960), pp.5–64'),
 ('Grauert1963', 'https://www.numdam.org/item/PMIHES_1963__16__35_0.pdf', 'Publ.Math.IHES 16 (1963), pp.35–36'),
 ('RamisRuget1970', 'https://www.numdam.org/item/PMIHES_1970__38__77_0.pdf', 'Publ.Math.IHES 38 (1970), pp.77–91'),
 ('Demailly2012', 'https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf', 'author book; title-page date read separately'),
]

def fetch(item):
    key, url, version = item
    path = TMP / (key + '.pdf')
    result = dict(key=key, url=url, version=version,
                  opened_utc=datetime.now(timezone.utc).isoformat(),
                  temporary_path=str(path), status='', sha256='', bytes='')
    try:
        with urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=50) as response:
            content = response.read()
        if not content.startswith(b'%PDF'):
            raise ValueError('response is not PDF')
        path.write_bytes(content)
        result.update(status='downloaded', sha256=hashlib.sha256(content).hexdigest(),
                      bytes=str(len(content)))
        subprocess.run(['pdftotext', '-layout', str(path), str(path.with_suffix('.txt'))],
                       check=True, capture_output=True)
    except Exception as exc:
        result['status'] = type(exc).__name__ + ': ' + str(exc)
    return result

def main():
    TMP.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(max_workers=6) as pool:
        rows = list(pool.map(fetch, SOURCES))
    with (OUT / 'S6_SERIES_PUBLISH_next_downloads.tsv').open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), delimiter='\t')
        writer.writeheader()
        writer.writerows(rows)
    for row in rows:
        print(row['key'], row['status'], row['bytes'], row['sha256'])

if __name__ == '__main__':
    main()
