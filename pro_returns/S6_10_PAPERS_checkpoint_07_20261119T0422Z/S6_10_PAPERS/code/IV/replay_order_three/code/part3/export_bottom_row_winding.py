#!/usr/bin/env python3
"""Export only P3K.76, with its full relative and named OS49 proof."""
from pathlib import Path
from datetime import datetime,timezone
import re,subprocess,shutil,json,hashlib,argparse
p=argparse.ArgumentParser();p.add_argument('--proved',action='store_true');args=p.parse_args()
ROOT=Path(__file__).resolve().parents[2]
src=ROOT/'notes/part3_bottom_row_winding_working.md'
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
history=ROOT/'records/attempts/k76_pre_export'/stamp;history.mkdir(parents=True)
shutil.copy2(src,history/src.name)
proof='## BW.1.'+src.read_text().split('## BW.1.',1)[1]
proof=re.sub(r'(?m)^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',proof)
proof=re.sub(r'`((?:code|notes|records)/[^`]+)`',lambda m:r'\path{'+m.group(1)+'}',proof)
tex=subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex','-t','latex','--wrap=preserve'],input=proof,text=True,capture_output=True,check=True).stdout
tex=tex.replace(r'\tightlist','')
statement=r'''Retain the actual OS49 source
\[
y^2=x^3-3t^3(t-1)x+2t^4(t-1)(t-\tfrac12),\qquad G=(t^2,t^2),
\]
the line \(M=\mathcal O(G-O)\), suspension over \(-3G\), and
its target-point linearization divisor \(C_0\) on the \(I_2\) fibre.
Retain the \(IV^*\) cap of order \(m=3k>0\), either norm
\(\nu=\pm1\), every fixed character \(d\), and the full root,
type-II and annular arrows of P3K.65. In the physical character
lattice put \(T_n=T(e_1+ne_2,e_2)\). The negative fan is \(T_0\)
and the positive fan is \(T_1\), by the literal cone maps below.

For the positive canonical \(r\)-loop with \(\lambda=r^m\), set
\(j=m\). For the actual shorter positive \(w=r^3\)-loop with
\(\lambda=w^k\), set \(j=k\). On every \(T_n\) the complete
physical integer pair, index and native fixed-star free pair are
\[
\begin{aligned}
k_{M,n}&=2j-6j(n-1)^2,&\ell_{M,n}&=8j,\\
A_{M,n}&=-j(n-1)^2,&
(\mu_n,\rho_n)&=(2j,-6j(n-1)^2).
\end{aligned}
\]
The dual line \(U=M^*\) has the negative characteristic pair.
The actual oriented clutched-sphere class is
\(-j(n-1)^2\pmod {28}\) in the physical convention of P3K.68.
Formula (BW.30) gives the complete variation and stable-derivative
seed on the literal double parameter cover. The proof retains
both norm signs, every cap character, all full unit factors and
the actual shorter endpoint. It establishes these vertical-edge
fans and does not use the withdrawn universal fan polynomial.'''
out=ROOT/'notes/part3_os49_vertical_integer_seed.tex'
if out.exists():shutil.copy2(out,history/out.name)
status='Proved' if args.proved else 'Unresolved'
out.write_text(r'\subsection{The actual OS49 integer seed on every vertical-edge fan}'+'\n'+r'\begin{statement}{P3K.76}{'+status+'}\n'+statement+'\n'+r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+tex+'\n'+r'\par\medskip The exact certificate is \path{code/part3/bottom_row_winding.py}, with its saved JSON and captured output. It checks the complete period, line, seam, tangent, collar and named OS49 identities.'+'\n'+r'\end{proof}'+'\n')
preamble=(ROOT/'S6_06_BLIND_paper.tex').read_text().split(r'\begin{document}')[0]
(ROOT/'code/part3/k76_standalone.tex').write_text(preamble+'\n'+r'\begin{document}'+'\n'+r'\input{notes/part3_os49_vertical_integer_seed.tex}'+'\n'+r'\end{document}'+'\n')
(ROOT/'records/k76_export_manifest.json').write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'statement':'P3K.76','status':status,'include':str(out.relative_to(ROOT)),'include_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'preserved_prior':str(history.relative_to(ROOT)),'master_modified':False},indent=2)+'\n')
print(out.relative_to(ROOT),status)
