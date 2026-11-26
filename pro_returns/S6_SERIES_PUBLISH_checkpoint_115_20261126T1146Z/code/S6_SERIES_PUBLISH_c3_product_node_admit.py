"""Admit the full-scope product-node proof and common finite intersection owner."""
from S6_SERIES_PUBLISH_c3_edit import *
import json

folder=ROOT/'agents/continuation3_foundations/sec07'
prefix='S6_SERIES_PUBLISH_sec07_product_node_'
guards=json.loads((folder/(prefix+'guards.json')).read_text())
assert len(guards)==4
before=SOURCE.read_text();after=before
for row in guards:
    assert after.count(row['old'])==1,row['key']
    preserve_identifiers(row['old'],row['new'])
    after=after.replace(row['old'],row['new'],1)
    print('Applied',row['key'])
preserve_identifiers(before,after)
for old,new in zip(identifiers(before),identifiers(after)):
    for name,count in old.items():assert new[name]==count,name
    for name,count in (new-old).items():assert new[name]==1,name
SOURCE.write_text(after,newline='\n')
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
    _,rows=read_tsv(folder/(prefix+suffix));print(suffix,append_rows(ROOT/target,rows,key))
add_event('lem:II:smooth-curve-intersection; cdp:st:C.2.UN.9; night:P4R.14',
 'II-C3-ROOT-PRODUCT-NODE-ADMISSION','used and rechecked in this run',
 'Root read every old/new exact guard, the complete P299/UN9 receiving text and comparison. P299 uses finite complete-intersection algebra over C{z}, its free rank and special-fibre length, giving the exact invertible coordinate maps at ranks one and two. R14 uses the identical factors and z with rank two; its complete weighted full-function proof is preserved. The reducible UN9 case uses rank one and the inverse of X=V phi, allowing all original positive component multiplicities. The locally irreducible case first establishes F=(U^(1/M)f)^M. Root checked the full original symmetric-matrix perturbation, the nonzero adjugate trace, the exact X^2+y^2Z coordinates, the spherical square -4 and the fixed-boundary P295 transport into F=b^M. All old hypotheses, conclusions, formula payloads and permanent targets are retained. The UN9 full-multiplicity proof premise is resolved. No entire surrounding-unit closure, independent proof credit or final-page credit is inferred.',
 'S6_SERIES_PUBLISH_II.tex: finite intersection and product-node owners',source=__file__)
print('UN9 full-scope proof admitted; surrounding unit remains under review.')
