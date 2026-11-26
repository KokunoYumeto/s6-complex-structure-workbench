#!/usr/bin/env python3
"""Two exact guards for the same suspension-branch shear in 02L8."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import difflib
import json
import re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation9_findings'
stem='S6_SERIES_PUBLISH_c9_current02_02L8_branch_retention'
source=(ROOT/'S6_SERIES_PUBLISH_III.tex').read_text()
old1=r'''The line bundle keeps the Chern class \(C_p^*-C_0^*\). An integral branch change of the
suspension logarithm acts by
\((t_\delta,t_\gamma)\mapsto(t_\delta+k t_\gamma,t_\gamma)\),
with inverse \(-k\); the complete fixed-sweep kernel below is
unchanged by this displayed map.'''
new1=old1.replace('+k t_',r'+k_{\rm br} t_').replace(r'\(-k\)',r'\(-k_{\rm br}\)')
old2=r'''The possible suspension branch change by \(k_0\delta\) replaces
\(\ell\) by \(\ell+k_0\delta\). It replaces one fixed sweep by
that sweep plus \(k_0\) times the other. The inverse subtraction
preserves their entire kernel. It also leaves the first area
row in the fibre quotient map unchanged; the class of
\(\beta_0\wedge\delta\) in the fibre quotient is zero, as the fibre quotient map
checks. Hence the primitive class \(k\) and \eqref{maps:eq:D.OC1} are unaffected.
This proves the needed independence from the actual logarithm
branch by its explicit coordinate morphism.'''
new2=old2.replace('k_0',r'k_{\rm br}')
assert old2.count('k_0')==3
reasons=[
    'Name the integer suspension-branch coefficient k_br in the actual shear and its inverse, preserving k for the primitive wedge class beta_0 wedge ell. The map on the marked lattice is the same I+k_br delta gamma^*, with inverse I-k_br delta gamma^*. Every coordinate, sign and Chern class is unchanged.',
    'Use the same branch-family parameter k_br in the later fixed-period comparison. The shear sends ell to ell+k_br delta and fixes beta_0 and delta, so its exterior square changes k only by k_br beta_0 wedge delta, which has zero displayed quotient coordinates. The normal-sweep change and inverse subtraction are the original maps. The three removed zero digits belonged only to the old variable index k_0; no numerical coefficient, coordinate or parameter value changes.'
]
rows=[]
for i,(old,new,reason) in enumerate(zip([old1,old2],[new1,new2],reasons),1):
    assert source.count(old)==1
    rows.append(dict(change_id=f'CLAUDE-III-P15-current02-02L8-branch-{i:03}',
                     type='D20',statement_id='maps:src:D.2.32',
                     old_location=f'Paper III, tag02L8; branch-shear paragraph {i}',
                     old_page='candidate02 315--322; Theorem 12.8',
                     new_location='same proof, same branch shear and fixed-period comparison',
                     new_page='pending changed rendering',old_text=old,new_text=new,
                     reason=reason,
                     review_status='Used and rechecked in this run after exposure. Reread the complete current neighbourhood/roof, primitive fibre-image and full normal/fibre-kernel arguments, including both branch paragraphs and all quotient/section formulas. Earlier complete 02L8 proof and actual image evidence retained. Both exact differences read; scoped assignments, full-source reversal, labels and targets passed. All numerical literals outside the three renamed k_0 index digits are identical in order. No independent proof or new image credit. Admission and changed rendering pending.'))
full=source
for row in rows:
    assert full.count(row['old_text'])==1
    full=full.replace(row['old_text'],row['new_text'],1)
for pattern in [r'\\label\{[^}]+\}',r'\\hypertarget\{[^}]+\}']:
    assert re.findall(pattern,full)==re.findall(pattern,source)
number_reference=source.replace(old2,old2.replace('k_0','k'),1)
assert re.findall(r'\d+',full)==re.findall(r'\d+',number_reference)
assert full.count(r'k=\beta_0\wedge\ell')==source.count(r'k=\beta_0\wedge\ell')
for row in reversed(rows):
    assert full.count(row['new_text'])==1
    full=full.replace(row['new_text'],row['old_text'],1)
assert full==source
(OUT/(stem+'.json')).write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
with (OUT/(stem+'_defects.tsv')).open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t',lineterminator='\n')
    w.writeheader();w.writerows(rows)
with (OUT/(stem+'.diff')).open('w') as f:
    for i,row in enumerate(rows,1):
        f.write(''.join(difflib.unified_diff((row['old_text']+'\n').splitlines(True),(row['new_text']+'\n').splitlines(True),fromfile=f'02L8 branch {i} before',tofile=f'02L8 branch {i} proposed'))+'\n')
event_id='ce:c9-iii-current02-02l8-branch-retention'
event=dict(statement_id='maps:src:D.2.32',date='2026-11-26',
           who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode',
           type='used and rechecked in this run',
           outcome='Reconciled the concrete retained branch coefficient against the actual admitted 02L8 source. Read the complete current neighbourhood/roof, primitive fibre-image and full normal/fibre-kernel arguments; compared both exact source fragments. Verified the lattice shear I+k_br delta gamma^*, its inverse, its action on ell and beta_0, the exterior-square correction with zero quotient coordinates, and the fixed-sweep inverse. Full-source reversal, labels/targets and all numeric literals except the three explicitly renamed k_0 index digits passed. Earlier full-proof/image evidence retained; no independent proof or new image credit. Admission and changed rendering pending.',
           event_id=event_id,phase='publication continuation 9',
           source_file='agents/continuation9_findings/'+stem+'_review.md',
           source_row='complete current affected proof parts 2--4 and both final differences',
           source_event_type='used and rechecked in this run',evidence_group=event_id,
           publish_input_file='agents/continuation9_findings/'+stem+'_defects.tsv',
           publish_input_row='both guarded fragments',
           date_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
           where='Paper III, tag02L8 / maps:src:D.2.32; the logarithm branch shear and its fixed-period/kernel comparison')
with (OUT/(stem+'_CHECK_EVENTS.tsv')).open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(event),delimiter='\t',lineterminator='\n')
    w.writeheader();w.writerow(event)
print('02L8 branch: two exact guarded fragments; complete-source forward/reverse comparison passed.')
print('Labels/targets preserved. Every numerical literal is preserved except three zero digits in the renamed k_0 variable index.')
print('The primitive class k=beta_0 wedge ell and all other source text are unchanged; canonical source not written.')
