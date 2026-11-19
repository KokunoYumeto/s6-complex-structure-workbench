#!/usr/bin/env python3
"""Export P3K.70 only; leave the root master and its include list untouched."""
from pathlib import Path
from datetime import datetime,timezone
import re,subprocess,shutil,json,hashlib
R=Path(__file__).resolve().parents[2]
src=R/'notes/part3_scalar_nonvertical_working.md'
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
A=R/'records/attempts/k70_pre_export'/stamp;A.mkdir(parents=True)
shutil.copy2(src,A/src.name)
text=src.read_text()
text=text.replace('Working proof after checkpoint16, 17 November 2026.','Proved as P3K.70 after the root geometric audit and exact certificate, 17 November 2026.')
text=text.replace('Promotion awaits the\nindependent audit of NV.2\'s C0 product/closing match and NV.4\'s full\nselected target-product comparison. The formulas above are retained\nas a complete working derivation, not yet an active theorem.', 'The root independently audited NV.1–4, including the exact C0 closing,\nproduct comparison and target reconstruction. The complete closing\nand repeated-fan certificate below has also passed. This assigns the\nreturn of the stated concrete family and fan only.')
src.write_text(text)
proof=text[text.index('## NV.1.'):]
proof=re.sub(r'(?m)^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',proof)
proof=re.sub(r'`((?:code|notes|records)/[^`]+)`',lambda m:r'\path{'+m.group(1)+'}',proof)
proof=proof.replace('value is3','value is 3').replace('Formula(NV.18) is102','Formula (NV.18) is 102').replace('adds18 and gives21','adds 18 and gives 21')
tex=subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex','-t','latex','--wrap=preserve'],input=proof,text=True,capture_output=True,check=True).stdout
tex=tex.replace(r'\tightlist','')
statement=r'''Retain the exact OS45 rational elliptic source, section, line and cap
\[
\begin{gathered}
y^2=x^3-3f(t)x+2g(t),\qquad
f=(t^2+1)^2+t,\\
g=(t^2+1)^3+\tfrac32t(t^2+1)+\tfrac38,\qquad
G=(t^2+1,\sqrt3/2),\\
\mathcal M=\mathcal O(8G-O),\qquad Q=G.
\end{gathered}
\]
Choose one of the four marked simple roots of
\(48t^4+8t^3+96t^2+72t+57\) as its whole-fibre linearization zero,
and retain the ordinary order-one logarithmic cap at \(t=0\) from
K10. Use its primitive scalar parameter \(\lambda=r\), its actual
forward closing \(t/(t-\tau)\), and all the original source, line
and cap maps.

In the original Tate/source and line period lattice, replace the cusp
fan by the periodic triangulation with ordered basis
\[
 v=(2,-1),\qquad w=(-1,1),
\]
and triangles \((n,n+v,n+w)\),
\((n+v,n+w,n+v+w)\) for every \(n\in\mathbb Z^2\).
The resulting actual holomorphic sphere family has positive
single-loop physical return
\[
 [\Sigma_\Phi]=11\quad\hbox{in }\mathbb Z/28,
 \qquad \mu(\Sigma_\Phi)=11/28\pmod{\mathbb Z}.
\]
It is obtained by the two explicit Cox flops below, with initial,
intermediate and final physical classes \(3,21,11\). Its mapping
torus is not diffeomorphic to \(S^1\times S^6\), by the retained
spin/connected-sum argument of F24 and the physical transfer K68.
This statement assigns no universal scalar-fan formula or value at
an unevaluated fixed-star target.'''
out=R/'notes/part3_scalar_nonvertical.tex'
if out.exists():shutil.copy2(out,A/out.name)
out.write_text(r'\subsection{A concrete scalar return on a nonvertical fan}'+'\n'+r'\begin{statement}{P3K.70}{Proved}'+'\n'+statement+'\n'+r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+tex+'\n'+r'\end{proof}'+'\n')
preamble=(R/'S6_06_BLIND_paper.tex').read_text().split(r'\begin{document}')[0]
(R/'code/part3/k70_standalone.tex').write_text(preamble+'\n'+r'\begin{document}'+'\n'+r'\input{notes/part3_scalar_nonvertical.tex}'+'\n'+r'\end{document}'+'\n')
(R/'records/k70_export_manifest.json').write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'include':str(out.relative_to(R)),'include_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'preserved_prior':str(A.relative_to(R)),'master_modified':False},indent=2)+'\n')
print(out.relative_to(R))
