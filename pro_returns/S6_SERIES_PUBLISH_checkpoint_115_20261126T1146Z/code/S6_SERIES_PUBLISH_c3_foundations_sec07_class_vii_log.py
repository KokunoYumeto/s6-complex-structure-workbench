from S6_SERIES_PUBLISH_c3_foundations_sec07_helpers import *
from datetime import datetime,timezone

prefix='S6_SERIES_PUBLISH_sec07_class_vii'
path=OUT/(prefix+'_defects.tsv')
with path.open(newline='') as f:
    r=csv.DictReader(f,delimiter='\t');fields=r.fieldnames;rows=list(r)
for row in rows:row['review_status']='Complete original and receiving proofs read and compared; precise source and consumer maps checked; root admission pending.'
with path.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
with (ROOT/'agents/continuation3_foundations/S6_SERIES_PUBLISH_foundations_CHECK_EVENTS.tsv').open(newline='') as f:
    event_fields=next(csv.reader(f,delimiter='\t'))
now=datetime.now(timezone.utc).isoformat()
events=[]
data=[
 ('vii1','cdp:st:C.2.VII.1','Read complete original VII.1 and current P4.23 proofs, the complete expanded early VII.1 proof, and the complete receiving P4.23 proof. Match Z=T, Z0=T0, σ=β, D0=β*D and L=O(K+D0); preserve m=1 and F=L^−1 as the NAC datum. Move all minimal-model alternatives, the reduced Inoue–Hirzebruch coefficient comparison, parabolic D0=E+C, C²=0, C numerically trivial, E²=−b2 and exact rational-curve counts to one earlier owner. Keep torsion descent, every blowup support/genus/count conclusion, and the complete later P4.23 normal-crossing/tangent and one-relator arguments. Its P232/P245/P246 uses remain unchanged. Opened Dloussky math/0406387v3,13Apr2005, SHA256f461b07b3bb60a6c1433172a5514fa6e90a41e43dac6f23396a4713d99f5c3f9: read Theorem0.2 p2, Remark0.6 pp3–4, Section1 pp4–5, Definition2.20 p14, Lemma2.22/full proof p15, Corollary2.25/full proof pp16–17, Proposition2.27/full proof pp17–19, Proposition2.29/full proof p19, Theorem2.38/full proof pp24–25. Opened DOT2003 publisher PDF SHA256b1b66ca42a4765dc3242dd68342cb62d414f45527486932fe425b6a8fe8cc962 and read pp283–285 and296. No unchanged bibliography write is proposed.'),
 ('vii234','cdp:st:C.2.VII.2','Read every original and receiving statement/proof of VII.2, VII.3 and VII.4. Preserve full conductor-scheme duality, χ≥−1, the exact negative-node exclusion via branch reception and connected exceptional fibre, the a/b/r complement counts, both curve-pattern directions, the nonconstant Picard differential, χ≥0, the square-zero rational-cycle obstruction and the smooth minimal Hopf equivalence. P222 is used at its exact surface hypotheses, P281 supplies the original numerical inputs, and P243 supplies the exceptional matrix. The receiving statements retain disjoint unions of elliptic conductor curves and do not reintroduce the old connected-image conclusion of refined P4R.13. No P4.40 global all-fibres assumption is used.'),
 ('curve','lem:II:curve-euler-delta','Read complete original VII.2/VII.4/INT.3 proofs, complete P290 proof, and complete receiving INT.3 proof. The coherent normalization quotient gives δ, P245 gives the topological formula componentwise, and independent constants modulo the diagonal give the quotient of dimension s−1. These prove the exact Euler identity, its χ≥0 equality criterion and the empty case. The old r_x and new s_x denote the same normalization branch count. C.VII.5 and C.INT.26 remain at the earlier owner; the two later applications verify their respective genus and coherent-Euler hypotheses. C.INT.26/C.INT.27 are cited as two equations after their separation, not as the enlarged numbering interval.'),
 ('minimality','lem:II:last-blowup-minimal-resolution','Read the complete P291 proof and its complete receiving VII.4 and INT.3 consumers. In VII.4, σ is the blowdown to the Hopf minimal model and all its rational exceptional curves are π-exceptional by b2=r+a. In INT.3, σ_i is the given component minimal-model map and equality r_i+a_i=N_i gives the same inclusion into π_i-exceptional curves. The final blowup curve has square−1 on the same smooth source and contradicts minimality of the normal-surface resolution. Thus the identical argument has one owner, with both maps stated at each application.')
]
for suffix,owner,outcome in data:
    identity='publish:c3:foundations:sec07:class-vii:'+suffix
    e=dict.fromkeys(event_fields,'')
    e.update(statement_id=owner,date=now[:10],who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 foundations',type='used and rechecked in this run',outcome=outcome+' Exact in-memory replay matched all11 guards once and preserved every existing label and target multiplicity. During the receiving read, the D19 helper’s single-letter tag collision with the argument e(C) was detected in an unadmitted proposal and corrected by excluding single-letter replacements; the complete corrected receiving proofs were reread. No original mathematical refutation, independent check, required-check increment or final PDF read is claimed.',event_id=identity,phase='publication text and proof comparison',source_file=str(path.relative_to(ROOT)),source_event_type='used and rechecked in this run',evidence_group=identity,date_utc=now,where='Earlier VII.1/P4.23 input and class-VII conductor subsection; bounded INT.3 and reference consumers')
    events.append(e)
with (OUT/(prefix+'_CHECK_EVENTS.tsv')).open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=event_fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(events)
status=[]
for kind in [f'D{i:02}' for i in range(1,26)]+['restructuring']:
    state='done';basis='The complete receiving class-VII conductor subsection was read against this class; every changed instance is logged. Early VII.1/P4.23 and bounded INT.3 consumers have separate complete-proof comparison events, not extra subsection completion claims.'
    if kind in ('D14','D24','restructuring'):
        state='open';basis='The earlier VII.1 owner precedes P4.23; P290/P291 and VII.2–4 precede CR.1. All written premises are now earlier in the proposal. Root admission and final whole-paper placement remain; the contracted-boundary remainder stays open.'
    if kind in ('D10','D16'):basis='Existing closure preserved: every statement keeps its titled header, permanent tag and label, with hidden dependency apparatus.'
    if kind=='D23':basis='Source typography, including the multiline curve formula, was read; root owns integrated build and final page-reading gates.'
    status.append(dict(unit='subsec:II:class-vii-canonical-boundaries',row=kind,status=state,basis=basis,fragment='agents/continuation3_foundations/sec07/S6_SERIES_PUBLISH_II_sec07_class_vii.tex'))
with (OUT/(prefix+'_unit_progress.tsv')).open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(status[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(status)
print(f'{len(rows)} defects, {len(events)} exposed-reading events, 26 bounded subsection rows; P290/P291 used, VII.1 owner moved with its original identifier.')
