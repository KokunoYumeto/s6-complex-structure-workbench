# A valuation-one coordinate on a simple elliptic hypersurface

**Proved.** The complete intrinsic derivation has passed both root and independent checks audits.

Let \((V,0)\subset(\mathbb C^3,0)\) be an isolated normal
hypersurface germ whose minimal resolution \(\pi:\widetilde V\to V\)
has sole exceptional curve a smooth elliptic curve \(H\).
Write \(d=-H^2>0\). Let \(r\) be a fixed analytic ambient
coordinate whose restriction has \(\operatorname{ord}_H(r)=1\).
Then \(d\) is one of \(3,2,1\). In analytic ambient
coordinates retaining this exact \(r\), the divisorial orders
and the weighted leading degree of the defining equation are
respectively
\[
 (1,1,1;3),\qquad(1,1,2;4),\qquad(1,2,3;6).             \tag{SEW.1}
\]
The weighted leading equation defines the actual smooth elliptic
curve \(H\) in the corresponding weighted projective plane.
The coordinate changes needed below are linear changes preserving
\(r\), followed, only in the last case, by subtracting a
constant multiple of \(r^2\) from the third coordinate.
Their exact descent through the specified blowdown chart is
given in Section 5.

This proves the required valuation form intrinsically. It does
not replace the given defining function by a right-equivalent
weighted homogeneous function, nor discard its higher terms.

## 1. Analytic formal functions and the exact associated graded ring

Put \(L=\mathcal O_H(-H)\), of degree \(d\), and
\[
 I_m=(\pi_*\mathcal O_{\widetilde V}(-mH))_0
     =\{a\in\mathcal O_{V,0}:\operatorname{ord}_H(a)\ge m\}.
\]
For \(m\ge1\), the restrictions of
\(\mathcal O(-mH)\) to successive infinitesimal neighbourhoods
of \(H\) have graded factors \(L^{m+j}\), \(j\ge0\).
Each has zero first cohomology, by Serre duality on the elliptic
curve and its strictly positive degree. Their extensions also
have zero first cohomology.

The analytic formal-functions theorem is Grauert1960,
Section6, Hauptsatz IIa, printed p.59; Hauptsatz I on the same
page supplies coherence. The maximal-ideal pullback and the
ideal of \(H\) have the same radical. On a finite cover of
the compact exceptional curve, Noetherianity gives one uniform
power of the latter contained in the former. Their powers are
therefore cofinal. Applying the theorem with
\(\mathcal O(-mH)\) gives a zero completion for
\(R^1\pi_*\mathcal O(-mH)\). This coherent module is
supported at the origin, so it is zero. Consequently
\[
 I_m/I_{m+1}\simeq H^0(H,L^m)\qquad(m\ge1),             \tag{SEW.2}
\]
through the actual restriction maps in
\[
 0\longrightarrow\mathcal O(-(m+1)H)
 \longrightarrow\mathcal O(-mH)
 \longrightarrow L^m\longrightarrow0.
\]
These maps respect multiplication. Since normality gives
\(\pi_*\mathcal O_{\widetilde V}=\mathcal O_V\), and a
function vanishes at the contracted point exactly when its
restriction to \(H\) vanishes, \(I_1=\mathfrak m\).
The degree-zero piece is \(\mathbb C\). Thus
\[
 \operatorname{gr}_{I}\mathcal O_{V,0}
   =\bigoplus_{m\ge0}H^0(H,L^m)                         \tag{SEW.3}
\]
as graded algebras, not only as vector spaces.

The same formal-functions theorem in degree zero identifies
\[
 \widehat{\mathcal O}_{V,0}
      \simeq\varprojlim_m H^0(mH,\mathcal O_{mH})
      \simeq\varprojlim_m\mathcal O_{V,0}/I_m.          \tag{SEW.4}
\]
The second equality uses the just-proved first-direct-image
vanishing. This supplies the exact completeness and separation
needed in Section 4; no unproved equivalence between a
divisorial and an ordinary degree filtration is being used.

Because \(\mathfrak m^2\subset I_2\), (SEW.2) gives a
surjection
\(\mathfrak m/\mathfrak m^2\to H^0(H,L)\).
The source has dimension three and the target dimension \(d\).
Hence \(d\le3\).

## 2. The three section rings and their actual elliptic curves

For \(d=3\), Riemann--Roch shows that \(L\) separates
points and tangent vectors: subtracting any length-two
subscheme leaves a degree-one line bundle with one section.
The complete linear series therefore embeds \(H\) as a smooth
plane cubic. The restriction sequence on \(\mathbb P^2\),
using \(H^1(\mathbb P^2,\mathcal O(k))=0\), gives its whole
section ring as
\[
 \mathbb C[x,y,z]/(F_3),\qquad \deg(x,y,z)=(1,1,1),
\]
where \(F_3=0\) is that smooth cubic.

For \(d=2\), the complete pencil is base-point free and gives
a degree-two map \(p:H\to\mathbb P^1\), with
\(L=p^*\mathcal O(1)\). Trace splits
\(p_*\mathcal O_H=\mathcal O\oplus B^{-1}\).
Its Euler characteristic is zero, so \(\deg B=2\).
The algebra structure is therefore a double-cover equation
\(z^2=F_4(x,y)\), where the binary quartic has four distinct
zeros because the double cover is smooth. Projection formula
gives the entire section ring with generator weights
\((1,1,2)\) and that single degree-four relation.

For \(d=1\), write \(L=\mathcal O_H(p)\).
Riemann--Roch gives a degree-one section \(x\), one new
degree-two section \(y\), and one new degree-three section
\(z\). Dividing by powers of \(x\) gives functions of pole
orders two and three at \(p\). Their Weierstrass relation
has weighted degree six. Equivalently, after graded changes
only for describing this section ring, it is
\[
 z^2=y^3+A x^4y+B x^6,
 \qquad 4A^3+27B^2\ne0,
 \qquad\deg(x,y,z)=(1,2,3).
\]
The pole-order count shows that the monomials with at most one
factor \(z\), reduced by this relation, give every space
\(H^0(H,L^m)\). Thus this is the whole section ring. Its
weighted projective curve is the actual smooth \(H\).
The coordinate choice below does not require completing the
square or applying any of these optional graded simplifications.

## 3. Retaining the given coordinate using only permitted changes

Start with analytic ambient coordinates \((r,u,v)\), retaining
the given \(r\). Their images form a basis of
\(\mathfrak m/\mathfrak m^2\). The map to
\(I_1/I_2=H^0(L)\) has the rank just computed.

When \(d=3\), it is an isomorphism, so any linear complement
to \(r\) supplies the other two valuation-one coordinates.

When \(d=2\), choose a linear coordinate \(s\) whose
leading section complements that of \(r\), and choose the
remaining independent linear coordinate \(v_0\) in the
kernel of the degree-one restriction. Thus
\(\operatorname{ord}_H(v_0)\ge2\). Its degree-two leading
section must be independent of \(r^2,rs,s^2\). Otherwise
all degree-two initial sections of analytic functions would
lie in that three-dimensional span: a Taylor expansion shows
that every term of ordinary order at least three has valuation
at least three, and the linear terms of valuation two are
accounted for by \(v_0\). This contradicts
\(h^0(L^2)=4\). Therefore \(v_0\) has valuation exactly
two and is the required indecomposable degree-two generator.
The coordinates \((r,s,v_0)\) were obtained by an invertible
linear change.

When \(d=1\), first choose two independent linear coordinates
\(u_0,v_0\) in the kernel of the degree-one restriction.
At least one linear combination, denoted \(s\), has a
degree-two initial section independent of \(r^2\), since
\(h^0(L^2)=2\). Choose the remaining independent linear
coordinate \(v_1\), and subtract a scalar multiple of \(s\)
so that its degree-two initial term is \(\alpha r^2\).
Set
\[
                         v_2=v_1-\alpha r^2.
\]
This is a triangular analytic coordinate change, and
\(\operatorname{ord}_H(v_2)\ge3\). Its degree-three
initial section must be independent of \(r^3,rs\).
Indeed, if it were absent or in that span, any Taylor series
of valuation three would have degree-three initial section
in that same span: the possible terms are precisely the
linear \(v_2\) term and the weighted-degree-three monomials
\(r^3,rs\); its valuation-one and valuation-two terms
must first vanish. This contradicts \(h^0(L^3)=3\).
Thus \(v_2\) has valuation exactly three and supplies the
indecomposable degree-three generator. The three ambient
coordinates remain analytically invertible, because only
an invertible linear change and the displayed quadratic
translation were performed.

This argument proves directly that the chosen analytic
coordinates have the prescribed orders and generate the
graded ring. It avoids a circular appeal to filtered
Nakayama or to a coordinate normalization that might move
the fixed \(r\).

## 4. The actual weighted leading equation

Write the defining analytic equation in the coordinates just
constructed, with the weights in (SEW.1). Its weighted initial
form is the single defining relation of the graded section
ring, up to a nonzero scalar. Here is an explicit proof of that
last assertion.

Let \(F_D\) be the graded relation from Section 2, expressed
in the actual chosen initial generators. The analytic function
\(F_D(r,s,v)\) has valuation at least \(D+1\).
At each successive valuation, (SEW.3) writes its initial
section as a weighted homogeneous polynomial in the three
generators. Subtract that polynomial. This produces a formal
series \(G=F_D+F_{D+1}+\cdots\) whose image in every
\(\mathcal O_{V,0}/I_m\) is zero. Since all generator
weights are at most three, the correction polynomials tend
to zero in ordinary power-series degree; their sum is a
well-defined formal power series. By (SEW.4), its image in
\(\widehat{\mathcal O}_{V,0}\) is zero.

The completed hypersurface ideal is principal, generated by
the actual analytic equation \(f\). Thus \(G=h f\) for
a formal series \(h\). Taking weighted initial forms gives
\(F_D=\operatorname{in}(h)\operatorname{in}(f)\).
The polynomial \(F_D\) is irreducible because its weighted
projective curve is the smooth connected elliptic curve
\(H\). Also \(f\) is nonconstant and vanishes at the
origin. Hence \(\operatorname{in}(h)\) is a nonzero
constant, and \(\operatorname{in}(f)\) is a scalar multiple
of \(F_D\). This proves (SEW.1) for the actual defining
equation, with all higher terms retained.

## 5. The exact descent to the original blowdown coordinates

In the chart with original coordinates
\(x=r u\), \(y=r v\), every change above has the form
\[
 s=a u+b v+c r,\qquad
 v'=a'u+b'v+c'r-\alpha r^2,
 \qquad ab'-a'b\ne0.
\]
It descends to the actual holomorphic coordinate map
\[
 \begin{aligned}
 x'&=r s=a x+b y+c r^2,\\
 y'&=r v'=a'x+b'y+c'r^2-\alpha r^3,\\
 r'&=r.
 \end{aligned}                                        \tag{SEW.5}
\]
Its Jacobian determinant at the origin is \(ab'-a'b\),
so the inverse-function theorem supplies an analytic inverse.
This is the required morphism preserving the original
parameter and blowdown structure.

## 6. Primary-source control

The analytic comparison used in Section 1 was read directly in
Hans Grauert, *Ein Theorem der analytischen Garbentheorie und
die Modulräume komplexer Strukturen*, Publ. Math. IHES5(1960),
Section6, Hauptsätze I, II and IIa, printed p.59. The 1963
corrigendum had already been read in the blind Part5 work.
Primary PDF: `https://www.numdam.org/item/PMIHES_1960__5__5_0.pdf`.

Saito's own 1973 Oberwolfach abstract, printed p.15 of
Tagungsbericht36/1973, was also read in the primary scan. It
states the equations for exceptional self-squares minus
three, minus two and minus one:
\[
 y(y-x)(y-\lambda x)-xz^2,\quad
 xy(y-x)(y-\lambda x)-z^2,\quad
 y(y-x^2)(y-\lambda x^2)-z^2,
 \qquad\lambda\ne0,1.
\]
Their weights agree with the intrinsic derivation above. That
abstract is corroboration, not a substitute for the
\(r\)-preserving argument. The full Saito1974 publisher text
was not accessible in this lookup and is not treated as read.
Primary scan:
`https://oda.mfo.de/bitstream/handle/mfo/1521/full-text.pdf?isAllowed=y&sequence=1`.
