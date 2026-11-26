"""Typed outline references and exact first-part explanations."""
from S6_SERIES_PUBLISH_c3_edit import *

apply_edit(
    'the central support and every nontrivial normalization-gluing line\n',
    'the other discriminant value is $-4/27$. The central support and every nontrivial normalization-gluing line\n',
    'DII-C3-FIRSTPART-NODAL-RADIUS', ['D22'], 'series:II:A', 'Theorem A nodal family',
    'The family singularity equations y=0 and x(3x+2)=0 in the complete nodal computation give t=0,-4/27. State this reason for the chosen disc bound at its first appearance.',
    'Root read the whole main-theorem unit and the nodal owner statement and exact singularity paragraph; final whole-unit receiving read follows this edit.')
apply_edit(
    'The sign and equality criterion in\n\\cref{cdp:st:C.2.G.1} extends the standard-family Euler value',
    'The sign and equality criterion in\n\\cref{cdp:st:C.2.G.1} extend the standard-family Euler value',
    'DII-C3-FIRSTPART-SIGN-GRAMMAR', ['D23'], 'series:II:C', 'Theorem C literature line',
    'Correct the verb for the coordinated subject without altering any literature claim.',
    'Whole original main-theorem unit read; final whole-unit receiving read follows this edit.')

text = SOURCE.read_text()
a = text.index(r'\subsection{The proofs in outline}')
b = text.index(r'\subsection{Known and new}', a)
old = text[a:b]
pattern = r'\\hyperref\[([^\]]+)\]\{\\ref\*\{\1\}\}'
new, count = re.subn(pattern, lambda m: r'\cref{' + m.group(1) + '}', old)
assert count > 40, count
for label in re.findall(r'\\cref\{([^}]+)\}', new):
    assert r'\label{' + label + '}' in text, label
apply_edit(old, new, 'DII-C3-FIRSTPART-TYPED-OUTLINE', ['D06', 'D23'],
    'series:II:outline', 'Complete proofs-in-outline subsection',
    f'All {count} unchanged internal targets now print their current statement kind and number through cref; every step, formula, target and scope is preserved.',
    'Root read the complete old outline and all seven main-theorem statements. Final complete receiving outline read follows this edit; no independent-check credit.')

first = '\\item \\cref{cdp:st:C.2.UN.70}\\quad Elliptic fibrations and vertical point blowups.\n'
second = '\\item \\cref{cdp:st:C.2.UN.83}\\quad The negative-coefficient interfaces have exact elliptic or one-section models.\n'
combined = '\\item \\cref{cdp:st:C.2.UN.83}\\quad Torsion-normal elliptic boundaries have explicit elliptic, nonlinear Hopf or one-section ruled models.\n'
apply_edit(first, combined, 'DII-C3-FURTHER-COMMON-MODELS', ['D12', 'D15'],
    'cdp:st:C.2.UN.70;cdp:st:C.2.UN.83', 'Further results',
    'The two complete model statements now have one proved owner, with UN70 its exact nonnegative-coefficient specialization. One navigation entry describes all three models.',
    'Root read both original list entries and the entire common receiving statement and proof. All body identifiers remain in place.')
apply_edit(second, '', 'DII-C3-FURTHER-COMMON-MODELS-DUPLICATE', ['D12', 'D15'],
    'cdp:st:C.2.UN.83', 'Further results',
    'Remove the second navigation entry for the same consolidated owner; the preceding revised entry gives its complete three-model scope.',
    'Root read both old entries and the entire common owner; no mathematical statement or label is removed.')
print('Outline references converted:', count)
