#!/usr/bin/env python3
"""Archive bounded page-reading residues without changing the paper or events."""
from pathlib import Path
import datetime
import hashlib
import json
from S6_SERIES_PUBLISH_editing import block

R = Path(__file__).resolve().parents[1]
OUT = R / 'records/S6_SERIES_PUBLISH_I_candidate13_root_residue'
OUT.mkdir(exist_ok=True)
sha = lambda x: hashlib.sha256(x).hexdigest()
source = (R/'S6_SERIES_PUBLISH_I.tex').read_text()
expected = '26a6f5f8b1e911de363bed7346e970bc8fb77b21cf04fe9a2ce4d1f90d95b49e'
assert sha(source.encode()) == expected
baseline = (R.parent/'source/S6_SERIES_GRIND_I.tex').read_text()
guards = [
    {'statement_id':'fam:src:B.2.1', 'page':53, 'defect':'D02',
     'old':r'There is no condition on $k_1$.',
     'new':r'The integer $k_1$ is arbitrary.',
     'reason':'State the parameter freedom positively. The exact arithmetic conditions and every construction map remain byte-identical. The comparison of parameter sets is the identity on the integer k_1 coordinate and on every other displayed datum; no restriction is added or removed.'},
    {'statement_id':'inv:A2.2', 'page':84, 'defect':'D23',
     'old':r'$j(\tau)=-512i\pi^3E_6(\rho)(\tau-\rho)^3+cdots$.',
     'new':r'$j(\tau)=-512i\pi^3E_6(\rho)(\tau-\rho)^3+\cdots$.',
     'reason':'The rendered page prints the literal letters cdots after the cubic Taylor term. Restore the missing TeX command backslash for the ellipsis, retaining the complete coefficient, variable, exponent, branch and all subsequent calculations. The same missing backslash is present in the attached baseline.'},
]
for index,g in enumerate(guards,1):
    current = block(source,g['statement_id'])
    original = block(baseline,g['statement_id'])
    assert current.count(g['old']) == 1
    replacement = current.replace(g['old'],g['new'],1)
    assert replacement.count(g['new']) == 1
    assert replacement.replace(g['new'],g['old'],1) == current
    assert current.split(r'\begin{proof}',1)[0] == replacement.split(r'\begin{proof}',1)[0]
    base = f'S6_SERIES_PUBLISH_I_candidate13_root_residue_{index:02d}'
    files={}
    for name,value in [('original',original),('current',current),('replacement',replacement)]:
        path=OUT/(base+'_'+name+'_full_block.tex')
        path.write_text(value)
        files[name]={'path':str(path.relative_to(R)),'sha256':sha(path.read_bytes()),'characters':len(value)}
    g['archive']=files
    g['statement_bytes_identical']=True
    g['exact_inverse_restores_current_full_block']=True
    g['all_other_proof_bytes_identical']=True
record={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'source_sha256':expected,'pdf_sha256':'519355e39d7d821a10d728d5c8dbf69a50826ee215ab98619803d44e1cae2a2b',
        'guards':guards,'check_events_added':0,
        'scope':'Current complete pages52-54 and84-85 actually read. Exact current complete source blocks read. Full replacement blocks require root reading before application; no independent derivation is claimed.',
        'replacement_full_blocks_read':False}
path=R/'records/S6_SERIES_PUBLISH_I_candidate13_root_residue_guards.json'
path.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'record':str(path.relative_to(R)),'guards':len(guards),'source_unchanged':sha((R/'S6_SERIES_PUBLISH_I.tex').read_bytes())==expected}))
