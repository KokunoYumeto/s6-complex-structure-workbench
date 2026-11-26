"""Extract eight exact Paper II owner blocks and adjacent prose for editorial review.

This creates no candidate full paper and makes no canonical mutation.
"""
from pathlib import Path
import datetime
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_D09_D04_batch06_working'
OUT.mkdir(exist_ok=True)
source = (ROOT / 'S6_SERIES_PUBLISH_II.tex').read_text()
sha = lambda text: hashlib.sha256(text.encode()).hexdigest()
owners = {
    '01B9': 'cdp:st:A.5.19',
    '01BC': 'cdp:st:A.5.21',
    '02XD': 'night:P4.4',
    '01GE': 'cdp:st:D.2.7',
    '01D7': 'cdp:st:C.2.UN.29',
    '01DC': 'cdp:st:C.2.UN.33',
    '01DF': 'cdp:st:C.2.UN.36',
    '01DI': 'cdp:st:C.2.UN.39',
}
env = re.compile(r'\\begin\{(?:proposition|lemma|theorem|corollary|definition|remark)\}')
rows = []
for tag, owner in owners.items():
    token = '\\label{' + owner + '}'
    assert source.count(token) == 1
    location = source.index(token)
    start = list(env.finditer(source, 0, location))[-1].start()
    end = source.index('\\end{proof}', location) + len('\\end{proof}')
    next_env = env.search(source, end)
    assert next_env
    body = source[start:end]
    following = source[end:next_env.start()]
    assert '\\hypertarget{tag-' + tag + '}' in body
    for suffix, text in [('before', body), ('following_before', following)]:
        path = OUT / f'S6_SERIES_PUBLISH_II_A2_{tag}_{suffix}.tex'
        assert not path.exists(), path
        path.write_text(text)
    rows.append(dict(tag=tag, owner=owner, source_character_span=[start, end],
                     source_line=source.count('\n', 0, start) + 1,
                     bytes=len(body.encode()), sha256=sha(body),
                     following_bytes=len(following.encode()), following_sha256=sha(following)))
record = dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
              source_sha256=sha(source), owners=rows, canonical_mutations=0)
(OUT / 'S6_SERIES_PUBLISH_II_A2_batch06_extraction.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
