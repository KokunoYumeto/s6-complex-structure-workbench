#!/usr/bin/env python3
"""Export the exact scalar marked-product obstruction as P3K.61."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[2]
source=ROOT/'notes/part3_scalar_outer_clutch_audit.md'
stamp=datetime.now(timezone.utc).isoformat()
with (ROOT/'records/literature_fourfold.md').open('a') as log:
 log.write('\n- '+stamp+' — Opened '+str(source.relative_to(ROOT))+'. Reason: export exact K61 maps and marked-product obstruction. Material: actual scalar seam, full outer positive-weight determinant transition, and endpoint/bundle-map contradiction; no corrected global residue is asserted.\n')
raw=source.read_text()
body='## SOC.1.'+raw.split('## SOC.1.',1)[1].split('## SOC.4.',1)[0]
body=body.replace('the same actual\nlogarithms and cutoff as SCN.1','the actual\nlogarithms on the cut disc and a smooth cutoff zero on the initial collar and one on the final collar')
statement=r'''For an actual primitive scalar family of P3K.22, including
the OS45 family of P3K.10, retain its positive physical circle, full
source and line units, actual cap-to-ordinary gluing and forward
parameter arrow. On every nonzero signed degree-\(M\) pullback of
its primitive scalar loop, the three labelled cusp curves, their two
labelled vertices and their positive complex curve orientations admit
no periodic smooth product intertwining the physical delta action and
carrying all these marked submanifolds to constant copies.

The literal comparison at the second outer fixed branch between the
fixed-curve native product and the horizontal-curve native product is
\[
 z_1=(g/\kappa)z_0,\qquad
 (N_{1,-},N_{1,+})=
 \bigl((\eta/\alpha)N_{0,-},\,
       (\kappa\alpha/(g\eta))N_{0,+}\bigr).
\]
After conjugating the negative-weight first line, its determinant is
\[
 \det_+\Gamma
 =\frac\kappa g\frac\alpha{\overline\alpha}
                 \frac{\overline\eta}{\eta},
 \qquad\operatorname{wind}(\det_+\Gamma)=-2M.
\]
The other outer branch comparison is the identity. This identifies
the retained outer line clutch missing from P3K.25's claimed
parameter-free determinant, and disproves the marked simultaneous
equivariant-product premise used in P3K.29, Section3. It assigns no
corrected global characteristic number. The separately proved
cellular topology, reciprocal-section basis maps, variation symmetry,
and stable-frame change identities do not require that premise.'''
def tex(s):
 s=s.replace(r'\tag{SOC.',r'\tag{P3K.61.SOC.').replace('(SOC.','(P3K.61.SOC.')
 s=s.replace(')--(P3K.61.',')--\\allowbreak (P3K.61.')
 s=re.sub(r'^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'.}\par\nopagebreak[4]',s,flags=re.M)
 s=re.sub(r'`([^`]+)`',lambda m:r'\path{'+m.group(1)+'}',s)
 return s.strip()+'\n'
export=r'\begin{statement}{P3K.61}{Proved}'+'\n'+tex(statement)+r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+tex(body)+r'\end{proof}'+'\n'
assert not re.search(r'(?<!\\)#',export)
(ROOT/'notes/part3_scalar_outer_clutch_obstruction.tex').write_text(export)
(ROOT/'notes/part3_scalar_outer_clutch_obstruction.md').write_text('# P3K.61. Exact outer scalar clutch and marked-product obstruction\n\n'+statement+'\n\n**Proof.**\n\n'+body+'\n\n**End of proof.**\n')
mp=ROOT/'code/part3_fourfold/results_mapping.json';mapping=json.loads(mp.read_text())
mapping['results']=[r for r in mapping['results'] if r.get('id')!='P3K.61']
mapping['results'].append(dict(id='P3K.61',status='Proved',item_of_prompt='3.4',
 statement='For nonzero signed scalar winding M, the actual marked three-curve plumbing has no periodic delta-equivariant product; the exact outer positive-normal determinant clutch has winding -2M.',
 proof_file='notes/part3_scalar_outer_clutch_obstruction.md',latex_file='notes/part3_scalar_outer_clutch_obstruction.tex',
 working_proof=str(source.relative_to(ROOT)),source_sha256=hashlib.sha256(raw.encode()).hexdigest(),
 correction_scope=['K25 outer determinant pullback assertion misses the actual clutch','K29 simultaneous marked equivariant product premise fails'],
 preserved_scope=['cellular topology','reciprocal-section maps','variation symmetry','frame-change identity','separate fixed/native star products'],
 remaining_scope='No corrected closed fixed-base residue or replacement all-fan scalar formula is assigned.'))
mp.write_text(json.dumps(mapping,indent=2)+'\n')
print(json.dumps(dict(id='P3K.61',source_sha256=hashlib.sha256(raw.encode()).hexdigest(),tex_file='notes/part3_scalar_outer_clutch_obstruction.tex'),indent=2))
