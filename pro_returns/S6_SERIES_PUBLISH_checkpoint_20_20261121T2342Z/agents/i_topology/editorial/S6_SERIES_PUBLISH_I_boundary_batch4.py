from pathlib import Path
import re,json,hashlib,datetime
P=Path(__file__).resolve().parent;initial=Path('work/S6_SERIES_PUBLISH_I.tex').read_text();s=initial;patches=[];archive=[]
def patch(old,new,why,ids=[]):
 global s
 ident='I-topology4-%02d'%(len(patches)+1);assert s.count(old)==1,(ident,s.count(old),old[:100])
 patches.append(dict(id=ident,old=old,new=new,reason=why,statement_ids=ids));s=s.replace(old,new,1)
def block(lab):
 i=s.index('\\label{'+lab+'}');a=s.rfind('\\begin{',0,i);b=s.index('\\end{proof}',i)+len('\\end{proof}');return s[a:b]
# State the precise sheaves and restriction maps positively.
old=r'''Here the torsor is formed from the \emph{associated
log-torus sheaves}, not from the fixed proper fan models
themselves, which need not be group objects. The conclusion
excludes an origin cap obtained from a locally trivial
torsor of this specified kind with the given axial
identifications. No implication from an arbitrary proper
analytic cap with vertical threefold components to this
torsor category is asserted.'''
new=r'''On each axial chart its extending origin identifies the associated sheaf with the Jacobian log-torus sheaf $\mathcal A$. On the overlap the two identifications differ by the section $F$ in (\ref{push:src:B.4.24}.3). An extension here is a locally trivial $\mathcal A$-torsor carrying these prescribed axial identifications.'''
patch(old,new,'State the exact associated-sheaf maps and extension datum positively.', ['push:src:B.4.24'])
old=r'''This result concerns the specified associated
log-torus sheaf. It does not assert that flattening
or resolving an arbitrary analytic origin cap
produces a torsor under that sheaf.'''
new=r'''Writing $U_S=\beta^{-1}(B\setminus\{0\})$, the extension datum is an $\mathcal A_S$-torsor whose restriction along the isomorphism $\beta|_{U_S}:U_S\to B\setminus\{0\}$ is the specified axial torsor.'''
patch(old,new,'Specify the actual restriction morphism defining the extension problem.', ['push:src:B.4.27'])
patch('components of the origin fibre. No K\\"ahler or\nprojective hypothesis is imposed on a putative\ncompletion.','components of the origin fibre.','The quantified class of all proper Hausdorff analytic completions already states the complete scope.', ['push:src:B.4.30'])
old=r'''This holds for every proper global filling. It
does not assert that the unknown rank-one axial completion is
the prescribed model of \ref{push:src:B.4.19}, or that an affine origin in one
model extends into the other.'''
patch(old,'','Retain the full quantified filling hypothesis and exact meridian conclusion without a repeated disclaimer.', ['push:src:B.4.31'])
old=r'''Refining a fan does not
replace the pairing or its associated quotient
sheaf; we use the explicit presentations, without
claiming that an arbitrary proper model determines
such a presentation.'''
new=r'''The identity on the character and period lattices identifies the associated quotient sheaves under a fan refinement: both are defined by the same multiplicative pairing (\ref{push:src:B.4.24}.1).'''
patch(old,new,'Give the identity map inducing the associated-sheaf comparison.', ['push:src:B.4.24'])
old=r'''\item \emph{The full gauge and the scope of the conclusion.}
There is no contradiction with \ref{push:src:B.4.19}'s identity'''
patch(old,r'''\item \emph{The ordinary gauge.}
The exact identity in Proposition~\ref{push:src:B.4.19} is''','Present the actual gauge identity directly.', ['push:src:B.4.24'])
old=r'''The ordinary gauge $kv\delta$ is not an extending
log section at $q=0$. Equation (\ref{push:src:B.4.24}.7) gives
the correct raw overlap and its fan extension
on $q\ne0$; it is not an allowed change of
both axial log-group origins. Changing either
origin by a section that does extend along its
own axis changes the clutching section by one
of the two terms already excluded by the
ghost calculation.'''
new=r'''On $q\ne0$, this is the raw overlap in the ordinary gauge. Its second multiplicative character is
\[
 e^{-2\pi i kv}=Q^{12v}e^{-24\pi i\kappa_0v},\qquad q=Q^{12}.
\]
The second factor is a holomorphic unit on a fixed branch of $\log r$. A bounded logarithmic character at $Q=0$ has integral $Q$-order, while $12v$ varies with $r$. Multiplication by a period changes that order by an integer. Thus this gauge cannot give an extending log-torus section along the full $Q$-axis. Changes of the two extending axial origins instead lie in the image of
\[
 H^0(B_q,\mathcal A)\oplus H^0(B_r,\mathcal A)
 \longrightarrow H^0(U,\mathcal A),\qquad(h_q,h_r)\longmapsto h_r-h_q.
\]
The ghost calculation shows that $F$ lies outside this image.'''
patch(old,new,'Make the nonextension of the ordinary gauge explicit through its character order and the actual axial difference map.', ['push:src:B.4.24'])
patch('This proves (\\ref{push:src:B.4.27}.3), including at crossings\nand at intersections with $D_R$; replacing the\nbounded sheaf by the full log-character sheaf\nin both coordinates would be incorrect.','This proves (\\ref{push:src:B.4.27}.3), including at crossings\nand at intersections with $D_R$. In particular the first character has zero order along $D_R$.','Keep the exact bounded-character condition positively.', ['push:src:B.4.27'])
patch('We record the elementary ingredients to fix\nthe analytic scope. For a point blowup $p$ of','For a point blowup $p$ of','Remove process introduction before the concrete cohomology proof.', ['push:src:B.4.27'])
patch('map is injective over $\\Z$, not merely over\n$\\Q$.','integral map is injective.','State the proved integral injectivity directly.', ['push:src:B.4.27'])
# The zero-loop essential translation is already an explicit proved example.
a=s.index('\\paragraph{Scope of the loop calculation}');b=s.index('\\section{The cotangent direct images',a);old=s[a:b];archive.append(dict(statement_id='post-B432-loop-scope',original_block=old))
new=r'''\begin{remark}[A zero loop class with a nonextending translation]
\hypertarget{tag-PT07}{}\label{I:zero-loop-essential-translation}
\StatementRecord{I:zero-loop-essential-translation}{proved}{PT07}{\SeriesRef{push:src:B.4.29}}
In Proposition~\ref{push:src:B.4.29}, the additive lift of the translation is $h(t)=1/t$. It is single-valued on the punctured disc, so its radial deck difference and loop class are zero. Its translated zero section has the two distinct central limits computed there, and hence the translation has no meromorphic extension. The loop class and the affine comparison are related by the endpoint-period map used in Proposition~\ref{push:src:B.4.32}; this example has zero image under that map.
\end{remark}

'''
patch(old,new,'Retain the actual zero-loop counterexample with its exact endpoint-period map; remove process prose and relocate the program reference.', ['I:zero-loop-essential-translation'])
# Number the actual boundary conventions.
a=s.index('We use the standard twists throughout this section. Put');b=s.index('\\subsection{The intrinsic obstruction',a);old=s[a:b]
new=r'''\begin{definition}[Boundary coordinates and the Hausdorff reflection]
\hypertarget{tag-PT08}{}\label{I:def:boundary-coordinates}
\StatementRecord{I:def:boundary-coordinates}{proved}{PT08}{}
For the standard twists put $H_*=(3/\pi)\log6$, fix $c_*=x+iH_*$ and set $a=x+3/2$. All topological group quotients carry their quotient topology. A Hausdorff reflection is a continuous quotient universal for continuous maps to Hausdorff spaces.
\end{definition}

'''
patch(old,new,'Number the existing parameter and quotient conventions without an unproved categorical contrast.', ['I:def:boundary-coordinates'])
# One natural-boundary proof, transported by the exact parameter map.
b11=block('push:src:D.1.1');archive.append(dict(statement_id='push:src:D.1.1',original_block=b11));a=b11.index('\\item For completeness we reproduce');b=b11.index('\\end{enumerate}',a)
new=b11[:a]+r'''\item Proposition~\ref{fam:src:C.3.4} proves the natural boundary in the $c$-coordinate for this exact Albanese lattice. The parameter map is $w=e^{-\pi i c}$, with nonzero derivative at every finite $c$. A local inverse logarithm at a point of $|w|=216$ maps that circle to $\operatorname{Im}c=\log216/\pi=H_*$. A meromorphic continuation in $w$ would pull back to the excluded continuation in $c$.
'''+b11[b:]
patch(b11,new,'Use the already proved natural boundary once through the explicit locally invertible exponential parameter map.', ['push:src:D.1.1'])
# Exact existing natural transformations replace defensive wording.
old=r'''This is a statement in the original,
possibly non-Hausdorff central fibre. Its own Hausdorffization is the
rank-three quotient described in \cref{fam:src:C.3.1}, \cref{fam:src:C.3.2}; it is not the central fibre of
\(\mathcal T^{\mathrm H}\).'''
new=r'''The natural map from this central quotient to the central fibre of $\mathcal T^{\mathrm H}$ is $[(\eta,\xi)]\mapsto\operatorname{Re}\xi\bmod G_a$ for rational $a$, and the constant map for irrational $a$, as in Theorem~\ref{push:src:D.2.3}. It is well defined because the real second coordinate of every central period belongs to $G_a$.'''
patch(old,new,'Give the exact map from the central quotient to the family reflection.', ['push:src:D.2.4'])
old='and the final good locus is open; we do not assert that successive\nexceptional sets cannot accumulate at an earlier removed point.'
patch(old,'and the final good locus is open.','Retain the precise countability and openness conclusion once.', ['push:src:D.1.2'])
old='''Its proper image is
analytic by Grauert (1960, \\S7, Satz~1), the proper mapping theorem.'''
new='''Its proper image is analytic by the coherent direct-image argument in Theorem~\\ref{night:P2.4}, applied to the structure sheaf of this proper analytic locus.'''
patch(old,new,'Use the already proved precise proper-image argument with its coherent sheaf map.', ['push:src:D.1.2'])
old=r'''Grauert's direct-image theorem
(1960, \S6, Hauptsatz~I) makes \(F=\pi_*L\) and \(R^1\pi_*L\)
coherent. We prove the needed base change directly over the smooth
curve; we do not use the originally stated \S7, Satz~2, whose claimed
closed exceptional locus was corrected in Grauert's 1963 erratum.'''
new=r'''Grauert's direct-image theorem \cite[\S6, Hauptsatz~I, p.~59]{Grauert1960D} makes \(F=\pi_*L\) and \(R^1\pi_*L\) coherent. His erratum \cite[item~2, p.~36]{Grauert1963ErratumD} corrects the assertion in \S7, Satz~2 that the locus where the comparison map fails to be bijective is always closed. For the present smooth curve, the following exact sequence computes the canonical base-change map and its torsion obstruction.'''
patch(old,new,'State the actual coherent direct image and canonical curve base-change argument; the general corrected theorem is already cited in the common foundation.', ['push:src:D.1.2'])
# Pure wording/program movements preserve the complete formulas and their analytic error estimates.
repls=[
('The coefficient arithmetic is independently checked in\n\\texttt{d\\_push\\_exact.py}. In particular','In particular'),
('This argument checks the\nquadratic coefficient omitted by the proposed first-order approximation.',''),
('The\nquadratic model calculation and its integer coefficients are checked\nexactly in \\texttt{d\\_push\\_exact.py}; the analytic error is','The analytic error is'),
('the asserted complex line is','the line $\\mathbb C(2,-1)^t$ is'),
('their difference is not in the asserted relation.','their difference has nonzero imaginary second coordinate modulo that line and the central periods.'),
('Multiplication by \\(A^t\\) proves the formula; the entire equation is\nchecked symbolically in \\texttt{d\\_push\\_exact.py}.','Multiplication by \\(A^t\\) proves the formula.'),
('They are assertions about real topological and\nmetric groups, not complex tori of a varying complex dimension.','Their group structures and quotient metrics are the ones displayed above.'),
('We verify properness of the reflected map, rather than assume it.\nOn a closed small base disc','On a closed small base disc'),
('These functions descend through the proposed quotient','These functions descend through this quotient'),
('The program \\texttt{d\\_push\\_gradient.py} cross-checks the identity\nagainst a separate symmetric difference of the theta-product norm;\nthat numerical check is not needed for the algebraic proof.',''),
('zero, tangent to the imaginary axis. This proves the crossing value\nand its local regularity requested in \\ref{push:section:D.4}, without using an unproved\nclosed form for \\(\\beta^{\\rm part}(z_1)\\).','zero, tangent to the imaginary axis.'),
('We verify regularity in the coarse coordinate rather than infer it\nfrom the ramified modulus. Multiplication','For regularity in the coarse coordinate, multiplication'),
('nonzero, as in \\ref{push:src:D.4.5}. The earlier interval proof and its 400 local rectangles remain in\nthe S6\\_09 proof compendium under this label. We give the consequence\nof the full critical-point classification here.','nonzero, as in \\ref{push:src:D.4.5}.'),
('and Hausdorff reflection are those of \\ref{push:src:D.4.3}. Thus this statement\nclassifies the locus and the local degeneration requested in D.4.','and Hausdorff reflection are those of \\ref{push:src:D.4.3}.')]
for old,new in repls:patch(old,new,'Remove process prose or relocate a program reference while retaining every displayed formula and analytic estimate.')
b45=block('push:src:D.4.5');a=b45.index('\\item The degree-three lattice matrix');b=b45.index('\\end{enumerate}',a)
patch(b45,b45[:a]+b45[b:],'Move the program-only final paragraph to the program table; all four analytic proof steps remain.', ['push:src:D.4.5'])
# Mathematical titles for all still untitled statements in this assigned D block and the named B statements.
for lab,typ,title in [
('push:src:D.1.1','proposition','The natural boundary in the multiplicative parameter'),
('push:src:D.1.2','lemma','The intrinsic anticanonical surface family'),
('push:src:D.2.1','lemma','The quadratic normal form at the boundary'),
('push:src:D.2.3','theorem','The Hausdorff reflection of the boundary family'),
('push:src:D.2.4','proposition','The finite boundary quotient and its leaves'),
('push:src:D.3.1','theorem','All marked limiting period groups'),
('push:src:D.3.2','corollary','Path dependence of the limiting torus'),
('push:src:D.4.1','proposition','The small supercritical level curve'),
('push:src:D.4.2','proposition','The maximal open locus and the negative region'),
('push:src:D.4.3','proposition','Closed period groups at a rank-three fibre'),
('push:src:D.4.4','proposition','The derivative along the moving Weierstrass zero'),
('push:src:D.4.5','proposition','The equianharmonic crossing'),
('push:src:D.4.7','proposition','Nonvanishing near the elliptic points and cusp'),
('push:src:D.4.8','proposition','The supercritical level classification'),
('push:src:B.4.15','proposition','Local insertion of vertical Hopf bundles')]:
 b=block(lab);h=b[:b.index('\\StatementRecord')];needle='\\begin{'+typ+'}\\hypertarget';assert needle in h
 patch(h,h.replace(needle,'\\begin{'+typ+'}['+title+']\\hypertarget',1),'Give the statement its short mathematical title.',[lab])
# Capitalize existing mathematical titles within our four section blocks, without changing their content.
for start,end in [('\\section{The boundary of the parameter disc}','\\section{The limit at the puncture}'),('\\subsection{Nonexistence of a proper analytic filling}','\\section{The cotangent direct images')]:
 a=s.index(start);b=s.index(end,a);chunk=s[a:b]
 for m in list(re.finditer(r'\\begin\{(theorem|lemma|proposition|corollary|remark)\}\[([a-z][^\]]*)\]',chunk)):
  old=m.group(0);new=old[:old.index('[')+1]+m.group(2)[0].upper()+m.group(2)[1:]+']'
  if s.count(old)==1:patch(old,new,'Capitalize the existing mathematical title.')
# Exact anchors.
pat=r'\\label\{([^}]+)\}|\\hypertarget\{(tag-[^}]+)\}'
def anchors(t):return [a or b for a,b in re.findall(pat,t)]
a0=anchors(initial);a1=anchors(s);lost=[x for x in a0 if a1.count(x)<a0.count(x)];dups=[x for x in set(a0) if a1.count(x)>a0.count(x)];assert not lost,lost;assert not dups,dups
(P/'S6_SERIES_PUBLISH_I_boundary_batch4_guarded.json').write_text(json.dumps(dict(input_sha256=hashlib.sha256(initial.encode()).hexdigest(),created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),patches=patches,anchor_check=dict(lost=lost,duplicates=dups,new=[x for x in a1 if x not in a0])),indent=2))
(P/'S6_SERIES_PUBLISH_I_boundary_batch4_preview.tex').write_text(s)
(P/'S6_SERIES_PUBLISH_I_boundary_batch4_archived_proofs.json').write_text(json.dumps(archive,indent=2))
print(dict(patches=len(patches),removed_chars=len(initial)-len(s),new_anchors=[x for x in a1 if x not in a0]))
