#!/usr/bin/env python3
"""Reconstructed exports; no central master, report, or mapping writes."""
from pathlib import Path
import re,json,subprocess,hashlib,ast
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[2]
rep={}
for file in ['export_os49_higher_smooth_caps.py','export_os49_reduced_ii_caps.py']:
 p=R/'code/part3'/file
 for n in ast.parse(p.read_text()).body:
  if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id=='rep':
   try:rep.update(ast.literal_eval(n.value))
   except Exception:pass
  if isinstance(n,ast.Expr) and isinstance(n.value,ast.Call) and isinstance(n.value.func,ast.Attribute) and isinstance(n.value.func.value,ast.Name) and n.value.func.value.id=='rep' and n.value.func.attr=='update':
   rep.update(ast.literal_eval(n.value.args[0]))
rep.update({'lambda=r^M':r'\lambda=r^M','m=3k,h=6l+1':r'm=3k,\ h=6l+1','M=mh':r'M=mh','chi=k(3l+1)':r'\chi=k(3l+1)','A0=3kl':r'A_0=3kl','epsilon=+/-1':r'\epsilon=\pm1','gamma_B':r'\gamma_B','gamma_out':r'\gamma_{\rm out}','delta':r'\delta','epsilon':r'\epsilon','lambda':r'\lambda','theta':r'\theta','sigma':r'\sigma','beta':r'\beta','alpha':r'\alpha','kappa':r'\kappa','rho':r'\rho','eta':r'\eta','chi':r'\chi','psi':r'\psi','tau':r'\tau','ell_0':r'\ell_0','n_A':r'n_A','n_B':r'n_B','d_A':r'd_A','d_B':r'd_B','y_B':r'y_B','u_B':r'u_B','u_out':r'u_{\rm out}','q_H':r'q_H','T_n':r'T_n','U=M*':r'U=M^*','B_0':r'B_0','F_t':r'F_t','C_r':r'C_r'})
keys=re.compile(r'(?<![A-Za-z0-9_\\])(?:'+'|'.join(re.escape(k) for k in sorted(rep,key=len,reverse=True))+r')(?![A-Za-z0-9_])')
def convert(s):
 parts=re.split(r'(\\\[.*?\\\]|\\\(.*?\\\))',s,flags=re.S)
 for j in range(0,len(parts),2):
  parts[j]=keys.sub(lambda m:r'\('+rep[m.group()]+r'\)',parts[j])
 s=''.join(parts)
 s=re.sub(r'(?<![A-Za-z])((?:notes|records|code)/[A-Za-z0-9_./-]+)',lambda m:r'\path{'+m.group(1)+'}',s)
 s=re.sub(r'(?m)^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',s)
 t=subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex-superscript-subscript-smart','-t','latex','--wrap=preserve'],input=s,text=True,capture_output=True,check=True).stdout
 return t.replace(r'\tightlist','')
statements={85:r'''Keep the actual OS49 source, Cartier line and two caps of P3K.84, with \(m=3k\), \(h=6l+1\), \(k,l>0\), \(hn_A+mn_B=\epsilon=\pm1\), and arbitrary retained \(d_A,d_B\). For the canonical full positive \(r\)-loop \(\lambda=r^{mh}\), the positive fan \(T_1\) has physical characteristic pair and return
\[(k_M,\ell_M)=(6kh,24k(3l+1)),\qquad A_M=3kl\pmod {28}.\]
The proof retains the actual solid-torus quotients, both root actions, the corrected contracting/outward/Hopf coordinates, the complete page line and the physical dual-line gluing. The smallest tuple \((3,7,1,-2,0,0)\) gives \((42,96)\) and class \(3\).''',87:r'''For the named two-cap OS49 sphere data of P3K.84--85, set \(M=mh\), \(\chi=k(3l+1)\), \(A_0=3kl\). On the vertical fan \(T_n\), the canonical full \(r\)-loop has
\[(k_{M,n},\ell_{M,n})=(2M-6M(n-1)^2,24\chi),\qquad [\Phi_{T_n}]=A_0-M(n-1)^2\pmod {28}.\]
The exact full-unit Cox algorithm in the proof computes its physical return on every lattice-basis cusp fan. The smallest source/cap tuple \((3,7,1,-2,0,0)\) realizes every element of \(\Theta_7\) through the listed explicit fans. The statement retains the canonical full \(r\)-loop; its actual shorter endpoints are treated in P3K.91.''',91:r'''Retain a fixed OS49 source and the two actual finite caps of P3K.84, on any lattice-basis fan, together with finitely many marked smooth order-one clutches. Put \(m=3k\), \(h=6l+1\), \(M=mh\), and \(D=hn_A+mn_B+M\sigma=\epsilon=\pm1\). Their full integral root-groupoid class is \((D,d_A\bmod k,d_B\bmod h)\) in \(\mathbb Z\oplus\mathbb Z/k\oplus\mathbb Z/h\). The explicit family isomorphism redistributes the ordinary clutches to the canonical two-cap datum, retaining both finite characters and all annular integers. Every holomorphic endpoint is covered by the actual physical scalar action; the minimum positive scalar winding is \(kh\). The constructed parameter \(w=r^3\), \(\lambda=w^{kh}\), has positive-fan physical pair \((2kh,8k(3l+1))\) and return \(kl\). On every fan, use the P3K.87 algorithm with \(M=kh\), \(A_0=kl\); an endpoint of winding \(Nkh\) has \(N\) times that return. The proof constructs the endpoint and native cover maps before using integral characteristic naturality.'''}
base={85:'part3_os49_reduced_ii_return',87:'part3_os49_reduced_ii_all_fans',91:'part3_os49_reduced_ii_endpoints'}
preamble=(R/'S6_06_BLIND_paper.tex').read_text().split(r'\begin{document}')[0]
manifest={'recovery':'mathematical reconstruction, not byte replay','utc':datetime.now(timezone.utc).isoformat(),'master_modified':False,'report_modified':False,'mapping_modified':False,'exports':{}}
for k,b in base.items():
 src=R/'notes'/(b+'_working.md');text=src.read_text();body=text[text.index('## '):]
 out=R/'notes'/(b+'.tex')
 title={85:'The actual reduced-II page and physical return',87:'Reduced-II returns on every cusp fan',91:'The complete reduced-II groupoid and holomorphic endpoints'}[k]
 t='\\subsection{'+title+'}\n\\begin{statement}{P3K.'+str(k)+'}{Proved}\n'+statements[k]+'\n\\end{statement}\n\\begin{proof}\n'+convert(body)+'\n\\end{proof}\n'
 if k==87:t+='\\input{notes/part3_os49_reduced_ii_fan_witness_table.tex}\n'
 if k==85:
  t=t.replace(r"u=(2s,s)^t+U(q),\quad\gamma_B=(-3s,-s+Mv)^t+C(q),"+"\n"+r"\quad H=-u-\gamma_B,\quad K=3u+2\gamma_B=\mathcal D+(s+2Mv)\delta,",r"\begin{gathered}u=(2s,s)^t+U(q),\quad\gamma_B=(-3s,-s+Mv)^t+C(q),\\"+"\n"+r"H=-u-\gamma_B,\quad K=3u+2\gamma_B=\mathcal D+(s+2Mv)\delta.\end{gathered}")
  t=t.replace(r'\end{proof}',r'\qedhere'+'\n'+r'\end{proof}')
 if k==87:
  t=t.replace(r'A_{L,J}=dd+(\alpha_q+J\theta)d\gamma+L\theta dv,',r'\begin{gathered}A_{L,J}=dd+(\alpha_q+J\theta)d\gamma+L\theta dv,\\')
  t=t.replace(r'\quad A_n=dd_n+(\alpha_q+J\theta)d\gamma_n+(L+nJ)\theta dv,',r'A_n=dd_n+(\alpha_q+J\theta)d\gamma_n+(L+nJ)\theta dv,\\')
  t=t.replace(r'\quad\beta_n=A_n-A_{ext}=-n(du+\alpha_qdv).',r'\beta_n=A_n-A_{ext}=-n(du+\alpha_qdv).\end{gathered}')
  t=t.replace(r"(x,y)^t=(P')^{-1}e_2,\quad w=(x,y,-x-y),\quad",r"\begin{gathered}(x,y)^t=(P')^{-1}e_2,\quad w=(x,y,-x-y),\\")
  t=t.replace(r'd=(-x-2y,-2x-y,x-y),\quad',r'd=(-x-2y,-2x-y,x-y),\\')
  t=t.replace(r'I_i=t_0w_i+d_i(\lambda_i-t_0),\quad W_i=t_0w_i-d_i(\lambda_i-t_0).',r'I_i=t_0w_i+d_i(\lambda_i-t_0),\quad W_i=t_0w_i-d_i(\lambda_i-t_0).\end{gathered}')
 out.write_text(t)
 (R/'code/part3'/f'k{k}_standalone.tex').write_text(preamble+'\n\\begin{document}\n\\input{notes/'+b+'.tex}\n\\end{document}\n')
 manifest['exports'][str(k)]={'source':str(src.relative_to(R)),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'include':str(out.relative_to(R)),'include_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'pdf_qa':'new build pending; historical QA not reused'}
d=json.loads((R/'code/part3/os49_reduced_ii_all_fans.json').read_text())
lines=[r'\par\medskip\noindent\textbf{Explicit smallest-family witnesses.}',r'\begin{longtable}{r r r l r}',r'Class & Basis $(p,-r;q,s)$ & Seed & Word & Integer sum\\\hline']
for w in d['smallest_family_witnesses']:
 a,b,c,e=w['input_basis'];word=''.join(str(i) for i in w['word']) or r'\varnothing'
 lines.append(f"{w['physical_class_mod28']} & $({a},{b};{c},{e})$ & {w['vertical_index']} & ${word}$ & {w['integer_path_sum']}\\\\")
lines.append(r'\end{longtable}');(R/'notes/part3_os49_reduced_ii_fan_witness_table.tex').write_text('\n'.join(lines)+'\n')
# Corrected OC retains the checkpoint19 Refuted statement verbatim.
p=R/'notes/part3_os49_full_framing.tex';prefix=p.read_text().split(r'\begin{proof}')[0]
s=(R/'notes/part3_os49_full_framing_working.md').read_text();p.write_text(prefix+'\\begin{proof}\n'+convert(s[s.index('## '):] if '## ' in s else s.split('\n',2)[2])+'\n\\end{proof}\n')
(R/'code/part3/k34_standalone.tex').write_text(preamble+'\n\\begin{document}\n\\input{notes/part3_os49_full_framing.tex}\n\\end{document}\n')
(R/'records/post19_blind_export_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(manifest,indent=2))
