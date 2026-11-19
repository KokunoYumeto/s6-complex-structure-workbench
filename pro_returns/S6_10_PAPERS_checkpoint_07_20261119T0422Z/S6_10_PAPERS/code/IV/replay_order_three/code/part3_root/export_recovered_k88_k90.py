"""Export the reconstructed complete K88/K90 proof sources for fresh PDF QA."""
from pathlib import Path
import subprocess,re,json,hashlib
ROOT=Path(__file__).resolve().parents[2]
specs=[(88,'source_zero_base_sector','ZB.1.','The fixed-scalar source-zero return in the initial sector',r'''For the actual E7 source-zero loop with fixed scalar, both marked
branches \((a,b)=(1,2),(2,1)\), every retained cap datum and every fan
obtained from \(T_0\) by a word beginning \(Q_0\) and continuing in
\(Q_0,Q_1\), equations (ZB.5)--(ZB.10) compute its exact physical
return in the K68 convention. Each branch attains every class of
\(\Theta_7=\mathbb Z/28\); the two tables below give all 28 actual
fan witnesses for each branch. The initial free normal correction
is the complete \(\Gamma=0\) of K86.'''),
(90,'source_zero_all_fans','ZA.1.','The actual source-zero return on every lattice-basis fan',r'''For the actual E7 source-zero family and marked data of ZA.1,
\(a=1,2\), \(b=3-a\), \(p\ge1\), \(k\ge0\), and every
\(P\in GL_2(\mathbb Z)\), the terminating construction
(ZA.4)--(ZA.12) gives the physical positive-loop return
\(S\bmod28\) with its full source, Cartier, cap and closing maps.
The vertical seed has physical pair
\((\mu+6A_j,4\mu)\), where
\[
\mu=2-a+6pk,\qquad
A_j=2b\binom{j+1}{3}+(3-b)\binom{j+1}{2}
+k(a-1)(3p-1)-k(4p-a+1)\binom j2.
\]
All free integral matrices and derivatives are computed before
reduction. Both fixed-scalar branches attain every element of
\(\Theta_7\) by the full K88 witnesses.''')]
preamble=(ROOT/'S6_06_BLIND_paper.tex').read_text().split(r'\begin{document}')[0]
records=[]
for number,stem,heading,title,claim in specs:
    src=ROOT/f'notes/part3_{stem}_working.md';raw=src.read_text()
    proof='## '+heading+raw.split('## '+heading,1)[1]
    proof=re.sub(r'(?m)^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nopagebreak[4]',proof)
    proof=re.sub(r'`((?:code|notes|records)/[^`]+)`',lambda m:r'\path{'+m.group(1)+'}',proof)
    tex=subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex','-t','latex','--wrap=preserve'],input=proof,text=True,capture_output=True,check=True).stdout.replace(r'\tightlist','')
    out=ROOT/f'notes/part3_{stem}.tex'
    out.write_text(r'\subsection{'+title+'}\n'+r'\begin{statement}{P3K.'+str(number)+r'}{Proved}'+'\n'+claim+'\n'+r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+tex+'\n'+r'\end{proof}'+'\n')
    standalone=ROOT/f'code/part3_root/k{number}_standalone.tex'
    standalone.write_text(preamble+'\n'+r'\begin{document}'+'\n'+r'\input{'+str(out.relative_to(ROOT))+'}\n'+r'\end{document}'+'\n')
    rec={'statement':f'P3K.{number}','reconstruction':True,'old_bytes_restored':False,'source':str(src.relative_to(ROOT)),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'include':str(out.relative_to(ROOT)),'include_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'master_modified':False,'new_visual_QA':'pending'}
    (ROOT/f'records/k{number}_export_manifest.json').write_text(json.dumps(rec,indent=2)+'\n');records.append(rec)
print(json.dumps(records,indent=2))
