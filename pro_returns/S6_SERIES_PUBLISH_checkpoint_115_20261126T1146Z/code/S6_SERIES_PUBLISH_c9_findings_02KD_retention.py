#!/usr/bin/env python3
"""Guarded 02KD role reconciliation and the two 02KF circle imports."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import difflib
import json
import re
from S6_SERIES_PUBLISH_c9_scoped_notation import ScopedReview, math_letters

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation9_findings'
source=(ROOT/'S6_SERIES_PUBLISH_III.tex').read_text()
stem='S6_SERIES_PUBLISH_c9_current02_02KD_retention'
p=ScopedReview(source,
    r'\begin{theorem}[Integral homology of the universal cover]',
    r'\subsection{Framings and the quotient homotopy class}',
    '02KD','maps:src:D.1.4','26--31; Theorem 3.8',
    'Used and rechecked in this run after exposure. Read Definition Q009 and the complete current 02KD statement/proof, all final differences and the downstream 02KF statement/proof. Compared each affected coordinate map, inverse, signed boundary and exported class. Scoped/full-source reversal, numeric literals, labels and targets passed. Formal coefficient arguments retained explicitly. No independent proof or new image credit. Admission and changed rendering pending.')

p.exact(r''' Q_2^*H^2(S'_2)=\langle\beta_2,C_2\rangle,\quad
 \beta_2=2\alpha_2,\ C_2=\alpha_2+Q .''',
        r''' Q_2^*H^2(S'_2)=\langle\beta_2,C_2^{\rm coh}\rangle,\quad
 \beta_2=2\alpha_2,\ C_2^{\rm coh}=\alpha_2+Q .''',
        'Name the integral cohomology preimage C_2^{coh}. It is exactly the old alpha_2+Q, paired with the same dual finite-fibre basis; the subgroup and inverse coordinates ((a-b)/2,b) are unchanged. The later trace chains retain their separate explicit names.',
        [r'C_2^{\rm coh}'])
p.edit('Let $A,B,C,D$ be homology bases dual',
       '\\item\nFor the cusp pair',
       lambda t:math_letters(t,{'C':r'C_{\rm fin}'}),
       'Name the third finite-fibre homology basis element C_fin, preserving the holomorphic period matrix C(q). The dual-basis identification is the identity, so M_2, its image generators and their preimages, h=-C_fin and the quotient functional have the same coefficients. The tuple coefficients a,b,c,f remain formal arguments, including the exact decomposition proving the quotient and inverse.',
       [r'C_{\rm fin}'])
p.exact(r' -e A-2pB,\qquad e C+\frac{e+3p}{2}D.',
        r' -e A-2pB,\qquad e C_{\rm fin}+\frac{e+3p}{2}D.',
        'Propagate C_fin into the second finite orbit torus. Its coordinate coefficient is still e, so the quotient functional still gives -p on the sum and the same signed attachment matrix.',
        [r'C_{\rm fin}'])

p.exact(r' \bigwedge^2\mathbb Z\langle w,\delta,q\rangle .',
        r' \bigwedge^2\mathbb Z\langle w,\delta,q_{\rm circ}\rangle .',
        'Name the positive coordinate-circle generator q_circ in the relative boundary target. It is the same oriented loop and the same ordered wedge basis, with the same conical inverse representatives.',
        [r'q_{\rm circ}'])
p.exact('that chart. Here and below $q$ is the positive coordinate circle.',
        'that chart. Here $q_{\\rm circ}$ denotes the positive coordinate circle.',
        'Give the positive coordinate circle its explicit name q_circ while retaining q as the base coordinate used in Y_0, the chart radius and C(q). The renamed circle is exactly the original positive loop in that coordinate.',
        [r'q_{\rm circ}'])


def circle_action(t):
    t=math_letters(t,{'q':r'q_{\rm circ}'})
    return t.replace(r'C(q_{\rm circ})','C(q)')


p.edit('On $H_1(T)$ the prescribed period action is',
       'To pass to the quotient pair',circle_action,
       'Propagate the circle name through the two period-action shears and the exterior-square coinvariants. The base argument in C(q) remains q. The actions still send q_circ to q_circ+w and q_circ-d delta; their inverse shears and the killed wedge w wedge delta are unchanged.',
       [r'q_{\rm circ}'])
p.exact(r'''with the length-two free resolution for $\mathbb Z^2$,
with differentials $(a-1,b-1)$ and $(1-b,a-1)^t$.''',
        r'''with the length-two free resolution for $\mathbb Z^2$.
Write $\mathsf a,\mathsf b$ for the group-ring generators corresponding
to $u,d\gamma$; its differentials are
$(\mathsf a-1,\mathsf b-1)$ and $(1-\mathsf b,\mathsf a-1)^t$.''',
        'Qualify the two group-ring generators as mathsf a,mathsf b and bind them to the same deck generators u,d gamma. The ring isomorphism sends the old a,b to these generators with inverse the unique integer deck coordinates. Every differential entry has the same group action; a^lambda remains the translation notation and b=u+w-delta remains the persistent homology generator.',
        [r'\mathsf a',r'\mathsf b'])
p.exact(r'''$\partial c_w=(q,w)$, $\partial c_\delta=(q,\delta)$,''',
        r'''$\partial c_w=(q_{\rm circ},w)$, $\partial c_\delta=(q_{\rm circ},\delta)$,''',
        'Propagate q_circ into both ordered relative boundary tori, retaining the base-circle-first orientation and the same c_w,c_delta representatives.',
        [r'q_{\rm circ}'])
p.exact('vector path. The lift of the positive $q$ loop is',
        'vector path. The lift of the positive $q_{\\rm circ}$ loop is',
        'Use the same named positive circle in its based lift. The basepoint path, winding, translation exponent and based word mu remain unchanged.',
        [r'q_{\rm circ}'])
p.exact('with $0<r<\\epsilon$. Its positive boundary is $q+j\\delta$.',
        'with $0<r<\\epsilon$. Its positive boundary is $q_{\\rm circ}+j\\delta$.',
        'Propagate q_circ to the actual ray-disc boundary. The disc map in coordinates (x_1,x_2,q), its radius and orientation are unchanged, so its image in H_1(U) remains z_0.',
        [r'q_{\rm circ}'])
p.exact('image $z$ of $(q,w)$ maps to $b$',
        'image $z$ of $(q_{\\rm circ},w)$ maps to $b$',
        'Propagate the same circle into the torus defining z. Its Mayer-Vietoris boundary is the same persistent vector b, so the exported (h,z) basis and its inverse remain unchanged.',
        [r'q_{\rm circ}'])
p.exact('identifies the class of $(q,\\delta)$',
        'identifies the class of $(q_{\\rm circ},\\delta)$',
        'Propagate q_circ into the delta-orbit torus. The actual free circle action and its evaluation on mu=t_1+t_2 retain the same chain and signed finite coordinates.',
        [r'q_{\rm circ}'])


def trace_chains(t):
    for j in ['j','1','2']:
        t=t.replace('C_'+j+'(', 'C_'+j+r'^{\rm tr}(')
    return math_letters(t,{'q':r'q_{\rm circ}'})


p.edit('The trace cylinders along $t_j$',
       'The cycles',trace_chains,
       'Name the actual trace chains C_j^{tr}(lambda), preserving their domains, boundary (A_j-I)lambda and the linear triangles correcting sums. The same combination defines D_delta with boundary delta. Use q_circ in the same covering-plane triangle, leaving every boundary and splitting cycle unchanged.',
       [r'C_j^{\rm tr}',r'C_1^{\rm tr}',r'q_{\rm circ}'])

old=r''' Q_1^*H^2(S'_1)=\langle\alpha_1,Q\rangle,\qquad
 Q_2^*H^2(S'_2)=\langle\beta_2,C_2^{\rm coh}\rangle,\quad
 \beta_2=2\alpha_2,\ C_2^{\rm coh}=\alpha_2+Q .'''
new=r''' \begin{gathered}
 Q_1^*H^2(S'_1)=\langle\alpha_1,Q\rangle,\\
 Q_2^*H^2(S'_2)=\langle\beta_2,C_2^{\rm coh}\rangle,\\
 \beta_2=2\alpha_2,\ C_2^{\rm coh}=\alpha_2+Q .
 \end{gathered}'''
def layout_tokens(t):
    t=re.sub(r'\\(?:begin|end)\{gathered\}', '',t)
    t=t.replace(r'\\','').replace(r'\qquad','').replace(r'\quad','')
    return re.sub(r'\s+','',t)
assert layout_tokens(old)==layout_tokens(new)
p.exact(old,new,
        'Break the cohomology subgroup display into three gathered rows. Removing only the gathered environment, row separators and spacing leaves the same ordered mathematical tokens; both integral subgroups and basis definitions are unchanged.',
        [r'C_2^{\rm coh}'])

assert p.new.count('C(q)')==p.old.count('C(q)')
assert p.new.count(r'\mathbb C')==p.old.count(r'\mathbb C')
assert p.new.count('a^')==p.old.count('a^')
assert r'$b=u+w-\delta$' in p.new
rows=p.finish(OUT,stem)
for row in rows:
    row['change_id']=row['change_id'].replace('-02KD-','-02KD-retention-')

imports=[
    (r''' \qquad\partial n_v=q+v_1w+v_2\delta.
\]
Here $q,w,\delta$ denote the positive coordinate circles.''',
     r''' \qquad\partial n_v=q_{\rm circ}+v_1w+v_2\delta.
\]
Here $q_{\rm circ},w,\delta$ denote the positive coordinate circles.'''),
    ('Their boundary loops are $q$ and $q+w$ at $b$.',
     'Their boundary loops are $q_{\\rm circ}$ and $q_{\\rm circ}+w$ at $b$.')]
for i,(old,new) in enumerate(imports,1):
    assert source.count(old)==1
    row=dict(rows[0])
    row.update(change_id=f'CLAUDE-III-P15-current02-02KD-retention-import-{i:02}',
               statement_id='maps:src:D.1.6',
               old_location=f'Paper III, tag02KF; integral ruling calculation, circle import {i}',
               old_page='candidate02 75 onward; Theorem 5.10',
               old_text=old,new_text=new,
               reason='Propagate the same positive-circle name from the imported 02KD normal-disc calculation. The actual toric discs and their ordered boundaries retain the same q_circ loop and w/delta periods. The base coordinate q, the holomorphic function C(q), the period action, exported h,z,z_0 and finite generator B remain unchanged.',
               review_status='Used and rechecked in this run after exposure. Read the complete current 02KF statement/proof, its imports from 02KD, both actual toric discs and the subsequent period/ruling calculation; compared this guarded circle-name change. No independent proof or new image credit. Admission and changed rendering pending.')
    rows.append(row)
    with (OUT/(stem+'.diff')).open('a') as f:
        f.write('\n'+''.join(difflib.unified_diff((old+'\n').splitlines(True),(new+'\n').splitlines(True),fromfile=f'02KF circle import {i} before',tofile=f'02KF circle import {i} proposed')))
full=source
for row in rows:
    assert full.count(row['old_text'])==1
    full=full.replace(row['old_text'],row['new_text'],1)
for pattern in [r'\\label\{[^}]+\}',r'\\hypertarget\{[^}]+\}',r'\d+']:
    assert re.findall(pattern,full)==re.findall(pattern,source)
for row in reversed(rows):
    assert full.count(row['new_text'])==1
    full=full.replace(row['new_text'],row['old_text'],1)
assert full==source
(OUT/(stem+'.json')).write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
with (OUT/(stem+'_defects.tsv')).open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t',lineterminator='\n')
    w.writeheader();w.writerows(rows)
print(len(rows),'total guarded fragments, including two explicit 02KF circle imports.')
print('Complete current 02KD and 02KF proof contexts read; canonical manuscript unchanged.')
event_id='ce:c9-iii-current02-02kd-retention-reconciliation'
event=dict(statement_id='maps:src:D.1.4',date='2026-11-26',
           who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode',
           type='used and rechecked in this run',
           outcome='Read Definition Q009 and the complete current 420-line 02KD statement/proof, plus the complete downstream 02KF statement/proof and actual named imports. Compared all 10 final fragments from 14 internal reversible operations plus two imported circle-name changes. Verified the identity assignments, cohomology subgroup inverse, finite-basis functional and image preimages, deck-resolution coefficient isomorphism, signed circle boundaries, trace chains and unchanged exported h,z,z_0,B. Explicit formal coefficient arguments retained. One display token comparison, full-source reversal, numeric literals, labels and targets passed. No independent proof, new matrix replay or image credit. Admission and changed rendering pending.',
           event_id=event_id,phase='publication continuation 9',
           source_file='agents/continuation9_findings/'+stem+'_review.md',
           source_row='complete current 02KD and 02KF statements/proofs, every affected binding and final difference',
           source_event_type='used and rechecked in this run',evidence_group=event_id,
           publish_input_file='agents/continuation9_findings/'+stem+'_defects.tsv',
           publish_input_row='all 10 guarded fragments',
           date_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
           where='Paper III, tag02KD / maps:src:D.1.4 within progress unit maps:src:D.1.1, with the two tag02KF / maps:src:D.1.6 positive-circle imports')
with (OUT/(stem+'_CHECK_EVENTS.tsv')).open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(event),delimiter='\t',lineterminator='\n')
    w.writeheader();w.writerow(event)
