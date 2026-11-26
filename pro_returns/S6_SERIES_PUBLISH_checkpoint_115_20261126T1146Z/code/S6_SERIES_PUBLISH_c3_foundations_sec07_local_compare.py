from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation3_foundations/sec07'
source=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
guards=json.loads((OUT/'S6_SERIES_PUBLISH_sec07_local_guards.json').read_text())
receiving=source
for guard in guards:
    count=receiving.count(guard['old'])
    assert count==1,(guard['key'],count)
    receiving=receiving.replace(guard['old'],guard['new'],1)
for pattern in (r'\\label\{([^{}]+)\}',r'\\hypertarget\{([^{}]+)\}'):
    before=re.findall(pattern,source)
    after=re.findall(pattern,receiving)
    for identity in set(before):
        assert before.count(identity)==after.count(identity),(identity,before.count(identity),after.count(identity))
print('All 11 exact guards match once. Every pre-existing label and permanent target has unchanged multiplicity. No shared file written.')
for key in sys.argv[1:]:
    p=receiving.index(r'\label{'+key+'}')
    a=receiving.rfind(r'\begin{',0,p)
    b=receiving.index(r'\end{proof}',p)+len(r'\end{proof}')
    print(receiving[a:b])
