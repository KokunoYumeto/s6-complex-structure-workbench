#!/usr/bin/env python3
"""Complete 02L8 source reread: guarded proposals, canonical source read only."""
from pathlib import Path
import re
from S6_SERIES_PUBLISH_c9_scoped_notation import ScopedReview, math_letters

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation9_findings'
source=(ROOT/'S6_SERIES_PUBLISH_III.tex').read_text()
p=ScopedReview(source,
 r'\subsection{All original additive caps and their integral homology}',
 r'\subsection{Original multiplicative caps and the full natural catalogue}',
 '02L8','maps:src:D.2.32','315–322',
 'Used and rechecked after exposure. Full Q128 definition, 02L8 statement/proof, and Q129/Q130 remarks read; all actual candidate02 pages315–322 read earlier. Every changed role and inverse compared. Scoped and full-source reverse substitutions, labels, targets and numeric literals verified. Existing geometric/enumeration evidence retained; no independent proof credit. Admission and changed rendering pending.')

p.edit(r'\(Q=\operatorname{Exp}L\)', 'actual base translation.',
 lambda t:t.replace(r'\operatorname{Exp}L',r'\operatorname{Exp}L_{\rm log}').replace('(tL)',r'(tL_{\rm log})'),
 'Name the actual identity-component logarithm L_log, retaining L as the number of nonzero-Chern caps. The section and its scalar multiples are identical; the translation flow, horizontal lift and inverse flow are unchanged.',
 [r'L_{\rm log}'])
p.edit('For the complete boundary map put',
       'The nonzero-Chern cases and their local free ranks are',
 lambda t:re.sub(r'\\beta(?![A-Za-z_])',lambda _:r'\beta_{\rm row}',t),
 'Name the angular monodromy row beta_row, retaining beta as the total component defect and beta_0 as the primitive lift. The row has the same entries -a g^t J A; the period matrix, conjugacy, coinvariant identity and all cap maps are identical.',
 [r'\beta_{\rm row}'])

def monodromy(t):
    t=math_letters(t,{'T':r'{\mathsf T}'})
    return t.replace(r'{\mathsf T}^+', 'T^+')

p.edit('For the complete boundary map put',
       'The nonzero-Chern cases and their local free ranks are',
 monodromy,
 'Name the actual local monodromy matrix mathsf T and its three-dimensional block mathsf T_3, retaining T as the global Smith torsion group. Every entry, conjugacy R^{-1} mathsf T R, Wang relation and Smith image is unchanged. The constructor T^+(...) for a forward mapping torus is retained exactly.',
 [r'{\mathsf T}'])

def row(t):
    t=re.sub(r'\\rho(?![A-Za-z])',lambda _:r'\rho_{\rm cov}',t)
    for j in ['1','2','3']:
        t=t.replace(r'\rho_{\rm cov}_'+j,r'\rho_{{\rm cov},'+j+'}')
    return t

p.edit('The primitive coinvariant row on the first three coordinates is',
       'To identify the second coordinate geometrically',
       row,
 'Name the primitive coinvariant row rho_cov and its three entries rho_{cov,j}, retaining rho_i for the component-orbit counts in the input definition. The vector q(az_2,-az_1,1), its value on delta, its primitive section v_0 and the complete two-row fibre quotient matrix are identical.',
 [r'\rho_{\rm cov}',r'\rho_{{\rm cov},'])

p.edit('Let $\\mathbb Z^r\\oplus A_1$',r'\end{proof}',
 lambda t:t.replace('A_1',r'A_{1,\rm tor}'),
 'Qualify the Seifert abelianization torsion as A_{1,tor}, retaining A for the local elliptic monodromy. Identity on the same Smith coordinates identifies all homology-table and abelianization occurrences, with the same torsion duality and inverse coordinates.',
 [r'A_{1,\rm tor}'])

p.edit(r'\item \emph{The full degree-one bridge, including the zero-Euler case.}',
       'Choose an integral basis of this kernel',
 lambda t:t.replace('c_i',r'c_i^{\rm fix}').replace('c_j',r'c_j^{\rm fix}')
            .replace('T_i',r'{\mathsf T}_i'),
 'Name the fixed-lattice ranks c_i^{fix},c_j^{fix}, retaining c_i for the peripheral group generators. The integers and all boundary/cap ranks are unchanged. Mathsf T_i is the identical local period matrix in the fixed-lattice rank; the Mayer--Vietoris map and rank equation therefore retain the same values.',
 [r'c_i^{\rm fix}',r'c_j^{\rm fix}',r'{\mathsf T}_i'])
p.edit('normal-disc maps. The exterior', 'Choose an integral basis of this kernel',
 lambda t:math_letters(t,{'N':r'N_{\partial}'}),
 'Name the number of boundary circles N_partial, retaining N as the actual original neighbourhood. It is the identical integer count; the exterior rank, base rank N_partial-1 and every term of the bridge-rank equation are unchanged.',
 [r'N_{\partial}'])

for first,last in [
 ('Here \\(C\\) is presented by', 'All peripheral comparisons use'),
 ('For a mixed row of Theorem~\\ref{maps:src:D.2.21}',r'\end{remark}')]:
    p.edit(first,last,
      lambda t:t.replace('g_i',r'g_{i,\rm den}').replace('r_i',r'r_{i,\rm tw}'),
      'Propagate the finite denominator and twist names g_{i,den},r_{i,tw} from the reviewed Theorem 12.5 formulas into their quoted three Thom columns and the mixed-row specialization. The integers, all fractions, the power vector and inverse reads k=m_i/q_0,n=n_i,r=r_{i,tw} have exactly their original values. The raw elliptic cocycle g keeps its own name.',
      [r'g_{i,\rm den}',r'r_{i,\rm tw}'])

for text in [r'T^+(t_{-Q}:N)',r'\mathbb ZF',r'\{O,F\}']:
    assert p.new.count(text)==p.old.count(text),text
assert r'\rho_{\rm cov}_' not in p.new
p.finish(OUT,'S6_SERIES_PUBLISH_c9_current02_02L8_notation')
print('Canonical manuscript unchanged.')
