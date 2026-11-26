"""Consolidate the complete monodromy proof and its nineteen-row application.

This writes text and defect records only. Receiving reading is recorded separately.
"""
from S6_SERIES_PUBLISH_c3_edit import *

s = SOURCE.read_text()
original = s

def block(label):
    p = s.index(r'\label{' + label + '}')
    a = s.rfind(r'\begin{proposition}', 0, p)
    b = s.index(r'\end{proof}', p) + len(r'\end{proof}')
    return s[a:b]

old413 = block('night:P4.13')
old11 = block('cdp:st:C.2.UN.11')
oldc = block('cdp:st:C2c')
statement11, proof11 = old11.split(r'\begin{proof}', 1)
parts = proof11.split('\n\\item ')
assert len(parts) == 15
items = parts[1:]
items[-1] = items[-1].split(r'\end{enumerate}', 1)[0].rstrip()

def display(text, label):
    p = text.index(r'\label{' + label + '}')
    a = text.rfind(r'\[', 0, p)
    b = text.index(r'\]', p) + 2
    return text[a:b]

eq1 = display(statement11, 'cdp:eq:C.MS.1')
eq2 = display(statement11, 'cdp:eq:C.MS.2')
eq10 = display(statement11, 'cdp:eq:C.MS.10')
eq4 = display(statement11, 'cdp:eq:C.MS.4')
start413 = old413.split('Let a proper holomorphic', 1)[0]
start413 = start413.replace('Monodromy and the smooth locus of an irreducible fibre',
                           'Monodromy traces and minimum-multiplicity strata')
start413 = start413.replace('the definitions and constructions stated in the proof',
    r'\cite[\S2, pp.~237--243, and \S3, pp.~243--245]{ACampo1975}')
new413 = start413 + r'''
Let $f:U\to\Delta$ be a proper holomorphic map from a smooth complex
threefold, with connected fibres and smooth complex two-torus fibres
over $\Delta^*$. Choose an embedded resolution
$\pi:U'\to U$, unchanged away from the central fibre, and write
the full central divisor of $f\pi$ as $\sum_jN_jE_j$, with simple
normal crossings. Define
''' + eq1 + r'''
Let $T$ be the monodromy on $H^1(F,\Z)$ of a nearby fibre and $M$
the order of its semisimple part. Then $T\in\operatorname{SL}_4(\Z)$
is quasi-unipotent and
''' + eq2 + r'''
where $\mu$ is the integer M\"obius function. On $H^1(F,\Q)$,
''' + eq10 + r'''
Every $L_k$ is nonnegative. The sequence $(a_n)$ vanishes exactly
when $T$ has eigenvalue one.

Write the original full central fibre as $\sum_i m_iS_i$, put
$m_0=\min_i m_i$, and let $S_i^\circ$ be the smooth locus of $S_i$
with its intersections with the other components removed. Then
''' + eq4 + r'''
For $m_0>1$ the entire sequence $(a_n)$ vanishes. In particular, for
an irreducible full fibre $mS$, with monodromy $A$ on $H_1(F,\Z)$,
\[
 m e(S_{\mathrm{reg}})=\det(I-A^m),\qquad
 0\le e(S_{\mathrm{reg}})\le16/m,
 \qquad m>1\ \Longrightarrow\ e(S_{\mathrm{reg}})=0.
\]
\end{proposition}
\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
'''
item0 = items[0].replace('We specify first the comparison with the analytic\nfamily. ', '')
item0 = item0.replace('the actual nearby\ntorus', 'the nearby\ntorus')
item0 = item0.replace('using the actual analytic normal-crossings\ncomparison; no ambient K\\"ahler assumption enters.',
                      'for this proper analytic normal-crossings\nmodel.')
item1 = items[1].replace('actual monodromy', 'monodromy')
positivity = r'''The characteristic polynomial of $T$ has real coefficients.
Its nonreal eigenvalues occur in conjugate root-of-unity pairs,
whose contribution to $\det(I-T^k)$ is $|1-\lambda^k|^2$.
The real eigenvalues are $1$ and $-1$, contributing zero or two.
Thus $L_k\ge0$ and $L_k\le16$. An eigenvalue one makes every
$L_k$, and hence every $a_n$, zero. Conversely, the absence of
that eigenvalue makes every factor of $L_1$ positive, so
$a_1=L_1>0$.'''
minimum = items[5].replace('the specified\n$S_i^\\circ$', 'the\n$S_i^\\circ$ defined in the statement')
last = r'''For $m_0>1$, the resolved divisor has no multiplicity-one
component: strict-transform multiplicities are at least $m_0$,
and the exceptional multiplicities have the bound just proved.
Hence $a_1=0$ and the preceding criterion makes the entire
sequence vanish. For the irreducible full fibre $mS$,
\eqref{cdp:eq:C.MS.4} gives $m e(S_{\mathrm{reg}})=L_m$.
Under the evaluation pairing $H^1(F;\C)=H_1(F;\C)^\vee$, the
cohomology action is $A^T$, since $(T\alpha)(c)=\alpha(Ac)$.
Consequently $L_m=\det(I-(A^m)^T)=\det(I-A^m)$.
The bound $0\le L_m\le16$ and the vanishing for $m>1$ prove
all the remaining assertions.'''
new413 += '\n'.join('\\item '+x.strip() for x in [item0,item1,positivity,minimum,last])
new413 += '\n\\end{enumerate}\n\\end{proof}'

head11 = old11.split('Let $f:U', 1)[0]
record_start = head11.index(r'\StatementRecord')
head11 = head11[:record_start] + r'''\StatementRecord{cdp:st:C.2.UN.11}{proved}{01CO}{\cref{night:P4.13,cdp:st:C.2.UN.1,cdp:st:C.2.UN.4}; \cite[Theorem~1.6]{BierstoneMilman1997}}

'''
table_a = statement11.index(r'\begin{center}')
table_b = statement11.index(r'\end{center}',table_a)+len(r'\end{center}')
table = statement11[table_a:table_b]
eq3 = display(statement11,'cdp:eq:C.MS.3')
eq5 = display(statement11,'cdp:eq:C.MS.5')
new11 = head11 + r'''For the proper torus degeneration $f:U\to\Delta$, resolution
$\pi:U'\to U$, monodromy $T$ and stratum sequence $(a_n)$ of
\cref{night:P4.13}, the complete range of
\eqref{cdp:eq:C.MS.2} is the following table. Here $\Phi_d$ is
the $d$th cyclotomic polynomial, $P_T$ is the characteristic
polynomial of $T$, and every unlisted $a_n$ is zero.

''' + table + r'''

The table is the range on all orientation-preserving quasi-unipotent
integral rank-four matrices, so every filling in
\cref{night:P4.13} has one of its signatures. One has $a_n=0$
unless $n\mid M$, where
''' + eq3 + r'''
Every row is realized by a map from a smooth projective threefold
to $\PP^1$ whose general fibre is an abelian surface and every
fibre has Euler number zero. It can be chosen to have exactly
two singular fibres, both with reducible simple-normal-crossings
support.

For an irreducible full fibre $mS$, the table and
\eqref{cdp:eq:C.MS.4} give
''' + eq5 + r'''
\end{proposition}
\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
'''
enumeration = r'''Apply \cref{night:P4.13} to the same map $f$, embedded
resolution $\pi$, nearby fibre $F$ and its cohomology monodromy
$T$. It gives the determinant and M\"obius identities
\eqref{cdp:eq:C.MS.2}. ''' + items[2].replace('We compute their complete range. ','')
finite = items[4].split(' If $T$ has an\neigenvalue one,',1)[0]
finite = finite.replace('There is also a direct verification that no\nunlisted index can be concealed by cancellation.\nThe actual exterior-power identity gives',
    'The exterior-power identity gives')
finite = finite.replace('including\nall possible cancellations.', 'as claimed.')
irreducible = r'''For $m>1$, the vanishing assertion of \cref{night:P4.13}
gives $e(S_{\mathrm{reg}})=0$. For $m=1$,
\eqref{cdp:eq:C.MS.4} gives $e(S_{\mathrm{reg}})=a_1$,
whose table entries are exactly the set in \eqref{cdp:eq:C.MS.5}.'''
realization = items[7].replace('We now realize every row by an actual compact\nfamily.',
                              'We realize every row by a compact family.')
snc = r'''The operations in \cref{cdp:st:C.2.UN.4} preserve SNC
supports. In that proposition choose the point on one component
of the present central support away from all the others, and
use its Fermat quartic in the exceptional plane. The coordinates
$(r,u,v)$ and blowdown substitutions in
\eqref{cdp:eq:C.VR.6} and \eqref{cdp:eq:C.VR.8} apply to this
same pair of blowups: the base functions are $(ru)^m$ and
$(uvw)^m$, with the components given by their coordinate
hyperplanes. This proves the SNC assertion for these realizations.
''' + items[12].split('After the Euler number is zero,',1)[1]
snc = snc.replace('\n one additional','\nAfter the Euler number is zero, one additional',1)
# The split tail begins with a space; put its complete sentence back explicitly.
if 'After the Euler number is zero,' not in snc:
    snc = snc.replace('\n one additional','\nAfter the Euler number is zero, one additional')
    snc = snc.replace('\n\n one additional','\n\nAfter the Euler number is zero, one additional')
tail_start = snc.index(' one additional') if ' one additional' in snc and 'After the Euler' not in snc else -1
if tail_start>=0:
    snc=snc[:tail_start]+'After the Euler number is zero, one additional'+snc[tail_start+len(' one additional'):]
noninjective = r'''The matrix-to-signature map has nontrivial fibres. The matrices
$I_4$ and $I_4+E_{12}$ both have characteristic polynomial
$(x-1)^4$ and zero signature. Their minimal polynomials are
$x-1$ and $(x-1)^2$, respectively: $E_{12}\ne0$ and
$E_{12}^2=0$. Thus the two matrices give distinct conjugacy
classes in the same fibre of the displayed map.'''
newitems=[enumeration,items[3],finite,irreducible,realization,items[8],items[9],items[10],items[11],snc,noninjective]
new11 += '\n'.join('\\item '+x.strip() for x in newitems)
new11 += '\n\\end{enumerate}\n\\end{proof}'
for before,after in [('define actual automorphisms','define automorphisms'),
                     ('induces the actual\nisomorphism','induces the\nisomorphism'),
                     ('The actual positive meridian','The positive meridian'),
                     ('preserve the actual punctured family','preserve the punctured family')]:
    new11=new11.replace(before,after)
new11=new11.replace('by \\ref{cdp:st:C.2.UN.1}', 'by \\cref{cdp:st:C.2.UN.1}')
new11=new11.replace('of \\ref{cdp:st:C.2.UN.4}', 'of \\cref{cdp:st:C.2.UN.4}')

newc=oldc.replace(r'\cite[Section~6, especially (6.3)--(6.7)]{Mumford1972}',
                  r'\cite[\S6, pp.~264--268, (6.3)--(6.7)]{Mumford1972}')
newc=newc.replace(r'use the lattice $N=\mathbb Z^2\oplus\mathbb Z$',
                  r'use the lattice $\widetilde N=\mathbb Z^2\oplus\mathbb Z$')
newc=newc.replace('by a basis of $N$,','by a basis of $\\widetilde N$,')
newc=newc.replace(r'\item Let $\Lambda_N=',r'\item Fix an integer $N\ge1$ and let $\Lambda_N=')
newc=newc.replace('Here is also the required analytic properness check. For $t\\ne0$,',
                  'To prove proper discontinuity, for $t\\ne0$,')
a=newc.index('This supplies the actual convergent')
b=newc.index('\n\\item The quotient triangulation',a)
newc=newc[:a]+r'''These charts and compactness prove that the quotient is a proper
holomorphic degeneration over the complex disc. The comparison
with \cite[\S6, pp.~264--268, (6.3)--(6.7)]{Mumford1972}
is given by the monomials of each chart. For a triangle with
vertices $u_j$, its dual-cone semigroup consists of the pairs
$(\alpha,r)$ satisfying
$r+\langle\alpha,u_j\rangle\ge0$ for every $j$.
Its monomial is $t^rz^\alpha$. Base change along
$\C[t]\to\C[[\pi]]$, $t\mapsto\pi$, sends this monomial to
$\pi^r\mathcal X^\alpha$ in the affine ring of (6.1), with
the same inequalities. Face inclusions give the same monomial
localizations as (6.5), and translation by $\ell$ is the shear
already displayed. The integral affine difference
$q(u+\ell)-q(u)$ gives the polarization data for (6.7).
Thus the chart, face and period maps identify the polyhedral
model used here with the cited construction after that base change.
''' + newc[b:]
newc=newc.replace('The quotient triangulation has $V=N$ and $F=2N$, as required.',
                   'The quotient triangulation has $V=N$ and $F=2N$.')

def number_equations(t):
    def change(m):
        body=m.group(1)
        if not re.search(r'\\tag\{C\.(?:MS\.|2)',body):return m.group(0)
        body=re.sub(r'\\tag\{[^}]+\}', '', body)
        return '\\begin{equation}\n'+body.strip()+'\n\\end{equation}'
    return re.sub(r'\\\[([\s\S]*?)\\\]',change,t)

new413,new11,newc=map(number_equations,(new413,new11,newc))
preserve_identifiers(old413+old11+oldc,new413+new11+newc)
assert table in new11
assert r'\tag{C.MS.' not in new413+new11
assert '\\path{' not in new11
assert 'After the Euler number is zero,' in new11

s=s.replace(old413,new413,1).replace(oldc,newc,1).replace(old11,'',1)
hopf=r'\subsection{Hopf components and fibre boundaries}\label{subsec:II:hopf-component-boundaries}'
assert s.count(hopf)==1
newheading=r'\subsection{Rank-four monodromy stratum signatures}\label{subsec:II:rank-four-monodromy-signatures}'
s=s.replace(hopf,newheading+'\n\n'+new11+'\n\n'+hopf,1)
s=s.replace(r'\subsection{Euler numbers and monodromy signatures}\label{subsec:II:euler-monodromy-signatures}',
            r'\subsection{Semistable toric Euler models}\label{subsec:II:euler-monodromy-signatures}',1)

program=ROOT/'agents/continuation3_provenance/S6_SERIES_PUBLISH_c3_provenance_program_edits158.tsv'
_,program_rows=read_tsv(program)
assert len(program_rows)==1
p=program_rows[0]
assert s.count(p['old_text'])==1
s=s.replace(p['old_text'],p['new_text'],1)
preserve_identifiers(original,s)
SOURCE.write_text(s,newline='\n')

changes=[('MONODROMY-OWNER',['D08','D12','D19'],old413,new413,'night:P4.13',
 'Move the complete general analytic nearby-cycle proof, minimum-multiplicity calculation and their tagged formulas from UN11 to P413. Keep every original P413 hypothesis on its irreducible specialization and its exact A-to-T transpose map. Preserve every transferred conclusion and prove it in this single earlier owner.'),
 ('MONODROMY-RANGE',['D02','D08','D09','D11','D12','D14','D19'],old11,new11,'cdp:st:C.2.UN.11',
 'Apply P413 to the identical f, resolution, nearby fibre and T. Preserve all nineteen rows, every compact realization and both reducible SNC zero-Euler fibres. Apply UN4 to the identical blowup coordinates instead of repeating its chart proof. Remove only program bookkeeping and replace the closing scope disclaimer by the explicit I4 versus I4+E12 conjugacy calculation. Move the owner before its Hopf consumers.'),
 ('TORIC-EULER',['D02','D05','D08','D18','D19','D20'],oldc,newc,'cdp:st:C2c',
 'Read Mumford 1972 printed pages264–268 in full rendered images. Preserve the complete analytic fan, free proper action and compactness proof. Give its exact base-change monomial, face-localization and lattice-shear comparisons with the source; distinguish the ambient lattice symbol from its positive integer quotient index by identity on its displayed basis. Remove workflow wording and number the formula by section.')]
rows=[]
for name,kinds,before,after,statement,reason in changes:
    for j,kind in enumerate(kinds,1):
        rows.append(dict(change_id=f'II-C3-{name}-{j:02}',type=kind,statement_id=statement,
          old_location='Complete current statement and proof',old_page='cp35 continuation source; final concordance pending',
          new_location='Single earlier monodromy owner; complete signature application; toric models',new_page='integrated build pending',
          old_text=before,new_text=after,reason=reason,
          review_status='Complete originals read. Receiving proof comparison is recorded separately after writing.'))
append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',rows,'change_id')
append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',program_rows,'change_id')
print('Text written:',len(rows),'root defect rows and program158; all original labels and tags preserved.')
print('Receiving proof reading and unit status remain pending.')
