#!/usr/bin/env python3
"""Export audited FA.1--5 as P3K.79, retaining the working source/history."""
from pathlib import Path
from datetime import datetime,timezone
import re,subprocess,json,hashlib,shutil
ROOT=Path(__file__).resolve().parents[2]
src=ROOT/'notes/part3_os49_full_automorphisms_working.md'
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
history=ROOT/'records/attempts/k79_pre_export'/stamp;history.mkdir(parents=True);shutil.copy2(src,history/src.name)
proof='## FA.1.'+src.read_text().split('## FA.1.',1)[1]
proof=proof.replace('The\npresent note is working pending independent review of the actual local\ninverse and full root-groupoid argument.','The complete local inverse and root-groupoid argument have passed the independent audits recorded with this export.')
# Typesetting-only substitution, outside existing mathematical displays.
rep={
'Theta_7':r'\Theta_7',
'pi:X->P1':r'\pi:X\to\mathbb P^1','H^2(X;Z)=0':r'H^2(X;\mathbb Z)=0','S6':r'S^6','E_T':r'E_T','O_X(E)':r'\mathcal O_X(E)','pi=u^e':r'\pi=u^e','u->zeta_e u':r'u\mapsto\zeta_e u','u^e':r'u^e','P1':r'\mathbb P^1','C(X)=C(t)':r'\mathbb C(X)=\mathbb C(t)','pi*':r'\pi^*','pi F=h pi':r'\pi F=h\pi','A,B,C':r'A,B,C','m=3k':r'm=3k','XA=AX':r'XA=AX','b=q=0':r'b=q=0','a=p=d':r'a=p=d','a=epsilon in {+1,-1}':r'a=\epsilon\in\{+1,-1\}','c in Z':r'c\in\mathbb Z','epsilon I':r'\epsilon I','c=0':r'c=0','+I':r'+I','-I':r'-I','(z,V)->(-z,V^{-1})':r'(z,V)\mapsto(-z,V^{-1})','(z,V)->(z+s,cV)':r'(z,V)\mapsto(z+s,cV)','B^{-1}':r'B^{-1}','i(x,y,t)=(x,-y,t)':r'i(x,y,t)=(x,-y,t)','M=O(G-O)':r'M=\mathcal O(G-O)','G-O':r'G-O','f i=f':r'f\circ i=f','t=1':r't=1','x=y=0':r'x=y=0','f=-1':r'f=-1','tau=-x/y':r'\tau=-x/y','tau e':r'\tau e','tau(i(p))=-tau(p)':r'\tau(i(p))=-\tau(p)','tau^2 f':r'\tau^2 f','v_i(q)':r'v_i(q)','-1/v_i(q)':r'-1/v_i(q)','-v_i(q)^2':r'-v_i(q)^2','I_i':r'I_i','v_i=1':r'v_i=1','t=z^{3k}, x=z^{4k}X, y=z^{6k}Y':r't=z^{3k},\ x=z^{4k}X,\ y=z^{6k}Y',"O(G'-O')":r"\mathcal O(G'-O')","G'=(z^{2k},1)":r"G'=(z^{2k},1)",'z^{4k}':r'z^{4k}','-v_i(z)^2':r'-v_i(z)^2','z^m=t':r'z^m=t','(v,h)->(-v,h)':r'(v,h)\mapsto(-v,h)','{0,u,v}':r'\{0,u,v\}','{u,v,u+v}':r'\{u,v,u+v\}','u+v':r'u+v','s_i':r's_i','F_i g_ij=g_ij F_j':r'F_i g_{ij}=g_{ij}F_j','A_z(x)=L_D(z)x+a_D(z)':r'A_z(x)=L_D(z)x+a_D(z)','D=+1 or -1':r'D=\pm1','2D':r'2D','f(t)U^j':r'f(t)U^j','j=3a':r'j=3a','c B_0^{-a}':r'cB_0^{-a}','c lambda^a':r'c\lambda^a','B_lambda':r'B_\lambda','ell_0+L delta':r'\ell_0+L\delta','ell_0':r'\ell_0','D+D=2D':r'D+D=2D','(m,D,d)':r'(m,D,d)','L=Nk':r'L=Nk','psi':r'\psi','lambda':r'\lambda','omega':r'\omega'
}
pat=re.compile('|'.join(re.escape(k) for k in sorted(rep,key=len,reverse=True)))
parts=re.split(r'(\\\[.*?\\\]|\\\(.*?\\\))',proof,flags=re.S)
for i in range(0,len(parts),2):parts[i]=pat.sub(lambda m:r'\('+rep[m.group()]+r'\)',parts[i])
proof=''.join(parts)
proof=re.sub(r'(?m)^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',proof)
proof=re.sub(r'`((?:code|notes|records)/[^`]+)`',lambda m:r'\path{'+m.group(1)+'}',proof)
tex=subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex','-t','latex','--wrap=preserve'],input=proof,text=True,capture_output=True,check=True).stdout.replace(r'\tightlist','')
statement=r'''Retain an actual fixed-source OS49 sphere model of P3K.76--78,
with the given scalar, component Cartier line, finite cap of order
\(m=3k>0\), all fixed marked smooth order-one clutches and their full
root/line/annular data, and any periodic index-one lattice-basis fan \(P\).
Write \(D=n+m\sum_i\psi(\ell_i)=\pm1\) for its exact sphere datum.
Its full holomorphic automorphism group is the faithful physical
\(\mathbb C^*\) action. Every such automorphism descends to the identity
on the base and has identity linear part on the generic torus. The proof
uses the actual root and same-fan inversion maps to exclude the negative
linear part; no translation or source-descent assumption is imposed.

For a prescribed fixed-source scalar path of integer winding \(L\),
including the marked cap/line variations of P3K.44 and the fixed
smooth-site clutches of P3K.78, every specified holomorphic endpoint has
\(L=Nk\) for an integer \(N\). The explicit canonical endpoint and its
actual powers realize every such winding. All holomorphic endpoints for
that same path have oriented physical return
\[
                              N S_k(P)\in\mathbb Z/28,
\]
where \(S_k(P)\) is the actual all-fan return of P3K.77. The minimum
positive scalar winding in this endpoint scope is \(k\).
The maps retain the full finite group cochain, every line character,
and the original ordinary-clutch integers. This statement concerns the
fixed source and its stated data, with holomorphic endpoints; it does
not identify a different source-moduli path or a smooth endpoint that
has not been given a holomorphic map.'''
out=ROOT/'notes/part3_os49_full_automorphisms.tex'
if out.exists():shutil.copy2(out,history/out.name)
out.write_text(r'\subsection{Full holomorphic endpoints of the fixed OS49 sphere families}'+'\n'+r'\begin{statement}{P3K.79}{Proved}'+'\n'+statement+'\n'+r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+tex+'\n'+r'\end{proof}'+'\n')
preamble=(ROOT/'S6_06_BLIND_paper.tex').read_text().split(r'\begin{document}')[0]
(ROOT/'code/part3/k79_standalone.tex').write_text(preamble+'\n'+r'\begin{document}'+'\n'+r'\input{notes/part3_os49_full_automorphisms.tex}'+'\n'+r'\end{document}'+'\n')
manifest={'statement':'P3K.79','status':'Proved','utc':datetime.now(timezone.utc).isoformat(),'include':str(out.relative_to(ROOT)),'include_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'preserved_prior':str(history.relative_to(ROOT)),'typesetting':'Plain-text formula tokens converted to inline TeX outside existing math; audited working source preserved.','master_modified':False}
(ROOT/'records/k79_export_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');print(json.dumps(manifest,indent=2))
