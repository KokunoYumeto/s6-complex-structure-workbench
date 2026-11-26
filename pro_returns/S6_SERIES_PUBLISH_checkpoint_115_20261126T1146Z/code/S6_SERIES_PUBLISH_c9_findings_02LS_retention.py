#!/usr/bin/env python3
"""Complete current 02LS strict-name review; prepare reversible exact guards."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import difflib
import json
import re
from S6_SERIES_PUBLISH_c9_scoped_notation import ScopedReview, math_letters

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation9_findings'
source=(ROOT/'S6_SERIES_PUBLISH_III.tex').read_text()
p=ScopedReview(source,
    r'\begin{theorem}[Vertical corrections and fillings]',
    r'\section{Invariant-Chern caps and height-integral pairs}',
    '02LS','maps:src:D.2.50','407--417; Theorem 14.9, vertical-correction unit',
    'Used and rechecked in this run after exposure. Complete current 750-line statement/proof and Definition Q202 read. Every binding, affected formula and final difference compared, including cap domains, graph-coordinate inverses and both presentation maps. Scoped/full-source reversal, all numeric literals, labels and targets checked. No independent proof or new image credit. Admission and changed rendering pending.')


def elliptic_smith(t):
    t=t.replace('D_{jj}',r'(\Delta_{\rm ell})_{jj}')
    return math_letters(t, {'U':r'{\mathsf U}_{\rm ell}',
                            'V':r'{\mathsf V}_{\rm ell}',
                            'D':r'\Delta_{\rm ell}',
                            'h':r'h_{\rm comp}'})


p.edit('orders too: in a Smith decomposition',
       r'Thus \eqref{maps:eq:D.VC6}', elliptic_smith,
       'Name the local elliptic Smith matrices mathsf U_ell,mathsf V_ell and diagonal Delta_ell, preserving D as the vertical divisor and V as the exterior. Name its computed component order h_comp, preserving the later narrow-cover integer h. Every matrix entry, nonzero diagonal value, lcm, coordinate Ug and preimage Vx remains the same. The unit matrices and their inverses identify the same lattices; h_comp g has the identical explicit preimage.',
       [r'{\mathsf U}_{\rm ell}',r'\Delta_{\rm ell}',r'h_{\rm comp}'])

p.edit(r'$A=a\kappa/d$, $B=b\kappa/n$.',
       'The ordered integral period matrix',
       lambda t:math_letters(t,{'B':r'b_{\rm rk}'}),
       'Name the derived rank-one scalar b_rk=b kappa/n, preserving B and B_i for elliptic matrices. The scalar has the same integer value in its gcd, Bezout equation, C_L and its inverse, and the outer-product factorization of N. Both determinant-one basis changes therefore have the same entries and inverses.',
       [r'b_{\rm rk}'])


def cap_maps(t,kind):
    name='H_{\\rm '+kind+'}'
    t=math_letters(t,{'H':name})
    for i in range(7):
        t=t.replace(name+'_'+str(i),'H_'+str(i))
    t=t.replace('f_1','f_1^{\\rm '+kind+'}')
    t=t.replace('f_2','f_2^{\\rm '+kind+'}')
    assert name+'_' not in t
    return t


p.edit('The ordered integral period matrix',
       r'\item \emph{The selected triangular cap and all boundary kernels.}',
       lambda t:cap_maps(t,'rk'),
       'Name the rank-one period matrix H_rk and its degree-one/two specialization maps f_1^{rk},f_2^{rk}. They have the identical ordered columns, the same map from the marked lattice to the rank-one core coordinates, the same zero-insertion sections and the same transports by H_rk and its exterior square. The conjugacy, Wang preimages, primitive kernel and all homology groups are unchanged.',
       [r'H_{\rm rk}',r'f_1^{\rm rk}',r'f_2^{\rm rk}'])
p.edit('is removed by $(z,x)\\mapsto(z,x-f(z)a_0)$',
       'This describes the actual nodal ruled normalization',
       lambda t:math_letters(t,{'f':r'f_{\rm cut}'}),
       'Name the pole cutoff f_cut, preserving f as the original elliptic fibration. It is the same function with values zero and one on the same pole collars. Subtraction of f_cut(z) a_0 and addition of that same term are the original inverse coordinate maps.',
       [r'f_{\rm cut}'])
p.edit(r'\item \emph{The selected triangular cap and all boundary kernels.}',
       'For both cap types the actual fixed circles',
       lambda t:cap_maps(t,'cusp'),
       'Name the triangular-cap matrix H_cusp and its maps f_1^{cusp},f_2^{cusp}. Their original domains and targets, four columns, two coordinate formulas, explicit sections and primitive Wang kernel are retained. H_cusp and its inverse transport the same actual fan characters and period units; no rank-one map is substituted for this cap map.',
       [r'H_{\rm cusp}',r'f_1^{\rm cusp}',r'f_2^{\rm cusp}'])
p.exact('There are no additional quotient classes: the displayed $f_2$\nhas an integral section,',
        'There are no additional quotient classes: $f_2^{\\rm rk}$ and its\n'
        'triangular-cap counterpart both have their displayed integral sections,',
        'Name both already displayed degree-two specialization maps in the common boundary-kernel paragraph. The earlier zero-insertion sections are right inverses to their respective coordinate maps. This makes the two existing domains explicit while retaining the original assertion for both cap types.',
        [r'f_2^{\rm rk}',r'f_2^{\rm cusp}'])


def graph_matrix(t):
    t=t.replace('U_D',r'{\mathsf U}_{\rm gr}').replace('V_D',r'{\mathsf V}_{\rm gr}')
    return math_letters(t,{'D':r'{\mathsf D}_{\rm gr}'})


p.edit('For the five singular matrices put',
       'The nonzero Smith factors of $R$', graph_matrix,
       'Name the graph differential mathsf D_gr and its Smith transforms mathsf U_gr,mathsf V_gr, preserving the vertical divisor D. The differential and transforms have exactly the same entries. K is the same kernel; K_0 is the same columns of V_gr and K_0^vee the same inverse rows. Both already admitted coordinate-inverse identities are preserved.',
       [r'{\mathsf D}_{\rm gr}',r'{\mathsf V}_{\rm gr}'])
p.exact(r'For $k=(u_0,\ldots,u_4)\in K$, let $B_i(u_i)$ be the',
        r'For $k=(u_0,\ldots,u_4)\in K$, let $\mathcal B_i(u_i)$ be the',
        'Name the normalized prism chain mathcal B_i(u_i), preserving B_i for its elliptic matrix. It is the same oriented prism with the same boundary, ordered polygon, self terms and central coordinate. The stated cycle splitting and subtraction inverse therefore retain the same chains.',
        [r'\mathcal B_i'])
p.edit(r'For $k=(u_0,\ldots,u_4)\in K$, let $\mathcal B_i(u_i)$ be the',
       'The inverse projects a cycle',
       lambda t:t.replace('z(k)',r'z_{\rm pr}(k)'),
       'Name the prism-section central-coordinate map z_pr(k), preserving z as the component coefficient column and as a formal coordinate in displayed bar-map domains. Its value is the same central coordinate of the identical prism/polygon chain; subtracting fibre(z_pr(k)) gives the same splitting and the same subtraction inverse.',
       [r'z_{\rm pr}'])
p.exact('The ordinary $m=1$ cap has boundary map',
        'The ordinary $m_{\\rm ord}=1$ cap has boundary map',
        'Qualify the ordinary cap order m_ord=1, preserving m as the corrected component multidegree. The positive order stays exactly one; both boundary coordinate maps, the meridian and every Thom column are unchanged.',
        [r'm_{\rm ord}'])


def presentation_smith(t):
    t=t.replace('D_B',r'\Delta_{\rm rel}')
    return math_letters(t,{'U':r'{\mathsf U}_{\rm rel}',
                            'V':r'{\mathsf V}_{\rm rel}'})


p.edit('Write $D_B=UBV$',
       'Taking the ordinary word as the first graph generator',
       presentation_smith,
       'Name the presentation Smith diagonal Delta_rel and transforms mathsf U_rel,mathsf V_rel, preserving exterior V and the preceding local Smith transforms. All entries and diagonal factors remain identical. The residue quotient, inverse image of the last coordinate and relation b U_rel^{-1}e_23=B V_rel e_23 retain the exact original maps.',
       [r'\Delta_{\rm rel}',r'{\mathsf U}_{\rm rel}',r'{\mathsf V}_{\rm rel}'])


def presentation_matrices(t):
    t=math_letters(t,{'B':r'{\mathsf B}'})
    t=t.replace(r'{\mathsf B}_o',r'{\mathsf B}_{o,\rm rel}')
    t=re.sub(r'\{\\mathsf B\}(?!_)',lambda _:r'{\mathsf B}_{\rm rel}',t)
    return t


p.edit(r'\item \emph{The exact finite presentation and its inverse coordinates.}',
       r'\end{enumerate}',presentation_matrices,
       'Name the singular-first 23-by-59 presentation mathsf B_rel and the ordinary-first 23-by-70 presentation mathsf B_{o,rel}, preserving the elliptic matrices B/B_i. Every column, ordering, Smith factor, quotient coordinate, word-change map and full H_2 presentation is the same. The two relation identities and their quotient inverses are propagated through the exact matrices.',
       [r'{\mathsf B}_{\rm rel}',r'{\mathsf B}_{o,\rm rel}'])
p.edit('relation matrices $C_r,D_r$ with',
       'the quotient maps induced by',
       lambda t:t.replace('C_r',r'{\mathsf C}_{\rm rel}').replace('D_r',r'{\mathsf D}_{\rm rel}'),
       'Name the two integral relation-transport matrices mathsf C_rel,mathsf D_rel, preserving the Dynkin lattice D_r and the component names. The matrices retain their entries in B_rel C_rel=M_Gamma B_{o,rel} and B_{o,rel} D_rel=M_Gamma^{-1}B_rel. Thus the stated quotient maps remain well defined and mutually inverse.',
       [r'{\mathsf C}_{\rm rel}',r'{\mathsf D}_{\rm rel}'])


def layout_tokens(t):
    t=re.sub(r'\\(?:begin|end)\{gathered\}', '',t)
    t=t.replace(r'\\','').replace(r'\qquad','').replace(r'\quad','')
    return re.sub(r'\s+','',t)


def layout(old,new,markers):
    assert layout_tokens(old)==layout_tokens(new)
    p.exact(old,new,
            'Break the widened display into gathered rows. Removing only the gathered environment, row separators and spacing gives the identical ordered mathematical tokens; all matrix entries, operations and maps are retained.',
            markers)


layout(r''' C_S=\begin{pmatrix}n&\sigma\\-A&\theta\end{pmatrix},
 \quad C_S^{-1}=\begin{pmatrix}\theta&-\sigma\\A&n\end{pmatrix},
 \quad C_L=\begin{pmatrix}x&-b_{\rm rk}\\y&d\end{pmatrix},
 \quad C_L^{-1}=\begin{pmatrix}d&b_{\rm rk}\\-y&x\end{pmatrix}.''',
       r''' \begin{gathered}
 C_S=\begin{pmatrix}n&\sigma\\-A&\theta\end{pmatrix},
 \quad C_S^{-1}=\begin{pmatrix}\theta&-\sigma\\A&n\end{pmatrix},\\
 C_L=\begin{pmatrix}x&-b_{\rm rk}\\y&d\end{pmatrix},
 \quad C_L^{-1}=\begin{pmatrix}d&b_{\rm rk}\\-y&x\end{pmatrix}.
 \end{gathered}''', [r'b_{\rm rk}'])

layout(r''' R=(\Lambda^2T_0-I\mid\cdots\mid\Lambda^2T_4-I),\qquad
 {\mathsf D}_{\rm gr}=(T_0-I\mid\cdots\mid T_4-I),\qquad K=\ker {\mathsf D}_{\rm gr}.''',
       r''' \begin{gathered}
 R=(\Lambda^2T_0-I\mid\cdots\mid\Lambda^2T_4-I),\\
 {\mathsf D}_{\rm gr}=(T_0-I\mid\cdots\mid T_4-I),\qquad
 K=\ker {\mathsf D}_{\rm gr}.
 \end{gathered}''', [r'{\mathsf D}_{\rm gr}'])

layout(r''' [z]\longmapsto ({\mathsf U}_{\rm rel}z)_{23}\pmod b,\qquad
 1\pmod b\longmapsto[{\mathsf U}_{\rm rel}^{-1}e_{23}].''',
       r''' \begin{gathered}
 [z]\longmapsto ({\mathsf U}_{\rm rel}z)_{23}\pmod b,\\
 1\pmod b\longmapsto[{\mathsf U}_{\rm rel}^{-1}e_{23}].
 \end{gathered}''', [r'{\mathsf U}_{\rm rel}'])


def math_with_equations(t,mapping):
    t=math_letters(t,mapping)
    def equation(m):
        inner=math_letters(r'\['+m.group(1)+r'\]',mapping)[2:-2]
        return r'\begin{equation}'+inner+r'\end{equation}'
    return re.sub(r'\\begin\{equation\}([\s\S]*?)\\end\{equation\}',equation,t)


def component_labels(t):
    fonts=re.findall(r'\\rm\s+[A-Za-z]+',t)
    for font in dict.fromkeys(fonts):
        t=t.replace(font,r'\mathrm{'+font.split()[-1]+'}')
    t=math_with_equations(t,{'p':r'p_{\rm comp}','q':r'q_{\rm comp}'})
    for letter in ['p','q']:
        t=t.replace('_'+letter+r'_{\rm comp}',r'_{'+letter+r'_{\rm comp}}')
    for font in dict.fromkeys(fonts):
        t=t.replace(r'\mathrm{'+font.split()[-1]+'}',font)
    return t


p.edit(r'\item \emph{Actual component maps and the integral equation.}',
       r'\item \emph{The twenty-one profiles and all residues.}',
       component_labels,
       'Name the component labels p_comp,q_comp, preserving the later base coordinate q and the geometric point p in formal tensor-map arguments. Each new label is exactly the previous label of the same section on the same component diagram. The indices of e_p, f_q and z_q, all component divisibility conditions and the displayed inverse Laplacian use the identity relabelling; every component entry is retained.',
       [r'p_{\rm comp}',r'q_{\rm comp}'])
p.exact('multiplicity column, and put $C=(C_iC_j)$. In particular $\\mu_0=1$.',
        'multiplicity column, and put $C=(C_iC_j)$. In particular $\\mu_0=1$.\n'
        'Write $p_{\\rm comp},q_{\\rm comp}$ for the component labels of $P,Q$.',
        'Bind the renamed component labels explicitly to the existing section-component labels; their coordinate identification and inverse are both the identity on the original marked component set.',
        [r'p_{\rm comp}',r'q_{\rm comp}'])
p.exact(r'on $I_4$ with $(p,q)=(2,2)$',
        r'on $I_4$ with $(p_{\rm comp},q_{\rm comp})=(2,2)$',
        'Propagate the identical component-label names into the concrete I_4 example, retaining its divisor, degree vector and orbit-coordinate inverse.',
        [r'p_{\rm comp}',r'q_{\rm comp}'])
p.edit('The positive-valuation Tate labels are obtained',
       'The explicit Laplacian inverse above',component_labels,
       'Propagate the same component-label names through the actual Tate reflection and the two marked pairs. The involution F, its square and the component shifts retain all entries and signs.',
       [r'p_{\rm comp}',r'q_{\rm comp}'])


def component_count(t):
    t=math_with_equations(t,{'v':r'v_{\rm comp}'})
    return t.replace(r'^v_{\rm comp}',r'^{v_{\rm comp}}')


p.edit('Let $C_0,\\ldots,C_{v-1}$',
       r'\item \emph{A rational function and the exact base line.}',
       component_count,
       'Name the number of components v_comp, preserving the later period vector v and geometric point arguments. The components are still indexed from zero to the same final index, and the ambiguity lattice has the same rank. The identity on each component basis is the forward and inverse coordinate identification.',
       [r'v_{\rm comp}'])


def base_degree(t):
    t=math_letters(t,{'t':r't_{\rm base}'})
    return t.replace(r'^t_{\rm base}',r'^t')


p.edit('coefficient is an integer. Therefore',
       r'\item \emph{Integral solutions for every component pair.}',
       base_degree,
       'Name the computed base-line degree t_base, preserving the later angular parameter t. Its integer value, base divisor t_base[infinity], line-bundle isomorphism and reciprocal inverse remain the same; t_base=<P,Q>=ab/d_0 is the original equality. Transpose superscripts t are explicitly preserved.',
       [r't_{\rm base}'])


def laplacian_differences(t):
    return re.sub(r'r_(?:\{([^}]+)\}|([A-Za-z0-9]))',
                  lambda m:r'r_{{\rm lap},'+(m.group(1) or m.group(2))+'}',t)


p.edit('Indeed, for such $h$, put',
       r'Put ${g_{\rm comp}}',laplacian_differences,
       'Name the component-Laplacian difference sequence r_{lap,i}, preserving r_i for the monodromy line row. Its initial moment, successive sums and cyclic difference equation are identical. Summing the same differences reconstructs the same component column, and subtracting its common coefficient remains the same inverse choice.',
       [r'r_{{\rm lap},'])


def smith_preimage(t):
    t=math_letters(t,{'x':r'x_{\rm ell}'})
    return t.replace(r'x_{\rm ell}_j',r'(x_{\rm ell})_j')


p.edit('An integral preimage of $h_{\\rm comp}g$',
       r'on the zero rows. Thus \eqref{maps:eq:D.VC6}',smith_preimage,
       'Name the elliptic Smith preimage vector x_ell, preserving x as the elliptic-coordinate function and later formal arguments. Its jth coordinate is the same integer h_comp(U_ell g)_j/(Delta_ell)_jj. Multiplication by the same V_ell gives precisely the original preimage of h_comp g.',
       [r'x_{\rm ell}'])


def rank_one_integers(t):
    t=math_letters(t,{'n':r'n_{\rm rk}',
                     'x':r'x_{\rm Bez}',
                     'y':r'y_{\rm Bez}'})
    return t.replace(r'\sigma',r'\sigma_{\rm Bez}')


p.edit(r'Set $d=\gcd(\nu,a\kappa)$',
       'The ordered integral period matrix',rank_one_integers,
       'Name the rank-one quotient n_rk, Bezout coordinates x_Bez,y_Bez and scalar sigma_Bez, preserving the earlier fibre index n, Smith preimage x_ell and component permutation sigma. They are the same selected integers in n_rk theta+A sigma_Bez=1 and d x_Bez+b_rk y_Bez=1. C_S,C_L, both inverse matrices and the factorization of N retain every original entry.',
       [r'n_{\rm rk}',r'x_{\rm Bez}',r'\sigma_{\rm Bez}'])


p.edit(r'At an $I_\nu$ site, write',
       'Changing $z_G$',
       lambda t:math_letters(t,{'u':r'u_{\rm per}','v':r'v_{\rm per}'}),
       'Name the marked elliptic period vectors u_per,v_per, preserving u for the tensor-comparison holomorphic unit. These are the same basis vectors with u_per^t J v_per=1; the rank-one elliptic block and logarithm z_G=(kappa/nu)v_per use the same vectors and inverse symplectic coordinates.',
       [r'u_{\rm per}',r'v_{\rm per}'])
p.exact(r' i&\nu_i&\kappa_i&u_i&v_i\\\hline',
        r' i&\nu_i&\kappa_i&u_{{\rm per},i}&v_{{\rm per},i}\\\hline',
        'Propagate the period-vector names to the five actual multiplicative data rows. All ten vectors and their orders are identical; the indexed base units u_i(q) remain unchanged.',
        [r'u_{{\rm per},i}',r'v_{{\rm per},i}'])
p.exact(r'Embed $u,v$ in the first two coordinates and put'+'\n'+r'$\mathcal S=(u,\delta)$, $\mathcal L=(v,\gamma)$.',
        r'Embed $u_{\rm per},v_{\rm per}$ in the first two coordinates and put'+'\n'+r'$\mathcal S=(u_{\rm per},\delta)$, $\mathcal L=(v_{\rm per},\gamma)$.',
        'Propagate the same period vectors into the actual short and long embeddings. Their column maps into the marked lattice, and hence both cap period matrices, are unchanged.',
        [r'u_{\rm per}',r'v_{\rm per}'])
p.edit(r'Let $v=-e\gamma$.',
       r'\item \emph{The exact finite presentation and its inverse coordinates.}',
       lambda t:math_letters(t,{'v':r'v_{\rm cl}'}),
       'Name the ordinary clutch vector v_cl=-e gamma, preserving the earlier elliptic period vectors. The boundary map subtracts tau v_cl and its inverse adds tau v_cl; the meridian, wedge terms, bar lifts and every ordinary Thom column keep the identical vector and signs.',
       [r'v_{\rm cl}'])

layout(r''' r_{{\rm lap},0}=-\frac1n\sum_{i=0}^{n-1}(n-1-i)h_i,
 \quad r_{{\rm lap},i}=r_{{\rm lap},0}+\sum_{j<i}h_j,
 \quad z_0=0,\quad z_i=\sum_{k=1}^{i}r_{{\rm lap},k}.''',
       r''' \begin{gathered}
 r_{{\rm lap},0}=-\frac1n\sum_{i=0}^{n-1}(n-1-i)h_i,
 \quad r_{{\rm lap},i}=r_{{\rm lap},0}+\sum_{j<i}h_j,\\
 z_0=0,\quad z_i=\sum_{k=1}^{i}r_{{\rm lap},k}.
 \end{gathered}''', [r'r_{{\rm lap},'])
layout(r''' (y,\tau)\longmapsto(x=y-\tau v_{\rm cl},e^{2\pi i\tau}),\qquad
 (x,\tau)\longmapsto(y=x+\tau v_{\rm cl},\tau)''',
       r''' \begin{gathered}
 (y,\tau)\longmapsto(x=y-\tau v_{\rm cl},e^{2\pi i\tau}),\\
 (x,\tau)\longmapsto(y=x+\tau v_{\rm cl},\tau)
 \end{gathered}''', [r'v_{\rm cl}'])
layout(r''' \left(c_o(u)-u\wedge v_{\rm cl},K_0^{\vee}J_o u\right)
       \quad(u=e_1,e_2,\delta,\gamma),\qquad
 \left(c_o(v_{\rm cl}),K_0^{\vee}J_o v_{\rm cl}\right).''',
       r''' \begin{gathered}
 \left(c_o(u)-u\wedge v_{\rm cl},K_0^{\vee}J_o u\right)
       \quad(u=e_1,e_2,\delta,\gamma),\\
 \left(c_o(v_{\rm cl}),K_0^{\vee}J_o v_{\rm cl}\right).
 \end{gathered}''', [r'v_{\rm cl}'])

assert p.new.count('K_0^{\\vee}')==p.old.count('K_0^{\\vee}')
assert p.new.count(r'\label{')==p.old.count(r'\label{')
for x in ['rk','cusp']:
    assert 'H_{\\rm '+x+'}_' not in p.new
assert r'\Delta_{\rm ell}_{jj}' not in p.new
rows=p.finish(OUT,'S6_SERIES_PUBLISH_c9_current02_02LS_retention')
for row in rows:
    row['change_id']=row['change_id'].replace('-02LS-','-02LS-retention-')
stem='S6_SERIES_PUBLISH_c9_current02_02LS_retention'
import_old=r'''Definition~\ref{maps:def:height-integral-data}. Its local coefficient
column $z$ is the present column $d$, and its pullback matrix
$\mathsf S$ is the present $S$. Thus the identity coordinate maps
carry \eqref{maps:eq:D.VC3} to'''
import_new=r'''Definition~\ref{maps:def:height-integral-data}. Its local coefficient
column $z$ is the present column $d$, its component label
$p_{\rm comp}$ is the present $p$, and its pullback matrix
$\mathsf S$ is the present $S$. Thus the identity coordinate maps
carry \eqref{maps:eq:D.VC3} to'''
assert source.count(import_old)==1
import_row=dict(rows[0])
import_row.update(change_id='CLAUDE-III-P15-current02-02LS-retention-import',
                  statement_id='maps:src:D.2.52',
                  old_location='Paper III, tag02LU; opening corrected-lines import from tag02LS',
                  old_page='candidate02 429; Theorem 15.4',
                  old_text=import_old,new_text=import_new,
                  reason='Propagate the explicit component-label identification into the existing corrected-line comparison. The original label p in the earlier VC3 is now p_comp; the present proof keeps p. The identity on the same marked component set sends p_comp to p, while the already stated z-to-d, mathsf S-to-S identifications and left multiplication by -I remain unchanged.',
                  review_status='Used and rechecked in this run after exposure. Read the complete opening corrected-lines comparison and its displayed equation, inverse -I and subsequent tensor maps; compared this exact import fragment. No new whole-02LU-proof, independent or image credit. Admission and changed rendering pending.')
rows.append(import_row)
full=source
for row in rows:
    assert full.count(row['old_text'])==1
    full=full.replace(row['old_text'],row['new_text'],1)
for pattern in [r'\\label\{[^}]+\}',r'\\hypertarget\{[^}]+\}',r'\d+']:
    assert re.findall(pattern,full)==re.findall(pattern,source)
for row in reversed(rows):
    assert full.count(row['new_text'])==1
    full=full.replace(row['new_text'],row['old_text'],1)
assert full==source
with (OUT/(stem+'.diff')).open('a') as f:
    f.write('\n'+''.join(difflib.unified_diff(import_old.splitlines(True),import_new.splitlines(True),fromfile='02LU import before',tofile='02LU import proposed')))
(OUT/(stem+'.json')).write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
with (OUT/(stem+'_defects.tsv')).open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t',lineterminator='\n')
    w.writeheader();w.writerows(rows)
print(len(rows),'total guarded fragments, including one explicit 02LU component-label import.')
print('Complete current 02LS unit and bounded 02LU import read; canonical manuscript unchanged.')
event_id='ce:c9-iii-current02-02ls-retention-reconciliation'
event=dict(statement_id='maps:src:D.2.50',date='2026-11-26',
           who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode',
           type='used and rechecked in this run',
           outcome='Read Definition Q202 and the complete current 750-line 02LS statement/proof, plus the bounded 02LU component-equation and tensor-map import. Compared every final difference: 32 internal reversible operations and one explicit downstream import give 22 guarded fragments. Verified the exact identity assignments, component inverse and local Smith preimage, both cap-map sections and kernels, graph K_0/K_0^vee identities, ordinary clutch inverse, presentation quotient and both relation transports. Six layout token comparisons, full-source reversal, numeric literals, labels and targets passed. No new matrix replay, independent proof or image credit. Admission and changed rendering pending.',
           event_id=event_id,phase='publication continuation 9',
           source_file='agents/continuation9_findings/'+stem+'_review.md',
           source_row='complete current 02LS statement/proof, bounded 02LU import, all final differences',
           source_event_type='used and rechecked in this run',evidence_group=event_id,
           publish_input_file='agents/continuation9_findings/'+stem+'_defects.tsv',
           publish_input_row='all 22 guarded fragments',
           date_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
           where='Paper III, tag02LS / maps:src:D.2.50; Theorem14.9 complete current proof, and tag02LU / maps:src:D.2.52 opening imported component identity')
with (OUT/(stem+'_CHECK_EVENTS.tsv')).open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(event),delimiter='\t',lineterminator='\n')
    w.writeheader();w.writerow(event)
