#!/usr/bin/env python3
"""Export the complete audited P3K.78 proof without changing master inputs."""
from pathlib import Path
from datetime import datetime, timezone
import subprocess, re, shutil, json, hashlib
ROOT=Path(__file__).resolve().parents[2]
src=ROOT/'notes/part3_os49_order_one_clutches_working.md'
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
history=ROOT/'records/attempts/k78_pre_export'/stamp
history.mkdir(parents=True)
shutil.copy2(src,history/src.name)
proof='## OCS.1.'+src.read_text().split('## OCS.1.',1)[1]
proof=re.sub(r'(?m)^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',proof)
proof=re.sub(r'`((?:code|notes|records)/[^`]+)`',lambda m:r'\path{'+m.group(1)+'}',proof)
tex=subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex','-t','latex','--wrap=preserve'],input=proof,text=True,capture_output=True,check=True).stdout.replace(r'\tightlist','')
statement=r'''Retain the fixed OS49 source
\[
y^2=x^3-3t^3(t-1)x+2t^4(t-1)(t-\tfrac12),\qquad G=(t^2,t^2),
\]
the actual Cartier line \(M=\mathcal O(G-O)\), suspension over
\(-3G\), retained type-II fibre at \(1\), selected component cusp
at infinity, and good \(IV^*\) cap at \(0\). Let the finite cap
have order \(m=3k>0\), invariant vector \(n\ell_0+d\delta\), and
an actual free action as in P3F.33, where
\(\ell_0=(1,-1,0,0)^t\). Fix any periodic index-one lattice-basis
fan \(P\), with the original source, line, root and annular markings.

At finitely many fixed, marked, disjoint smooth-site discs, retain
ordinary-to-disc translation clutches and their full line lifts
\[
 \Phi_i(x,z_i)=x+\frac{\log z_i}{2\pi i}\Pi(z_i)\ell_i+u_i(z_i),
 \qquad \ell_i\in\Lambda=\mathbb Z^4.                 \tag{OCS.1}
\]
Here every vector is transported along its marked cut, and every
single-valued Lie term \(u_i\), including its line component and
annular units, is retained. In the basis \((\gamma,u,w,\delta)\), put
\[
 \psi=(1,0,0,0),\qquad
 \sigma=\sum_i\psi(\ell_i),\qquad D=n+m\sigma.        \tag{OCS.2}
\]

The complete integral extending-period groupoid has
\(H^2(\mathcal H)=\mathbb Z\oplus\mathbb Z/k\), with these data
represented by \((D,d\bmod k)\). The explicit integral cochain
and actual holomorphic maps below identify the entire clutched
family, on the same fan and at the same scalar, with the one-cap
datum \((m,D,d)\). They retain every finite group cochain and the
actual parameter-closing maps. Its fundamental group is
\(\mathbb Z/|D|\), with \(D=0\) interpreted as \(\mathbb Z\), and
its sphere members are exactly \(D=\pm1\).

For the canonical positive \(r\)-loop \(\lambda=r^m\) in this
sphere sector, the oriented physical return is \(S_m(P)\) of
P3K.77. Transporting the actual shorter OR65 endpoint by the
constructed family map gives the shorter return \(S_k(P)\),
with its full three-step norm. This last assertion concerns that
specified transported endpoint. The theorem retains fixed smooth
order-one sites, the fixed source and its stated singular models;
it makes no assertion about an additional unspecified short-loop
identification or a change of source.'''
out=ROOT/'notes/part3_os49_order_one_clutches.tex'
if out.exists(): shutil.copy2(out,history/out.name)
out.write_text(r'\subsection{OS49 smooth order-one clutches and their actual return comparison}'+'\n'+r'\begin{statement}{P3K.78}{Proved}'+'\n'+statement+'\n'+r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+tex+'\n'+r'\end{proof}'+'\n')
preamble=(ROOT/'S6_06_BLIND_paper.tex').read_text().split(r'\begin{document}')[0]
wrapper=ROOT/'code/part3/k78_standalone.tex'
wrapper.write_text(preamble+'\n'+r'\begin{document}'+'\n'+r'\input{notes/part3_os49_order_one_clutches.tex}'+'\n'+r'\end{document}'+'\n')
manifest={'utc':datetime.now(timezone.utc).isoformat(),'statement':'P3K.78','status':'Proved','include':str(out.relative_to(ROOT)),'include_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'preserved_prior':str(history.relative_to(ROOT)),'master_modified':False}
(ROOT/'records/k78_export_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(manifest,indent=2))
