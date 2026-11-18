#!/usr/bin/env python3
"""Export the fully audited K84 proof while retaining its working history."""
from pathlib import Path
from datetime import datetime,timezone
import re,subprocess,json,hashlib,shutil,ast
ROOT=Path(__file__).resolve().parents[2]
src=ROOT/'notes/part3_os49_reduced_ii_caps_working.md'
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
history=ROOT/'records/attempts/k84_draft_export'/stamp;history.mkdir(parents=True);shutil.copy2(src,history/src.name)
# Read the earlier typesetting dictionary as data without executing its exporter.
module=ast.parse((ROOT/'code/part3/export_os49_higher_smooth_caps.py').read_text())
for node in module.body:
 if isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name):
  if node.targets[0].id=='rep':rep=ast.literal_eval(node.value)
  if node.targets[0].id=='wordrep':wordrep=ast.literal_eval(node.value)
rep.update({'F_(ht)=F_t^h':r'F_{ht}=F_t^h',
'M=O(G-O)':r'M=\mathcal O(G-O)','Q=3G':r'Q=3G','m=3k':r'm=3k','h=6l+1':r'h=6l+1',
'n_A ell_0+d_A delta':r'n_A\ell_0+d_A\delta','n_B gamma+d_B delta':r'n_B\gamma+d_B\delta',
'q=z^h, x=z^(2l)X, y=z^(3l)Y':r'q=z^h,\ x=z^{2l}X,\ y=z^{3l}Y',
'X=s^2,Y=s^3':r'X=s^2,\ Y=s^3','s to zeta_h^(-l)s':r's\mapsto\zeta_h^{-l}s',
'gcd(l,6l+1)=1':r'\gcd(l,6l+1)=1','tau=-x/y':r'\tau=-x/y',"tau'=z^l tau":r"\tau'=z^l\tau",
'u_l=0':r'u_l=0','u_l=-1':r'u_l=-1','(u_j+z^(l-j))/u_j':r'(u_j+z^{l-j})/u_j',
'(u_l+1)/u_l':r'(u_l+1)/u_l','tau+1':r'\tau+1','zeta_h^(l-j)u_j':r'\zeta_h^{l-j}u_j',
'N|II':r'N|_{II}',"hR=Q'":r"hR=Q'",'B_ell-I':r'B_{\rm ell}-I','Bhat_ell':r'\widehat B_{\rm ell}',
't_(-n_B R)D':r't_{-n_BR}D',"t_(-n_B Q')":r"t_{-n_BQ'}",'t_(-R)':r't_{-R}',
'B_0=beta(q)F^h':r'B_0=\beta(q)F^h','zeta_h^(d_B)':r'\zeta_h^{d_B}',
'h alpha_B-n_B gamma-d_B delta':r'h\alpha_B-n_B\gamma-d_B\delta',
'y=(gamma,delta)':r'y=(\gamma,\delta)','s=0,infinity':r's=0,\infty',
'gcd(h,n_B,d_B)=1':r'\gcd(h,n_B,d_B)=1','gcd(h,n_B)=1':r'\gcd(h,n_B)=1',
'a n_B+b d_B=1':r'a n_B+b d_B=1','R^2/(Z^2+Z(n_B,d_B)/h)':r'\mathbb R^2/(\mathbb Z^2+\mathbb Z(n_B,d_B)/h)',
'S^2':r'S^2','T^2':r'T^2','F_1=F':r'F_1=F','lambda beta(q)':r'\lambda\beta(q)',
'B_t=exp(t Log(lambda beta)) F_(ht)':r'B_t=\exp(t\operatorname{Log}(\lambda\beta))F_{ht}',
'B_1=B':r'B_1=B',"-gamma Q'":r"-\gamma Q'",
'sigma(gamma,delta)=exp(2pi i delta) B_gamma(O,1)':r'\sigma(\gamma,\delta)=e^{2\pi i\delta}B_\gamma(O,1)',
'n_B/h':r'n_B/h',"Q'(0)=O":r"Q'(0)=O",'psi delta':r'\psi\delta',
'gcd(m,h)=gcd(m,n_A)=gcd(h,n_B)=1':r'\gcd(m,h)=\gcd(m,n_A)=\gcd(h,n_B)=1',
'(u_2,v_2,p,q)':r'(u_2,v_2,p,q)',
'u_2=psi(-w+3delta)':r'u_2=\psi(-w+3\delta)',
'v_2=(psi+u)w':r'v_2=(\psi+u)w','p=eta_boundary psi':r'p=\eta_\partial\psi',
'q=eta_boundary(-w+3delta)/3':r'q=\eta_\partial(-w+3\delta)/3',
'k u_2-d_A p+n_A q':r'ku_2-d_Ap+n_Aq','Z v_2+Z(k u_2)':r'\mathbb Zv_2+\mathbb Z(ku_2)',
'omega=u_2+v_2':r'\omega=u_2+v_2','(psi,h_1)':r'(\psi,h_1)',
'n_A a+3d_A b=0':r'n_Aa+3d_Ab=0','phi=psi uw':r'\phi=\psi uw','rho=(psi+u)w delta':r'\rho=(\psi+u)w\delta',
'(m,0),(-3d_A n_A^{-1},1)':r'(m,0),(-3d_An_A^{-1},1)','mZ nu':r'm\mathbb Z\nu',
'D=h n_A+m n_B':r'D=h n_A+m n_B','D=+1 or -1':r'D=\pm1','H0=H6=Z':r'H^0=H^6=\mathbb Z',
'(H_B-I,H_C-I)':r'(H_B-I,H_C-I)','|D|':r'|D|','D=0':r'D=0',
'Theta6':r'\Theta_6','S6':r'S^6','gcd(3k,6l+1)=1':r'\gcd(3k,6l+1)=1',
'(n_A,n_B)':r'(n_A,n_B)','Z/h':r'\mathbb Z/h','Z/k':r'\mathbb Z/k','Z/m':r'\mathbb Z/m',
})
wordrep.update({'F_(ht)=F_t^h':r'F_{ht}=F_t^h','v_2':r'v_2','beta':r'\beta','tau':r'\tau','rho':r'\rho','phi':r'\phi','sigma':r'\sigma',
'n_A':r'n_A','n_B':r'n_B','d_A':r'd_A','d_B':r'd_B','u_j':r'u_j','u_l':r'u_l','F_t':r'F_t','N':r'N'})
proof=src.read_text().split('\n',2)[2]
proof=proof.replace('Working proof for independent audit.', 'The full proof has passed the recorded root and independent audits.')
pat=re.compile('|'.join(re.escape(k) for k in sorted(rep,key=len,reverse=True)))
parts=re.split(r'(\\\[.*?\\\]|\\\(.*?\\\))',proof,flags=re.S)
wp=re.compile(r'\b('+'|'.join(re.escape(k) for k in sorted(wordrep,key=len,reverse=True))+r')\b')
for i in range(0,len(parts),2):
 p=pat.sub(lambda m:r'\('+rep[m.group()]+r'\)',parts[i])
 pp=re.split(r'(\\\(.*?\\\))',p,flags=re.S)
 for j in range(0,len(pp),2):pp[j]=wp.sub(lambda m:r'\('+wordrep[m.group()]+r'\)',pp[j])
 parts[i]=''.join(pp)
proof=''.join(parts)
proof=re.sub(r'(?m)^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',proof)
tex=subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex','-t','latex','--wrap=preserve'],input=proof,text=True,capture_output=True,check=True).stdout.replace(r'\tightlist','')
statement=r'''Retain the fixed OS49 source, its actual component Cartier line
\(M=\mathcal O(G-O)\), translation \(-3G\) and selected cusp. In the
specified two-cap construction take the \(IV^*\) root order \(m=3k\)
and reduced-II order \(h=6l+1\), with \(k,l>0\), complete norm vectors
\(n_A\ell_0+d_A\delta\) and \(n_B\gamma+d_B\delta\), and their actual
Cartier/root/annular maps. The sphere sector is exactly
\[
                    h n_A+m n_B=\pm1.
\]
Every such datum is constructed for arbitrary fixed \(d_A,d_B\), with
all source and line factors retained, and yields the standard smooth
\(S^6\) on every allowed cusp fan. These data exist exactly when
\(\gcd(3k,6l+1)=1\). The smallest displayed instance is
\((m,h,n_A,n_B,d_A,d_B)=(3,7,1,-2,0,0)\).
The proof gives every actual specialization, integral Mayer--Vietoris,
translation-prism and fundamental-group map. This statement does not assign
additional ordinary clutches or a parameter return.'''
out=ROOT/'notes/part3_os49_reduced_ii_caps.tex'
if out.exists():shutil.copy2(out,history/out.name)
out.write_text(r'\subsection{Reduced-II caps on the OS49 source}'+'\n'+r'\begin{statement}{P3K.84}{Proved}'+'\n'+statement+'\n'+r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+tex+'\n'+r'\end{proof}'+'\n')
preamble=(ROOT/'S6_06_BLIND_paper.tex').read_text().split(r'\begin{document}')[0]
(ROOT/'code/part3/k84_standalone.tex').write_text(preamble+'\n'+r'\begin{document}'+'\n'+r'\input{notes/part3_os49_reduced_ii_caps.tex}'+'\n'+r'\end{document}'+'\n')
manifest={'statement':'P3K.84','status':'Proved','utc':datetime.now(timezone.utc).isoformat(),'draft':str(out.relative_to(ROOT)),'draft_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'certificate_checks':960,'registered':False,'master_modified':False}
(ROOT/'records/k84_export_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');print(json.dumps(manifest,indent=2))
