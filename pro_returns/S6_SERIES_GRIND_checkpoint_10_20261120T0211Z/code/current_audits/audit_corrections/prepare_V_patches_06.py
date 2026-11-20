from pathlib import Path
import json,hashlib,datetime
p=Path('/workspace/scratch/6c4e6df38b6d/S6_SERIES_GRIND_work');s=(p/'parts/V.body.linked.tex').read_text();out=p/'audit_corrections';patch=[]
pref='code/current_audits/audit_corrections/code/'
def add(label,old,new,reason):
 n=s.count(old)
 if n!=1:raise ValueError((label,n,old[:120]))
 patch.append({'label':label,'old_text':old,'new_text':new,'reason':reason,'matches':n})
add('night:P1.1',r'''The files in \texttt{code/part1/} contain the complete
matrices, including the changes of basis in every Smith computation.''',r'''The exact matrix and affine calculations below use the displayed integral
data. Their current independent computations and the scope of each are
identified beside the corresponding formulas.''','Remove blanket assertion that absent historical directory contains all matrices; retain exact per-row arithmetic scope.')
add('night:P1.1',r'''The order and characteristic-polynomial
computations, and the full fixed-lattice calculations, are reproduced by
\texttt{tuple\_check.py}; its output records every power tested.''',r'''The orders, characteristic polynomials, fixed-space dimensions,
coinvariant Smith factors, primitive cusp image and every affine-power
obstruction are recomputed exactly in
\path{'''+pref+r'''independent_V_connection_spectra_06.py}.
Its JSON output retains each assertion. The displayed matrix $S$ and its
standard-form equality are also verified in
\path{'''+pref+r'''independent_V_markings_06.py}.''','Fresh programs match the listed linear/affine scope; no claim to replay absent tuple_check.py or unexported Smith change matrices.')
add('night:P1.4',r'''The discriminant and all substitutions are
checked in \texttt{pencil\_charts.py/.out}.''',r'''The discriminant, the nodal root and its transverse derivatives,
both exact root substitutions, square-freeness of the central polynomials,
and the line degree are recomputed in
\path{'''+pref+r'''independent_V_markings_06.py}, with its exact JSON output.''','Replace absent historical execution by newly reconstructed complete displayed algebraic checks; the geometric differential/deck argument remains printed.')
add('night:P1.5',r'''The formula in the prompt with $P$ the image of
$\ell_0\wedge\mathcal H$, and $\mathcal H$ the rank-two Hodge bundle,
cannot produce a rank-three subbundle.  The required rank-three image
is instead the image of $\ell_0\wedge\mathcal H_{\mathrm{dR}}$, where
$\mathcal H_{\mathrm{dR}}$ is the full rank-four de Rham bundle.''',r'''For the Hodge line $\ell_0\subset\mathcal H$ of the genus-two pencil,
the image of $\ell_0\otimes\mathcal H\to\bigwedge^2\mathcal H$
has rank one. The wedge map from
$\ell_0\otimes(\mathcal H_{\mathrm{dR}}/\ell_0)$, followed by
projection modulo the nondegenerate polarization bivector, is
injective and has rank-three image. This image defines the bundle
$P$ used in the period construction.''','Make the correction standalone using precisely the explicit wedge/projection map proved below; no scope widening.')
add('night:P1.7',r'''The invariant forms, integral inverses, peripheral
words and exterior minors are independently reproduced in
\texttt{P1\_7\_integral\_marking\_fresh.py} in the directory 
\texttt{code/continuation\_root/}.''',r'''The invariant form, actual Picard--Lefschetz rank-one map,
unimodular orbit matrix, integral inverse, reversal, based peripheral
word and exterior-quotient identities are recomputed exactly in
\path{'''+pref+r'''independent_V_markings_06.py}; its JSON output records those checks.
The integral saturation argument in steps 2--4 supplies the map $\mu$
for the actual geometric lattice.''','Fresh complete printed matrix scope, with geometric saturation still proved in text; do not claim absent historical producer was run.')
add('night:P1.8',r'''real parameters giving $F_c\cap\overline{F_c}=0$ everywhere is
$c>-h_{\min}$.''',r'''real parameters giving $F_c\cap\overline{F_c}=0$ on the completed
base, including both finite root points and excluding only the cusp
before its toroidal filling, is $c>-h_{\min}$.''','Explicitly retain finite-root testing: P1.18 locates the minimum at the infinity root, so the strict endpoint belongs to the completed-family criterion.')
add('night:P1.8',r'''These polynomial identities, with arbitrary symbols for the entries of
$a,b$, are checked in \texttt{cusp\_lift\_asymptotic.py}.''',r'''The full scalar and quotient-kernel identities for arbitrary symbolic
entries of $a,b$ are checked directly from the displayed companion and
rank-six matrices in
\path{'''+pref+r'''independent_V_markings_06.py}.''','Fresh exact full cusp identity, retaining all terms; no numerical or central-only substitute.')
add('night:P1.8',r'''Connectedness and the intermediate value
theorem give $h(U)=[h_{\min},\infty)$, with finite-root points included
when testing the completed family.''',r'''Connectedness and the intermediate value theorem give
$h(\widehat B\setminus\{\text{cusp}\})=[h_{\min},\infty)$,
where both finite root points are included.''','Remove ambiguity between the regular punctured base U and the completed base on which the attained minimum is tested.')
add('night:P1.8',r'''\paragraph{Scope of P1.8.}
The definition of $h$ is exact and specifies its normalization, its
range, and its cusp growth.  We have not evaluated $h_{\min}$ or
supplied the two independent thirty-digit period calculations requested
in item 1.4.  These numerical requirements remain separately recorded;
they are not consequences of the existence proof.''',r'''\paragraph{Normalization and evaluation.}
The construction above specifies $h$, its normalization, range and cusp
growth. The exact minimum and the translation to the algebraic splitting
are evaluated in \cref{night:P1.18}, using the connection of
\cref{night:P1.15}.''','Replace obsolete unfinished-work claim; completed numerical theorem is an explicit later dependency, not inferred from the existence proof.')
add('night:P1.15',r'''Taking the exterior-square connection and this quotient gives
(1.15.2), as checked symbolically in \texttt{de\_rham\_connection.py}.''',r'''Taking the exterior-square connection and this quotient gives
(1.15.2). The polynomial reduction, all exact primitives, the horizontal
polarization relation and all twenty-five quotient entries are reconstructed
in \path{'''+pref+r'''independent_V_connection_spectra_06.py} and its JSON output.''','Fresh independent symbolic reduction matches complete displayed lower-connection scope; no inference about upper extension from numerics.')
add('night:P1.15',r'''Existence follows from P1.15; uniqueness follows from the
scalar centralizer, whose exact linear equations are in
\texttt{centralizer\_torsion.py}.''',r'''Existence follows from the flat-extension identification in P1.15.
The exact simultaneous commutator equations for $A,B$ have a
one-dimensional solution space spanned by the identity; this is checked
in \path{'''+pref+r'''independent_V_extension_06.py}.
The same program verifies the root-regular extension terms, the nilpotent
residue quotient and the contraction normalization used in that proof.
The condition $Xe_0=e_0$ removes the scalar freedom and proves uniqueness.''','Separate exact existence from scalar uniqueness and computational approximation; fresh exact equations replace missing historical file.')
add('night:P1A.1',r'''Their constants form precisely the cellular
cochain complex of the dual three-torus, with the incidences in
\path{code/part1/cusp_complex.json}. Its cohomology is
$\bigwedge^q\mathbb C^3$, and its cup product is the exterior product.''',r'''Their constants form the cellular cochain complex of the periodic
Kuhn triangulation modulo $\mathbb Z^3$: its simplices are the faces of
$(0,e_{\pi(1)},e_{\pi(1)}+e_{\pi(2)},(1,1,1))$ for
$\pi\in S_3$, identified by integral translations. The quotient map
$x\mapsto x\bmod\mathbb Z^3$ identifies its realization with the dual
three-torus and respects every face map. Its cohomology is
$\bigwedge^q\mathbb C^3$, with the exterior cup product.
The face incidences, unit Smith factors and the Alexander--Whitney
products of the three coordinate cocycles are reconstructed in
\path{'''+pref+r'''independent_V_analytic_06.py} and its JSON output.''','Replace missing cusp_complex.json by actual explicit periodic simplicial maps and fresh complete constant-cochain/cup calculation. This is coherent dual-complex scope, not the full P1.11 topological cusp.')
add('night:P1A.2',r'''These entries result from the exact Gauss--Manin reduction of
P1.15, with the quotient projection taken after lifting $F$.
They are independently recomputed in
\path{code/part1/analytic_cohomology.py}.''',r'''These entries result from the exact Gauss--Manin reduction of
P1.15, with the quotient projection taken after lifting $F$.
The full projected residue and both connecting determinants are
recomputed in \path{'''+pref+r'''independent_V_analytic_06.py}.
Its JSON output also records the root-line cohomology sums used below.''','Fresh explicit P*Gamma6*F projection matches every entry and excludes dimension-only inference.')
old=r'''P1.15 identifies
$z=-(625\pi/128)c$ on the real slice in its algebraic splitting.
The exact exceptional parameter is therefore $c=5/(3\pi)<1$.
The certified continuation in
\path{code/part1/certified_lift_bound.py} proves
\[
\begin{aligned}h_b(1)\in\bigl[&'''
# Locate the complete obsolete certification paragraph by exact current anchors.
a=s.index('P1.15 identifies\n$z=-(625\\pi/128)c$');b=s.index('Consequently the three connecting ranks are $1,3,1$.',a)
add('night:P1A.2',s[a:b],r'''P1.15 identifies $z=(625\pi i/128)\xi$ on the full complex
parameter plane, and hence $z=-(625\pi/128)c$ when $\xi=ic$.
The unique exceptional parameter is therefore
$\xi=5i/(3\pi)$. By \cref{night:P1.18}, the admissible half-plane is
$\operatorname{Im}\xi>-h_{b,\min}>1$, whereas $5/(3\pi)<1$.
Thus this zero lies outside the whole admissible parameter domain.
The bound used here is the complete current certificate of
\cref{night:P1.18}; no separate historical continuation program is required.
''','The complete fresh global certificate already proves the needed strict exclusion. Preserve exact complex parameter map and remove unsupported historical execution assertion.')
add('night:P1A.2',r'''The program verifies this polynomial exactly.''',r'''The exact Chern-number substitution and the resulting polynomial are
verified in \path{'''+pref+r'''independent_V_analytic_06.py}.''','Match new program scope: substitution consistency, with universal analytic RR still supplied by opened source and printed derivation.')
add('night:P1A.4',r'''Solving the two exact matrix equations in
\path{code/continuation_root/P1A4_integral_fresh.py} gives the rational
centralizer $\mathbb Q I$; its integral invertible elements
are $\pm I$.''',r'''The two simultaneous commutator equations have rational solution
space $\mathbb QI$, as recomputed in
\path{'''+pref+r'''independent_V_extension_06.py}; their integral invertible
elements are therefore $\pm I$.''','Fresh exact commutator solution dimension and identity span replace absent historical program.')
add('night:P1A.4',r'''All displayed bases, the integral elimination and the coordinate
identity are checked independently in
\path{code/continuation_root/P1A4_integral_fresh.py}.''',r'''The norm-kernel ranks, primitive column bases, full identity
$(B-I)T=KZ$ and Smith factors are recomputed exactly in
\path{'''+pref+r'''independent_V_analytic_06.py}.
The same output verifies the zero invariant alternating space and,
for the half-period below, the explicit integral subtraction
$\tau-e_4\in\ker N$ in the zero-based six-coordinate convention.''','Complete fresh displayed quotient scope; does not claim the absent eleven-generator historical comparison was rerun.')
add('night:P1.17',r'''The equations and this certificate are in
\texttt{centralizer\_torsion.py} and
\texttt{real\_structure\_check.py}.''',r'''The exact anti-intertwiner equations, their one-dimensional rational
solution space, unimodularity of $R$, the based cusp block and the
specific ray obstruction below are recomputed in
\path{'''+pref+r'''independent_V_markings_06.py} and its JSON output.''','New program matches the full displayed linear/cusp obstruction, with actual extension argument retained in body.')
add('night:P1B.2',r'''The executed program \texttt{code/part1/spectral\_filter.py}
enumerates every exponent vector satisfying total degree six
and a positive exponent at $\Phi_1$, with bounds supplied by
these degrees. It writes all thirty-eight exponent vectors,
polynomials and least common multiples of their active indices.''',r'''The exact enumeration in
\path{'''+pref+r'''independent_V_connection_spectra_06.py}
visits every cyclotomic exponent vector of total degree six with a
positive exponent at $\Phi_1$, using the displayed degree bounds.
Its JSON output retains all thirty-eight exponent vectors, their
linear orders and both real-eigenspace parity tests.''','Fresh finite enumeration complete, not a replay or a claim of global gluing classification.')
# Optional definition clarification, separately flagged for root review.
add('night:P1A.6',r'''A holomorphic punctured-disc family whose fibres are all
members of this fourfold family has an interior parameter
limit.''',r'''Let $p:\mathcal M\to\Delta^*$ be a proper holomorphic submersion
whose fibres are members of this fourfold family. Its classifying
parameter has an interior limit.''','State the smooth proper family hypothesis used by local miniversality and the torsor proof explicitly; interpret the existing term family at its operative scope. Root should confirm the established family convention.')
receipt={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source':'parts/V.body.linked.tex','source_sha256':hashlib.sha256(s.encode()).hexdigest(),'patch_count':len(patch),'all_guards_unique':True,'fresh_assertions':186,'scope':'Every historical execution replacement has a newly reconstructed matching displayed scope. P1.19 full global matrices remain unresolved and are deliberately not patched into a fresh certificate.'}
(out/'V_guarded_patches_06.json').write_text(json.dumps(patch,indent=2));(out/'V_guarded_patches_receipt_06.json').write_text(json.dumps(receipt,indent=2));print(json.dumps(receipt))
