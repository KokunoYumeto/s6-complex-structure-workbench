# P3K.37 working proof: actual shorter scalar loop for the component-supported OS49 family

This note is separate from the frozen checkpoint10 manuscript. The cap arrow
in Section 4 was independently checked by blind_control and checks on
2026-11-17. The complete statement awaits the root's audit.

Keep the exact source, component line, cap and fans of F26/F29/K34:
\(M=O(G-O)\), suspension by \(-3G\), source \(I_2\) at
\(q=1/t=0\), cap order \(m=3k\), \(k>0\), norm
\(n=\pm1\), and arbitrary fixed delta character \(d\).
The already constructed parameter is \(\lambda=r^{3k}\).
The construction below produces an actual family over
\[
 w=r^3,\qquad \lambda=w^k.                                      \tag{OS.1}
\]
Its initial positive-diagonal closed Cox pair is
\[
 (k_{\rm Jin},\ell_{\rm Jin})=(-2k,-8k),\qquad
 (m_{\rm rel},n_{\rm rel},s)=(2k,0,0).
                                                                    \tag{OS.2}
\]
For every actual allowed fan, with the physical delta cocharacter norm
\(S=a^2-ab+b^2\), its positive-loop class is
\[
 [\Sigma_{\Phi,T}]=\frac{k}{4}(S-1)(S-3)\pmod {28}.              \tag{OS.3}
\]
These are conclusions of the actual quotient and framed covering maps below,
not a division of a covered homotopy-sphere class.

## 1. The actual meromorphic +G lift and its component norm

Let \(B_0\) be the actual contracting line lift over \(-3G\), before
its scalar parameter is inserted, so \(B_\lambda=\lambda B_0\).
The target-point linearization has divisor \(C_0\); as a map of
source-point line fibres, \(B_0\) has its zero on source \(C_1\),
which is mapped to \(C_0\). This is the exact graph calculation in F31.
Consequently \(B_0^{-1}\), over \(+3G\), has its simple pole on
source \(C_0\).

There is an actual rational lift \(U\) over \(+G\). In the rational
section frame of \(M=O(G-O)\), the function
\[
 f=\frac1{x-x(G)},\qquad
 \operatorname{div}(f)=2O-G-(-G)
       =t_G^*(G-O)-(G-O)
\]
defines the isomorphism \(t_G^*M\to M\); its inverse gives \(U\).
All its remaining zeros and poles are vertical. The source translation
extends on the actual relatively minimal regular elliptic source, by the
canonical-form graph argument already proved in K22.

At the I2 cusp use F31's literal line graph
\(h_j=\lceil j/2\rceil\), \(h_{j+2}=h_j+1\).
The forward +G source shift is \(j\mapsto j+1\). After multiplying
\(U\) by an integral base monomial, its line multiplier has valuation
zero. The two actual graph defects are
\[
 h_j-h_{j+1}=-1\quad(j\ {
m even}),\qquad
 h_j-h_{j+1}=0\quad(j\ {
m odd}).                              \tag{OS.4}
\]
Thus the pole divisor is \(-C_0\). This includes both node charts,
because their endpoint graph defects determine the two fibre-coordinate
monomials. The third translated norm has divisor \(-2C_0-C_1\).
The maps \(B_0^{-1}\) and \(U^3\) cover the same translation,
so their ratio is a rational base function
\[
 \rho=B_0^{-1}/U^3,\qquad \operatorname{ord}_{q=0}\rho=1.         \tag{OS.5}
\]
The ratio is constant on each compact generic elliptic fibre. With another
whole-fibre normalization of \(U\), the last order is \(1-3e\),
which is the same exact congruence needed below.

In particular the component divisor has not been replaced by a whole fibre.
It is precisely the unequal translated coefficients in (OS.4) that produce
the whole-fibre ratio in (OS.5).

## 2. Actual cap root lift and its character

On the actual order-\(m\) good root at IV*, the line is the degree-zero
root line with Picard point \(G'\). Its marked central point has order
three. In the explicit root \(t=z^3,x=z^4X,y=z^6Y\), it is
\((X,Y)=(0,1)\) on \(Y^2=X^3+1\); the deck derivative on the
elliptic curve is \(\varrho=\zeta_3^2\). For the order-\(3k\)
root the same effective deck acts on the central curve.

The translation by +G' has an invertible line lift \(L\) on this actual
root line. One may construct it in the universal flat-line model
\((\mathbb C\times\mathbb C^*)/\Lambda\), and then compare it to
the rational pulled-back \(U\). Their ratio is a meromorphic base scalar;
on the smooth central fibre its only divisor is a whole fibre, so removing
that base power gives the extending invertible lift. Translation lifts on
this degree-zero line commute, as their universal representatives are a
source translation and a constant fibre scalar.

The exact Cartier line has deck weights \(\varrho\) at G',
\(\varrho^{-1}\) at O, and 1 at the remaining point of the order-three
orbit. Translation by +G' cyclically permutes them. Their successive ratios
are all \(\varrho^{-1}=\zeta_3\), giving
\[
 DLD^{-1}=\zeta_3 L.                                             \tag{OS.6}
\]
The finite cyclic averaging of K35 removes any nonconstant unit in this
commutator; an invariant analytic cube root then fixes the actual norm
\(L^3=B_0^{-1}\). The fixed \(d\)-character is scalar and commutes
with this map.

Write the global rational lift on the root as
\(U=z^e a(z)L\). Global deck invariance and the target-scalar identity
\(D m_f D^{-1}=m_{f(\zeta_m^{-1}z)}\) give
\[
 \zeta_m^e=\zeta_3,\qquad a(\zeta_mz)=a(z),\qquad
 \operatorname{ord}_{t=0}\rho=-\frac{3e}{m}\equiv-1\pmod3.
                                                                    \tag{OS.7}
\]
At the retained type-II fibre, and at every other ordinary fibre, the
irreducible vertical divisor of \(U\) is an integral whole-fibre divisor;
the order of \(\rho\) is therefore a multiple of three. No cap or line
character has been dropped in these calculations.

## 3. The global rational endpoint

K34's one-r-turn ordinary CLOSING map is multiplication by
\(h_0=t^n=q^{-n}\). Its arrow is from the continued endpoint to the
initial chart. Equations (OS.5)--(OS.7) prove that
\[
                    h_0\rho^{-2n}
\]
has divisor divisible by three at every source fibre. At the I2 cusp its
order is \(-3n\) modulo multiples of three; at IV* its order is
\(n+2n=3n\) modulo three; elsewhere it is divisible by three.
Factor the rational function on \(\mathbb P^1\), and fix a cube root
of its nonzero constant. This gives an actual rational function
\[
                    g_0^3=h_0\rho^{-2n}.                         \tag{OS.8}
\]
The proposed ordinary closing map is
\[
 C_r=r^{2nk}g_0(t)U^{-2n}: X_{\zeta_3r}\longrightarrow X_r.
                                                                    \tag{OS.9}
\]
Its inverse is the forward parameter deck. At an ordinary fibre its base
power cancels the whole-fibre power of \(U^{-2n}\), so it is an
invertible map of the actual line-complement quotients. The exact maps
commute with \(B_\lambda\); the scalar \(\lambda\) is unchanged
under \(r\mapsto\zeta_3r\).

On the IV* root, inserting \(U=z^eaL\) and (OS.7) leaves the precise
base power \(z^{mn/3}\) times an invariant unit and \(L^{-2n}\).
This is the power used in the cap comparison below, not a discarded pole.

## 4. The typed finite-cap commuting square

Retain F26/F29's physical convention \(V=e^{2\pi i\zeta_2}\).
Its root action is
\[
 A_r=r^n A_0,
\]
because the actual cap period is
\(\ell=n(e_\gamma-e_u)+d\delta\) in F26's homology marking and the
gamma period has line multiplier \(\lambda=r^m\).
The displayed plus-log map is ordinary to cap:
\[
 \Phi_r(z,s)=z+\frac{\log s}{2\pi i}\Pi_r(s)\ell.
\]
Under \(r\mapsto\zeta_3r\), its parameter difference is
\((mn/3)\log s\,\delta/(2\pi i)\). It is exactly the positive
power left in (OS.9). Thus the actual punctured maps satisfy
\[
 \Phi_r C_r=C_{\rm cap}\Phi_{\zeta_3r},\qquad
 C_{\rm cap}=\text{invariant unit}\cdot L^{-2n}.                 \tag{OS.10}
\]
This bounded cap map extends across the root fibre. Its conjugation is
\[
 C_{\rm cap} A_{\zeta_3r} C_{\rm cap}^{-1}
   =\zeta_3^n\,(\zeta_3)^{2n} A_r=A_r.                         \tag{OS.11}
\]
It therefore descends to the exact cap, with the original \(d\)-character.
The opposite direction would reverse both the parameter deck and this
conjugation; (OS.10) specifies the actual direction used here.

## 5. The cusp charts, cyclic quotient and identical Cox origin

Use K34's actual periods
\[
 u=(2s,s)+U(q),\qquad
 \gamma=(-3s,-s+mv)+C(q),\qquad
 K=3u+2\gamma=D+(s+2mv)\delta,
\]
where \(D=3U+2C\), \(v=\log r/(2\pi i)\), and
\(s=\log q/(2\pi i)\). The source map of \(U\) has Tate
valuation +1 and, after the chosen base normalization, line valuation 0.
Hence (OS.9) has tropical vector \((-2n,-n)\). Reindexing by the
actual source period \(h^n=(2n,n)\) makes it bounded on every toric
chart, not only on the fixed curve. This period preserves every allowed
index-one fan and every cell label. Choose K34's logarithms coherently with
the actual bounded Tate unit of G: the source unit of \(B_0\) is the
inverse cube of that unit, because both are the same marked source translation
and their valuations already agree. This specifies the first-coordinate
logarithm, including its integral period. Changing a previous logarithm by an
integer supplies the literal bounded unit torus loop; K34's quaternion
identity carries that loop as a normal rotation constant along the fixed
sphere, so its free framing class is unchanged. Retain every line unit as
follows. Put \(R=\log\rho/(2\pi i)\), let \(L_U\) be the coherent
Tate logarithm of \(U\), and put \(g=\log g_0/(2\pi i)\). The
actual norm and rational root equations give, with the constant choices
retained,
\[
 3L_U=-\gamma+mv\delta-R\delta,\qquad
 3g=-ns-2nR.
\]
Consequently the logarithm of \(C_r\), after the actual \(h^n\)
reindexing, is literally
\[
 nu-2nL_U+(2nkv+g)\delta
   =\frac{nK}{3}-\frac{ns}{3}\delta
   =\frac{nD}{3}+\frac{2nmv}{3}\delta.
\]
Thus all nonconstant units cancel by their actual norm identity, not by an
omitted change of frame. The bounded logarithm is exactly
\[
 \tau(v)=\frac n3\bigl(D+2mv\delta\bigr).                      \tag{OS.12}
\]
Changing the cube root in (OS.8) by the actual cube root of unity
\(e^{-4\pi i nk/3}\) gives the closing map
\(\widetilde C_r=e^{2\pi i\alpha}C_r\),
\(\alpha=-2nk/3\). This constant is physical delta.

The already specified K34 origin, with no new framing choice, satisfies
\[
 \sigma(v)=nvD+nmv(v-1)\delta,
\]
\[
 \sigma(v+1/3)-\sigma(v)=\tau(v)+\alpha\delta,
\qquad
 \sum_{j=0}^{2}\bigl(\tau(v+j/3)+\alpha\delta\bigr)
       =nD+2nmv\delta.                                         \tag{OS.13}
\]
The threefold ordinary composition is exactly
\[
 \widetilde C_r\widetilde C_{\zeta_3r}
       \widetilde C_{\zeta_3^2r}
     =h_0 B_\lambda^{2n};                                      \tag{OS.14}
\]
the parameter-root phase is \(e^{2\pi i2nk}=1\), and the constant
correction has cube one. The period \(B_\lambda^{2n}\) is already
divided out in the ordinary family. Thus this is exactly its prescribed
one-r-turn closing, with the cap square (OS.10), not just its action on
cohomology.

First use these maps over the universal v-plane. Their third iterate is
the existing v-to-v+1 family gluing. Quotient first by that gluing, obtaining
the already constructed r-family. The inverse of (OS.9) then induces an
order-three deck over \(r\mapsto\zeta_3r\). It is free because
\(r\ne0\). Its quotient is an actual proper holomorphic w-family with
(OS.1). The toric bounded units in (OS.12) act on every Cox character,
so this quotient retains all three curves, both triple points, and every
allowed fan simultaneously.

In K34's product convention the coordinate translation by \(\sigma\)
matches the endpoint-to-initial closing (OS.13). Thus the same Cox product
closes on the w-loop, and its pullback is literally the original r-product.
The constant correction is physical delta. In K34's actual quaternion frame
it is right multiplication by a scalar and fixes the Hopf normal vector.
The bounded unit comparison is the same \(q_H\mapsto Lq_HR\),
independent of the fixed-sphere point. The decreasing-K reflection and both
norm signs remain at both endpoints exactly as in K34; no free normal-frame
term is introduced.

## 6. The actual framed covering and the return

For the initial positive fan, the w-loop now has an actual closed normal
framing. Its threefold parameter pullback is the exact K34 loop and framing.
The induced mapping-torus covering preserves the physical circle Euler line,
the complex orientation and the prescribed spin structures. Ordinary
characteristic-number naturality therefore gives
\[
 3k_{\rm Jin}=-6k,\qquad 3\ell_{\rm Jin}=-24k.
\]
This proves (OS.2) as equations of integers of the constructed mapping torus.
Its index is zero. K31's proved recurrence applies to the simultaneous Cox
product just obtained, and substituting these two actual integers gives
(OS.3). The formula is integral because the physical cocharacter is primitive,
so S is odd and \((S-1)(S-3)\) is divisible by eight.

The executed exact certificate is
`code/part3_fourfold/os49_shorter_loop.py`. It retains the homology-to-positive
Tate sign, rather than identifying those two u coordinates silently. In the
displayed F26 homology basis,
\(u_{\rm Tate}=-e_u\), \(K=2e_\gamma-3e_u\), and
\[
 (A-I)K=-3e_w-\delta,\quad
 (B-I)K=3e_u+3e_w,\quad (C-I)K=\delta.
\]
The integral one-step cochain is explicitly
\[
 p=\frac{-n\delta-n(A-I)K}{3}=ne_w,\qquad
 q=-\frac{n(B-I)K}{3}=-n(e_u+e_w),
\]
\[
 p+Aq=0,\qquad q=(B-I)(ne_u),\qquad
 k(1+A+A^2)p=-nk\delta.
\]
Moreover \(-n\delta-3p=n(A-I)K\) and \(-3q=n(B-I)K\),
so the threefold comparison retains the exact integer period primitive.
These agree with the literal local periods and the finite-root logarithmic
power. The component defects, character/divisor identities, cyclic norm,
bounded origins and characteristic substitutions all pass in the same
certificate; its JSON and captured output are retained alongside the script.
