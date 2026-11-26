#!/usr/bin/env python3
"""Prepare the proved splitting inputs and final problem; no shared writes."""
from pathlib import Path
from collections import Counter
import csv
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation3_provenance/splitting'
old = (ROOT.parents[1] / 'tmp/c3_split_unit_old.tex').read_text()
main = (ROOT / 'S6_SERIES_PUBLISH_II.tex').read_text()
proved = (OUT / 'S6_SERIES_PUBLISH_splitting_proved.tex').read_text()
problem = (OUT / 'S6_SERIES_PUBLISH_splitting_problem.tex').read_text()
anchor = r'\begin{proposition}[Comb members with more than two vector fields]\hypertarget{tag-01SX}{}\label{inv:E2.4}'
assert main.count(anchor) == 1
assert main.count(old) == 1
for tag in ['P320', 'P321']:
    assert '{tag-' + tag + '}' not in main


def cut(text, start, stop):
    a = text.index(start)
    b = text.index(stop, a)
    return text[a:b]


def statement(text):
    a = text.index(r'\begin{problem}')
    b = text.index(r'\end{problem}', a) + len(r'\end{problem}')
    return text[a:b]


p320 = cut(proved, r'\begin{proposition}[Degree', r'\begin{proposition}[Tangent')
p321 = cut(proved, r'\begin{proposition}[Tangent', r'\subsection{Vector fields')
step1 = cut(p320, r'\item Write', r'\item Put')
step2 = cut(p320, r'\item Put', r'\item The nonzero')
step3 = cut(p320, r'\item The nonzero', r'\end{enumerate}')
rows = []


def defect(kinds, where, before, after, why, owner='prop:II:comb-kernel-bounds'):
    assert before in old or before in main, (where, before[:80])
    rows.append(dict(change_id=f'II-C3-SPLIT-{len(rows)+1:03d}', type=kinds,
        statement_id=owner, old_location='Final splitting section: ' + where,
        old_page='original source; final concordance pending',
        new_location=('Earlier comb section: ' + owner if owner != 'inv:E2.3'
                      else 'Final splitting problem, existing tag01SW'),
        new_page='integrated build pending', old_text=before, new_text=after,
        reason=why, review_status='Draft; full receiving comparison pending'))


defect('D08;D11;D12;D14', 'complete problem statement', statement(old), statement(problem),
    'Preserve every general-tooth-count and special-member question, the same nonempty open twelve-tooth family, and the complete E15 tangent/Kuranishi scope. Remove repeated status narration. The two new proved owners supply the existing numerical and duality inputs earlier in the comb section.', 'inv:E2.3')
defect('D13;D14', 'proved facts presented as the proof of an open problem',
    cut(old, r'\begin{proof}[The remaining finite data', r'\paragraph{Bounds'),
    p320 + p321,
    'Extract the proved degree, bounds, explicit pencils and cup duality into two numbered owners after their complete E15/P278/E2.2 premises. The final open problem has no proof environment. This is an identity-of-data transfer, with all old mathematical pieces assigned individually below.')
defect('D13;D19;D20;D22', 'rank, degree, target and cokernel calculation',
    cut(old, r'\item If $e_m$', r'Although \eqref{invII:eq:E.4a}'), step1,
    'Use identical E_m,G_m,rho,kappa_1,K_m,e_m. The exact coarse matrix [[a,tb],[c,d]] has equivariant inverse lift [[a,w^(r-k)b],[w^kc,d]], with (r,k)=(3,2),(4,1). This proves the two elementary conditions and degree minus2. Weighted coordinate y gives the exact coarse target frame. The kernel degree and tag01TW/labelE.7 are unchanged.')
defect('D11;D12;D20', 'tangent dimensions and obstruction status',
    cut(old, r'Although \eqref{invII:eq:E.4a}', r'\item We evaluated'),
    cut(p321, r'By \eqref{invII:eq:E.4a}', r'\end{proof}') +
    cut(problem, r'For all these combs', r'\end{problem}'),
    'R1 tangent remains rho_*N and Q_m remains the exterior-cup cokernel of that same period tensor, so its support and elementary divisors retain their exact map. E15, whose complete proof was read, is the single full tangent/Kuranishi owner. Its local-family tangent isomorphism and inverse-function argument remain untouched.', 'prop:II:comb-cup-duality;cdp:st:E15')
defect('D01;D08;D09;D21', 'finite program evaluation narrative',
    cut(old, r'\item We evaluated', r'Proposition~\ref{inv:E2.5} now'),
    cut(step2, r'At $m=12$', '\n\n') if '\n\n' in step2[step2.index(r'At $m=12$'):] else step2[step2.index(r'At $m=12$'):],
    'Retain every displayed m12 value by substitution into the full formulas. The programs and their finite m12/13/20/100 scopes move to exact appendix addition159. Their full pinned sources were read and not executed. The analytic theorems are supplied by E15/E2.2 and the full local calculation, not by finite sample agreement.')
defect('D01;D02;D08;D11;D12', 'repeated twelve-tooth computation and closing scope',
    cut(old, r'Proposition~\ref{inv:E2.5} now', r'\end{enumerate}'),
    cut(problem, r'On that family', r'For all these combs'),
    'The complete E2.5 proof was read: root lift, relative kernel, mixed node condition, conic frame maps, two-jet dominance, balanced modifications and tooth collapse. The same data give (-8,-9,-9), zero cokernel and Hodge values49/48. Keep that single owner and state the exact remaining question once.', 'inv:E2.3;inv:E2.5')
defect('D13;D14;D20;D22', 'unnumbered uniform-bounds paragraph',
    cut(old, r'\paragraph{Bounds', r'\paragraph{Why'), step2,
    'Same two coarse bundles and nonnegative direct-sum splittings. Exchanging summands is the indicated permutation isomorphism. Keep all four Hom contributions, both displayed arithmetic cases, the upper bound2m+2, all middle Hodge bounds, and the m12 lower endpoint. The latter attainment stays at E2.5 and the final question. The upper-endpoint realization remains within the unchanged splitting question.')
defect('D13;D14;D20;D22', 'unnumbered pencil examples and their exact scope',
    cut(old, r'\paragraph{Why', 'There is an exact relation'),
    cut(p320, r'On $B=', r'\end{proposition}') + step3,
    'D_0 is precisely the old D=O^2+O(-1)^2, with identity on each summand. The same phi_A/phi_B maps are preserved. Give their global kernel injections and chartwise inverse divisions; the kernel isomorphisms and section counts are therefore proved by actual maps. Their domain is the displayed pair of bundle morphisms, with no new comb-occurrence assertion.')
defect('D13;D14;D20;D22', 'unnumbered tangent/cotangent relation',
    cut(old, 'There is an exact relation', 'The tangent calculation determines'), p321,
    'Same F=E_m^*,G,D=detG,L and unsaturated cokernelN. The same Cech convention gives -delta0^* after dualization. Preserve J, row(b,-a,d,-c) and K_m=rho_*(N^*D); add the explicit inverse I_F tensor J^{-1}. Exact finite averaging and vanishing of Hom(torsion,O) prove the stated scope without saturation.', 'prop:II:comb-cup-duality')
defect('D08;D11;D12;D14', 'closing computational task and recap',
    cut(old, 'The tangent calculation determines', r'\clearpage'),
    cut(problem, r'The degree formula', r'\end{problem}'),
    'Keep the exact remaining geometric splitting problem under its original final tag. The transition/cup data are the N and delta0 of P321; E15 retains the cohomology of rho_*N and its full Kuranishi conclusion. Remove repeated workflow directions and closing recap.', 'inv:E2.3')

# Record the individual vocabulary/file/heading instances as exact local rows.
instances = [
    ('D08', 'the actual splitting', 'the splitting', 'Remove workflow emphasis from the same kernel isomorphism.'),
    ('D08', 'the actual kernel', 'the kernel', 'Use the bundle name and precise open-family domain.'),
    ('D08', 'an actual admissible period section', 'the admissible period section', 'The root-period section and its tangent cup map specify the input.'),
    ('D08', 'cohomology dimensions themselves are fully determined', 'cohomology dimensions', 'Refer once to the complete E15 result.'),
    ('D01', 'first case already', 'At $m=12$', 'Give the numerical substitution directly.'),
    ('D01', r'Proposition~\ref{inv:E2.5} now computes', r'\cref{inv:E2.5}', 'Remove temporal narration and keep the exact owner.'),
    ('D01;D08', 'The already proved nonnegative splitting implies', 'The nonnegative splittings proved in\n\\cref{cdp:st:E15}', 'Use the exact earlier input without draft chronology.'),
    ('D08', 'Here is a complete derivation. Put', r'\item Put', 'Use a normal proof step under the new numbered owner.'),
    ('D09', r'\texttt{d\_exact.py}', r'\nolinkurl{pro_returns/S6_01_INVARIANTS/return/code/d_exact.py}', 'Move the sole path citation to the precise plain-path Programs row in addition159.'),
    ('D09', r'\texttt{d\_comb.py}', r'\nolinkurl{pro_returns/S6_01_INVARIANTS/return/code/d_comb.py}', 'Move the sole path citation to the precise plain-path Programs row in addition159.'),
    ('D02;D11', 'This proves the open-family case without\nassigning transition matrices to an unspecified individual member.',
     'On that family,\n$K_{12}\\simeq\\mathcal O_B(-8)\\oplus\\mathcal O_B(-9)^{\\oplus2}$\nand $h^0(K_{12})=0$', 'Keep the stated family and its exact splitting as the positive scope.'),
    ('D02;D11', 'We do not assert that either morphism is the cup map of an admissible\ncomb period section, or that different such geometric sections have\ndifferent Hodge numbers.',
     'On $B=\\mathbb P^1$ with homogeneous coordinates $[X:Y]$, put\n$D_0=\\mathcal O_B^{\\oplus2}\\oplus\\mathcal O_B(-1)^{\\oplus2}$.', 'State the two maps on their exact bundle domain; no geometric-occurrence conclusion is introduced.'),
    ('D02', 'so no saturation of\n$\\operatorname{im}\\delta_0$ is assumed.',
     'The identification therefore\nuses the stated cokernel $N$ itself.', 'The preceding Hom(torsion,O)=0 argument gives the complete unsaturated-cokernel scope positively.'),
    ('D13;D14', r'\paragraph{Bounds obtained from all possible coarse splittings.}',
     r'\begin{proposition}[Degree and section bounds for comb kernels]', 'Move this whole proved block to its numbered earlier owner.'),
    ('D13;D14', r'\paragraph{Why the numerical constraints do not determine the answer.}',
     r'\item The nonzero entries of each $\phi_A,\phi_B$', 'The explicit examples become a proved clause of P320 with actual inverse kernel maps.'),
]
for kind, before, after, why in instances:
    defect(kind, 'individual occurrence: ' + before[:65], before, after, why)
    if kind == 'D09':
        rows[-1]['new_location']='Programs table, exact addition159 row'

old_display = cut(old, '\\[\n \\deg K_m', '\\]\n') + '\\]'
new_display = cut(p320, r'\begin{equation}', r'\end{equation}') + r'\end{equation}'
defect('D19;D23', 'legacy manual equation tagE.7', old_display, new_display,
       'Use the section equation counter, retaining the exact displayed degree identity, labelinvII:eq:E.7 and permanent targettag01TW.')
defect('D23', 'duplicated final clearpages', old[old.index(r'\clearpage'):], '\\clearpage\n\n',
       'Keep one page break before the Programs appendix.', 'inv:E2.3')


def write(name, items):
    with (OUT / name).open('w', newline='') as f:
        w = csv.DictWriter(f, list(items[0]), delimiter='\t', lineterminator='\n')
        w.writeheader()
        w.writerows(items)


write('S6_SERIES_PUBLISH_splitting_guards.tsv', [
    dict(change_id='II-C3-SPLIT-PROVED-INSERTION', old_text=anchor, new_text=proved+anchor),
    dict(change_id='II-C3-SPLIT-FINAL-PROBLEM', old_text=old, new_text=problem),
])
write('S6_SERIES_PUBLISH_splitting_defects.tsv', rows)
oldlabels = Counter(re.findall(r'\\label\{([^}]+)\}', old))
newlabels = Counter(re.findall(r'\\label\{([^}]+)\}', proved+problem))
oldtags = Counter(re.findall(r'\\hypertarget\{([^}]+)\}', old))
newtags = Counter(re.findall(r'\\hypertarget\{([^}]+)\}', proved+problem))
assert not oldlabels-newlabels
assert not oldtags-newtags
assert newtags-oldtags == Counter({'tag-P320':1,'tag-P321':1})
for env in ['proposition','problem','proof','enumerate','equation']:
    assert (proved+problem).count('\\begin{'+env+'}') == (proved+problem).count('\\end{'+env+'}')
assert not re.search(r'\\tag\{|\\path\{|\\texttt\{|\bactual\b', proved+problem)
for m in re.finditer(r'\\begin\{equation\}([\s\S]*?)\\end\{equation\}', proved+problem):
    assert not re.search(r'\n\s*\n',m.group(1))
status = dict(old_lines=len(old.splitlines()), proved_lines=len(proved.splitlines()),
    problem_lines=len(problem.splitlines()), guards=2, defect_rows=len(rows),
    preserved_old_labels=sum(oldlabels.values()), preserved_old_targets=sum(oldtags.values()),
    new_statement_tags=['P320','P321'], shared_source_changed=False,
    complete_receiving_read='pending')
(OUT/'S6_SERIES_PUBLISH_splitting_status.json').write_text(json.dumps(status,indent=2)+'\n',newline='\n')
print(json.dumps(status,indent=2))
