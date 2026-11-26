from S6_SERIES_PUBLISH_c3_foundations_sec07_helpers import *
from collections import Counter

s=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text();before=s
dependent=False
if r'\label{lem:II:cubic-spectral-genus}' not in s:
    dependent=True
    for g in json.loads((OUT/'S6_SERIES_PUBLISH_sec07_two_junctions_guards.json').read_text()):
        assert s.count(g['old'])==1,(g['key'],s.count(g['old']))
        s=s.replace(g['old'],g['new'])
for g in json.loads((OUT/'S6_SERIES_PUBLISH_sec07_three_junction_guards.json').read_text()):
    assert s.count(g['old'])==1,(g['key'],s.count(g['old']))
    s=s.replace(g['old'],g['new'])
for pattern in [r'\\label\{([^{}]+)\}',r'\\hypertarget\{([^{}]+)\}']:
    oldc=Counter(re.findall(pattern,before));newc=Counter(re.findall(pattern,s))
    for key,value in oldc.items():assert newc[key]==value,(key,value,newc[key])
print('R20 complete-subsection guard matches once '+
      ('after the four exact P323 prerequisite guards' if dependent else 'on the admitted current source')+
      '; every old label and target has unchanged multiplicity. No shared write.')
