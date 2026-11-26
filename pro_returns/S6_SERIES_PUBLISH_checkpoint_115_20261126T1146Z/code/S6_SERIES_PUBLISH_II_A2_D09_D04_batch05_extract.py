"""Extract six exact Paper II owner blocks and their following material."""
from pathlib import Path
import datetime,hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_D09_D04_batch05_working'
OUT.mkdir(exist_ok=True)
s=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
sha=lambda t:hashlib.sha256(t.encode()).hexdigest()
owners={'02YF':'night:P4R.3','02YC':'night:P4R.19','02YE':'night:P4R.20',
        '02WI':'night:P4.11','033O':'push:src:E.5.2','033P':'push:src:E.5.3'}
env=re.compile(r'\\begin\{(?:proposition|lemma|theorem|corollary|definition|remark)\}')
rows=[]
for tag,owner in owners.items():
    token='\\label{'+owner+'}'
    assert s.count(token)==1
    k=s.index(token)
    start=list(env.finditer(s,0,k))[-1].start()
    end=s.index('\\end{proof}',k)+len('\\end{proof}')
    n=env.search(s,end);assert n
    following=s[end:n.start()]
    body=s[start:end]
    assert '\\hypertarget{tag-'+tag+'}' in body
    for suffix,text in [('before',body),('following_before',following)]:
        p=OUT/f'S6_SERIES_PUBLISH_II_A2_{tag}_{suffix}.tex'
        assert not p.exists(),p
        p.write_text(text)
    rows.append(dict(tag=tag,owner=owner,source_character_span=[start,end],
                     source_line=s.count('\n',0,start)+1,bytes=len(body.encode()),sha256=sha(body),
                     following_bytes=len(following.encode()),following_sha256=sha(following)))
record=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
            source_sha256=sha(s),owners=rows,canonical_mutations=0)
(OUT/'S6_SERIES_PUBLISH_II_A2_batch05_extraction.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
