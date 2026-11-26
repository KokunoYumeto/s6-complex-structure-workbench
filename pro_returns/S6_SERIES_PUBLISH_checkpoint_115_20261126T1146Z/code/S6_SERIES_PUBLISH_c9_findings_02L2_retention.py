#!/usr/bin/env python3
"""Complete 02L2 retained-role comparison; canonical source is read only."""
from pathlib import Path
from datetime import datetime, timezone
import csv, difflib, json, re
from S6_SERIES_PUBLISH_c9_scoped_notation import ScopedReview, math_letters
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation9_findings'
source=(ROOT/'S6_SERIES_PUBLISH_III.tex').read_text()
stem='S6_SERIES_PUBLISH_c9_current02_02L2_retention'
p=ScopedReview(source,
 r'\begin{theorem}[Integral obstructions for the three $I_1^*$ profiles]',
 r'\subsection{The classification over twenty-one profiles}',
 '02L2','maps:src:D.2.27','283--292; Theorem 11.5',
 'Used and rechecked in this run after exposure. Complete current statement/proof and directly affected imports read. Selected coefficients, periods, quotient/lift maps, conductor, specialization and kernel inverses compared. Scoped/full-source reversals and numeric/identifier comparisons. No independent proof, new computation or image credit. Admission and changed rendering pending.')

def math(t,mapping):
    saved=[]
    def protect(m):
        saved.append(m.group())
        return '\ue000'+str(len(saved))+'\ue001'
    t=re.sub(r'\\rm [A-Za-z,]+|\\mathbb [A-Za-z]',protect,t)
    t=math_letters(t,mapping)
    def equation(m):
        inner=math_letters(r'\['+m.group(1)+r'\]',mapping)[2:-2]
        return r'\begin{equation}'+inner+r'\end{equation}'
    t=re.sub(r'\\begin\{equation\}([\s\S]*?)\\end\{equation\}',equation,t)
    for i,value in enumerate(saved,1): t=t.replace('\ue000'+str(i)+'\ue001',value)
    return t

def letters(first,last,mapping,reason):
    p.edit(first,last,lambda t:math(t,mapping),reason,list(mapping.values()))

def star_operator(t):
    t=t.replace('T^4','\ue002').replace('H^2(T^2;','\ue003')
    t=math(t,{'T':r'{T_{\rm st}}'})
    return t.replace('\ue002','T^4').replace('\ue003','H^2(T^2;')

p.edit(r'\emph{The marked inputs and the primitive star periods.}',
 r'\emph{Additional multiplicative root quotients.}',star_operator,
 'Name the marked star return T_st. Preserve standard torus notation, all entries, H conjugacy, exterior relations, fixed lattice, Wang maps and normal indices.',[r'T_{\rm st}'])
letters('Here $\\langle G,G\\rangle=1/12$.','First take $a$ odd',
 {'g':r'{g_{\rm ell}}','C':r'{\mathsf C_{\rm st}}'},
 'Name the elliptic cocycles g_ell and its primed representative and the marking conjugacy mathsf C_st. Vector entries, conjugacy and inverse are identical; the root path g keeps its group meaning.')
p.exact('First take $a$ odd and write $b=4B$, where $B$ is odd.',
 'First take $a$ odd and write $b=4B_{\\rm per}$, where $B_{\\rm per}$ is odd.',
 'Name the selected integer b/4 as B_per, preserving its value and parity.',[r'B_{\rm per}'])
letters('Set $s=(a+1)/2$','The primitive exterior-square relation columns',
 {'s':r'{s_{\rm per}}','k':r'{k_{\rm per}}','h':r'{h_{\rm per}}'},
 'Name the selected period coefficients s_per,k_per,h_per. The H matrix, determinant, inverse adjugate and fixed-period shear have identical entries.')
letters('For the other half, $4\\mid a$',r'\emph{Original star caps and the rational rank obstruction.}',
 {'w':r'{w_{\rm st}}','l':r'{l_{\rm st}}','z':r'{z_{\rm st}}','t':r'{t_{\rm st}}'},
 'Qualify the basis for 4 dividing a and b odd. Its determinant-one coordinates, induced action, fixed lattice and even-return argument remain identical.')
letters('For $a$ odd, the line Euler row','For $4\\mid a$, the line',
 {'p':r'{p_{\rm comp}}'},'Name the selected component p_comp=4 or 5, preserving the Euler row and inverse reconstruction of its omitted coordinate.')
letters('The intersection\nmatrix $I$','Its kernel is',
 {'I':r'{I_{\rm comp}}'},'Name the component intersection matrix I_comp, preserving its entries, quadratic form and kernel; identity matrices retain I.')
p.exact('subtract\n$f(Z)\\tau$, with $f(0)=0$, $f(\\infty)=1$;',
 'subtract\n$f_{\\rm pole}(Z)\\tau$, with $f_{\\rm pole}(0)=0$, $f_{\\rm pole}(\\infty)=1$;',
 'Name the pole cutoff f_pole. Pointwise equality preserves subtraction and addition as inverse coordinate maps.',[r'f_{\rm pole}'])
p.exact('form is $Z\\mapsto u(s,y)s^c/Z$, with a nonzero unit;',
 'form is $Z\\mapsto u_{\\rm node}(s,y)s^{c_{\\rm st}}/Z$, with a nonzero unit;',
 'Name the reflection unit u_node and selected shift c_st; preserve the reciprocal inverse at the inverse-transformed point.',[r'u_{\rm node}',r'c_{\rm st}'])
p.exact('on the components is exactly $j\\mapsto c-j\\pmod k$. Affine changes\nalter $c$ and the units',
 'on the components is exactly $j\\mapsto c_{\\rm st}-j\\pmod k$. Affine changes\nalter $c_{\\rm st}$ and the units',
 'Propagate c_st in the same reflection and affine-choice statement, preserving all components and cycle lengths.',[r'c_{\rm st}'])

def conductor_lattices(t):
    t=t.replace('L(',r'\mathcal L_{\rm lat}(')
    a=t.index('The identity of $\\mathbb R^2$'); b=t.index('At $m=4$')
    t=t[:a]+math(t[a:b],{'E':r'{\mathcal E_{\rm cond}}'})+t[b:]
    return math(t,{'h':r'{h_{\rm stab}}'})
p.edit('For $d=2$ or $4$ put','All odd $n$ are covered',conductor_lattices,
 'Name mathcal L_lat, conductor torus mathcal E_cond and node stabilizer h_stab. Preserve the same lattices, covering maps, K-based inverse on the image and stabilizer powers. K remains a formal input basis matrix.',
 [r'\mathcal L_{\rm lat}',r'\mathcal E_{\rm cond}',r'h_{\rm stab}'])
letters('All odd $n$ are covered','For $m=2$, cut the base',
 {'u':r'{u_{\rm st}}','v':r'{v_{\rm st}}'},
 'Name the selected star Bezout pair u_st,v_st in its equation, g-prime word, power and alpha_0,beta_0 inverse. Every exponent is unchanged.')
p.exact('These maps retain the original meridian for the subsequent\nnormal calculation.',
 'These maps retain the original meridian for the subsequent\nnormal calculation. Let $q_{\\rm col}$ be the quotient killing\n$\\alpha$. Use the original marked lifts\n$g_{\\rm lift},\\lambda_{\\rm lift},\\ell_{\\rm lift}$, with respective\nimages $g,\\lambda,\\ell$. The specified lift\n$g^{\\prime}_{\\rm lift}=g_{\\rm lift}^{u_{\\rm st}}\\ell_{\\rm lift}^{v_{\\rm st}}$\nhas image $g\'$ under $q_{\\rm col}$.',
 'Bind the existing collapsed quotient and original marked lifts explicitly. Alpha is killed and the same selected word lifts g-prime; no group section or new relation is introduced.',
 [r'q_{\rm col}',r'g_{\rm lift}'])
p.exact("$g'\\lambda(g')^{-1}\\lambda^{-1}=\\alpha^{-1}$ from",
 "\\[\n g^{\\prime}_{\\rm lift}\\lambda_{\\rm lift}(g^{\\prime}_{\\rm lift})^{-1}\\lambda_{\\rm lift}^{-1}=\\alpha^{-1}\n\\]\nfrom",
 'Write the existing winding commutator on the specified original lifts, in a separate display. The ST3 action and odd u_st give the same alpha-inverse; its collapsed image is the identity.',
 [r'g^{\prime}_{\rm lift}',r'\lambda_{\rm lift}'])
letters('A unitary lift of the projective clutch','The lift obstruction',
 {'J':r'{\mathsf J_{\rm cl}}'},'Name the clutch mathsf J_cl, preserving every entry, conjugate-transpose inverse and endpoint sign; the skew pairing J is retained.')
p.exact('Its class is $2\\sigma+kf$; squaring gives\n$4+4k=0$',
 'Its class is $2\\sigma+k_{\\rm cond}f$; squaring gives\n$4+4k_{\\rm cond}=0$',
 'Name the conductor coefficient k_cond; its class and square retain their values while k remains the component count.',[r'k_{\rm cond}'])
def star_two(t):
    return math(t.replace(r'\sigma',r'\sigma_{\rm two}'),{'f':r'{f_{\rm two}}','h':r'{h_{\rm stab}}'})
p.edit('The oriented $S^2$ bundle therefore has odd section square.','At $m=4$ the stabilizer',star_two,
 'Name the U2 section and ruling class sigma_two,f_two; preserve the degree-r replacement, conductor relation and its inverse. Propagate h_stab to the normalized conductor bases.',[r'\sigma_{\rm two}',r'f_{\rm two}',r'h_{\rm stab}'])
def star_four(t):
    return math(t.replace(r'\sigma',r'\sigma_{\rm four}'),{'f':r'{f_{\rm four}}','h':r'{h_{\rm stab}}'})
p.edit('At $m=4$ the stabilizer','These calculations compute the cap groups.',star_four,
 'Name the U4 section and ruling class sigma_four,f_four; preserve both relation columns, torsion generator, inverse substitutions and conductor relations.',[r'\sigma_{\rm four}',r'f_{\rm four}',r'h_{\rm stab}'])
letters('To see the retraction\nexplicitly in a node chart','Scaling $X,Y$',
 {'d':r'{d_{\rm rad}}'},'Name the squared-radius difference d_rad; both retraction radii retain the same values.')
p.edit('For $m=2$, the vertical','For $m=4$, these same cover tori',
 lambda t:math(t.replace(r'\sigma',r'\sigma_{\rm two}'),{'f':r'{f_{\rm two}}'}),
 'Propagate sigma_two,f_two through the U2 boundary map and inverse, preserving all classes and coefficients.',[r'\sigma_{\rm two}',r'f_{\rm two}'])
letters('For $m=4$, these same cover tori','Let $V_*=',
 {'f':r'{f_{\rm four}}'},'Propagate f_four through the U4 diagonal map and torsion-sensitive quotient, with identical entries and orders.')

def rank_one_periods(t):
    t=t.replace('T_0','\ue004')
    t=math(t,{'w':r'{w_{\rm rk}}','l':r'{l_{\rm rk}}',
              'z':r'{z_{\rm rk}}','t':r'{t_{\rm rk}}',
              'T':r'{T_{\rm rk}}','g':r'{g_{\rm rk}}',
              'v':r'{v_{\rm rk}}','c':r'{c_{\rm rk}}','p':r'{p_{\rm rk}}'})
    return t.replace('\ue004','T_0')
p.edit(r'\emph{Additional multiplicative root quotients.}',
 r'\emph{The exterior lattice and the full normal determinant.}',rank_one_periods,
 'Name the additional-root periods w_rk,l_rk,z_rk,t_rk, return T_rk, root path g_rk, power v_rk and c_rk,p_rk coefficients. Every root/chart map, collapsed relation, inclusion, wedge and prism keeps its original values.',
 [r'w_{\rm rk}',r'T_{\rm rk}',r'g_{\rm rk}',r'v_{\rm rk}',r'c_{\rm rk}',r'p_{\rm rk}'])
p.exact('The map $(x,y)\\mapsto(x,y-h(x)\\tau)$, with $h$ zero and one at',
 'The map $(x,y)\\mapsto(x,y-h_{\\rm cut}(x)\\tau)$, with $h_{\\rm cut}$ zero and one at',
 'Name the cutoff h_cut; pointwise equality preserves subtraction and addition as inverse coordinate maps. The node stabilizer is h_stab.',[r'h_{\rm cut}'])
p.exact('The integral normalization sequence has the two degree-one\nconductor columns $(B,-E)$; its $H_1$ kernel gives the two\nnodal-loop cross tori.',
 'In the integral normalization sequence, write $B_{\\rm pole}$ for\nthe common pole-section class and $E_{\\rm dbl}$ for the double-curve\nclass. The two degree-one conductor columns are $(B_{\\rm pole},-E_{\\rm dbl})$;\nits $H_1$ kernel gives the two nodal-loop cross tori.',
 'Bind the two existing conductor-column classes as B_pole,E_dbl. The two degree-one inclusion columns retain their entries and signs; the later cap class and global graph matrix have different names.',
 [r'B_{\rm pole}',r'E_{\rm dbl}'])
letters('Choose $u,r$ with','At $m=1$ the same formulas',
 {'u':r'{u_{\rm rk,Bez}}','r':r'{r_{\rm rk,Bez}}'},
 'Name the additional-root Bezout pair u_{rk,Bez},r_{rk,Bez} throughout eta_0, both inverse equations, the inclusion, cap lifts and matrices. The determinant and all four section/kernel identities retain their exact coefficients.')

def rank_one_matrices(t):
    saved=[]
    for old,new in [(r'K_{w_{\rm rk}}',r'K_{w,\rm rk}'),
                    (r'K_{z_{\rm rk}}',r'K_{z,\rm rk}'),
                    (r'K_{t_{\rm rk}}',r'K_{t,\rm rk}'),('E_0','E_0')]:
        token='\ue010'+str(len(saved))+'\ue011'
        saved.append((token,new))
        t=t.replace(old,token)
    t=math(t,{'f':r'{f_{\rm bd}}','W':r'{W_{\rm bd}}','C':r'{C_{\rm rk}}',
              'E':r'{E_{\rm rk}}','F':r'{\mathsf F_{\rm rk}}',
              'S':r'{\mathsf S_{\rm rk}}','K':r'{\mathsf K_{\rm rk}}',
              'R':r'{\mathsf R_{\rm rk}}'})
    for token,new in saved: t=t.replace(token,new)
    return t
p.edit('Use the boundary generators','At $m=1$ the same formulas',rank_one_matrices,
 'Name the additional-root boundary f_bd,W_bd, cap C_rk,E_rk and matrices mathsf F_rk,S_rk,K_rk,R_rk. The kernel columns, section and inverse coordinates keep every entry; all four matrix identities are preserved.',
 [r'f_{\rm bd}',r'W_{\rm bd}',r'C_{\rm rk}',r'E_{\rm rk}',r'\mathsf F_{\rm rk}',r'\mathsf K_{\rm rk}'])
letters('Here $h_i=(A_i-I)^{-1}g_i$','The weight $w_i$',
 {'u':r'{u_{\rm ell}}','r':r'{r_{\rm ell}}'},
 'Name the selected vanishing period and determinant-one elliptic complement u_ell,r_ell; preserve the rank-one factorization, cocycle, logarithm and determinant.')
letters('Set $D=[T_1-I','The matrix with columns',
 {'D':r'{\mathsf D_{\rm gr}}','B':r'{\mathsf B_{\rm gr}}',
  'U':r'{\mathsf U_{\rm gr}}','V':r'{\mathsf V_{\rm gr}}'},
 'Name the graph differential, fixed-column matrix and Smith transforms mathsf D_gr,B_gr,U_gr,V_gr. Preserve the cut-graph columns, kernel, primitive relation, Hermite comparison and inverse column operations.')
letters('Choose $ax-by=1$','The image relations',
 {'x':r'{x_{\rm fib,Bez}}','y':r'{y_{\rm fib,Bez}}'},
 'Name the selected fibre Bezout coefficients x_{fib,Bez},y_{fib,Bez}; the same identity gives the same inverse representative, while the star vertical x,y classes are retained.')
letters('the generator of the fibre quotient','For example, take profile',
 {'s':r'{s_{\rm fib}}'},
 'Name the fibre-quotient generator s_fib in the global relation, root-disc boundary and determinant coordinates. Its evaluation-one representative and all relation entries are identical.')
letters('Adjoin the global relation to these columns.','Let $Q_o$',
 {'k':r'{N_{\partial}}'},
 'Name the number of boundary holes N_partial in the block presentation and degree-one ranks; preserve its value and the complete relation matrix.')
p.exact('$(m_i/q_i,0),(0,m_i),(r_i,n_i)$. If $A n_i+B m_i=1$, their\ncombination $A(r_i,n_i)+B(0,m_i)$ has second coordinate one,',
 '$(m_i/q_i,0),(0,m_i),(r_i,n_i)$. If $A_{i,\\rm Bez} n_i+B_{i,\\rm Bez} m_i=1$, their\ncombination $A_{i,\\rm Bez}(r_i,n_i)+B_{i,\\rm Bez}(0,m_i)$ has second coordinate one,',
 'Name the selected finite-column coefficients A_{i,Bez},B_{i,Bez}. Their exact column combination and inverse elimination are unchanged.',[r'A_{i,\rm Bez}',r'B_{i,\rm Bez}'])
p.exact("A B\\'ezout functional $\\lambda(v_i)+\\alpha m_i=1$ gives the",
 "A B\\'ezout functional $\\lambda_{i,\\rm Bez}(v_i)+\\alpha_{i,\\rm Bez}m_i=1$ gives the",
 'Name the selected regular-root covector and scalar lambda_{i,Bez},alpha_{i,Bez}, preserving their values, inverse coset coordinates and full lattice.',[r'\lambda_{i,\rm Bez}',r'\alpha_{i,\rm Bez}'])
p.edit('If $c_i=\\operatorname{rank}','Let $Q_o$',
 lambda t:t.replace('c_i',r'c_i^{\rm fix}'),
 'Name the fixed-lattice ranks c_i^{fix}, preserving the rank equality while peripheral generators keep their actual group names.',[r'c_i^{\rm fix}'])
letters('Let $Q_o$',r'\emph{Completion over all fillings and refinements.}',
 {'R':r'{R_{\rm ord}}'},
 'Name the product of additional-root orders R_ord in its definition, square, parity and example; all values are unchanged.')
letters('For example, take profile','The basis $(e_1+2',
 {'T':r'{T_{\rm ex}}'},
 'Name the explicit I3 return T_ex in the order-18 example, preserving all entries and its determinant-one conjugating basis.')
letters('If their number is\n$r$','An equivariant toric refinement',
 {'r':r'{r_{\rm orb}}'},
 'Name the further-cusp orbit count r_orb, preserving its value in b4 and the rational defect.')
def refinement(t):
    t=math(t,{'f':r'{f_{\rm ref}}','p':r'{p_{\rm cov}}','k':r'{k_{\rm cov}}'})
    return t.replace(r'{f_{\rm ref}}_*',r'(f_{\rm ref})_*').replace(r'\widetilde {f_{\rm ref}}',r'\widetilde f_{\rm ref}')
p.edit('An equivariant toric refinement',r'\end{proof}',refinement,
 'Name the refinement f_ref, associated connected cover p_cov and degree k_cov. Preserve the Poincare-duality right inverse, pushforward identity, lifted degree equation and all obstruction conclusions.',
 [r'f_{\rm ref}',r'p_{\rm cov}',r'k_{\rm cov}'])
p.exact('$(\\eta_0,z,t)$ above.','$(\\eta_0,z_{\\rm rk},t_{\\rm rk})$ above.',
 'Propagate the additional-root period names in its later free-abelian basis import; the three generators and inverse coordinates are unchanged.',[r'z_{\rm rk}',r't_{\rm rk}'])
p.exact('\\eqref{maps:eq:D.ST3}; every odd power has this same action on\n$\\lambda$.',
 '\\eqref{maps:eq:D.ST3}; every odd power has this same action on\n$\\lambda_{\\rm lift}$.',
 'Keep the winding sentence on the same original marked lift as its displayed commutator; the collapsed image commutes after alpha is killed.',[r'\lambda_{\rm lift}'])
p.exact('At $m=4$ the stabilizer $g^2$ fixes both branches and\n$\\alpha,\\lambda,\\ell$. Its open ruling has abelian period lattice\nwith relation $2g^2=t_0\\alpha+R\\lambda+n\\ell$.',
 'At $m=4$ the stabilizer lift $g_{\\rm lift}^2$ fixes both branches and\n$\\alpha,\\lambda_{\\rm lift},\\ell_{\\rm lift}$. Its open ruling has abelian\nperiod lattice with relation\n$2g_{\\rm lift}^2=t_0\\alpha+R\\lambda_{\\rm lift}+n\\ell_{\\rm lift}$.',
 'Use the same specified original marked lifts in the open-ruling period relation. Its abelian classes and original alpha component are retained; the subsequent conductor H1 equations take their images under the existing conductor maps.',
 [r'g_{\rm lift}',r'\lambda_{\rm lift}',r'\ell_{\rm lift}'])
p.edit('At $m=2$, choose the lift fixing a component','All odd $n$ are covered',
 lambda t:math(t,{'W':r'{W_m}'}),
 'Index the star normalizations by their input root order as W_m. Each is the same ruled normalization for that m; the pole sections and basis matrices K_{W_m} are unchanged.',[r'W_m'])
p.exact('At $m=2$, choose the lift fixing a component of the infinite chain.',
 'Write $W_m$ for the normalization at root order $m$.\nAt $m=2$, choose the lift fixing a component of the infinite chain.',
 'Explicitly bind the normalization family W_m to the existing root-order input, preserving the two actual conductor constructions.',[r'W_m'])
p.edit(r'\emph{Additional multiplicative root quotients.}',
 r'\emph{The exterior lattice and the full normal determinant.}',
 lambda t:re.sub(r'(H_[1234])\(U\)',r'\1(U_{\\rm rk})',t),
 'Name the additional-root quotient cap U_rk in all four integral homology groups. It is the same constructed quotient, with the same inclusions and normalization maps.',[r'U_{\rm rk}'])
p.edit('If their number is\n${r_{\\rm orb}}$','An equivariant toric refinement',
 lambda t:t.replace('b_4(U)',r'b_4(U_{\rm cusp})').replace('b_1(U)',r'b_1(U_{\rm cusp})'),
 'Name the further-cusp quotient U_cusp in its Betti-number calculation, preserving the same normalization and boundary maps and every rank.',[r'U_{\rm cusp}'])
p.exact('rank-two group. For finite caps the primitive relation\n$m_i g=v_i$',
 'rank-two group. For finite caps the primitive relation\n$m_i g_{i,\\rm fin}=v_i$',
 'Name the selected finite-cap root generator g_{i,fin}, preserving the primitive relation, group and Bezout inverse. The star and additional-root generators keep their different full names.',[r'g_{i,\rm fin}'])

def layout_tokens(t):
    t=re.sub(r'\\(?:begin|end)\{gathered\}','',t)
    t=t.replace(r'\\','').replace(r'\qquad','').replace(r'\quad','')
    return re.sub(r'\s+','',t)
def layout(old,new,markers):
    assert layout_tokens(old)==layout_tokens(new)
    p.exact(old,new,'Break a widened display into gathered rows. Removing only the added environment, row separators and spacing gives identical ordered mathematical tokens.',markers)
layout(r''' \alpha=2e_1+a\delta,\qquad
 \lambda=e_1+{s_{\rm per}}\delta,\qquad
 \beta=e_2+{k_{\rm per}}\lambda,\qquad
 \ell=\gamma+(b/2)e_2-{h_{\rm per}}\lambda.''',
 r''' \begin{gathered}
 \alpha=2e_1+a\delta,\qquad \lambda=e_1+{s_{\rm per}}\delta,\\
 \beta=e_2+{k_{\rm per}}\lambda,\qquad \ell=\gamma+(b/2)e_2-{h_{\rm per}}\lambda.
 \end{gathered}''',[r's_{\rm per}'])
layout(r''' {T_{\rm st}}\alpha=-\alpha,\quad {T_{\rm st}}\beta=-\beta-\lambda,\quad
 {T_{\rm st}}\lambda=\lambda-\alpha,\quad {T_{\rm st}}\ell=\ell,\\''',
 r''' {T_{\rm st}}\alpha=-\alpha,\quad {T_{\rm st}}\beta=-\beta-\lambda,\\
 {T_{\rm st}}\lambda=\lambda-\alpha,\quad {T_{\rm st}}\ell=\ell,\\''',[r'T_{\rm st}'])
layout(r''' {w_{\rm st}}=e_1+(a/2)\delta,\quad {l_{\rm st}}=((b+1)/2)e_2+\gamma,
 \quad {z_{\rm st}}=\delta,\quad {t_{\rm st}}=b e_2+2\gamma.''',
 r''' \begin{gathered}
 {w_{\rm st}}=e_1+(a/2)\delta,\quad {l_{\rm st}}=((b+1)/2)e_2+\gamma,\\
 {z_{\rm st}}=\delta,\quad {t_{\rm st}}=b e_2+2\gamma.
 \end{gathered}''',[r'w_{\rm st}'])
layout(r''' {\mathsf J_{\rm cl}}(\theta)=\begin{pmatrix}0&-e^{-\pi i\theta}\\
                       e^{\pi i\theta}&0\end{pmatrix},
 \qquad {\mathsf J_{\rm cl}}^{-1}={\mathsf J_{\rm cl}}^*,\qquad {\mathsf J_{\rm cl}}(1)=-{\mathsf J_{\rm cl}}(0).''',
 r''' \begin{gathered}
 {\mathsf J_{\rm cl}}(\theta)=\begin{pmatrix}0&-e^{-\pi i\theta}\\
                       e^{\pi i\theta}&0\end{pmatrix},\\
 {\mathsf J_{\rm cl}}^{-1}={\mathsf J_{\rm cl}}^*,\qquad {\mathsf J_{\rm cl}}(1)=-{\mathsf J_{\rm cl}}(0).
 \end{gathered}''',[r'\mathsf J_{\rm cl}'])
layout(r''' H_2(U_2)=\langle\sigma_{\rm two},{f_{\rm two}},D\mid2\sigma_{\rm two}-{f_{\rm two}}-2D=0\rangle
        =\mathbb Z\langle\sigma_{\rm two},D\rangle.''',
 r''' \begin{gathered}
 H_2(U_2)=\langle\sigma_{\rm two},{f_{\rm two}},D\mid2\sigma_{\rm two}-{f_{\rm two}}-2D=0\rangle\\
        =\mathbb Z\langle\sigma_{\rm two},D\rangle.
 \end{gathered}''',[r'\sigma_{\rm two}'])
layout(r''' (s,Z)\longmapsto
 (\zeta s,\eta s^{c_{\rm rk}} U_{\rm per}(q)^{{c_{\rm rk}}/m}V_{\rm per}(q)Z),\qquad
 \zeta=e^{2\pi i/m},\quad
 \eta^m\zeta^{{c_{\rm rk}} m(m-1)/2}=1.''',
 r''' \begin{gathered}
 (s,Z)\longmapsto
 (\zeta s,\eta s^{c_{\rm rk}} U_{\rm per}(q)^{{c_{\rm rk}}/m}V_{\rm per}(q)Z),\\
 \zeta=e^{2\pi i/m},\quad
 \eta^m\zeta^{{c_{\rm rk}} m(m-1)/2}=1.
 \end{gathered}''',[r'c_{\rm rk}'])
layout(r''' {l_{\rm rk}}=m\eta_0-{u_{\rm rk,Bez}}{p_{\rm rk}}{z_{\rm rk}}-{u_{\rm rk,Bez}}q_0{t_{\rm rk}},\qquad
 {g_{\rm rk}}={c_{\rm rk}}\eta_0+{r_{\rm rk,Bez}}{p_{\rm rk}}{z_{\rm rk}}+{r_{\rm rk,Bez}}q_0{t_{\rm rk}}.''',
 r''' \begin{gathered}
 {l_{\rm rk}}=m\eta_0-{u_{\rm rk,Bez}}{p_{\rm rk}}{z_{\rm rk}}-{u_{\rm rk,Bez}}q_0{t_{\rm rk}},\\
 {g_{\rm rk}}={c_{\rm rk}}\eta_0+{r_{\rm rk,Bez}}{p_{\rm rk}}{z_{\rm rk}}+{r_{\rm rk,Bez}}q_0{t_{\rm rk}}.
 \end{gathered}''',[r'l_{\rm rk}',r'g_{\rm rk}'])
layout(r''' {f_{\rm bd}}={w_{\rm rk}}\wedge {l_{\rm rk}},\quad A_0={l_{\rm rk}}\wedge {z_{\rm rk}},\quad B_0={l_{\rm rk}}\wedge {t_{\rm rk}},\quad
 E_0={z_{\rm rk}}\wedge {t_{\rm rk}},\quad {W_{\rm bd}}=\operatorname{sw}({w_{\rm rk}}),\quad
 Z_0=\operatorname{sw}({z_{\rm rk}}),\quad T_0=\operatorname{sw}({t_{\rm rk}}).''',
 r''' \begin{gathered}
 {f_{\rm bd}}={w_{\rm rk}}\wedge {l_{\rm rk}},\quad A_0={l_{\rm rk}}\wedge {z_{\rm rk}},\quad B_0={l_{\rm rk}}\wedge {t_{\rm rk}},\\
 E_0={z_{\rm rk}}\wedge {t_{\rm rk}},\quad {W_{\rm bd}}=\operatorname{sw}({w_{\rm rk}}),\\
 Z_0=\operatorname{sw}({z_{\rm rk}}),\quad T_0=\operatorname{sw}({t_{\rm rk}}).
 \end{gathered}''',[r'f_{\rm bd}',r'W_{\rm bd}'])
layout(r''' K_{w,\rm rk}=m{W_{\rm bd}}-{c_{\rm rk}}{f_{\rm bd}},\qquad K_{z,\rm rk}=mZ_0+{c_{\rm rk}}A_0-q_0E_0,\qquad
 K_{t,\rm rk}=mT_0+{c_{\rm rk}}B_0+{p_{\rm rk}}E_0.''',
 r''' \begin{gathered}
 K_{w,\rm rk}=m{W_{\rm bd}}-{c_{\rm rk}}{f_{\rm bd}},\\
 K_{z,\rm rk}=mZ_0+{c_{\rm rk}}A_0-q_0E_0,\\
 K_{t,\rm rk}=mT_0+{c_{\rm rk}}B_0+{p_{\rm rk}}E_0.
 \end{gathered}''',[r'K_{w,\rm rk}'])
layout(r''' {C_{\rm rk}}={r_{\rm rk,Bez}}{f_{\rm bd}}+{u_{\rm rk,Bez}}{W_{\rm bd}},\quad J_{z_{\rm rk}}={r_{\rm rk,Bez}}A_0-{u_{\rm rk,Bez}}Z_0,\quad
 J_{t_{\rm rk}}={r_{\rm rk,Bez}}B_0-{u_{\rm rk,Bez}}T_0,\quad {E_{\rm rk}}=E_0.''',
 r''' \begin{gathered}
 {C_{\rm rk}}={r_{\rm rk,Bez}}{f_{\rm bd}}+{u_{\rm rk,Bez}}{W_{\rm bd}},\quad J_{z_{\rm rk}}={r_{\rm rk,Bez}}A_0-{u_{\rm rk,Bez}}Z_0,\\
 J_{t_{\rm rk}}={r_{\rm rk,Bez}}B_0-{u_{\rm rk,Bez}}T_0,\quad {E_{\rm rk}}=E_0.
 \end{gathered}''',[r'C_{\rm rk}',r'E_{\rm rk}'])
p.exact('Then ${\\mathsf F_{\\rm rk}}{\\mathsf K_{\\rm rk}}=0$, ${\\mathsf F_{\\rm rk}}{\\mathsf S_{\\rm rk}}=I$, ${\\mathsf R_{\\rm rk}}{\\mathsf K_{\\rm rk}}=I$, and $I-{\\mathsf S_{\\rm rk}}{\\mathsf F_{\\rm rk}}={\\mathsf K_{\\rm rk}}{\\mathsf R_{\\rm rk}}$, by ${u_{\\rm rk,Bez}}{c_{\\rm rk}}+{r_{\\rm rk,Bez}}m=1$.',
 'Then\n\\[\n\\begin{gathered}\n {\\mathsf F_{\\rm rk}}{\\mathsf K_{\\rm rk}}=0,\\qquad {\\mathsf F_{\\rm rk}}{\\mathsf S_{\\rm rk}}=I,\\\\\n {\\mathsf R_{\\rm rk}}{\\mathsf K_{\\rm rk}}=I,\\qquad I-{\\mathsf S_{\\rm rk}}{\\mathsf F_{\\rm rk}}={\\mathsf K_{\\rm rk}}{\\mathsf R_{\\rm rk}},\n\\end{gathered}\n\\]\nby ${u_{\\rm rk,Bez}}{c_{\\rm rk}}+{r_{\\rm rk,Bez}}m=1$.',
 'Place the same four complete section/kernel identities on two gathered rows. Every equation and the Bezout justification are retained; only display delimiters, separators and the prose conjunction change.',
 [r'\mathsf F_{\rm rk}',r'\mathsf K_{\rm rk}',r'\mathsf R_{\rm rk}'])

p.exact('Adjoin the global relation to these columns. On ${s_{\\rm fib}}$ and all the\nfixed sweep coordinates the square matrix is',
 'Adjoin the global relation to these columns. Write $N_{\\partial}$ for\nthe total number of boundary holes. On ${s_{\\rm fib}}$ and all the fixed\nsweep coordinates the square matrix is',
 'Bind N_partial at its first presentation-matrix use as the same complete boundary-hole count. All matrix indices and the later degree-one rank statement are unchanged.',[r'N_{\partial}'])

assert '\ue000' not in p.new and '\ue010' not in p.new
assert p.new.count('T^4')==p.old.count('T^4')
assert p.new.count(r'\mathbb C')==p.old.count(r'\mathbb C')
rows=p.finish(OUT,stem)
for row in rows:
    row['change_id']=row['change_id'].replace('-02L2-','-02L2-retention-')
old='Hermite comparisons, universal $F/S/K/R$ identities and the order-$18$ example.'
new='Hermite comparisons, universal $\\mathsf F_{\\rm rk}$, $\\mathsf S_{\\rm rk}$, $\\mathsf K_{\\rm rk}$ and $\\mathsf R_{\\rm rk}$ identities, and the order-$18$ example.'
assert source.count(old)==1
row=dict(rows[0])
row.update(change_id='CLAUDE-III-P15-current02-02L2-retention-programs',
 old_location='Paper III Programs table; existing c7_l2 auxiliary row',
 old_page='candidate02 Programs table',old_text=old,new_text=new,
 reason='Propagate the four actual qualified specialization/section/kernel names into their existing Programs-table scope. The code files and asserted computation scope are unchanged; no new computation credit or link.')
rows.append(row)
full=source
for row in rows:
    assert full.count(row['old_text'])==1
    full=full.replace(row['old_text'],row['new_text'],1)
for pat in [r'\\label\{[^}]+\}',r'\\hypertarget\{[^}]+\}',r'\d+']:
    assert re.findall(pat,full)==re.findall(pat,source),pat
back=full
for row in reversed(rows):
    assert back.count(row['new_text'])==1
    back=back.replace(row['new_text'],row['old_text'],1)
assert back==source
(OUT/(stem+'.json')).write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
with (OUT/(stem+'_defects.tsv')).open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t',lineterminator='\n')
    w.writeheader();w.writerows(rows)
(OUT/(stem+'.diff')).write_text(''.join(difflib.unified_diff(
 source.splitlines(True),full.splitlines(True),fromfile='02L2 current source',
 tofile='02L2 proposed source',n=5)))
(OUT/(stem+'_proposed_scope.tex')).write_text(p.new)
print('Including the Programs import:',len(rows),'guarded fragments.')
print('Complete-source reverse and all ordered numerical literals/identifiers passed.')
print('Canonical source unchanged. Complete proposed scope and all final differences read.')
event_id='ce:c9-iii-current02-02l2-retention-reconciliation'
event=dict(statement_id='maps:src:D.2.27',date='2026-11-26',
 who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode',
 type='used and rechecked in this run',
 outcome='Read the complete current 818-line 02L2 statement/proof, every directly affected import, the complete proposed proof and every final difference. Compared 23 guarded fragments from 58 reversible operations, including the sole Programs import and first-use boundary-hole binding. Checked the original/qualified period maps, both selected generator changes and their inverse equations, explicit collapsed quotient and original marked lifts, conductor and cap relations, full F/S/K/R inverse coordinates, global coefficient maps and refinement right inverse. Ten gathered token comparisons and the remaining equation layouts preserve all mathematics. All ordered numeric literals, labels and targets and scoped/complete-source reversals passed. Explicit formal-map arguments and actual full-symbol retentions recorded; the historical local-Bezout retention is superseded. No independent proof, new computation or image credit. Admission and changed rendering pending.',
 event_id=event_id,phase='publication continuation 9',
 source_file='agents/continuation9_findings/'+stem+'_review.md',
 source_row='complete current 02L2 theorem/proof and all final differences; direct citation and Programs import review',
 source_event_type='used and rechecked in this run',evidence_group=event_id,
 publish_input_file='agents/continuation9_findings/'+stem+'_defects.tsv',
 publish_input_row='all 23 guarded fragments',
 date_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
 where='Paper III, tag02L2 / maps:src:D.2.27 and its existing Programs-table row')
with (OUT/(stem+'_CHECK_EVENTS.tsv')).open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(event),delimiter='\t',lineterminator='\n')
    w.writeheader();w.writerow(event)
print('One used-and-rechecked event written; admission and changed-PDF gate remain.')
