# P3F.22. The Hopf gluing homomorphism and its Eells--Kuiper normalization

**Proved.** Use the oriented Hopf bundle with Euler class the positive
generator of the oriented two-sphere. Orient its total three-sphere by
the circle followed by the base, and orient the four-ball which it
bounds accordingly. Use the product orientation on each four-ball and
the outward-normal-first convention on
\(\partial(D^4_u\times D^4_y)\). For the gluing convention
\[
 \lambda(f)=(D^4_u\times S^3_y)\cup_{\widetilde f}
                  (S^3_u\times D^4_y),
 \qquad x\in\partial(D^4_u\times S^3_y)
       \sim\widetilde f(x),
\]
where \(\widetilde f\) is a principal-circle lift of
\(f\in I(S^2\times S^3)\), the oriented Eells--Kuiper invariant is
\[
 \mu(\lambda(f))=\frac{A(f)}{28}\pmod{\mathbb Z},
 \qquad A(f)=\frac{4k(f)-\ell(f)}{24}.                 \tag{P3F.22.1}
\]
Consequently \(\lambda\) is a homomorphism to \(\Theta _7\),
\(\lambda(a)=0\), and \(\lambda(b)\) is the generator with
\(\mu=1/28\). Its kernel is
\(\mathbb Za\oplus28\mathbb Zb\).

The assertion is a transfer computation for the specified gluing map.
An assignment of its value to a parameter loop also requires that loop's
actual oriented return map. In particular, this proposition by itself
does not select the sign of the OS47 parameter loop.

## 1. The marked double and its bordism

Put \(K=S^2\times D^4\), with boundary \(M=S^2\times S^3\), and form
\[
 N_f=K_+\cup_f(-K_-),\qquad x\in\partial K_+\sim f(x)\in\partial K_-.
\]
Let \(x\in H^2(N_f;\mathbb Z)\) restrict to the positive generator on
both copies of \(S^2\). Mayer--Vietoris and van Kampen give
\[
 \pi_1(N_f)=0,\qquad H^j(N_f;\mathbb Z)=
 \begin{cases}\mathbb Z&j=0,2,4,6,\\0&\text{otherwise}.
 \end{cases}
\]
The two spin structures on the pieces agree on the simply connected
boundary, so \(N_f\) is spin. There is a unique
\(y\in H^4(N_f;\mathbb Z)\) with \(\langle xy,[N_f]\rangle=1\).

For clarity the required bordism is an actual collar construction,
the one in Jin26v2 Lemma6.2. Write an inward collar of \(K\) as
\(M\times[0,1]_s\), and identify the two collars at the ends of
\(K\times[0,1]_t\) by
\((z,s,0)\sim(f(z),s,1)\). Rounding corners gives a seven-manifold.
Its \(s=0\) boundary is the mapping torus in the convention
\((z,0)\sim(f(z),1)\); its other boundary is \(-N_f\).
Indeed, near that collar the orientation is
\(\operatorname{or}(M)\,ds\,dt\); contraction with the outward
normal \(-\partial_s\) gives
\(\operatorname{or}(M)\,dt\). At \(t=0,1\) the other boundary pieces
are \(-K\) and \(+K\), respectively, with exactly the displayed
identification. The class \(x\) extends, as does the preferred spin
structure (choose the appropriate one of the two spin structures of
the bordism). This verifies the direction and the orientation of the
comparison, not only equality of the unoriented manifolds.

It follows that
\[
 x^2=k(f)y,\qquad p_1(TN_f)=\ell(f)y.                 \tag{P3F.22.2}
\]

## 2. Removal of the cubic coordinate by an extending map

Set \(f_0=f\circ a^{-k(f)}\). Jin's additive integral coordinates give
\[
 k(f_0)=0,\qquad \ell(f_0)=\ell(f)-4k(f)=-24A(f).
\]
The explicit quaternionic map in P3F.4 extends every lift of
\(a^n\) over \(D^4_u\times S^3_y\). Apply that extension on the
first gluing piece and the identity on the second. With the convention
above it identifies \(\lambda(f_0)\) and \(\lambda(f)\) by an
orientation-preserving diffeomorphism. This step does not assume in
advance that \(\lambda\) is a group homomorphism.

We can therefore suppose \(k=0\). Write \(p=\ell(f_0)\), so that
\(x^2=0\) and \(p_1(TN_{f_0})=py\).

## 3. The surgery and its bounding eight-manifold

Let \(L\to N_{f_0}\) have first Chern class \(x\), let
\(E=S(L)\), and let \(D(L)\) be its oriented disc bundle. The
preimage of the first \(K=S^2\times D^4\) is
\(S^3\times D^4\). Perform the framed surgery which replaces that
piece by \(D^4\times S^3\). Its framing is the product framing of
the \(D^4\) factor, so the attaching map is completely specified.
The result is a homotopy sphere, either by its explicit identification
below or by the elementary Mayer--Vietoris computation in P3F.4.

The orientation is relevant. The oriented circle bundle decomposes as
\[
 E=(S^3\times D^4)_+\cup_{\widetilde f_0}
                                      -(S^3\times D^4)_-.
\]
The boundary of \(S^3\times D^4\) has orientation
\(-\operatorname{or}(S^3\times S^3)\), whereas the boundary of
\(D^4\times S^3\) has the positive product orientation. Thus the
replacement has orientation \(-(D^4\times S^3)\). The oriented
surgery sphere is exactly \(-\lambda(f_0)\).

An eight-manifold bounding that surgery sphere is
\[
 W=D(L)\cup (D^4\times D^4),
\]
where the four-handle attaches along the specified
\(S^3\times D^4\). Equivalently it is obtained by replacing the
Hopf-disc neighbourhood of \(S^2\) by
\(\mathbb CP^2\times D^4\). This is the explicit construction in
Jiang14, proof of Lemma3.5, Case2. It has an embedded
\(\mathbb CP^2\) with trivial normal four-plane and a second
four-cycle coming from the generator of \(H_4(N_{f_0})\).
Their intersection matrix is
\[
 \begin{pmatrix}0&1\\1&0\end{pmatrix}.              \tag{P3F.22.3}
\]
The first self-intersection is zero by the trivial normal bundle; the
second is zero because the disc-bundle Thom map
\(H^2(N_{f_0})\to H^4(N_{f_0})\) is multiplication by \(x\), and
\(x^2=0\). The mixed intersection is one because the core
\(S^2\) is dual to \(y\). These facts also give a direct check of
the intersection matrix in the cited proof.

Let \(z\in H^2(W;\mathbb Z)\) be the class extending \(x\), positive
on the projective line in that \(\mathbb CP^2\). It lifts
\(w_2(TW)\): on \(D(L)\) the latter is \(x\bmod2\), and on
\(\mathbb CP^2\times D^4\) it is the hyperplane class modulo two.
Let \(u,v\) be the relative degree-four classes dual to the two
cycles in (P3F.22.3). The restrictions to those two cycles give
\[
 z^2=jv,\qquad p_1(TW)=p\,ju+3jv,
\]
where \(j:H^4(W,\partial W)\to H^4(W)\) is the natural map.
Indeed the restrictions of \(z^2\) are \((1,0)\), and those of
\(p_1\) are \((3,p)\). Hence
\[
 \sigma(W)=0,\quad
 \langle p_1^2,[W,\partial W]\rangle=6p,\quad
 \langle z^2p_1,[W,\partial W]\rangle=p,\quad
 \langle z^4,[W,\partial W]\rangle=0.              \tag{P3F.22.4}
\]

## 4. The invariant and the resulting homomorphism

For a spin boundary homotopy seven-sphere and this characteristic
extension \(z\), the spin-c Eells--Kuiper formula is
\[
 \mu(\partial W)=
 \frac{p_1^2-4\sigma(W)}{896}
 -\frac{z^2p_1}{192}+\frac{z^4}{384}\pmod{\mathbb Z}.
\]
The formula is Jiang14 Section3.1(v), with its stated hypotheses;
here \(\partial W\) is a homotopy sphere, so the required rational
relative-to-absolute degree-four map is an isomorphism. Its
normalization also follows by subtracting the spin-c index
\(\int e^{z/2}\widehat A\) from the signature polynomial.
Substitution of (P3F.22.4) gives
\[
 \mu(-\lambda(f_0))=
 \frac{6p}{896}-\frac{p}{192}=\frac{p}{672}.
\]
Since \(p=-24A(f)\), reversal of the boundary orientation proves
(P3F.22.1).

The Eells--Kuiper invariant is additive under connected sum and
identifies \(\Theta _7\) with \(\frac1{28}\mathbb Z/\mathbb Z\).
For the positive normalization one can also check the Milnor sphere
\(S_{2,-1}(\mathbb H)\): its disc bundle has Euler number one,
Pontryagin number six and signature one, giving
\((36-4)/896=1/28\). Davis82 Section3 computes the same value.
Thus (P3F.22.1), together with Jin's additivity of \(A\), proves
that \(\lambda\) is a homomorphism and gives its exact image and
kernel. No classification statement about circle actions is needed
for this last deduction. **End of proof.**
