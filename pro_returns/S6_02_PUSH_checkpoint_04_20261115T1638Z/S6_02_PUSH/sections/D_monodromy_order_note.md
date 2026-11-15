# Independent check of the proposed sixth-power reduction

Status: the order-two conclusion is **not proved**. The calculation below identifies an exact residual cusp transformation that a global quotient trivialization must handle. This is not a proof that the conclusion is false.

## An explicit affine lift of every even parameter shift

Use all conventions of R2, and put β=βpart. On the universal covering of B° choose

\[
 L_0=\frac{\log t}{2\pi i},\qquad L_1=\frac{\log(t-1)}{2\pi i}.
\]

Choose the peripheral logarithms so that g1 sends L0 to L0−1, g2 sends L1 to L1−1, and the other one is unchanged in each case. For even n define

\[
 a_n^1=-\frac{7n}{2}\mu-\frac{3n}{2}\tau+2n,
\qquad
 a_n^2=-\frac{7n}{12}\beta-\frac{3n}{2}\mu
          +\frac n3L_0-\frac n4L_1.
\]

An arbitrary constant multiple of e=(0,1) can be added. This gives exactly the affine section used in R2. Indeed the displayed period transformations give

\[
 a_n(g_1z)-R_1(z)a_n(z)=(-n,0)^t
   =\Pi_{c+n}(g_1z)(-n\widehat w),
\]

\[
 a_n(g_2z)-R_2(z)a_n(z)
 =\left(-\frac{n}{2\tau},\frac n2(1+\mu/\tau)\right)^t
 =\Pi_{c+n}(g_2z)(n\widehat u/2).
\]

At the cusp g0, μ is unchanged, τ decreases by 1, β increases by 1, and both L0 and L1 increase by 1. Thus the affine defect is (3n/2,−n/2), exactly Πℓ0 from R2.

At the first finite place, a_n−n(log s1)/(2πi)e−Πr1 is holomorphic; at the second, a_n+n(log s2)/(2πi)e−Πr2 is holomorphic. Here log t−3 log s1 and log(t−1)−4 log s2 are holomorphic logarithms of the nonvanishing coordinate units. The affine defects give precisely the required equivariance of those holomorphic corrections. At the cusp β+s, τ−s, L0+s and L1+s are holomorphic, so

\[
 a_n=s(-3n/2,n/2)^t+\eta_0,
\]

with η0 holomorphic. The required original fan map therefore exists for each even n. This confirms the same actual global map as R2, up to its stated constant scalar ambiguity. Since every displayed term is linear in n and independent of c, these choices also satisfy the coherent composition rule.

The first coordinate for n=2 is −7μ−3τ+4. After adding the γ period and the integral periods 3u−4w, its first coordinate is −μ. Thus the informal identification with translation by −P was correct only modulo those full periods; those periods also alter the second coordinate and its cusp valuation.

## The exact 12-shift scalar and its cusp valuation

For n=12 the integral lattice vector

\[
 \lambda=(-7,-18,24,0)^t
\]

has first period equal to a12^1. Subtracting its target period gives

\[
 a_{12}-\Pi_{c+12}\lambda
 =\left(0,\,7c+84+4L_0-3L_1\right)^t.
\]

After exponentiation in the original C* direction, the scalar is therefore

\[
 G(t)=C\,e^{14\pi ic}\frac{t^4}{(t-1)^3}
     =C\,u^{-7}\frac{t^4}{(t-1)^3},\qquad C\in\mathbb C^*.
\]

The same formula applies to the closing map F12,c0−12 for six positive w-loops, because e^{14πi(c0−12)}=e^{14πic0}. It is a formula for the closing isomorphism between the two glued fibres in their local charts, not by itself a calculation of the parallel-transport monodromy.

On the first finite filling the logarithmic comparison divides G by t^4, leaving the unit C u^−7/(t−1)^3. On the second it multiplies G by (t−1)^3, leaving C u^−7 t^4. At the cusp the remaining scalar has a simple pole. In the fan notation this is checked without any asymptotic convention:

\[
 q_{12}-B_0(-7,-18)^t=(-18,6)^t-(-18,7)^t=(0,-1)^t.
\]

Thus after removing the full integral periods there remains the toric transformation x2↦t_c^−1 x2, up to a holomorphic nonvanishing unit. It extends as an integral fan translation, as R2 requires. It is not multiplication by a scalar whose logarithmic modulus extends continuously to the cusp.

An earlier scratch calculation erroneously took the γ coefficient as −42 by forgetting that the γ period's first entry is 6μ. The correct coefficient is −7, and the residual exponent is −1. Only the corrected calculation is used here; the earlier numbers were reported to the root and explicitly corrected.

## What quotienting by the circle does establish

On the ordinary prequotient M×, a Hermitian norm identifies M×/S1 with a positive-real line torsor. The map uφ on this quotient depends on |u| and the norm of φ, so changes of arg u disappear there. The cusp deck action likewise changes only by the δ-circle phase as Re(c) varies, so its local quotient has a constant description. On a finite overlap, however, the exact difference σj,c+Δ−σj,c=Δ εj(log sj)/(2πi)e has imaginary part −Δ εj log|sj|/(2π). This is a genuine radial translation and is retained by quotienting by S1.

Over annuli such positive-real cocycles can be solved by smooth partitions of unity. This addresses the ordinary finite overlaps. It does not make the above cusp transition a bounded positive-real gauge. Its log modulus has the nonzero term −log|t_c|. The elementary proposed interpolation t_c^−r, 0≤r≤1, is not an original integral fan automorphism; taking only its positive modulus does not by itself prove a continuous, let alone smooth, extension across the central toric strata.

Consequently a proof that the quotient family is globally a product must construct an actual smooth quotient isotopy absorbing this residual cusp translation, including both triple points and the fixed double curve. Alternatively it must supply a different global construction with the same endpoint. The fine-sheaf argument for bounded scalar functions on B does not supply it. The local circle quotient calculation alone therefore does not establish 6[Φ]=0 or [Φ]∈{0,14}.

If such a quotient trivialization is constructed, one must still verify that the lifted endpoint gauge extends with the correct smooth behaviour at the fixed S2. On the free complement its circle-valued multiplier lifts to a real function because the complement is simply connected (codimension four in S6); extension at the fixed set is an additional local statement. No distinction between 0 and 14 has been obtained by this calculation.

## Verification and literature scope

All displayed transformation identities and the lattice/fan residual were independently verified in exact SymPy arithmetic in code/d_push_monodromy.py; its complete output is code/d_push_monodromy.out. The derivation checks the exact formulas of the attached R2 construction and the original τ, μ, β transformation laws. It uses no unverified global quotient trivialization.

A web search for smooth Dehn twists on T*S3 and exotic sphere mapping classes was tried as an alternative route. Its returned sources concerned several different twist constructions and did not identify this actual cusp transformation; no theorem from those results is asserted or applied. Search record: turn64search0–turn64search39 and turn64academia30–33. A local analogy with a Dehn twist is not being promoted to a global identification.


## Subsequent source comparison and clarification

The E agent's source audit identified the simpler known formula in DGKX version 1: b_{h,c}=−h Π_c gamma/12+(h ell−h²/24)e, ell=(2πi)^−1 log(F/G), F³=t,G⁴=t−1. Its h=12 scalar representative is exactly t⁴/(t−1)³; the earlier factor u^−7 is absorbed by the allowed parameter-dependent scalar automorphism. The full proof and finite/cusp comparisons are now sections/C_closing_cocycle.tex, Proposition C.3.5, independently checked by code/d_push_closing.py/.out.

The earlier discussion of the cusp pole must be read as an obstruction only to a bounded scalar gauge with first coordinate zero. The actual cusp map has a holomorphic two-coordinate torus-unit representative and is locally isotopic to the identity in that larger group. It is therefore not an intrinsic obstruction to an arbitrary smooth quotient isotopy. The remaining exact issue is patching the ordinary scalar isotopy with the cusp torus-unit isotopy: their logarithms differ on the overlap by one gamma period, whose fractional multiples do not vanish during interpolation. No order bound follows from the pole alone.

The finite scalar formulas in the earlier simplified display assume s1³=t and s2⁴=t−1. With the fixed original root coordinates retained, the exact formulas are K(t)/s1^12 and K(t)*s2^12, respectively. The extra coordinate units remain holomorphic and nonvanishing and do not alter their orders. C.3.5 retains these units explicitly.
