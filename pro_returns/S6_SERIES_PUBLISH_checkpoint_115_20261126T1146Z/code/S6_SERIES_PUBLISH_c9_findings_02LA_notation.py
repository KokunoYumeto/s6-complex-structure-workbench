#!/usr/bin/env python3
"""Complete 02LA review; prepare guarded proposals without canonical writes."""
from pathlib import Path
import re
from S6_SERIES_PUBLISH_c9_scoped_notation import ScopedReview, math_letters

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation9_findings'
source=(ROOT/'S6_SERIES_PUBLISH_III.tex').read_text()
p=ScopedReview(source,
 r'\subsection{All positive weights of the Engel construction}',
 r'\subsection{Weighted natural profiles and their integral cap maps}',
 '02LA','maps:src:D.2.34','329–337',
 'Used and rechecked after exposure. Full Q133 definition, entire 02LA statement and 559-line proof, and Q134/Q135 remarks read. Actual candidate02 pages329–337 were read in the completed assigned pass. Every changed mathematical role, map and inverse compared. Scoped and full-source reversals, all labels/targets and numeric literals verified. Existing geometric and classification evidence retained; no independent proof credit. Admission and changed rendering pending.')

p.edit(r'\begin{definition}[Positive-weight Engel data]',r'\begin{proof}',
 lambda t:t.replace('A_1',r'A_{1,\rm tor}'),
 'Name the Seifert torsion summand A_{1,tor} in its defining cokernel, theorem and homology table, retaining the explicit four-by-four monodromy A_1. Identity on the same Smith torsion coordinates identifies every group. The coefficient ring mathcal A_d, including its d=1 value, remains unchanged.',
 [r'A_{1,\rm tor}'])

p.edit('For $(v_0,v_1)$ in the graph kernel, put',
        'The first two columns are the angular cusp sweeps.',
 lambda t:math_letters(t,{'h':r'h_{\rm gr}'}),
 'Name the graph-inverse integer h_gr, preserving the later affine Lie section and meridian order. It equals the same gamma coordinate of v_1; the equations b^*(v_1)=3d h_gr, lambda=v_1-h_gr u_1 and the remaining first component retain the same values and two inverse composites.',
 [r'h_{\rm gr}'])
p.edit('In its Lie-bundle notation, the difference', 'A period change',
 lambda t:math_letters(t,{'h':r'h_{\rm aff}'}),
 'Name the affine conjugating Lie section h_aff. Its finite-operator sum is identical, (I-mathcal R)h_aff=b_0 is unchanged, and translation by its negative remains the inverse over the same whole root disc.',
 [r'h_{\rm aff}'])
p.edit('At $P=0$ its exact order is',
        'Its free quotient has rank',
 lambda t:math_letters(t,{'h':r'h_{\rm mer}'}).replace(r'\frac h_{\rm mer}',r'\frac{h_{\rm mer}}'),
 'Name the finite cusp-meridian order h_mer, preserving the graph coordinate and affine section. It is the same lcm, with the same power-disc combination, basis vector h_mer e_0, divided-sum inverse coordinate and relative section.',
 [r'h_{\rm mer}'])
p.edit('Conversely, a relation for $k(x_0+x_1)$',
        'The kernel basis is',
 lambda t:math_letters(t,{'k':r'k_{\rm mult}'}),
 'Name the tested integer multiple k_mult, preserving the input logarithmic-order parameter k. This is the same arbitrary integer in the meridian-relation test; the divisibility condition and the resulting exact order are unchanged.',
 [r'k_{\rm mult}'])

p.exact('Put $q_0=3,q_1=2$ and $e_0=3,e_1=4$.',
        r'Put $q_0=3,q_1=2$ and $e_0^{\rm ord}=3,e_1^{\rm ord}=4$.',
        'Qualify the two finite linear orders e_i^{ord}, preserving e_0,e_1 as the integral coordinate basis vectors in the relative kernels and Smith targets. The positive orders remain exactly 3 and 4 and every freeness condition is retained.',
        [r'e_0^{\rm ord}',r'e_1^{\rm ord}'])
p.edit('For $c_i=2d,3d$ respectively', 'Projection forgetting the line sends',
 lambda t:t.replace('c_i',r'\kappa_i'),
 'Name the local period coefficient kappa_i=2d,3d, retaining c_i for the finite core generator. Each coefficient has the identical value in the quotient row, raw kernel basis and all xi_d evaluations, so the original-cap boundary map and its inverse are unchanged.',
 [r'\kappa_i'])

p.edit('For reversible Smith matrices $URV=S$', 'Its determinant is',
 lambda t:math_letters(t,{'U':r'{\mathsf U}_R',
                          'V':r'{\mathsf V}_R',
                          'S':r'{\mathsf S}_R'}).replace(r'{\mathsf U}_RR',r'{\mathsf U}_R R '),
 'Name the reversible Smith matrices mathsf U_R,mathsf V_R,mathsf S_R, preserving V as the torus-bundle exterior and S as the elliptic surface. The matrices are identical, with mathsf U_R R mathsf V_R=mathsf S_R. The maps mathsf U_R^{-1} mathsf V_R^t and mathsf V_R^{-t} mathsf U_R retain the exact inverse isomorphisms between the two presentation cokernels.',
 [r'{\mathsf U}_R',r'{\mathsf V}_R',r'{\mathsf S}_R'])
p.edit('The row matrix $U$ gives the quotient',
        'At the rank-one endpoint',
 lambda t:math_letters(t,{'U':r'{\mathsf U}_K'}).replace(r'{\mathsf U}_Ky',r'{\mathsf U}_K y'),
 'Name the Euclidean row matrix for K as mathsf U_K, preserving the earlier Smith transform of R. It is the identical unimodular matrix in the displayed Smith calculation; the quotient [y] maps to [mathsf U_K y] and its inverse remain unchanged.',
 [r'{\mathsf U}_K'])
p.edit('In the coprime two-logarithm sector choose',
        'The four integers',
 lambda t:math_letters(t,{'C':r'{\mathsf C}'}),
 'Name the three block columns mathsf C_1,mathsf C_2,mathsf C_3 and their combination mathsf C prime, preserving C_j as Kodaira component cycles and C as the global cokernel. Every column entry, Bezout combination, inverse substitution, unit coordinate and target shear is identical.',
 [r'{\mathsf C}'])
p.edit(r'$\alpha w_1+\beta w_2=1$', 'The cyclic group coordinate,',
 lambda t:re.sub(r'\\(alpha|beta)(?![A-Za-z_])',
                 lambda m:'\\'+m.group(1)+r'_{\rm Bez}',t),
 'Name the endpoint Bezout integers alpha_Bez,beta_Bez, preserving beta as the component defect and alpha_i as the earlier coprime presentation coefficients. They satisfy the same unit identity and give the identical determinant-one row matrix, coordinate map and inverse.',
 [r'\alpha_{\rm Bez}',r'\beta_{\rm Bez}'])

p.edit('use the full relative sequence', r'\emph{Every finite affine filling.}',
 lambda t:math_letters(t,{'I':r'{\mathcal I}'}),
 'Name the relative component-intersection map mathcal I, preserving I for identity matrices. It reads the same relative disc coordinates; its kernel, the section Sigma_j and the statement that finite-boundary classes have zero component coordinate remain identical.',
 [r'{\mathcal I}'])

assert p.new.count(r'\mathcal A_d')==p.old.count(r'\mathcal A_d')
assert p.new.count(r'A_1&=\begin{pmatrix}')==1
assert r'c_i=2d,3d' not in p.new
p.finish(OUT,'S6_SERIES_PUBLISH_c9_current02_02LA_notation')
print('Canonical manuscript unchanged.')
