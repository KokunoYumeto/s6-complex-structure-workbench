"""Prepare the 02KS receiving proof from the frozen independent derivation.

The only original text read is the individually released 02KS statement
and proof.  This program never opens a canonical manuscript.  It writes
the local receiving TeX and two exact replacement rows; root admission
and canonical application are separate operations.
"""
from pathlib import Path
import csv
import hashlib
import re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation7_iii_ks'
FRESH=OUT/'S6_SERIES_PUBLISH_III_02KS_c7_fresh_derivation.md'
assert hashlib.sha256(FRESH.read_bytes()).hexdigest()=='e44b377b7cc2ec20e4356dbea3196c71ee89581f8ef58d3ede56de5972059f0f'

def released(name,environment):
    s=(OUT/name).read_text()
    a=s.index('\\begin{'+environment+'}')
    b=s.index('\\end{'+environment+'}',a)+len('\\end{'+environment+'}')
    return s[a:b]

old_statement=released('S6_SERIES_PUBLISH_III_02KS_released_statement.tex','theorem')
old_proof=released('S6_SERIES_PUBLISH_III_02KS_released_proof.tex','proof')
assert hashlib.sha256(old_proof.encode()).hexdigest()=='1661f987fb16aa77e5e42e66202bbba0eec7b81386899a1f32b326db6141e622'

statement=r'''\begin{theorem}[Three-component cusp with original additive fillings]
\hypertarget{tag-02KS}{}\label{maps:src:D.2.18}
\textnormal{\small tag02KS.}
For OS50 profile $II$, with ordered fibres $II,I_3,I_1^*$,
take $P=12G$, $Q=G$ and the degree-one linearization whose
zero is the whole $I_3$ fibre. Use the original $II$ and $I_1^*$
fillings. At an additional regular fibre perform a free log of order
$m>0$ with vector $v=ae_1+b'e_2+c\delta+n\gamma$, where
$\gcd(m,a,b',c,n)=1$. Put
\[
 t=\gcd(m,n,a,b')\gcd(m,n,12,c),\qquad
 \mathcal G=\mathbb Z/t\oplus\mathbb Z/m\oplus\mathbb Z/(m|n|/t)
 \quad(n\ne0).
\]
For $n\ne0$ the integral homology groups are
\[
\begin{aligned}
 \pi_1(X)&=H_1(X)=\mathbb Z/|n|,&H_5(X)&=0,\\
 H_2(X)&=\mathbb Z^3\oplus\mathcal G,
 &H_3(X)&=\mathbb Z^2\oplus\mathcal G,\\
 H_4(X)&=\mathbb Z^3\oplus\mathbb Z/|n|.
\end{aligned}
\tag{D.V1}\hypertarget{tag-0269}{}\label{maps:eq:D.V1}
\]
For $n=0$, put $\mathcal T=\mathbb Z/t\oplus\mathbb Z/m$; then
\[
\begin{aligned}
 \pi_1(X)&=H_1(X)=H_5(X)=\mathbb Z,\\
 H_2(X)&=\mathbb Z^5\oplus\mathcal T,
 &H_3(X)&=\mathbb Z^4\oplus\mathcal T,\\
 H_4(X)&=\mathbb Z^5.
\end{aligned}
\tag{D.V2}\hypertarget{tag-026A}{}\label{maps:eq:D.V2}
\]
In both cases $H_0(X)=H_6(X)=\mathbb Z$ and $\chi(X)=6$.
The simply connected members are exactly those with $n=\pm1$.
Their oriented smooth type is
\[
 X\cong\operatorname{Fl}(\mathbb C^3)\#(S^2\times S^4)
       \#(S^3\times S^3)\#\widetilde\Sigma_0N_m.
\tag{D.V3}\hypertarget{tag-026B}{}\label{maps:eq:D.V3}
\]
The flag manifold has its complex orientation. The spin five-manifold
$N_m$ and the framed twisted suspension are those of
\ref{maps:src:D.2.14}; in particular $\widetilde\Sigma_0N_1=S^6$.
\end{theorem}'''

body=FRESH.read_text().split('## 1. ',1)[1]
body='## 1. '+body.split('## 11. ',1)[0]

def one(old,new):
    global body
    assert body.count(old)==1,(old,body.count(old))
    body=body.replace(old,new,1)

one('## 1. The actual periods, units, and central fibre',r'\emph{The marked periods and the central fibre.}')
one('## 2. Conductor homology and the complete cusp boundary map',r'\emph{The conductor and the cusp boundary.}')
one('## 3. The original II and I1* caps',r'\emph{The original additive fillings.}')
one('## 4. Global integral elimination, including the order-three group',r'\emph{The section frame and the global integral map.}')
one('## 5. The regular log and every integral homology group',r'\emph{The regular logarithmic filling.}')
one('## 6. The divisor cubic and the refutation of D.V3',r'\emph{The divisor cubic.}')
one('## 7. The circle quotient in the simply connected cases',r'\emph{The circle quotient.}')
one('## 8. Localizing the fixed link while preserving the free section',r'\emph{Localization of the fixed link.}')
one('## 9. The rank-two block is the flag manifold',r'\emph{The flag-manifold block.}')
one('## 10. Reconstructing the full manifold, with its suspension framing',r'\emph{Reconstruction and the suspension framing.}')

# The counterexample to the former conclusion belongs to the check record.
start=body.index('Take \\(m=1,v=\\gamma\\).')
end=body.index(r'\emph{The circle quotient.}',start)
body=body[:start]+body[end:]

one('The ordered elliptic matrices and section columns of the safe fixture are',
    r'The marked realization of \ref{mapsD:repair:collision-realization} has elliptic matrices and section columns')
one('The new multiplication verifies', 'Multiplication gives')
one('No monodromy conjugacy substitutes for the actual period marking.\n','')
one('These rules give the three matrices\nin the new output, with their full integer Smith transformations and\ninverses. Their respective nonzero Smith factors are two, five, and\nseven ones.',
    'Elementary integer row and column operations on these three\nmatrices give respectively two, five, and seven nonzero Smith\nfactors, all equal to one. Each operation is inverted by the\nopposite row or column operation.')
one('No boundary\ntorsion has been dropped. Formula (9) retains its order-three group.',
    'The boundary description includes its order-three torsion group.')
one('The logarithm and the extension of translation are the primary inputs\nspecified in the continuation-six reading record (Ulmer--Urzua,\n§2.4 and Proposition 3.5; Schuett--Shioda, §§7.5--7.6).',
    r'The logarithm follows from \cite[\S2.4, equation (2.2)]{manUU21}, and the translation extension from \cite[\S7.6, pp.~33--34]{manSS10}.')
one('Exactly as in the\nadmitted original-star construction, set', 'Set')
one('For the star the following construction is made on the KS original\nneighbourhood itself.', 'For the star, let us construct its mapping-torus model over the\noriginal neighbourhood.')
one('No identification of this analytic germ with a germ\nfrom a different OS50 configuration is needed.', '')
one('This is a change of coordinates on the same marked KS boundary:',
    'This changes coordinates on the marked boundary:')
one('Its\nagreement with the admitted KQ matrices checks the marking. The\nsmooth maps needed below are now constructed using the KS objects\n\\(N_*,M_*^{\\rm lin},\\phi_*\\) themselves.',
    r'The following maps use \(N_*,M_*^{\rm lin},\phi_*\) with this marking.')
one('The section\ncocycle \\(g_*=(0,1)\\) has residue three.',
    'The section\ncocycle \\(g_*=(0,1)\\) has residue three.')
one("Proposition 3.5(1),(3) there extends this leaf to the actual order-four\ntorsion section \\(T_*\\) of the KS surface.",
    r'By \cite[Proposition 3.5(1),(3), pp.~8--10]{manUU21}, this leaf extends to an order-four torsion section \(T_*\) of the surface.')
one('The local exact sequence (2.2) of Ulmer--Urzua §2.4, after shrinking\nthis base disc, supplies its actual Lie logarithm',
    r'The local exact sequence of \cite[\S2.4, equation (2.2)]{manUU21}, after shrinking this base disc, supplies its Lie logarithm')
one('Schuett--Shioda §§7.6--7.7 gives their translation extension on the\nentire original smooth \\(N_*\\);',
    r'By \cite[\S\S7.6--7.7, pp.~33--34]{manSS10}, these translations extend over the entire smooth \(N_*\);')
one('Thus (18e) includes the\nboundary marking and its collar, not just an abstract mapping-torus\nidentification.',
    'This fixes the boundary marking and its collar in the\nmapping-torus identification.')
one('The new verifier retains\nthese Smith maps, their inverses, the actual orbit permutation,\nthe invariant and coinvariant maps, and the sections just specified.\n','')
one('These are all original-filling maps, with no finite-quotient\nreplacement.\n','')
one('The surface realization and generator are the admitted 02OG input.',
    r'The generator has height \(1/12\) in the realization of \ref{mapsD:repair:collision-realization}.')
one('The component residues of \\(G\\) are respectively \\(0,1,3\\) in\nthe II, I3 and I1* groups.',
    r'''Label the original \(I_3\) components by Tate valuation modulo
three. Write \(\alpha(q)q^3\) for the elliptic long period and
\(\mu(q)q^4\) for the forward \(\gamma\) multiplier, where
\(\alpha,\mu\) are nonzero units. The latter covers \(-G\),
so its inverse represents \(G\). Multiplication by the square of
the long period gives the same point with coordinate
\(\alpha^2\mu^{-1}q^2\). Thus the component residues of
\(G\) are respectively \(0,2,3\) in the II, I3 and I1* groups.''')
one('Its line has\ndegree zero on every original component, the linearization has base\ndegree one, and \\(\\deg(M|_O)=6\\).',
    r'''The line \(M=\mathcal O(P-O)\) has degree zero on every
component. Its translation difference is fibrewise trivial, hence
vertical. The kernel of each component intersection matrix is generated
by the whole fibre, so its zero multidegrees make it a pullback from
the base. Its degree is the mixed height \(\langle12G,G\rangle=1\).
This gives the degree-one linearization, and \(\deg(M|_O)=6\).''')
one('This is the admitted 02KM section construction with its six literal\ninverse iterates and its component residue tracked.',
    r'These are the inverse-iteration section maps of \ref{maps:src:D.2.12}, here with six iterates and residue zero.')
one('The new exact multiplication gives', 'Multiplication gives')
one('The new Smith computation retains\ninteger matrices \\(P\\) with \\(B_2P=F\\), as well as their complete\nrow and column inverses. Together with \\(\\omega B_2=0\\) this proves',
    r'''Define a right-preimage matrix \(P\) by its five columns
\((0,\alpha_i,\beta_i)\) in the three wedge blocks, where
\[
\begin{array}{c|l|l}
i&\alpha_i&\beta_i\\\hline
1&-12e_{13}-3e_{14}-9e_{23}&e_{14}\\
2&-3e_{13}+e_{23}&0\\
3&-12e_{13}-3e_{23}+e_{24}&-e_{14}\\
4&-7e_{13}+2e_{23}&0\\
5&24e_{13}-4e_{14}-39e_{23}+2e_{24}&-e_{14}.
\end{array}
\]
Multiplication gives \(B_2P=F\). Together with
\(\omega B_2=0\), this proves''')
one('One can form \\(P\\) directly from\nthe saved Smith reduction of \\(([s,F]^{-1}B_2)_{2:6}\\): its five\nnonzero diagonal entries are units, so multiply the first five right\ncolumns by their inverse diagonal and by the left matrix. This is the\nformula used in the new program, and every identity is verified there.\n','')
one('which fixes the splitting\nwithout a hidden fibre summand.', 'which fixes the splitting.')
one('The actual collar is the admitted 02KQ holomorphic collar. Explicitly\nits isotopy and inverse in real-period coordinates are',
    r'The holomorphic collar of \ref{maps:src:D.2.16} has the following isotopy and inverse in real-period coordinates:')
one('These are actual Thom\ncoordinates, not only a presentation of the central lattice.',
    'They identify the normal line and its Thom coordinates.')
one('This recovers (27) without any unrecorded\nchange of the geometric free generators.',
    'The resulting log relation matrix fixes the geometric free generators.')
one('The full determinantal calculation is the p=12 case of the admitted\n02KQ transfer, now derived from the actual KS attachments.',
    r'This is the \(p=12\) relation matrix of \ref{maps:src:D.2.16}.')
one('The primewise pivot proof in\n02KQ applies to precisely (27):',
    r'The primewise pivot calculation in \ref{maps:src:D.2.16} applies to this matrix:')
a=body.index('The new computation verifies the polynomial signed maximal-minor')
b=body.index('In degree one the four boundary free ranks',a)
body=body[:a]+r'''The signed maximal-minor vector is \(m^2nq_0\).
For any allowed integral parameter tuple, integer Smith operations give
\(U_RRV_R=D_R\), with \(U_R,V_R\) unimodular. Applying
\(U_R\) to a target vector and reducing modulo the diagonal entries
is the quotient map; applying \(U_R^{-1}\) to coordinate
representatives is its inverse into the cokernel. The source coordinates
use \(V_R,V_R^{-1}\) and \(H_v,E_v\) on the log lattice.
Thus the diagonal calculation gives the integral maps as well as the
abstract factors.

'''+body[b:]
one('exactly as in the admitted\n02KQ construction.',r'as in \ref{maps:src:D.2.16}.')
one('This proves D.V1 and D.V2\nin their full stated scope.',
    r'These are \eqref{maps:eq:D.V1} and \eqref{maps:eq:D.V2}.')
one('Their oriented real normal bundle has the explicit scalar-circle\ntrivialization of 02KO. To recall the maps, multiply normal',
    r'The scalar-circle normal trivialization of \ref{maps:src:D.2.14} is given by the following maps. Multiply normal')
one('the original KS star', 'the original star')
one('canonical bundle formula of Schuett--Shioda Theorem 6.8 pulls',
    r'canonical bundle formula \cite[Theorem 6.8, p.~26]{manSS10} pulls')
one('KS original star quotient.', 'original star quotient.')
one("Its torsion linking form is alternating by\nBarden's Lemma F, p.372.",
    r'Its torsion linking form is alternating by \cite[Lemma F, p.~372]{manBarden65}.')
one("Barden's\nTheorems 2.2--2.3, pp.376--377, applied to these linking coordinates\nand the free coordinate in (43), give an oriented diffeomorphism",
    r'Applying \cite[Theorems 2.2--2.3, pp.~376--377]{manBarden65} to these linking coordinates and the free coordinate gives an oriented diffeomorphism')
one("The relevant embedding-isotopy theorem is\nBarden's Theorem B(b), pp.367--368, for an arbitrary ambient\nmanifold:",
    r'Theorem B(b) of \cite[pp.~367--368]{manBarden65} applies to this ambient manifold:')
one('No claim that the three spheres are unlinked enters\nthis construction. ', '')
one('Since \\(H^1(Q\\setminus\\mathring D\\times S^1)\\to\nH^1(S^4\\times S^1)\\) is an isomorphism, the relative-to-absolute\nmap identifies this kernel with the classes supported in \\(W_D\\).\nExtend the same relative cocycles by zero into the cap of (45).',
    r'''The relative groups of the two decompositions are both
\(H^2(W_D,\partial W_D)\). In each, the kernel of extension
to the closed manifold is the same image of
\(H^1(\partial W_D)\), because the outside product and the
new cap each restrict isomorphically in degree one to
\(S^4\times S^1\). Their quotient therefore identifies the
classes of \(X\) that vanish outside with \(H^2(M_L)\).
Use this quotient map to extend the same relative cocycles by zero
into the cap of \(M_L\).''')
one('The new exact symbolic solve checks all four coefficients, giving\nthe binary cubic',
    'Solving for the four coefficients gives the binary cubic')
one("For precision, apply Zhubr's spin bordism Theorem 5, p.796, and the\nzero-free-middle-homology construction and uniqueness in §4.1,\npp.809--810 (Theorem 3).",
    r'Apply the injectivity theorem \cite[Theorem 5, p.~796]{manZhubr75} and the construction and uniqueness for zero free third homology in \cite[\S4.1, p.~809]{manZhubr75}.')
one('Its uniqueness gives an orientation-preserving diffeomorphism',
    'That uniqueness gives an orientation-preserving diffeomorphism')
one('This application uses the free middle group\nin that proof; it does not rely on the inconsistent printed rank\nsubscript in the English introductory notation.\n','')
one('constructed explicitly in 02KO.',r'constructed in \ref{maps:src:D.2.14}.')
one('Those maps and their inverses are the admitted\n02KO framing comparison.',
    r'These are the framing maps and their inverses from \ref{maps:src:D.2.14}.')
one('This reconstruction preserves the entire fixed link, including its\nlinking data. The link was localized, not replaced by three unlinked\nspheres. The primitive nonzero classes of the fixed curves upstairs\nin (13) are retained throughout.',
    'The reconstruction carries the localized fixed link, its linking\nclasses and its primitive upstairs classes to their specified images.')
one('The neck construction in the admitted 02KQ proof distributes the',
    r'The neck construction in \ref{maps:src:D.2.16} distributes the')
one('The admitted product-clutching comparison\nthen gives',
    r'The product-clutching maps of \ref{maps:src:D.2.14} then give')
one('Combining (52)--(54) proves (KS.R)',
    r'Composing the flag identification, reconstruction and suspension maps proves \eqref{maps:eq:D.V3}')
one('by the explicit boundary-of-\\(D^5\\times D^2\\) map in 02KO.',
    r'by the boundary-of-\(D^5\times D^2\) map in \ref{maps:src:D.2.14}.')

# Preserve the two original proof identities on their corrected maps.
one(r'\tag{4}',r'\tag{D.V4}\hypertarget{tag-026C}{}\label{maps:eq:D.V4}')
anchor='                   \\oplus\\mathbb Z\\langle F_0,F_1\\rangle.        \\tag{14}\n\\]'
one(anchor,anchor+r'''
In particular the quotient and its inverse are
\[
 H_2(U_c)/\operatorname{im}H_2(M_c)\xrightarrow{\ \cong\ }\mathbb Z^2,
 \qquad [rF_0+sF_1]\longmapsto(r,s),
 \qquad(r,s)\longmapsto[rF_0+sF_1].
\tag{D.V5}\hypertarget{tag-026D}{}\label{maps:eq:D.V5}
\]''')
body=re.sub(r'\\tag\{\d+[a-z]?\}', '',body)

# Numbered references from the independent working proof become local names;
# the original permanent D.V identities are the only display tags retained.
ranges={
 '(15)--(16)':'the variable-roof and type-II product maps',
 '(31)--(32)':'the displayed second-homology groups',
 '(13)--(14)':'the fixed-curve matrix and cusp splitting',
 '(39)--(40)':'the normal trivialization and orbit map',
 '(42)--(43)':'the quotient kernel and its inverse coordinates',
 '(36)--(37)':'the divisor cubic identities',
 '(48)--(50)':'the primitive and flag cubic identities',
}
for old,new in ranges.items():body=body.replace(old,new)
names={
 '1':'the period matrices','2':'the cusp basis identity','3':'the period maps',
 '4':r'\eqref{maps:eq:D.V4}','5':'the six ray directions','6':'the boundary-curve classes',
 '7':'the conductor complex','8':'the cusp homology groups','9':'the boundary description',
 '10':'the normal boundary map','11':'the normal-kernel basis','12':'the fixed-curve charts',
 '13':'the fixed-curve intersection matrix','14':'the cusp splitting','15':'the variable-roof map',
 '16':'the type-II product model','17':'the type-II specialization rows','18':'the star marking identity',
 '18a':'the star component map','18b':'the translation isotopy','18c':'the variable-roof quotient',
 '18d':'the cutoff translations','18e':'the star mapping-torus model','19':'the star boundary maps',
 '20':'the graph boundary maps','21':'the graph-kernel basis','22':'the complement matrix',
 '23':'the graph inverse','24':'the fibre coinvariant isomorphism','25':'the pre-log basis',
 '26':'the logarithmic collar maps','27':'the log relation matrix','28':'the Smith factors',
 '29':'the normal matrix','30':'the filling identity','31':'the nonzero-normal homology formula',
 '32':'the zero-normal homology formula','33':'the first duality formula','34':'the second duality formula',
 '35':'the normal-line isomorphism','36':'the divisor self-intersection identity','37':'the component cubic',
 '38':'the simply connected homology groups','39':'the normal trivialization','40':'the orbit map',
 '41':'the free-circle exact sequence','42':r'\(\Theta\)','43':'the quotient homology formula',
 '44':'the quotient diffeomorphism','45':r'\(M_L\)','46':'the block homology splitting',
 '47':'the divisor basis','48':'the primitive cubic','49':'the Pontryagin pairings',
 '50':'the flag cohomology ring','51':'the characteristic-class identities','52':'the flag diffeomorphism',
 '53':'the reconstruction','54':'the suspension splitting',
}
# Protect math and citations, including (1) arguments and Proposition 3.5(1).
parts=re.split(r'(\\\[.*?\\\]|\\\(.*?\\\)|\\cite\[.*?\]\{.*?\})',body,flags=re.S)
for i in range(0,len(parts),2):
    parts[i]=re.sub(r'\((\d+[a-z]?)\)',lambda m:names[m[1]],parts[i])
body=''.join(parts)
body=body.replace('§§2--3','the local boundary computations')
body=body.replace('§4.1',r'\cite[\S4.1, p.~809]{manZhubr75}')
body=body.replace('§2','the regular-neighbourhood construction')
body=body.replace('§4 below','the section-frame construction below')
body=body.replace('§4','the section-frame construction')
body=body.replace('§8','the link-localization argument')
body=re.sub(r'\bactual\s+','',body).replace('literal ','')
body=body.replace('KS ','')

# Distinguish the section from its monodromy matrix and the original-II
# torus class from the cusp component carrying the same former subscript.
for old,new in {
    r'torsion section \(T_*\)':r'torsion section \(q_{\rm tor}\)',
    r'-G-T_*':r'-G-q_{\rm tor}',
    r't_{T_*+':r't_{q_{\rm tor}+',
    r't_{-T_*+':r't_{-q_{\rm tor}+',
    r'\tau_0=t_{T_*}':r'\tau_0=t_{q_{\rm tor}}',
    r'T(t_{-T_*}:':r'T(t_{-q_{\rm tor}}:',
    r'U_0\cong N_0':r'U_{\rm II}\cong N_0',
    r'H_2(U_0)':r'H_2(U_{\rm II})',
    r'\langle V_0,D_0\rangle':r'\langle V_0,D_{\rm II}\rangle',
    r'D_0=\delta\times\gamma':r'D_{\rm II}=\delta\times\gamma',
    r'd_0(x)D_0':r'd_0(x)D_{\rm II}',
    r'V_0=12s,D_0=-s':r'V_0=12s,D_{\rm II}=-s',
}.items():
    assert old in body,old
    body=body.replace(old,new)
body=body.replace('U_0','U_{*,0}').replace('U_1','U_{*,1}')

grammar={
 r'\phi=qU':r'\phi=q\mathcal U',
 r'with \(U\) a nowhere-zero line isomorphism.':r'with \(\mathcal U\) a nowhere-zero line isomorphism.',
 r'U_5^{-1}\cdots U_{*,0}^{-1}v':r'\mathcal U_5^{-1}\cdots\mathcal U_0^{-1}v',
 'Multiplication gives \\(T_0T_cT_*=I\\), fixes \\(\\delta\\) and\n\\(\\chi=\\gamma^*\\), and preserves':
 'The matrices satisfy \\(T_0T_cT_*=I\\), fix \\(\\delta\\) and\n\\(\\chi=\\gamma^*\\), and preserve',
 'We retain this\nlattice in the unit-triangle fan.':'The unit-triangle fan is quotiented by this lattice.',
 'Its degree-two column is the negative of the curve the boundary-curve classes\nat the source and the opposite-ray curve at the target.':
 r'Its degree-two column is \(-[C_d]_i+[C_{-d}]_{\rho((i,0)+d)}\), where \(C_d\) is the boundary curve corresponding to the ray \(d\) in the six-curve list.',
 'The complete boundary map to the kernel of the boundary description is therefore':
 r'The boundary map to \(\ker(H_1(M_c)\to H_1(U_c))\) is therefore',
 'The section-frame normalization in the section-frame construction below identifies':
 'The section-frame construction below identifies',
 'The kernel in the normal boundary map has':'The kernel of this map has',
 'the combination the normal-kernel basis of \\(F_0,F_1\\),':'the combination of \\(F_0,F_1\\) with the displayed normal-kernel coordinates,',
 'The regular-neighbourhood collapse described in the regular-neighbourhood construction\ntherefore gives':
 'The regular-neighbourhood collapse therefore gives',
 'and no\nother positive homology below its boundary dimension.':'and zero homology in every other positive degree.',
 'The regular-neighbourhood collapse in the regular-neighbourhood construction\ngives':'The regular-neighbourhood collapse gives',
 'The origin disc is fixed by the section frame in the section-frame construction.':
 'The section-frame construction below fixes the origin disc.',
 'The quotient of the star boundary maps by its boundary image':
 r'The quotient of \(H_2(U_*)\) by the boundary image',
 'At the cusp, the cusp splitting leaves':'The cusp splitting leaves',
 'These inverse additions and the split kernel\nthe normal-kernel basis prove that the pre-log basis is the full group, including its primitivity.':
 'These inverse additions and the normal-kernel splitting prove that the displayed pre-log coordinates form an integral basis.',
 'in the logarithmic collar maps, whose fibre triangle has signed area':'of the logarithmic collar, whose fibre triangle has signed area',
 'zero invariant factor of the Smith factors.':'zero Smith factor.',
 'is semi-free and has exactly the three fixed spheres the fixed-curve charts.':
 'is semi-free and has exactly the three fixed spheres described above.',
 'the continuous orbit map the orbit map proves':'the continuous orbit map proves',
 'the fixed-curve charts gives':'the fixed-curve charts give',
 'Hence \\(c_1(X)=0\\), including its integral scope, and \\(w_2(X)=0\\).':
 'Hence \\(c_1(X)=0\\) and \\(w_2(X)=0\\).',
 'The last basis in the block homology splitting follows also from the\nkernel computation the quotient kernel and its inverse coordinates.':
 'The basis of \\(H_2(M_L)\\) follows from the computed kernel of \\(\\Theta\\).',
 'The intersection matrix the fixed-curve intersection matrix gives':'The fixed-curve intersection matrix gives',
 'Substitution in the complete polynomial the component cubic, or polarization of':'Substitution in the component cubic, or polarization of',
 'The blow-up basis the boundary-curve classes gives':'The boundary-curve classes in the blow-up basis give',
 'Use the oriented map the quotient diffeomorphism, adjusted':'Use the oriented quotient diffeomorphism, adjusted',
}
for old,new in grammar.items():
    assert old in body,old
    body=body.replace(old,new)
# Display math cannot contain paragraph breaks introduced by removing tags.
body=re.sub(r'(\\\[)(.*?)(\\\])',lambda m:m[1]+re.sub(r'\n[ \t]*\n','\n',m[2])+m[3],body,flags=re.S)
body=re.sub(r'[ \t]+\n','\n',body)
body=re.sub(r'\n{3,}','\n\n',body).strip()
proof='\\begin{proof}\n'+body+'\n\\end{proof}'

old=old_statement+'\n\n'+old_proof
new=statement+'\n\n'+proof+'\n'
for pattern in [r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}',r'\\tag\{([^}]+)\}']:
    assert sorted(re.findall(pattern,old))==sorted(re.findall(pattern,new)),pattern
residue=re.search(r'\\StatementRecord|^#|```|`|S6_SERIES|\.json|\.py|405|731|97 cases|continuation|02K[OQM]|02OG|fresh|admitted|verifier',new,re.M)
assert residue is None, new[max(0,residue.start()-80):residue.end()+80] if residue else ''
assert new.count('\\begin{theorem}')==new.count('\\end{theorem}')==1
assert new.count('\\begin{proof}')==new.count('\\end{proof}')==1
assert new.count('\\[')==new.count('\\]')
assert new.count('\\(')==new.count('\\)')
path=OUT/'S6_SERIES_PUBLISH_III_02KS_receiving.tex'
path.write_text(new)
rep=OUT/'S6_SERIES_PUBLISH_III_02KS_replacements.tsv'
with rep.open('w',newline='') as f:
    writer=csv.writer(f,delimiter='\t',lineterminator='\n')
    writer.writerow(['statement_id','old_text','new_text','reason'])
    writer.writerow(['maps:src:D.2.18',old_statement,statement,'D27: retain D.V1/V2 and replace D.V3 by the proved flag-manifold classification; preserve every permanent statement identity.'])
    writer.writerow(['maps:src:D.2.18',old_proof,proof,'D25/D27: correct the period/fan transport and fixed-curve classes; replace the resulting false surgery/cancellation chain by the integral quotient, linked localization, primitive cubic, flag recognition and framed reconstruction. Preserve D.V4 and D.V5.'])
print('Frozen fresh derivation unchanged:',hashlib.sha256(FRESH.read_bytes()).hexdigest())
print('Released proof identity verified:',hashlib.sha256(old_proof.encode()).hexdigest())
print('Receiving proof:',path.relative_to(ROOT),'lines',len(new.splitlines()))
print('Permanent labels, hypertargets and tags preserved exactly.')
print('Exact guarded replacements: statement and proof separately; no canonical source read or changed.')
print('PASS: local preparation and structural assertions.')
