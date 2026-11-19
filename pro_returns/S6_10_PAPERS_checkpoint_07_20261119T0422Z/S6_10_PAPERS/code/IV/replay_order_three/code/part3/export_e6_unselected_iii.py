#!/usr/bin/env python3
"""Full K94 proof export; no master, report, or mapping mutation."""
from pathlib import Path
import hashlib,json,re,subprocess
R=Path(__file__).resolve().parents[2]
src=R/'notes/part3_e6_unselected_iii_working.md'
s=src.read_text()
local=s[s.index('Set \\(U='):s.index('The reduced IV-star root at infinity')]
local=local.replace('by y->-y','by \\(y\\mapsto-y\\)')
local=local.replace('For the line, M6 is','For the line, \\(M_6\\) is')
local=local.replace('and M6 has','and \\(M_6\\) has')
inline={
 'r=0':r'\(r=0\)', 'z=1/w':r'\(z=1/w\)',
 'y=xv,t=xu':r'\(y=xv,\ t=xu\)',
 'x=1/4-r':r'\(x=1/4-r\)', 'x=ta,y=tb':r'\(x=ta,\ y=tb\)',
 'a in (b-1)(b+1)':r'\(a\) in \((b-1)(b+1)\)',
 "x',y'":r"\(x',y'\)", "x'(G)=1/4-r":r"\(x'(G)=1/4-r\)",
 't=0':r'\(t=0\)', 'a=0,b=-1':r'\(a=0,\ b=-1\)',
 "(a',b')=(0,1)":r"\((a',b')=(0,1)\)",
 '6G-O':r'\(6G-O\)', '(1/4,-1/8)':r'\((1/4,-1/8)\)',
 '1+c kappa':r'\(1+c\kappa\)', 'kappa^2':r'\(\kappa^2\)',
 'I1 and I2':r'\(I_1\) and \(I_2\)',
}
parts=re.split(r'(\\\[.*?\\\]|\\\(.*?\\\))',local,flags=re.S)
for i in range(0,len(parts),2):
 for old,new in sorted(inline.items(),key=lambda kv:len(kv[0]),reverse=True):
  parts[i]=parts[i].replace(old,new)
local=''.join(parts)
body=s[s.index('## EU.1.'):]
body=re.sub(r'The preceding text is the preserved initial local calculation\..*?pre_full_attachment\.md`\.\n\n','The preceding source charts and the following full line and cap maps are used together. The initial local calculation remains in the preserved attempt record.\n\n',body,flags=re.S)
body=body.replace('This result is submitted for independent audit; no numbered statement\nor manuscript promotion is made here.','The preserved working history records the earlier local-only stage; the present proof retains the complete attachment.')
body='## EU.0. Actual source resolution and translation charts\n\n'+local+'\n'+body
cert=R/'code/part3/e6_unselected_iii.json'
data=json.loads(cert.read_text())
body+='\n## EU.7. Executed exact certificate\n\nThe independent symbolic chart certificate executes '+str(data['checks'])+' exact identities for the source addition, root translations, full Miller leading factors, finite averaging, signed annular cochains, and marked-cover weight cancellation. Its source is \\path{code/part3/e6_unselected_iii.py}; the complete output is \\path{code/part3/e6_unselected_iii.json}. The certificate supplements the complete geometric quotient and properness proof above.\n'
body=re.sub(r'(?m)^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',body)
body=re.sub(r'`((?:notes|records|code)/[^`]+)`',lambda m:r'\path{'+m.group(1)+'}',body)
tex=subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex-superscript-subscript-smart','-t','latex','--wrap=preserve'],input=body,text=True,capture_output=True,check=True).stdout.replace(r'\tightlist','')
statement=r'''Retain the actual source family
\[
 y^2=x^3+r x^2+t x+t^2,\qquad G=(0,t),\qquad M_6=\mathcal O(6G-O),
\]
on a small disc about \(r=0\), with the analytic branch \(\rho(0)=-1\), \(\rho^2=1-3r\), and selected whole \(I_1\) zero at \(t_c=(1-3\rho^2+2\rho^3)/27\). Use the exact rational Cartier suspension \(B_{\rm sel}=(t-t_c)B_6/t^3\) defined in the proof, with fixed sufficiently small nonzero scalar. At infinity retain the reduced quadratic \(IV^*\) cap, either primitive norm \(n=\pm1\), the prescribed character \((-1)^d\), and the entire reference annular map. There is no extra logarithmic disc at either colliding fibre. For every prescribed lattice-basis fan at the selected cusp, these actual source, line, root, cap and toric maps define a smooth proper oriented sphere family over the full \(r\)-disc, with identity parameter closing. Its positive boundary return is \(0\in\Theta_7\). Under the exact marked-cover rescaling \(D=w^2-3\), \(r=(3-2w^2)/D^2\), the same conclusion holds at both points \(w^2=3/2\), with the scalar unchanged and the same transported fan.'''
approved_source_sha='d704afdd5bf8be33d59535031ea5980c3dae40002cd045a1960d1e486018469f'
status='Proved' if hashlib.sha256(src.read_bytes()).hexdigest()==approved_source_sha else 'Unresolved'
out=R/'notes/part3_e6_unselected_iii.tex'
out.write_text('\\subsection{The E6 unselected-III disc and its actual zero return}\n\\begin{statement}{P3K.94}{'+status+'}\n'+statement+'\n\\end{statement}\n\\begin{proof}\n'+tex+'\n\\end{proof}\n')
pre=(R/'S6_06_BLIND_paper.tex').read_text().split(r'\begin{document}')[0]
(R/'code/part3/k94_standalone.tex').write_text(pre+'\n\\begin{document}\n\\input{notes/part3_e6_unselected_iii.tex}\n\\end{document}\n')
manifest={'status':status,'source':str(src.relative_to(R)),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'include':str(out.relative_to(R)),'include_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'certificate':str(cert.relative_to(R)),'checks':data['checks'],'master_modified':False,'report_modified':False,'mapping_modified':False,'pdf_qa':'pending'}
(R/'records/k94_export_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(manifest,indent=2))
