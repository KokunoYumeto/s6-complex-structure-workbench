#!/usr/bin/env python3
"""Build guarded corrections found by actual visual reading of pages55–96."""
from pathlib import Path
import hashlib,json,re

root=Path('/workspace/scratch/653608133b22/work')
folder=root/'agents/v_topology'
source=root/'S6_SERIES_PUBLISH_V.tex'
original=source.read_text()
text=original
patches=[]

def add(identifier,old,new):
    global text
    assert text.count(old)==1,(identifier,text.count(old))
    patches.append(dict(id=identifier,expected_count=1,old=old,new=new))
    text=text.replace(old,new)

add('p056_remove_translation_contrast',
    'part, not only to integral or invariant choices.',
    'part.')
add('p056_remove_polynomial_count_disclaimer',
    'with some real complex structure.  These are necessary types,\nnot 38 or 19 conjugacy classes of admissible tuples.',
    'with some real complex structure.')
add('p056_remove_linear_filter_scope_repetition',
    '  This is a bounded exhaustive enumeration for the\nstated filter.  It does not bound affine multiplicities when\nthe affine action has larger order than its linear part.', '')
add('p057_resolved_part_reference',
    'checks this hypothesis for the fibre-product example of Part~I.',
    r'checks this hypothesis for the fibre-product example of Part~\ref{pub:V:part-resolved}.')
add('p057_remove_rank_existence_disclaimer',
    '  No existence of a tuple or of a\nperiod family with these ranks is asserted.', '')
add('p059_cite_the_actual_leray_argument',
    r'for the finite fixed ranks.  Theorem \ref{maps:src:F.3.1} gives $a=1$,',
    r'for the finite fixed ranks.  The Leray argument in the proof of Theorem \ref{maps:src:F.3.1} gives $a=1$,')
add('p062_remove_repeated_stable_lattice_sentence',
    '\nThe determinant argument applies to every stable lattice.\n','\n')
add('p063_remove_wang_lift_disclaimer',
    'No choice of lifts of the vertical Wang classes changes this\nquotient or its kernel.  At the first finite cap,',
    'At the first finite cap,')
add('p066_remove_repeated_unbounded_index_scope',
    'This proves the assertion for all invariant lattices, with no\nbound on their indices.\n','')
add('p067_remove_wang_splitting_disclaimer',
    'image.  Thus no choice of a Wang splitting changes this quotient.',
    'image.')
add('p069_combine_cusp_references',
    r'cap of \cref{night:P1.9}, \cref{night:P1.11} by the',
    r'cap of \cref{night:P1.9,night:P1.11} by the')
add('p070_remove_necessary_condition_repetition',
    'are impossible.  The table gives necessary conditions only.',
    'are impossible.')
add('p071_remove_local_complex_scope_disclaimer',
    'with real complex structures.  This assertion concerns the\nindividual finite actions and does not produce simultaneous\nglobal periods.',
    'with real complex structures.')
add('p071_remove_unused_three_point_recap',
    r'''hypothesis used in the subsequent reductions.  For three genuine
finite fillings \ref{maps:src:F.2.7} has already excluded simple
connectivity without this argument.''',
    'hypothesis used in the subsequent reductions.')
add('p075_state_fixed_marking_equality_positively',
    'both the matrices and the affine numerators without a further\nchange of basis.',
    'both the matrices and the affine numerators in the fixed marking.')
add('p076_translate_boolean_flags_into_restriction_maps',
    r'''nonzero factors one.  Its torsion class has peripheral
triviality flags $(\mathrm{true},\mathrm{false},\mathrm{true})$,
so the parabolic groups are torsion free, of ranks $0,3,0$.''',
    r'''nonzero factors one. Its torsion class restricts to zero at the
order-five boundary and at the cusp, and to a nonzero class at
the order-four boundary. Thus the parabolic groups are torsion
free, of ranks $0,3,0$.''')
add('p077_remove_integrability_scope_repetition',
    'oriented diffeomorphism type.  No integrability at the finite\npunctures is used for this smooth classification.',
    'oriented diffeomorphism type.')
add('p080_name_the_eight_linear_equations',
    r'The first eight are \eqref{maps:eq:F.R4}.  The last two are exactly',
    r'The first eight are $YX=0$ and $YRX=I_2$. The last two are exactly')
add('p080_define_the_exact_solution_coordinates',
    r'''For $D\ne0$ this proves uniqueness and gives the explicit
formula $Y=\operatorname{reshape}(E^{-1}b)$, where $E$ is
the coefficient matrix of the displayed linear equations
and $b$ their displayed right side.''',
    r'''For $D\ne0$, the column of the ten row-ordered entries of $Y$
is $E^{-1}b$, where $E$ is the coefficient matrix of the
displayed linear equations and $b$ is their right-hand side.
This gives the unique solution.''')
add('p082_remove_negative_completeness_phrase',
    'The bounds below depend on the input rational pair and lose no lattice.',
    'The bounds below depend on the input rational pair.')
add('p085_keep_positive_wang_generation',
    'primitive suspension generate the free second homology;\nthere is no omitted period condition.',
    'primitive suspension generate the free second homology.')
add('p087_remove_multiplicity_search_disclaimer',
    'There is no multiplicity search bound in this statement:\nthe only possible affine multiplicities are the\ntwo displayed pairs.\n','')
add('p088_remove_localization_method_contrast',
    'No lattice splitting over a localization\nor semisimplification modulo a prime is used here.','')
add('p088_keep_positive_specialization_kernel_statement',
    'kernel, not an additional restriction on these free periods.',
    'kernel.')
add('p090_keep_the_resulting_finite_representation',
    'We have proved, without a global lattice classification,\nthat the full finite representation over $R$ is',
    'Thus the full finite representation over $R$ is')
add('p091_remove_extension_issue_preface',
    r'''\item There is one extension issue, and it cannot remove
this torsion.  The second vanishing in \eqref{maps:eq:F.X5} says''',
    r'''\item The second vanishing in \eqref{maps:eq:F.X5} says''')
add('p091_replace_moved_forward_dependency_by_exact_sheaf_maps',
    r'''Point-supported changes do not alter this degree-two
base cohomology; it is the coinvariant module, as
in \eqref{maps:eq:E.9}.  It is a finitely generated torsion $R$-module
and hence a finite group.''',
    r'''Point-supported changes leave degree-two base cohomology
unchanged. Put $\mathcal L=\bigwedge^2\mathcal V_R$ on the
punctured base $B^\circ$. The quotient $j_*\mathcal L/j_!\mathcal L$
is supported at the punctures, so its exact sequence and integral
Poincar\'e duality give
\[
 H^2(B,j_*\mathcal L)=H_c^2(B^\circ,\mathcal L)
 =H_0(B^\circ,\mathcal L)=(\mathcal L_b)_\Gamma,
 \qquad b\in B^\circ.
\]
Thus the group is a finitely generated torsion $R$-module and
hence a finite group.''')
add('p091_keep_positive_finite_extension_argument',
    'of $H^4(M;R)$; in particular it cannot be absorbed\nas a finite quotient of a free filtration kernel.',
    'of $H^4(M;R)$.')
add('p092_keep_unique_normalized_filling_conclusion',
    'homology conditions; no affine-twist enumeration remains.',
    'homology conditions.')
add('p095_remove_black_box_preface',
    r'''\item For reproducibility, no sheaf calculation is left
as a black box in the integer test.
Given $A=\bigwedge^qT_1$, $B=\bigwedge^qT_2$ on a''',
    r'''\item Given $A=\bigwedge^qT_1$, $B=\bigwedge^qT_2$ on a''')
add('p095_keep_exact_integral_image_instruction',
    'This uses the integral images of peripheral\ndifferences, not their saturations.',
    'Use the integral images of the peripheral differences.')

# Update only the metadata whose moved forward input has just been removed.
m=re.search(r'\\StatementRecord\{maps:src:F\.2\.27\}[^\n]*',text)
if m and r'\eqref{maps:eq:E.9}' in m.group():
    old=m.group()
    new=old.replace(r', \eqref{maps:eq:E.9}','').replace(r'\eqref{maps:eq:E.9}, ','')
    assert new!=old
    add('p091_remove_resolved_formula_dependency_metadata',old,new)

# Move unchanged complete proof blocks into their actual dependency order.
# The prior textual guards have already been applied to this in-memory text.
def proof_block(label):
    marker=r'\label{'+label+'}'
    pos=text.index(marker)
    start=text.rfind(r'\begin{proposition}',0,pos)
    assert start>=0
    end=text.index(r'\end{proof}',pos)+len(r'\end{proof}')
    return text[start:end]

local=proof_block('maps:src:F.2.15')
rank=proof_block('maps:src:F.2.9')
add('dependency_order_remove_later_local_complex_block',local,'')
add('dependency_order_remove_later_fixed_rank_block',rank,'')
marker=r'\label{maps:src:F.2.8}'
pos=text.index(marker)
start=text.rfind(r'\begin{proposition}',0,pos)
end=text.index('\n',pos)
anchor=text[start:end]
add('dependency_order_insert_local_then_rank_before_involution',anchor,
    local+'\n\n'+rank+'\n\n'+anchor)

for pattern in [r'\\label\{([^}]+)\}',r'\\hypertarget\{(tag-[^}]+)\}']:
    assert sorted(re.findall(pattern,text))==sorted(re.findall(pattern,original)),pattern
payload=dict(
    source=str(source),source_sha256=hashlib.sha256(original.encode()).hexdigest(),
    candidate_pdf_sha256='8b2d18bb43fedda842510e01967074589e0439c491fa3bb53928ab1d7eeedc2d',
    instruction='Apply sequentially only if each old string occurs exactly once. These guards follow actual visual reading of every candidate01 page55–96. All old labels/tags are preserved. No main-source edit was made. The page78 article and page94 cokernel concerns were cleared by zoom/source confirmation and have no guards.',
    patches=patches)
out=folder/'S6_SERIES_PUBLISH_V_final_reading_guarded_patch.json'
out.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
print('Wrote',len(patches),'guards to',out)
print('All old guards unique; all label/tag multiplicities preserved; main source unchanged.')
