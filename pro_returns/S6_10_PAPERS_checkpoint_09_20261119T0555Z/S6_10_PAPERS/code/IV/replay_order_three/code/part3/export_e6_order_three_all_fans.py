#!/usr/bin/env python3
"""Complete K100 export, retaining the exact physical native and target maps."""
from pathlib import Path
import json,hashlib,re,subprocess
R=Path(__file__).resolve().parents[2]
source=R/'notes/part3_e6_order_three_all_fans_working.md'
expected='47b698d80e2ec7803f4d9f3f03f8dfe9e851db5fa8fa66a00010fb8ef2e2d965'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(source)==expected
peer=R/'records/checks_audit_e6_order_three_all_fans.json'
audit=json.loads(peer.read_text());assert audit['status']=='PASS_COMPLETE_OF_1_6' and audit['source_sha256']==expected
statement=r'''Retain the complete original source, line, selected-node order,
quadratic root cap, prescribed finite character and reference annular map
of P3K.99. Thus \((a,b;m)=(6,1;2)\), the norm is \(n=1\),
\(s=1/4-r\) makes one positive loop, the scalar is the fixed admitted
value of E87, and the physical line and orientation are those of P3K.68.

For \(P\in\operatorname{GL}_2(\mathbb Z)\), use the actual periodic fan
whose triangles, for \(v\in\mathbb Z^2\), are
\[
 \{v,v+Pe_1,v+Pe_2\},\qquad
 \{v+Pe_1,v+Pe_2,v+P(e_1+e_2)\}.
\]
Carry its complete character, period, Cox, physical-circle, line and
finite-cap maps specified in the proof. Put
\[
 (x,y)^t=P^{-1}(0,1)^t,\qquad S=x^2+xy+y^2.
\]
The actual oriented return on this selected fan is
\[
 [\Phi_P]=\left[-4+\frac{3(S-1)}2-\frac{27(S^2-1)}8\right]
       \quad\hbox{in }\Theta_7=\mathbb Z/28.
\]
The complete image over these fans is
\[
 \{0,3,4,5,7,10,11,12,14,17,18,19,21,24,25,26\}.
\]
On every vertical fan \(T_j=\left(\begin{smallmatrix}1&0\\j&1\end{smallmatrix}\right)\)
the full physical Jin pair is \((-27,-12)\), and the native relative
free pair in the displayed Hopf product is \((-3,-24)\). Its ordinary
data are \(V=\operatorname{diag}(27,0,0)\) and
\(\delta=(-21,0,0)\). The first fixed-edge flop has class zero.
All these statements use the same prescribed full reference and
fixed-scalar source loop.'''
body=source.read_text();body=body[body.index('## OF.1.'):]
body=re.sub(r'(?m)^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',body)
body=re.sub(r'`((?:code|records|notes)/[^`\n]+)`',lambda m:r'\path{'+m.group(1)+'}',body)
body=re.sub(r'(?<![\w/`{])((?:code|records|notes)/[A-Za-z0-9_./*+-]+)',lambda m:r'\path{'+m.group(1)+'}',body)
tex=subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex-superscript-subscript-smart','-t','latex','--wrap=preserve'],input=body,text=True,capture_output=True,check=True).stdout.replace(r'\tightlist','')
def outer(m):
 tags=re.findall(r'\\tag\{[^{}]*\}',m.group(2));assert len(tags)<=1
 s=re.sub(r'\\tag\{[^{}]*\}','',m.group(2))
 return r'\begin{aligned}'+s+r'\end{aligned}'+(' '+tags[0] if tags else '')
tex=re.sub(r'\\begin\{(split|aligned)\}([\s\S]*?)\\end\{\1\}',outer,tex)
out=R/'notes/part3_e6_order_three_all_fans.tex'
out.write_text(r'\subsection{The order-three source generator on every selected fan}'+'\n'+r'\begin{statement}{P3K.100}{Proved}'+'\n'+statement+'\n'+r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+tex+'\n'+r'\end{proof}'+'\n')
pre=(R/'S6_06_BLIND_paper.tex').read_text().split(r'\begin{document}')[0]
(R/'code/part3/k100_standalone.tex').write_text(pre+'\n'+r'\begin{document}'+'\n'+r'\input{notes/part3_e6_order_three_all_fans.tex}'+'\n'+r'\end{document}'+'\n')
(R/'notes/part3_e6_order_three_all_fans_statement.md').write_text('# P3K.100: the order-three source generator on every selected fan\n\n'+statement+'\n')
dependencies=['records/checks_audit_e6_order_three_all_fans.json','records/blind_audit_e6_order_three_native_products.json','code/part3_root/e6_order_three_fan_algebra.json','code/part3/e6_order_three_all_fans_peer.json','records/root_audit_e6_order_three_outer_transfer.json','records/k99_export_manifest.json']
manifest={'id':'P3K.100','status':'Proved; standalone QA pending','source':str(source.relative_to(R)),'source_sha256':expected,'include':str(out.relative_to(R)),'include_sha256':sha(out),'scope':'All selected lattice-basis fans of the exact P3K.99 fixed-scalar source loop; (6,1;2), n=1; original finite character and F0.','dependencies':[{'path':x,'sha256':sha(R/x)} for x in dependencies],'master_modified':False,'mapping_modified':False,'qa':'pending'}
(R/'records/k100_export_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'include':manifest['include'],'sha256':manifest['include_sha256'],'source_sha256':expected},indent=2))
