#!/usr/bin/env python3
"""Export the independently audited root CF.1--5 proof as P3K.59."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,re

ROOT=Path(__file__).resolve().parents[2]
source=ROOT/'notes/part3_source_cusp_mutation_staircase_working.md'
stamp=datetime.now(timezone.utc).isoformat()
with (ROOT/'records/literature_fourfold.md').open('a') as log:
    log.write('\n- '+stamp+' — Opened '+str(source.relative_to(ROOT))+
      '. Reason: export the complete root-audited and independently audited K59 proof. '
      'Material: full CF.1--5 Cox/unit maps, explicit U(2) path, selected native reset, '
      'trace uniqueness and all-j induction. Root working source is not edited.\n')
raw=source.read_text()
assert r'\tag{CF.6a}' in raw
body='## CF.1.'+raw.split('## CF.1.',1)[1]
body=body.replace(r''' V_{jj}=I_j/w_j,\quad V_{rj}=V_{jr}=-I_r/w_j,
 \quad V_{pq}=0\quad(p,q\ne r,\ p\ne q),\qquad
 \delta_j=(W_j-W_r)/w_j\quad(j\ne r).                 \tag{CF.13}''',r''' \begin{aligned}
 V_{jj}&=I_j/w_j,\qquad V_{rj}=V_{jr}=-I_r/w_j,\\
 V_{pq}&=0\qquad(p,q\ne r,\ p\ne q),\\
 \delta_j&=(W_j-W_r)/w_j\qquad(j\ne r).
 \end{aligned}                                      \tag{CF.13}''')
statement=r'''Retain the actual positive selected-cusp source loop of
P3F.54 and P3F.56, with its fixed scalar, prescribed finite cap,
physical height, Cartier line and complete period units. For every
integer \(j\geq0\), consider the two specified periodic fans with bases
\[
 P_j=\begin{pmatrix}1&-j\\0&1\end{pmatrix},\qquad
 R_j=\begin{pmatrix}j+1&-j\\-1&1\end{pmatrix}.
\]
Their actual oriented clutched-sphere classes are
\[
 [\Phi_{P_j}]=1-3j(j+1),\qquad
 [\Phi_{R_j}]=-5-24j(j+1)\quad\text{in }\Theta_7=\mathbb Z/28.
\]
On \(P_j\), the complete ordinary-product variation and ambient
stable-derivative invariants in the marked three-curve basis are
\[
 V_j=\begin{pmatrix}
 0&6(j+1)&-6\\
 6(j+1)&18j(j+1)&-6j\\
 -6&-6j&0
 \end{pmatrix},\qquad
 \delta_j=\begin{pmatrix}-12(j+1)\\-24j(j+1)-12\\12j\end{pmatrix}.
\]
The corresponding native relative pairs, in the order \(C_0,C_1,C_2\), are
\[
 (6j,-6(j+1)),\qquad
 (3j(j+1),-21j(j+1)-6),\qquad
 (-6j-6,6j).
\]
For each selected periodic flop used in these constructions, write
\(a=V_{ii}\), \(b=\delta_i\), and let \(i'\) be the new label of that
same flopped curve. The actual native Cox arrow and the carried
ordinary-product comparison give exactly
\[
 V'_{i'i'}=a,\qquad \delta'_{i'}=2a-b,\qquad
 s'=s+\frac{b-a}{2}\pmod {28}.
\]
The \(R_j\) return sequence has least positive period seven and exact
range \(\{3,15,19,23\}\). In particular \(R_1\) has class three.
The statement concerns these explicitly constructed families and their
selected updates; it assigns no return to an additional fan.'''

def tex(value):
    value=value.replace(r'\tag{CF.',r'\tag{P3K.59.CF.')
    value=value.replace('(CF.','(P3K.59.CF.')
    value=value.replace(')--(P3K.59.',')--\\allowbreak (P3K.59.')
    value=re.sub(r'^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'.}\par\nopagebreak[4]',value,flags=re.M)
    value=re.sub(r'`([^`]+)`',lambda m:r'\path{'+m.group(1)+'}',value)
    return value.strip()+'\n'

export=r'\begin{statement}{P3K.59}{Proved}'+'\n'+tex(statement)+r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+tex(body)+r'\end{proof}'+'\n'
assert not re.search(r'(?<!\\)#',export)
assert '`' not in export
(ROOT/'notes/part3_source_cusp_mutation_staircase.tex').write_text(export)
(ROOT/'notes/part3_source_cusp_mutation_staircase.md').write_text('# P3K.59. Proved: actual native Cox mutations and two complete source-loop fan families\n\n'+statement+'\n\n**Proof.**\n\n'+body+'\n\n**End of proof.**\n')
record=dict(utc=stamp,status='PASS',reviewer='fourfold',source=str(source.relative_to(ROOT)),source_sha256=hashlib.sha256(raw.encode()).hexdigest(),
 scope=['CF.1 actual first/second Cox charts and complete period-unit change','CF.6a constant U(2) bundle path','CF.2 selected native/ordinary L^6 and fixed-J reset','CF.3 actual trace-map uniqueness, including declared zero-weight scope','CF.4 all-j invariants and native pairs by exact target induction','CF.5 adjacent family and exact residue range'],
 findings='No mathematical gap found in the declared two-family scope; no simultaneous old-product matrix reset or universal all-fan value is used.',
 tex_file='notes/part3_source_cusp_mutation_staircase.tex')
(ROOT/'records/k59_fourfold_audit.json').write_text(json.dumps(record,indent=2)+'\n')
mp=ROOT/'code/part3_fourfold/results_mapping.json'
mapping=json.loads(mp.read_text())
mapping['results']=[r for r in mapping['results'] if r.get('id')!='P3K.59']
mapping['results'].append(dict(id='P3K.59',status='Proved',item_of_prompt='3.4',
 statement='Actual positive selected-cusp source return on P_j is 1-3j(j+1), and on R_j is -5-24j(j+1), modulo28, for every j>=0; complete P_j variation/derivative and native pairs are explicit.',
 proof_file='notes/part3_source_cusp_mutation_staircase.md',latex_file='notes/part3_source_cusp_mutation_staircase.tex',
 working_proof=str(source.relative_to(ROOT)),parameter='original positive marked rho loop, fixed scalar, retained source and finite-cap data',
 adjacent_residue_range=[3,15,19,23],adjacent_period=7,
 source_sha256=record['source_sha256'],audit_file='records/k59_fourfold_audit.json',
 remaining_scope='No return outside the two explicitly constructed fan families is assigned.'))
mp.write_text(json.dumps(mapping,indent=2)+'\n')
print(json.dumps(record,indent=2))
