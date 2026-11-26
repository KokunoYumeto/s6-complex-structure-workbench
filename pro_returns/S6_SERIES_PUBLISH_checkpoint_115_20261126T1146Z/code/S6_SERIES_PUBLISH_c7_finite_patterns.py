#!/usr/bin/env python3
"""Complete fresh finite-pattern extension and exact scope comparison.

All inputs are new derivations from this continuation or the admitted
raw period definitions. No L4/L6 original, old program or old table.
"""
from pathlib import Path
from itertools import product, combinations
from collections import Counter
from math import gcd
import json

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation7_iii_finite_general'
raw=json.loads((ROOT/'agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json').read_text())['rows']
profiles={(r['OS'],r['profile']):r for r in raw}
initial=json.loads((ROOT/'agents/continuation7_iii_root/S6_SERIES_PUBLISH_III_02KX_fresh_candidate_data.json').read_text())['natural']
positions=json.loads((OUT/'S6_SERIES_PUBLISH_III_finite_fresh_lattices.json').read_text())['positions']
prior_data=json.loads((ROOT/'agents/continuation7_iii_nonstar/S6_SERIES_PUBLISH_III_02L1_fresh_catalogue.json').read_text())
prior_fresh=prior_data['minimal_patterns']


def rowkey(row):
    return (row['OS'],row['profile'],row['a'],row['b'],row['zero_index'])


def patternkey(p):
    return rowkey(p)+(tuple(p['finite_indices']),tuple(p['original_additive_indices']))


grouped={}
for pos in positions:grouped.setdefault(rowkey(pos),[]).append(pos)
counts=Counter()
for pos in positions:
    star=pos['OS'] in (46,50)
    counts['all_g1' if pos['g']==1 else 'all_gq']+=1
    if not star:counts['nonstar_g1' if pos['g']==1 else 'nonstar_gq']+=1
    else:print('ODD_STAR_LOCAL_POSITION',rowkey(pos),pos['finite_index'],pos['kind'],'g',pos['g'])
assert dict(counts)=={'all_g1':68,'all_gq':34,'nonstar_g1':62,'nonstar_gq':32}
print('EXACT_FINITE_SCOPE',dict(counts))

boundary_count=0
for row in prior_data['natural']:
    if not row['nonstar']:continue
    for T in row['T']:
        A=[[T[i][j]-int(i==j) for j in range(4)] for i in range(4)]
        first=gcd(*(x for r in A for x in r))
        second=gcd(*(A[i][k]*A[j][l]-A[i][l]*A[j][k]
                     for i,j in combinations(range(4),2)
                     for k,l in combinations(range(4),2)))
        assert first==1 and second in (0,1)
        # The local Jordan/finite calculations give rank one or two.
        # These primitive minors prove the full coinvariant has no torsion.
        boundary_count+=1
print('PRIMITIVE_BOUNDARY_H1_MATRICES',boundary_count,'PASS')

patterns=[]
for row in initial:
    prof=profiles[row['OS'],row['profile']]
    if any(t in ('I1*','I3*') for t in prof['fibers']):continue
    local=grouped.get(rowkey(row),[])
    choices=[]
    for p in local:
        options=['finite']
        if p['kind'] in ('II','III','IV') and row['a']%p['q']==0 and gcd(row['b'],p['q'])==1:
            options.append('original')
        choices.append(options)
    for modes in product(*choices):
        p={k:row[k] for k in ('OS','profile','a','b','zero_index')}
        p['finite_indices']=[x['finite_index'] for x,mode in zip(local,modes) if mode=='finite']
        p['original_additive_indices']=[x['finite_index'] for x,mode in zip(local,modes) if mode=='original']
        p['finite_lattices']=[{k:x[k] for k in ('finite_index','kind','order','q','g','qv')}
                              for x,mode in zip(local,modes) if mode=='finite']
        p['all_finite_gamma_primitive']=all(x['g']==1 for x in p['finite_lattices'])
        patterns.append(p)
oldkeys={patternkey(p) for p in prior_fresh}
newkeys={patternkey(p) for p in patterns}
primitivekeys={patternkey(p) for p in patterns if p['all_finite_gamma_primitive']}
assert len(patterns)==len(newkeys)==198
assert primitivekeys==oldkeys and len(oldkeys)==164
extras=[p for p in patterns if patternkey(p) not in oldkeys]
assert len(extras)==34
assert len({rowkey(p) for p in patterns})==148
profile_counts=Counter((p['OS'],p['profile']) for p in patterns)
for key,num in profile_counts.items():print('PROFILE_PATTERNS',*key,num)
for i,p in enumerate(patterns,1):
    print('PATTERN',i,*rowkey(p),'FINITE',p['finite_indices'],
          'ORIGINAL',p['original_additive_indices'],
          'GAMMA_INDICES',[x['g'] for x in p['finite_lattices']])
(OUT/'S6_SERIES_PUBLISH_III_finite_fresh_patterns.json').write_text(
    json.dumps({'scope':'Fresh complete nonstar pattern list, with exact primitive-gamma inclusion.',
                'finite_position_counts':dict(counts),'patterns':patterns,
                'primitive_pattern_count':164,'additional_pattern_count':34},indent=2)+'\n',newline='\n')
print('PASS exact inclusion of the 164 independently derived primitive-gamma patterns;')
print('PASS 34 additional patterns, 198 total, on exactly 148 initial rows;')
print('PASS 102 total finite positions split into 94 nonstar and 8 odd-star positions.')
