"""Admit the fully compared tacnode proof at its original multiplicity domain."""
from S6_SERIES_PUBLISH_c3_edit import *
import json
import subprocess
import sys

folder=ROOT/'agents/continuation3_foundations/sec07'
prefix='S6_SERIES_PUBLISH_sec07_tacnode_'
guards=json.loads((folder/(prefix+'guards.json')).read_text())
assert len(guards)==1
before=SOURCE.read_text();after=before
def statement_payload(text):
    text=text[text.index('Let $S$'):text.index(r'\end{proposition}')]
    text=re.sub(r'\\(?:tag|label)\{[^}]+\}','',text)
    text=text.replace(r'\begin{equation}','').replace(r'\end{equation}','')
    text=text.replace(r'\[','').replace(r'\]','')
    return re.sub(r'\s+','',text)
for row in guards:
    assert after.count(row['old'])==1,row['key']
    assert statement_payload(row['old'])==statement_payload(row['new'])
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
add_event('night:P4R.14','II-C3-ROOT-TACNODE-ADMISSION','used and rechecked in this run',
 'Root read the entire original and receiving R14 statements and proofs and the full comparison. The statement payload is unchanged after removal only of equation-numbering wrappers. The locally irreducible discriminant argument uses the exact full-function root. The reducible intersection algebra is finite free of rank two over the axis, forcing a smooth factor and unit discriminant without moving either factor. The graph root and parameter Morse maps retain the original reduced generator. Absorbing U^(1/b) into the second factor gives the exact full function X^a(Y^2+XK)^b and K(0,z)=U(0,0,z)^(1/b)H(0,z). Root directly checked the branch-chain identity, positive coefficients N+bj/r, finite-map equations, nonzero critical value, full logarithmic Hessian determinant and its a=b=1 specialization. The boundary chart T=XK_s, its implicit inverse and weighted unit map give the full fixed transverse polynomial, so P295 applies with m=1. The complete positive-genus example and six-root computation remain; the agent symbolic recheck has exposed credit only. R14 full-multiplicity gate is resolved; P4.41 and P4.45 remain open. No independent or final-page credit.',
 'S6_SERIES_PUBLISH_II.tex: smooth critical curve of transverse type A3',
 source='agents/continuation3_foundations/sec07/S6_SERIES_PUBLISH_sec07_tacnode_comparison.md')
data=dict(unit='night:P4R.14',event_id='II-C3-ROOT-SMOOTH-TACNODE-UNIT-READ',
 complete_original_and_receiving_read=True,
 outcome='Complete original and receiving R14 unit read against all local defect classes and compared. Every old mathematical formula and normalization conclusion remains, with the five labelled equations now in section numbering. The exact full-function factor and multiplicity proof closes the newly discovered D25 premise at the unchanged original domain. All identified local instances are logged. D14/D23 and final whole-paper placement remain open; P4.41/P4.45 receive no closure. No independent credit.',
 unit_detail='Full unequal-multiplicity tacnode deformation proved through explicit factor, coordinate, Hessian and boundary maps.')
subprocess.run([sys.executable,str(ROOT/'code/S6_SERIES_PUBLISH_c3_read_unit.py')],input=json.dumps(data),text=True,check=True)
print('Admitted R14 full-multiplicity proof; two local deformation gates remain open.')
