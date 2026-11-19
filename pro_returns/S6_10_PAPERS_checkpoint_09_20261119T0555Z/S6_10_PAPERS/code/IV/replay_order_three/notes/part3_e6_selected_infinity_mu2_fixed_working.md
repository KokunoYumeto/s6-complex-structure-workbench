# Fixed strata of the actual two-torsion quotient resolution

This calculation uses the resolved quotient maps in
part3_e6_selected_infinity_mu2_root_working.md. It supplies the compact
fixed-point terms and the exceptional curves inside the fixed surfaces.
The remaining global fixed-surface characteristic terms are not assigned.

## The two compact stabilizer curves and their normal bundle

Keep the entire ordinary chain before taking its period quotient. Its
actual transition is
\[
 X_{j+1}=Y_j^{-1},\qquad Y_{j+1}=X_jY_j^2.
\]
At either of the two source points \(\bar X=\pm i,\bar Y=0\),
the order-two stabilizer fixes the \(Y_j\) axis for odd \(j\),
and the \(X_j\) axis for even \(j\). Consequently the compact
fixed curves are assembled from an odd chart \(j\) and its next
even chart \(j+1\). Write \(u=Y_j\) and \(u'=X_{j+1}\).
Their two affine axes glue by \(u'=u^{-1}\), giving an actual
\(\mathbb P^1\). The odd normal coordinates satisfy
\[
 (\chi',\zeta',Y_{j+1})=(\chi,\zeta,u^2X_j).
\tag{MF2a}
\]
Here the source coordinates do not change: the chain transition fixes
\(\sigma=X_jY_j\), and therefore the same implicit root \(\bar X\)
and coordinate \(\zeta=\bar Y\) are used. Formula MF2a is the
literal normal-coordinate arrow. With the convention that a fibre
coefficient for \(\mathcal O(n)\) transforms as \(u^{-n}\), it
identifies the cover normal bundle with
\[
 N=\mathcal O\oplus\mathcal O\oplus\mathcal O(-2).
\tag{MF2b}
\]
The physical circle acts on \(u\) with weight \(-1\), on \(u'\)
with weight \(+1\), on \(\chi,\zeta\) with weight zero, and on
the third normal coordinate with weights \(+1,-1\) at these two
endpoints. This equivariant structure follows by substituting MF2a;
its two fibre weights differ by the displayed exponent two.

One period shifts the chain index by four and exchanges the two source
points. The fourth-root arrow exchanges those points and preserves the
chain index. Taking one source point as representative consequently uses
the exact closing map \(\gamma^{-1}B\). The two compact curves can be
represented by \(j=1,2\) and \(j=3,4\). No nonzero period shift
stabilizes either of these whole curves in the infinite chain: its
index changes by a nonzero multiple of four. The remaining order-two
stabilizer fixes the curve pointwise and is exactly the involution already
used in the coarse resolution. Thus the quotient contains two such
compact base curves. The formulas below retain the complete closing
arrow when a period fundamental region uses chart zero instead of four.

The exceptional divisor over either curve is \(\mathbb P(N)\), where
\(\mathbb P\) parametrizes lines, and its radial normal line is the
square of the tautological line. Indeed the cover blowup has a vector
\(t z\) in the tautological line, and the quotient coordinate is
\(\rho=t^2\). This is an explicit bundle morphism and recovers the
quadratic-invariant coarse blowup in the preceding note.

## Physical fixed loci in the three quotient charts

At a chain node write \(\ell\) for its odd line coordinate and
\(u\) for its neutral line coordinate. Their physical weights are
\(w,-w\), where \(w=+1\) for odd \(j\) and \(w=-1\) for even
\(j\). The other odd coordinates are \(\chi,\zeta\), both of
physical weight zero. In the \(\ell\)-pivot chart the coordinates
\[
 (\rho=\ell^2,\ z_\chi=\chi/\ell,
 z_\zeta=\zeta/\ell,\ u)
\]
have weights
\[
 (2w,-w,-w,-w).
\tag{MF2c}
\]
All four are nonzero. The coordinate origin is therefore an isolated
fixed point, and it is the only fixed point of this chart. There is one
such point at each of the four node indices modulo the actual period.
The fourth-root source arrow identifies the two source copies at the
same node; it does not change the node index. Hence this yields exactly
four isolated fixed points in this part of the quotient atlas.

In the \(\chi\)-pivot chart put
\[
 (\rho=\chi^2,z=\zeta/\chi,a=\ell/\chi,u).
\]
The physical weights are \((0,0,w,-w)\). The full fixed locus in
this chart is the surface \(a=u=0\). The \(\zeta\)-pivot chart
gives its other chart, and their exact overlap is
\[
 \rho'=\rho z^2,\quad z'=z^{-1},\quad a'=a/z,\quad u'=u.
\tag{MF2d}
\]
The fixed surface is therefore the total space of
\(\mathcal O_{\mathbb P^1}(-2)\) in this local source
neighbourhood. Its zero section \(C\) is the complete exceptional
\(\mathbb P^1\). The two physical normal lines restrict to
\[
 \mathcal O_C(1)_{w}\oplus\mathcal O_C{}_{-w}.
\tag{MF2e}
\]
This assertion uses the actual transition \(a'=a/z\) in MF2d,
and the unchanged coordinate \(u\); it does not infer a degree from
weights alone. There are four such surface patches at the four node
indices. Each continues through the ordinary source charts. Their global
compactification and boundary doubles belong to the global surface
ledger. The curves \(C\) lie in these fixed surfaces and do not
constitute additional one-dimensional components of the fixed locus.

## Entire source mixing and the representative closing map

Retain the complete chord coefficients \(A_b,B_b\), so that
\(\zeta_{\rm new}=A_b\zeta+B_b\sigma\), and the complete genuine
line unit \(\mathcal C=\lambda H\mathcal B_{a,b}\). In this
paragraph write \(s=+1\) at an odd node, \(s=-1\) at an even
node. Thus \(\ell_{\rm new}=\mathcal C^s\ell\),
\(u_{\rm new}=\mathcal C^{-s}u\). On the \(\chi\)-pivot chart
the whole source reset is
\[
 \rho_{\rm new}=\rho,\quad
 z_{\rm new}=A_bz+B_bau,\quad
 a_{\rm new}=\mathcal C^s a,\quad
 u_{\rm new}=\mathcal C^{-s}u.
\tag{MF2f}
\]
In particular the source mixing is retained. It is quadratic in the two
physical normal variables along the fixed surface, and thus the induced
linear normal arrow is precisely the displayed pair of line factors.

Let \(e_\ell,e_u\) be the actual fourth-root exponents of \(\ell,u\).
They are \((j,-j-1)\) at odd \(j\) and \((-j-1,j)\) at even
\(j\). The exact representative change \(\gamma^{-1}B\) in
MF2f is
\[
 \rho'=-\rho,\quad z'=-A_bz-B_bau,\quad
 a'=i^{1-e_\ell}\mathcal C^s a,\quad
 u'=i^{-e_u}\mathcal C^{-s}u.
\tag{MF2g}
\]
Every coefficient is evaluated at the actual source point before the
specified arrow. The full inverse is obtained from the inverse chord,
inverse line unit, and inverse fourth-root arrow. On the exceptional
curve, \(A_b=1\), so its projective map is literally \(z'=-z\).
Its full neighbourhood map remains MF2g. The source parameter square is
also exact: \(\sigma'=i\sigma\), \(\chi'=-i\chi\), and hence
\(\epsilon'=\chi'\sigma'=\epsilon\).

For completeness, in the \(\ell\)-pivot chart the source reset is
\[
 \rho_{\rm new}=\mathcal C^{2s}\rho,\quad
 z_{\chi,{\rm new}}=\mathcal C^{-s}z_\chi,\quad
 z_{\zeta,{\rm new}}=\mathcal C^{-s}(A_bz_\zeta+B_bu),\quad
 u_{\rm new}=\mathcal C^{-s}u.
\tag{MF2h}
\]
Composing with the inverse fourth-root phases multiplies these four
coordinates by \(i^{-2e_\ell},i^{e_\ell-1},i^{e_\ell+1},
i^{-e_u}\), respectively. This map preserves the isolated origin
and its full physical representation MF2c. Equations MF2f--h are
compatible with MF2d by substitution of the actual variables. They
supply the source, line and representative maps used to count the
compact components.

## Original volume and the isolated-point residue

Use the full source differential unit \(u_{\rm src}\), whose central
value is \(-1/2\), and the original volume from the previous note,
\[
 -8(X_jY_j)^3d^{-2}u_{\rm src}
       d\chi\wedge d\zeta\wedge dX_j\wedge dY_j.
\]
Substituting the explicit \(\chi\)-pivot coordinates gives exactly
\(-4w d^{-2}u_{\rm src}\rho^2a^3u^3\,
d\rho\wedge dz\wedge da\wedge du\). The factor \(w\) retains
the coordinate permutation between the odd and even chain charts.
The three divisor orders are therefore \(2,3,3\). Their degrees
on \(C\) are \(2(-2)+3(1)+3(0)=-1\). This agrees with
\(\deg K_W|_C=-1\), computed from \(\deg T F|_C=2-2=0\)
and the degree one normal pair MF2e. Thus the inherited divisor and
the exact normal arrows give the same adjunction identity.

For the positive-hyperplane variable of SZ.57--59, an isolated point
with actual weights \(w_i\) contributes
\[
 R_u=\frac{4-\sum_i w_i^2}{24\prod_i w_i}.
\]
Substitution of MF2c gives \(\sum_iw_i^2=7\),
\(\prod_iw_i=-2\), and therefore \(R_u=1/16\) at each of
the four points. Their sum in this specified polynomial is \(1/4\).
The complete boundary calculation still carries its actual generator
arrow to the physical line and its inner/outer boundary orientation.
No physical total, surface contribution, or return class is assigned
by this local sum.

The companion program
code/part3_root/e6_selected_infinity_mu2_fixed.py verifies all four
node representations, both actual normal-bundle transitions, the
whole source-mixing chart square, the representative phases, the
marked-volume divisor and the rational point terms exactly.
