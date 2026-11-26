#!/usr/bin/env python3
"""Focused receiving-text corrections after the complete draft reread.

Run after the receiver preparer, before local guard freeze only.
No frozen fresh evidence or global file is written.
"""
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/'agents/continuation7_iii_all_original'

def change(s,a,b):
    assert a in s,a
    return s.replace(a,b)

p7=LANE/'S6_SERIES_PUBLISH_III_02L7_receiving.tex'
p8=LANE/'S6_SERIES_PUBLISH_III_02L8_receiving.tex'
s7=p7.read_text(); s8=p8.read_text()

edits7=[
('In the natural initial catalogue we may retain every original\nadditive cap at which $P$ is narrow, without requiring a single\ncomponent orbit.',
 'For the natural initial data of Theorem~\\ref{maps:src:D.2.22},\nretain any original additive cap at which $P$ is narrow, with\nany number of component orbits.'),
('the choices and twists of \\ref{maps:src:D.2.30}.','the choices and twists of Theorem~\\ref{maps:src:D.2.30}.'),
('original component defect. \nFor','original component defect.\n\nFor'),
('Compute the Seifert group and its Smith cokernel\n$\\mathbb Z^r\\oplus A_1$ as before,',
 'Let $\\mathbb Z^r\\oplus A_1$ be the abelianization of the Seifert\ngroup in Theorem~\\ref{maps:src:D.2.23},'),
('Let $T$ be the torsion of the matrix in \\ref{maps:src:D.2.30},',
 'Let $T$ be the torsion subgroup of the cokernel of the matrix in\nTheorem~\\ref{maps:src:D.2.30},'),
('The complete fundamental group is \\ref{maps:src:D.2.23}, including every\norder and affine twist. Thus the component defect adds free\nhomology, with no uncomputed torsion extension.',
 'The fundamental group is the presentation in\nTheorem~\\ref{maps:src:D.2.23}, for every permitted order and affine\ntwist. These homology identifications split the component\nsummands integrally.'),
('$N_M$ defined in \\ref{maps:src:D.2.14}.','$N_M$ defined in Theorem~\\ref{maps:src:D.2.14}.'),
('Iterate every positive divisor \\(a\\) of\n\\(d/\\nu\\), puts \\(b=d/(\\nu a)\\), and checks the component equation, transitivity,',
 'For each positive divisor \\(a\\) of \\(d/\\nu\\), put\n\\(b=d/(\\nu a)\\) and impose the component equation, transitivity,'),
('The same original neighbourhood, section and line.',
 'The original neighbourhood, section and line.'),
('Let \\(N\\to\\Delta\\) be the actual minimal elliptic-surface germ',
 'Let \\(N\\to\\Delta\\) be the minimal elliptic-surface germ'),
('are defined on the actual neighbourhood, including its components.\nTranslation by a section extends over the minimal surface. Thus the translation isotopy\nidentifies its actual mapping-torus roof with the torsion roof; it\ndoes not identify distinct germs from a monodromy matrix alone.',
 'are defined on this neighbourhood, including its components.\nTranslation extends over the minimal surface, and the displayed\nisotopy carries the mapping-torus roof to the torsion roof.'),
('The actual period exponential, rather than a\nmatrix alone, implements the line-frame shear:',
 'The period exponential implements the line-frame shear:'),
('All angular unit\nfunctions are retained.','Use the angular parts of all line multipliers.'),
('In particular no local\ntorsion is suppressed in \\eqref{maps:eq:D.OD4}.',
 'These coordinate maps prove that all the groups are torsion-free.'),
('\\begin{tabular}{llll}\n\\hline\nType & Component action',
 '\\begin{tabular}{lp{0.47\\textwidth}cl}\n\\hline\nType & Component action'),
('The original orientation or its inverse gives exactly the same\norbit coefficient maps.',
 'Replacing the component permutation by its inverse preserves each\norbit and its coefficient map, through the relation-generator\nidentity in part 3.'),
('These component permutations are the actual translation maps.',
 'These permutations are induced by section translation.'),
('To obtain the map in the original marking, apply the map \\(f_2\\) to',
 'In the original marking, evaluate \\(f_2\\) on'),
('The boundary Wang exact sequence has fibre quotient of rank two\nand fixed quotient the fixed-basis formula. The section the displayed section of \\(f_2\\) makes the fibre map onto',
 'The boundary Wang exact sequence has fibre quotient of rank two\nand fixed quotient \\(\\mathbb Z\\delta\\oplus\\mathbb Z\\ell\\).\nThe displayed section makes the fibre map onto'),
('ordered product identity and preserves the alternating form the definition of \\(\\omega\\).',
 'ordered product identity, and each matrix preserves \\(\\omega\\).'),
('These chains, the cut-graph map--the primitive fibre quotient, give the integral splitting',
 'These chains, the cut-graph inverse and the primitive fibre quotient\ngive the integral splitting'),
('Thus no extension in the exterior splitting is assumed to split.',
 'These forward and inverse maps establish the integral splitting.'),
('The actual fixed and coinvariant bases','The fixed and coinvariant bases'),
('The actual boundary parametrization','The boundary parametrization'),
('For clarity, a peripheral replacement', 'A peripheral replacement'),
('\\(v_i\\mapsto v_i+N_{m_i}\\lambda_i\\), not by \\(m_i\\lambda_i\\)\nunless \\(\\lambda_i\\) is invariant.',
 '\\(v_i\\mapsto v_i+N_{m_i}\\lambda_i\\). For an invariant\n\\(\\lambda_i\\), this is \\(v_i\\mapsto v_i+m_i\\lambda_i\\).'),
('primitive boundary image and the explicit component complement of\nthe definition of \\(W\\).',
 'primitive boundary image and the component complement constructed\nfrom \\(W\\) in part 4.'),
('this is an isomorphism of integral groups, not a rank reduction.',
 'these are inverse isomorphisms of integral groups.'),
('The finite columns the finite Thom columns reduce,','The finite Thom columns reduce,'),
('Modulo \\(R\\), the two Seifert relations gives','Modulo \\(R\\), the two Seifert relations give'),
('Thus the equalities \\(s=T(\\delta)=0\\)--the displayed second-homology splitting include those cases.',
 'The equalities \\(s=T(\\delta)=0\\) and the resulting\nsecond-homology splitting therefore include empty sets of sites.'),
('Crucially, the equalities \\(s=T(\\delta)=0\\) is an equality of the actual exterior class in',
 'In particular, \\(s=0\\) is an equality of the exterior class in'),
('The simply connected \\(b=1\\) matrix and the actual cusp class.',
 'The simply connected \\(b=1\\) matrix and the cusp class.'),
('Moving the given cusp fan with its actual maps.','The global comparison of cusp fans.'),
("The selected cusp is KY's specified Jordan fan.",
 'The selected cusp has the Jordan fan of\nTheorem~\\ref{maps:src:D.2.23}.'),
('At a basis \\(E=(p,q)\\), the actual period change is',
 'At a basis \\(E=(p,q)\\), the period change is'),
('is the actual flop comparison.','is the flop comparison.'),
('The comparison is a global map of these completed outputs.',''),
('Repeating the construction fixes their actual\nsection maps throughout. The composite fixes the chosen component-section spheres.',
 'Repeating the construction fixes the chosen component-section maps\nthroughout.'),
('On the resulting model the physical \\(\\delta\\)-circle acts',
 'Use this oriented global diffeomorphism for the remainder of the\nproof, preserving the component sections. On the resulting\ncompleted model the physical \\(\\delta\\)-circle acts'),
('The free basis in the displayed second-homology splitting consists of the actual component-section',
 'The free basis of \\(H_2(X)\\) consists of the component-section'),
('The component complement in the definition of \\(W\\) is represented by actual central',
 'The component complement constructed from \\(W\\) is represented by central'),
('the primitive free basis of the quotient homology and with Euler value zero.',
 'a primitive free basis of \\(H_2(Q)\\), with Euler value zero.'),
('this actual sphere into a small five-disc','this sphere into a small five-disc'),
('This proves the required global bundle','This constructs the global bundle'),
('The parametrized-disc adjustment used in the maps in Theorem~\\ref{maps:src:D.2.16}',
 'The parametrized-disc adjustment of Theorem~\\ref{maps:src:D.2.16}'),
('Combining them with the suspension comparison--the linking coordinates gives exactly',
 'Combining the suspension and linking-coordinate maps gives'),
]
for a,b in edits7:s7=change(s7,a,b)

# Include the complete local homology under its retained display identity.
s7=change(s7,r' \quad D_B=\delta\times\gamma_B.                            \tag{D.OD4}',
 r' \quad D_B=\delta\times\gamma_B,'+'\n'+r' \quad H_3(U)=\mathbb Z^{2\rho},\quad H_4(U)=\mathbb Z^\rho.'+'\n'+r' \tag{D.OD4}')
s7=change(s7,'The higher groups are \\(H_3(U)=\\mathbb Z^{2\\rho}\\) and\n\\(H_4(U)=\\mathbb Z^\\rho\\). The maps','The maps')

folded=r'''
The component-intersection description gives the same primitive
image. Let \(Q_K\) be the Kodaira intersection matrix, let
\(I\) send each orbit to the sum of its components, and let
\(R_0\) choose one representative of each orbit. Intersecting
with the orbit tubes identifies the component part of
\(H_2(U)\to H_2(U,\partial U)=H^4(U)\) with
\(I^tQ_KR_0\). Its columns are independent of the chosen
representatives because section translation preserves \(Q_K\).
In the orbit orders above the nonzero folded matrices are
\[
 \begin{array}{c|c}
 III^*&\begin{pmatrix}
 -2&1&0&0&0\\1&-2&1&0&0\\0&1&-2&2&0\\
 0&0&1&-2&1\\0&0&0&1&-2
 \end{pmatrix}\\[3pt]
 IV^*&\begin{pmatrix}-2&1&0\\1&-2&3\\0&1&-2\end{pmatrix}\\[3pt]
 I_3^*&\begin{pmatrix}-2&2&0\\1&-2&1\\0&1&-1\end{pmatrix}\\[3pt]
 I_1^*&\begin{pmatrix}-2&2\\1&-1\end{pmatrix}.
 \end{array}
\]
They kill the corresponding vector \(W\). Their leading
\((\rho-1)\)-minors are \(2,3,3,-2\), so their rank is
\(\rho-1\); the II, III and IV matrices are zero of size one.
The additional class \(D_B\) is in the boundary image and maps
to zero in the relative group. This also proves the rank of
the entire intersection map. Its image is free because the
relative target is free, in agreement with
\eqref{maps:eq:D.OD5}.

At an unselected multiplicative site, the component equations
for \(P\) narrow give \(\gcd(b\kappa_i,\nu_i)=1\) on each
natural row. Thus \(Q\) acts transitively. The pair
\((u_i,\delta)\) is primitive because \(u_i\) is primitive in
the elliptic plane; a Bezout complement to \(u_i\), followed
by \(\gamma\), extends it to an integral basis. Consequently
its original zero-Chern alternative has the same primitive
one-orbit filling maps in Theorem~\ref{maps:src:D.2.26}.
The natural factor-pair enumeration gives 316 such multiplicative
occurrences and 80 additive occurrences, hence 396 unselected
zero-Chern original occurrences in total.

'''
s7=change(s7,r'\item \emph{The integral exterior on all natural rows.}',folded+r'\item \emph{The integral exterior on all natural rows.}')

fanexample=r'''
For example, the OS47 default row with the \(I_2\) zero and
\((a,b)=(7,1)\) has \(\kappa=1\) and
\[
 C=\begin{pmatrix}2&1\\-7&-3\end{pmatrix},\qquad
 C^{-1}\delta=(-1,2).
\]
Along the first Jordan edge, the first circle collapses and
the scalar action on the remaining angular coordinate is
\(z\mapsto z^2\); its stabilizer is \(\{1,-1\}\).
We therefore make the following global fan comparison before
using a semifree scalar action.

'''
s7=change(s7,'Euclidean reduction of the first row of \\(C\\)',fanexample+'Euclidean reduction of the first row of \\(C\\)')

# Distinguish the five-dimensional quotient from the section Q=bG.
start=s7.index(r'\item \emph{The angular quotient')
tail=s7[start:]
tail=re.sub(r'(?<![A-Za-z\\])Q(?![A-Za-z])',r'\\mathcal Q',tail)
tail=tail.replace('TQ_0',r'T\mathcal Q_0')
tail=tail.replace(r'\(P\) narrow and \(\mathcal Q\) transitive',r'\(P\) narrow and \(Q\) transitive')
tail=tail.replace(r'C_\mathcal Q',r'C_{\mathcal Q}').replace(r'F_\mathcal Q',r'F_{\mathcal Q}')
s7=s7[:start]+tail

edits8=[
('Every original additive cap on the $172$ natural initial\nrows can now be included.',
 'Every original additive cap on the $172$ natural initial rows\nof Theorem~\\ref{maps:src:D.2.22} is allowed.'),
('Keep the preceding marked Mumford models at multiplicative\nsites, with the zero-degree original alternatives already\nproved.',
 'Use the marked Mumford models at multiplicative sites, together\nwith the zero-Chern original alternatives in\nTheorem~\\ref{maps:src:D.2.31}.'),
('Take $T$ from the exact Smith matrix of \\ref{maps:src:D.2.30}, adding',
 'Let $T$ be the torsion subgroup of the cokernel of the matrix in\nTheorem~\\ref{maps:src:D.2.30}, adding'),
('Take $\\mathbb Z^r\\oplus A_1$ from the same complete Seifert\nmatrix, with the actual finite and regular numerators.',
 'Let $\\mathbb Z^r\\oplus A_1$ be the abelianization of the\nSeifert group in Theorem~\\ref{maps:src:D.2.23}, with its finite\nand regular numerators.'),
('When $L=0$ the answer is \\ref{maps:src:D.2.31}.','When $L=0$ the homology is given by Theorem~\\ref{maps:src:D.2.31}.'),
('fundamental group is still \\ref{maps:src:D.2.23}. In particular the extra\ndegree-one Mayer--Vietoris kernel has been retained, including\nwhen the rational Seifert Euler number is zero.',
 'fundamental group is the presentation in Theorem~\\ref{maps:src:D.2.23}.\nThe degree-one Mayer--Vietoris kernel has rank $L+r$, including\nthe case of zero rational Seifert Euler number.'),
('The original nonzero-Chern neighbourhood and actual roof map.',
 'The nonzero-Chern original neighbourhood and its roof.'),
('the raw\ngenerator has order','the marked\ngenerator has order'),
('The line bundle keeps the nonzero Chern class the Chern vector.',
 'The line bundle keeps the Chern class \\(C_p^*-C_0^*\\).'),
('evaluation the Chern vector on','evaluation of this Chern vector on'),
('Formula the product description now gives','The product description now gives'),
('Every group in the circle-bundle homology--\\eqref{maps:eq:D.OC4} is integral and torsion-free.',
 'These maps identify every group integrally and prove that it is\ntorsion-free.'),
('in the circle-bundle homology--\\eqref{maps:eq:D.OC4}.',
 'given by the circle-bundle projection in part 2.'),
('All remaining target coordinates are the free components the component-basis inverse.',
 'The remaining coordinates are the free component classes with\nthe inverse constructed above.'),
('Formula\nthe full boundary-kernel formula supplies','This formula supplies'),
('the primitive \\(s\\) of the definition of \\(\\omega\\).',
 'the primitive class \\(s\\), with fibre functional \\(\\omega\\).'),
('Thus the degree-two cokernel splitting--the global relation retain the full marked affine scope, not only\none chosen normal form.',
 'The cokernel splitting and the global relation therefore hold\nfor every marked affine lift.'),
('with cokernel the degree-two cokernel splitting.',
 'with cokernel \\(C\\oplus\\mathbb Z^\\beta\\).'),
('the explicit elimination map of the degree-two cokernel splitting.',
 'the cap-elimination map of part 6.'),
('For a concrete zero-Euler check,','For example, at zero rational Euler number,'),
('This example is a direct\nsubstitution into the complete maps, and illustrates the\nparameter case covered in the proof.',
 'This follows by substitution into the integral cap and bridge maps.'),
]
for a,b in edits8:s8=change(s8,a,b)

# Keep the retained D.OC identities in their original display order.
g0=s8.index('The kernel of the area row on the original six-dimensional wedge')
g1=s8.index(r'\item \emph{The full normal and fibre kernel.}',g0)
gcd_block=s8[g0:g1]
s8=s8[:g0]+s8[g1:]
s8=change(s8,r'\tag{D.OC6}\hypertarget{tag-0210}{}\label{maps:eq:D.OC6}','')
s8=change(s8,'and its complete cokernel is '+r'\eqref{maps:eq:D.OC6}.'+' These are integral direct',r'''Its complete cokernel is
\[
 H_2(U)/\operatorname{im}H_2(\partial U)
       =\ker c/\mathbb ZF=\mathbb Z^{s_i-2}.
 \tag{D.OC6}\hypertarget{tag-0210}{}\label{maps:eq:D.OC6}
\]
These are integral direct''')
s8=change(s8,'The nonzero-Chern cases and their local free ranks are',gcd_block+'The nonzero-Chern cases and their local free ranks are')

s7=change(s7,r''' H_1(U)=\mathbb Z\langle\delta,\gamma_B\rangle,
 \quad H_2(U)=\mathbb Z^\rho\langle U_j\rangle
                    \oplus\mathbb Z\langle D_B\rangle,
 \quad D_B=\delta\times\gamma_B,
 \quad H_3(U)=\mathbb Z^{2\rho},\quad H_4(U)=\mathbb Z^\rho.''',r''' \begin{aligned}
 H_1(U)&=\mathbb Z\langle\delta,\gamma_B\rangle,\\
 H_2(U)&=\mathbb Z^\rho\langle U_j\rangle
                    \oplus\mathbb Z\langle D_B\rangle,
 \qquad D_B=\delta\times\gamma_B,\\
 H_3(U)&=\mathbb Z^{2\rho},\qquad H_4(U)=\mathbb Z^\rho.
 \end{aligned}''')
s7=change(s7,r''' \operatorname{im}(H_2(\partial U)\to H_2(U))
     =\mathbb ZW\oplus\mathbb ZD_B,\qquad
 H_2(U)/\operatorname{im}H_2(\partial U)=\mathbb Z^{\rho-1}.''',r''' \begin{gathered}
 \operatorname{im}(H_2(\partial U)\to H_2(U))
     =\mathbb ZW\oplus\mathbb ZD_B,\\
 H_2(U)/\operatorname{im}H_2(\partial U)=\mathbb Z^{\rho-1}.
 \end{gathered}''')

# Eliminate proof copies of the complete homology tables, retaining the
# statements and their permanent equation identities.
for which,s,eq in [(7,s7,'D.OD2'),(8,s8,'D.OC3')]:
    proof=s.index(r'\begin{proof}')
    pat=r'\\\[\s*\\begin\{array\}\{c\|c\}\s*j&H_j\(X;\\mathbb Z\)[\s\S]*?\\end\{array\}\s*\\\]'
    tail=s[proof:]
    matches=list(re.finditer(pat,tail))
    assert len(matches)==1,(which,len(matches))
    tail=tail[:matches[0].start()]+r'\eqref{maps:eq:'+eq+r'}.'+tail[matches[0].end():]
    s=s[:proof]+tail
    if which==7:s7=s
    else:s8=s

for path,s in [(p7,s7),(p8,s8)]:
    # Whitespace and accents are presentation changes only.
    s=s.replace('Bezout',r"B\'ezout").replace('Poincare',r"Poincar\'e")
    s='\n'.join(x.rstrip() for x in s.splitlines())+'\n'
    s=re.sub(r'\\\[([\s\S]*?)\\\]',lambda m:r'\['+'\n'+'\n'.join(x for x in m.group(1).splitlines() if x.strip())+'\n'+r'\]',s)
    path.write_text(s)
    print(path.name,len(s.splitlines()),'lines')
print('Corrected receiver prose, reference conversion and finite mathematical additions; frozen files unchanged.')
