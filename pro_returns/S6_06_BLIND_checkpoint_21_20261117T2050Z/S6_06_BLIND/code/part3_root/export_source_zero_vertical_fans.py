"""Export the independently audited complete vertical source-zero comparison."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,subprocess,shutil

root=Path(__file__).resolve().parents[2]
src=root/'notes/part3_source_zero_vertical_fans_working.md'
audit=json.loads((root/'records/fourfold_audit_source_zero_vertical_fans.json').read_text())
assert audit['status']=='PASS'
raw=src.read_text();proof='## ZV.1.'+raw.split('## ZV.1.',1)[1]
rep={
 '(Z,V,q) to (Z_j,V_j,q)=(Z,Z^-j V,q)':r'(Z,V,q)\mapsto(Z_j,V_j,q)=(Z,Z^{-j}V,q)',
 'h_j=hB^j':r'h_j=hB^j','B_j=B':r'B_j=B',
 'P_j^-1 W P_j':r'P_j^{-1}WP_j','L0=nu k':r'L_0=\nu k',
 '(Z,V) to\n(Z,q^L0 V)':r'(Z,V)\mapsto(Z,q^{L_0}V)',
 'B^-L0':r'B^{-L_0}',
 '(g_j^-L0 Z_j,eta_j^-L0 V_j)':r'(g_j^{-L_0}Z_j,\eta_j^{-L_0}V_j)',
 'G_j=log(g_j), H_j=log(eta_j)':r'G_j=\log g_j,\ H_j=\log\eta_j',
 'A=exp(L0 chi G_j), D=exp(L0 chi H_j)':r'A=e^{L_0\chi G_j},\ D=e^{L_0\chi H_j}',
 'ell=0,1':r'\ell=0,1','C_tau E_tau^-ell':r'C_\tau E_\tau^{-\ell}',
 'diag(eta_j/alpha_j,kappa_j alpha_j)':r'\operatorname{diag}(\eta_j/\alpha_j,\kappa_j\alpha_j)',
 'diag(kappa_j/g_j,g_j eta_j)':r'\operatorname{diag}(\kappa_j/g_j,g_j\eta_j)',
 'diag(eta_j,kappa_j)':r'\operatorname{diag}(\eta_j,\kappa_j)',
 'H_t Q H_(l_i-t)':r'H_t Q H_{l_i-t}',
 'w=(0,1,-1) and d=(-2,-1,-1)':r'w=(0,1,-1),\ d=(-2,-1,-1)',
 'P_j^-1 e2=e2':r'P_j^{-1}e_2=e_2',
 'w0=0 and w1=1':r'w_0=0,\ w_1=1',
 '(z,n0,n1)=(c0,a0,b0)':r'(z,n_0,n_1)=(c_0,a_0,b_0)',
 "z'=z^-1 and n'=z n":r"z'=z^{-1},\ n'=zn",
 '(U H_t U^-1) q_H H_(l1-t)':r'(UH_tU^{-1})q_HH_{l_1-t}',
 '(delta1-V11)/2':r'(\delta_1-V_{11})/2',
 '(-2t,0)':r'(-2t,0)','z=a1/a0 and n_i=a0 c_i':r'z=a_1/a_0,\ n_i=a_0c_i',
 'q=a0 a1 c0 c1':r'q=a_0a_1c_0c_1',
 '(n0/n1,z n1,n1) and (n1/n0,z n0,n0)':r'(n_0/n_1,zn_1,n_1),\ (n_1/n_0,zn_0,n_0)',
 'P_j Q1=P_(j-1)':r'P_jQ_1=P_{j-1}',
 'Q1=((1,0),(-1,1))':r'Q_1=\left(\begin{smallmatrix}1&0\\-1&1\end{smallmatrix}\right)',
 '(h,q_H) to (q_H^-1 h q_H,q_H)':r'(h,q_H)\mapsto(q_H^{-1}hq_H,q_H)',
 'F(0)=0 and F(j-1)-F(j)=r_j':r'F(0)=0,\ F(j-1)-F(j)=r_j',
 'a=2,b=1':r'a=2,\ b=1',
 'F(j)=2 binom(j+2,3)-N binom(j,2)':r'F(j)=2\binom{j+2}{3}-N\binom j2',
 'Z1-Z0=a':r'Z_1-Z_0=a',
}
# Replace only ordinary prose; retain every supplied display literally.
pat=re.compile('|'.join(re.escape(k) for k in sorted(rep,key=len,reverse=True)))
parts=re.split(r'(\\\[.*?\\\]|\\\(.*?\\\))',proof,flags=re.S)
for i in range(0,len(parts),2):
    parts[i]=pat.sub(lambda m:r'\('+rep[m.group()]+r'\)',parts[i])
proof=''.join(parts)
wordrep={'T_j':r'T_j','P_j':r'P_j','H_d':r'H_d','H_t':r'H_t',
 'q_H':r'q_H','l_i':r'l_i','r_j':r'r_j','C1':r'C_1','C2':r'C_2',
 'Q1':r'Q_1','Theta7':r'\Theta_7','V00':r'V_{00}','E²':r'E^2'}
wp=re.compile(r'\b('+'|'.join(re.escape(k) for k in sorted(wordrep,key=len,reverse=True))+r')\b')
parts=re.split(r'(\\\[.*?\\\]|\\\(.*?\\\))',proof,flags=re.S)
for i in range(0,len(parts),2):
    parts[i]=wp.sub(lambda m:r'\('+wordrep[m.group()]+r'\)',parts[i])
proof=''.join(parts)
proof=re.sub(r'(?m)^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nopagebreak[4]',proof)
proof=re.sub(r'`((?:code|notes|records)/[^`]+)`',lambda m:r'\path{'+m.group(1)+'}',proof)
tex=subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex','-t','latex','--wrap=preserve'],input=proof,text=True,capture_output=True,check=True).stdout
statement=r'''Retain the actual marked source
\[
 Y^2=X^3+(1-2v)X^2+TX+v^2,\quad G=(0,v),\quad
 q=T-(v^2-2v),\quad\lambda=v^{N}\lambda_0,
\]
with \((a,b,m)=(1,2,4p)\) or \((2,1,4p-1)\), \(p\ge1\),
\(N=km\), both cap norm signs \(\nu=\pm1\), every finite character
and the full annular cochain. The case \(k=0\) is the actual fixed-scalar
loop separated by RT.12 on its compact source annulus. For each
\(j\in\mathbb Z\) use the physical vertical-edge fan
\(T_j=T(e_1+je_2,e_2)\), and write \(Z_j\) for its actual positive
source-zero return in the physical K68 presentation \(\Theta_7=\mathbb Z/28\).
Then
\[
 Z_j-Z_0=2b\binom{j+1}{3}+(3-b)\binom{j+1}{2}
                            -N\binom j2\pmod {28}. \tag{ZV.1}
\]
The binomials are the integer-valued falling-factorial polynomials at
all integers. In the reduced branch \(a=2,b=1,m=4p-1\), P3K.80 gives
the fully evaluated formula
\[
 Z_j=k(3p-1)+2\binom{j+2}{3}
                  -k(4p-1)\binom j2\pmod {28}.       \tag{ZV.2}
\]
The proof constructs the actual single-loop \(C_1\) flop and derives
its free right integer from the literal doubled product. The good
branch retains its independently determined \(Z_0\) in the relative
formula; no absolute value is assigned to it here.'''
out=root/'notes/part3_source_zero_vertical_fans.tex'
if out.exists():
    hist=root/'records/attempts/k82_pre_export'/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    hist.mkdir(parents=True);shutil.copy2(out,hist/out.name)
out.write_text(r'\subsection{The source-zero return on every vertical-edge fan}'+'\n'+r'\begin{statement}{P3K.82}{Proved}'+'\n'+statement+'\n'+r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+tex.rstrip()+'\n'+r'\end{proof}'+'\n')
preamble=(root/'S6_06_BLIND_paper.tex').read_text().split(r'\begin{document}')[0]
(root/'code/part3_root/k82_standalone.tex').write_text(preamble+'\n'+r'\begin{document}'+'\n'+r'\input{notes/part3_source_zero_vertical_fans.tex}'+'\n'+r'\end{document}'+'\n')
record={'utc':datetime.now(timezone.utc).isoformat(),'statement':'P3K.82','status':'Proved',
 'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
 'include':str(out.relative_to(root)),'include_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
 'audit':'records/fourfold_audit_source_zero_vertical_fans.json','master_modified':False}
(root/'records/k82_export_manifest.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
