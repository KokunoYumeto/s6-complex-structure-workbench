#!/usr/bin/env python3
"""Stage reversible source proposals for the complete 02S8 statement/proof."""
from pathlib import Path
import csv
import difflib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation9_findings'
source = (ROOT / 'S6_SERIES_PUBLISH_III.tex').read_text()
anchor = source.index(r'\hypertarget{tag-02S8}{}')
start = source.rfind(r'\begin{theorem}', 0, anchor)
proof = source.index(r'\begin{proof}', anchor)
end = source.index(r'\end{proof}', proof) + len(r'\end{proof}')
original = source[start:end]
proposed = original
operations = []


def replace_math(text, mapping):
    """Replace specified letter tokens only inside explicit TeX math spans.

    TeX commands and textual command arguments are retained.  The supplied
    regions are each manually read, so mathematical subscript roles are scoped
    by their actual definitions rather than inferred by a global search.
    """
    spans = re.compile(r'\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\]|(?<!\\)\$(?:\\.|[^$])*?\$')
    text_commands = {'begin', 'end', 'operatorname', 'text', 'hbox',
                     'textrm', 'mathrm', 'mathbf', 'mathsf', 'mathcal',
                     'mathfrak', 'label', 'hypertarget', 'ref'}
    def math_span(match):
        value = match.group()
        out = []
        i = 0
        while i < len(value):
            if value[i] == '\\':
                command = re.match(r'\\[A-Za-z]+|\\.', value[i:])
                if command:
                    token = command.group()
                    out.append(token)
                    i += len(token)
                    if token[1:] in text_commands and i < len(value) and value[i] == '{':
                        depth = 1
                        j = i + 1
                        while depth:
                            assert j < len(value), token
                            if value[j] == '{': depth += 1
                            elif value[j] == '}': depth -= 1
                            j += 1
                        argument = value[i:j]
                        out.append(argument)
                        i = j
                        if token == r'\begin' and argument in ['{array}', '{tabular}']:
                            assert value[i] == '{'
                            depth = 1
                            j = i + 1
                            while depth:
                                if value[j] == '{': depth += 1
                                elif value[j] == '}': depth -= 1
                                j += 1
                            out.append(value[i:j])
                            i = j
                    continue
            out.append(mapping.get(value[i], value[i]))
            i += 1
        return ''.join(out)
    return spans.sub(math_span, text)


def edit(first, last, transform, reason, markers):
    global proposed
    a = proposed.index(first)
    b = proposed.index(last, a) if last else len(proposed)
    before = proposed[a:b]
    after = transform(before)
    assert before != after, ('empty region', first)
    assert proposed.count(before) == 1
    proposed = proposed[:a] + after + proposed[b:]
    operations.append(dict(before=before, after=after, reason=reason, markers=markers))


def exact(before, after, reason, markers):
    global proposed
    assert proposed.count(before) == 1, ('exact guard', before)
    proposed = proposed.replace(before, after, 1)
    operations.append(dict(before=before, after=after, reason=reason, markers=markers))


unit_reason = ('Name the three initial nonzero holomorphic units a_un,b_un,c_un, '
               'preserving the later graph cochain a, characteristic class b and '
               'source log-norm c. These functions agree pointwise with the old '
               'units, including all products, powers, logarithms, node maps and '
               'reciprocal inverses; d_0 is retained unchanged.')
unit_mapping = dict(a=r'a_{\rm un}', b=r'b_{\rm un}', c=r'c_{\rm un}')
for first, last in [
    (r'On \(q=t^{-1}\) its periods and physical line are',
     r'\hypertarget{tag-034S}{}'),
    (r'The full \(g\)-maps into chart',
     'Thus the nonzero arrow on the even source component'),
    (r'The full period \(K=h^3g^2\) is', 'It covers'),
    (r'At the odd node the full \(H^{-1}\)-period gives',
     'The two nodes lie in the complementary free core arcs'),
    (r'Indeed, with \(L_q=\log|q|\)', 'Inverting this radial period matrix gives')]:
    edit(first, last, lambda text: replace_math(text, unit_mapping),
         unit_reason, list(unit_mapping.values()))
edit('Inverting this radial period matrix gives',
     r'For' + '\n' + r'\(G=\Im',
     lambda text: text.replace('q^2a', r'q^2a_{\rm un}'),
     unit_reason, [r'a_{\rm un}'])

edit(r'On a regular cut band write the arrow', 'At the finite end',
     lambda text: replace_math(text, {'L': r'L_{\rm line}'}),
     'Name the contracting line logarithm L_line, preserving L as the later based period matrix imported by 02S9. Its complex value is identical, so the real and imaginary parts, arrow multiplier, suspension maps, inverse height and reciprocal inverses are unchanged.',
     [r'L_{\rm line}'])
edit(r'Choose \(B(a+1)=B(a)+1\)', 'An increasing circle reparametrization',
     lambda text: replace_math(text, {'B': r'\vartheta_{\rm sus}'}),
     'Name the suspension cutoff lift vartheta_sus. It is exactly the same real function with the same endpoint-flat intervals and unit translation law. All Phi_a, their inverses and the source radial-shell restriction are pointwise unchanged.',
     [r'\vartheta_{\rm sus}'])
edit('An increasing circle reparametrization', 'At the finite end',
     lambda text: text.replace('B_t', r'\vartheta_{{\rm sh},t}'),
     'Name the shell circle-reparametrization lift vartheta_{sh,t}, preserving the distinct suspension cutoff. The same increasing lift, its inverse and periodic positive multiplier give the same radial-shell map.',
     [r'\vartheta_{{\rm sh},t}'])
edit('An increasing circle reparametrization', 'At the finite end',
     lambda text: text.replace('c(t)', r'c_{\rm sh}(t)'),
     'Name the positive shell multiplier c_sh(t), preserving the source log-norm c. This is the same positive function in the radial power and logarithmic inverse-height denominator, so the shell map and its inverse are identical.',
     [r'c_{\rm sh}'])
edit('One explicit choice is', 'The map to the compact-cover annulus is',
     lambda text: replace_math(text, {'c': r'c_{\rm sm}'}),
     'Name the positive smoothing coefficient c_sm, preserving the source log-norm c used later. Its displayed integral quotient and positive value are identical, so the smoothing function s(rho), derivative and inverse are unchanged.',
     [r'c_{\rm sm}'])

edit(r'The full period \(K=h^3g^2\) is',
     'The positive-fan fixed-edge charts are',
     lambda text: replace_math(text, {'A': r'A_{\rm un}', 'B': r'B_{\rm un}'}),
     'Name the two composite period units A_un and B_un, preserving A and B for the later raw monodromy matrices. Their definitions are the same products a_un^3 c_un^2 and b_un^3 d_0^2, and both height-straightening exponents and reciprocal inverse are unchanged.',
     [r'A_{\rm un}', r'B_{\rm un}'])
edit('Successive real-height charts have positive transition derivative:',
     'At the central overlap it is',
     lambda text: replace_math(text, {'R': r'R_{\rm ht}', 'X': r'X_{\rm ht}', 'Q': r'Q_{\rm ht}'}),
     'Name the three squared-modulus chart quantities R_ht,X_ht,Q_ht, preserving R as the later rim, X as the filled threefold and Q as the later intersection pairing. They are exactly |V|^2, |Z|^2, |q|^2, so both displayed height functions and their transition derivative retain the same values.',
     [r'R_{\rm ht}', r'X_{\rm ht}', r'Q_{\rm ht}'])
exact(r'At the central overlap it is \(\mu' + "'=-1/(X\\mu)\\), also increasing.",
      r'At the central overlap it is \(\mu' + "'=-1/(X_{\\rm ht}\\mu)\\), also increasing.",
      'Propagate the same positive squared-modulus quantity X_ht into the central real-height transition. The rational function and its derivative are unchanged.',
      [r'X_{\rm ht}'])

edit(r'There is one fixed-edge orbit \(F=S^2\);', 'Use the complete based period map',
     lambda text: replace_math(text, {'F': r'{\mathcal F}'}),
     'Name the fixed sphere mathcal F, preserving F as the elliptic fibre class in the compact-model and handle calculations. Identity on the same fixed-edge orbit identifies its complement, meridians, normal bundle and quotient maps.',
     [r'{\mathcal F}'])
exact(r'\(F-\bar E_\epsilon\)', r'\({\mathcal F}-\bar E_\epsilon\)',
      'Propagate mathcal F into the oriented compression boundary. The two boundary components, orientations, compression map and inverse are unchanged.',
      [r'{\mathcal F}'])
edit(r'The circle quotient \(B_0\)', 'Use the complete based period map',
     lambda text: text.replace('B_0', r'{\mathcal Q}_0'),
     'Name the free-circle orbit space mathcal Q_0, preserving B_0 for the already displayed chart coordinate. Identity on the same physical-circle orbits identifies the quotient, its Gysin sequence and the gluing to S^2 times D^3.',
     [r'{\mathcal Q}_0'])
exact(r'\left(\begin{smallmatrix}a&1\\1&0\end{smallmatrix}\right)',
      r'\left(\begin{smallmatrix}\alpha_{\rm bd}&1\\1&0\end{smallmatrix}\right)',
      'Name the unspecified boundary-map entry alpha_bd, preserving the graph cochain a. The same integer entry yields the same determinant -1 and the same integral Mayer--Vietoris map and inverse.',
      [r'\alpha_{\rm bd}'])

edit('The outer line is the physical dual through', 'In source log-norm',
     lambda text: replace_math(text, {'D': r'D_{\rm dual}'}),
     'Name the physical dual map D_dual. Its value on each nonzero line vector is the same evaluation-normalized dual vector; D_dual(v)(v)=1 and D_dual(av)=a^{-1}D_dual(v) retain the exact original linear-dual identification.',
     [r'D_{\rm dual}'])
edit(r'Indeed, with \(L_q=\log|q|\)', r'For' + '\n' + r'\(G=\Im',
     lambda text: replace_math(text, {'D': r'D_{\rm rad}'}),
     'Name the radial period determinant D_rad, preserving the physical dual map and the earlier local conifold coordinate. Its determinant expression, inverse-matrix denominator and asymptotic sign are identical.',
     [r'D_{\rm rad}'])
edit(r'\(G=\Im', r'Make \(V_m\cap W\) transverse',
     lambda text: replace_math(text, {'G': r'G_{\rm bind}'}),
     'Name the real binding function G_bind, preserving G as the elliptic section. The function, derivative on the source normal and dG_bind=1 normalization are identical, so the same positive binding normal and homotopy remain.',
     [r'G_{\rm bind}'])
edit(r'Make \(V_m\cap W\) transverse',
     r'\paragraph{The global graph class.}',
     lambda text: re.sub(r'\\sigma(?![A-Za-z_])',
                         lambda _: r'\varepsilon_{\rm node}', text),
     'Name the node orientation sign epsilon_node, preserving sigma as the finite-root coordinate. It equals the same sign(c_phi); the two oriented boundary lists, the equation (m-epsilon_node m)w=0 and the resulting even-node choice are unchanged.',
     [r'\varepsilon_{\rm node}'])
exact(r'in the free group \(H_1(\bar E;\mathbb Z)\).',
      r'in the free abelian group \(H_1(\bar E;\mathbb Z)\).',
      'Specify free abelian for the displayed integral first-homology lattice. The group law is the same addition of integer cycles and the primitive w coordinate is unchanged; the boundary equation and conclusion about the node orientation are preserved.',
      ['free abelian group'])

edit('The type-II values satisfy', 'Resolving its edges into parallel lanes',
     lambda text: replace_math(text, {'R': r'R_{\rm II}'}),
     'Name the type-II critical-value radius R_II, preserving R as the later integral rim. Its positive real value (t_b-1)^{-1/m} and both annular inequalities are unchanged, so the same ring tree and inverse isotopy apply.',
     [r'R_{\rm II}'])
exact(r'''For the peripheral words define \(b_j=a^jba^{-j}\),
\(c_j=a^jca^{-j}\).
The stems realize the exact free-word identity
\[
 (bac)^m=(b_0c_1)(b_1c_2)\cdots(b_{m-1}c_m)a^m .
\]''',
      r'''For the peripheral words define
\(\mathfrak b_j=\mathfrak a^j\mathfrak b\mathfrak a^{-j}\),
\(\mathfrak c_j=\mathfrak a^j\mathfrak c\mathfrak a^{-j}\).
The stems realize the exact free-word identity
\[
 (\mathfrak b\mathfrak a\mathfrak c)^m
   =(\mathfrak b_0\mathfrak c_1)(\mathfrak b_1\mathfrak c_2)
     \cdots(\mathfrak b_{m-1}\mathfrak c_m)\mathfrak a^m .
\]''',
      'Name the three peripheral free-group generators frak a,frak b,frak c, preserving the later cochain a and class b and the source radial coordinate c. The generator map sends each old letter to the identically represented based loop, with inverse substitution. Every conjugate and the complete ordered free word remain the same group element.',
      [r'\mathfrak a', r'\mathfrak b', r'\mathfrak c'])

edit('For a transverse geometric thimble with tangent',
     'A small nonzero stem-angle perturbation',
     lambda text: replace_math(text, {'P': r'P_{\rm tan}', 'Q': r'Q_{\rm tan}',
                                     'U': r'c_{\rm tr}', 'V': r's_{\rm tr}'}),
     'Name the two real tangent coefficients P_tan,Q_tan and trigonometric scalars c_tr,s_tr, preserving the quotient-disc map P, intersection pairing Q and ordered/nodal matrices U,V. The values are exactly the original P,Q,cos(phi),sin(phi); both tangent vectors and every factor in the oriented determinant are identical.',
     [r'P_{\rm tan}', r'Q_{\rm tan}', r'c_{\rm tr}', r's_{\rm tr}'])
exact(r' B(z,t)=\bigl(P(z),(1-t)c_P(z)+tc_W(z),',
      r' {\mathcal B}(z,t)=\bigl(P(z),(1-t)c_P(z)+tc_W(z),',
      'Name the embedded interpolating ball map mathcal B, preserving the raw monodromy matrix B. The parametrization has identical coordinates, collapsed incoming boundary and inverse reading q,w and the ordered real radius.',
      [r'{\mathcal B}'])
edit(r'Put \(z=s+it\), \(U=\cos\phi_*\)', 'Terms from the other height',
     lambda text: replace_math(text, {'U': r'c_{{\rm tr},*}',
                                     'V': r's_{{\rm tr},*}'}),
     'Name the fixed-angle trigonometric values c_{tr,*},s_{tr,*}, preserving U,V as the ordered and nodal matrices. They equal cos(phi_*),sin(phi_*) exactly, so N_1,N_2, the normal first jet, its coordinate Jacobian and oriented determinant have identical coordinates and signs.',
     [r'c_{{\rm tr},*}', r's_{{\rm tr},*}'])

def dual_cycle(text):
    text = replace_math(text, {'x': r'x_{\rm PD}'})
    for index in ['i', 'j', 'h']:
        text = text.replace(r'x_{\rm PD}_' + index,
                            r'x_{{\rm PD},' + index + '}')
    return text.replace(r'x_{\rm PD}_{\rm cap}', r'x_{{\rm PD},{\rm cap}}')


edit('The b cochain is', 'For the tangent Pontryagin number',
     dual_cycle,
     'Name the displayed integral dual cycle x_PD, preserving x as the meridian-one cohomology class. Its twelve-entry blocks and cap coordinate are identical, as are Vx_PD=0, the ordered-pairing equation and b(x_PD)=-8k. The image of this same cycle is the Poincare dual of b under the unchanged quotient and intersection form.',
     [r'x_{\rm PD}', r'x_{{\rm PD},'])
exact('Hence the image of x is the integral Poincar\\\'e dual of b, and',
      'Hence the image of \\(x_{\\rm PD}\\) is the integral Poincar\\\'e dual of b, and',
      'Propagate x_PD into the Poincare-dual identification. The image is the same integral cycle class under the same handle quotient; its b pairing is unchanged.',
      [r'x_{\rm PD}'])

edit(r'Let \(\pi:B=S(\bar\nu)\to\bar X_m\)', 'These equations use',
     lambda text: replace_math(text, {'B': r'B_\nu'}),
     'Name the capped normal sphere bundle B_nu, preserving B as the raw monodromy matrix. This is the identical sphere bundle S(bar nu), projection, vertical orientation, tangent bundle and fundamental class. All fibre-integration and Pontryagin pairings use the same maps and meridian class.',
     [r'B_\nu'])
exact(r'\(-P_f\sqcup-B\)', r'\(-P_f\sqcup-B_\nu\)',
      'Propagate B_nu into the oriented deleted-tube bordism boundary. Identity on the same sphere-bundle boundary preserves the stated orientation reversal and return-index comparison.',
      [r'B_\nu'])

def layout_tokens(value):
    value = re.sub(r'\\(?:begin|end)\{(?:aligned|gathered)\}', '', value)
    value = re.sub(r'\\(?:qquad|quad)\b', '', value)
    return re.sub(r'\s+|&|\\\\', '', value)


def layout(before, after, markers):
    assert layout_tokens(before) == layout_tokens(after)
    exact(before, after,
          'Break the unchanged display into aligned or gathered rows so the explicit names have sufficient width. Removing the added layout environments, alignment markers, row breaks and spacing recovers the identical ordered mathematical tokens.',
          markers)


layout(r''' h(Z,V)=(q^2a_{\rm un}Z,qb_{\rm un}V),\qquad
 g(Z,V)=(q^{-3}c_{\rm un}Z,\lambda q^{-1}d_0V),\qquad M=\mathcal O(G-O),''',
       r''' \begin{aligned}
 h(Z,V)&=(q^2a_{\rm un}Z,qb_{\rm un}V),\\
 g(Z,V)&=(q^{-3}c_{\rm un}Z,\lambda q^{-1}d_0V),\qquad M=\mathcal O(G-O),
 \end{aligned}''',
       [r'h(Z,V)&='])
layout(r''' \eta\longmapsto c_{\rm sh}(t)^{\vartheta_{{\rm sh},t}(a)-a}\eta,\qquad
 a=\log\|\eta\|/\log c_{\rm sh}(t),\qquad \vartheta_{{\rm sh},t}(a+1)=\vartheta_{{\rm sh},t}(a)+1,''',
       r''' \begin{gathered}
 \eta\longmapsto c_{\rm sh}(t)^{\vartheta_{{\rm sh},t}(a)-a}\eta,\\
 a=\log\|\eta\|/\log c_{\rm sh}(t),\\
 \vartheta_{{\rm sh},t}(a+1)=\vartheta_{{\rm sh},t}(a)+1,
 \end{gathered}''',
       [r'\vartheta_{{\rm sh},t}'])
layout(r''' s(\rho)=s_0+\int_0^\rho
 \bigl((1-\chi(t))c_{\rm sm}+\chi(t)e^{-1}t^{1/e-1}\bigr)\,dt,\qquad
 c_{\rm sm}=\frac{\rho_1^{1/e}-s_0-\int_0^{\rho_1}
              \chi(t)e^{-1}t^{1/e-1}\,dt}
          {\int_0^{\rho_1}(1-\chi(t))\,dt},''',
       r''' \begin{aligned}
 s(\rho)&=s_0+\int_0^\rho
 \bigl((1-\chi(t))c_{\rm sm}+\chi(t)e^{-1}t^{1/e-1}\bigr)\,dt,\\
 c_{\rm sm}&=\frac{\rho_1^{1/e}-s_0-\int_0^{\rho_1}
              \chi(t)e^{-1}t^{1/e-1}\,dt}
          {\int_0^{\rho_1}(1-\chi(t))\,dt},
 \end{aligned}''',
       [r'c_{\rm sm}'])
layout(r''' 2\pi r c_\phi\bigl(
 \cos^2\alpha(P_{\rm tan}s_{\rm tr}-Q_{\rm tan}c_{\rm tr})^2+\sin^2\alpha(P_{\rm tan}s_{\rm tr}+Q_{\rm tan}c_{\rm tr})^2\bigr),
 \qquad c_{\rm tr}=\cos\phi,\quad s_{\rm tr}=\sin\phi .''',
       r''' \begin{gathered}
 \begin{aligned}
 2\pi r c_\phi\bigl(&
 \cos^2\alpha(P_{\rm tan}s_{\rm tr}-Q_{\rm tan}c_{\rm tr})^2\\
 &+\sin^2\alpha(P_{\rm tan}s_{\rm tr}+Q_{\rm tan}c_{\rm tr})^2\bigr),
 \end{aligned}\\
 c_{\rm tr}=\cos\phi,\quad s_{\rm tr}=\sin\phi .
 \end{gathered}''',
       [r'P_{\rm tan}', r'c_{\rm tr}'])
layout(r'''       &\hspace{24mm}-6j-4,6j+3,-1,-1),\qquad x_{{\rm PD},{\rm cap}}=6k .''',
       r'''       &\hspace{24mm}-6j-4,6j+3,-1,-1),\\
 x_{{\rm PD},{\rm cap}}=&6k .''',
       [r'x_{{\rm PD},'])

# All operations have exact inverses at their actual scopes.
back = proposed
for operation in reversed(operations):
    assert back.count(operation['after']) == 1
    back = back.replace(operation['after'], operation['before'], 1)
assert back == original, 'scoped operation inverse'
for pattern in [r'\\label\{[^}]+\}', r'\\hypertarget\{[^}]+\}', r'\d+']:
    assert re.findall(pattern, proposed) == re.findall(pattern, original), pattern
# New subscripts must be braced before adding old subscripts to the renamed
# integral dual cycle; no double-subscript forms are allowed in the proposal.
for bad in [r'x_{\rm PD}_i', r'x_{\rm PD}_j', r'x_{\rm PD}_{\rm cap}', r'x_{\rm PD}_h']:
    assert bad not in proposed, ('double-subscript candidate', bad)
assert r'\begin{array}{c|c|c}' in proposed
assert proposed.count(r'\begin{array}{c|c|c}') == original.count(r'\begin{array}{c|c|c}')
assert r'\begin{array}{c_{\rm un}' not in proposed

oldlines = original.splitlines(keepends=True)
newlines = proposed.splitlines(keepends=True)
rows = []
matcher = difflib.SequenceMatcher(a=oldlines, b=newlines, autojunk=False)
for number, group in enumerate(matcher.get_grouped_opcodes(n=3), 1):
    a, b = group[0][1], group[-1][2]
    c, d = group[0][3], group[-1][4]
    old, new = ''.join(oldlines[a:b]), ''.join(newlines[c:d])
    assert source.count(old) == 1, ('guard count', number)
    reasons = []
    for operation in operations:
        if any(marker in new for marker in operation['markers']):
            if operation['reason'] not in reasons:
                reasons.append(operation['reason'])
    assert reasons, ('unexplained fragment', number)
    rows.append(dict(
        change_id=f'CLAUDE-III-P15-current02-02S8-{number:03}',
        type='D20', statement_id='night:P3F.31',
        old_location=f'Paper III, tag 02S8; bounded statement/proof fragment {number}',
        old_page='candidate02 568–578 (actual images read by root)',
        new_location='same permanent statement and proof',
        new_page='pending changed build', old_text=old, new_text=new,
        reason=' '.join(reasons),
        review_status='Used and rechecked after exposure. Entire current 02S8 statement/proof and relevant 02S9 imports read. Exact values, maps, inverses, generators, orientations and all changed uses compared. Every scoped inverse and full-source guard inverse passed; numerical literals and labels/targets retained. This agent claims source reading; root owns actual 568–578 images. No independent mathematical-proof credit. Admission and changed rendering pending.'))

candidate = source
for row in rows:
    assert candidate.count(row['old_text']) == 1
    candidate = candidate.replace(row['old_text'], row['new_text'], 1)
restored = candidate
for row in reversed(rows):
    assert restored.count(row['new_text']) == 1
    restored = restored.replace(row['new_text'], row['old_text'], 1)
assert restored == source, 'complete source inverse'

base = OUT / 'S6_SERIES_PUBLISH_c9_current02_02S8_notation'
base.with_suffix('.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n')
base.with_suffix('.diff').write_text(''.join(difflib.unified_diff(
    oldlines, newlines, fromfile='02S8 before', tofile='02S8 proposed', n=5)))
with base.with_name(base.name + '_defects.tsv').open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
print(f'02S8: {len(oldlines)} statement/proof lines; {len(operations)} scoped operations; {len(rows)} guarded rows.')
print('All scoped and full-source inverses, numbers, labels and targets verified. Canonical source unchanged.')
