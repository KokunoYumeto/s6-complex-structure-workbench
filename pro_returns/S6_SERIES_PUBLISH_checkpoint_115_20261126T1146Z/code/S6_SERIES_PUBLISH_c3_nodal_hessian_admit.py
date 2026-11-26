"""Admit the complete nodal-Hessian multiplicity repair; retain unit gates."""
from S6_SERIES_PUBLISH_c3_edit import *
import json

folder=ROOT/'agents/continuation3_foundations/sec07'
prefix='S6_SERIES_PUBLISH_sec07_nodal_hessian_'
guards=json.loads((folder/(prefix+'guards.json')).read_text());assert len(guards)==1
before=SOURCE.read_text();after=before
def payload(text):
    text=text[text.index('At a point of a support'):text.index(r'\end{proposition}')]
    text=re.sub(r'\\(?:tag|label)\{[^}]+\}','',text)
    for a in [r'\begin{equation}',r'\end{equation}',r'\[',r'\]']:text=text.replace(a,'')
    return re.sub(r'\s+','',text)
for row in guards:
    assert after.count(row['old'])==1,row['key']
    assert payload(row['old'])==payload(row['new'])
    for equation in re.findall(r'\\begin\{equation\}(.*?)\\end\{equation\}',row['new'],re.S):
        assert not re.search(r'\n[ \t]*\n',equation)
    after=after.replace(row['old'],row['new'],1)
    print('Applied',row['key'])
preserve_identifiers(before,after)
for old,new in zip(identifiers(before),identifiers(after)):
    for name,count in old.items():assert new[name]==count,name
    for name,count in (new-old).items():assert new[name]==1,name
SOURCE.write_text(after,newline='\n')
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),
                         ('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
    _,rows=read_tsv(folder/(prefix+suffix))
    print(suffix,append_rows(ROOT/target,rows,key))
add_event('night:P4.41','II-C3-ROOT-NODAL-HESSIAN-ADMISSION','used and rechecked in this run',
 'Root read every line of the original and receiving P4.41 statement and proof and the full comparison. Its statement payload is identical after removal only of equation-numbering wrappers. The nonzero ambient Hessian case applies the already repaired R15 to the original full function. In the remaining case, root checked the conductor multiplier syzygy giving normalization R+R(G/z^2), its one-point fibre for D(0)=0 and its exact two-factor split for D(0) nonzero. The common-root case keeps the original epsilon^2 critical value and all Hessian entries through the displayed invertible maps. The unequal-power case retains U,a,b; root checked the rescaled logarithmic-gradient limit, its unique zero, determinant 2N^2T and exact HessF=(F/epsilon)D_rL. Both nested full boundary comparisons use P295 with the correct root power or m=1. All original q=0 inequalities, ring-condition matrices, ideal coordinate changes and finite birational equality-normalization maps remain. The agent additionally read complete current P222/R10 inputs. P4.41 full-multiplicity gate is resolved. P4.45 remains open, and no whole-unit closure is inferred before its P4.42 companion comparison is admitted. No independent or final-page credit.',
 'S6_SERIES_PUBLISH_II.tex: nodal critical curve and Hessian defect',
 source='agents/continuation3_foundations/sec07/S6_SERIES_PUBLISH_sec07_nodal_hessian_comparison.md')
print('P4.41 full-multiplicity premise resolved; P4.45 remains open.')
