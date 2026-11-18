#!/usr/bin/env python3
"""Export the audited P3K.58 groupoid, full dictionary and paired returns."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,re,shutil,subprocess

ROOT=Path(__file__).resolve().parents[2]
source=ROOT/'notes/part3_source_global_groupoid_working.md'
text=source.read_text()
cert=json.loads((ROOT/'code/part3/source_global_groupoid.json').read_text())
assert cert['status']=='PASS' and cert['checks']==215
assert json.loads((ROOT/'records/root_audit_source_global_groupoid.json').read_text())['status']=='PASS'
assert json.loads((ROOT/'records/root_audit_source_infinity_excision.json').read_text())['status']=='PASS'
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
archive=ROOT/'records/attempts'/f'k58_export_{stamp}'
archive.mkdir(parents=True,exist_ok=True)
shutil.copy2(source,archive/source.name)
target=ROOT/'notes/part3_source_global_groupoid.tex'
if target.exists():shutil.copy2(target,archive/target.name)
body=text[text.index('## RG.1.'):]
# Layout-only division of one long pair of chart equations.
old=r""" T^+_{i,j}:\quad q=x_0x_1x_2,\quad Z=q^ix_1,\quad V=q^jx_2,
\qquad
 T^-_{i,j}:\quad q=y_0y_1y_2,\quad
 Z=q^iy_0y_1,\quad V=q^jy_0y_2,"""
new=r""" \begin{aligned}
 T^+_{i,j}:\quad &q=x_0x_1x_2,\quad Z=q^ix_1,\quad V=q^jx_2,\\
 T^-_{i,j}:\quad &q=y_0y_1y_2,\quad
 Z=q^iy_0y_1,\quad V=q^jy_0y_2.
 \end{aligned}"""
assert old in body
body=body.replace(old,new)
body=re.sub(r'(?m)^#{2,3} (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',body)
body=re.sub(r'(?<![\w{/])(code/[A-Za-z0-9_./-]+)',lambda m:r'\path{'+m.group(1).rstrip('.')+'}'+('.' if m.group(1).endswith('.') else ''),body)
converted=subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex','-t','latex','--wrap=preserve'],input=body,text=True,capture_output=True,check=True).stdout
statement=r"""
Use the actual marked E7 source and section
\[
 Y^2=X^3+(1-2v)X^2+TX+v^2,\qquad
 G=(0,v),\qquad T_0(v)=v^2-2v.
\]
Retain the selected whole-zero \(I_1\) cusp, one III-star cap,
and the complete Cartier line, finite character and reference
annular data of P3K.49. The cap data are
\[
 (a,b,m)=(1,2,4p)\quad\hbox{or}\quad(2,1,4p-1),
 \qquad p\ge1,\quad n=\pm1,\quad
 N=km,\quad k\ge1.
\]
The literal scalar is \(\lambda(v)=v^N\lambda_0\), in the
common contracting range of each bounded parameter surface
used below. No additional logarithmic disc meets the two
finite sites that coalesce. The cusp fan is the initial
physical-vertical-edge fan \(\mathcal T_0\) or its reflection
\(J\mathcal T_0\), where \(J=\operatorname{diag}(-1,1)\).

On the cover \(v=\rho^2-1\), the constructed four-holed
parameter surface has the actual cut-surface endpoint relation
\[
 [Z_{\mathcal T}]+[Z_{J\mathcal T}]+1+[I_{\mathcal T}]=0
                    \quad\text{in }\Theta_7\cong\mathbb Z/28.
\]
Here \(Z_{\mathcal T}\) is the positive source-zero return
near \(\rho=1\), and \(I_{\mathcal T}\) is the positive
\(\epsilon=1/\rho\) return with the full original scalar
path. The reflected source-zero object and every closing
arrow are supplied by the literal source, theta/Cartier,
root and annular maps in the proof.

The full infinity comparison retains \(D^{-4}\), the reduced
doubled lattice period, and the scalar quadratic cochain.
Together with the independently proved infinity excision
P3K.57 and the actual independent scalar parameter, it gives
\[
 \begin{array}{c|c|c}
 (a,b,m)&I_{\mathcal T}
                &[Z_{\mathcal T}]+[Z_{J\mathcal T}]\\ \hline
 (1,2,4p)&0&-1\\
 (2,1,4p-1)&1-2k(1-3p)&-2+2k(1-3p).
 \end{array}
\]
These formulas retain both norm signs and the stated two
fan objects. P3K.49 carries each original positive \(u\)-loop
to three positive \(v\)-loops by an actual family morphism.
No individual source-zero class or division of a class is
assigned by this statement.
"""
out=r'\subsection{The actual global source-loop groupoid and paired source-zero returns}'+'\n'+r'\begin{statement}{P3K.58}{Proved}'+'\n'+statement+r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+converted+r'\end{proof}'+'\n'
for forbidden in (r'\^{}',r'\textsuperscript{',r'\textbackslash'):
    assert forbidden not in out,forbidden
target.write_text(out)
pre=(ROOT/'code/part3_root/k55_standalone.tex').read_text().split(r'\begin{document}')[0]
(ROOT/'code/part3/k58_standalone.tex').write_text(pre+'\n'+r'\begin{document}'+'\n'+r'\input{notes/part3_source_global_groupoid.tex}'+'\n'+r'\end{document}'+'\n')
manifest={'utc':datetime.now(timezone.utc).isoformat(),'statement':'P3K.58','source':str(source.relative_to(ROOT)),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'latex':str(target.relative_to(ROOT)),'all_proof_sections':['RG.1','RG.2','RG.2a','RG.3','RG.4','RG.5','RG.6','RG.7'],'layout_changes':['Split the two long triangle-chart equations into aligned rows; same formulas.'],'frontmatter':'Source setup is retained in the formal statement; provenance/history remains in the archived complete Markdown.','dependency':'P3K.57 actual infinity excision; no arithmetic replacement of that morphism.','archive':str(archive.relative_to(ROOT))}
(ROOT/'records/k58_export_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
detail={'id':'P3K.58','status':'Proved','item_of_prompt':'3.4','proof':str(source.relative_to(ROOT)),'latex_file':str(target.relative_to(ROOT)),'certificate':'code/part3/source_global_groupoid.json','audit':'records/root_audit_source_global_groupoid.json','dependency':'P3K.57','statement':'Actual global source-loop groupoid, complete infinity source/root/Cartier/closing dictionary, and paired source-zero returns for the initial and reflected fans.','values':cert['paired_return_rows'],'scope':'No individual source-zero return, no class division, no additional colliding-site logarithmic discs.'}
p=ROOT/'code/part3/results_mapping.json'
mapping=json.loads(p.read_text()) if p.exists() else {'comparisons':[]}
extra=mapping.setdefault('additional_source_loop_results',[])
if isinstance(extra,list):
    extra[:]=[row for row in extra if not isinstance(row,dict) or row.get('id')!='P3K.58']
    extra.append(detail)
else:
    extra['P3K.58']=detail
p.write_text(json.dumps(mapping,indent=2)+'\n')
print('Exported P3K.58, full RG.1–7, 215 exact checks and explicit P3K.57 dependency. Maininput untouched.')
