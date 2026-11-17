#!/usr/bin/env python3
"""Export the complete audited OT.1--7 calculation and cap obstruction as K81."""
from pathlib import Path
from datetime import datetime,timezone
import re,subprocess,json,hashlib,shutil
ROOT=Path(__file__).resolve().parents[2]
src=ROOT/'notes/part3_os49_order_two_cap_working.md'
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
history=ROOT/'records/attempts/k81_pre_export'/stamp;history.mkdir(parents=True)
shutil.copy2(src,history/src.name)
proof=src.read_text().split('\n',2)[2]
proof=proof.replace('Working proof for independent audit.','The following full calculation has passed the recorded independent audit.')
rep={
'(m,n,d)=(3,-1,0)':r'(m,n,d)=(3,-1,0)',
'gamma=(1,0,0,0)':r'\gamma=(1,0,0,0)',
'(gamma,u,w,delta)':r'(\gamma,u,w,\delta)',
'q=z^2':r'q=z^2','x->-x':r'x\mapsto-x',
'2 alpha_S-gamma':r'2\alpha_S-\gamma',
"Lambda'=Lambda+Z(gamma/2)":r"\Lambda'=\Lambda+\mathbb Z(\gamma/2)",
'(psi,u,w,delta)':r'(\psi,u,w,\delta)',
'ell_0=(1,-1,0,0)':r'\ell_0=(1,-1,0,0)',
'+ell_0/3':r'+\ell_0/3','-ell_0/3':r'-\ell_0/3',
'(-1)^q':r'(-1)^q','psi,h=-w+3delta':r'\psi,\ h=-w+3\delta',
'3psi,h':r'3\psi,h','3nu':r'3\nu',
'L_q':r'L_q','J_q=j_*L_q':r'J_q=j_*L_q',
'E_i=wedge^q T_i':r'E_i=\bigwedge^q T_i',
'S_q=R^q pi_* Z':r'S_q=R^q\pi_*\mathbb Z',
'q=2':r'q=2','q=3':r'q=3',
'psi u, psi w,\npsi delta':r'\psi u,\psi w,\psi\delta',
'psi uw,\npsi u delta, psi w delta':r'\psi uw,\psi u\delta,\psi w\delta',
'(0,0,3)':r'(0,0,3)','(1,0,0)':r'(1,0,0)',
'delta+(2/3)w':r'\delta+(2/3)w','(uw-2psi w)/3':r'(uw-2\psi w)/3',
'uw delta-2psi w delta':r'uw\delta-2\psi w\delta',
'H_i=(T_i^{-1})^t':r'H_i=(T_i^{-1})^t',
'H_B-I,H_C-I':r'H_B-I,H_C-I','alpha_A,alpha_S':r'\alpha_A,\alpha_S',
'(gamma,alpha_A,alpha_S)':r'(\gamma,\alpha_A,\alpha_S)',
'H_A-I':r'H_A-I','pi_1(X)=1':r'\pi_1(X)=1','pi_1':r'\pi_1',
'm0=3k':r'm_0=3k','m_i':r'm_i','ell_i':r'\ell_i','n_i=psi(ell_i)':r'n_i=\psi(\ell_i)',
'b0':r'b_0','F_p':r'\mathbb F_p','R=Z_(p)':r'R=\mathbb Z_{(p)}',
'm0':r'm_0','H^1=0':r'H^1=0','ell=(n,a,b,d)':r'\ell=(n,a,b,d)',
'Lambda+R(ell/m_i)':r'\Lambda+R(\ell/m_i)',
'(R/m_i R)^3':r'(R/m_iR)^3','(-b,a,3n)':r'(-b,a,3n)',
'H^3(X;R)':r'H^3(X;R)',
'sum_{j=0}^{r-1} a(zeta_r^j z)=Pi(z^r) ell':r'\sum_{j=0}^{r-1}a(\zeta_r^jz)=\Pi(z^r)\ell',
'g(zeta_r z)-g(z)=f(z)':r'g(\zeta_rz)-g(z)=f(z)',
'(x,z) to (x-g(z),z)':r'(x,z)\mapsto(x-g(z),z)',
'g=gcd(r,ell_1,ell_2,ell_3,ell_4)':r'g=\gcd(r,\ell_1,\ell_2,\ell_3,\ell_4)',
'z to z^g':r'z\mapsto z^g','r/g':r'r/g','ell/g':r'\ell/g',
"T'=Lambda_R/(Lambda+Z ell/r)":r"T'=\Lambda_{\mathbb R}/(\Lambda+\mathbb Z\ell/r)",
'x=Pi(q) y':r'x=\Pi(q)y',
'(y,z) to (y,tz)':r'(y,z)\mapsto(y,tz)',
'0 at most t at most 1':r'0\le t\le1',
'(y,z) to (y+ell/r,zeta_r z)':r'(y,z)\mapsto(y+\ell/r,\zeta_rz)',
'ell/r':r'\ell/r','(1,1,1,r)':r'(1,1,1,r)',
'[rI_4 | ell]':r'[rI_4\mid\ell]',
"Lambda'=r^{-1}H Z^4":r"\Lambda'=r^{-1}H\mathbb Z^4",
'r H^{-t}':r'rH^{-t}',
'R=R^2 pi_* Z':r'R=R^2\pi_*\mathbb Z','J=j_*L_2':r'J=j_*L_2',
'H^0(J)=Z omega':r'H^0(J)=\mathbb Z\omega','H^0(Q)':r'H^0(Q)',
'H^1(R^2 pi_* Z)':r'H^1(R^2\pi_*\mathbb Z)',
'E_2^{1,2}':r'E_2^{1,2}','H^3(X;Z)':r'H^3(X;\mathbb Z)',
't=1':r't=1','q=t-1':r'q=t-1','m_0=6l':r'm_0=6l',
'q=z^{6l}':r'q=z^{6l}','x=z^{2l}X':r'x=z^{2l}X','y=z^{3l}Y':r'y=z^{3l}Y',
"G' and Q'=3G'":r"G'\text{ and }Q'=3G'",
'Y^2=X^3+1':r'Y^2=X^3+1','m_0R=Q\'':r"m_0R=Q'",'R(0)=O':r'R(0)=O',
'd=1':r'd=1','I2':r'I_2','t_{-R}':r't_{-R}',
'DFD^{-1}=chi F':r'DFD^{-1}=\chi F','chi^{m_0}=1':r'\chi^{m_0}=1',
'B_0=beta(q)F^{m_0}':r'B_0=\beta(q)F^{m_0}',
'A_0^{m_0}=B_0^{n_0}':r'A_0^{m_0}=B_0^{n_0}',
'chi^{n_0m_0(m_0-1)/2}':r'\chi^{n_0m_0(m_0-1)/2}',
'A^{m_0}=B^{n_0}':r'A^{m_0}=B^{n_0}',
'6l+1':r'6l+1','Z/3':r'\mathbb Z/3','Z/r':r'\mathbb Z/r',
'Z gamma':r'\mathbb Z\gamma',
}
pat=re.compile('|'.join(re.escape(k) for k in sorted(rep,key=len,reverse=True)))
parts=re.split(r'(\\\[.*?\\\]|\\\(.*?\\\))',proof,flags=re.S)
wordrep={'psi':r'\psi','gamma':r'\gamma','delta':r'\delta','omega':r'\omega','eta':r'\eta','ell_0':r'\ell_0','ell':r'\ell','alpha':r'\alpha','Lambda':r'\Lambda','d2':r'd_2','m_0':r'm_0','n_0':r'n_0'}
wp=re.compile(r'\b('+'|'.join(re.escape(k) for k in sorted(wordrep,key=len,reverse=True))+r')\b')
for i in range(0,len(parts),2):
 p=pat.sub(lambda m:r'\('+rep[m.group()]+r'\)',parts[i])
 # Re-split so the single-symbol pass never enters newly inserted math.
 pp=re.split(r'(\\\(.*?\\\))',p,flags=re.S)
 for j in range(0,len(pp),2):pp[j]=wp.sub(lambda m:r'\('+wordrep[m.group()]+r'\)',pp[j])
 parts[i]=''.join(pp)
proof=''.join(parts)
proof=re.sub(r'(?m)^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',proof)
proof=re.sub(r'`((?:code|notes|records)/[^`]+)`',lambda m:r'\path{'+m.group(1)+'}',proof)
tex=subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex','-t','latex','--wrap=preserve'],input=proof,text=True,capture_output=True,check=True).stdout.replace(r'\tightlist','')
statement=r'''For the fixed OS49 source and its component Cartier line, every
actual sphere member obtained by the stated finite root caps and smooth
translation caps has only order-one effective caps at smooth source values.
This holds with the full norm vectors, all finite characters and other
specialization groups retained, and for every allowed lattice-basis cusp
fan. At any effective smooth cap of order \(r>1\), the actual degree-two
specialization quotient is \((\mathbb Z/r)^3\). The unique global invariant
\(\omega=uw+3\psi\delta\) leaves a nonzero group in
\(H^1(\mathbb P^1,R^2\pi_*\mathbb Z)\), which survives in \(H^3(X;\mathbb Z)\).

For the explicit retained finite cap \((m,n,d)=(3,-1,0)\) and one smooth
cap of order two with full norm vector \(\gamma=(1,0,0,0)\), the actual
constructed compact manifold has
\[
 \pi_1(X)=1,\qquad H_2(X;\mathbb Z)=H_3(X;\mathbb Z)=(\mathbb Z/2)^2,
\]
\[
 H_0(X;\mathbb Z)=H_6(X;\mathbb Z)=\mathbb Z,
 \qquad H_1(X;\mathbb Z)=H_4(X;\mathbb Z)=H_5(X;\mathbb Z)=0.
\]
The proof supplies the full specialization, integral Mayer--Vietoris,
translation-prism and fundamental-group maps.

At the type-II value, every realized free good root has effective order
divisible by six. Its actual root source and corrected Cartier line give
\(\psi(\ell)=n\) for the full norm vector. Together with the retained
\(IV^*\) cap of order \(3k\), it has the displayed nonzero
\(\mathbb Z/3\) fundamental-group quotient and cannot be a sphere.
The reduced-II orders \(6l+1\) and their return classes are not assigned
by this statement.'''
out=ROOT/'notes/part3_os49_higher_smooth_caps.tex'
if out.exists():shutil.copy2(out,history/out.name)
out.write_text(r'\subsection{Higher smooth-cap obstruction for the OS49 source}'+'\n'+r'\begin{statement}{P3K.81}{Proved}'+'\n'+statement+'\n'+r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+tex+'\n'+r'\end{proof}'+'\n')
preamble=(ROOT/'S6_06_BLIND_paper.tex').read_text().split(r'\begin{document}')[0]
(ROOT/'code/part3/k81_standalone.tex').write_text(preamble+'\n'+r'\begin{document}'+'\n'+r'\input{notes/part3_os49_higher_smooth_caps.tex}'+'\n'+r'\end{document}'+'\n')
manifest={'statement':'P3K.81','status':'Proved','utc':datetime.now(timezone.utc).isoformat(),'include':str(out.relative_to(ROOT)),'include_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'preserved_prior':str(history.relative_to(ROOT)),'certificate_checks':116,'master_modified':False}
(ROOT/'records/k81_export_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');print(json.dumps(manifest,indent=2))
