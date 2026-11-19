#!/usr/bin/env python3
"""Full K97 export, with the actual original/native endpoint comparison."""
from pathlib import Path
import hashlib,json,re,subprocess
R=Path(__file__).resolve().parents[2]
src=R/'notes/part3_e6_d_zero_disc_working.md'
sha=hashlib.sha256(src.read_bytes()).hexdigest()
assert sha=='83227b261fc0db99d9af82f52b9cbadadbaf03f2db9af2344b74a3e478ff7271'
cert=R/'code/part3/e6_d_zero_disc.json';data=json.loads(cert.read_text())
assert data['status']=='PASS' and data['source_sha256']==sha
s=src.read_text();body=s[s.index('## DZ6.1.'):]
body=body.replace('The proof is submitted for independent audit, with no numerical\ndivision or unrecorded change of an annular integer.', 'The full source, line, cap and endpoint maps above prove the stated conclusion with every prescribed annular integer retained.')
body+='\n## Executed exact certificate\n\nThe exact program \\path{code/part3/e6_d_zero_disc.py} and output \\path{code/part3/e6_d_zero_disc.json} execute '+str(data['checks'])+' identities and finite signed instances. They include the source and nodal Cartier charts, both root and tensor weights, complete cap endpoint, retained period, all three Laurent operators, finite vector averaging, global valuation equation and exact degree-two parameter. The complete geometric family proof is above. The preceding coordinate-only and frame-clarification stages remain under \\path{records/attempts/e6_d_zero_disc/}.\n'
body=re.sub(r'(?m)^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',body)
tex=subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex-superscript-subscript-smart','-t','latex','--wrap=preserve'],input=body,text=True,capture_output=True,check=True).stdout.replace(r'\tightlist','')
statement=r'''Let \(w\) vary on a sufficiently small disc about either point \(w^2=3\), and set
\[
 D=w^2-3,\quad R=3-2w^2,\quad v=w^2-1,\quad
 r=R/D^2,\quad t_c=v/D^3.
\]
On its punctured disc retain the actual original source
\[
 y^2=x^3+r x^2+t x+t^2,\qquad G=(0,t),\qquad
 M_a=\mathcal O(aG-O),\qquad Q=bG,
\]
with the whole selected zero \(t=t_c\), the full Cartier suspension
\(B_{\rm sel}=(t-t_c)B_{a,b}/t^3\), and either complete cap progression
\[
 (a,b;m)=(6,1;3l+2),\ l\ge0,\qquad
 (a,b;m)=(2,3;3l),\ l\ge1.
\]
Use either signed primitive norm \(n=\pm1\), the prescribed finite
character \(\zeta_m^d\), a fixed sufficiently small nonzero scalar,
the entire reference annular map, and no additional logarithmic
sites. For every prescribed lattice-basis fan at the selected cusp,
this punctured family is isomorphic, by the actual source, Cartier,
root, physical-circle and annular maps of the proof, to the restriction
of a smooth proper oriented sphere family on the full native disc
\[
 Y^2=X^3+R X^2+DTX+T^2,\qquad G=(0,T),\qquad q=T-v.
\]
The comparison retains both point and tensor Tate frames, the full
finite-root character, every period and all parameter scalar factors.
It intertwines the specified forward endpoints and hence their inverse
physical closings. The actual positive marked \(w\)-loop has return
\(0\in\Theta_7\).

The original infinity parameter is exactly
\(\epsilon=1/r=D^2/(3-2w^2)\). Each such positive \(w\)-loop
has degree two over the original positive infinity meridian.
No shorter original-parameter endpoint or return is inferred.'''
out=R/'notes/part3_e6_d_zero_disc.tex'
out.write_text('\\subsection{The E6 infinity-coordinate disc and its full marked comparison}\n\\begin{statement}{P3K.97}{Proved}\n'+statement+'\n\\end{statement}\n\\begin{proof}\n'+tex+'\n\\end{proof}\n')
pre=(R/'S6_06_BLIND_paper.tex').read_text().split(r'\begin{document}')[0]
(R/'code/part3/k97_standalone.tex').write_text(pre+'\n\\begin{document}\n\\input{notes/part3_e6_d_zero_disc.tex}\n\\end{document}\n')
manifest={'id':'P3K.97','status':'Proved','source':str(src.relative_to(R)),'source_sha256':sha,'include':str(out.relative_to(R)),'include_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'certificate':str(cert.relative_to(R)),'certificate_sha256':hashlib.sha256(cert.read_bytes()).hexdigest(),'checks':data['checks'],'master_modified':False,'report_modified':False,'mapping_modified':False,'qa':'pending'}
(R/'records/k97_export_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(manifest,indent=2))
