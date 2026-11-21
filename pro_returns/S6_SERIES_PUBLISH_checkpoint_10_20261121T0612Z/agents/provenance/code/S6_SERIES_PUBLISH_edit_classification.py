#!/usr/bin/env python3
"""Guarded editorial proposals for V classification and period sections.

This script writes only agent-owned proposals and records. Its exact snippets
can be applied independently, preserving the parent's new section divisions.
It does not claim a new mathematical check or rewrite the Sp4 textbook passage.
"""
import csv
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / 'S6_SERIES_PUBLISH_V_classification_original.tex'
original = SOURCE.read_text()
text = original
paragraphs = re.split(r'\n\s*\n', original)
changes = []

def location(s, at):
    opening = re.match(r'\\begin\{(?:theorem|proposition|corollary|lemma)\}(?:\[[^\]]*\])?[^\n]*\\label\{(maps:src:[^}]+)\}', s[at:])
    if opening:
        return opening.group(1)
    matches = list(re.finditer(r'\\label\{(maps:src:[^}]+)\}', s[:at]))
    return matches[-1].group(1) if matches else 'sec:classification'

def change(old, new, kind, reason):
    global text
    if text.count(old) != 1:
        raise ValueError(f'Expected one match, found {text.count(old)}: {old[:150]}')
    at = text.index(old)
    changes.append(dict(type=kind, location=location(text, at),
        old_pdf_page='root to fill from corrected baseline',
        new_pdf_page='root to fill after final pagination',
        old_text=old, new_text=new, reason=reason))
    text = text.replace(old, new, 1)

def para(i, new, kind, reason):
    change(paragraphs[i], new, kind, reason)

programs = []
for m in re.finditer(r'\\texttt\{([^}]*\.py)\}', original):
    name = m.group(1).replace(r'\_', '_')
    before = original[max(0, m.start()-850):m.start()]
    url = re.search(r'\\href\{([^}]+)\}\{$', before)
    programs.append(dict(filename=name, location=location(original,m.start()),
        retained_url=url.group(1) if url else '',
        disposition='program table/check record; proof retains mathematical inputs, operations and conclusions'))

# Exact computations remain in the proof; file and replay narration moves out.
edits = [
('All arithmetic in this item is reproduced by a separate program (\\S1.5).\nThe argument from that determinant treats all lattices, without a\nbound on their indices.',
 'The determinant argument applies to every stable lattice.', 'D09',
 'Move verification narration; retain the all-lattice scope proved by the determinant.'),
('kernel basis of $\\Delta_q$ give the following certificates:',
 'kernel basis of $\\Delta_q$ give the following Smith forms:', 'D08',
 'Name the mathematical output of the displayed integer calculation.'),
('All displayed groups are therefore free over $R$.  These computations are done by three separate programs (\\S1.5).  Their computations use the printed models.',
 'All displayed groups are therefore free over $R$.', 'D09',
 'The preceding HNF and Smith calculation remains; move the replay count to records.'),
('cokernel of the collapse and must be retained.',
 'cokernel of the collapse.', 'D08', 'State the identified kernel without editorial instructions.'),
('The independent exact calculation gives $A^5=B^6=I$, exact orders five',
 'Direct multiplication gives $A^5=B^6=I$, exact orders five', 'D09',
 'Name the operation proving the matrix identities.'),
('Finally use the checked rational invariant-extension table for these\nexact models.',
 'Use the rational invariant-extension table above for these models.', 'D08',
 'Refer to the mathematical table without check-status narration.'),
('The identity $C^4=I$ is checked separately; it is not inferred\nfrom the repeated factor $x+1$ of the characteristic polynomial.',
 'Direct multiplication gives $C^4=I$.', 'D02',
 'Retain the independent finite-order calculation in positive mathematical form.'),
('Here $\\det L=-1/4$. Expanding these products gives entries in\n$\\mathbb Z[v]$ for both matrices. The complete expanded entries\nand the exact identities\n$LA_v=\\widehat A L$, $LB_v=\\widehat B L$ are given by the\npolynomial certificate described in the last item. Thus the',
 'Here $\\det L=-1/4$. Expanding these products gives entries in\n$\\mathbb Z[v]$ for both matrices, with\n$LA_v=\\widehat A L$ and $LB_v=\\widehat B L$. Thus the', 'D09',
 'Keep the exact conjugation formula and polynomial integrality; move the program certificate to records.'),
('For completeness, at $v=0$ the symmetric matrix',
 'At $v=0$ the symmetric matrix', 'D08', 'Begin directly with the explicit equivariant form.'),
('By \\cref{maps:src:F.3.11} it has holomorphic periods with bounded cusp correction on the punctured base; a compact complex structure on it is not constructed here.',
 'By \\cref{maps:src:F.3.11} it has holomorphic periods with bounded cusp correction on the punctured base.', 'D02',
 'Keep precisely the proved punctured-base period assertion.'),
('The exact program\n\\texttt{fourfolds\\_v1\\_homology.py} runs every matrix,\nSmith, Hermite, suspension-period, pairing and differential\ncertificate just displayed.  The proof uses the explicit monomial marking displayed above.',
 'These calculations use the explicit monomial marking displayed above.', 'D09',
 'Keep the marking on which the calculation depends; move the replay list to records.'),
('holds for \\emph{all} stable lattices and all twists, not just\nthe lattice in \\eqref{maps:eq:F.U6}.',
 'holds for every stable lattice and every twist.', 'D02',
 'State the established universal scope directly.'),
('The exact expanded matrix and all ten rational functions\nare printed by \\texttt{fourfolds\\_relative\\_normalform.py}.\nThere is no search or degree cutoff in this calculation.\n',
 '', 'D09', 'The preceding inverse-matrix formula reconstructs all ten rational functions.'),
('The program prints the corresponding two polynomial rows\nand verifies those identities, so they remain necessary\nalso when $D=0$.',
 'These polynomial identities remain necessary when $D=0$.', 'D09',
 'The preceding adjugate identity supplies the exact mathematical reason.'),
('The saved program checks all determinant, adjugate,\ncharacteristic-polynomial and finite-order identities over\nthe rational function field, and checks the exceptional\nline symbolically for every $z$.\n',
 '', 'D09', 'Move the verification list; all symbolic formulas and the bijection proof remain.'),
('$A,C$ is retained by the algorithm.',
 '$A,C$ is included by the algorithm.', 'D08', 'Describe the exhaustive lattice algorithm directly.'),
('\\item Here is a finite enumeration bound which is also implemented.',
 '\\item The enumeration has the following finite bound.', 'D08',
 'Keep the mathematical bound without implementation narration.'),
('All 374 subspaces of $\\mathbb F_2^5$, including zero and\nthe whole space, are enumerated, with no height restriction\nor neighbor-depth assumption.',
 'Enumerate all $374$ subspaces of $\\mathbb F_2^5$, including zero\nand the whole space.', 'D02', 'The explicit complete finite domain supplies the exhaustive scope.'),
('The generic prime-by-prime implementation of \\eqref{maps:eq:F.L5} and\nan independent bit-vector enumeration give exactly the\nsame two Hermite forms.\n',
 '', 'D09', 'Move the independent replay description; the complete enumeration and its two outputs remain.'),
('For each extension the program computes the image of the\nprimitive global invariant homology covector $\\ell$ on\nthe two finite fixed lattices.  The resulting positive\ndivisibilities are',
 'For each extension, restrict the primitive global invariant homology\ncovector $\\ell$ to the two finite fixed lattices. The resulting\npositive divisibilities are', 'D09', 'State the exact restriction operation underlying the table.'),
('All six full matrices, the integral kernel bases, the\nSmith factors and the finite divisibilities are computed\nexactly by \\texttt{fourfolds\\_two\\_classes\\_lattices.py}\n.\n',
 '', 'D09', 'Move the implementation reference; the extension algorithm, bases and divisibility table remain.'),
('The sole remaining class has an explicit integral\nintertwiner of determinant $\\pm1$ with the corresponding\npair in \\eqref{maps:eq:F.U6}, as printed and checked by the program.\nThose pairs already have the verified simply connected,\nthree-connected fillings.',
 'For the sole remaining class, solve the integral intertwiner\nequations with the corresponding pair in \\eqref{maps:eq:F.U6}.\nThey have a solution of determinant $\\pm1$. The fillings of\n\\cref{maps:src:F.2.6,maps:src:F.2.18} for those pairs are three-connected.',
 'D09', 'Keep the exact intertwiner calculation and cite the proved fillings; move replay narration.'),
('This completes the classification for this rational family.\n',
 '', 'D08', 'Remove a closing recapitulation already contained in the theorem statement.'),
('They are also independently printed for both pairs by\n\\texttt{fourfolds\\_family\\_twists.py}.\n',
 '', 'D09', 'Move replay narration; the cited invariant two-form computation stays.'),
('This proves surjectivity.  The saved program additionally\ngives integral preimages $q_i\\in\\ker\\ell$ with\n$\\operatorname{Norm}_{n_i}q_i=\\lambda_i$.',
 'This proves surjectivity. Choose integral preimages\n$q_i\\in\\ker\\ell$ with\n$\\operatorname{Norm}_{n_i}q_i=\\lambda_i$.', 'D09',
 'Use the established surjectivity to choose exactly the preimages used next.'),
('This is independently checked in the saved program.\n',
 '', 'D09', 'The preceding five unit Smith factors already establish the coinvariant group.'),
('\\item For completeness, apply \\eqref{maps:eq:F.S8} to the entire eight-case',
 '\\item Apply \\eqref{maps:eq:F.S8} to the eight-case', 'D08',
 'Introduce the finite spectrum calculation directly.'),
('The complete table is checked by\n\\texttt{fourfolds\\_suspension\\_filter.py}; its input is\nexactly these eight spectra, with no matrix-entry or\nrelative-position cutoff.  This proves \\eqref{maps:eq:F.S1} and all\nclaimed universal exclusions.',
 'This proves \\eqref{maps:eq:F.S1} and the stated universal exclusions.', 'D09',
 'Retain the exact table and its conclusion; move the implementation and replay scope.'),
('has three-adic valuation two.  The program \\texttt{fourfolds\\_universal\\_56\\_obstruction.py} checks\nthe full invariant kernel, its primitivity, and the\npairing independently by exterior multiplication and\nsix-column determinants; its Smith factors are\n$(1,1,3,3)$.',
 'has three-adic valuation two. Exterior multiplication in the displayed\nintegral basis gives Smith factors $(1,1,3,3)$.', 'D09',
 'Keep the exact basis, pairing, determinant valuation and Smith output.'),
('This argument does not assume that the normal closure of\ncusp vanishing cycles already exhausts $\\ker\\ell$.\n',
 '', 'D02', 'The argument has proved abelianness directly from the two coprime meridian relations.'),
('Now $T=0$, so it is exactly $\\mathbb Z$ detected by\n$\\ell$, not just a rational or free quotient.',
 'Since $T=0$, this group is $\\mathbb Z$, detected by $\\ell$.', 'D02',
 'State the integral obstruction group and detecting homomorphism positively.'),
('the prescribed cusp is retained throughout.',
 'each comparison respects the prescribed cusp marking.', 'D08',
 'Name the marked compatibility already proved for these maps.'),
('\\item We first establish the uniform local calculations needed\nfor the criterion, so the test does not assume that a\ngeneral finite matrix is globally conjugate to the example\nin \\ref{maps:src:F.2.6}.',
 '\\item We establish the uniform local calculations for the criterion.', 'D02',
 'Introduce the exact local argument without an unneeded contrasting assumption.'),
('These local comparisons apply to cap cohomology, not just\nto abstract representation lattices.',
 'These local comparisons induce isomorphisms on cap cohomology, as follows.', 'D02',
 'State the precise induced morphism that the following isogeny argument proves.'),
('For completeness, the determinants of the pairings between',
 'The determinants of the pairings between', 'D08', 'Introduce the complementary-degree pairing calculation directly.'),
('These determinant identities and all the Wang Smith\nforms are verified by the fixed, exhaustive computation\nin \\texttt{fourfolds\\_local\\_caps.py}, for both orders and\nall exterior degrees zero through six.\nThus no unexamined finite matrix is being inferred from\nan example.',
 'For both local normal forms, exterior multiplication gives these\npairing determinants, and integer row and column operations give the\nWang Smith forms in exterior degrees zero through six.', 'D09',
 'Retain the specified local inputs, exterior degrees and exact reduction method.'),
('The exact matrices and a torsion representative are\nsaved by \\texttt{fourfolds\\_cusp\\_boundary.py}.\n',
 '', 'D09', 'The cusp matrix and its exterior differences already specify the Smith problem.'),
('Consequently the cusp contribution to $d_2$ is\nexactly $c_4$ as defined above.  In particular this\ncolumn must not be discarded merely because it\nvanishes in the first examples.',
 'Consequently the cusp contribution to $d_2$ is exactly $c_4$\nas defined above.', 'D02', 'Retain the proved boundary map without instructions about earlier examples.'),
('\\item The program \\texttt{fourfolds\\_survivor\\_test.py}\nimplements exactly these operations.\nIts executed test set is precisely $v=0,1,2$ from\n\\ref{maps:src:F.2.16}.  For $v=0,1$ all six tests pass;',
 '\\item For the parameters $v=0,1$ of \\ref{maps:src:F.2.16}, all six\nconditions hold;', 'D09', 'Retain the three exact parameter calculations as examples of the criterion.'),
('fourth and fifth tests fail.  The computation thus\nchecks both accepted and rejected data.',
 'fourth and fifth conditions fail.', 'D09', 'Keep the exact failed conditions and remove test-suite narration.'),
('\\item We finish by making the convention dictionary explicit.\nThe imported family matrices called $A,B$ in that\nprogram are geometric cohomology pullbacks, so the\ngeometric homology inputs are $(A^t,B^t)$.\nTheir genuine left cohomology transport in \\eqref{maps:eq:F.HC2}\nis $(A^{-1},B^{-1})$, which is what the code uses.',
 '\\item For the family matrices $A,B$ in \\eqref{maps:eq:F.U6}, which\nare geometric cohomology pullbacks, the geometric homology inputs\nare $(A^t,B^t)$. Their left cohomology transport in\n\\eqref{maps:eq:F.HC2} is $(A^{-1},B^{-1})$.', 'D09',
 'Keep the exact transpose/inverse dictionary independently of a program.'),
('Thus the new cusp is conjugate to the inverse old\ncusp, not an independently chosen third matrix.',
 'The image of the cusp generator is $g_1^{-1}g_0^{-1}g_1$.', 'D02',
 'State the exact conjugacy displayed in the preceding formula.'),
('The implementation uses \\eqref{maps:eq:F.HC2} directly and hence\ndoes not depend on this comparison for its validity.\n',
 '', 'D09', 'Move implementation convention narration; the full convention morphism remains.'),
('presentation.  The program below also determines exactly which\nquotient of the apparent fibre subgroup injects.',
 'presentation. The formulas below determine the injected quotient\nof the fibre subgroup.', 'D09', 'State the group-theoretic output of the following exact sequence formulas.'),
('injected abelian kernel and all extension data.  These statements\ndo not claim a conjugacy classification of the original tuples.',
 'injected abelian kernel and all extension data.', 'D02',
 'Keep the theorem\'s group and extension scope; the separate conjugacy theorem is unchanged.'),
('Here the bottom left zero block has $k$ rows.  The code records\nthe full matrix, not only its invariant factors.',
 'Here the bottom left zero block has $k$ rows.', 'D09',
 'The full matrix is already printed in the statement.'),
('\\item \\emph{Actual finite and cusp caps.}',
 '\\item \\emph{Finite and cusp caps.}', 'D08', 'Use a mathematical proof-step title.'),
('termination and gives the computable bound used by the code;\nit never replaces a finite-index lattice by its saturation.',
 'termination with a computable bound. At every step the Hermite\nbasis represents the integer sum of the generated columns.', 'D02',
 'Specify the exact lattice operation that preserves finite indices.'),
('For completeness this step computes the fibre injection; it\ndoes not infer it from the appearance of a normal subgroup in\na presentation.',
 'We compute the fibre injection by the homotopy sequence of a\nfibration over the orbifold classifying space.', 'D02',
 'Name the exact morphism used in the subsequent proof.'),
('$\\Gamma$ invariant, as also checked by the code.  The long',
 '$\\Gamma$ invariant. The long', 'D09', 'The coset sum proves invariance; move its replay status.'),
('\\item There is no implicit infinite search for a spherical group.\nAfter sorting its orders the possibilities are',
 '\\item After sorting its orders, the spherical possibilities are', 'D02',
 'State the complete finite family used by the group construction.'),
('The code constructs the dihedral, tetrahedral, octahedral,\nor icosahedral permutation group and finds the marked\nperipheral generators in that finite group.  Breadth-first\nwords supply their actions on $A$; every generator edge is\nchecked modulo the lattice $L$.  It then computes\nthe two finite sums in \\eqref{maps:eq:F.G9} and their integer Smith form.',
 'Construct the dihedral, tetrahedral, octahedral, or icosahedral\npermutation group and find the marked peripheral generators in that\nfinite group. Breadth-first words supply their actions on $A$;\nthe generator-edge equalities are evaluated modulo the lattice $L$.\nCompute the two finite sums in \\eqref{maps:eq:F.G9} and their integer Smith form.',
 'D09', 'Keep each finite algorithmic operation without naming an implementation.'),
('primitive covectors.  The code computes the powers in the\nrational affine matrix group and performs these finite tests.',
 'primitive covectors. Compute the powers in the rational affine\nmatrix group and apply these finite tests.', 'D09',
 'Keep the exact affine-power and fixed-covector criterion.'),
('The sheaf comparison, which does not assert a map\nbetween the total manifolds, is therefore',
 'The covering pullback at the new point gives the sheaf comparison', 'D02',
 'Specify the actual morphism of sheaves; the next sentence gives its stalk maps.'),
('Thus no torsion extension has been inferred from\nrational ranks.\n',
 '', 'D02', 'The displayed exact sequence and free-quotient splitting give the full integral extension.'),
('For an integral check of this degree-one row, its\nfinite sheaf cokernel is',
 'The finite sheaf cokernel in this degree-one row is', 'D08',
 'Present the exact integral cokernel as mathematics.'),
('\\item For completeness, the second contraction used in the algorithm\nis also explicit.',
 '\\item The second contraction used in the algorithm is as follows.', 'D08',
 'Introduce the full contracting homotopy directly.'),
('can be checked without an unspecified comparison theorem.',
 'are given by the following formulas.', 'D02',
 'State the explicit projection formulas rather than contrast with an unnamed theorem.'),
('The program enumerates every object, every translated\nincidence and every flag, verifies composition, checks\n$d^2=0$ on every generator, and checks the collapse-chain\nidentity on every generator.',
 'Enumerate the objects, translated incidences and flags. Composition\nand the alternating boundary formulas give $d^2=0$ and the\ncollapse-chain identity on their generators.', 'D09',
 'Keep the finite chain construction and its generator-level identities.'),
('Smith reduction gives \\eqref{maps:eq:F.CK1}.  All matrices\nand the remaining differentials are saved by\n\\texttt{fourfolds\\_kuhn\\_cap\\_chains.py}; the reduced cap and\nrelative differentials vanish, and the boundary has one',
 'Smith reduction gives \\eqref{maps:eq:F.CK1}. The reduced cap and\nrelative differentials vanish, and the boundary has one', 'D09',
 'Keep all cancellation counts and reduced differentials; move the file reference.'),
('This independently checks the affine power relation and\nthe degree-one prism sign, including negative numerators.',
 'This establishes the affine power relation and the degree-one\nprism sign for every integer numerator.', 'D08',
 'Present the exact group identity as the reason for the sign.'),
('\\item For clarity the exact finite size bound can be read off\nbefore running any matrix calculation.',
 '\\item The chain ranks give an explicit finite size bound.', 'D08',
 'Introduce the reconstructible bound by its mathematical input.'),
('Thus Hermite or Smith\nreduction computes full bases, rather than sublattices of finite index.',
 'Thus Hermite or Smith reduction computes bases of these saturated\ninteger kernels.', 'D02', 'State the exact integral lattices computed.'),
('\\item For clarity this decomposition is effective without a split-algebra\noracle.',
 '\\item The decomposition can be computed as follows.', 'D02',
 'Introduce the explicit algebra decomposition rather than an unneeded oracle contrast.'),
('The program verifies multiplication on every pair of basis elements.',
 'The multiplication table verifies the algebra homomorphism on every\npair of basis elements.', 'D09',
 'Keep the concrete verification of the exact algebra isomorphism.'),
('In the recorded implementation the class and unit groups of every\nnumber-field component are certified with \\texttt{GRH=false} before\nthe principal-ideal decision is used. The negative decision thus\ndoes not presume the generalized Riemann hypothesis.',
 'Use unconditional class-group and unit-group computations for every\nnumber-field component before applying the principal-ideal decision.', 'D09',
 'Keep the unconditional mathematical algorithm requirement; move the software flag to records.'),
('normal form \\ref{maps:src:F.2.38}, and all of its $56$ classes have been\ncomputed.',
 'normal form \\ref{maps:src:F.2.38}, consisting of $56$ classes.', 'D08',
 'State the finite classification rather than its production history.'),
('separate retained gluing datum; the construction in item1 gives',
 'specified gluing datum; the construction in item~1 gives', 'D23',
 'Repair the item reference and state the datum directly.'),
('returns a canonical representative and a checked unimodular',
 'returns a canonical representative and an explicit unimodular', 'D08',
 'State the mathematical witness produced by the algorithm.'),
('No finite-index sublattice has been substituted for a norm\nimage; the displayed block calculations are surjective\ninteger formulas.',
 'The displayed block formulas are surjective over $\\mathbb Z$, so\nthey compute the full norm image.', 'D02',
 'State the integral surjectivity proved by the displayed formulas.'),
('\\item It remains a genuinely finite classification.',
 '\\item The remaining classification is over the finite field.', 'D08',
 'Name the parameter space for the finite similarity calculation.'),
('\\item This also gives an effective normalizer for an arbitrary\ninput, not merely a list of representatives.',
 '\\item The construction also gives an effective normalizer for every input.', 'D02',
 'State the additional algorithmic output directly.'),
('presentation are also returned.  Independently replacing\n$P\'$ by another Smith marking is not this comparison.',
 'presentation are also returned. The cusp marking in this\ncomparison is $P\'=RP$.', 'D02',
 'Keep the exact specified morphism of cusp markings.'),
('torsion factors.  Its independent\nabelianization check compares the resulting $H_1$ with the\nvan Kampen answer.',
 'torsion factors. Its degree-one homology agrees with the\nabelianization of the van Kampen presentation.', 'D09',
 'State the mathematical compatibility; move replay narration.'),
('type.  There is no residual untested rational-height bound\nin this parametrization.  The canonical-representative\nalgorithm can remove duplicates from it if desired, but\nno finite global enumeration is asserted or needed for\nthese complete per-input decisions.',
 'type. Applying the canonical-representative algorithm identifies\nprecisely the simultaneously integrally conjugate inputs in this\nparametrization.', 'D02',
 'State the exact equivalence relation decided by the proved canonical algorithm.'),
('No polarization on $T$ is assumed.',
 'Here polarization is used through the semisimplicity of the middle term $W$.',
 'D02', 'Name exactly where the source hypothesis enters the filtration argument.'),
('It does not exclude an arbitrary unpolarized torus period family.\n',
 '', 'D02', 'Keep the proved obstruction for the expressly stated semisimple-middle filtration.'),
('These assertions concern the unpolarized domain.\n',
 '', 'D11', 'The displayed definition and theorem title already specify the unpolarized domain.'),
('Thus it is a spanning\ntube in the precise sense of \\cite[Definition 2.1, p.~4]{IVVOkaOneV5},\nnot merely a neighborhood of one entire line.',
 'Thus it is a spanning tube in the sense of\n\\cite[Definition 2.1, p.~4]{IVVOkaOneV5}.', 'D02',
 'The displayed union of nine independent lines verifies the cited definition.'),
('gives Oka--1.  The exact program\n\\texttt{fourfolds\\_oka\\_tubes.py} checks all nine integer\nmatrices, their linear independence and the symbolic identity\n\\eqref{maps:eq:F.O3}.',
 'gives Oka--1.', 'D09',
 'The spanning basis and symbolic identity were proved in the preceding steps; move replay information.'),
('of its interior.  No fibre-bundle or Serre-fibration assertion\nis required at the points of $S$.',
 'of its interior.', 'D11',
 'Retain the exact stated open-Grassmannian and off-S bundle hypotheses.'),
('This is the critical case of Theorem 6.1 of\nthat paper, with no approximation performed at a singular\npoint of the projection: here the projection is a submersion\neverywhere, as $\\mathscr U$ is open in a Grassmannian bundle.',
 'This is the critical case of Theorem 6.1 of that paper. The\nprojection is a submersion everywhere because $\\mathscr U$ is\nopen in a Grassmannian bundle.', 'D02',
 'State the exact geometric reason the projection is a submersion.'),
('Consequently every admissible datum with three-connected gluing admits such a period family.  No good-reduction\ncondition at the other, still punctured, points is included\nin this assertion.',
 'Consequently every admissible datum with three-connected gluing\nadmits such a period family on $B^*$. The points\n$p_1,\\ldots,p_k$ remain punctures of its base.', 'D02',
 'Make the precise domain explicit without asserting any compactification.'),
('\\item Retain the cusp as a point of the \\emph{open} surface',
 '\\item Adjoin the cusp to obtain the open surface', 'D08',
 'Describe the base operation directly; the displayed open surface is unchanged.'),
('The projection is consequently a holomorphic submersion,\nalthough its fibre at $p_0$ is $\\mathbb C^9$ rather than $D_3$.',
 'The projection is consequently a holomorphic submersion. Its fibre\nat $p_0$ is the affine chart $\\mathbb C^9$ just described; over\n$B^*$ its fibre is $D_3$.', 'D02',
 'State both explicitly identified fibres of the proved open subset.'),
('The flat bundle is trivial over each\ncell.  This argument uses no fibration property at $p_0$.',
 'The flat bundle is trivial over each cell.', 'D11',
 'The proof already extends only across cells outside the cusp disc.'),
]
for args in edits:
    change(*args)

# Verification-only paragraphs have no role in the logical derivation. Their
# complete text remains in the edit record and program/check inventory.
para(108, '\\end{enumerate}\n\\end{proof}', 'D09',
     'Move polynomial/replay verification metadata; the universal identity equal to one remains in the proof.')
para(169, '', 'D09', 'Move the implementation-only proof item into the program index; retain the full lattice algorithm.')
para(208,
     '\\item The finite lattice and extension algorithm of \\ref{maps:src:F.2.22}\n'
     'enumerates the integral lattices and extensions over every point of\n'
     '\\eqref{maps:eq:F.R10}.', 'D09',
     'Move symbolic replay history; retain the algorithm\'s exact lattice-and-extension scope.')
para(276, 'The bounds in this construction depend on the input.', 'D09',
     'Move the finite test-suite narrative and its output examples to records; preserve the input-dependent bound.')
para(291, '', 'D09', 'Move the thirty-case replay list; all general sheaf and integral-extension derivations remain.')
para(304, '', 'D09', 'Move program hyperlinks and finite replay domains from the main text to the program/check index.')
para(332, '', 'D09', 'Move the three program names and methodology pointer to the program table.')
para(334, '', 'D09', 'Move all replay counts and execution-history claims to the records.')

# The source/chain comparison between these two proofs is a mathematical remark.
para(315, '\\begin{remark}[Cusp quotient and global chains]'
     '\\label{rem:V:cusp-input-and-global-chains}\n'
     'The finite-pair and cusp-pair chain models enter the global\n'
     'gluing cone of \\cref{maps:src:F.2.35}. Its maps to the common\n'
     'torus-bundle complement include the peripheral word and clutching\n'
     'translation.', 'D13',
     'Number the exact comparison between the local models and the global cone.')
para(316, paragraphs[316]+'\n\\end{remark}', 'D13',
     'Include the precise Yang credit and primitive-grid Euler specialization in the numbered remark.')

# This explicit output example was a result orphaned between proofs.
example = paragraphs[333]
example = example.replace('A third full integration uses',
    'Take the gluing with').replace('Its 7345 integral unit cancellations give free ranks',
    'Applying $7345$ integral unit cancellations to its gluing cone gives free ranks')
example = example.replace('The independent van Kampen $H_1$ agrees.',
    'Abelianizing its van Kampen presentation gives the same $H_1$.')
example = example.replace('have the required nonorientable form.  Thus this integration\nalso tests the orientation-reversing part of the stated scope.',
    'are those of a closed nonorientable eight-manifold.')
para(333, '\\begin{remark}[An orientation-reversing gluing]'
     '\\label{rem:V:orientation-reversing-gluing}\n'+example+'\n\\end{remark}',
     'D13', 'Number the explicit gluing example; preserve every input, homology group and exact count.')

# Titles only: preserve every old theorem/proposition/lemma label and tag.
for m in list(re.finditer(r'\\begin\{(theorem|proposition|corollary|lemma)\}\[([^\]]+)\]',text)):
    title = m.group(2)
    cap = title[0].upper()+title[1:]
    if cap != title:
        change(m.group(0),m.group(0).replace('['+title+']','['+cap+']'),
               'D16','Capitalize the mathematical title; preserve every label and permanent tag.')

# Exact structural invariants; these are editorial checks, not proof checks.
before_labels = re.findall(r'\\label\{([^}]+)\}',original)
after_labels = re.findall(r'\\label\{([^}]+)\}',text)
assert set(before_labels) <= set(after_labels)
assert all(after_labels.count(x)==before_labels.count(x) for x in before_labels)
assert re.findall(r'\\hypertarget\{tag-[^}]+\}\{\}',original)==re.findall(r'\\hypertarget\{tag-[^}]+\}\{\}',text)
assert re.findall(r'\\tag\{[^}]+\}',original)==re.findall(r'\\tag\{[^}]+\}',text)
assert paragraphs[21] in text and paragraphs[22] in text and paragraphs[23] in text
assert not re.search(r'\\texttt\{[^}]*\.py\}',text)

(ROOT/'S6_SERIES_PUBLISH_V_classification_revised.tex').write_text(text)
for name,rows in [('S6_SERIES_PUBLISH_V_classification_edits.tsv',changes),
                  ('S6_SERIES_PUBLISH_V_classification_programs.tsv',programs)]:
    with (ROOT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t')
        w.writeheader(); w.writerows(rows)
(ROOT/'S6_SERIES_PUBLISH_V_classification_replacements.json').write_text(
    json.dumps(changes,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(dict(input_bytes=len(original.encode()), output_bytes=len(text.encode()),
    edits=len(changes),program_mentions_moved=len(programs),
    original_labels_preserved=len(before_labels),
    new_numbered_labels=sorted(set(after_labels)-set(before_labels)),
    sha256=hashlib.sha256(text.encode()).hexdigest()),indent=2))
