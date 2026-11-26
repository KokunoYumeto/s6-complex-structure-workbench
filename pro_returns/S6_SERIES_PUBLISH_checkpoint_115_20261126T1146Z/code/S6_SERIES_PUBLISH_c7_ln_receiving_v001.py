#!/usr/bin/env python3
"""Assemble one LN receiving proof from frozen mathematics and exact identities.
No canonical source, frozen fresh file, or global register is written.
"""
from pathlib import Path
from hashlib import sha256
import re
ROOT=Path.cwd()
LANE=ROOT/'agents/continuation7_iii_general_initial_receiving'
FRESH=ROOT/'agents/continuation7_iii_general_initial/S6_SERIES_PUBLISH_III_02LN_fresh_derivation.md'
assert sha256(FRESH.read_bytes()).hexdigest()=='5ec1801a4ab89089407ce1c069bdeb64e4ca3f14c5e3c6bdb36996cea8417ce3'
released=(LANE/'S6_SERIES_PUBLISH_III_02LN_released_statement.tex').read_text()
statement=released[released.index('\\begin{theorem}'):]
statement=re.sub(r'^\\StatementRecord[^\n]*\n','',statement,flags=re.M)
statement=statement.replace('\\label{maps:src:D.2.46}\n','\\label{maps:src:D.2.46}\n\\textup{\\scriptsize[02LN]}\n',1)
statement=statement.replace('Its implementation is\n\\path{code/III/manifolds_general_initial.py}; no bound on\n$a,b,w_i$, logarithmic orders or affine numerators occurs in the\nalgorithm or proof.','The algorithm below applies to every finite input list and all\nintegers $a,b,w_i$, logarithmic orders and affine numerators satisfying\nthe stated conditions.')
statement=statement.replace('Arbitrary regular logarithms and an arbitrary ordinary clutching\ninteger are allowed.','Arbitrary regular logarithms at additional weight-zero regular sites\nand an arbitrary ordinary clutching integer are allowed.')
statement=statement.replace('zero-free multiplicative fibre','weight-zero multiplicative fibre')
body=FRESH.read_text().split('## 1. The actual line and the marked return\n\n',1)[1]
body='\\smallskip\\noindent\\emph{The line and its marked return.}\n'+body
body=re.sub(r'^## \d+\. (.+)$',lambda m:'\\smallskip\\noindent\\emph{'+m.group(1)+'.}',body,flags=re.M)
# Remove only fresh local display numbers; original permanent numbers are added below.
body=re.sub(r'\s*\\tag\{\d+\.\d+\}', '', body)
body=body.replace('The admitted geometric input includes\nthe ordered elliptic matrices \\(B_i\\), the generator cocycle \\(g_i\\),\nand the component markings.',r'The marked data of \ref{maps:src:D.2.19} give the ordered elliptic matrices \(B_i\), the generator cocycle \(g_i\), and the component markings.')
body=body.replace('The admitted height map gives',r'The height formula \cite[Section 11.8]{manSS10} gives')
body=body.replace('The Poincare period map of the admitted local\nconstruction gives',r'The Poincar\'e period map in \ref{maps:src:D.2.22} gives')
body=body.replace('The new markings program verifies this polynomial identity and\nprints every profile\'s expression. It can also be obtained from\nthe base line (1.1): its degree is precisely the remaining line\nwinding.', 'It follows geometrically from the base-line map above: its degree\nis precisely the remaining line winding. Direct multiplication of\nthe recorded matrices gives the same bilinear identity in each of\nthe 21 profiles.')
body=body.replace('the admitted KX construction',r'the construction of \ref{maps:src:D.2.22}')
body=body.replace('We apply the authorized LK same-fan result, including\nits complete integral maps.',r'Apply \ref{maps:src:D.2.43} to this same fan, including its integral boundary maps.')
body=body.replace("LK's normalization and duality\ncalculation, including its Laurent/Tor inverse maps.",r'the normalization and duality calculation in \ref{maps:src:D.2.43}, including its integral inverse maps.')
body=body.replace('the LK explicit disc basis','the explicit disc basis below')
body=body.replace('The unit-retaining local comparison in LK is',r'The unit-retaining local comparison of \ref{maps:src:D.2.43} is')
body=body.replace('These sections extend the\nadmitted natural-row local maps to arbitrary compatible \\(a,b\\)\nby their literal orbit and Bezout constructions.', 'The orbit and Bezout maps prove these assertions for every compatible\n\\(a,b\\), including nontransitive component permutations.')
body=body.replace('The new markings calculation prints an integer inverse for\nboth basis vectors. It obtains that inverse as follows.', 'An integer inverse for both basis vectors is obtained as follows.')
body=body.replace('This is a displayed exact inverse map, and the output records\nevery nonzero coefficient after multiplying out (6.2).', 'The gcd of the two-by-two minors of the recorded column matrix is\none in each of the 21 profiles. The extended Euclidean algorithm\ngives the integers \\(c_{jk}\\); the displayed identity is the inverse\non both basis vectors. All these columns are the actual recorded\nmonodromy images.')
body=body.replace('The admitted LI comparison is an integral statement for any ordered\nmatrices of determinant one with product one.',r'The integral comparison of \ref{maps:src:D.2.41} applies to every ordered tuple of determinant-one matrices with product one.')
body=body.replace('The section onto \\(C\\oplus K\\) is the LI ordered bar section:', 'The section onto \\(C\\oplus K\\) is its ordered bar section:')
body=body.replace('The finite-disc version is the\nadmitted averaging map with its reciprocal units.',r'The finite-disc version is the averaging map of \ref{maps:src:D.2.29}, with its reciprocal units.')
body=body.replace('A power not divisible by \\(h\\) has a fixed\npoint exactly when this projected translation vanishes.', 'On the moving real two-plane of each finite-good cap the rotation\nhas primitive order \\(h\\); hence a power not divisible by \\(h\\) has\na fixed point exactly when this projected translation vanishes.')
# Permanent relative and projected-vanishing equations.
needle='For each remaining cap, relative duality gives\n\\(H_2(U_i,\\partial U_i)=H^4(U_i)\\). Sections 2--5 show that this\ngroup is free, of rank'
assert needle in body
body=body.replace(needle,r'''Excision and Poincar\'e--Lefschetz duality give
\[
 H_2(X,E)=\bigoplus_iH^4(U_i)=\mathbb Z^{\sum h_i},
 \qquad H_1(X,E)=0.
 \tag{D.GI10}\hypertarget{tag-01ZD}{}\label{maps:eq:D.GI10}
\]
The local cap calculations show that these groups are free, with''')
needle='   \\longrightarrow\\ker\\Gamma\\longrightarrow0.'
# The fresh display uses one leading space.
needle='   \\longrightarrow\\ker\\Gamma\\longrightarrow0.' if needle in body else '   \\longrightarrow\\ker\\Gamma\\longrightarrow0'
# Use exact display terminator independently of indentation.
assert body.count('\\longrightarrow\\ker\\Gamma\\longrightarrow0.')==1
body=body.replace('\\longrightarrow\\ker\\Gamma\\longrightarrow0.',r'\longrightarrow\ker\Gamma\longrightarrow0.\tag{D.GI11}\hypertarget{tag-01ZE}{}\label{maps:eq:D.GI11}')
needle='After \\(\\delta\\) is killed, its Mumford relation contains\n\\(\\nu u\\).'
assert needle in body
body=body.replace(needle,r'''For every multiplicative fibre in the recorded profiles,
\(\gcd(\nu,\kappa)=1\). Thus the projected primitive relation is
\[
       \frac{\nu}{\gcd(\nu,a)}u.
       \tag{D.GI9}\hypertarget{tag-01ZM}{}\label{maps:eq:D.GI9}
\]
After \(\delta\) is killed, it contains \(\nu u\).''')
old='''For the 16 profiles without an original odd-star requirement,
the new markings calculation uses only these coarse vectors
\\(\\nu u\\) and their first \\(B_i^{\\pm1}\\) translates. Formula
(6.2) supplies an integer right inverse onto \\(\\mathbb Z^2\\)
in every profile except OS49/II. The complete output prints
these actual relation words and coefficients. Thus this is
an unbounded proof for every compatible \\(a,b\\), every weight
distribution and every filling choice, rather than a finite
search over those parameters.'''
new=r'''For each of the 16 profiles without a required original odd-star cap,
form the two-row matrix whose columns are \(\nu u\) and their first
\(B_i^{\pm1}\) translates. The gcd of its two-by-two minors is one
in every profile except OS49/II. Hence the same Bezout-adjugate formula
above supplies an integer right inverse onto \(\mathbb Z^2\).
Here the profiles are OS43/default, OS43/II, OS45/default, OS45/II,
OS47/default, OS47/II, OS47/III, OS49/default, OS49/II, OS49/III,
OS55/default, OS55/II, and OS56/default, OS56/II, OS56/III, OS56/IV.
The five remaining profiles contain a required original odd-star cap.
The column containment used here is independent of \(a,b\), the weights,
and the other filling choices; it proves the stated unbounded scope.'''
assert old in body
body=body.replace(old,new)
# Formula references become mathematical descriptions or existing permanent links.
ranges={
 '(2.3)--(2.8)':'the cusp maps above',
 '(3.2)--(3.5)':'the rank-one quotient, specialization and cap-group maps',
 '(7.2)--(7.3)':'the last-boundary maps',
 '(9.6)--(9.7)':'the splitting and rank identities',
}
for a,b in ranges.items():body=body.replace(a,b)
refs={
 '1.1':r'the base-line map', '1.2':r'\eqref{maps:eq:D.GI2}',
 '1.3':'the symplectic identity above', '1.4':'the product identity above',
 '2.1':r'the matrix \(C\)', '2.2':'the long-period maps',
 '2.3':'the displayed Smith maps', '2.4':r'the first kernel in \eqref{maps:eq:D.GI3}',
 '2.5':'the cusp groups above', '2.6':'the short/long quotient map',
 '2.7':'the component-disc boundary formula', '2.8':'the complete disc map',
 '3.1':'the node charts', '3.2':'the rank-one quotient map',
 '3.3':'the rank-one specialization', '3.4':'the rank-one fibre kernel',
 '3.5':'the rank-one cap groups', '4.1':'the additive orbit groups',
 '4.2':r'the map \((\phi,\chi)\)', '4.3':r'the rows \((L,D)\)',
 '4.4':'the saturated return kernel', '4.5':'the displayed period basis',
 '5.1':'the integral return basis', '5.2':r'\(E(M)\times S^1_\ell\)',
 '5.3':r'the row \(\omega\)', '5.4':'the additive cap groups',
 '5.5':'the three displayed killed wedges', '5.6':'the multiplicative cap groups',
 '6.1':'the integral rim identity', '6.2':'the Bezout-adjugate identity',
 '7.1':r'the function \(f_A\)', '7.2':'the last cochain formula',
 '7.3':'the peripheral graph map', '7.4':'the fixed-normal formula',
 '7.5':'the two freeness conditions', '7.6':'the full five-column formula',
 '7.7':'the finite-core presentation', '8.1':r'the Smith quotient \(\mathbb Z^g\oplus T\)',
 '8.2':r'\eqref{maps:eq:D.GI5}', '9.1':r'\eqref{maps:eq:D.GI3}',
 '9.2':'the component-disc kernel basis', '9.3':'the full component boundary formula',
 '9.4':r'\eqref{maps:eq:D.GI11}', '9.5':r'\(Mz=Pz\prime\)',
 '9.6':'the integral splitting', '9.7':'the rank identity',
 '10.1':'the primitive vanishing-vector formula', '10.2':'the displayed raw matrices',
 '10.3':'the displayed Klein-four actions', '10.4':'the displayed quotient map',
 '11.1':r'\eqref{maps:eq:D.GI6}', '11.2':r'\eqref{maps:eq:D.GI7}',
}
for a,b in refs.items():body=body.replace('('+a+')',b)
# Internal section references are prose, without introducing permanent aliases.
sections={
 'Sections 3--5':'the rank-one and original-cap calculations above',
 'Sections 2--5':'the local cap calculations above',
 'Sections 3--5':'the rank-one and original-cap calculations above',
 'Section 2':'the positive-cusp calculation',
 'Section 4':'the zero-Chern calculation',
 'Section 6':'the full boundary-kernel calculation',
}
for a,b in sections.items():body=body.replace(a,b)
body=body.replace('the clean theorem','the theorem').replace('the clean statement','the statement')
body=body.replace('All subsequent lattice bases are bases\nof these actual periods.','All subsequent lattice bases are bases of these actual periods.')
# Convert the four genuine algorithm steps, leaving the proof itself unnumbered.
start=body.index('1. Form ')
end=body.index('\nAll operations are finite',start)
steps=body[start:end]
steps=re.sub(r'^([1-4])\. ',r'\\item ',steps,flags=re.M)
body=body[:start]+'\\begin{enumerate}\n'+steps+'\n\\end{enumerate}\n'+body[end:]
# A corrected explanation of the original explicit example.
body+=r'''

\smallskip\noindent\emph{A pair beyond the scalar-iteration catalogue.}
In OS45/default take \(P=2G,Q=8G\), weight two at the \(I_8\)
fibre, all other weights zero, Mumford fillings throughout, and \(e=1\).
The literal positive period matrix and its Smith factors are
\[
 C=\begin{pmatrix}8&24\\-6&-16\end{pmatrix},\qquad
 \det C=16,\qquad(s,t)=(2,8).
\]
The preceding integral algorithm gives
\(\operatorname{coker}\mathcal B=\mathbb Z/8\),
\(\sum h_i=20\), \(b_1(E)=5\), and \(H_1(X)=0\).
The vertical quotient is trivial by the OS45 vanishing relations;
the ordinary power \(\tau=-\gamma\), together with the product relation,
then kills \(\gamma\). Thus \(\pi_1(X)=1\), and
\[
 H_2(X)=\mathbb Z^{15}\oplus\mathbb Z/8,\quad
 H_3(X)=\mathbb Z/8,\quad H_4(X)=\mathbb Z^{15},\quad\chi(X)=32.
\]
The scalar iteration map on the original construction is the period
subgroup inclusion \(\gamma_D\mapsto D\gamma\), covering the identity
of the elliptic base. It changes the positive weight to \(D\) and
retains its support. Every natural OS45 positive fibre is \(I_1\),
by \ref{maps:src:D.2.22}; hence none of these scalar iterates has this
positive \(I_8\) support. This proves the claimed extension of the
marked construction family. The determinant alone would not prove it:
the \(D=16\) iterate of a natural OS45 \(I_1\) input also has period
index sixteen, while retaining its \(I_1\) support.
'''
body=body.replace('Poincare','Poincar\\\'e').replace('Bezout','B\\\'ezout')
# Fix prose artifacts created by replacing parenthesized local references.
fixes={
 'The prescribed total weight makes the product identity above the identity.':'The prescribed total weight makes the ordered product equal to the identity.',
 'This records precisely the actual-map hypothesis\nneeded in applying the cusp maps above.':'These maps verify the actual-period hypotheses of the cusp calculation.',
 'The two composites are identity by the bar':'The two composites are the identity by the bar',
 'The free middle\nrank is the Euler identity.':'The free middle rank follows from the Euler identity.',
 'with their sections.':'with their sections.',
}
for a,b in fixes.items():body=body.replace(a,b)
assert not re.search(r'\(\d+\.\d+\)',body)
assert not re.search(r'^##|^\d+\. ',body,re.M)
receiver=statement.rstrip()+'\n\n\\begin{proof}\n'+body.rstrip()+'\n\\end{proof}\n'
oldproof=(LANE/'S6_SERIES_PUBLISH_III_02LN_released_proof.tex').read_text()
original=statement+oldproof
for command in ('label','hypertarget','tag'):
    pattern=r'\\'+command+r'\{([^{}]+)\}'
    old=set(re.findall(pattern,original));new=set(re.findall(pattern,receiver))
    assert old==new,(command,old-new,new-old)
assert receiver.count('\\begin{proof}')==receiver.count('\\end{proof}')==1
assert '\\StatementRecord' not in receiver and '\\path{code/' not in receiver
path=LANE/'S6_SERIES_PUBLISH_III_02LN_receiving.tex'
with path.open('x') as f:f.write(receiver)
print('RECEIVER',path,'LINES',len(receiver.splitlines()),'SHA256',sha256(receiver.encode()).hexdigest())
for command in ('label','hypertarget','tag'):
 print('IDENTITIES',command,len(set(re.findall(r'\\'+command+r'\{([^{}]+)\}',receiver))))
print('COMPLETE one proof; all original identities retained; canonical and frozen fresh files untouched.')
