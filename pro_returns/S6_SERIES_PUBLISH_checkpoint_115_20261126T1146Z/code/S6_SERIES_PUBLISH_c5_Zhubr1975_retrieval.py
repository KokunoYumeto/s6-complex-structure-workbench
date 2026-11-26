#!/usr/bin/env python3
"""Retrieve the primary English scan outside the checkpoint; report metadata only."""
from pathlib import Path
import hashlib
import http.cookiejar
import urllib.request

page='https://www.mathnet.ru/eng/im2054'
endpoint='https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=2054&what=fullteng'
path=Path('/tmp/S6_SERIES_PUBLISH_c5_Zhubr1975.pdf')
expected='619389545e0b3f808339cab5ea0d55faf42770565d4b714e53e7b91bb17e1b83'
final='https://www.mathnet.ru/links/9fd2049669a05bb4d8184e53fd4b13eb/im2054_eng.pdf'
if not path.exists():
    opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
    opener.addheaders=[('User-Agent','Mozilla/5.0'),('Referer',page)]
    with opener.open(page,timeout=45) as response:
        response.read()
    with opener.open(endpoint,timeout=45) as response:
        data=response.read();final=response.geturl()
    assert data.startswith(b'%PDF-')
    path.write_bytes(data)
data=path.read_bytes()
assert data.startswith(b'%PDF-')
assert len(data)==917690
assert hashlib.sha256(data).hexdigest()==expected
print('A. V. Zhubr, Classification of simply-connected six-dimensional spin manifolds, English 1975 scan')
print('Archive:',page)
print('Endpoint:',endpoint)
print('Successful retrieval final URL:',final)
print('Bytes:',len(data))
print('SHA256:',expected)
print('Primary scan stays in /tmp; no source content enters a checkpoint.')
