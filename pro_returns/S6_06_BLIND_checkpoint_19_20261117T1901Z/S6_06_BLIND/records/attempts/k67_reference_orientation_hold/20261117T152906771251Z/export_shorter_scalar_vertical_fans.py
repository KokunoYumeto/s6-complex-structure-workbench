#!/usr/bin/env python3
"""Export the complete audited shorter-endpoint vertical-fan proof as K67."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,shutil,subprocess

ROOT=Path(__file__).resolve().parents[2]
source=ROOT/'notes/part3_shorter_scalar_vertical_fans_working.md'
target=ROOT/'notes/part3_shorter_scalar_vertical_fans.tex'
cert=json.loads((ROOT/'code/part3/shorter_scalar_vertical_fans.json').read_text())
assert cert['status']=='PASS' and cert['symbolic_checks']==54 and cert['signed_instances']==952
peer=ROOT/'records/checks_audit_shorter_scalar_vertical_fans.json'
root=ROOT/'records/root_audit_shorter_scalar_vertical_fans.json'
for p in (peer,root):
    d=json.loads(p.read_text())
    assert d['status']=='PASS',(p,d['status'])
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
archive=ROOT/'records/attempts'/('k67_export_'+stamp)
archive.mkdir(parents=True,exist_ok=True)
shutil.copy2(source,archive/source.name)
if target.exists():shutil.copy2(target,archive/target.name)
body=source.read_text().split('## SE.1.',1)[1]
body='## SE.1.'+body
body=body.replace(r'\begin{split}',r'\begin{aligned}').replace(r'\end{split}',r'\end{aligned}')
body=re.sub(r'(?m)^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',body)
body=re.sub(r'`(code/[A-Za-z0-9_./-]+)`',lambda m:r'\path{'+m.group(1)+'}',body)
body=re.sub(r'\bSE\.(\d+)\b',r'P3K.67.\1',body)
converted=subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex','-t','latex','--wrap=preserve'],input=body,text=True,capture_output=True,check=True).stdout
statement=r'''
Retain the actual whole-zero \(I_1\) source, Cartier line, affine
root caps, finite characters and annular maps of the weighted shorter
construction in P3K.35.2--5. Write the contracting source translation
as \(-bG\), the canonical scalar as \(\lambda=r^M\), and the actual
shorter parameter as \(w=r^b\), with \(b\mid M\). Keep its specified
forward endpoint, including the rational source lift, bounded source
factor and constant physical-delta normalization. Put \(J=M/b\).
For the actual periodic fan \(T_n\) with edge directions
\[
                 e_2,\qquad (1,n),\qquad(1,n-1),
                         \qquad n\in\mathbb Z,
\]
the positive shorter-loop return satisfies
\[
 A_n=A_0-J\frac{n(n-1)}2\pmod{28},\qquad
 A_0=\frac{\chi-H_{\rm page}/2}{b}\in\mathbb Z,
 \qquad H_{\rm page}=Ma^2/d_{\rm source}.
 \tag{P3K.67.0}
\]
Its actual native relative free pairs are
\[
 C_1:\bigl(J(1-n),J(n-1)\bigr),\qquad
 C_2:\bigl(nJ,-nJ\bigr).
\]
The two oriented Cox flips go respectively to \(T_{n-1}\) and
\(T_{n+1}\). All source, cap and line factors are retained in their
explicit morphisms. No simultaneous equivariant product of the full
three-curve plumbing is used.

For the original P3K.33 endpoint, with root orders \(3K,4L\),
\(\gcd(3K,4L)=1\), either sphere sign, and its prescribed delta
characters, retain exactly
\[
 w_h=e^{-\pi ic/(KL)},\qquad u=\kappa w_h^{2KL}.
\]
Here \(J=2KL\), \(A_0=0\), and
\[
                       A_n=-KL\,n(n-1)\pmod{28}.
\]
In particular the original \(K=L=1\) member on \(T_2\) has class
\(-2=26\), while \(T_0,T_1\) have class zero. The proof supplies
the actual endpoint and cover maps, not a division in \(\Theta_7\).
This statement assigns neither an arbitrary-fan formula nor separate
characteristic integers on the changed fans.
'''
out=r'\subsection{Shorter scalar endpoints on the physical-vertical-edge fans}'+'\n'+r'\begin{statement}{P3K.67}{Proved}'+'\n'+statement+r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+converted+r'\end{proof}'+'\n'
for bad in (r'\^{}',r'\textbackslash',r'\textsuperscript{'):
    assert bad not in out,bad
target.write_text(out)
pre=(ROOT/'code/part3/k62_standalone.tex').read_text().split(r'\begin{document}')[0]
(ROOT/'code/part3/k67_standalone.tex').write_text(pre+'\n'+r'\begin{document}'+'\n'+r'\input{notes/part3_shorter_scalar_vertical_fans.tex}'+'\n'+r'\end{document}'+'\n')
manifest={'utc':datetime.now(timezone.utc).isoformat(),'statement':'P3K.67','source':str(source.relative_to(ROOT)),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'latex':str(target.relative_to(ROOT)),'proof_sections':['SE.1','SE.2','SE.3','SE.4','SE.5'],'proof_content_omitted':False,'archive':str(archive.relative_to(ROOT)),'certificate':'code/part3/shorter_scalar_vertical_fans.json','peer_audit':str(peer.relative_to(ROOT)),'root_audit':str(root.relative_to(ROOT)),'layout_changes':['Proof equation tags and section headings receive the P3K.67 prefix; every mathematical formula and actual arrow retained.'],'main_input_modified':False}
(ROOT/'records/k67_export_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
p=ROOT/'code/part3/results_mapping.json'
mapping=json.loads(p.read_text())
extra=mapping.setdefault('additional_source_loop_results',[])
detail={'id':'P3K.67','status':'Proved','item_of_prompt':'3.4','proof':str(source.relative_to(ROOT)),'latex_file':str(target.relative_to(ROOT)),'certificate':manifest['certificate'],'peer_audit':manifest['peer_audit'],'root_audit':manifest['root_audit'],'statement':'Actual K35/K33 shorter endpoints on the complete physical-vertical-edge fan line.','class':'A_n=A_0-(M/b)*n*(n-1)/2 mod28','original_class':'-K*L*n*(n-1) mod28','original_KL1_T2_class':26,'C1_native_pair':'((M/b)*(1-n),(M/b)*(n-1))','C2_native_pair':'((M/b)*n,-(M/b)*n)','scope':'Explicit forward source/root/line endpoint, native Cox products and literal cover pullbacks; no arbitrary-fan or individual changed-fan characteristic-pair claim.'}
if isinstance(extra,list):
    extra[:]=[r for r in extra if not isinstance(r,dict) or r.get('id')!='P3K.67']
    extra.append(detail)
else:extra['P3K.67']=detail
p.write_text(json.dumps(mapping,indent=2)+'\n')
print('Exported full K67 / SE.1--5, 54 exact checks and 952 signed instances; maininput untouched.')
