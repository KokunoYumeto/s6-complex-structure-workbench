#!/usr/bin/env python3
"""Export P3K.72 only, retaining its full actual-map proof and audit status."""
from pathlib import Path
from datetime import datetime,timezone
import re,subprocess,shutil,json,hashlib,argparse
p=argparse.ArgumentParser();p.add_argument('--proved',action='store_true');args=p.parse_args()
ROOT=Path(__file__).resolve().parents[2]
src=ROOT/'notes/part3_scalar_vertical_integer_seed_working.md'
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
history=ROOT/'records/attempts/k72_pre_export'/stamp;history.mkdir(parents=True)
shutil.copy2(src,history/src.name)
proof=src.read_text().split('## SI.1.',1)[1]
proof='## SI.1.'+proof
proof=re.sub(r'(?m)^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',proof)
proof=re.sub(r'`((?:code|notes|records)/[^`]+)`',lambda m:r'\path{'+m.group(1)+'}',proof)
tex=subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex','-t','latex','--wrap=preserve'],input=proof,text=True,capture_output=True,check=True).stdout
tex=tex.replace(r'\tightlist','')
statement=r'''Retain an actual fixed-source whole-\(I_1\) canonical scalar family
of K26, K28 or K32, its original source, Cartier line, finite caps and
complete ordinary forward closing \(q^e u(q)\). Its scalar winding is
\(J\), with positive canonical parameter \(\lambda=r^J\), and its
initial physical characteristic pair is
\((k_{M,0},\ell_{M,0})=(3H,24\chi)\) in the K68 convention.
Replace only the selected cusp fan by
\(T_n=T(e_1+ne_2,e_2)\), using the literal character and period maps
below. Then its actual integer characteristic data and native fixed-star
free coordinates are
\[
\begin{aligned}
k_{M,n}&=3H-3Jn(n-1),&\ell_{M,n}&=24\chi,\\
k_{U,n}&=-3H+3Jn(n-1),&\ell_{U,n}&=-24\chi,\\
A_{M,n}&=H/2-\chi-Jn(n-1)/2,\\
(m_0^{\rm native},n_0^{\rm native})
  &=(6\chi,3H-6\chi-3Jn(n-1)).
\end{aligned}
\]
Here \(M\) is the physical line and \(U=M^*\) is its meridian-one
dual. Formula (SI.36) gives the full integer variation and derivative
seed in the literal doubled ordinary product. All full-unit maps,
annular integers and finite-cap factors are retained. This statement
concerns the specified canonical closing and its literal covers; it
does not include a new shorter source-translation endpoint or an OS49
component-supported construction.'''
out=ROOT/'notes/part3_scalar_vertical_integer_seed.tex'
if out.exists():shutil.copy2(out,history/out.name)
status='Proved' if args.proved else 'Unresolved'
out.write_text(r'\subsection{The complete integer scalar seed on the vertical-edge fans}'+'\n'+r'\begin{statement}{P3K.72}{'+status+'}\n'+statement+'\n'+r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+tex+'\n'+r'\par\medskip The exact certificate is \path{code/part3/scalar_vertical_integer_seed.py}, with its saved JSON, output and full-unit scope.'+'\n'+r'\end{proof}'+'\n')
preamble=(ROOT/'S6_06_BLIND_paper.tex').read_text().split(r'\begin{document}')[0]
(ROOT/'code/part3/k72_standalone.tex').write_text(preamble+'\n'+r'\begin{document}'+'\n'+r'\input{notes/part3_scalar_vertical_integer_seed.tex}'+'\n'+r'\end{document}'+'\n')
(ROOT/'records/k72_export_manifest.json').write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'statement':'P3K.72','status':status,'include':str(out.relative_to(ROOT)),'include_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'preserved_prior':str(history.relative_to(ROOT)),'master_modified':False},indent=2)+'\n')
print(out.relative_to(ROOT),status)
