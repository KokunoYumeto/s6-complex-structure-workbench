#!/usr/bin/env python3
"""Record the exact normal-clutch calculation and its comparison scope."""
from pathlib import Path
import json

directory=Path(__file__).resolve().parent
path=directory/'results_mapping.json'
data=json.loads(path.read_text())
data['results']=[row for row in data['results'] if row['id']!='P3K.9']
data['results'].append({
    'id':'P3K.9',
    'status':'Proved',
    'value':'The rotating normal clutch has Pontryagin number zero; its exact sixfold descent has original Jin (k,ell)=(-1,-4).',
    'one_gamma_turn':{'k':-6,'ell':-24},
    'parameter_cover_degree':6,
    'original_return':{'k':-1,'ell':-4},
    'framing':'Descended rotating framing, constructed explicitly from the Z/2 plus Z gauge-space covering map.',
    'ambiguity':'Other tubular framings add n*(1,4).',
    'item_of_prompt':'3.3',
    'agrees_with_prompt_stated_values':True,
    'code':'code/part3_fourfold/normal_clutch.py',
    'output':'code/part3_fourfold/normal_clutch.json'
})
for row in data['results']:
    if row['id']=='P3K.7':
        row['orientation']='Physical positive family is Jin M_(f^(-1)); the complement boundary is -P_f and -B, so Jin(f)=B.'
    if row['id']=='P3K.8':
        row['symbol_comparison']='Invariant round-sphere vertical Dirac kernel is the trivial constants line; the orthogonal complement is invertible in the explicit operator decomposition.'
        row['base_change']='Stacks Project Lemma 30.22.1, tag 07VK, verified.'
path.write_text(json.dumps(data,indent=2)+'\n')
print('Recorded P3K.9 and the exact orientation/operator comparisons for P3K.7--8.')
