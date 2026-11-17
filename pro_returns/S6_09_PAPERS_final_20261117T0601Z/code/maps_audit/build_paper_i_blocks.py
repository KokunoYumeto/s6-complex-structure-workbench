"""Reproducible editorial blocks; extraction is distinguished from proof audit."""
from pathlib import Path
import re,json,hashlib

ROOT=Path('/workspace/scratch/037cd144174c')
OUT=ROOT/'deliverables/work/maps_audit'
source=ROOT/'sources/returns/S6_04_MAPS_MANIFOLDS/sections/real_forms.tex'
s=source.read_text()
s=s.replace(r'\subsection{A.3. The two real forms and their fixed sets}',
            r'\section{Real structures and their fixed three-spheres}\label{mapsI:real-forms}')
s=s.replace('In this subsection $d=\\widehat\\delta$ and $g=\\widehat\\gamma$.',r'''We use the family marking
$\Lambda=\mathbb Z\langle\widehat\gamma,\widehat u,\widehat w,
\widehat\delta\rangle$ and its dual covector $\gamma$.
In this section $d=\widehat\delta$, $g=\widehat\gamma$,
$u=\widehat u$, and $w_{\Lambda}=\widehat w$; an unadorned $w$ in a
lattice expression denotes $w_{\Lambda}$, whereas the scalar parameter is
$w=\exp(-\pi i c)$. Put
\[
 e=\Pi_c d=(0,1)^t,\qquad E=d\otimes\gamma,
 \qquad \Pi_c=
 \begin{pmatrix}6\mu&\tau&1&0\\\beta^{\rm part}+c&\mu&0&1\end{pmatrix},
\]
\[
 D_c=\operatorname{Im}(\beta^{\rm part}+c)
       -6(\operatorname{Im}\mu)^2/\operatorname{Im}\tau<0.
\]
Thus $d$ is a lattice vector and $e$ is its image in the complex translation
space. The circle $\rho(s)$ is translation by $se$, $s\in\mathbb R/\mathbb Z$.
The clockwise root generators and the affine vectors are
\[
 A_1=\begin{pmatrix}1&0&0&0\\6&0&1&0\\-6&-1&-1&0\\-2&1&0&1\end{pmatrix},\quad
 A_2=\begin{pmatrix}1&0&0&0\\0&0&-1&0\\-6&1&0&0\\3&0&1&1\end{pmatrix},
\]
\[
 M_0=(A_1A_2)^{-1},\qquad
 v_1=(1,2,-4,0)^t,\qquad v_2=(-1,-3,3,0)^t.
\]
These are the same conventions as in the family construction. In cusp
coordinates $q=1/t$ and $s=(2\pi i)^{-1}\log q$, the bounded matrix $C_c(q)$
is defined by $Z_c=sB_0+C_c(q)$, with
$B_0=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$.
In particular $\Pi_cg=(6\mu,-s+C_{c,21})^t$.''')

# Every complex translation uses the period image e; occurrences of d in
# lattice matrices, half-period cosets and the integral centralizer stay d.
replacements={
 r'b_c(z)=\alpha\Pi_c(z)g+S(t(z))d.':r'b_c(z)=\alpha\Pi_c(z)g+S(t(z))e.',
 r'b^{\rm norm}_{c_0}=\tfrac13\Pi_{c_0}g+(2L_F-4L_G)d.':r'b^{\rm norm}_{c_0}=\tfrac13\Pi_{c_0}g+(2L_F-4L_G)e.',
 'constant translation $d/6$':'constant translation $e/6$',
 r'\left(h(L_F-L_G)-\frac{h^2}{24}\right)d.':r'\left(h(L_F-L_G)-\frac{h^2}{24}\right)e.',
 'constant translation $-d/4$':'constant translation $-e/4$',
 'finite difference vectors are $2d$ and $-4d$':'finite difference vectors in the complex translation space are $2e$ and $-4e$',
 r'$H^0=\C d$ with integral periods $\Z d$':r'$H^0=\C e$ with integral periods $\Z e$',
 r'$\beta(t)=\Pi_c(t)^{-1}b_c(t)$':r'$r_c(t)=\Pi_c(t)^{-1}b_c(t)$',
 r'\beta(t)+\epsilon d/2':r'r_c(t)+\epsilon d/2',
 r'\gamma(\beta(t))':r'\gamma(r_c(t))',
 r'\frac{\Im S(t)}{D(t)}':r'\frac{\Im S(t)}{D_c(t)}',
 r'sends $S d$':r'sends $S e$',
 r'$\Im S/D$':r'$\Im S/D_c$',
 'The checked real comparison':'The real comparison of Proposition~\\ref{fam:src:B.4.2}',
 'The automorphism computation used here is the supplied family return\nB.4.1:':'The automorphism computation used here is Proposition~\\ref{fam:src:B.4.1}:',
 'Use the lattice reflection from the\nsupplied real-comparison proof,':'Use the lattice reflection from Proposition~\\ref{fam:src:B.4.2},',
 'the checked even-shift formula with $h=-2$':'the following explicit even-shift formula with $h=-2$',
 'This uses the actual unit representative of K8, so no fractional deck\ntranslation is asserted to extend.':'The displayed translation has integral affine defects on the ordinary cover, holomorphic finite-chart corrections, and a nonvanishing toric-unit expression at the cusp; it represents the even shift of Proposition~\\ref{fam:src:A.3.1}. Its cusp expression is checked immediately below.',
 'The repaired map $e$ may be chosen $\\rho$-invariant.':'The repaired map $e_{\\rm q}$ of Theorem~\\ref{mapsI:src:A.2.1} may be chosen $\\rho$-invariant.',
 'annihilated by $e$.':'annihilated by $e_{\\rm q}$.',
 r'Thus $e|_{\operatorname{Fix}\sigma}$':r'Thus $e_{\rm q}|_{\operatorname{Fix}\sigma}$',
}
for a,b in replacements.items():
    if a not in s: raise RuntimeError('Missing exact replacement: '+a)
    s=s.replace(a,b)

# Smith's finite-dimensional G-CW hypothesis is supplied by an opened theorem.
s=s.replace("three-manifold. Smith's theorem, in the form of", r'''three-manifold. The smooth $\mathbb Z/2$ action admits an equivariant
triangulation by \cite[Theorem~3.1, p.~48]{Illman1972}; compactness and finite
dimension give the finite-dimensional $G$-CW hypothesis. Smith's theorem,
in the form of''')

# Original tags become referenceable labels; no source numbering is retained.
for i in range(1,10):
    s=s.replace(r'\tag{A.3.'+str(i)+'}',r'\label{mapsI:real-eq-'+str(i)+'}')
    s=s.replace('(A.3.'+str(i)+')',r'\eqref{mapsI:real-eq-'+str(i)+'}')

titles={
 'A.3.1':('proposition','Two conjugacy classes of real structures'),
 'A.3.2':('theorem','Explicit real involutions and all fixed fibres'),
 'A.3.3':('theorem','The real three-manifolds'),
 'A.3.4':('proposition','Restrictions of the repaired circle quotient'),
}
for sid,(env,title) in titles.items():
    pat=r'\\paragraph\{(?:Proposition|Theorem) '+re.escape(sid)+r' \([^\n]*\)\.\}'
    m=re.search(pat,s)
    if not m:raise RuntimeError(sid)
    p=s.index(r'\begin{proof}',m.end())
    statement=s[m.end():p].strip()
    s=s[:m.start()]+r'\begin{'+env+'}['+title+']'+r'\label{mapsI:src:'+sid+'}\n'+statement+'\n'+r'\end{'+env+'}\n\n'+s[p:]
s=s.replace('Theorem A.3.2',r'Theorem~\ref{mapsI:src:A.3.2}')

# Prove the explicit representative used by both sign classes, without relying
# on the earlier cohomological choice of the family shift.
needle='Over $t>1$ we have'
insert=r'''Indeed put $\ell=L_F-L_G=-s/12+\kappa_0(q)$ and
$C_{c,21}(q)=c+C_{0,21}(q)$, and set
$D_0(q)=C_{0,21}(q)-12\kappa_0(q)$.
The explicit even-shift translation becomes
\[
 b_{h,c}=
 \left(-h\mu/2,-h(c+D_0)/12-h^2/24\right)^t.
\]
The logarithmic terms have cancelled exactly. Exponentiating both
coordinates gives holomorphic nonzero torus multipliers on the whole cusp
disc; multiplication by these units extends over every toric stratum.
Compatibility with the period deck group is the integral identity
$\exp(2\pi i h\lambda_1)=1$ for $h\in2\mathbb Z$ and
$\lambda_1\in\mathbb Z$. The finite-chart defects are checked by the
same displayed $A_j$ and root logarithms used for the normalization.
'''
s=s.replace(needle,insert+'\n'+needle,1)

prep=r'''
\begin{lemma}[The circle quotient needed for the real restriction]
\label{mapsI:real-quotient-preparation}
The primitive covector $\gamma$ defines a smooth circle quotient on the
ordinary and finite-filled part. Its three-dimensional target, filled at
the cusp by the prescribed solid torus, is $S^3$. There is a smooth map
$e_{\rm q}:X_c\to S^3$ over the base that equals this quotient outside an
arbitrarily small cusp neighbourhood and maps that neighbourhood into the
prescribed solid torus. Its homotopy class under this image condition is
independent of the cusp replacement.
\end{lemma}
\begin{proof}
The equations $\gamma A_j=\gamma$ make
$[z,\Pi_cx]\mapsto([z],\gamma(x)\bmod\mathbb Z)$ well defined on the
ordinary part. The root generator acts on its target by
$(s,\theta)\mapsto(e^{-2\pi i/m}s,\theta+\kappa/m)$, where
$(m,\kappa)=(3,1)$ or $(4,-1)$. This action is free. If
$r\kappa\equiv1\pmod m$, the invariant coordinates
$(s e^{2\pi ir\theta},e^{2\pi im\theta})$ identify its quotient with
$D^2\times S^1$. Thus the target has the indicated two Seifert solid tori.
The actual finite overlap translations give their residues $1,-1$;
the untwisted cusp collar gives residue zero.

Let $\rho_0+\rho_1+\rho_2=0$ be the oriented boundary classes of the base
pair of pants and $h$ the quotient circle. The three meridians are
$3\rho_1-h$, $4\rho_2+h$, and $\rho_0$. After filling the last one,
$\rho_2=-\rho_1$, so the first two meridians, in the basis
$(\rho_1,h)$, are $(3,-1)$ and $(-4,1)$. Their determinant is $-1$.
Primitive meridians intersecting once give the standard genus-one
Heegaard splitting of $S^3$: an integral automorphism of the boundary
torus takes them to its two coordinate circles, after which the gluing
is the usual decomposition of $S^3\subset\mathbb C^2$ into two solid tori.

By the cusp fundamental-group computation,
$\pi_1(N_0)=\Lambda/\langle\widehat w,d\rangle$. The boundary inclusion
is surjective and kills the base meridian and the two vanishing cycles.
The class of $\gamma$ therefore extends over $N_0$. Since
$S^1=K(\mathbb Z,1)$, choose a representing map $\theta':N_0\to S^1$.
Its boundary restriction is homotopic to the prescribed character because
the two maps induce the same homomorphism on the boundary fundamental
group. The collar homotopy extension property and relative smooth
approximation make the maps agree exactly on a smaller outer collar.
Then $(f,\theta')$ is the required smooth map into $D^2\times S^1$,
also at the critical points of $f$.

Surjectivity of the boundary fundamental-group map makes
$H^1(N_0)\to H^1(\partial N_0)$ injective. Both spaces are connected,
so the exact sequence of the pair gives $H^1(N_0,\partial N_0)=0$.
The quotient of two circle replacements agreeing on the boundary
therefore has trivial relative $H^1$ class and is relatively homotopic
to the constant map. Keeping $f$ fixed gives the required homotopy
inside the designated solid torus.
\end{proof}

'''
needle=r'\begin{proposition}[Restrictions of the repaired circle quotient]'
# The parent requires one complete placement rather than duplicate proof blocks.
# A.1.1--A.1.3 and A.2.1 are transferred to I below; no preparatory duplicate
# is emitted. The string above remains only as an editorial derivation record.
s=s.replace(r'\texttt{code/real\_involutions.py}',r'\texttt{code/maps\_audit/MAPS/code/real\_involutions.py}')
s=s.replace(r'\texttt{code/real\_finite\_four.py}',r'\texttt{code/maps\_audit/MAPS/code/real\_finite\_four.py}')

out=OUT/'paperI_real_forms.tex';out.write_text(s)
record={
 'output':str(out.relative_to(ROOT)),'source':str(source.relative_to(ROOT)),
 'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'output_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
 'source_results':['MAPS:A.3.1','MAPS:A.3.2','MAPS:A.3.3','MAPS:A.3.4'],
 'source_proof_preservation':'All four statement/proof arguments retained in full; notation and exact references corrected.',
 'construction_dependency':'MAPS A.1.1--A.1.3 and A.2.1 transferred in full to paperI_circle_quotient.tex; III cites this construction and retains the homotopy computations.',
 'changes':['Distinguished d in Lambda from e=Pi_c d in C^2.',
 'Renamed real inverse translation beta(t) to r_c(t) to avoid the holomorphic period beta.',
 'Renamed repaired quotient e to e_q, preserving FAMILY e=(0,1).',
 'Explicit D_c and full period/monodromy conventions.',
 'Explicit logarithmic cancellation proving the even-shift representative extends over the cusp.',
 'Source equation numbers replaced with local labels; source result IDs retained in labels.'],
 'proof_check':{'reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','date':'2026-11-17','effort':'Pro','scope':'All four proofs read and rederived; integral and affine checks rerun in real_involutions.py, real_finite_four.py, maps_real_audit.py, maps_exact.py. Knudson Th 4.1(1) opened and matched. Dependent FAMILY automorphism and real-comparison propositions remain parent-owned.'},
 'external_labels':['fam:src:B.4.1','fam:src:B.4.2','fam:src:A.3.1'],
 'citation_keys':['Knudson2004','Illman1972'],
}
(OUT/'paperI_real_forms_manifest.json').write_text(json.dumps(record,indent=2)+'\n')
print('Wrote',out.relative_to(ROOT),len(s),'characters')

source=ROOT/'sources/returns/S6_04_MAPS_MANIFOLDS/sections/maps_A.tex'
s=source.read_text()
end=s.index(r'\paragraph{Proposition A.2.2')
s=s[:end]
s=re.sub(r'^%[^\n]*\n','',s,flags=re.M)
s=s.replace(r'\subsection{A.1. The integral quotient and its three-dimensional target}',
            r'\section{The integral circle quotient and its cusp replacement}\label{mapsI:circle-quotient}')
s=s.replace(r'\subsection{A.2. The repaired map and the scope of its uniqueness}',
            r'\subsection{The repaired map and its relative uniqueness}')
headings={
 'A.1.1':('proposition','The primitive integral quotient and its finite fillings'),
 'A.1.2':('proposition','Pointwise cusp obstruction and the corrected double curve'),
 'A.1.3':('proposition','The filled three-dimensional target'),
 'A.2.1':('theorem','The repaired map and its relative homotopy class'),
}
for sid,(env,title) in headings.items():
    pat=r'\\paragraph\{(?:Proposition|Theorem) '+re.escape(sid)+r' \([^\n]*\)\.\}'
    m=re.search(pat,s)
    if not m:raise RuntimeError(sid)
    p=s.index(r'\begin{proof}',m.end())
    statement=s[m.end():p].strip()
    s=s[:m.start()]+r'\begin{'+env+'}['+title+']'+r'\label{mapsI:src:'+sid+'}\n'+statement+'\n'+r'\end{'+env+'}\n\n'+s[p:]
for i in range(1,8):
    s=s.replace(r'\tag{A.1.'+str(i)+'}',r'\label{mapsI:quotient-eq-'+str(i)+'}')
    s=s.replace('(A.1.'+str(i)+')',r'\eqref{mapsI:quotient-eq-'+str(i)+'}')
s=s.replace('in the prompt','of the family construction')
s=s.replace("Lemma 3.8, labelled \\texttt{covect} in the supplied source\n\\cite{mapsEngel}.",
            r'Lemma~3.8 \cite[Lemma~3.8]{mapsEngel}.')
s=s.replace('the parenthesis in A.1 identifying the extendible\ncurve with the fixed curve is false',
            'the extendible double curve and the fixed double curve are distinct')
s=s.replace('This directly locates the\nincorrect identification in the prompt.',
            'This directly distinguishes the two geometrically different curves.')
s=s.replace('This is the precise sign convention in the supplied family\nreturn, B.2.2;',
            'This is the precise sign convention in Proposition~\\ref{fam:src:B.2.2};')
s=s.replace('the\nglobal cohomological obstruction K5','the\nglobal cohomological obstruction')
s=s.replace(r'$e:X\to Q$',r'$e_{\rm q}:X\to Q$')
s=s.replace(r'\texttt{code/maps\_exact.py}',r'\texttt{code/maps\_audit/MAPS/code/maps\_exact.py}')
out=OUT/'paperI_circle_quotient.tex';out.write_text(s)
record={
 'output':str(out.relative_to(ROOT)), 'source':str(source.relative_to(ROOT)),
 'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'output_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
 'transferred_results':list(headings), 'destination':'Paper I',
 'subsequent_placement':'Paper III retains MAPS A.2.2 and B homotopy results and cites these Paper I definitions/theorems.',
 'proof_preservation':'Four entire original statements and their full proofs preserved, including intermediate geometry and Engel convention dictionary. No proof duplicated in real-forms block.',
 'proof_check':{'reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','date':'2026-11-17','effort':'Pro','scope':'All four proofs read/rederived, maps_exact.py rerun. Cusp proof depends on independently checked toric fundamental-group calculation; distinct double curves rechecked from toric action.'},
 'external_labels':['fam:src:B.2.2'],
 'citation_keys':['mapsAC26','mapsEngel'],
}
(OUT/'paperI_circle_quotient_manifest.json').write_text(json.dumps(record,indent=2)+'\n')
print('Wrote',out.relative_to(ROOT),len(s),'characters')
