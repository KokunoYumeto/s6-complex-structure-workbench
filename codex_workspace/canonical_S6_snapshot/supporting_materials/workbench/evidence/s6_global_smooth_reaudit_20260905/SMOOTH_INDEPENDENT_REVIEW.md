# Independent mathematical reaudit of the smooth literal scalar--Gauss domain

## 1. Verdict, inputs and scope

PASS. Every mathematical claim in the entire staged smooth addendum is correct
on its stated domain. No staged correction is required.

Candidate: [smooth_literal_domain_addendum.tex](workspace/agent_work/scalar_gauss_independent_review_20260905/smooth_literal_domain_addendum.tex),
SHA-256 8ee198f193f6606838cc44a05ec08a1d277efe280331fe5f1df1a57d8b5d64be.
Current canonical dependency: [scalar_gauss_domain_shared.tex](workspace/output/s6_consolidated_canonical_2026-08-26/supporting_materials/workbench/research/scalar_gauss_domain_shared.tex),
SHA-256 d3555001fc55181f0ef5ea55d44ddfb9f444787928fe28be855d460686102606.
Both entire sources were read. The comparison uses the current canonical
source, not just the historical hashes in the candidate comments.

The conclusions concern the ordered literal scalar--Gauss tuples:
an embedded real six-dimensional manifold in the stated 18-dimensional
ambient manifold, exactly four connected components, an exact global
coupling product retaining both signs and three quotient-phase coordinates,
and at each original positive coupling exactly four embedded
five-dimensional connected components, each diffeomorphic to
\(\mathbb R^2\times U(1)^3\). The whole fixed-coupling fibre is the disjoint
union of these four components, not one connected copy.

“Root-free” means that the literal inverse does not choose a complex square
root of the temporal phase. The displayed positive real square roots in
\(e,k,a_\pm\) remain, with strictly positive arguments proved below.
No spatial residual is assumed zero. No physical gauge quotient, frequency
sign identification, exchange of the ordered spatial matrices, or claim
at \(t=0\) is used.

## 2. Literal data, ambient space and full zero set

The retained matrices and constants are
\[
H_0=\begin{pmatrix}0&0&0\\0&-\frac12&\frac1{2\sqrt2}\\
0&\frac1{2\sqrt2}&\frac12\end{pmatrix},\quad
q=\frac1{2\sqrt2}(1,0,0)^{\mathsf T},\quad
A_0=\sqrt2\begin{pmatrix}0&-1&0\\1&0&0\\0&0&0\end{pmatrix},
\quad m^2=\Gamma=1,\quad\kappa=6.
\]
Multiplication gives
\[
F_0=[A_0,[A_0,H_0]]
=-2H_0+\operatorname{diag}(-2,1,1),\quad
H_0^2=\tfrac38\operatorname{diag}(0,1,1),\quad q^*q=\tfrac18.
\]
Put \(P=\operatorname{diag}(1,0,0)\) and
\[
X(v)=\begin{pmatrix}0&-v^*\\v&0_2\end{pmatrix},\qquad
\mathfrak p=X(\mathbb C^2).
\]
The map \(X\) is real linear with inverse its lower first column, giving
\(\dim_{\mathbb R}\mathfrak p=4\). Every traceless anti-Hermitian matrix
has the unique form
\[
\begin{pmatrix}
ia&z_{12}&z_{13}\\
-\bar z_{12}&ib&z_{23}\\
-\bar z_{13}&-\bar z_{23}&-i(a+b)
\end{pmatrix},
\quad a,b\in\mathbb R,\quad z_{12},z_{13},z_{23}\in\mathbb C.
\]
Thus \(\dim_{\mathbb R}\mathfrak{su}(3)=8\), without restricting the
temporal matrix in the ambient space. Consequently
\[
\mathcal E=(0,\infty)\times(\mathbb R\setminus\{0\})
\times\mathfrak{su}(3)\times\mathfrak p\times\mathfrak p
\]
has real dimension \(1+1+8+4+4=18\).

For \(Y_{\rm tf}=Y-(\operatorname{tr}Y)I_3/3\), retain
\[
\mathcal I_{H_0}Y=([H_0,[H_0,Y]]+qq^*Y+Yqq^*)_{\rm tf},\qquad
\mathcal K Y=-\sum_{j=1}^2[Z_{j,0},[Z_{j,0},Y]].
\]
The set \(\mathcal S_{\rm sg}\) is exactly the zero set in \(\mathcal E\)
of the three full residuals
\[
Q_H=[C_0,[C_0,H_0]]-\sum_j[Z_{j,0},[Z_{j,0},H_0]]-F_0,
\]
\[
Q_q=(C_0^2-Z_{1,0}^2-Z_{2,0}^2)q+2q,\qquad
Q_G=(t\mathcal I_{H_0}+2\mathcal K)C_0-4\omega[Z_{1,0},Z_{2,0}].
\]
Their full codomains are \(\operatorname{Herm}_3(\mathbb C)_0\),
\(\mathbb C^3\), and \(\mathfrak{su}(3)\), respectively. The original
Gauss residual is \(Q_G/t\); clearing its denominator and dividing by
the same retained \(t=g^2>0\) are inverse operations. These objects agree
entry for entry with the canonical source. Neither spatial residual is
in this definition.

## 3. Exhaustion of the entire literal set: independent algebraic check

Let \(\mathfrak k=\{Y:[Y,P]=0\}\subset\mathfrak{su}(3)\). Block
multiplication gives the real orthogonal decomposition
\(\mathfrak{su}(3)=\mathfrak k\oplus\mathfrak p\), with
\([\mathfrak p,\mathfrak p]\subset\mathfrak k\) and
\([\mathfrak k,\mathfrak p]\subset\mathfrak p\). Both \(\mathcal I_{H_0}\)
and \(\mathcal K\) preserve these summands, and the displayed \(H_0^2\)
and \(qq^*\) give \(\mathcal I_{H_0}X(v)=X(v)/2\). For the positive real
inner product \(\langle Y,Z\rangle=-\operatorname{tr}(YZ)\), cyclicity gives
\[
\langle Y,\mathcal K Y\rangle
=-\sum_j\operatorname{tr}([Z_{j,0},Y]^2)
=\sum_j\|[Z_{j,0},Y]\|^2\ge0.
\]
The \(\mathfrak p\) projection of Gauss is
\[
\left(\tfrac t2\operatorname{id}_{\mathfrak p}
+2\mathcal K|_{\mathfrak p}\right)(C_0)_{\mathfrak p}=0.
\]
Pairing with \((C_0)_{\mathfrak p}\) and using \(t>0\) forces this
component to vanish. Thus \(C_0\in\mathfrak k\), using no spatial equation.

Retain
\[
r=\tfrac{\sqrt6}{4},\quad\delta=\tfrac1{2r}=\sqrt{\tfrac23},
\quad x=\tfrac12,\quad d_0=\tfrac1{2\sqrt2},\quad
S=\frac{\begin{pmatrix}d_0&-(r+x)\\r+x&d_0\end{pmatrix}}
{\sqrt{2r(r+x)}},\quad U=\operatorname{diag}(1,S).
\]
The identity \(r^2=x^2+d_0^2\) gives orthogonal numerator columns of
squared length \(2r(r+x)\), and determinant \(2r(r+x)>0\).
Their products with the lower block of \(H_0\) give eigenvalues \(r,-r\).
Hence \(U^*U=I_3,\det U=1,Uq=q\), and
\(U^*H_0U=\operatorname{diag}(0,r,-r)\).

The arbitrary first-frame temporal block is now
\[
C_d=U^*C_0U=
\begin{pmatrix}ia&0&0\\0&i(h-a)/2&z\\0&-\bar z&-i(a+h)/2\end{pmatrix}.
\]
For first-frame spatial columns \(\widetilde v,\widetilde w\), put
\(\widetilde M=\widetilde v\widetilde v^*+\widetilde w\widetilde w^*\).
Multiplication of all entries gives
\[
Q_q=(-a^2+\operatorname{tr}\widetilde M+2)q,\qquad
Q_H=
\begin{pmatrix}
2-2r(\widetilde M_{11}-\widetilde M_{22})&0&0\\
0&-4r|z|^2+2r\widetilde M_{11}-1+2r&-2irhz\\
0&2irh\bar z&4r|z|^2-2r\widetilde M_{22}-1-2r
\end{pmatrix}.
\]
Their vanishing is equivalent to
\[
a^2=2+\operatorname{tr}\widetilde M,\quad
2|z|^2-\widetilde M_{11}=1-\delta,\quad
2|z|^2-\widetilde M_{22}=1+\delta,\quad hz=0.
\]
The upper matrix entry is minus the lower trace. Adding the middle
equations gives \(4|z|^2=a^2\); the last middle equation and
\(\widetilde M_{22}\ge0\) give \(z\ne0\). Hence \(h=0,e=a\ne0\), with
the unique data
\[
C_d=\begin{pmatrix}ie&0&0\\0&-ie/2&z\\0&-\bar z&-ie/2\end{pmatrix},
\qquad |z|=|e|/2.
\]

Set \(\gamma=-2iz/e\), and for either \(\zeta^2=-\bar\gamma\) use
\[
W(\zeta)=\frac1{\sqrt2}
\begin{pmatrix}-\zeta^{-1}&-\zeta^{-1}\\\zeta&-\zeta\end{pmatrix},
\qquad B(\zeta)=U\operatorname{diag}(1,W(\zeta)).
\]
The displayed columns give \(W^*W=I_2,\det W=1\) and
\[
B^*C_0B=ie\operatorname{diag}(1,0,-1),\quad
B^*H_0B=H'=\begin{pmatrix}0&0&0\\0&0&r\\0&r&0\end{pmatrix},
\quad Bq=q,\quad B^*F_0B=-2H'+\operatorname{diag}(-2,1,1).
\]
For the temporal block these are the eigenvectors
\((\gamma,1)^{\mathsf T},(\gamma,-1)^{\mathsf T}\) with eigenvalues
\(0,-e\) after multiplying \(C_d\) by \(-i\). Unitarity intertwines
all products, brackets, adjoints and trace projections exactly; the vector
residual is multiplied by \(B^*\). The inverse on every matrix is
\(Y_0=BY'B^*\), and \(B\) commutes with \(P\).

In the classified frame put
\[
C=ie\operatorname{diag}(1,0,-1),\quad Z_1=X(v),\quad Z_2=X(w),\quad
M=vv^*+ww^*=\begin{pmatrix}u&m\\\bar m&v_0\end{pmatrix},\quad
N=i(vw^*-wv^*),
\]
\[
b=\operatorname{Im}(v^*w),\quad Q=\operatorname{diag}(1,2),\quad
E=\operatorname{diag}(2/3,-5/6).
\]
The complete residuals are
\[
Q_H=\begin{pmatrix}
2-4r\operatorname{Re}m&0&0\\
0&2r\operatorname{Re}m-1&r(u+v_0-e^2+2)\\
0&r(u+v_0-e^2+2)&2r\operatorname{Re}m-1
\end{pmatrix},\quad Q_q=(u+v_0-e^2+2)q,
\]
\[
Q_G=i\operatorname{diag}(\gamma_0,\mathcal G),\quad
\gamma_0=et/6+4e(u+2v_0)+8\omega b,\quad
\mathcal G=etE-2e(QM+MQ)-4\omega N.
\]
The exact multiplication identities producing these entries are
\[
X(v)^2=\operatorname{diag}(-v^*v,-vv^*),\quad
[C,X(v)]=X(-ieQv),\quad
[X(v),X(w)]=\operatorname{diag}(-2ib,iN),
\]
\[
\mathcal I_{H'}C=ie\operatorname{diag}(1/6,2/3,-5/6),\quad
\mathcal KC=\operatorname{diag}(2ie\operatorname{tr}(QM),-ie(QM+MQ)).
\]
Since \(\operatorname{tr}N=2b\), \(\gamma_0=-\operatorname{tr}\mathcal G\);
no Gauss entry is discarded. The scalars force \(m=\delta+iy\) and
\(e^2=2+u+v_0\).

With \(D_v=(v\ w)\) and \(J=\left(\begin{smallmatrix}0&i\\-i&0\end{smallmatrix}\right)\),
\[
M=D_vD_v^*,\quad N=D_vJD_v^*,\quad
M\pm N=(v\mp iw)(v\mp iw)^*.
\]
The nonzero \(m\) gives \(u,v_0>0\). If \(M\) had rank one, the Hermitian
\(N\), supported on its range line, would equal \(\nu M\) with \(\nu\) real.
For \(k=e/\omega\ne0\), Gauss says \(N=kT\), where
\[
T=\frac t4E-\frac12(QM+MQ)
=\begin{pmatrix}t/6-u&-3m/2\\-3\bar m/2&-5t/24-2v_0\end{pmatrix}.
\]
The off-diagonal entry gives \(\nu=-3k/2\); the first diagonal then
gives \(t/6=-u/2\), impossible. Hence \(M>0\).
Similarity of \(M^{-1}N\) to \(J\) gives
\(\operatorname{tr}(M^{-1}N)=0,\det N=-\det M\).
For \(d=uv_0-\delta^2-y^2\), \(c=4v_0-5u\), direct substitution gives
\[
0=d\operatorname{tr}(M^{-1}T)
=v_0(t/6-u)+u(-5t/24-2v_0)+3|m|^2
=tc/24-3d.
\]
Thus \(d>0,c>0,t=72d/c\), and all original signs and scalars are
\[
k=\sigma\sqrt{\frac d{-\det T}},\quad
e=\epsilon\sqrt{2+u+v_0},\quad \omega=e/k,\quad N=kT.
\]

Conversely, for any \(u>0,d>0,c>0\),
\[
M=L_cL_c^*,\qquad
L_c=\begin{pmatrix}\sqrt u&0\\\bar m/\sqrt u&\sqrt d/\sqrt u\end{pmatrix}.
\]
The Hermitian \(R=L_c^{-1}TL_c^{-*}\) has trace zero by the trace
identity, and is nonzero since \(T_{12}=-3m/2\ne0\).
Writing \(R=\left(\begin{smallmatrix}a&z_1\\\bar z_1&-a\end{smallmatrix}\right)\)
gives \(\det R=-a^2-|z_1|^2<0\), so \(\det T=d\det R<0\).
For either sign, \(J_0=kR\) has trace zero, determinant \(-1\), and
\(J_0^2=I_2\). The identity
\[
z_0^*(I_2\pm J_0)z_0=\tfrac12\|(I_2\pm J_0)z_0\|^2
\]
and their trace two and determinant zero show they are positive
semidefinite of rank one. Hence so are
\(A_\pm=M\pm N=L_c(I_2\pm J_0)L_c^*\).
If \(h_s=(A_s)_{11}=0\), determinant zero forces
\(m(1-3sk/2)=(A_s)_{12}=0\), thus \(sk=2/3\), but then
\[
h_s=u+sk(t/6-u)=u/3+t/9>0,
\]
a contradiction. Thus \(h_\pm>0\) for both signs on the whole domain.
The exact rank-one factors are therefore
\[
a_\pm=\binom{\sqrt{h_\pm}}{(A_\pm)_{21}/\sqrt{h_\pm}},\qquad
A_\pm=a_\pm a_\pm^*.
\]
For arbitrary unit \(p_\pm\), define
\(v=(p_+a_++p_-a_-)/2,\ w=i(p_+a_+-p_-a_-)/2\).
Then \(v-iw=p_+a_+,v+iw=p_-a_-\), so the complete \(M,N\) are
recovered. The displayed scalar entries vanish, and \(N=kT,\omega k=e\)
make the entire Gauss lower block zero; its trace identity checks the
upper entry. A column \(c\) with \(cc^*=a_\pm a_\pm^*\) has
\(|c_1|=\sqrt{h_\pm}>0\); its \((2,1)\) outer-product entry forces
\(c_2=(c_1/\sqrt{h_\pm})(a_\pm)_2\). Thus its unique phase is recovered
by the first entry, giving
\[
p_+=(v-iw)_1/\sqrt{h_+},\qquad p_-=(v+iw)_1/\sqrt{h_-}.
\]
This verifies the full canonical algebraic inverse used by the addendum,
including the original \(t,\omega,e\), not merely a dimension or invariant
calculation.

## 4. Convexity and the exact phase quotient

Put \(h=\delta^2+y^2,m=\delta+iy\) and
\[
\mathcal D=\{(u,v_0,y):u>0,\ d=uv_0-h>0,\ c=4v_0-5u>0\}.
\]
For any \(a,b\in\mathbb C\),
\[
(\bar a,\bar b)M(a,b)^{\mathsf T}
=u\left|a+\frac m u b\right|^2+\frac d u|b|^2.
\]
This proves equivalence of \(u>0,d>0\) with \(M>0\): in the reverse
direction use the first coordinate vector and then \((-m/u,1)\).
These are exactly the positive definite matrices in the affine slice
\(\operatorname{Re}M_{12}=\delta\). Every convex combination is positive
definite because its quadratic form at a nonzero column is a convex
combination of positive values. The slice and the additional affine
inequality \(c>0\) are preserved. The coordinate map into matrices is
affine and injective, proving convexity in the unchanged coordinates.
Strict continuous inequalities prove openness. The point
\((\delta,2\delta,0)\) has \(u=\delta,d=\delta^2,c=3\delta>0\).
Thus the domain is nonempty, three-dimensional and path connected.
This verifies the convexity lemma.

On \(\mathbb T=U(1)\) define
\[
\Psi(\zeta,p_+,p_-)=(\zeta^2,p_+/\zeta,p_-/\zeta)
=(\eta,\alpha,\beta).
\]
It is a smooth group homomorphism with kernel exactly
\(\{(1,1,1),(-1,-1,-1)\}\): the kernel equations are
\(\zeta^2=1,p_+=p_-=\zeta\). For any target its two preimages are obtained
from either \(\zeta^2=\eta\) and \(p_\pm=\zeta(\alpha,\beta)_\pm\).
For a base \(\eta_0=\zeta_0^2\) and arc
\(\eta=\eta_0e^{i\theta}\), \(-\pi<\theta<\pi\), the two lifts are exactly
\[
(\zeta,p_+,p_-)
=\left(\pm\zeta_0e^{i\theta/2},
\ \pm\zeta_0e^{i\theta/2}\alpha,
\ \pm\zeta_0e^{i\theta/2}\beta\right).
\]
They form two disjoint open root arcs times \(\mathbb T^2\), each
diffeomorphic to the target arc times \(\mathbb T^2\). The quotient
projection is open because the inverse image of the image of an open
set is its union with its simultaneous-sign translate. Thus these give
the actual quotient topology and smooth charts; their transitions are
ordinary torus transitions. This proves the quotient diffeomorphism.

The canonical raw map has exactly this identification. Indeed
\(W(-\zeta)=-W(\zeta)\), and with \(D_0=\operatorname{diag}(1,-I_2)\),
\[
B(-\zeta)=B(\zeta)D_0,\quad D_0CD_0=C,\quad D_0X(v)D_0=X(-v).
\]
Simultaneously changing \(p_\pm\) changes \(v,w\) to \(-v,-w\) and fixes
the entire literal tuple. Conversely equal temporal matrices recover the
same \(e,z,\gamma\), so the roots are equal or opposite. In the equal case
the full classified inverse fixes every parameter. In the opposite case
the inverse spatial matrices are conjugated by \(D_0\), giving \(-v,-w\)
and hence precisely the opposite \(p_\pm\), with unchanged
\(M,N,\epsilon,\sigma\). No further case exists. Both independent signs
are retained by the quotient.

## 5. Root-free full literal matrices and exact inverse compositions

Using the unchanged \(M,N,a_\pm,e,k,\omega,t\), set
\[
v^\flat=(\alpha a_++\beta a_-)/2,\quad
w^\flat=i(\alpha a_+-\beta a_-)/2,\quad
L(\eta)=\frac1{\sqrt2}\begin{pmatrix}-1&-1\\\eta&-\eta\end{pmatrix},
\quad B^\flat=U\operatorname{diag}(1,L(\eta)).
\]
The entries give \(L^*L=I_2,\det L=\eta,\det B^\flat=\eta\). No
determinant-one assertion is made for this auxiliary matrix.
For either \(\zeta^2=\eta\) and \(p_+=\zeta\alpha,p_-=\zeta\beta\),
\[
L(\eta)=\zeta W(\zeta),\quad
B^\flat=B(\zeta)D_\zeta,\quad
D_\zeta=\operatorname{diag}(1,\zeta I_2),\quad
v=\zeta v^\flat,\quad w=\zeta w^\flat.
\]
The full matrix equalities
\[
D_\zeta C D_\zeta^*=C,\quad
D_\zeta X(v^\flat)D_\zeta^*=X(\zeta v^\flat),\quad
D_\zeta X(w^\flat)D_\zeta^*=X(\zeta w^\flat)
\]
prove that the candidate's
\[
C_0=B^\flat C(B^\flat)^*,\quad
Z_{1,0}=B^\flat X(v^\flat)(B^\flat)^*,\quad
Z_{2,0}=B^\flat X(w^\flat)(B^\flat)^*
\]
are exactly all three canonical original matrices. The scalars \(t,\omega\)
remain unchanged. Thus the map takes values in \(\mathcal S_{\rm sg}\).

The first-frame lower temporal block is
\[
(U^*C_0U)_{\rm lower}
=-\frac{ie}{2}\begin{pmatrix}1&\bar\eta\\\eta&1\end{pmatrix}.
\]
Accordingly
\[
e=-i(U^*C_0U)_{11},\quad z=(U^*C_0U)_{23}=-ie\bar\eta/2,\quad
\eta=-2i\bar z/e.
\]
The last sign is correct: \(\bar z=ie\eta/2\), and \(-2i(ie\eta/2)/e=\eta\).

For a literal tuple recover the unit \(\eta\) this way and set
\(Z_j^\flat=(B^\flat)^*Z_{j,0}B^\flat\).
Block-diagonal unitarity implies \(Z_j^\flat\in\mathfrak p\), so its entire
matrix, not only a selected projection, is fixed by its lower first
column: the upper row is its negative adjoint and the diagonal blocks
are zero. Taking these columns as \(v^\flat,w^\flat\) gives
\[
Z_1^\flat=X(v^\flat),\quad Z_2^\flat=X(w^\flat),\quad
B^\flat Z_j^\flat(B^\flat)^*=Z_{j,0}.
\]
In original entries, with \(\ell_1=SL(\eta)v^\flat,\ell_2=SL(\eta)w^\flat\),
\[
Z_{1,0}=\begin{pmatrix}0&-\ell_1^*\\\ell_1&0_2\end{pmatrix},\quad
Z_{2,0}=\begin{pmatrix}0&-\ell_2^*\\\ell_2&0_2\end{pmatrix},\quad
C_0=\operatorname{diag}\left(ie,\
S\left[-\frac{ie}{2}\begin{pmatrix}1&\bar\eta\\\eta&1\end{pmatrix}\right]S^*
\right).
\]
Thus reconstruction includes every literal matrix entry.

Recover
\[
M=v^\flat(v^\flat)^*+w^\flat(w^\flat)^*,\quad
N=i(v^\flat(w^\flat)^*-w^\flat(v^\flat)^*),
\]
\[
u=M_{11},\ v_0=M_{22},\ y=\operatorname{Im}M_{12},\
\epsilon=\operatorname{sign}e,\ \sigma=\operatorname{sign}(e/\omega),
\]
\[
h_\pm=(M\pm N)_{11},\quad
\alpha=(v^\flat-iw^\flat)_1/\sqrt{h_+},\quad
\beta=(v^\flat+iw^\flat)_1/\sqrt{h_-}.
\]
To check all domains, choose either root of the recovered \(\eta\).
The canonical inverse gives \(v=\zeta v^\flat,w=\zeta w^\flat\).
Common multiplication by this unit leaves the entire \(M,N\) unchanged.
Section 3 therefore proves \((u,v_0,y)\in\mathcal D\),
\(M_{12}=\delta+iy\), \(h_\pm>0\), the original \(t=72d/c\), the original
signed \(e\), \(k=e/\omega\), and \(\omega=e/k\).
Its phase inverse gives \(\alpha=p_+/\zeta,\beta=p_-/\zeta\), both unit.
The first and second rank-one factor entries then give
\[
v^\flat-iw^\flat=\alpha a_+,\qquad
v^\flat+iw^\flat=\beta a_-.
\]
The forward formulas recover both columns completely, and the full
conjugations recover all original matrices and scalars.
Conversely, a forward parameter is recovered first by its temporal
\(e,\eta\), then the two complete spatial matrices, then their
\(M,N,u,v_0,y\), both signs and both phases. These are both inverse
compositions on the entire domains. The temporary root in the
verification can be either representative; neither actual formula
requires choosing it.

We have thus proved the literal bijection
\[
\mathcal F^\flat:\{1,-1\}^2\times\mathcal D\times\mathbb T^3
\longrightarrow\mathcal S_{\rm sg}.
\]
This checks the candidate's phase-map, phase-quotient, literal-forward,
literal-temporal-inverse and literal-spatial-inverse labels.

## 6. Smoothness, off-zero-set extension, and embeddedness

Every forward operation on each fixed sign sector is real smooth. All
denominators and positive-real-square-root arguments have been checked:
\[
c>0,\quad d>0,\quad-\det T>0,\quad
2+u+v_0>0,\quad h_+>0,\quad h_->0,\quad k\ne0.
\]
Matrix products, adjoints and complex conjugation are real smooth; no
holomorphic assertion is made. The inverse is continuous in the literal
subspace topology because \(e\ne0,\omega\ne0,h_\pm>0\), with its signs
locally constant. Thus the bijection is a homeomorphism onto the actual
matrix subset.

At any fixed image point the inverse coordinate formulas extend to an
ambient open neighbourhood in \(\mathcal E\). In that whole ambient
space, \(C_0\) is anti-Hermitian, so
\(e=-i(U^*C_0U)_{11}\) remains real. Shrink the neighbourhood to keep it
nonzero. The formula for \(\eta\) is a complex smooth function there even
when \(|\eta|\ne1\). Although \(B^\flat(\eta)\) then need not be unitary,
the expressions \((B^\flat)^*Z_{j,0}B^\flat\) are still smooth and
anti-Hermitian. Their lower first columns define smooth complex vectors;
the resulting \(M,N\) are Hermitian, so their first diagonal entries
\(h_\pm\) are real. In fact the exact factor identities give
\[
h_+=|(v^\flat-iw^\flat)_1|^2,\qquad
h_-=|(v^\flat+iw^\flat)_1|^2.
\]
Both remain positive near the chosen point. Hence the same formulas
define smooth complex \(\alpha,\beta\) there. No off-zero-set unitarity
or off-zero-set scalar equation has been assumed.

For a unit base value \(q_0\) of any one of \(\eta,\alpha,\beta\), the
ambient complex neighbourhood \(\operatorname{Re}(q/q_0)>0\) carries the
smooth real function
\[
\vartheta_{q_0}(q)=
\arctan\left(\frac{\operatorname{Im}(q/q_0)}
{\operatorname{Re}(q/q_0)}\right).
\]
On the unit arc this is exactly its centered angle coordinate in
\((-\pi/2,\pi/2)\). These three functions and \(u,v_0,y\) give an ambient
smooth six-coordinate map \(G\). For the corresponding local parameter
chart \(f:V\subset\mathbb R^6\to\mathcal E\), the exact inverse gives
\[
G\circ f=\operatorname{id}_V.
\]
By the chain rule \(dG\,df=I_6\). Thus \(df\) is injective and has rank
six, proved from an actual ambient inverse rather than parameter counting.

To check the embedded structure explicitly, choose six ambient linear
coordinate projections \(P_6\) whose composite with \(df\) is invertible;
six such rows exist because \(df\) has rank six. The finite-dimensional
inverse function theorem makes \(P_6\circ f\), on a sufficiently small
open parameter neighbourhood, a diffeomorphism onto an open set.
Complete to ambient linear coordinates \((P_6,P_{12})\).
The image of that restricted parametrization is then the smooth graph
\[
(a,\phi(a)),\qquad
\phi=P_{12}\circ f\circ(P_6\circ f)^{-1}.
\]
The previously proved continuous whole-set inverse makes this
parameter-neighbourhood image open in \(\mathcal S_{\rm sg}\), hence
equal to \(\mathcal S_{\rm sg}\cap O\) for some ambient open \(O\).
Thus near the base point no other parameter region adds points of the
subset outside the graph. Its graph neighbourhood is straightened by
\[
(a,b)\longmapsto(a,b-\phi(a)),\qquad
(a,b')\longmapsto(a,b'+\phi(a))
\]
as mutually inverse ambient smooth coordinates. This proves that the
literal subset is an embedded six-dimensional manifold. The explicit
inverse is smooth for this embedded structure.

The only standard analytic theorem used here is the real inverse
function theorem, with its square derivative explicitly proved invertible.
The relevant local primary literature read for this audit was John W.
Milnor, *Topology from the Differentiable Viewpoint* (1965), Section 1:
the smooth-subset definitions on printed p. 1, inverse function theorem
on p. 4, and ambient-inverse/rank argument on p. 5. Local source:
[milnortop.pdf](workspace/literature_primary/Milnor_Framed_Cobordism_20260905/milnortop.pdf);
the relevant text was read from
[Milnor_full.txt](workspace/tmp/Milnor_full.txt), lines
102 through 410. No properness, compactness, regular-value theorem,
or global fibration theorem is assumed.

## 7. Exactly four connected six-dimensional components

Each sign sector of
\(\{1,-1\}^2\times\mathcal D\times\mathbb T^3\) is nonempty: use
\((\delta,2\delta,0)\) with any phases and either independent pair of
signs. It is path connected: \(\mathcal D\) has straight-segment paths,
and two unit endpoints can be joined on a circle by choosing real
arguments for the endpoints and interpolating them. Taking products
gives paths in each sector.

On the literal set,
\(\operatorname{sign}e\) and \(\operatorname{sign}(e/\omega)\) are
continuous functions with discrete values because \(e,\omega\ne0\).
Their values cannot change on a connected subset. Therefore distinct
sectors cannot join, and the four path-connected sectors are exactly
the four connected components. By the diffeomorphism each is
\(\mathcal D\times\mathbb T^3\), of real dimension six.
The original frequency sign remains
\(\operatorname{sign}\omega=\epsilon\sigma\).
This completes the literal-diffeomorphism theorem, including its
no-additional-gauge-quotient statement.

## 8. Exact coupling differential and the whole inverse domain

Keep \(h=\delta^2+y^2,d=uv_0-h,c=4v_0-5u\).
For \(t=72d/c\), the quotient rule gives precisely
\[
t_u=\frac{72(v_0c+5d)}{c^2}
=\frac{72(4v_0^2-5h)}{c^2},\qquad
t_{v_0}=\frac{72(uc-4d)}{c^2}
=\frac{72(4h-5u^2)}{c^2},\qquad
t_y=-\frac{144y}{c}.
\]
On \(\mathcal D\), \(v_0=(d+h)/u>0\), so \(v_0c+5d>0\), proving
\(t_u>0\) everywhere and directly proving differential rank one.
For the additional simultaneous-zero check, the first two derivative
equations would give \(4v_0^2=5h\) and \(4h=5u^2\).
Positivity implies \(v_0=5u/4\), whence \(c=d=0\), excluded. The third
derivative also has the stated retained sign and factor.

Define the fixed domain
\[
\mathcal B=\left\{(v_0,y):
v_0>\frac{\sqrt5}{2}\sqrt{\delta^2+y^2}\right\}.
\]
The identity \(4v_0^2-5h=v_0c+5d>0\), with \(v_0>0\), sends every
point of \(\mathcal D\) into \(\mathcal B\).
For \(\tau=t=72d/c>0\), preserving all coefficients,
\[
\tau(4v_0-5u)=72(uv_0-h),\qquad
(72v_0+5\tau)u=4\tau v_0+72h.
\]
The denominator is positive, so the only inverse value is
\[
u=\frac{4\tau v_0+72h}{72v_0+5\tau}.
\]
Conversely every \(\tau>0,(v_0,y)\in\mathcal B\) has positive numerator
and denominator for this \(u\), and exact substitution gives
\[
c=\frac{72(4v_0^2-5h)}{72v_0+5\tau}>0,\qquad
d=\frac{\tau(4v_0^2-5h)}{72v_0+5\tau}>0.
\]
Therefore the entire stated product domain maps into \(\mathcal D\),
and \(72d/c=\tau\). Starting instead with \(u,v_0,y\) and substituting
its \(t\) returns that same \(u\) by the preceding linear identity.
Both compositions are identities, with smooth rational formulas and
positive denominators. This proves the global diffeomorphism
\[
\Theta:\mathcal D\longrightarrow(0,\infty)\times\mathcal B,\qquad
(u,v_0,y)\longmapsto(t,v_0,y).
\]
The set \(\mathcal B\) is nonempty, for example at
\((\sqrt5\delta/2+1,0)\), so every original \(\tau>0\) occurs.
Together with the differential calculation this proves a smooth
surjective submersion, without inferring surjectivity merely from rank.

Since \(\delta>0\), the function \(\sqrt{\delta^2+y^2}\) is smooth for
all real \(y\). The maps
\[
(y,s)\longmapsto
\left(\frac{\sqrt5}{2}\sqrt{\delta^2+y^2}+e^s,\ y\right),
\]
\[
(v_0,y)\longmapsto
\left(y,\log\left(v_0-\frac{\sqrt5}{2}\sqrt{\delta^2+y^2}\right)\right)
\]
are defined on exactly \(\mathbb R^2\) and \(\mathcal B\), respectively.
Their compositions are identities because the logarithm argument is
positive and exponential and logarithm are smooth inverse functions on
these domains. Hence \(\mathcal B\cong\mathbb R^2\) smoothly.
This verifies every derivative, trivialization, coupling-inverse,
inverse-domain and B-chart formula in the coupling theorem.

## 9. Global coupling product and every complete level set

Compose the explicitly proved inverse maps. Given
\[
(\epsilon,\sigma,\tau,y,s,\eta,\alpha,\beta)
\in\{1,-1\}^2\times(0,\infty)\times\mathbb R^2\times\mathbb T^3,
\]
put
\[
v_0=\frac{\sqrt5}{2}\sqrt{\delta^2+y^2}+e^s,\qquad
u=\frac{4\tau v_0+72(\delta^2+y^2)}{72v_0+5\tau},
\]
and use the retained \(e,k,\omega,M,N,a_\pm\) and literal forward
formulas above. Section 8 proves every domain inequality and proves
its original coupling is exactly \(t=\tau\).
The inverse on the entire literal set is the matrix inverse of Section 5,
followed by keeping the original \(\tau=t\) and recovering
\[
s=\log\left(v_0-\frac{\sqrt5}{2}\sqrt{\delta^2+y^2}\right).
\]
The preceding inverse proofs verify both compositions and smoothness.
Therefore
\[
\mathcal S_{\rm sg}\cong
\{1,-1\}^2\times(0,\infty)\times\mathbb R^2\times\mathbb T^3,
\]
and the original coupling projection is projection to the displayed
positive coordinate. Its differential is onto everywhere and it is
surjective.

For every specified original \(\tau>0\), the entire fibre is
\[
\pi^{-1}(\tau)\cong\{1,-1\}^2\times\mathbb R^2\times\mathbb T^3.
\]
In product angle charts fixing the \(\tau\) coordinate is an embedded
five-dimensional coordinate slice in \(\mathcal S_{\rm sg}\).
The ambient graph coordinates from Section 6 show its inclusion into
\(\mathcal E\) is embedded as well. Alternatively the explicit forward
map restricted to fixed \(\tau\) retains five continuous coordinates
with a smooth literal inverse, so the same left-inverse/graph argument
has rank five. Since the \(t\) coordinate is constant, this proof also
works in the fixed-\(t\) ambient hyperplane \(\mathcal E_\tau\), of real
dimension 17, with the same induced structure.

The plane is path connected by straight segments; the three circles
are path connected by angle paths. Each sign sector is thus connected.
The two continuous sign invariants cannot change on any connected
subset and prevent different sectors from joining. The four sectors
are exactly all connected components, each diffeomorphic to
\(\mathbb R^2\times\mathbb T^3\). This proves the global-product equation
and the complete levels corollary.

No assertion that a general surjective submersion is a global product
has been used. Here that conclusion, and the fibre topology, follow
from the full global inverse and its exact domain inequalities.

## 10. Evidence, scope checks and completion

The candidate neither sets nor uses either spatial residual and does
not claim a full rotating-ansatz solution. It concerns exactly the
three full zero residuals of Section 2. It leaves unchanged the canonical
joint exclusion that the two additional spatial residuals cannot vanish
simultaneously in the two-cross class. It does not settle unrestricted
exceptional-set existence, give a quantum spectral conclusion, or certify
the independent S6 global-construction arguments.

The independent exact supplement
[check_exact_identities.py](workspace/agent_work/scalar_gauss_smooth_reaudit_20260905/check_exact_identities.py)
ran once serially under SymPy 1.13.1 and passed all 36 groups, with exit
code zero. It uses independent real spatial coordinates and checks all
first-frame and classified scalar/Gauss entries, the complete root-free
original temporal matrix and both ordered spatial matrices, both entire
inverse spatial matrices, retained phase determinants and inverse signs,
and all coupling derivative and inverse identities.
Its unit-circle identities use an arbitrary real angle, not samples.
No numerical samples or file writes occur in that script.

These checks supplement the analytic proofs above. Strict positivity,
convexity, exhaustion of the literal zero set, sign components,
embeddedness, smooth inverses and full fibre topology were proved
analytically and are not inferred from sampled identities or a dimension
count.

The candidate has 16 new labels, all accounted for by the proofs:
section; convex; phase-map; phase-quotient; literal-forward;
literal-diffeomorphism; literal-temporal-inverse; literal-spatial-inverse;
coupling; derivatives; trivialization; coupling-inverse; B-chart;
inverse-domain; levels; global-product. The exact prefix is
sgd:smooth-addon:. Source-static checks and immutable file identities
are recorded in AUDIT_RECEIPT.json.

No candidate or canonical source was edited. No correction fragment is
needed. No build, PDF work, publication, Lean run, child agent or
other-thread contact was performed. All new artifacts are confined to
this audit directory.
