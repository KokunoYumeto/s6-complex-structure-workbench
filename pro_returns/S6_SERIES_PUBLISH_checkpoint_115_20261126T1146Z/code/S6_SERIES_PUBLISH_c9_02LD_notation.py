#!/usr/bin/env python3
"""Stage exact, reversible notation/wording edits for the complete 02LD proof.

The canonical manuscript is read only.  Each operation has an exact inverse;
the final guards are tested in both directions against the complete source.
"""
from pathlib import Path
import csv
import difflib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation9_findings'
source = (ROOT / 'S6_SERIES_PUBLISH_III.tex').read_text()
anchor = source.index(r'\hypertarget{tag-02LD}{}')
start = source.rfind(r'\begin{theorem}', 0, anchor)
proof = source.index(r'\begin{proof}', anchor)
end = source.index(r'\end{proof}', proof) + len(r'\end{proof}')
original = source[start:end]
proposed = original
operations = []


def word(letter, target):
    """Replace an unindexed TeX symbol, not a command, word or indexed family."""
    return lambda text: re.sub(r'(?<![A-Za-z_\\])' + re.escape(letter) +
                               r'(?![A-Za-z_])', lambda _: target, text)


def literal(pairs):
    def transform(text):
        for before, after in pairs:
            assert before in text, ('missing literal', before)
            text = text.replace(before, after)
        return text
    return transform


def edit(first, last, transform, reason, markers):
    global proposed
    a = proposed.index(first)
    b = proposed.index(last, a) if last else len(proposed)
    before = proposed[a:b]
    after = transform(before)
    assert before != after, ('empty change', first)
    assert proposed.count(before) == 1
    proposed = proposed[:a] + after + proposed[b:]
    operations.append(dict(before=before, after=after, reason=reason,
                           markers=markers))


def exact(before, after, reason, markers):
    global proposed
    assert proposed.count(before) == 1, ('exact guard', before)
    proposed = proposed.replace(before, after, 1)
    operations.append(dict(before=before, after=after, reason=reason,
                           markers=markers))


edit('At a finite-good site of linear order', 'For each free such logarithm',
     lambda text: word('F', r'F_{\rm fix}')(text).replace('Fz', r'F_{\rm fix}z'),
     'Use F_fix for the primitive fixed-basis map, matching its existing name in the proof. The map has precisely the same two columns and inverse coordinates: F_fix(x)=F_old(x) for every x in Z^2. The projected lattice and invariant power are unchanged.',
     [r'F_{\rm fix}'])

for first, last in [
    ('At a finite-good site of linear order', 'For each free such logarithm'),
    (r'\emph{Every finite-good affine logarithm and its full kernel.}',
     r'\emph{Full normal Thom columns, including the root generator.}')]:
    edit(first, last,
         lambda text: word('H', r'H_{\rm norm}')(text).replace(r'hH^{-1}', r'hH_{\rm norm}^{-1}'),
         'Use H_norm for the two-column norm-image basis, retaining H_d for the four-dimensional conjugacy. H_norm is the identical integer matrix H_old; the maps H_norm^{-1} F_fix^{-1} N_h, h H_norm^{-1}, the projected lattice, every power coordinate and its integral section retain the same entries.',
         [r'H_{\rm norm}'])

edit(r'\emph{Existence at every finite-good position.}',
     r'\emph{The torsion and the normal character.}',
     literal([('H_1', r'H_{1,\rm norm}')]),
     'Use H_{1,norm} for the weight-one norm-image basis, preserving the already defined four-by-four conjugacy H_1 and the homology functor. The two diagonal formulas, projected coordinates w_± and transported basis are exactly the original two-by-two matrices.',
     [r'H_{1,\rm norm}'])

exact(r'These follow by summing \(I+A_1+\cdots+A_1^{h-1}\) and applying',
      r'These follow by summing \(I+A(1)+\cdots+A(1)^{h-1}\) and applying',
      'Write the weight-one additive return as A(1), using the already displayed family A(d) and conjugacy A(d)H_d=H_dA(1). The identity S_1=I gives A(1)=A_i at the currently selected site, so every term of the norm sum is the identical endomorphism. This removes the competing reading of A_1 as the globally indexed first-site matrix.',
      [r'I+A(1)+\cdots+A(1)^{h-1}'])

for first, last in [
    ('Write its abelianization as', r'\end{theorem}'),
    ('The abelianization matrix,', r'\emph{Enumeration and the two starred-cap scopes.}')]:
    edit(first, last, literal([('A_1', r'A_{1,\rm tor}')]),
         'Use A_{1,tor} for the torsion summand of the displayed Seifert abelianization, preserving A_1 in the actual monodromy norm sum. Identity on the same Smith torsion coordinates identifies the groups, dual linking characters and all homology-table entries. The coefficient ring mathcal A_d is also retained unchanged.',
         [r'A_{1,\rm tor}'])

edit('In a line frame with multiplier', 'The inclusion of groups',
     word('u', r'u_{\rm line}'),
     'Use u_line for the nonzero line multiplier, preserving u as a marked vanishing vector. The function agrees pointwise with the old multiplier, so its ordered translated product, divisor and lifted contraction are identical.',
     [r'u_{\rm line}'])

edit(r'\emph{Raw matrices and complete primitive exterior maps.}',
     'Substitution of the defining elliptic matrices',
     literal([('c_i', r'c_{i,\rm mat}')]),
     'Use c_{i,mat} for the angular entry of the raw period matrix, preserving c_i for the peripheral group generator. Each integer entry equals its original expression, so the full period matrix, ordered product and all induced wedge maps are unchanged.',
     [r'c_{i,\rm mat}'])

edit(r'Choose integers \(\alpha,\beta\)', 'This is an integer right inverse',
     literal([(r'\alpha', r'\alpha_{\rm Bez}'),
              (r'\beta', r'\beta_{\rm Bez}')]),
     'Name the two Bezout coefficients alpha_Bez and beta_Bez, preserving beta as the component-defect total. Their values and alpha_Bez a + beta_Bez d = 1 identity are unchanged; the literal combination giving R_d and G_d R_d = I_3 is the same right inverse.',
     [r'\alpha_{\rm Bez}', r'\beta_{\rm Bez}'])

edit(r'Indeed choose \(u,v\in\mathbb Z\)',
     'These formulas give both inverse composites.',
     literal([(r'\(u,v\in', r'\(u_{\rm Bez},v_{\rm Bez}\in'),
              ('ua+vdb=1', r'u_{\rm Bez}a+v_{\rm Bez}db=1'),
              ('s_0=u e_{12}-v', r's_0=u_{\rm Bez} e_{12}-v_{\rm Bez}'),
              (r'\(v x_{12}+u x_', r'\(v_{\rm Bez} x_{12}+u_{\rm Bez} x_')]),
     'Name the wedge-section Bezout integers u_Bez and v_Bez, preserving the marked vanishing vector u and affine power v. The same two integers give the same s_0 and the same last relation coordinate, so both inverse composites are literally preserved.',
     [r'u_{\rm Bez}', r'v_{\rm Bez}'])

edit(r'\emph{The weighted cusp and its integral boundary.}',
     r'\emph{Component powers and unchanged component defects.}',
     lambda text: word('C', r'{\mathsf C}')(text).replace('Ce_', r'{\mathsf C}e_'),
     'Use mathsf C for the cusp comparison matrix. It has the same four entries and determinant one; both short-coordinate maps mathsf C and mathsf C^{-1}, all four basis vectors, and the physical short thimbles remain identical.',
     [r'{\mathsf C}'])

edit(r'Write \(S_{\mathrm{bas}}=', 'This is a coordinate map on the period subgroup;',
     word('L', r'{\mathsf L}'),
     'Use mathsf L for the ordered long-period basis (r,gamma), preserving L as the count of nonzero-Chern original caps. Its columns and all four vectors in the determinant-one basis are identical, with the same coordinate inverse.',
     [r'{\mathsf L}'])

for first, last in [
    ('The quotient, section and relation-coordinate inverse are',
     'The Wang sequence adds'),
    ('For both the original and the marked Mumford filling,',
     'The three fixed-normal sweeps bound in both fillings.')]:
    edit(first, last,
         lambda text: re.sub(r'(?<![A-Za-z\\])Q(?![A-Za-z])',
                             lambda _: r'{\mathsf Q}', text),
         'Use mathsf Q and mathsf Q_d for the explicit wedge quotient maps, preserving the section Q. The coordinate formulas agree pointwise with the original Q maps, and the same sigma sections, Q sigma = I identities and relation-coordinate inverse remain in place.',
         [r'{\mathsf Q}'])

edit(r'\emph{Component powers and unchanged component defects.}',
     r'At a multiplicative site \(I_\nu\)',
     literal([(r'\sigma', r'\sigma_{\rm perm}')]),
     'Use sigma_perm for the component permutation, preserving sigma for the explicit quotient section. It is the identical permutation on the same finite component set; its d-th power, inverse exponent, orbit indexing and two integral relation-subgroup identities are unchanged.',
     [r'\sigma_{\rm perm}'])

edit('At every additive site write',
     r'\emph{Multiplicative caps with nonzero Chern class.}',
     lambda text: word('B', r'B_{\rm ell}')(text).replace('JB,', r'JB_{\rm ell},'),
     'Use B_ell for the local two-dimensional elliptic block, preserving B for the complete global boundary matrix. B_ell equals B_old entry by entry, so z, A(d), the integral conjugacy, T_3, its coinvariants and all ensuing cap maps are the same.',
     [r'B_{\rm ell}'])

edit('At every additive site write',
     r'\emph{Multiplicative caps with nonzero Chern class.}',
     lambda text: re.sub(r'\\beta(?![A-Za-z_])',
                         lambda _: r'\beta_{\rm row}', text),
     'Use beta_row for the local angular row, preserving beta as the total component defect and beta_0 as the primitive lift. The row has identical entries; multiplication in A(d), the angular conjugacy check and T_3 therefore use exactly the original linear maps.',
     [r'\beta_{\rm row}'])

edit(r'\emph{Zero-Chern original additive caps.}',
     r'\emph{Multiplicative caps with nonzero Chern class.}',
     word('N', r'N_{\rm loc}'),
     'Use N_loc for the local Kodaira plumbing, preserving N for the total number of sites. Identity on the same neighbourhood identifies its central fibre inclusion, circle bundle, translation mapping torus and homology maps.',
     [r'N_{\rm loc}'])
exact(r'\(H_2(N)=\mathbb Z^{s_j}\)',
      r'\(H_2(N_{\rm loc})=\mathbb Z^{s_j}\)',
      'Propagate N_loc into the later relative-disc calculation. The exact same local plumbing and its component basis compute the displayed H^4 group.',
      [r'N_{\rm loc}'])

edit(r'Let \(U_j\) be its component-orbit basis',
     'The forward basis change replaces',
     literal([('U_j', r'U_j^{\rm orb}')]),
     'Use U_j^{orb} for the component-orbit basis vectors, preserving U_j for the remaining cap spaces in the later relative attachment. Identity on each component-orbit cycle identifies the basis and direct-sum coordinates.',
     [r'U_j^{\rm orb}'])
exact(r'The forward basis change replaces \(U_1\) by $W$.',
      r'The forward basis change replaces \(U_1^{\rm orb}\) by $W$.',
      'Propagate the component-orbit basis name into the primitive basis change. Its x_1 and x_j-w_j x_1 inverse coordinates are unchanged.',
      [r'U_1^{\rm orb}'])

edit(r'\emph{Nonzero-Chern original additive caps.}',
     r'\emph{Multiplicative caps with nonzero Chern class.}',
     word('F', r'F_{\rm fib}'),
     'Use F_fib for the whole-fibre multiplicity vector. It is the identical vector (m_j), and the same component-kernel basis, inverse coordinates and e_12 image are retained.',
     [r'F_{\rm fib}'])

edit('The primitive coinvariant row is',
     'The original cap sends',
     literal([(r'\rho', r'\rho_{\rm cov}')]),
     'Use rho_cov for the primitive coinvariant row, preserving rho as the component-orbit count. The row, equation rho_cov v_0 = 1, mixed-product coordinate and integral Wang section agree entry by entry with the original maps.',
     [r'\rho_{\rm cov}'])

edit(r'Let \(u=\gcd(m,v_1,v_2,v_3,v_4)\).',
     'All remaining obstruction indices',
     word('u', r'g_{\rm pow}'),
     'Use g_pow for the integer gcd obstruction, preserving the marked vanishing vector u. The integer and the proper power m/g_pow have exactly the old values; every fixed-point and every-power freeness criterion is unchanged.',
     [r'g_{\rm pow}'])

edit('unimodular matrix $V$, giving the coordinate maps',
     r'Consequently \(\delta+\ell_d\)',
     word('V', r'V_{\rm bas}'),
     'Use V_bas for the unimodular change of projected-lattice basis, preserving V as the torus-bundle exterior. The matrix and the inverse-coordinate pair V_bas^{-1},V_bas are literally identical to the original pair.',
     [r'V_{\rm bas}'])

for first, last in [
    (r'At \(I_\nu\), choose \(u,r\)',
     'At every other fibre'),
    (r'Write \(S_{\mathrm{bas}}=',
     'This is a coordinate map on the period subgroup;'),
    (r'\emph{Multiplicative caps with nonzero Chern class.}',
     r'\emph{Every finite-good affine logarithm and its full kernel.}')]:
    edit(first, last,
         lambda text: word('r', r'r_{\rm per}')(text).replace('=xr+', r'=xr_{\rm per}+'),
         'Use r_per for the complementary marked elliptic period, preserving r as the rank of the Seifert abelianization. At each selected local marking r_per is exactly the previously chosen period; determinant-one bases, long shears, covectors, rim classes, the primed basis and their stated inverses are unchanged.',
         [r'r_{\rm per}'])

exact('then the remaining return exponent $r$,\nand writes \\(\\gamma^r c_i^j\\).',
      'then the remaining return exponent $k_{\\rm ret}$,\nand writes \\(\\gamma^{k_{\\rm ret}} c_i^j\\).',
      'Use k_ret for the normal-form return exponent, preserving r as the homology rank. The integer read from the lifted loop is identical, and the same word gamma^{k_ret} c_i^j gives the inverse local-group map.',
      [r'k_{\rm ret}'])

for before, after in [
    ('Its quotient inside the free group obtained',
     'Its quotient inside the free abelian group obtained'),
    ('rank-zero subgroup of a free group and is zero.',
     'rank-zero subgroup of a free abelian group and is zero.'),
    ('and the remaining component cokernel is the free group\n',
     'and the remaining component cokernel is the free abelian group\n')]:
    exact(before, after,
          'Specify free abelian for the explicit integral homology lattice. The group law and basis are the same displayed additive Z-coordinate group; the primitive quotient and rank-zero argument are unchanged.',
          ['free abelian group'])

exact(r''' \sigma_{\rm perm}^d-I=(\sigma_{\rm perm}-I)(I+\cdots+\sigma_{\rm perm}^{d-1}),\qquad
 \sigma_{\rm perm}-I=(\sigma_{\rm perm}^d-I)(I+\sigma_{\rm perm}^d+\cdots+\sigma_{\rm perm}^{(E-1)d}).''',
      r''' \begin{aligned}
 \sigma_{\rm perm}^d-I
   &=(\sigma_{\rm perm}-I)(I+\cdots+\sigma_{\rm perm}^{d-1}),\\
 \sigma_{\rm perm}-I
   &=(\sigma_{\rm perm}^d-I)(I+\sigma_{\rm perm}^d+\cdots+\sigma_{\rm perm}^{(E-1)d}).
 \end{aligned}''',
      'Place the two unchanged component-permutation identities on separate aligned rows so their explicit subscript remains legible. Removing only aligned, alignment markers, row breaks and spacing recovers the same ordered mathematical tokens.',
      [r'\sigma_{\rm perm}'])

# Reversing the actual scoped operations avoids any global replacement when an
# alias already denotes the same role in another explicitly bound local case.
back = proposed
for operation in reversed(operations):
    assert back.count(operation['after']) == 1
    back = back.replace(operation['after'], operation['before'], 1)
assert back == original, 'scoped operation inverse'
for marker in [r'D_B', r'\gamma_B', r'B_{\rm Bez}', r'\mathcal B_d']:
    assert proposed.count(marker) == original.count(marker), marker
for stale in ['Fz', r'hH^{-1}', r'S_{\mathrm{bas}}Ce_',
              'JB,', '=xr+', r'D_B_{', r'\gamma_B_{']:
    assert stale not in proposed, ('stale/invalid renamed occurrence', stale)
for pattern in [r'\\label\{[^}]+\}', r'\\hypertarget\{[^}]+\}', r'\d+']:
    assert re.findall(pattern, proposed) == re.findall(pattern, original), pattern

oldlines = original.splitlines(keepends=True)
newlines = proposed.splitlines(keepends=True)
matcher = difflib.SequenceMatcher(a=oldlines, b=newlines, autojunk=False)
rows = []
for number, group in enumerate(matcher.get_grouped_opcodes(n=3), 1):
    a, b = group[0][1], group[-1][2]
    c, d = group[0][3], group[-1][4]
    old = ''.join(oldlines[a:b])
    new = ''.join(newlines[c:d])
    assert source.count(old) == 1, ('guard count', number)
    reasons = []
    for operation in operations:
        if any(marker in new for marker in operation['markers']):
            if operation['reason'] not in reasons:
                reasons.append(operation['reason'])
    assert reasons, ('unexplained hunk', number)
    rows.append(dict(
        change_id=f'CLAUDE-III-P15-current02-02LD-{number:03}',
        type='D20', statement_id='maps:src:D.2.37',
        old_location=f'Paper III, tag 02LD; guarded statement/proof fragment {number}',
        old_page='candidate02 338–358; own actual images through 348, backend images 349–358',
        new_location='same permanent statement and proof',
        new_page='pending changed build', old_text=old, new_text=new,
        reason=' '.join(reasons),
        review_status='Used and rechecked after exposure. Entire current theorem and 1619-line proof read, including all normal maps, relative attachments, group arguments, duality and enumeration. Exact reverse of every scoped operation and every final source guard passed; numeric literals and all labels/targets retained. No independent mathematical-proof credit. Root admission and changed-PDF reading pending.'))

candidate = source
for row in rows:
    assert candidate.count(row['old_text']) == 1
    candidate = candidate.replace(row['old_text'], row['new_text'], 1)
restored = candidate
for row in reversed(rows):
    assert restored.count(row['new_text']) == 1
    restored = restored.replace(row['new_text'], row['old_text'], 1)
assert restored == source, 'full manuscript inverse'

base = OUT / 'S6_SERIES_PUBLISH_c9_current02_02LD_notation'
base.with_suffix('.diff').write_text(''.join(difflib.unified_diff(
    oldlines, newlines, fromfile='02LD before', tofile='02LD proposed', n=5)))
base.with_suffix('.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n')
fields = list(rows[0])
with base.with_name(base.name + '_defects.tsv').open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
print(f'02LD: {len(oldlines)} statement/proof lines; {len(operations)} reversible scoped operations; {len(rows)} exact guarded rows.')
print('Every scoped inverse, complete-manuscript inverse, numeric literal, label and target check passed. Canonical source unchanged.')
