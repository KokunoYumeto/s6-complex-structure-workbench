#!/usr/bin/env python3
"""Create guarded old/new proposals only; never edit the main source."""
from pathlib import Path
import hashlib,json,re

root=Path('/workspace/scratch/653608133b22')
source=root/'work/S6_SERIES_PUBLISH_V.tex'
text=source.read_text()
patches=[]
def add(pid,old,new):
    n=text.count(old)
    if n!=1:raise ValueError((pid,'guard occurrence count',n))
    patches.append({'id':pid,'expected_count':1,'old':old,'new':new})
def span(label,start,end):
    anchor=text.index('\\label{'+label+'}')
    a=text.index(start,anchor);b=text.index(end,a)
    return text[a:b]
def record(label,new_dependencies):
    pattern=r'\\StatementRecord\{'+re.escape(label)+r'\}\{[^\n]*'
    old=re.search(pattern,text).group(0)
    prefix=old.split('}{',3)
    new='}{'.join(prefix[:3])+'}{'+new_dependencies+'}'
    add('record_'+label,old,new)

add('define_lambda',r'We use column vectors and the integral cohomology matrices',
    r'Let $\Lambda=\mathbb Z^6$ be the marked homology lattice, with column vectors. We use the integral cohomology matrices')
add('self_contained_cusp_hypotheses',
    'Under the index-one condition of \\cref{def:admissible}, the cusp matrix is\nconjugate in $\\operatorname{GL}_6(\\mathbb Z)$ to',
    'Let $N=M_0-I$ satisfy $N^2=0$, $\\operatorname{rank}N=3$,\nand suppose that $\\operatorname{im}N$ is primitive in\n$\\Lambda=\\mathbb Z^6$. Then $M_0$ is conjugate in\n$\\operatorname{GL}_6(\\mathbb Z)$ to')
add('local_period_inputs',
    'The periodic Kuhn fan, in the marking $S$, gives a smooth proper\nholomorphic filling of the periods $Z(q)=sI_3+C(q)$ for a sufficiently\nsmall disk.',
    'Let $C(q)$ be a holomorphic $3\\times3$ matrix on a disc about\nzero, and put $s=\\log q/(2\\pi i)$ on its punctured universal cover.\nAfter shrinking the disc, the periodic Kuhn fan in the marking $S$\ngives a smooth proper holomorphic filling of the periods\n$Z(q)=sI_3+C(q)$.')
old=span('pub:V:cusp-smooth-dependence','Let $C_t(q)$',
         '\\begin{theorem}[The central cusp fibre')
new=r'''Let $n\in\{2,3\}$ and let $C_t(q)$, $0\leq t\leq1$, be a
smooth family of holomorphic $n\times n$ matrix functions on a disc,
uniformly bounded on a smaller closed disc. After choosing a sufficiently
small common disc, the marked Kuhn fillings with periods
$[I_n\mid (\log q/(2\pi i))I_n+C_t(q)]$ are diffeomorphic over
that common disc. The diffeomorphisms preserve the central-fibre
strata and the marked angular and deck lattices. They can be chosen
on the outer collar to extend a smooth marked trivialization of the
regular torus bundles.
\end{lemma}
\begin{proof}
For the linear deformation $C_t=tC$,
\cite[Theorem~8.7, arXiv v1, pp.~57--58]{Yang2026} applies directly
in dimension $n$ to $D(q,s)=sC(q)$ for $|s|<2$.
For a smooth bounded family the same local charts give the following
comparison. The maximal toric charts have coordinates
$(z_0,\ldots,z_n)$ with $q=z_0\cdots z_n$. Their changes of
coordinates depend smoothly on $t$ and are toric monomials multiplied
by the holomorphic units $\exp(2\pi iC_t(q)\lambda)$.
They therefore define a smooth family of manifolds with the same
coordinate-stratum charts. The parameter vector field in each chart
lifts $\partial/\partial t$, fixes $q$, and is tangent to every
coordinate stratum. Differences of these lifts are vertical fields
with the same properties. A partition of unity gives a global lift;
on an outer collar take the prescribed lift from the regular marked
torus bundle and use a partition subordinate to that collar and the
interior charts.

For $y=\operatorname{Im}(\log q/(2\pi i))$, uniform boundedness
of the corrections gives, on a sufficiently small common disc,
\[
 \tfrac12\|\lambda\|\leq
 \|(I_n+y^{-1}\operatorname{Im}C_t(q))\lambda\|
 \leq\tfrac32\|\lambda\|,
 \qquad 0\leq t\leq1.
\]
The same fundamental-domain estimate as in the local filling theorem
therefore gives a proper family over the closed disc times $[0,1]$.
The lifted field has a flow for the entire parameter interval.
That flow fixes $q$, preserves each stratum, and has the specified
collar restriction. Since the parameter interval is contractible
and the lattice marking is constant there, its induced lattice map
is the identity.
\end{proof}

'''
add('common_uniform_cusp_deformation',old,new)
add('aw_step_locator',r"Poincar\'e-dual Alexander--Whitney formula in step 9.",
    r"Poincar\'e-dual Alexander--Whitney formula in the following item.")

anchor='\\begin{lemma}[The marked smooth gluing]'
support=r'''\begin{lemma}[Integral degree-two classes on the Kuhn filling]
\hypertarget{tag-PV13}{}\label{pub:V:cusp-chern-generators}
\StatementRecord{pub:V:cusp-chern-generators}{proved}{PV13}{\cref{pub:V:cusp-smooth-dependence}}
For the standard Kuhn filling with bounded correction zero, in dimension
$n=2$ or $3$, every integral symmetric matrix $S$ gives a line bundle
whose Chern class on a smooth fibre is
$\sum_{i,j}S_{ij}a_i\wedge b_j$.
Here $a_i$ are the angular classes and $b_i$ the invariant deck
classes in the marked product description. The corresponding classes
on the central fibre specialize to these classes on the smooth fibre.
The deck classes $b_i$ also lie in the specialization image, and
the marked bounded-correction comparison preserves these specialization images.
\end{lemma}
\begin{proof}
At a fan vertex $m\in\mathbb Z^n$ put
\[
 q_S(m)=\frac{m^tSm-\sum_iS_{ii}m_i}{2}.
\]
This is integral because $m_i^2-m_i$ is even. Interpolation on
each unimodular Kuhn simplex gives an integral piecewise-linear
support function. Translation by $\lambda$ changes it by the
integral affine function $m^tS\lambda+q_S(\lambda)$.
The associated Cartier data consequently have deck linearization
\[
 f_\lambda(x,q)=q^{-q_S(\lambda)}x^{-S\lambda}.
\]
The identity
$q_S(\lambda+\mu)=q_S(\lambda)+q_S(\mu)+\lambda^tS\mu$
gives $f_\lambda(q^\mu x,q)f_\mu(x,q)=f_{\lambda+\mu}(x,q)$,
so the line bundle descends to the period quotient.

For the Chern-class convention write $q=e^{2\pi i s}$,
$y=\operatorname{Im}s>0$, and $x_i=e^{2\pi iz_i}$ with
$z=u+sv$. Then $a_i=du_i$ and $b_i=dv_i$.
The Hermitian squared norm
\[
 h(z)=\exp\!\left(-\frac{2\pi}{y}
 (\operatorname{Im}z)^tS(\operatorname{Im}z)
 +2\pi\sum_iS_{ii}\operatorname{Im}z_i\right)
\]
satisfies $h(z+s\lambda)|f_\lambda(z)|^2=h(z)$.
Its Chern form is
\[
 \frac{i}{2y}\sum_{i,j}S_{ij}\,dz_i\wedge d\bar z_j
 =\sum_{i,j}S_{ij}\,du_i\wedge dv_j,
\]
where symmetry of $S$ cancels the angular--angular and deck--deck
terms. Restriction of the line bundle to the central fibre gives
the stated specialization classes. The projection to the deck torus
in the moment-cell model supplies the classes $b_i$.
Finally \cref{pub:V:cusp-smooth-dependence} identifies the marked
collapse maps under a bounded correction, and hence transports
these integral classes and their specialization images.
\end{proof}

'''
add('restore_unique_cusp_support_function',anchor,support+anchor)
add('smooth_gluing_map',
    'translation clutch, gives a closed connected oriented smooth\neight-manifold $M$. It is simply connected, has Euler number six,',
    'translation clutch, gives a smooth map $f:M\\to S^2$ from a\nclosed connected oriented smooth eight-manifold $M$. It is simply\nconnected, has Euler number six,')
add('initial_zero_correction',
    'At the cusp we take the index-one Kuhn cap of\nTheorem~\\ref{night:P1.9}, in the marking of\nProposition~\\ref{maps:src:F.2.1}.',
    'At the cusp we take the index-one Kuhn cap of\nTheorem~\\ref{night:P1.9} with $C(q)=0$, in the explicit marking\n$S$ of Theorem~\\ref{night:P1.1}.')
record('pub:V:smooth-gluing',r'\SeriesRef{night:P1.1}, \SeriesRef{night:P1.9}, \SeriesRef{night:P1.11}; \cite[Theorem 4.1.1 and Lemmas 4.1.2--4.1.3, pp.~480--482]{ffAchingerOgus20}')

old=span('pub:V:integral-restrictions','For the marked smooth gluing',
         '\\end{lemma}')
new=r'''Let $f:M\to S^2$ be the map of the marked smooth gluing in
\cref{pub:V:smooth-gluing}, and let $j:U\hookrightarrow S^2$
be the complement of its three special values $p_1,p_2,p_0$.
Put $\mathcal R_q=R^qf_*\mathbb Z$,
$\mathcal L_q=\mathcal R_q|_U$,
$\mathcal S_q=\operatorname{im}(\mathcal R_q\to j_*\mathcal L_q)$,
and $\mathcal K_q=\ker(\mathcal R_q\to j_*\mathcal L_q)$.
The fibres are connected, so $\mathcal R_0=\mathbb Z$.
For $1\leq q\leq4$ the image sheaf has
$H^2(S^2,\mathcal S_q)=\mathbb Z/2$; its only nonzero groups
in base degrees zero and one are
$H^0(S^2,\mathcal S_1)=\mathbb Z$ and
$H^1(S^2,\mathcal S_3)=\mathbb Z^3$.
Writing $i_a:\{p_a\}\hookrightarrow S^2$, its kernels are
\[
\mathcal K_1=0,\qquad
\mathcal K_2=\mathcal K_3=(i_2)_*(\mathbb Z/2),\qquad
\mathcal K_4=(i_2)_*(\mathbb Z/2)\oplus(i_0)_*\mathbb Z.
\]
For $q=2,3,4$, the torsion suspension generator at $p_2$ has
nonzero image in the global coinvariant group of
$\mathcal L_{q-1}$.
'''
add('restriction_statement_objects_and_kernels',old,new)
old=span('pub:V:integral-restrictions','\\item We use the marked construction',
         '$m_1=5$, $m_2=4$, and put')
new=r'''\item Use the marked smooth gluing of
\cref{pub:V:smooth-gluing}, the matrices and affine vectors of
\cref{pub:V:rank-six-data}, and the integral cusp-collapse maps
of \cref{night:P1.11}. The matrix $S$ is the explicit integral
marking in the first proof item of \cref{night:P1.1}.
Write
'''
add('restriction_proof_moved_inputs',old,new)
add('restriction_stalk_notation',
    'Consequently its image in $L_q=\\bigwedge^q\\mathbb Z^6$ is',
    'Consequently its image in the marked stalk\n$L_q=\\bigwedge^q\\mathbb Z^6$ of $\\mathcal L_q$ is')
old=span('pub:V:integral-restrictions',
         '\\item Let $\\mathcal R_q=R^qf_*\\mathbb Z$',
         'Since $M$ is compact and the base is Hausdorff,')
add('restriction_remove_late_duplicate_definitions',old,'\\item ')
add('degree_one_stalk_kernel',
    'The kernel\n$\\mathcal K_q$ is supported at those points: for $q=2,3$ it is the',
    'The kernel\n$\\mathcal K_q$ is supported at those points. It is zero for $q=1$,\nsince the degree-zero norm on the finite suspension group is\ninjective and the cusp restriction is injective. For $q=2,3$ it is the')
record('pub:V:integral-restrictions',r'\cref{pub:V:smooth-gluing}, \cref{pub:V:rank-six-data}, \SeriesRef{night:P1.1}, \SeriesRef{night:P1.11}; \cite[Tag 09V5, Lemma 20.18.1]{StacksProject}')
record('mapsaudit:order-four-torsion-transgression',r'\cref{pub:V:rank-six-data}, \cref{pub:V:integral-restrictions}')
add('transgression_define_D',
    'Let $T=\\bigwedge^{q-1}D^t$ on the integral vertical cochains of the',
    'Let $D$ be the bottom-right $5\\times5$ block of $M_2$, and put\n$T=\\bigwedge^{q-1}D^t$ on the integral vertical cochains of the')
add('transgression_remove_forward_equation_dependency',
    'These are the two successive boundaries in the same base--fibre\ncomplex, so their composition is the Leray $d_2$ of\n\\eqref{maps:eq:F.6}.',
    'These are the two successive boundaries in the same base--fibre\ncomplex, so their composition is the Leray $d_2$ for $f$.')
record('maps:src:F.2.6',r'\cref{pub:V:smooth-gluing}, \cref{pub:V:integral-restrictions}, \SeriesRef{mapsaudit:order-four-torsion-transgression}, \SeriesRef{sec:V-known-inputs}, \SeriesRef{maps:src:F.3.7}')

old=span('night:P1.13','\\item \\Cref{night:P1.12}',
         '\\item Duality makes the middle form unimodular.')
new=r'''\item By \cref{night:P1.12}, the integral groups in degrees two
and six vanish, so $c_1=c_3=0$.
The proposition \cref{sec:V-known-inputs} gives
$c_4[M_c]=6$, $c_2^2[M_c]=2$, $\sigma(M_c)=2$, and the
integral middle form $I_{3,1}$.
The Chern-root identities
$p_1=-2c_2$ and $p_2=c_2^2+2c_4$ then give
$p_1^2[M_c]=8$ and $p_2[M_c]=14$.

'''
add('characteristic_numbers_single_proof',old,new)
old=span('night:P1.13','\\item Duality makes the middle form unimodular.',
         'Since $H^2(M_c;\\mathbb Z/2)=0$')
add('middle_form_single_proof',old,'\\item ')
record('night:P1.13',r'\SeriesRef{night:P1.12}, \SeriesRef{sec:V-known-inputs}')
old=span('maps:src:F.4.1','\\item The integral calculation in',
         '\\item We compute the complete normal clutching datum')
new=r'''\item The theorem \cref{maps:src:F.2.6} gives three-connectivity,
Euler number six, and free homology of ranks $1,4,1$ in degrees
$0,4,8$. The complex orientation is the one in
\cref{maps:src:F.3.7}. By \cref{night:P1.13}, its middle pairing
is $Q=I_{3,1}$ and $p=p_1/2=-c_2$ is characteristic with square two.

\item Use the integral isometry supplied by the terminating descent
in \cref{night:P1.13}. In diagonal coordinates it is a matrix $U$
with $Up=(1,1,1,1)^t$. We use this specific isometry in the
comparison of normal data below.

'''
add('classification_use_characteristic_pair',old,new)

# Content references moved out of the old theorem aliases.
replacements=[
 ('family_zero_marked_pair',
  'exactly the marked pair in Theorem~\\ref{maps:src:F.2.5}, and',
  'exactly the marked pair of \\cref{pub:V:rank-six-data}, and'),
 ('other_pair_first_matrix',
  '\\item The first cohomological matrix is the same $A$ as in\nTheorem \\ref{maps:src:F.2.5}.',
  '\\item The first cohomological matrix is the same $A$ as in\n\\cref{pub:V:rank-six-data}.'),
 ('other_pair_restriction_table',
  '\\item We give the integral data needed to reuse the differential calculation of \\ref{maps:src:F.2.6}.  The rational exterior invariant and parabolic ranks\nare exactly the table there.',
  '\\item We give the integral data needed to reuse the differential\ncalculation of \\cref{mapsaudit:order-four-torsion-transgression}.\nThe image-sheaf cohomology ranks are those of\n\\cref{pub:V:integral-restrictions}, as the following integral data verify.'),
 ('other_pair_crt_explicit',
  'The degree-one coboundary is primitive and the degree-one\nfinite covering cokernels are killed by the common invariant\ncovector and the Chinese remainder theorem, exactly as in\n\\ref{maps:src:F.2.6}.',
  'The degree-one coboundary is primitive. The common invariant\ncovector maps to $(1\\bmod5,-1\\bmod4)$ in the degree-one\nfinite covering cokernels. Its map from $\\mathbb Z$ onto\n$\\mathbb Z/5\\oplus\\mathbb Z/4$ is surjective by the Chinese\nremainder theorem.'),
 ('other_pair_almost_complex',
  'The relative almost-complex extension over the pair of pants\nin \\ref{maps:src:F.2.5} applies:',
  'The relative almost-complex extension over the pair of pants\nin \\cref{pub:V:smooth-gluing} applies:'),
 ('twists_normal_closure',
  'lattice in the fibre lattice is exactly $\\ker\\ell$, by\n\\ref{maps:src:F.2.5} and \\ref{maps:src:F.2.18}.',
  'lattice in the fibre lattice is exactly $\\ker\\ell$, by\n\\cref{pub:V:smooth-gluing} and \\ref{maps:src:F.2.18}.'),
 ('twists_invariant_two_forms',
  'The integral invariant two-form computations in \\ref{maps:src:F.2.6} and\n\\ref{maps:src:F.2.18} give',
  'The integral invariant two-form computations in\n\\cref{pub:V:integral-restrictions} and \\ref{maps:src:F.2.18} give'),
 ('full_classification_almost_complex',
  'two-dimensional pair of pants, exactly as in \\ref{maps:src:F.2.5}.',
  'two-dimensional pair of pants, exactly as in \\cref{pub:V:smooth-gluing}.'),
 ('primitive_characteristic_reason',
  'Since $H^2=0$, $p_1/2=-c_2$ is primitive,\ncharacteristic, and has square two.',
  'The vanishing $H^2=0$ gives $c_1=w_2=0$, so $p_1/2=-c_2$.\nThe spin Wu identity makes this class characteristic, and its square\nis two. A nontrivial integral multiple of a lattice vector has square\ndivisible by the square of that integer; hence this norm-two class\nis primitive.'),
 ('inserted_site_normal_closure',
  'as proved in \\ref{maps:src:F.2.5}.\nAdding the identity linear generator',
  'as proved in \\cref{pub:V:smooth-gluing}.\nAdding the identity linear generator'),
 ('shifted_product_support_reference',
  'apply the support-function construction of \\ref{maps:src:E.1.3} in two\ncoordinates.',
  'apply \\cref{pub:V:cusp-chern-generators} in dimension two.')]
for pid,old,new in replacements:add(pid,old,new)

for label in ['maps:src:F.2.18','maps:src:F.2.24','maps:src:F.2.30','maps:src:F.2.32']:
    pattern=r'\\StatementRecord\{'+re.escape(label)+r'\}\{[^\n]*'
    old=re.search(pattern,text).group(0)
    new=old.replace(r'\SeriesRef{maps:src:F.2.5}',r'\cref{pub:V:smooth-gluing}')
    if label in ['maps:src:F.2.18','maps:src:F.2.24']:
        new=new.replace(r'\SeriesRef{maps:src:F.2.6}',r'\SeriesRef{maps:src:F.2.6}, \cref{pub:V:integral-restrictions}')
    if old!=new:add('moved_record_'+label,old,new)
label='maps:src:E.2.5'
old=re.search(r'\\StatementRecord\{'+re.escape(label)+r'\}\{[^\n]*',text).group(0)
new=old.replace(r'\SeriesRef{maps:src:E.1.3}',r'\cref{pub:V:cusp-chern-generators}')
add('shifted_product_record_support_dependency',old,new)

# Validate the entire proposed sequence in memory, checking every old guard again.
candidate=text
for p in patches:
    if candidate.count(p['old'])!=1:raise ValueError(('sequential_guard',p['id'],candidate.count(p['old'])))
    candidate=candidate.replace(p['old'],p['new'],1)
before_labels=re.findall(r'\\label\{([^}]+)\}',text)
after_labels=re.findall(r'\\label\{([^}]+)\}',candidate)
before_tags=re.findall(r'\\hypertarget\{(tag-[^}]+)\}',text)
after_tags=re.findall(r'\\hypertarget\{(tag-[^}]+)\}',candidate)
for lab in before_labels:
    assert after_labels.count(lab)==before_labels.count(lab),lab
for tag in before_tags:
    assert after_tags.count(tag)==before_tags.count(tag),tag
assert after_labels.count('pub:V:cusp-chern-generators')==1
assert after_tags.count('tag-PV13')==1
target=root/'work/agents/v_topology/S6_SERIES_PUBLISH_V_topology_guarded_patch.json'
target.write_text(json.dumps({'source':str(source),'source_sha256':hashlib.sha256(text.encode()).hexdigest(),'instruction':'Apply sequentially only when each old string occurs exactly once. No main-file edits were made by this script. Front matter and analytic F3.7/M_xi patches are deliberately excluded.','patches':patches,'validation':{'all_guards_unique':True,'all_existing_labels_and_tags_preserved_with_multiplicity':True,'new_label':'pub:V:cusp-chern-generators','new_tag':'PV13'}},indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'patch_file':str(target),'patches':len(patches),'source_sha256':hashlib.sha256(text.encode()).hexdigest(),'validated_in_memory':True}))
