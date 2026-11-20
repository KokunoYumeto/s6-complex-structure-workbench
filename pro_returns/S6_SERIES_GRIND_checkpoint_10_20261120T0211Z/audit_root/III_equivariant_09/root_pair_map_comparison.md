# Exact comparison of the two frozen Borel maps

Root reviewer: GPT-6 Astra, ChatGPT Pro mode; inherited reasoning effort, no separate numeric setting exposed. This comparison follows root's complete reading of both frozen derivations. It adds no before-reading claim. The actual collar comparison is still with the two branch reviewers when this note is written.

The corrections freeze is `audit_corrections/III_equivariant_09/independent_full_derivation.md`, SHA256 `2f0e2955c56447e6e5f9d81184ab0ce02bae85cc75be00c50d32776154faf47c`. The sign freeze is `audit_sign/III_equivariant_09/statement_first_derivation.md`, SHA256 `b8ebe13a13fd8caea0fc942167a7c277becf7eb4486ddfa2b966bd1217b69724`. Root read both complete files and the printed D44.2–4 and D.WI6–13 mechanisms.

## The actual homeomorphism of the two comparison spaces

Write the free circle action on the supplied embedded sphere as a left action and choose its explicit Hopf coordinate

\[
v(\alpha,\beta)=(\overline\alpha,\beta).
\]

For the actual action `(alpha,beta) -> (s^-1 alpha,s beta)`, this coordinate satisfies `v(s n)=s v(n)`. It is a diffeomorphism of the unit three-sphere, with its orientation sign retained when an integer is used. Both branch results need only parity at this step.

The sign review uses

\[
W=(N\times D^2)/((n,z)\sim(sn,sz)).
\]

For `z != 0`, write `z=t h` with `t=|z|` and `h in S1`. The map

\[
[n,z]\longmapsto\left[h^{-1}n,\;r=\frac2\pi\arccos t\right]
\]

identifies `W` with the mapping cylinder of `N -> N/S1`, whose ordinary boundary is `r=0` and whose quotient end is `r=1`. At `z=0`, the circle orbit of `n` is precisely the equivalence relation at the quotient end. The inverse away from that end is

\[
[n,r]\longmapsto[n,\cos(\pi r/2)].
\]

At the quotient end this inverse is `[n,0]`, independent of the orbit representative. The two maps are continuous on the displayed quotient spaces and are mutually inverse. Compactness and the Hausdorff quotient descriptions also give the extension across the collapsed end. Under this homeomorphism the boundary identification is exactly `[n,z] -> z^-1 n` for `|z|=1`.

The sign Borel map becomes

\[
[n,r]\longmapsto
\left[n,\left(\cos(\pi r/2),\sin(\pi r/2)v(n)\right)\right].
\]

This is the corrections mapping-cylinder formula, coordinate for coordinate. Thus these are two descriptions of the same map of pairs, including its ordinary-fibre boundary and derivative action on the pulled-back tangent bundle. The displayed conjugations give the exact morphism relating the two constructions.

## Integer characteristic evaluation and its ambiguity

The map of collapsed spaces is

\[
W/N\longrightarrow\mathbb{CP}^2,\qquad
[n,z]\longmapsto[z:\sqrt{1-|z|^2}\,v(n)].
\]

Away from `[1:0:0]`, a unit representative `(Z_0,Z')` gives the inverse `[v^-1(Z'/||Z'||),Z_0]`. Multiplication of the unit representative by a common phase is exactly the defining diagonal relation in `W`. The collapsed boundary maps to the omitted point. Its degree is therefore a unit, with sign fixed by the chosen Hopf orientation; the pullback of the square of the degree-two generator evaluates as that unit.

The two complete low-degree integral arguments agree. The Gysin presentation writes the kernel of ordinary restriction as `t H2_S1(X)`, with `H2_S1(X)` free. The Serre-filtration presentation writes the same degree-four kernel as an extension of `Z^15` by `Z`. The fixed tangent roots `2x,-x+t,-x-t` give equivariant spin characteristic `t^2`. The even rational cohomology and localization eliminate the rational kernel, and the displayed integral free group eliminates the remaining torsion in this difference. Thus the calculation retains the integral identity, rather than inferring it from a division of the ordinary Pontryagin class.

A chosen global stable frame gives a relative lift of this characteristic class. Its difference from the base class lies in the image of `H3(X;Z)=Z/8`. Pullback to `H4(W,N;Z)=Z` is zero on that image. This identifies the relative integer with the unit evaluation just computed. It proves the odd global-versus-descending clutch with the actual relative map.

## The two frame descriptions

In the complex left Lie frame the scalar derivative acts on the two nonconstant coordinates by `D2(s)=diag(s^2,s^-2)`. The local Bott matrix `A2` satisfies `A2(sn)=D2(s)A2(n)`. Consequently the frame obtained by multiplying the Lie frame by `A2` is invariant as a frame and descends to the orbit quotient. This is the quotient-descending frame of the sign construction, up to a bundle automorphism over `S2`; the latter has a nullhomotopic stabilized spin gauge because `pi2 Spin=0`.

The corrections matrix `A1` has `A1(sn)=D1(s)A1(n)`. Therefore `C=A2 A1^-1` obeys

\[
C(sn)=D_2(s)C(n)D_1(s)^{-1}.
\]

It is the actual bundle map to the weight-one representation, with degree `4-1=3`. The reference frame and this weight-one frame differ by `A1^-1`, of odd degree. The sign relative Hopf map computes this same parity through a unit relative characteristic evaluation. The rank-three normal change has stable index two, as follows from the adjoint roots `2x,0,-2x` and `lambda(ad)=-2 c2(fundamental)`.

The receiving collar must still identify the local abstract kernel and target frames with the global reference. Fixing the nonzero abstract delta section reduces the remaining kernel frame changes to the quotient complex line and contractible choices of lifts. A quotient-line frame change is a map to `C*`, whose restriction to `S3` has zero degree-three homotopy class. Target-line changes have the same property, and splitting choices are affine. The geometric collar review must establish that these are the actual bundles and maps; the argument here specifies the exact remaining frame comparison rather than assigning it by notation.

## Source-reading scope

Root freshly opened Atiyah–Bott's original journal scan at section2, printed pp2–3, and section3 Lemma3.3, Proposition3.4, Theorem3.5 and the circle specialization, printed pp7–8: <https://www.math.stonybrook.edu/~mmovshev/MAT570Spring2008/BOOKS/atiyahbott_moment.pdf>. The source supplies characteristic-zero localization for the compact smooth circle action. The integral filtration arguments above are the displayed branch derivations.

Root freshly opened Bott's original journal scan at TheoremII and periodicity corollary(1.5), printed pp314–315, including the entire stable orthogonal period: <https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/bott.pdf>. These exact low homotopy groups give the obstruction range used on the six-dimensional mapping-cylinder union. No complete rereading of either source is claimed.

No manuscript, mathematical status or whole-row completion is changed by this note.
