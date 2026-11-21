#!/usr/bin/env python3
"""Open the stated immutable GitHub commit and match selected attached records."""
import hashlib
import json
import urllib.request
from pathlib import Path

BASE = Path(__file__).resolve().parents[4]
SOURCE = BASE / 'source'
REPO = 'KokunoYumeto/s6-complex-structure-workbench'
COMMIT = '83d76022bcd442278b760db9ff438afceed6c6ea'
DIRECTORY = 'pro_returns/S6_SERIES_GRIND_checkpoint_10_20261120T0211Z'

def get(url):
    request = urllib.request.Request(url, headers={'User-Agent':'S6-publication-provenance-check'})
    with urllib.request.urlopen(request, timeout=60) as response:
        body = response.read()
        return response.status, body

def main():
    receipt = {'commit':COMMIT,'repository':REPO,'directory':DIRECTORY,'checks':[]}
    url = f'https://api.github.com/repos/{REPO}/commits/{COMMIT}'
    status, body = get(url)
    data = json.loads(body)
    assert data['sha'] == COMMIT
    receipt['checks'].append({'url':url,'http_status':status,'resolved_sha':data['sha'],
                             'commit_date':data['commit']['committer']['date'],
                             'message':data['commit']['message'],
                             'response_sha256':hashlib.sha256(body).hexdigest()})
    url = f'https://api.github.com/repos/{REPO}/contents/{DIRECTORY}?ref={COMMIT}'
    status, body = get(url)
    data = json.loads(body)
    receipt['checks'].append({'url':url,'http_status':status,'entry_count':len(data),
                             'entries':[r['name'] for r in data],
                             'response_sha256':hashlib.sha256(body).hexdigest()})
    for name in ['CHECK_EVENTS.tsv','S6_SERIES_GRIND_tags.tsv','S6_SERIES_GRIND_V.tex']:
        url = f'https://raw.githubusercontent.com/{REPO}/{COMMIT}/{DIRECTORY}/{name}'
        status, body = get(url)
        actual = hashlib.sha256(body).hexdigest()
        attached = (SOURCE/name).read_bytes()
        expected = hashlib.sha256(attached).hexdigest()
        receipt['checks'].append({'url':url,'http_status':status,'bytes':len(body),
                                 'sha256':actual,'attached_sha256':expected,
                                 'matches_attached':actual==expected,
                                 'matches_after_CRLF_transport':body.replace(b'\r\n',b'\n') == attached.replace(b'\r\n',b'\n'),
                                 'attached_bytes':len(attached)})
    print(json.dumps(receipt,indent=2))

if __name__ == '__main__': main()
