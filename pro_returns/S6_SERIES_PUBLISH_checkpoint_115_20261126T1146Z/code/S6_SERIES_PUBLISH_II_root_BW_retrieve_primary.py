#!/usr/bin/env python3
"""Retrieve the exact primary editions needed for the BW comparison.

Downloaded works stay outside the checkpoint tree. Only retrieval metadata
and bounded reading records belong in the lean checkpoint.
"""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
TEMP = ROOT.parent.parent / 'S6_SERIES_PUBLISH_root_BW_primary_temp'
TEMP.mkdir(exist_ok=True)
SOURCES = [
    ('MerleTeissier1977', 'https://www.numdam.org/item/SSS_1976-1977____A16_0.pdf'),
    ('Steenbrink1989Spectrum', 'https://www.numdam.org/article/AST_1989__179-180__163_0.pdf'),
    ('Nemethi1991Join', 'https://www.numdam.org/article/CM_1991__80_1_1_0.pdf'),
]


def fetch(item):
    name, url = item
    request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(request, timeout=40) as response:
            data = response.read()
            final_url = response.geturl()
        assert data.startswith(b'%PDF')
        path = TEMP / (name + '.pdf')
        path.write_bytes(data)
        return dict(name=name, requested_url=url, final_url=final_url,
                    bytes=len(data), sha256=sha256(data).hexdigest(),
                    temporary_path=str(path), status='downloaded')
    except Exception as error:
        return dict(name=name, requested_url=url, status='failed', error=str(error))


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=3) as pool:
        entries = list(pool.map(fetch, SOURCES))
    output = dict(created_utc=datetime.now(timezone.utc).isoformat(),
                  sources=entries, scope='Retrieval only; reading is recorded separately')
    path = ROOT / 'agents/continuation2_root/01BW/S6_SERIES_PUBLISH_II_root_BW_primary_retrieval.json'
    assert not path.exists(), 'Do not overwrite an earlier retrieval event'
    path.write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps(output, indent=2))
