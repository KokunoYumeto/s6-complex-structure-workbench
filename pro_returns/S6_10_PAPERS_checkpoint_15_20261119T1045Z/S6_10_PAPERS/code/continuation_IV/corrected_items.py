"""Precisely scoped receiving corrections for sweep item 4.

The historical source statements are not overwritten.  Each entry specifies
the corrected conclusion and the retained construction used to name its
objects.  A retained construction locator is not a use of its false numerical
conclusion.  Geometric input proofs retain their own check records.
"""

ITEMS = []

def item(source, title, refs, retained, statement, proof):
    ITEMS.append(dict(source_id=source, label='iv:correction:'+source,
        historical_label='night:'+source, title=title,
        correction_inputs=['night:'+r for r in refs.split()],
        retained_construction_scope=retained,
        statement=statement.strip(), proof=proof.strip()))

item('P3F.25', 'The physical trace index and the weighted OS47 return',
     'P3K.68 P3K.69',
     'The explicit real trace, page, cap and endpoint maps; the original and coprime reference-fan zero cases.',
     r'''For the actual traces, page and cap maps of the historical record
\cref{night:P3F.25}, the physical line gives
\[
 A_M=\frac{p_{\rm rel}-12s_\delta}{24}=-A_U.
\]
The original and coprime higher reference-fan returns remain zero.
The positive degree-four weighted OS47 loop has
\(s_\delta=-14\), \(p_{\rm rel}=-72\), and physical class \(4\in\mathbb Z/28\).
The specified Viaclovsky and Liu--Rollenske reference returns on
\(\lambda=r^4\) remain zero.  The retained shorter Liu--Rollenske family
has \(u=w^2\); the intrinsic obstruction to a one-\(u\) endpoint is
unchanged. These statements use the actual covers, with the quotient
orientation fixed.''',
     r'''The explicit dual-line arrow of \cref{night:P3K.68} changes
the sign of both characteristic integers and of their index; it leaves
the quotient orientation fixed. Thus the old trace expression
\((12s_\delta-p_{\rm rel})/24\) is \(A_U\), and its negative is the
physical expression displayed here. Substitution gives
\((-72+168)/24=4\). The same sign change sends each retained zero to
zero. The covers and endpoint maps are the named construction data,
not consequences of a division in \(\Theta_7\); their physical transfer
is exactly \cref{night:P3K.69}.''')

item('P3K.6', 'The meridian-one line and its physical dual',
     'P3K.68 P3K.69',
     'The embedded trace, exterior and cap collars, orbit product and unique outward-meridian-one class.',
     r'''On the actual trace and collars displayed in
\cref{night:P3K.6}, let \(M\) be the physical line and \(U\) the
outward-meridian-one Thom line. Then \(U=M^{-1}\), including its
specified boundary identification. On nonzero fibres the map is
\[
 D:M^\times\longrightarrow (M^{-1})^\times,
 \qquad D(v)(v)=1,\qquad D(cv)=c^{-1}D(v).
\]
It sends the physical positive fibre circle to its inverse circle.
Consequently the page restriction of the Thom class is \(-c_1(M)\),
and
\[
 (k_U,\ell_U,A_U)=-(k_M,\ell_M,A_M),\qquad [\Phi]=A_M=-A_U\pmod{28}.
\]
The embedded trace and the integer uniqueness with its prescribed
meridian remain the same constructions.''',
     r'''A nonzero vector in a one-dimensional complex vector space
specifies the unique linear functional taking value one on it. This
gives the displayed map in every trivialization, and transition
functions change to their inverses, so the local maps glue. On
\(c=e^{i\theta}\), its circle degree is \(-1\). Hence the Chern class
changes sign, its cube changes sign, and its product with the unchanged
\(p_1\) changes sign. The index \((4k-\ell)/24\) therefore changes
sign. The actual inverse-closing and sphere-gluing arrow, with its
fixed quotient orientation, is proved in \cref{night:P3K.68}; applying
it yields the stated physical class. No orientation change of the
quotient is inserted.''')

item('P3K.10', 'The primitive OS45 generator in the physical convention',
     'P3K.68 P3K.69 P3F.24',
     'The primitive OS45 Weierstrass source, line O(8G-O), suspension by -G, ordinary order-one cap, and sphere topology.',
     r'''Retain the actual primitive OS45 family of
\cref{night:P3K.10}: put \(R=t^2+1\),
\[
 y^2=x^3-3fx+2g,\quad f=R^2+t,\quad
 g=R^3+\tfrac32tR+\tfrac38,\quad G=(R,\sqrt3/2),
\]
with its line \(\mathcal O(8G-O)\), suspension by \(-G\), specified
ordinary norm-one cap, and positive primitive scalar loop. Its
reference physical integer is \(3\), its Eells--Kuiper invariant is
\(3/28\), and its oriented return class is \(3\in\mathbb Z/28\).
The positive finite pullbacks realize all 28 classes. The mapping
torus of the primitive return is nonproduct in the precise sense of
\cref{night:P3F.24}.''',
     r'''This is the \(d=8\), \(\chi=1\) case of the actual
physical formula in \cref{night:P3K.69}: \(A_M=d/2-1=3\).
The gluing arrow in \cref{night:P3K.68} identifies this integer modulo
28 with the oriented sphere class. The characteristic formula gives
\(\mu=A_M/28\). An \(N\)-fold positive pullback concatenates the
same return \(N\) times, so its class is \(3N\). Since
\(\gcd(3,28)=1\), these are all residues. The nonzero primitive class
and the actual mapping-torus criterion of \cref{night:P3F.24} give
the last assertion. The construction and topology used to identify
this concrete family are retained at their original proof loci.''')

item('P3K.17', 'The two actual OS49 diagonal returns',
     'P3K.65 P3K.68 P3K.69',
     'The charged cap, both diagonal fans and their complete outer marking, with m=3k, n=+/-1 and the retained delta twist.',
     r'''For the actual OS49 component-line family and charged cap
of \cref{night:P3K.17}, take \(m=3k\), \(k>0\), the signed primitive
twist \(n=\pm1\), and its retained integral \(d\delta\) twist.
The negative and positive diagonal returns are respectively
\[
 \begin{array}{c|cc}
 &T_-&T_+\\\hline
 \lambda=r^{3k}\text{, one positive }r\text{-loop}&-3k&0\\
 \lambda=w^k\text{, one positive }w\text{-loop},\ w=r^3&-k&0
 \end{array}\quad\text{in }\mathbb Z/28.
\]
The full negative-to-positive native Cox comparison has identity
first outer map and second outer positive-normal determinant winding
\(-2m\). In particular, at \(k=1\) the negative classes are
\(25\) and \(27\).''',
     r'''Use the full relative diffeomorphism of \cref{night:P3K.65},
which includes both outer maps. Its directed central increment is
\(-3k\) for the specified \(r\)-loop and \(-k\) for the actual
shorter \(w\)-loop, from the positive-fan value zero. This comparison
is made in the oriented central generator; \cref{night:P3K.68,night:P3K.69}
identify the same generator with the physical convention. Reducing
\(-3\) and \(-1\) modulo 28 gives 25 and 27. Omitting the second
outer determinant would omit the recorded \(-2m\) winding, which
is exactly the missing datum in the historical equality claim.''')

item('P3K.22', 'The physical reference values for the ten primitive profiles',
     'P3K.68 P3K.69',
     'The ten source profiles, primitive section heights, sphere topology, page squares and effective smooth-site cap restrictions.',
     r'''For the ten actual primitive scalar-parameter sphere
families constructed in \cref{night:P3K.22}, grouped by
\(d=8,14,20,30\), the positive reference physical integers are
\[
 A_M=d/2-1=3,6,9,14,
\]
respectively. The source, topology and page data remain those
specified there: the page-line square is \(-d\) and
\((dG)\cdot O=(d-2)/2\). At the retained effective smooth-site
caps the first homology contribution
\((\mathbb Z/m_i)^2\) forces every such \(m_i=1\) in a sphere
member, with total signed order-one norm \(\pm1\).''',
     r'''The physical transfer in \cref{night:P3K.69} is
\(A_M=H/2-\chi\); these named profiles have \(H=d\) and
\(\chi=1\). Substituting the four values gives the displayed table.
The line duality of \cref{night:P3K.68} changes no source intersection
or cap homology calculation. The direct summand
\((\mathbb Z/m_i)^2\) vanishes exactly at \(m_i=1\); the retained
signed norm equation then has value \(\pm1\). Thus the topology
restriction has the same scope as the concrete construction, while
the signed physical table is the corrected one.''')

item('P3K.23', 'The physical fixed-edge flop formula',
     'P3K.68 P3K.69',
     'The quaternion maps, common-link identification, relative groups and oriented native commutator.',
     r'''For the actual fixed-edge Cox flop in
\cref{night:P3K.23}, let \(A_M\) be the physical reference integer
of its specified family. The native right integer is
\(n=6A_M=-6A_U\). The same directed flop has physical class
\(7A_M\pmod{28}\). Thus the four primitive profile classes
\(3,6,9,14\) give flopped classes \(21,14,7,14\), the weighted
OS47 class \(4\) gives zero, and a zero reference class stays zero.''',
     r'''The oriented native commutator adds the right integer
\(n\) to the existing physical class. The explicit line and gluing
comparison of \cref{night:P3K.68,night:P3K.69} gives
\(n=6A_M\), so the sum is \(A_M+6A_M=7A_M\).
Multiplying the listed integers by seven and reducing modulo 28
gives the claimed examples. No other fan-product identification is
part of this fixed-edge assertion.''')

item('P3K.24', 'The reduced III physical scalar return',
     'P3K.68 P3K.69',
     'Both explicitly constructed reduced III sources, their Cartier lines, caps and endpoint maps.',
     r'''For the two actual reduced III families and endpoint maps
of \cref{night:P3K.24}, with cap order \(m=4l+3\), the positive
scalar reference return is
\[
 A_M=3l+2,\qquad \mu=(3l+2)/28,\qquad [\Phi]=3l+2\pmod{28}.
\]
This includes the explicit alternative source
\(y^2=x^3+tx-t\), \(G=(1,1)\), with its stated line and cap data.
As \(l\) runs through any 28 consecutive admissible values, the
physical returns run through all 28 residues.''',
     r'''Apply the reduced-branch physical formula in
\cref{night:P3K.69}, with the exact dual-line arrow of
\cref{night:P3K.68}. Its scalar integer is \(3l+2\), and the
Eells--Kuiper expression divides that integer by 28. The increment
under \(l\mapsto l+1\) is three. Multiplication by three permutes
\(\mathbb Z/28\) because \(3\cdot19=1\pmod{28}\). The original
two endpoint constructions name the concrete families to which the
same physical formula applies.''')

item('P3K.25', 'The actual vertical-shear correction',
     'P3K.62 P3K.64 P3K.68 P3K.69',
     'The actual periodic vertical fans, full period group, cap gluing and fixed physical cocharacter.',
     r'''For the ten primitive families of
\cref{iv:correction:P3K.22}, retain their actual scalar loop of
winding \(J=1\). The fan written in the historical record as
\(e_2,(1,-j),(1,-j-1)\) is exactly \(T_{-j}\) in the convention
\(T_n=(e_2,(1,n),(1,n-1))\). Its physical class is
\[
 A_j=d/2-1-\frac{j(j+1)}2\pmod{28}.
\]
The initial and reflected fans \(j=0,-1\) have the same class.
For primitive OS45, \(j=-2\), namely \(T_2\), has class two,
whereas the reference class is three. The complete outer
\(C_1\) determinant has winding \(-2J\).''',
     r'''The literal ordered directions identify \(n=-j\), not
\(n=j\). Substitute this into the actual vertical formula
\(A(T_n)=A(T_0)-J n(n-1)/2\) of \cref{night:P3K.64}, and use
\(A(T_0)=d/2-1\) from \cref{night:P3K.68,night:P3K.69}.
Then \(n(n-1)=j(j+1)\). This product vanishes at \(j=0,-1\)
and equals two at \(j=-2\), giving \(3-1=2\).
The narrow initial/reflected comparison and its nonzero outer
winding are the full native maps of \cref{night:P3K.62}.''')

item('P3K.27', 'The primitive native free pair and physical central class',
     'P3K.68 P3K.69',
     'The actual Cox framing comparison and its two free relative coordinates.',
     r'''In the actual primitive \(d\)-profile Cox framing of
\cref{night:P3K.27}, the meridian-one characteristic pair is
\((-3d,-24)\), the physical pair is \((3d,24)\), and the retained
native free pair is \((6,3d-6)\). The physical central class is
\(d/2-1\pmod{28}\).''',
     r'''The dual-line map of \cref{night:P3K.68} negates the
characteristic pair without changing the displayed native free
coordinates. Therefore
\((4(3d)-24)/24=d/2-1\). The identification of this index with
the central physical class and the retained free pair is precisely
the primitive specialization of \cref{night:P3K.69}.''')

item('P3K.29', 'The retained exterior bases and the obstruction to a marked product',
     'P3K.61 P3K.62 P3K.68 P3K.69',
     'The integral cells, common-exterior meridian and dual-cycle maps, symmetry and local frame-change identity.',
     r'''For the literal common exterior of the actual index-one
cusp flop in \cref{night:P3K.29}, the retained maps are
\[
 m'_0=-m_0+2m_1+2m_2,\quad m'_1=m_1,\quad m'_2=m_2,
 \qquad D'_0=-D_0,\quad D'_j=D_j+2D_0\ (j=1,2).
\]
They preserve \(m_j\cdot D_i=\delta_{ji}\). For a nonzero actual
scalar winding \(J\), the simultaneous marked
\(\delta\)-equivariant plumbing product claimed in the old row
has the incompatible determinant requirement \(-J=0\).
The actual native \(C_1\) product has free pair \((J,-J)\);
in particular its right coordinate at \(J=1\) is \(-1\).''',
     r'''Write the meridian change as
\(L=\left(\begin{smallmatrix}-1&2&2\\0&1&0\\0&0&1\end{smallmatrix}\right)\).
The displayed dual-cycle change is \(L^t\), and
\(L(L^t)^t=L^2=I\), proving the pairing statement exactly.
The full marked-product compatibility calculation is
\cref{night:P3K.61}; its necessary equality \(-J=0\) fails for
each stated nonzero \(J\). The actual alternative native product
and its free pair are constructed in \cref{night:P3K.62}.
The physical duality in \cref{night:P3K.68,night:P3K.69} changes
the central convention, not these free coordinates or the
determinant obstruction.''')

item('P3K.30', 'The general reference physical pair',
     'P3K.68 P3K.69',
     'The actual canonical whole-zero page, its height and Euler characteristic, normal framing and native free pair.',
     r'''For the actual whole-zero reference families with
\(H=Ma^2/d\) and page holomorphic Euler characteristic \(\chi\)
of \cref{night:P3K.30}, both retained signed norm choices and the
specified joint determinant \(\pm1\) cases give
\[
 (k_U,\ell_U)=(-3H,-24\chi),\qquad
 (k_M,\ell_M)=(3H,24\chi),\qquad
 A_M=H/2-\chi.
\]
The actual native free pair remains \((6\chi,3H-6\chi)\).''',
     r'''The two lines are related by the exact map of
\cref{night:P3K.68}, so their characteristic pairs are negatives.
For the physical pair the index is
\((12H-24\chi)/24=H/2-\chi\). The full native comparison in
\cref{night:P3K.69} keeps the free pair and includes both signed
norm choices. This argument uses the actual reference framing and
makes no simultaneous all-fan product assertion.''')

item('P3K.31', 'The counterexample to the norm polynomial and its replacement',
     'P3K.64 P3K.68 P3K.69 P3K.73',
     'The actual single-star product-frame, boundary-flop and complex-normal reset maps.',
     r'''For the primitive OS45 scalar loop, the reference fan
\(T_0\) and the actual fan \(T_2\) have the same displayed
\(\delta\)-coordinates \((0,1)\) in the old norm expression,
so both have \(S=r^2-rs+s^2=1\). Their physical returns are
nevertheless three and two, respectively. Thus the universal
norm polynomial asserted in \cref{night:P3K.31} is false.
For the actual whole-zero \(I_1\) scalar scope, the complete
replacement is the target-by-target fan algorithm of
\cref{night:P3K.73}, using its full period matrix, ordered fan,
initial data and native reset maps.''',
     r'''The physical reference value is three by
\cref{night:P3K.68,night:P3K.69}. The actual vertical comparison
of \cref{night:P3K.64} subtracts
\(J\,2(2-1)/2=1\) at \(J=1\), giving two.
Equal input \(S=1\) cannot give these two unequal values under
the asserted single polynomial. The corrected algorithm in
\cref{night:P3K.73} retains the complete ordered matrix data and
solves every target prism; it supplies the specified replacement
without inferring a global marked product from a single star.''')

item('P3K.32', 'The reference conclusion for the full signed cap data',
     'P3K.64 P3K.67 P3K.68 P3K.69 P3K.73',
     'The full source/cap topology, ordinary framing chart, signed norm reduction and page data.',
     r'''For the actual sphere data, page and ordinary framing
chart of \cref{night:P3K.32}, the reference physical integer is
\(H/2-\chi\), the meridian-one pair is \((-3H,-24\chi)\),
the physical pair is \((3H,24\chi)\), and the native free pair
is \((6\chi,3H-6\chi)\). The topology and full signed norm
equation retain their displayed scope. For these actual families,
vertical fan changes use \cref{night:P3K.64,night:P3K.67};
the complete whole-zero \(I_1\) fan computation uses
\cref{night:P3K.73} with all its ordered data.''',
     r'''The actual reference calculation is the specialization
of \cref{night:P3K.69} to the complete signed cap data.
The map of \cref{night:P3K.68} negates the characteristic pair
and gives \((12H-24\chi)/24=H/2-\chi\). It leaves the named
topology and signed norm maps unchanged. The cited vertical and
whole-zero fan results prove their stated extensions; none uses
the withdrawn final all-fan sentence as a premise.''')

item('P3K.33', 'The original shorter family and its corrected fan values',
     'P3K.68 P3K.69 P3K.73 P3K.74',
     'The explicit finite-root, parameter and cap descent and individual reference fixed-star comparison.',
     r'''Retain the original source, finite roots and signed cap
data of \cref{night:P3K.33}, with orders \(3K,4L\),
\(\gcd(3K,4L)=1\), and \(4Ln_0+3Kn_1=\varepsilon=\pm1\).
The literal shorter parameter is
\[
 w_h=e^{-\pi i c/(KL)},\qquad u=\kappa w_h^{2KL},
 \qquad w_h=r^6.
\]
Its reference physical pair is \((KL,4KL)\) and its reference
class is zero. Its complete whole-zero \(I_1\) fan values are
given by \cref{night:P3K.73} with
\(J=2KL\), \(\widehat H=KL/3\), \(\widehat\chi=KL/6\).
For \(K=L=1\), its actual \(T_2\) return is \(26\pmod{28}\),
and its all-fan image is all of \(\mathbb Z/28\).''',
     r'''The actual descended line and tangent numbers, followed
by the map of \cref{night:P3K.68,night:P3K.69}, give
\((3\widehat H,24\widehat\chi)=(KL,4KL)\), hence index zero.
The parameter equality gives the scalar winding \(J=2KL\).
The retained endpoint identifies this actual shorter loop, so these
are the inputs of \cref{night:P3K.73}, not division of a sphere
class. At \(K=L=1\), its vertical specialization subtracts
\(J=2\) on \(T_2\), giving \(-2=26\). The complete all-fan
image and this precise counterexample are established in
\cref{night:P3K.74}.''')

item('P3K.34', 'The physical OS49 page and the corrected fan computation',
     'P3K.65 P3K.68 P3K.69 P3K.76 P3K.77',
     'The actual component-supported line, m=3k cap with its signed primitive vector, and corrected local page/framing proof.',
     r'''For the actual component-supported OS49 family of
\cref{night:P3K.34}, with \(m=3k\), scalar
\(\lambda=r^{3k}\), signed primitive cap vector and retained
\(d\delta\) twist, the positive-fan physical pair is
\((2m,8m)\) and its class is zero. On the vertical fans
\(T_n\), with negative \(T_0\) and positive \(T_1\),
\[
 (k_{M,n},\ell_{M,n})=
 \bigl(2m-6m(n-1)^2,8m\bigr),\qquad
 A(T_n)=-m(n-1)^2\pmod{28}.
\]
The general ordered-fan formula is the full target-prism
algorithm of \cref{night:P3K.77}. At \(k=1\), the negative
fan has class \(-3\), contradicting the old zero value at
\(S=1\).''',
     r'''The physical line identification is
\cref{night:P3K.68,night:P3K.69}. The actual OS49 seed and
vertical transport of \cref{night:P3K.76} give the displayed
pair with \(j=m\). Substitution in \((4k_M-\ell_M)/24\)
gives \(-m(n-1)^2\). At \(n=1\) this is zero and at
\(n=0,m=3\) it is \(-3\), in agreement with the full
relative Cox comparison of \cref{night:P3K.65}.
\Cref{night:P3K.77} retains the OS49 period matrix for
all target fans; the whole-zero \(I_1\) matrix is not substituted.''')

item('P3F.53', 'The retained source catalogue and corrected physical entries',
     'P3K.68 P3K.69 P3K.73 P3K.74 P3K.77',
     'The sixteen profiles, twenty-six source pairs, thirty-one root branches, cap topology and exact endpoint constructions.',
     r'''The source-pair and root tables of \cref{night:P3F.53}
retain their constructive scope: sixteen profiles, twenty-six
source pairs and thirty-one root branches, with the good/good
\(III^*+II\) branch having no sphere solution and the other
thirty carrying their stated determinant and coprimality data.
For each actual canonical scalar reference family put
\[
 H=Ma^2/d,\qquad
 \chi=\frac{M(12-e_\infty-e_0)+m_0e'_\infty+m_\infty e'_0}{12}.
\]
Its physical pair is \((3H,24\chi)\) and its reference integer
is \(H/2-\chi\). The primitive OS45 entry is three.
Complete whole-zero \(I_1\) fan entries are computed by
\cref{night:P3K.73}; the component-supported OS49 entries use
the different actual seed and period matrix in \cref{night:P3K.77}.''',
     r'''The exact retained catalogue and its construction scope
are identified in \cref{night:P3K.74}. Its page and line data
enter the physical transfer of \cref{night:P3K.68,night:P3K.69},
which gives \(A_M=(12H-24\chi)/24\). For primitive OS45,
\(H=8,\chi=1\), this is three, rather than the old residue 25.
The complete fan algorithms cited in the statement supply their
respective actual source scopes. The old norm-polynomial columns
do not enter any of these conclusions.''')

item('P3K.35', 'The actual shorter scalar descent in the physical convention',
     'P3K.68 P3K.69 P3K.73 P3K.74',
     'The finite-root, Cartier-line, period, cyclic-norm and shorter-parameter morphisms; individual reference fixed-star computation.',
     r'''For the actual whole-zero source and line
\(\mathcal O(aG-O+D)\) of \cref{night:P3K.35}, retain
\(ab=d\), \(M=\prod_i m_i\), the complete signed norm
equation including its ordinary framing chart, and the constructed
free deck action with \(b\mid M\). Its actual descent is
\[
 w=r^b,\qquad \lambda=w^{M/b}.
\]
Writing \(H=Ma^2/d\), its positive reference \(w\)-loop has
\[
 (k_M,\ell_M)=(3H/b,24\chi/b),\qquad
 A_M=(H/2-\chi)/b.
\]
These are characteristic-number identities for the descended
family. For complete whole-zero \(I_1\) fan values use
\cref{night:P3K.73} with the actual shorter-loop input
\(J=M/b\), \(\widehat H=H/b\), \(\widehat\chi=\chi/b\).''',
     r'''The retained free deck action and all its cap, line and
endpoint maps identify an actual degree-\(b\) pullback of the
descended family. Integrating the pulled-back characteristic forms
therefore multiplies their integer evaluations by \(b\).
Apply the physical dual-line map of
\cref{night:P3K.68,night:P3K.69} to the retained reference
calculation, obtaining the displayed pair and index. This uses
the explicit covering map and integration, with no division in
\(\Theta_7\). The corrected scope and counterexample to the old
polynomial are recorded in \cref{night:P3K.74}; the full algorithm
is \cref{night:P3K.73}.''')

item('P3K.36', 'The corrected Liu--Rollenske parameter and return',
     'P3K.68 P3K.69 P3K.73 P3K.74',
     'The intrinsic obstruction to a one-u endpoint and the actual degree-two source, cap and line family.',
     r'''For the fixed-source Liu--Rollenske data of
\cref{night:P3K.36}, the stated one-positive-\(u\) loop has
no biholomorphic endpoint identification with those data. The
retained corrected family closes over the explicit map
\(u=w^2\). Its positive reference \(w\)-loop has physical
pair \((3,12)\), native free pair \((3,0)\), and class zero.
Its actual \(T_2\) return is \(26\pmod{28}\).
The complete whole-zero \(I_1\) fan values use
\cref{night:P3K.73} with \(J=2\),
\(\widehat H=1\), \(\widehat\chi=1/2\).''',
     r'''The retained intrinsic endpoint obstruction and the
literal degree-two map specify the closed family to which any
return is assigned. Under the physical arrow of
\cref{night:P3K.68,night:P3K.69}, its characteristic pair is
\((3,12)\), so the reference index is zero. Its shorter input
has scalar winding two. The actual vertical specialization of
\cref{night:P3K.73} therefore subtracts two on \(T_2\), giving
\(-2=26\). These exact data and the counterexample are
\cref{night:P3K.74}; the old norm polynomial supplies no step.''')

item('P3K.37', 'The actual shorter OS49 family',
     'P3K.65 P3K.68 P3K.69 P3K.74 P3K.76 P3K.77',
     'The shorter scalar descent w=r^3, component line, cap/cusp endpoints and independent reference calculation.',
     r'''The actual OS49 shorter family of \cref{night:P3K.37}
has \(w=r^3\), \(\lambda=w^k\), and all its stated component
line, cap and cusp endpoint maps. For one positive \(w\)-loop
its positive-fan physical pair is \((2k,8k)\), its native
free pair is \((2k,0)\), and its positive class is zero.
Its negative class is \(-k\). More generally
\[
 A(T_n)=-k(n-1)^2\pmod{28};
\]
the general ordered-fan result is \cref{night:P3K.77}.''',
     r'''The actual shorter endpoint, rather than a formal
quotient of a sphere class, specifies this loop. The physical
line transfer of \cref{night:P3K.68,night:P3K.69} gives the
positive pair, of index zero. The full directed comparison in
\cref{night:P3K.65} gives the negative class \(-k\), and
\cref{night:P3K.76} gives its vertical extension with \(j=k\).
\Cref{night:P3K.77} uses the actual component-line period
matrix for all fans. At \(k=1\), the negative value is
\(27\), the counterexample in \cref{night:P3K.74}.''')

item('P3K.40', 'The selected-cusp first fixed-edge return',
     'P3K.68 P3K.69',
     'The selected-cusp source, literal cap/Cox comparison and native right coordinate -6.',
     r'''For the actual selected-cusp family and directed
fixed-edge flop of \cref{night:P3K.40}, the physical initial
class is \(-1\), the native right coordinate is \(-6\),
and the first flopped physical class is
\(-7=21\pmod{28}\).''',
     r'''The exact physical baseline in
\cref{night:P3K.68,night:P3K.69} is \(-1\). The retained
directed native Cox commutator adds its actual right integer
\(-6\). Hence the result is \(-1-6=-7=21\pmod{28}\).
The local source, cap and framing maps are precisely those
specified in the historical construction.''')

item('P3K.41', 'Marked cap-data loops and actual scalar iterates',
     'P3K.68 P3K.69 P3K.73 P3K.74',
     'The fixed-source marked affine cap, Cartier-line and annular comparison, with its necessary scalar winding and fixed-scalar trivialization.',
     r'''Within the fixed-source marked whole-zero \(I_1\)
cap-data space of \cref{night:P3K.41}, retain exactly its affine
cap, line and annular maps and shorter descent of degree \(b\).
The specified loops have scalar winding \(NM/b\), and their
return on the fixed ordered fan \(P\) is
\(N A(P)\pmod{28}\), where \(A(P)\) is the actual shorter
scalar return computed by \cref{night:P3K.73}. Fixed-scalar
loops have zero return. The primitive OS45 datum at
\(N=1,P=T_0\) has class three.''',
     r'''Here is the exact return-map transport in the retained
marked cap-data comparison. Write \(F_t:X_t\to Y_t\) for its
fibre isomorphisms, \(E_X:X_0\to X_1\) and \(E_Y:Y_0\to Y_1\)
for the forward endpoints, and \(\psi_X,\psi_Y\) for parallel
transport in the transported connections. Then
\[
\begin{aligned}
 F_1\psi_X&=\psi_YF_0,
 & A&=E_Y^{-1}F_1E_XF_0^{-1},\\
 F_0\Phi_XF_0^{-1}&=A^{-1}\Phi_Y,\\
 \Phi_X&=E_X^{-1}\psi_X,
 & \Phi_Y&=E_Y^{-1}\psi_Y.
\end{aligned}
\]
The actual endpoint calculation identifies \(A\) with the
extending physical \(\mathbb C^*\) action and supplies its path
to the identity. Thus the return classes agree. The target
family concatenates the actual shorter scalar return \(N\)
times, so addition in the oriented return group gives
\(N A(P)\). The scalar-zero-winding target is constant,
giving zero.
The physical identification and reference value are
\cref{night:P3K.68,night:P3K.69}; the full fan computation is
\cref{night:P3K.73}. The concrete OS45 counterexample to the
old value is \cref{night:P3K.74}. This statement concerns the
specified marked cap-data space, with no source-moduli loop or
additional endpoint map included.''')

item('P3K.43', 'Moving ordinary sites with their full retained markings',
     'P3K.68 P3K.69 P3K.73 P3K.74',
     'The moving regular-source order-one sites, their allowed permutation and complete cap, line and annular comparison.',
     r'''For the marked fixed source and effective caps of
\cref{night:P3K.43}, let its order-one ordinary sites move on
the stated regular locus, avoiding the fixed singular and
effective-cap sites, with the full retained cap maps and allowed
permutation. The displayed family morphism identifies these
data with the reference family at the same scalar. Fixed-scalar
loops have zero return, and loops of scalar winding \(NM/b\)
have return \(N A(P)\), with the actual shorter whole-zero
\(I_1\) value \(A(P)\) from \cref{night:P3K.73}.
Constant ordinary-site paths in the primitive OS45 reference
case give class three at \(N=1\).''',
     r'''Use the literal moving-site morphism with its source,
line, annular and cap restrictions, retained and scoped in
\cref{night:P3K.74}. Under every allowed site permutation,
its whole cap data give the exact equation
\(F_0\Phi_XF_0^{-1}=A^{-1}\Phi_Y\) displayed in the proof of
\cref{iv:correction:P3K.41}; the endpoint discrepancy \(A\)
is the extending physical action with its path to the identity.
Thus the value is \(N A(P)\), and the scalar-zero-winding
target is constant. The class three for the indicated
constant-site example is the physical transfer of
\cref{night:P3K.68,night:P3K.69}. Site collisions and
source-moduli motion do not belong to this named parameter
space or the morphism used here.''')

item('P3K.44', 'Marked OS49 cap-data loops',
     'P3K.65 P3K.68 P3K.69 P3K.74 P3K.76 P3K.77',
     'The fixed-chart OS49 component-line cap comparison, reference annular map and actual scalar-iterate reduction.',
     r'''Fix the actual OS49 source and component line
\(\mathcal O(G-O)\), suspension by \(-3G\), cap
\(m=3k,n=\pm1\), and retained \(d\delta\) twist and
annular marking of \cref{night:P3K.44}. In its fixed-chart
marked cap-data space, a loop of scalar winding \(Nk\)
has return \(N S_k(P)\), where \(S_k(P)\) is the actual
shorter OS49 return of \cref{night:P3K.77}. Fixed-scalar
loops have zero return. On \(T_n\) the formula is
\(-Nk(n-1)^2\); thus at \(N=k=1\) the negative fan has
class 27 and the positive fan has class zero.''',
     r'''The retained component-line cap comparison includes
the same source, finite characters, line and annular maps.
Its endpoint comparison has the exact equation
\(F_0\Phi_XF_0^{-1}=A^{-1}\Phi_Y\) displayed in the proof of
\cref{iv:correction:P3K.41}, with \(A\) the extending
physical action and its actual path to the identity. Here
the target is \(N\) copies of the constructed shorter OS49
loop. The oriented group operation therefore gives
\(N S_k(P)\). The physical convention is fixed by
\cref{night:P3K.68,night:P3K.69}; the negative and positive
values agree with \cref{night:P3K.65,night:P3K.74}.
Substitute \(S_k(T_n)=-k(n-1)^2\) from
\cref{night:P3K.76}. The complete all-fan computation uses
\cref{night:P3K.77}, not the whole-zero \(I_1\) formula.
The parameter space here contains the stated fixed-chart data;
no source-moduli motion or additional ordinary clutch is added.''')

item('P3K.45', 'The reflected selected-cusp return',
     'P3K.68 P3K.69',
     'The complete half-source conjugacy and its cap, line and endpoint restrictions.',
     r'''For the full half-source conjugacy of
\cref{night:P3K.45}, the reflected initial selected-cusp
physical return is \(-1=27\), while the separate actual
fixed-edge flopped return is \(-7=21\), in \(\mathbb Z/28\).''',
     r'''The retained half-source conjugacy identifies the
initial and reflected return maps with all their source,
line and cap markings. Their common physical baseline is
\(-1\) by \cref{night:P3K.68,night:P3K.69}.
The fixed-edge directed commutator adds the native right
integer \(-6\), giving \(-7\). These are respectively
27 and 21 modulo 28; the two operations are specified by
their actual maps.''')

item('P3K.46', 'The selected-cusp native coordinates',
     'P3K.68 P3K.69',
     'The exact cap map, parameter reversal and native Cox framing.',
     r'''For the actual cap map, parameter reversal and
native framing of \cref{night:P3K.46}, the meridian-one
pair is \((6,0)\), the physical pair is \((-6,0)\),
and the native relative coordinates are \((0,-6,-1)\).''',
     r'''The explicit dual-line map of \cref{night:P3K.68}
negates the characteristic pair. Its physical index is
\(4(-6)/24=-1\). The native free pair remains \((0,-6)\)
under the same comparison, giving the triple in
\cref{night:P3K.69}. The cap and parameter-reversal
maps used to identify the return are unchanged.''')

item('P3K.50', 'The selected-cusp ordinary coordinates',
     'P3K.68 P3K.69',
     'The ordinary plumbing product, variation entry V00=0, derivative delta0=-12 and pure-left product-change maps.',
     r'''In the actual ordinary product of
\cref{night:P3K.50}, the selected-cusp return has relative
coordinates \((6,-6,-1)\). The retained variation and
derivative entries are \(V_{00}=0\), \(\delta_0=-12\),
with the displayed pure-left product-change maps.''',
     r'''The ordinary product change retains the free
pair \((6,-6)\). The physical line and gluing arrow
of \cref{night:P3K.68,night:P3K.69} identifies the
common central coordinate as \(-1\). Neither the
variation entry nor the derivative is changed by
replacing the dual-line central label with this physical
one. This is the specified ordinary product only.''')

item('P3K.52', 'All three selected-cusp relative pairs',
     'P3K.68 P3K.69',
     'The ambient stable frame, integral relative cycles, literal derivative action and closed Spin lifts.',
     r'''In the actual ordinary plumbing product and frame
of \cref{night:P3K.52}, the derivative vector and ordinary
free pairs are
\[
 \delta=(-12,-12,0)^t,\qquad
 (m_0,n_0)=(6,-6),\quad(m_1,n_1)=(6,-6),\quad(m_2,n_2)=(0,0).
\]
Their common physical central coordinate is \(-1\).
The actual native nonfixed products have free pairs
\((0,-6)\) at \(C_1\) and \((-6,0)\) at \(C_2\).''',
     r'''The derivative and its closed Spin lifts are the
retained constructions; the line-convention correction
does not alter their integral free coordinates. The
physical baseline is \(-1\) by
\cref{night:P3K.68,night:P3K.69}. Attaching that baseline
to each specified single-curve product gives the claimed
coordinates. No subsequent fan reset is used in this
statement.''')

item('P3K.54', 'The three selected-cusp first flops',
     'P3K.68 P3K.69',
     'The three complete native products and their right coordinates (-6,-6,0).',
     r'''For the three actual first flops of
\cref{night:P3K.54}, the native right integers are
\((-6,-6,0)\), and the physical classes are
\((21,21,27)\), respectively.''',
     r'''The common physical initial class is \(-1\)
by \cref{night:P3K.68,night:P3K.69}. The same directed
central operation adds the actual right integer in
each native product, giving \((-7,-7,-1)\), which
reduces to \((21,21,27)\) modulo 28.''')

item('P3K.56', 'The selected-cusp vertical fan sequence',
     'P3K.68 P3K.69',
     'The full vertical-fan enumeration, source/cap maps and native right integers.',
     r'''For the actual selected-cusp vertical fans
\(T_n\) of \cref{night:P3K.56}, the physical return is
\[
 A_n=-1-3n(n-1)\pmod{28}.
\]
Its image, for all integers \(n\), is exactly
\(\{5,7,9,13,19,21,23,27\}\).''',
     r'''The actual directed recurrence in
\cref{night:P3K.69} has physical baseline \(-1\)
under \cref{night:P3K.68}; summing its retained native
increments gives \(-3n(n-1)\). To determine the full
image, replacing \(n\) by \(n+28\) changes the
integer by \(-28(6n+81)\). The residues for
\(0\le n<28\) are therefore exhaustive and give
the displayed eight-element set.''')

item('P3K.57', 'The physical fixed-scalar infinity indices',
     'P3K.68 P3K.69',
     'The complete E7 source/Cartier/cap maps, residue calculation, doubled lattice, root endpoint and annular cochain.',
     r'''For the actual E7 infinity family of
\cref{night:P3K.57}, retain its source
\[
 y^2=x^3+(-2+3\epsilon^2)x^2+tx+
 \epsilon^2(1-\epsilon^2)^2,
 \quad G=(0,\epsilon(1-\epsilon^2)),
\]
its selected whole-zero fibre, line
\(M_a=\mathcal O([aG]-[O])\), suspension by \(-bG\),
and either its initial or literal reflected fan.
At fixed small nonzero scalar, the positive infinity
\(\epsilon\)-loop has meridian-one indices \(0,1\)
and physical classes \(0,-1\), respectively, for
\[
 (a,b,m)=(1,2,4p),\qquad(2,1,4p-1),\quad p\ge1.
\]
Both signed primitive cap norms and the retained integral
\(d\delta\) twists have this stated scope.''',
     r'''The actual line in the retained residue
calculation is the meridian-one line, as checked by
the explicit source/cap and dual-line arrows of
\cref{night:P3K.68}. Applying the physical transfer
of \cref{night:P3K.69} negates its indices \(0,1\)
to \(0,-1\). The full root endpoint, doubled
lattice and annular cochain belong to the named
construction and are retained; no additional source-zero
or other-fan return is asserted by this fixed-scalar
infinity statement.''')

item('P3K.58', 'The physical cut relation and paired source-zero sum',
     'P3K.68 P3K.69',
     'The full E7 source/root/annular maps and actual cut-surface relation.',
     r'''For the actual source-zero and infinity loops
of \cref{night:P3K.58}, with
\(\lambda=v^{km}\lambda_0\), retain its full source,
line, root and annular markings. Put
\[
 A_{\rm scalar}=0\quad\text{for }(a,b,m)=(1,2,4p),
 \qquad A_{\rm scalar}=3p-1\quad\text{for }(2,1,4p-1).
\]
The actual cut relation is
\(Z_{\mathcal T}+Z_{J\mathcal T}-1+I_{\mathcal T}=0\).
The physical infinity returns and paired sums are
\[
 \begin{array}{c|cc}
 &I_{\mathcal T}&Z_{\mathcal T}+Z_{J\mathcal T}\\\hline
 (1,2,4p)&0&1\\
 (2,1,4p-1)&-1-2k(3p-1)&2+2k(3p-1).
 \end{array}
\]''',
     r'''The complete source and scalar comparison in
\cref{night:P3K.69}, with the physical line of
\cref{night:P3K.68}, gives the fixed-scalar infinity
baseline zero or \(-1\) and the scalar contribution
\(-2kA_{\rm scalar}\). Hence the two infinity values
are as displayed. Solving the retained actual cut
relation for the paired sum gives \(1-I_{\mathcal T}\),
which is one or \(2+2k(3p-1)\).''')

item('P3K.59', 'The two selected-cusp mutation sequences',
     'P3K.68 P3K.69',
     'The displayed mutation matrices, complete native free pairs and directed identities.',
     r'''For the two actual mutation sequences
\(P_j,R_j\) of \cref{night:P3K.59}, the physical
central classes are
\[
 A(P_j)=-1-3j(j+1),\qquad
 A(R_j)=-7-24j(j+1)\pmod{28}.
\]
The second sequence has least positive period seven
and image \(\{1,13,17,21\}\).''',
     r'''The physical baselines supplied by
\cref{night:P3K.68,night:P3K.69} are \(-1\) and
\(-7\). Summing the retained directed mutation
increments gives the respective quadratic terms
\(-3j(j+1)\) and \(-24j(j+1)\). For the second
sequence, the change under \(j\mapsto j+7\) is
\(-28(12j+48)\). Its seven values have image
\(\{1,13,17,21\}\). A positive period \(h\)
would give zero change in both \(j=0\) and \(j=1\);
their difference is \(-48h\), so \(7\mid h\).
Thus seven is the least positive period.''')

item('P3K.60', 'The physical source-zero pair and its order-two choice',
     'P3K.68 P3K.69',
     'The single native diagonal-star product, its double parameter pullback and the ordinary doubled plumbing product.',
     r'''For the marked E7 source and scalar
\(\lambda=v^{km}\lambda_0\) of \cref{night:P3K.60},
retain its complete root, Cartier, finite-character,
annular and integer-cochain maps. The single native
free pair is \((1-a,a)\), and the actual diagonal
return difference is \(Z_{J\mathcal T}-Z_{\mathcal T}=a\).
With the physical scalar integer
\(A_{\rm scalar}=0\) for \((1,2,4p)\) and
\(A_{\rm scalar}=3p-1\) for \((2,1,4p-1)\), the
paired physical possibilities are exactly
\[
 (Z_{\mathcal T},Z_{J\mathcal T})=
 (kA_{\rm scalar}+14e,\ a+kA_{\rm scalar}+14e),
 \qquad e\in\{0,1\},
\]
in \((\mathbb Z/28)^2\). The same \(e\) occurs in
both entries; the value of \(e\) remains unselected.''',
     r'''The retained native flop gives the difference
\(a\). The physical cut relation of
\cref{night:P3K.68,night:P3K.69} gives the sum
\(a+2kA_{\rm scalar}\): this is one in the good
branch and \(2+2k(3p-1)\) in the reduced branch.
Subtracting the difference from the sum yields
\(2Z_{\mathcal T}=2kA_{\rm scalar}\pmod{28}\).
The kernel of multiplication by two in \(\mathbb Z/28\)
is exactly \(\{0,14\}\). Hence
\(Z_{\mathcal T}=kA_{\rm scalar}+14e\), and adding
the known difference gives the second entry.
This lists both possibilities without dividing a
homotopy-sphere class or selecting an unproved one.''')

assert len(ITEMS) == 33
assert len({x['label'] for x in ITEMS}) == 33
