# Actual native parameter composition for source-zero returns

Recovery record, 2026-11-17: the complete NP.1–4 mathematical proof is reconstructed from retained pre-outage messages. The original bytes and certificate source were absent from restored checkpoint19. The original proof was independently read and accepted by root and checks before its integration into P3K.89.

## NP.1. The independent source/root family and its exact square

Retain
\[
 E_v:\quad Y^2=X^3+(1-2v)X^2+TX+v^2,\qquad G=(0,v),
\]
the actual Cartier line and selected whole-zero fibre
\(q=T-(v^2-2v)\).
The two branches are
\[
 (a,b,m)=(1,2,4p),\qquad(2,1,4p-1),\qquad p\ge1.
\]
The finite norm sign is \(n=\pm1\), and all fixed finite characters and full integral annular cochains remain prescribed.

Over the independent source and scalar-root parameter annuli, the actual maps are
\[
 B=r^mB_0(v),\qquad A=r^nA_0(v),\qquad A_0^m=B_0^n,
\]
\[
 F=F_0(v)+n\frac{\log r}{2\pi i}s_\infty\delta .
\]
The arrow \(F\) is ordinary to cap. The actual \(F_0\) includes its Cartier correction, integral period and finite character.

Write
\[
 q=q_\infty^{-1}h_\infty,\qquad
 h_\infty=1-T_0(v)q_\infty.
\]
A positive root-parameter turn has the exact forward square
\[
 F_{\rm end}R_{\rm ord}=R_{\rm cap}F_{\rm start},
 \qquad R_{\rm ord}=q^n,\quad R_{\rm cap}=h_\infty^n.
\]
Indeed the variation of \(F\) is \(n s_\infty\delta\), and the
\(q_\infty^{-n}\) part of \(q^n\) is its inverse in this square.
The remaining factor is exactly \(h_\infty^n\). This retains both annular logarithms with their directions.

At the chosen source-loop basepoint \(v_*\), use
\[
 r_{\rm base}=v_*^k r_0,\qquad r_0^m=\lambda_0.
\]
The coupled loop \(r=v^k r_0\) has this actual basepoint. Its amplitude is not replaced by \(r_0\).

## NP.2. All four edges of the phase square

Let \(t\in[0,1]\) be the positive source phase and \(\rho\in[0,1]\) the independent root-scalar phase. Keep all full units in
\[
 H_T:(Z,V,q)\mapsto(\kappa qZ,\alpha V,q),\qquad
 B:(Z,V,q)\mapsto(gZ,q\eta V,q).
\]
The fixed coefficient \(\eta\) includes \(r_{\rm base}^m\) and excludes the variable scalar phase. On the cut choose coherent logarithms
\[
 G=\log g,\qquad H=\log\eta,
\]
whose literal endpoint jumps are
\[
 G(t+1)-G(t)=2\pi ib,\qquad
 H(t+1)-H(t)=-4\pi i.
\]

The current-to-reference normal product, the inverse of the P3K.30 reference-to-current arrow, has two factors
\[
 C(t,\rho)=(A,D),\qquad
 A=e^{n\rho G},\qquad
 D=e^{n\rho H+\pi i n m\rho(\rho-1)}.
\]
For the vertical fan \(T_j\), put \(D_j=D A^{-j}\). On the two native \(C_0\) charts the full factors are
\[
 (A,(AD_j)^{-1},D_j),\qquad
 (A^{-1},D_j^{-1},AD_j).
\]
Their actual Cox lift is
\[
 (a_0,a_1,c_0,c_1)\mapsto
 (a_0,Aa_1,(AD_j)^{-1}c_0,D_jc_1).
\]
This preserves the rank-one matrix, both ruling charts, their overlap and the full \(q\)-normal germ.

The four boundary arrows are as follows. At \(\rho=0\) the map is the identity. At \(t=0\) it is the actual inverse P3K.30 scalar product with the retained units at the chosen basepoint. At \(\rho=1\),
\[
 C(t,1)=(g^n,\eta^n)=E_r^{-1},
 \qquad E_r=(g^{-n},\eta^{-n}),
\]
so the actual endpoint normal map composes to the identity.

Across the source cut, the ratio is exactly
\[
 K_j(\rho)=
 \left(e^{2\pi inb\rho},
       e^{-2\pi in(2+bj)\rho}\right).
\]
This follows from the two logarithm jumps above, and retains the whole source cut.

Here is its literal normal action. For bounded unit factors
\((a,p,q_1)\) with \(apq_1=1\), choose continuous
\(L^2=pq_1\), \(R^2=p/q_1\); the quaternion coordinate satisfies
\(q_H\mapsto Lq_HR\), independently of the fixed-sphere coordinate.
For the displayed \(K_j\),
\[
 L=e^{-\pi inb\rho},\qquad
 R=e^{\pi in(4+2bj-b)\rho}.
\]
Both endpoint factors are \((-1)^{nb}\). Their product action therefore closes on the real normal four-plane. The fixed-sphere and orbit-meridian rotations are both \(\operatorname{Ad}L\), and extend linearly over the actual three-ball cap. The Hopf lift remains \(q_H\mapsto Lq_HR\).

For odd \(nb\), the two factors individually end at minus one. The base and normal Spin endpoints are the same sign, so their product is plus one in the total lift. This is the actual periodic lift; no odd half-phase sign is omitted. The maps depend only on \(\rho\), so their degree-three pullbacks vanish. The positive coefficient factors and off-diagonal derivative terms contract by the explicit positive/triangular normal homotopies of P3K.27, carrying their full endpoint values.

## NP.3. Every intermediate seam and the actual coupled diagonal

For \(k\) root turns, use consecutive copies of the same square. At each integer \(\rho\),
\[
 e^{\pi inm\rho(\rho-1)}=1,
\]
because \(\rho(\rho-1)\) is even. In particular at \(\rho=k\),
\[
 C(t,k)=(g^{nk},\eta^{nk}).
\]
The ordinary and cap endpoint arrows are \(q^{nk}\) and
\(h_\infty^{nk}\), respectively. This is the product of the actual \(k\) directed squares, including every intermediate seam.

On the diagonal \(\rho=kt\), the current-to-reference DZ origin has logarithmic line factor
\[
 nktH+2\pi inm k^2t^2.
\]
Subtracting the logarithm of \(C(t,kt)\) leaves
\[
 \pi inm(k^2t^2+kt)\delta.
\]
Its endpoint is an integral physical circle phase because
\(k(k+1)\) is even. This is a based physical delta loop, with its actual winding retained. It extends over the physical line, both finite caps and the fixed-star Hopf cap. Its quotient normal map depends only on the parameter and has zero degree-three pullback. Collar flattening uses the actual endpoint identity, so the full normal jets agree after the specified product comparison.

The literal phase-square homotopy moves the coupled diagonal to the concatenation of the source loop and \(k\) scalar loops at the same basepoint. The four arrows in NP.2 and all seams above carry the source, Cartier, finite-root and normal maps throughout this homotopy. The resulting composition of native free coordinates is additive. The possible group commutator is retained in the central coordinate; no division in \(\Theta_7\) occurs.

## NP.4. The resulting free pair

The actual scalar page data in the two branches are
\[
\begin{array}{c|c|c|c}
 (a,b)&m&\chi&H=-M_{\rm page}^2\\ \hline
 (1,2)&4p&p&2p\\
 (2,1)&4p-1&p&8p-2 .
\end{array}
\]
The physical reference pair is \((3H,24p)\).
The actual scalar vertical calculation of P3K.72 gives native pair
\[
 \mu_{\rm scalar}=6p,\qquad
 \nu_{\rm scalar}
 =6\left[(a-1)(3p-1)-m\binom j2\right].
\]
Applying the exact composition above to a source-loop native pair
\((\mu_v,\nu_v)\) gives
\[
 \mu_{\rm coupled}=\mu_v+6pk,
\]
\[
 \nu_{\rm coupled}
 =\nu_v+6k\left[(a-1)(3p-1)-m\binom j2\right].
\]
In particular the full relative calculation PS.1–7 and P3K.86 give
\[
 \mu_v=2-a,\qquad
 \nu_v=6P_b(j),\qquad
 P_b(j)=2b\binom{j+1}{3}+(3-b)\binom{j+1}{2}.
\]
Thus the coupled native pair is
\[
 \mu=2-a+6pk,\qquad
 \nu=6\left[P_b(j)+k(a-1)(3p-1)-km\binom j2\right].
\]
The physical characteristic pair is \((\mu+\nu,4\mu)\).
Both norm signs use the actual inverse powers in NP.1–3 and yield this same oriented positive-parameter result.

