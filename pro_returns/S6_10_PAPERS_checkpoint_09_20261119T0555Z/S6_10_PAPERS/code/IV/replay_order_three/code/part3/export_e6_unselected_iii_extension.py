#!/usr/bin/env python3
"""Complete K96 export. Own artifacts only; central master untouched."""
from pathlib import Path
import hashlib,json,re,subprocess
R=Path(__file__).resolve().parents[2]
src=R/'notes/part3_e6_unselected_iii_extension_working.md'
s=src.read_text();sha=hashlib.sha256(src.read_bytes()).hexdigest()
approved='cb069cbf3c3019764e68fe18c447af5a75d921706aa4a0a2641146cc7e7cae2b'
assert sha==approved, 'Review the changed mathematical source before export'
cert=R/'code/part3/e6_unselected_iii_extension.json';d=json.loads(cert.read_text())
assert d['status']=='PASS' and d['source_sha256']==sha
body=s[s.index('## EX.1.'):]
body=body.replace('The preceding three sections are the retained initial local stage,\nalso saved in \\path{records/attempts/e6_unselected_iii_extension/initial_local.md}.\nWe now give the remaining maps for both admitted cap progressions.', 'The initial local stage is preserved in \\path{records/attempts/e6_unselected_iii_extension/initial_local.md}. The following maps complete both cap progressions.')
body=body.replace('The proofs below construct the full marked disc\nfamily; their final return conclusion has not yet been promoted.', 'The following maps construct the full marked disc family.')
body=body.replace('This conclusion is submitted for full independent audit;\nno numbered promotion is made in this working extension.', 'The quotient, line, annular and topology maps above prove the stated return for the full marked family.')
body=body.replace('the geometric proof is given\nabove and is subject to the separate named audits.', 'the complete geometric proof above has the recorded root and independent peer audits.')
body=re.sub(r'(?m)^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',body)
tex=subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex-superscript-subscript-smart','-t','latex','--wrap=preserve'],input=body,text=True,capture_output=True,check=True).stdout.replace(r'\tightlist','')
statement=r'''Retain the actual source
\[
 y^2=x^3+r x^2+t x+t^2,\qquad G=(0,t),\qquad
 M_a=\mathcal O(aG-O),\qquad Q=bG,
\]
on a sufficiently small disc about \(r=0\). Choose the analytic branch
\(\rho^2=1-3r\), \(\rho(0)=-1\), and the selected whole
\(I_1\) zero \(t_c=(1-3\rho^2+2\rho^3)/27\). For either of the
complete cap progressions
\[
\begin{array}{c|c|c|c}
(a,b)&m&\text{root fibre}&\text{range}\\\hline
(6,1)&3l+2&IV&l\ge0\\
(2,3)&3l&\text{smooth elliptic}&l\ge1
\end{array}
\]
use the exact Cartier suspension
\(B_{\rm sel}=(t-t_c)B_{a,b}/t^3\) of the proof, either primitive
norm \(n=\pm1\), every prescribed character \(\zeta_m^d\), and
the entire specified reference annular map. Retain a fixed sufficiently
small nonzero scalar for the chosen fan, and no extra logarithmic disc
at the colliding fibres. For every prescribed lattice-basis fan at the
selected cusp, these actual maps extend to a smooth proper oriented
sphere family over the full source disc, with identity parameter
closing. Its positive boundary return is \(0\in\Theta_7\).
The literal marked-cover map \(D=w^2-3\),
\(r=(3-2w^2)/D^2\), \((X,Y,T)=(D^2x,D^3y,D^3t)\)
carries the same conclusion to both points \(w^2=3/2\), with the
full scalar, line, cap and fan marking retained.'''
out=R/'notes/part3_e6_unselected_iii_extension.tex'
out.write_text('\\subsection{The full E6 unselected-III cap progressions}\n\\begin{statement}{P3K.96}{Proved}\n'+statement+'\n\\end{statement}\n\\begin{proof}\n'+tex+'\n\\end{proof}\n')
pre=(R/'S6_06_BLIND_paper.tex').read_text().split(r'\begin{document}')[0]
(R/'code/part3/k96_standalone.tex').write_text(pre+'\n\\begin{document}\n\\input{notes/part3_e6_unselected_iii_extension.tex}\n\\end{document}\n')
manifest={'id':'P3K.96','status':'Proved','source':str(src.relative_to(R)),'source_sha256':sha,'include':str(out.relative_to(R)),'include_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'certificate':str(cert.relative_to(R)),'certificate_sha256':hashlib.sha256(cert.read_bytes()).hexdigest(),'checks':d['checks'],'master_modified':False,'report_modified':False,'mapping_modified':False,'qa':'pending'}
(R/'records/k96_export_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(manifest,indent=2))
