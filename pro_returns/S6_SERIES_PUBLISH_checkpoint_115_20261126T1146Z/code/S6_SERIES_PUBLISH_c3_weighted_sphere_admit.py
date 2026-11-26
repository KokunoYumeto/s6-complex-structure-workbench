"""Admit the exact weighted full-fibre model; keep deformation consumers open."""
from S6_SERIES_PUBLISH_c3_edit import *
import json

folder=ROOT/'agents/continuation3_foundations/sec07'
guards=json.loads((folder/'S6_SERIES_PUBLISH_sec07_weighted_sphere_guards.json').read_text())
before=SOURCE.read_text();after=before
for row in guards:
    assert after.count(row['old'])==1,row['key']
    after=after.replace(row['old'],row['new'],1)
    print('Applied',row['key'])
preserve_identifiers(before,after)
for old,new in zip(identifiers(before),identifiers(after)):
    for name,count in old.items():assert new[name]==count,name
SOURCE.write_text(after,newline='\n')
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),
                         ('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
    _,rows=read_tsv(folder/('S6_SERIES_PUBLISH_sec07_weighted_sphere_'+suffix))
    print(suffix,append_rows(ROOT/target,rows,key))
add_event('lem:II:monomial-curve-matching-sphere; prop:II:weighted-two-branch-sphere; cdp:st:A.5.15; lem:II:conic-bundle-matching-sphere',
 'II-C3-ROOT-WEIGHTED-SPHERE-ADMISSION','used and rechecked in this run',
 'Root read the complete 148-line receiving P297/P296, the complete old A.5.15 matching construction and P247 proof, every bounded old/new guard, and the complete comparison/status record. The Bezout inverse is checked on both nonzero factors, including Y=Z=0. The cyclic root curve is smooth and connected, v has N simple zeros, and the coordinate identity gives the precise coprime monomial surface. The general arc/framing construction retains compact homotopies and square -2(k/e)(l/e), while the embedded k/e=l/e=1 clause retains the endpoint disks and negative determinant. The weighted unit map and implicit inverse carry the full original multiplicities. Five guards replay once and every old label/target multiplicity is preserved. The four broad rigidity consumers still require factor-preserving deformation and boundary comparison; their D25 gate remains open. No enclosing-unit closure, independent proof or final-page credit is claimed.',
 'S6_SERIES_PUBLISH_II.tex: common matching-sphere owner and weighted two-branch full fibre',
 source='agents/continuation3_foundations/sec07/S6_SERIES_PUBLISH_sec07_weighted_sphere_comparison.md')
print('Weighted model admitted; four factor-preserving deformation gates remain open.')
