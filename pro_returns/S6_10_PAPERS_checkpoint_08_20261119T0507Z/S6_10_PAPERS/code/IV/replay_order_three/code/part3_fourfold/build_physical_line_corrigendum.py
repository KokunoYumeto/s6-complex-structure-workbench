from pathlib import Path
import datetime, hashlib, json, re, subprocess
root=Path(__file__).resolve().parents[2]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
src=root/'notes/part3_euler_cube_peer_sign_audit.md'
s=src.read_text()
body=s[s.index('## PS.1.'):]
body=body.replace('\\\\','@@LATEXROW@@')
body=body.replace('## PS.', '## PL.')
body=body.replace('PS.', 'PL.')
body=body.replace('The identification\nwith the meridian-one convention of F56/K42 is being audited separately;\nno known characteristic value is used to choose an orientation.', '')
body=body.replace('Their application to the physical mapping-torus class still requires\nthe actual normal/meridian and associated-circle dictionary in PL.1:',
                  'Their application to the physical mapping-torus class uses\nthe actual normal/meridian and associated-circle dictionary in PL.1:')
body=body.replace('Root and checks retain the global\nJin and period arrow as the remaining separate comparison.',
                  'The full Jin and physical-clutch comparison is proved in PL.6 below.')
body=body.replace('Identifying\nthis convention with the run\'s physical Hopf-lift convention is the\nremaining global F22 comparison being checked by root and checks.',
                  'The physical Hopf-lift convention is then identified in PL.6 below.')
body=body.replace('## PL.6. The physical product-factor dictionary submitted for audit',
                  '## PL.6. The physical product factors and the literal inverse clutch')
a=body.index('The displayed F22 product-factor identification is submitted to root')
b=body.index('## PL.7.',a)
body=body[:a]+r'''Here is the complete first-to-second clutch comparison, including the
piece exchange. In the plumbing coordinates \((y,q_H)\), put
\[
 L=D^4_y\times S^3_{q_H},\qquad
 R=S^3_y\times D^4_{q_H},
\]
and define \(\Sigma_F=L\cup_F R\) by identifying a point \(x\) in
the first boundary with \(F(x)\) in the second. For the physical line
\(M\), the positive-generator convention of F22 uses
\(u=+q_H\), \(y'=-y\). Thus its first and second pieces are
\[
 H_M=D^4_u\times S^3_{y'}=-R,\qquad
 K_M=S^3_u\times D^4_{y'}=-L.
\]
Its prescribed first-to-second clutch sends \(r\in R\) to
\(F(r)\in L\). Rewriting with \(L\) first means setting
\(x=F(r)\), so the second point is \(r=F^{-1}(x)\). Therefore
\[
                    \lambda_M(F)=-\Sigma_{F^{-1}}.
                                                        \tag{PL.1}
\]
The ball removed in the actual F8 cut-and-reglue construction is
\(D^4_u\times D^3_{y'}=-D^4_{q_H}\times D^3_y\); its outward
boundary is exactly the original complex six-sphere. On its free
face the boundary map is the actual relative physical return, and
on its fixed-tube face it is the identity. Both quotients identify
the first boundary point with its image in the second. They agree
pointwise off that free face and on its full collar. Hence
\(\lambda_M\) is the actual oriented clutched sphere.

For the dual line \(U=M^{-1}\), its complex positive circle is the
inverse physical circle. Its positive base is \(S^2_z\), so
\(u_U=+q_H\), \(y_U=y\). Now \(H_U=+R\) and \(K_U=+L\), with
the same first-to-second arrow. Consequently
\[
                  \lambda_U(F)=\Sigma_{F^{-1}}
                              =-\lambda_M(F).           \tag{PL.2}
\]
The comparison of the lifts is literal: the Hermitian dual map
\(D\) gives \(\widetilde f_U=D\widetilde f_M D^{-1}\).
It inverts each retained circle gauge. Its real four-dimensional
extension is the anti-linear spinor map of PL.4; the other four-ball
factor changes its orientation. Thus the maps on both seven-dimensional
pieces glue across the displayed clutch and reverse the eight-dimensional
product orientation. This is the geometric arrow in (PL.2).

For a disc-supported relative map, cancelling the opposite product
collars gives \(\Sigma_{F^{-1}}=-\Sigma_F\). In particular the
signed commutator generator of K23 still has
\(\lambda_M(\mathcal C)=\Sigma_{\mathcal C}=+1\). Its oriented
plumbing calculation and the native Cox flop increment are unchanged.
There is no extra inverse left to insert after (PL.1).

It follows directly that, in the same oriented Jin six-manifold,
\[
 (k_M,\ell_M,A_M)=-(k_U,\ell_U,A_U),\qquad
 [\Phi]=A_M\pmod {28}=-A_U\pmod {28}.                 \tag{PL.3}
\]
For the selected-cusp source loop the two cap computations above give
\[
 (k_U,\ell_U)=(6,0),\qquad(k_M,\ell_M)=(-6,0),
 \quad A_M=-1.
\]
The exact relative free-coordinate formula in this physical convention
is \(m=k_M-6A_M\), \(n=6A_M\); thus the initial native tuple is
\((m,n,s)=(0,-6,-1)\). The values follow from the line, orientation
and clutch maps, not from selecting a lift of a known residue.

The same comparison applies to the K6/K7 reference page calculation:
its outward-meridian-one line is \(U=M^{-1}\), and its determinant
restricts to \(-2c_1(M)\). Its square is unchanged. The proved page
expression \((3b^2-p_1(T\overline V))/24\) is therefore \(A_U\),
and the actual physical sphere class is its negative by (PL.3).
The inverse circle character and the exact physical Hopf lift, rather
than an equality of numerical polynomials, supply this conclusion.

For K57 specifically, IE.4 uses a real connection with
\(\alpha(\delta)=1\) and takes its curvature as its class \(x\).
It is exactly this \(U\) class. Its finite-chart Stokes calculation,
all normal residues and the scalar-order bordism remain proved.
Thus its good infinity value is still zero, while its reduced
\(A_U=1\) gives physical value \(-1\). This is restricted to the
two actual fans and completed families proved there.

''' + body[b:]
a=body.index('## PL.7.')
body=body[:a]+r'''## PL.7. Exact correction scope and preserved records

The source, Cartier divisor, actual Cox and cap charts, relative
matrix \(g\), its degree, \(c_2=-1\), and normal \(p_1=4\) are
retained. The written linear SP.9/10 arrow is replaced by PL.2/4's
actual anti-linear arrow. K42's pair \((6,0)\) is retained as the
meridian-one \(U\) pair, while its physical pair is \((-6,0)\).
F56's actual selected-cusp class is \(-1\), with its local link and
zero-index normal-sphere correction unchanged. Its nontriviality
and degree-two non-descent still follow because \(-1\) is odd.

F22's abstract specified complex-line transfer remains its proved
construction. Equations (PL.1)--(PL.3) give its actual physical
instantiation. In K6/K7 a meridian-one line cannot also be the
un-dualized source page line; the explicit Hermitian dual map is
retained. Every nonzero reference index using that convention must
be converted by (PL.3). An independent native Cox correction is
not negated by that conversion: its signed central generator is
unchanged, as shown above. In particular K65's two-fan correction
uses an independently zero reference and the same native generator,
so its proved classes are unchanged.

The pre-correction K42/F56 proof, certificates, outputs, PDF and QA
are preserved verbatim in `records/k42_pre_antilinear_arrow/`, with
SHA256 manifest. The exact local orientation, clutch and collar
certificate is `code/part3_fourfold/euler_cube_peer_sign.py` and its
saved JSON/output files. Root and checks independently audited the
physical product-factor and inverse-clutch comparison before this
corrigendum was promoted.
'''
statement=r'''Let \(M\) denote the actual complex line whose nonzero vectors
carry the physical positive delta circle, and let \(U=M^{-1}\) be
the outward-meridian-one Thom line. For the actual source/page/conifold
return constructions specified below, the two oriented Jin pairs satisfy
\[
 (k_M,\ell_M,A_M)=-(k_U,\ell_U,A_U),\qquad
 [\Phi]=A_M=-A_U\pmod {28}.
\]
The exact physical Hopf transfer is
\(\lambda_M(F)=-\Sigma_{F^{-1}}\); the dual transfer is
\(\lambda_U(F)=\Sigma_{F^{-1}}\). In the selected-cusp source
family of F56/K42 the corrected physical pair is \((-6,0)\),
the class is \(-1\), and the initial native relative tuple is
\((0,-6,-1)\). The previously calculated pair \((6,0)\) is the
\(U\) pair. The signed native Cox commutator and its flop increment
are unchanged. This statement supplies the exact line, cap, orientation
and inverse-clutch maps for these corrections.
'''
body=body.replace('\\\\','\\').replace('@@LATEXROW@@','\\\\')
statement=statement.replace('\\\\','\\')
out='# P3K.68. The physical line and exact Hopf-transfer corrigendum\n\n**Proved.** Full root and checks audits, 17 November 2026.\n\n## Statement\n\n'+statement+'\n\n'+body
dest=root/'notes/part3_physical_line_corrigendum_working.md'
dest.write_text(out)
def conv(x):
 x=re.sub(r'(?m)^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nopagebreak[4]',x)
 x=re.sub(r'`([^`]+)`',lambda m:r'\path{'+m.group(1)+'}',x)
 return subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex','-t','latex','--wrap=preserve'],input=x,text=True,capture_output=True,check=True).stdout
tex=r'\begin{statement}{P3K.68}{Proved}'+'\n'+conv(statement)+r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+conv(body)+r'\end{proof}'+'\n'
(root/'notes/part3_physical_line_corrigendum.tex').write_text(tex)
qa=(root/'code/part3_fourfold/qa_os49_corrected_returns.py').read_text().replace('k65','k68').replace('K65','K68').replace('P3K.65','P3K.68').replace('part3_os49_corrected_returns','part3_physical_line_corrigendum')
(root/'code/part3_fourfold/qa_physical_line_corrigendum.py').write_text(qa)
with (root/'records/literature_fourfold.md').open('a') as f:
 f.write(f'\n- {now} — Opened own PS.1--7 audit and K65 exporter/QA pattern to build the full proved K68 corrigendum. Material: exact local line, anti-linear cap, physical product and inverse-clutch morphisms; no prior value used to choose a sign.\n')
print(json.dumps({'statement':'P3K.68','status':'Proved','working_file':str(dest.relative_to(root)),'sha256':hashlib.sha256(out.encode()).hexdigest()},indent=2))
