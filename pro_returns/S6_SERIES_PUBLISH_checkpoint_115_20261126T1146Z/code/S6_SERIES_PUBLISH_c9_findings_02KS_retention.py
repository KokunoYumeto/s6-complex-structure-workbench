#!/usr/bin/env python3
"""Complementary strict-name review of 02KS; root alone admits source edits."""
from pathlib import Path
import re
from S6_SERIES_PUBLISH_c9_scoped_notation import ScopedReview, math_letters

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation9_findings'
source = (ROOT/'S6_SERIES_PUBLISH_III.tex').read_text()
p = ScopedReview(source,
    r'\subsection{The three-component cusp}',
    r'\subsection{Six primitive original families}',
    '02KS', 'maps:src:D.2.18', '222–238',
    'Used and rechecked in this run after exposure. Complete current 02KS definition, statement and proof reread; all named-role contexts and inverse maps compared. Earlier actual candidate02 pages222–238 were read. Exact forward/reverse guards, ordered numeric literals, labels and targets checked. No independent proof credit. Admission and changed rendering pending.')
assert r'\mathsf D}_{\rm gr}' in p.old or r'\mathsf D_{\rm gr}' in p.old, 'Generate only after root admits the global graph-D packet.'

p.edit('The six boundary curves, in a suitable cyclic starting',
       'The residues of the six neighbours',
       lambda t: math_letters(t, {'L': r'L_{\rm bl}'}).replace(
           'E_1', r'E_1^{\rm exc}').replace('E_2', r'E_2^{\rm exc}').replace(
           'E_3', r'E_3^{\rm exc}'),
       'Qualify the blow-up line class L_bl and exceptional classes E_i^{exc}, preserving the later fixed-curve subgroup L and comparison curves E_i. The classes are exactly the old blow-up basis elements, so every boundary-curve class and intersection calculation is unchanged; reverse name substitution is the inverse.',
       [r'L_{\rm bl}', r'^{\rm exc}'])

p.exact(r' V=\begin{pmatrix}-1&-1&2\\2&-1&-1\\-1&2&-1\end{pmatrix}.',
        r' {\mathsf V}_{\rm int}=\begin{pmatrix}-1&-1&2\\2&-1&-1\\-1&2&-1\end{pmatrix}.',
        'Name the fixed-curve intersection matrix mathsf V_int, preserving exterior V and the subsequently qualified orbit sphere. The same nine entries give the same normal-coordinate columns and inverse kernel basis.',
        [r'{\mathsf V}_{\rm int}'])

p.edit('The II component group is trivial.', 'For the star, use the mapping-torus construction',
       lambda t: math_letters(t, {'R': r'R_{\rm log}'}),
       'Name the type-II Lie logarithm R_log, retaining R for the full regular-log transfer matrix. Every Exp(s R_log), backward translation and cutoff product map agrees pointwise with its original value, with the same inverse and endpoint identity.',
       [r'R_{\rm log}'])
p.edit('Use the nonzero line frame and write the contraction as',
       'The angular circle bundle is trivial:',
       lambda t: math_letters(t, {'a': r'u_{\rm II}',
                                 'r': r'r_{\rm roof}', 'k': r'k_{\rm roof}'}),
       'Name the contracting line multiplier u_II, positive roof r_roof and positive smoothing constant k_roof. These are the identical function, roof and real number; the contraction, logarithmic definition, increasing integral, both collar formulas and its inverse retain their values. The integer a, cusp period r and later integer frame correction keep their original roles.',
       [r'u_{\rm II}', r'r_{\rm roof}', r'k_{\rm roof}'])
p.edit(r'\(\exp(2\pi i kt)\)', 'mapping-torus identification.',
       lambda t: math_letters(t, {'k': r'k_{\rm fr}'}),
       'Name the integer boundary-frame correction k_fr. It is the same chosen integer in the same unit multiplier; the reciprocal exponential remains its inverse. The positive real roof constant and flag hyperplane class are separately named.',
       [r'k_{\rm fr}'])

p.edit(r'Define the \(12\times3\) matrix \(C_0\)',
       'The fibre degree-one quotient is',
       lambda t: t.replace('C_0', r'{\mathsf C}_{0,\rm gr}'),
       'Name the graph complement matrix mathsf C_{0,gr}, preserving the boundary curves C_j and the separately qualified orbit spheres. All nonzero rows, the D_gr C_{0,gr} identity, the determinant of [C_{0,gr} K], its adjugate inverse and the last-nine-row coordinates retain their exact entries. This guard is based on the admitted D_gr source.',
       [r'{\mathsf C}_{0,\rm gr}'])
p.edit('For the fibre degree-two map put',
       'The marked section and the real-period triangles',
       lambda t: math_letters(t, {'F': r'{\mathsf F}_{\rm bas}'}),
       'Name the five-column fibre basis matrix mathsf F_bas, retaining F for the flag threefold and F_i for the fixed curves. The same columns, unimodular [s,F_bas] basis, first inverse row and B_2 P_cyl=F_bas identity give the identical quotient map and section.',
       [r'{\mathsf F}_{\rm bas}'])

p.edit('matrix \\(A\\) with \\(Aq_0=e_1\\)',
       'The smooth normal-line trivialization is',
       lambda t: math_letters(t, {'A': r'{\mathsf A}_{\rm Bez}'}),
       'Name the unimodular lattice-completion matrix mathsf A_Bez. Its last rows H_v, inverse columns E_v and first row r_v remain exactly the same, preserving all three inverse-coordinate identities. The homology-group aliases and reconstruction involution receive their own distinct symbols.',
       [r'{\mathsf A}_{\rm Bez}'])
p.exact(r'\(\ell(v)+m\alpha=1\)',
        r'\(\ell(v)+m\alpha_{\rm Bez}=1\)',
        'Qualify the chosen Bezout integer alpha_Bez, preserving alpha(q) as the elliptic period unit. It is the identical integer in the unit identity; the line trivialization and opposite-exponential inverse are unchanged.',
        [r'\alpha_{\rm Bez}'])

def divisor_coefficients(t):
    for index in ['i', '0', '1', '2', '{i+1}', '{i+2}']:
        t = t.replace('d_'+index, 'd_'+index+r'^{\rm div}')
    return t

p.edit('For component coefficients \\(d_i\\)',
       r'\emph{The circle quotient.}', divisor_coefficients,
       'Qualify the arbitrary divisor coefficients d_i^{div}, retaining d_0 for the type-II fibre row and d_1,d_2 for the two logarithmic gcds. The cubic is evaluated on the identical linear combination of divisor classes; polarization, adjacent-index differences and every coefficient retain their original values.',
       [r'^{\rm div}'])

p.edit('and preserves \\(\\pi_1\\). The bundle sequence and Hurewicz give',
       'Adjoining the normal',
       lambda t: math_letters(t, {'A': r'{\mathcal A}_{\rm hom}',
                                 'B': r'{\mathcal B}_{\rm hom}'}),
       'Name the two free-circle homology-group aliases mathcal A_hom and mathcal B_hom, preserving the lattice matrix and collar translation previously denoted A and B. These aliases refer to the very same H_2 groups. The map p_*, Euler evaluation, splitting and inverse keep the same values on every class.',
       [r'{\mathcal A}_{\rm hom}', r'{\mathcal B}_{\rm hom}'])

def orbit_curves(t):
    sentinel = r'\mathbf{QKSFIELD}'
    assert sentinel not in t
    t = t.replace(r'\mathbb C', sentinel)
    t = math_letters(t, {'C': r'{\mathcal C}'})
    return t.replace(sentinel, r'\mathbb C')


p.edit(r'\(C_i\) for the three quotient spheres', r'\end{proof}',
       orbit_curves,
       'Print the three quotient spheres as mathcal C_i, preserving C_j for the six boundary curves and mathsf C_{0,gr} for the graph matrix. Identity on each sphere identifies its push-off, zero homology class, meridian, localization, link, normal framing and reconstruction. Every indexed occurrence through the final quotient pair is propagated.',
       [r'{\mathcal C}'])
p.edit('The quotient of the original-star representative of', r'\end{proof}',
       lambda t: math_letters(t, {'V': r'{\mathcal V}_{\rm orb}'}),
       'Name the embedded orbit sphere mathcal V_orb. It is the same quotient of the original-star representative U, with the same component section, primitive class and complement. All intersection, isotopy-support, Euler, cohomology and final reconstruction uses retain this identical sphere; the regular exterior V is unchanged.',
       [r'{\mathcal V}_{\rm orb}'])

p.edit(r'Let \(a,b\) be the integral basis dual',
       r'\emph{Reconstruction and the suspension framing.}',
       lambda t: math_letters(t, {'a': r'a_{\rm fl}', 'b': r'b_{\rm fl}'}),
       'Qualify the two integral flag-block cohomology classes a_fl,b_fl, preserving the integer logarithmic data. They are the identical dual basis to F_0,F_1. Their divisor coordinates, cubic, mixed evaluations, inverse pullback and recognition maps have exactly the same values.',
       [r'a_{\rm fl}', r'b_{\rm fl}'])
p.edit(r'Let \(h,k\) be the hyperplane classes',
       r'\emph{Reconstruction and the suspension framing.}',
       lambda t: math_letters(t, {'h': r'h_{\rm fl}', 'k': r'k_{\rm fl}'}),
       'Qualify the two flag hyperplane classes h_fl,k_fl. The projective-bundle presentation, both primitive evaluations, characteristic classes, forward cohomology map and inverse use the same original classes. The subsequent bordism h invariant is separately qualified in the next bounded operation.',
       [r'h_{\rm fl}', r'k_{\rm fl}'])
p.edit('Their \\(P\\) invariants are one quarter',
       'That uniqueness gives an orientation-preserving diffeomorphism',
       lambda t: t.replace(r'\(P\)', r'\(P_{\rm bord}\)')
                  .replace(r'Their \(h_{\rm fl}\)', r'Their \(h_{\rm bord}\)')
                  .replace(r'\((P,h_{\rm fl})\)', r'\((P_{\rm bord},h_{\rm bord})\)'),
       'Name the cited spin-bordism invariants P_bord,h_bord, preserving the marked section P and the hyperplane class h_fl. These are the identical two invariant maps from the cited theorem: their values and the four detecting monomials remain the same, so the asserted injectivity and class comparison are unchanged.',
       [r'P_{\rm bord}', r'h_{\rm bord}'])

p.edit('The opposite-direction mapping-torus',
       'Take the equivariant oriented connected sum',
       lambda t: math_letters(t, {'A': r'{\mathsf A}_{\rm inv}'}),
       'Name the reconstruction involution mathsf A_inv. Its five diagonal entries are unchanged, it remains its own inverse and its conjugation reverses the same clutch rotation. The collar homotopy and framed gluing maps are retained.',
       [r'{\mathsf A}_{\rm inv}'])

def clutch_name(t):
    t = t.replace(r'\alpha_z', r'\alpha_{{\rm rot},z}')
    return re.sub(r'\\alpha(?![A-Za-z_])', lambda _: r'\alpha_{\rm rot}', t)


p.edit(r'The model \(\widetilde\Sigma_0', r'\end{proof}', clutch_name,
       'Qualify the reconstruction clutch loop as alpha_rot and its value at z as alpha_{rot,z}, retaining alpha(q) for the elliptic period unit. The loop, its opposite-direction conjugacy, all collar maps and inverse rotations remain pointwise identical.',
       [r'\alpha_{\rm rot}', r'\alpha_{{\rm rot},z}'])

# The two named free holomorphic units in the period formula are kept
# distinct from the later Chern-class operators c_1 and c_2.
p.edit(r' (c_1(q)q^{3a+4b}X_1,c_2(q)q^bX_2,q)',
       'The inverse divides by these same units and',
       lambda t: t.replace('c_1', r'u_{1,\rm per}').replace(
           'c_2', r'u_{2,\rm per}').replace('c_j', r'u_{j,\rm per}'),
       'Qualify the period-unit functions u_{j,per}, preserving the Chern-class operators. Each function is the identical product of the original nonzero units; the valuation map and division inverse therefore agree pointwise.',
       [r'u_{1,\rm per}', r'u_{j,\rm per}'])
p.edit(r'\(z\mapsto(\epsilon\overline z,\epsilon z,c)\)',
       'Swapping the two angular coordinates',
       lambda t: math_letters(t, {'c': r'c_{\rm disc}'}),
       'Name the fixed nonzero normal-disc chart constant c_disc, preserving the integer logarithmic coefficient c. The disc, its fixed base value, its positive angular boundary and inverse chart are exactly the same pointwise maps.',
       [r'c_{\rm disc}'])


def layout(old, new, marker):
    def tokens(t):
        t = re.sub(r'\\(?:begin|end)\{(?:aligned|gathered)\}', '', t)
        t = t.replace(r'\\', '').replace('&', '')
        t = t.replace('\\ ', '')
        t = re.sub(r'\\(?:qquad|quad|,|;|!)', '', t)
        return re.sub(r'\s+', '', t)
    assert tokens(old) == tokens(new), ('layout mathematics', marker)
    p.exact(old, new,
            'Break the qualified-name display into readable rows. Removing only alignment environments, row separators, alignment marks and spacing gives the identical ordered mathematical tokens; every expression and its value are retained.',
            [marker])


layout(
 r''' (X_1,X_2,q)\longmapsto
 (u_{1,\rm per}(q)q^{3a+4b}X_1,u_{2,\rm per}(q)q^bX_2,q),\qquad (a,b)\in\mathbb Z^2,''',
 r''' \begin{gathered}
 (X_1,X_2,q)\longmapsto
 (u_{1,\rm per}(q)q^{3a+4b}X_1,u_{2,\rm per}(q)q^bX_2,q),\\
 (a,b)\in\mathbb Z^2,
 \end{gathered}''', r'u_{1,\rm per}')
layout(
 r''' E_1^{\rm exc},\ L_{\rm bl}-E_1^{\rm exc}-E_2^{\rm exc},\ E_2^{\rm exc},\ L_{\rm bl}-E_2^{\rm exc}-E_3^{\rm exc},\ E_3^{\rm exc},\ L_{\rm bl}-E_3^{\rm exc}-E_1^{\rm exc}.''',
 r''' \begin{gathered}
 E_1^{\rm exc},\ L_{\rm bl}-E_1^{\rm exc}-E_2^{\rm exc},\ E_2^{\rm exc},\\
 L_{\rm bl}-E_2^{\rm exc}-E_3^{\rm exc},\ E_3^{\rm exc},\ L_{\rm bl}-E_3^{\rm exc}-E_1^{\rm exc}.
 \end{gathered}''', r'L_{\rm bl}')
layout(
 r''' \Big\langle\Big(\sum d_i^{\rm div}\eta_i\Big)^3,[X]\Big\rangle
 =3(2d_0^{\rm div}-d_1^{\rm div}-d_2^{\rm div})(2d_1^{\rm div}-d_0^{\rm div}-d_2^{\rm div})(2d_2^{\rm div}-d_0^{\rm div}-d_1^{\rm div}).''',
 r''' \begin{aligned}
 \Big\langle\Big(\sum d_i^{\rm div}\eta_i\Big)^3,[X]\Big\rangle
 &=3(2d_0^{\rm div}-d_1^{\rm div}-d_2^{\rm div})\\
 &\quad (2d_1^{\rm div}-d_0^{\rm div}-d_2^{\rm div})(2d_2^{\rm div}-d_0^{\rm div}-d_1^{\rm div}).
 \end{aligned}''', r'd_i^{\rm div}')
layout(
 r''' \pi_1({\mathcal Q}_0)=0,\qquad
 0\longrightarrow {\mathcal A}_{\rm hom}:=H_2(X)
 \xrightarrow{p_*} {\mathcal B}_{\rm hom}:=H_2({\mathcal Q}_0)
 \xrightarrow{\langle e,-\rangle}\mathbb Z\longrightarrow0.''',
 r''' \begin{gathered}
 \pi_1({\mathcal Q}_0)=0,\\
 0\longrightarrow {\mathcal A}_{\rm hom}:=H_2(X)
 \xrightarrow{p_*} {\mathcal B}_{\rm hom}:=H_2({\mathcal Q}_0)
 \xrightarrow{\langle e,-\rangle}\mathbb Z\longrightarrow0.
 \end{gathered}''', r'{\mathcal A}_{\rm hom}')
layout(
 r''' \eta_0=-a_{\rm fl}-b_{\rm fl},\qquad \eta_1=2a_{\rm fl}-b_{\rm fl},\qquad \eta_2=-a_{\rm fl}+2b_{\rm fl}.''',
 r''' \begin{gathered}
 \eta_0=-a_{\rm fl}-b_{\rm fl},\qquad \eta_1=2a_{\rm fl}-b_{\rm fl},\\
 \eta_2=-a_{\rm fl}+2b_{\rm fl}.
 \end{gathered}''', r'a_{\rm fl}')
layout(
 r''' H^*(F;\mathbb Z)=
 \mathbb Z[h_{\rm fl},k_{\rm fl}]/(h_{\rm fl}^3,k_{\rm fl}^2-h_{\rm fl}k_{\rm fl}+h_{\rm fl}^2),\qquad
 \langle h_{\rm fl}^2k_{\rm fl},[F]\rangle=1.''',
 r''' \begin{gathered}
 H^*(F;\mathbb Z)=
 \mathbb Z[h_{\rm fl},k_{\rm fl}]/(h_{\rm fl}^3,k_{\rm fl}^2-h_{\rm fl}k_{\rm fl}+h_{\rm fl}^2),\\
 \langle h_{\rm fl}^2k_{\rm fl},[F]\rangle=1.
 \end{gathered}''', r'h_{\rm fl}')
layout(
 r''' c_1(F)=2h_{\rm fl}+2k_{\rm fl},\qquad
 p_1(F)=3h_{\rm fl}^2+3k_{\rm fl}^2-(h_{\rm fl}+k_{\rm fl})^2=2(h_{\rm fl}^2-h_{\rm fl}k_{\rm fl}+k_{\rm fl}^2)=0.''',
 r''' \begin{gathered}
 c_1(F)=2h_{\rm fl}+2k_{\rm fl},\\
 \begin{aligned}
 p_1(F)&=3h_{\rm fl}^2+3k_{\rm fl}^2-(h_{\rm fl}+k_{\rm fl})^2\\
 &=2(h_{\rm fl}^2-h_{\rm fl}k_{\rm fl}+k_{\rm fl}^2)=0.
 \end{aligned}
 \end{gathered}''', r'k_{\rm fl}')

assert p.new.count(r'\mathbb C') == p.old.count(r'\mathbb C')
assert r'\alpha_{\rm rot}_z' not in p.new
p.exact(' \\end{gathered}\n\\]\n\nThe residues of the six neighbours',
        ' \\end{gathered}\n\\]\nHere \\(L_{\\rm bl}\\) is the pullback of a projective line and\n'
        '\\(E_i^{\\rm exc}\\) are the exceptional classes.\n\nThe residues of the six neighbours',
        'Bind the qualified blow-up basis names to the same line and exceptional classes used by the preceding blow-up map. This states their existing geometric definitions explicitly; the boundary-class formulas and intersection pairing are unchanged.',
        [r'L_{\rm bl}', r'E_i^{\rm exc}'])

rows = p.finish(OUT, 'S6_SERIES_PUBLISH_c9_current02_02KS_retention')
# This is an addendum to the previously admitted 02KS rows, not a reuse
# of their defect identifiers. Rewrite only the artifact metadata.
for row in rows:
    row['change_id'] = row['change_id'].replace('-02KS-', '-02KS-retention-')
import csv
import json
stem = 'S6_SERIES_PUBLISH_c9_current02_02KS_retention'
(OUT/(stem+'.json')).write_text(json.dumps(rows, ensure_ascii=False, indent=2)+'\n')
with (OUT/(stem+'_defects.tsv')).open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
print('All current role scopes read; canonical manuscript unchanged.')
