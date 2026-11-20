"""Integrate reviewed outline, certificate and scoped boundary-prism passages."""
from pathlib import Path
import datetime, hashlib, json, re

R=Path(__file__).resolve().parents[1]
paths=['audit_sign/frontmatter_II.tex','audit_sign/frontmatter_II_map.json',
       'parts/II.body.linked.tex','parts/III.body.linked.tex','parts/V.body.linked.tex']
before={p:(R/p).read_text() for p in paths}
after=dict(before);receipts=[]
for file,target in [('audit_sign/II_main_outline_guards_07.json','audit_sign/frontmatter_II.tex'),
                    ('audit_sign/UN36_current_certificate_guard_08.json','parts/II.body.linked.tex'),
                    ('audit_corrections/V_P1A2_word_guard_07.json','parts/V.body.linked.tex')]:
    packet=json.loads((R/file).read_text());guards=packet['guards'] if isinstance(packet,dict) else packet
    for g in guards:
        assert after[target].count(g['old_text'])==1,(file,g['label'])
        after[target]=after[target].replace(g['old_text'],g['new_text'],1)
    receipts.append({'source':file,'source_sha256':hashlib.sha256((R/file).read_bytes()).hexdigest(),'target':target,'guards':guards})
    if 'map_updates' in packet:
        mapping=json.loads(after['audit_sign/frontmatter_II_map.json'])
        for g in packet['map_updates']:
            main=next(t for t in mapping['main_theorems'] if t['letter']==g['letter'])
            step=next(t for t in main['steps'] if t['number']==g['step'])
            assert step['claim_tex']==g['old_claim_tex']
            step['claim_tex']=g['new_claim_tex']
        after['audit_sign/frontmatter_II_map.json']=json.dumps(mapping,indent=2,ensure_ascii=False)+'\n'

old=r'''The refined class remains a separate \(0\) versus \(4\)
calculation until the actual odd middle-dimensional generator
and its reference framing have been evaluated.
'''
new=r'''The boundary class that enters this remaining calculation has an
explicit integral prism description. Put \(\alpha=e_1\wedge\delta\)
and retain \(A_0\) from \eqref{maps:eq:D.PC5}. At the first finite
\(I_1\) site the actual marked matrix is \(A_1=I+E_{12}\).
Direct exterior multiplication gives
\[
 (\wedge^2A_0-I)(e_1\wedge e_2+e_2\wedge\delta)=2\alpha,
 \qquad
 (\wedge^2A_1-I)(e_2\wedge\delta)=\alpha.
\]
In the ordered six-cell basis above, every entry of
\(\wedge^2A_0-I\) is even. The row
\((0,1,0,0,0,0)\bmod2\) kills its image and evaluates to one on
\(\alpha\); hence \(\alpha\) has exact order two in the cusp
fibre coinvariant group and in its injected term of the integral
mapping-torus sequence. In the actual full core matrix, its
exterior null witness is column9, and the positive-cap
fixed-exterior relation is column36 with coefficient minus one
(the saved arrays use zero-based indices).
These are the two explicit images of the same marked class.
The program \path{code/III_OS45_boundary_prisms_07.py} computes
both exterior maps, the detector and these complete core columns.
Its output \path{code/outputs/III_OS45_boundary_prisms_07.json}
also gives the exact integral Smith maps for the cusp exterior
and the \(23\)-by-\(55\) exterior relation matrix.
The refined class remains \(0\) versus \(4\) until the embedded
glued odd three-cycle, its reference framing and its linking with
the critical specialization have been evaluated.
'''
target='parts/III.body.linked.tex'
assert after[target].count(old)==1
after[target]=after[target].replace(old,new,1)
receipts.append({'target':target,'label':'maps:src:D.2.53','old_text':old,'new_text':new,
 'reason':'Print the completed21-check exact boundary-prism calculation with its actual matrices and scoped remaining framing gate. No refined-class value or embedded-cycle construction is claimed.'})
for p,s in after.items():
    if p.endswith('.tex'):
        assert re.findall(r'\\(?:label|tag)\{[^}]+\}',before[p])==re.findall(r'\\(?:label|tag)\{[^}]+\}',s),p
    (R/p).write_text(s)
receipt={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'receipts':receipts,
 'hashes':{p:{'before':hashlib.sha256(before[p].encode()).hexdigest(),'after':hashlib.sha256(after[p].encode()).hexdigest()} for p in paths},
 'pending':'Assembly, build28, log audit and actual changed-page inspection.'}
(R/'analysis/received_guards_integration_08.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'files_changed':paths,'received_guard_count':4,'III_scoped_prism_passage':1}))
