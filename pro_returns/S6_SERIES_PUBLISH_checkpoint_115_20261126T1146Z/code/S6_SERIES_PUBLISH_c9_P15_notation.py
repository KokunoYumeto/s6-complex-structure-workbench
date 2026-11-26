#!/usr/bin/env python3
"""Prepare scoped, reversible notation changes in III 02KM; no TeX writes."""
from pathlib import Path
import csv
import re
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation9_findings'
source=(ROOT/'S6_SERIES_PUBLISH_III.tex').read_text()
tag=source.index(r'\hypertarget{tag-02KM}')
start=source.rfind(r'\begin{theorem}',0,tag)
end=source.index(r'\end{proof}',tag)+len(r'\end{proof}')
proof=source[start:end]
rows=[]

def subblock(a,b):
    lo=proof.index(a);hi=proof.index(b,lo)+len(b)
    return proof[lo:hi]

def add(key,old,new,reason):
    assert old!=new
    assert proof.count(old)==1,(key,'proof',proof.count(old))
    assert source.count(old)==1,(key,'source',source.count(old))
    rows.append(dict(change_id='CLAUDE-III-P15-'+key,type='D20',statement_id='maps:src:D.2.12',old_location='Paper III, tag 02KM; '+key,old_page='cp100 pp.148–163',new_location='Paper III, tag 02KM; '+key,new_page='pending final build',old_text=old,new_text=new,reason=reason,review_status='Full original 02KM proof reread; reversible scoped notation substitution checked; canonical application pending.'))

old=subblock('For $P_j(t)=N(t)-jD(t)$, expand',r'where $|u+iv|_- =\max(|u|,|v|)$ and')
new=old.replace('For $P_j(t)=N(t)-jD(t)$, expand','Write $J=N_J/D_J$ and $P_j(t)=N_J(t)-jD_J(t)$. Expand')
new=new.replace('D(c+z)', 'D_J(c+z)')
new=re.sub(r'(?<![A-Za-z\\])k(?![A-Za-z])',lambda m:r'\nu',new)
new=new.replace('a_kz',r'a_{\nu}z').replace('d_kz',r'd_{\nu}z')
add('POLYNOMIAL',old,new,'The numerator N and denominator D of the same rational function J become N_J,D_J; the dummy Taylor index k becomes nu. Replacing these names back recovers every coefficient and inequality. The free positive logarithmic parameter k is untouched.')

old='Use the positively oriented projective period matrices $A,B$ of'
new=r'Use the positively oriented projective period matrices $A_{\rm per},B_{\rm per}$ of'
add('PERIOD-NAMES',old,new,'The two fixed projective matrices retain their referenced values under the new names A_per,B_per.')
old='using $A^3=B^2=-I$ projectively.'
new=r'using $A_{\rm per}^3=B_{\rm per}^2=-I$ projectively.'
add('PERIOD-POWERS',old,new,'These powers refer to the fixed projective matrices just named; the equality and every exponent are unchanged.')

old='$M_iH=HA_i$ for all four peripheral matrices, are'
new=r'$\mathsf M_i^{\rm ell}H=HA_i$ for all four peripheral matrices, are'
add('ELLIPTIC-MATRICES',old,new,'Only the elliptic peripheral matrices receive the separate symbol mathsf M_i^ell. Their conjugacy to the displayed A_i through H is unchanged, and the line bundle M keeps its name.')

old=subblock('exactly $c\\in(A-I)\\mathbb Z^2$. A raw $Q$ increment $kv$ means','the component by $+k$.')
new=old.replace('$kv$',r'$\kappa_{\rm loc}v$').replace('$-k$',r'$-\kappa_{\rm loc}$').replace('$+k$',r'$+\kappa_{\rm loc}$')
add('LOCAL-COMPONENT',old,new,'The arbitrary local coefficient formerly called k becomes kappa_loc, with exactly the same negative component and positive advance. The parameter m=dk is unchanged.')

old=subblock('Their full inverse decomposes any closed vector uniquely as',r'\end{array}'+'\n'+r'\]')
# This ends at the local-basis table, before the separate 5x5 matrix table.
new=old.replace('c=k g+C h.',r'c=a_G g+C h.')
new=new.replace(r'$\epsilon=\pm1$',r'$\sigma_g=\pm1$')
new=new.replace(r'k=\epsilon(UNc)_3',r'a_G=\sigma_g(UNc)_3')
new=new.replace('UN(c-kg)','UN(c-a_Gg)')
new=new.replace('$(h_1,h_2,k)$','$(h_1,h_2,a_G)$')
new=re.sub(r'B_([i1234])',lambda m:r'\mathcal U_'+m.group(1),new)
# Standalone matrix M throughout this block is exclusively the complete 5x5 section matrix.
new=re.sub(r'(?<![A-Za-z\\])M(?![A-Za-z])',lambda m:r'\mathsf M_{\rm sec}',new)
new=new.replace('$RM=',r'$R\mathsf M_{\rm sec}=')
add('COCYCLE-DECOMPOSITION',old,new,'The integer quotient coefficient is a_G, the sign of the displayed generator in the chosen quotient basis is sigma_g, the local saturated bases are mathcal U_i and the complete section matrix is mathsf M_sec. All entries, determinants, inverses and maps are retained. The reverse simultaneous replacement recovers the original block exactly.')

old=r'\text{row}&M\\\hline'+'\n'+r'1&\left(\begin{smallmatrix}0&8&3&1&-7'
new=old.replace('&M',r'&\mathsf M_{\rm sec}',1)
add('COCYCLE-MATRIX-TABLE',old,new,'The table heading adopts the same distinct section-matrix name; every numerical entry is unchanged.')

old=subblock("Mordell--Weil generator's coordinate $k$.", 'Pairing $k$ with $-k-1$ proves oddness.')
new=old.replace("Mordell--Weil generator's coordinate $k$.",r"Mordell--Weil generator's integer coordinate $\varepsilon_G$ in"+'\n'+r'$c_G=\varepsilon_Gg+Ch_G$.')
new=re.sub(r'(?<![A-Za-z\\])k(?![A-Za-z])',lambda m:r'\nu',new)
add('GENERATOR-AND-THETA',old,new,'The actual generator is explicitly decomposed as c_G=varepsilon_G g+C h_G, with integer coordinate varepsilon_G; its value ±1 is derived below. Theta uses the dummy index nu instead of k, including the paired index -nu-1. This is a bound-index bijection nu=k, separate from the free logarithmic parameter.')

old=subblock(r'For $A=\left(\begin{smallmatrix}a&b\\c_0&d\end{smallmatrix}\right)', 'inverse is literal on the line as well as on the circle.')
new=old.replace(r'c_0&d\end{smallmatrix}',r'c_0&d_A\end{smallmatrix}')
new=new.replace('$D=d-c_0\\tau$',r'$\Delta_A=d_A-c_0\tau$')
new=re.sub(r'(?<![A-Za-z\\])D(?![A-Za-z])',lambda m:r'\Delta_A',new)
new=new.replace(r'\frac zD',r'\frac z{\Delta_A}').replace(r'\frac wD',r'\frac w{\Delta_A}')
add('AUTOMORPHY',old,new,'The bottom-right matrix entry is d_A and its automorphy denominator is Delta_A=d_A-c_0 tau. Every occurrence in the holomorphic maps and their exact inverses receives the same substitution. The discriminant Delta and additive order d keep their prior meanings.')

old="Substitution of $c=kg+Ch$, $c'=lg+Cj$ gives\n$\\mathcal B(c,c')=kl/(pq)$; this is an identity in the arbitrary\ninteger variables."
new="Substitution of $c=a_Gg+Ch$, $c'=b_Gg+Cj$ gives\n$\\mathcal B(c,c')=a_Gb_G/(pq)$; this is an identity in the\narbitrary integer variables."
add('PAIRING-COORDINATES',old,new,'The two independent integer coordinates become a_G,b_G. The bilinear expression is unchanged by the bijection (k,l)->(a_G,b_G), whose inverse sends (a_G,b_G) to (k,l).')

old='sections by $D=pq$, which kills every fibre component group.'
new=r'sections by $N_{\rm comp}=pq$, which kills every fibre component group.'
add('COMPONENT-MULTIPLIER',old,new,'The same positive integer pq receives the name N_comp, keeping it distinct from the rational-function and automorphy denominators and the line-bundle degree.')
old='Both its height and $\\mathcal B$ scale by $D^2$ under multiplication\nby $D$. Dividing the narrow equality therefore gives\n$\\mathcal B(c,c)=\\langle G,G\\rangle$ with its entire integer part.'
new='Both its height and $\\mathcal B$ scale by $N_{\\rm comp}^2$ under\nmultiplication by $N_{\\rm comp}$. Dividing the narrow equality\ntherefore gives $\\mathcal B(c_G,c_G)=\\langle G,G\\rangle$ with\nits entire integer part.'
add('COMPONENT-SCALING',old,new,'The same pq-scaling argument applies to the actual section G, whose cocycle is now explicitly named c_G. The integer normalization and the square scaling factor are unchanged.')

old=subblock('Consequently $k^2=1$.', 'marking.\n\n\n\\emph{The line bundle, its linearization, and a section.}')
new=old.replace('$k^2=1$',r'$\varepsilon_G^2=1$')
new=new.replace('$c=kg+(A-I)h$',r'$c_G=\varepsilon_Gg+(A-I)h_G$')
new=new.replace('S_h', 'S_{h_G}')
new=new.replace('qh', 'qh_G').replace('ph^t', 'ph_G^t')
new=new.replace('C_k',r'C_{\varepsilon_G}').replace('kI_2',r'\varepsilon_G I_2').replace('$k=-1$',r'$\varepsilon_G=-1$')
add('GENERATOR-SIGN',old,new,'The derived sign concerns the actual generator coordinate varepsilon_G, rather than the arbitrary positive logarithmic parameter k. Its coboundary h_G and matrices S_{h_G},C_{varepsilon_G} receive the same substitution. Every matrix entry and conjugacy survives; reversing the scoped substitutions recovers the original argument.')

old=subblock('The restriction $M|_O$ has degree', 'the one in \\cite[Propositions~2.7 and~2.9, pp.~6--7]{E26}.')
new=re.sub(r'(?<![A-Za-z\\])D(?![A-Za-z])',lambda m:'d_M',old)
# TeX subscripts/exponents require braces where the old single-letter D was unbraced.
new=new.replace('t^Dv',r't^{d_M}v').replace('}DQ.',r'}d_M Q.')
add('LINE-DEGREE',old,new,'The unchanged integer degree of M restricted to O becomes d_M throughout its values, section order, forward and inverse iterates, and endpoint d_M Q. The seven integers 4,7,2,10,2,4,1 and all section maps are preserved.')

old=subblock('The graph complex has boundary $-D$, where',r'\hypertarget{tag-023H}{}\label{maps:eq:D.R1}')
new=re.sub(r'(?<![A-Za-z\\])D(?![A-Za-z.:])',lambda m:r'\partial_{\rm gr}',old)
# The existing permanent equation label contains D.R1 and is intentionally untouched.
new=new.replace('DK=0',r'\partial_{\rm gr}K=0')
add('GRAPH-BOUNDARY',old,new,'The graph boundary matrix becomes partial_gr, and its first three rows become partial_gr-prime. Its sign, columns, inverse decomposition and existing permanent label remain exactly the same.')

old=subblock('For the integral fibre quotient, order bivectors as', '$\\kappa=qe_{12}+pe_{34}$ and')
new=old.replace('$s=Ae_{12}+Be_{34}$',r'$s=a_s e_{12}+b_s e_{34}$').replace('(A,B)=','(a_s,b_s)=').replace('$pA-qB=1$', '$pa_s-qb_s=1$')
add('FIBRE-BEZOUT',old,new,'The two integer coefficients of the same primitive bivector s become a_s,b_s. The seven pairs and Bezout identity retain their exact values; this removes their encounter with the fixed projective matrices and elliptic A.')

old=subblock('Write $a$ for the pole order per root step, $\\epsilon$ for', 'c&0&0&3&0&2&3&1.\n\\end{array}\n\\]')
new=old.replace(r'\epsilon',r'\epsilon_{\rm line}')
add('LINE-WINDING',old,new,'The integral line winding receives the scoped name epsilon_line. Its seven values and relation c=d epsilon_line-a are unchanged; it is distinct from the generator sign varepsilon_G.')
old=r'x_0=t_{-\epsilon\delta}g,\qquad'
new=r'x_0=t_{-\epsilon_{\rm line}\delta}g,\qquad'
add('LINE-WINDING-MERIDIAN',old,new,'The exterior meridian uses the same line winding just renamed; the root generator and normal kernel are unchanged.')
old=subblock('For the collar\'s radial and unit terms', 'therefore exactly $d_0=t_{-v\'}x_0^m$ in the section marking.')
new=re.sub(r'(?<![A-Za-z\\])B(?![A-Za-z_])',lambda m:r'\mathcal B_{\rm col}',old)
new=new.replace(r'\epsilon\delta',r'\epsilon_{\rm line}\delta')
new=new.replace('tB(s)',r't\mathcal B_{\rm col}(s)').replace('RB(s)',r'R\mathcal B_{\rm col}(s)')
add('COLLAR-RESIDUAL',old,new,'The periodic residual function is mathcal B_col throughout the collar isotopy and its inverse; the winding uses epsilon_line. No residual function, equivariance identity, prism or attachment map is changed.')
old=r'w_{\rm sec}=w-\epsilon m\delta=\Pi v-ak\delta\in\Lambda,'
new=r'w_{\rm sec}=w-\epsilon_{\rm line}m\delta=\Pi v-ak\delta\in\Lambda,'
add('LINE-WINDING-TRANSPORT',old,new,'The same line winding is used in the transported section period; the free parameter k remains in the term ak.')

old=subblock('B=\\begin{pmatrix}n&-qR_0\\alpha\\\\0&1\\end{pmatrix}', 'preimage $((a+qR_0\\alpha b)/n,b)$ under $B$.')
new=old.replace('B=\\begin{pmatrix}',r'B_{\rm rel}=\begin{pmatrix}',1).replace('under $B$.',r'under $B_{\rm rel}$.')
add('RELATIVE-MATRIX',old,new,'The displayed reduced relative boundary matrix becomes B_rel; its entries, quotient, section and preimage formula are unchanged. This separates it from the earlier projective matrix and the bilinear pairing.')

candidate=source
for row in rows:
    assert candidate.count(row['old_text'])==1,(row['change_id'],'overlap or stale source')
    candidate=candidate.replace(row['old_text'],row['new_text'],1)
assert re.findall(r'\\label\{[^}]+\}',source)==re.findall(r'\\label\{[^}]+\}',candidate)
assert re.findall(r'\\hypertarget\{[^}]+\}',source)==re.findall(r'\\hypertarget\{[^}]+\}',candidate)
assert re.findall(r'(?<![A-Za-z])[-+]?[0-9]+',source)==re.findall(r'(?<![A-Za-z])[-+]?[0-9]+',candidate)
# Exact simultaneous alpha-renaming is verified row by row through these explicit reverse strings.
for row in reversed(rows):
    assert candidate.count(row['new_text'])==1,(row['change_id'],'nonunique inverse')
    candidate=candidate.replace(row['new_text'],row['old_text'],1)
assert candidate==source
fields=['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status']
with (OUT/'S6_SERIES_PUBLISH_c9_P15_defects.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
print('Prepared',len(rows),'scoped P15 replacements for the full 02KM proof.')
print('All original blocks are unique; labels and targets preserved; reverse guarded substitution recovers the entire canonical source byte for byte.')
print('Free logarithmic parameter k, all numerical matrices, input domains and theorem conclusions retained.')
print('Canonical TeX unchanged; no independent mathematical proof-check credit claimed.')
