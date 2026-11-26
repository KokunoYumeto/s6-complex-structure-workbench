"""Extract eight current Paper II editorial contexts without canonical writes."""
from pathlib import Path
import datetime
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_D09_D04_batch07_working'
OUT.mkdir(exist_ok=True)
source = (ROOT / 'S6_SERIES_PUBLISH_II.tex').read_text()
sha = lambda s: hashlib.sha256(s.encode()).hexdigest()
owners = {
 '01DO': 'cdp:st:C.2.UN.44',
 '01CD': 'cdp:st:C.2.RAT.1',
 '01CO': 'cdp:st:C.2.UN.11',
 '01DB': 'cdp:st:C.2.UN.32',
 '01EA': 'cdp:st:C.2.UN.64',
 '01EC': 'cdp:st:C.2.UN.66',
 '01E5': 'cdp:st:C.2.UN.6',
 '01ER': 'cdp:st:C.2.UN.8',
}
env = re.compile(r'\\begin\{(?:proposition|lemma|theorem|corollary|definition|remark)\}')
rows = []
for tag, owner in owners.items():
    token = '\\label{' + owner + '}'
    assert source.count(token) == 1, (owner, source.count(token))
    at = source.index(token)
    start = list(env.finditer(source, 0, at))[-1].start()
    end = source.index('\\end{proof}', at) + len('\\end{proof}')
    next_env = env.search(source, end)
    assert next_env
    body = source[start:end]
    following = source[end:next_env.start()]
    assert '\\hypertarget{tag-' + tag + '}' in body
    for suffix, contents in [('before',body),('following_before',following)]:
        f = OUT / f'S6_SERIES_PUBLISH_II_A2_{tag}_{suffix}.tex'
        assert not f.exists(), f
        f.write_text(contents)
    rows.append(dict(tag=tag, owner=owner, source_character_span=[start,end],
                     source_line=source.count('\n',0,start)+1,
                     bytes=len(body.encode()), sha256=sha(body),
                     following_bytes=len(following.encode()), following_sha256=sha(following),
                     labels=re.findall(r'\\label\{([^}]+)\}',body),
                     program_mentions=re.findall(r'(?:\\path|\\nolinkurl)\{([^}]+)\}',body+following)))
record=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
            source_sha256=sha(source),owners=rows,canonical_mutations=0)
(OUT/'S6_SERIES_PUBLISH_II_A2_batch07_extraction.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
