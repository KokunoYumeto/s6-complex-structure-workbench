# The selected-infinity completion and its actual outer transfer

This working proof concerns the original E6 row
\((M_6,b,m,n)=(M_6,1,2,1)\), the retained finite character and
ordinary-to-cap reference, the initial negative-square selected fan,
and one positive full turn of \(\epsilon=w^{-1}\). The original
suspension scalar \(\lambda\) is fixed. All coordinates below are
those of EI, IA, EIR, FO, FL, SS, CS and MC. The fixed-surface cap is
MC's actual product cap. Its second Chern number is retained as the
integer \(\kappa_c=\langle c_2(E_c),[F_c]\rangle\); this proof does
not choose that integer. The outer characteristic expression and
the actual sphere return are obtained without such a choice.

## OT.1. The outer family, source height and scalar word

Put \(d=1-3\epsilon^2\). The complete map from the native source is
\[
\begin{split}
y^2&=x^3+(3\epsilon^2-2)x^2+dt x+\epsilon^2t^2,
       \qquad G=(0,\epsilon t),\\
x_o&=\epsilon^2d^{-2}x,\quad
y_o=\epsilon^3d^{-3}y,\quad
t_o=\epsilon^4d^{-3}t,\quad
r=\epsilon^2(3\epsilon^2-2)d^{-2}.
\end{split}                                                   \tag{OT.1}
\]
It carries the entire cubic, its marked zero and G, and the selected
height
\[
q_o=\epsilon^4d^{-3}q_e,\qquad q_e=t-(1-\epsilon^2).       \tag{OT.2}
\]
The powers in these formulas are retained. In particular the loop
is the full ordered epsilon loop, and the displayed map to the
original r-disc has degree two. No half-turn endpoint is substituted.

On the complementary graph use
\[
\epsilon=\chi\sigma,\quad
(x_e,y_e,t_e)=(\chi^{-2}\bar X,\chi^{-3}\bar Y,\chi^{-4}),
\quad H=1-\chi^4(1-\epsilon^2).
                                                               \tag{OT.3}
\]
The original source map is
\((x_o,y_o,t_o)=(\sigma^2d^{-2}\bar X,
\sigma^3d^{-3}\bar Y,\sigma^4d^{-3})\).
The actual normalized Miller functions and point sections give
\[
f_{a,e}=\chi^{1-a}\bar f_a,\quad
B_{a,b,e}=\chi^{-6}\bar B_{a,b},\quad
\widehat B_e=\chi^{-4}H\,\sigma^{-6}\bar B_{a,b}.
                                                               \tag{OT.4}
\]
Consequently the full Hom coefficients satisfy the literal equality
\[
\lambda\epsilon^4\widehat B_e
 =\lambda\sigma^4H\mathcal B_{a,b},\qquad
\mathcal B_{a,b}=\sigma^{-6}\bar B_{a,b}.                 \tag{OT.5}
\]
The source and target line frames in this equality are carried by
the canonical point-section map: their O parameters and marked-point
parameters both multiply by \(\chi\). Their ratio is therefore
unchanged. The divisor cancellation proving that \(\mathcal B\)
extends as a unit through both O and T is EI.57--64/EIR.10; its
central value is 64. This is an equality of the full line maps,
including their source derivatives. Thus the native scalar
\(\epsilon^4\lambda\) in OT.5 belongs to the coordinate expression
of this fixed-original-scalar family. It is retained on the outer
circle and through the cap map below.

For native and complementary chain charts the entire overlap is
\[
A_jB_j=\epsilon,\quad X_jY_j=\sigma,\qquad
X_j=\chi^jA_j,\quad Y_j=\chi^{-j-1}B_j,
\quad V=\epsilon^jA_j=\sigma^jX_j.                     \tag{OT.6}
\]
Every exponent is an integer. The graph quarter-turn has
\((\chi,\sigma)\mapsto(i\chi,-i\sigma)\); OT.6 gives its
actual phases \((i^j,(-i)i^{-j})\). The full ordinary suspension
has the source translation \(T_b\), index change \(j\mapsto j+4\)
and normal factors
\((\lambda H\mathcal B,(\lambda H\mathcal B)^{-1})\).
These maps commute, since the source and line maps commute and
\(i^{j+4}=i^j\). They are the boundary maps of this particular
original family.

## OT.2. The old cap and the complete finite face ledger

The source-base graph is the proper projective graph of
\(t_o q_{\infty,e}=\epsilon^4d^{-3}\). Its fourth-root chart is
OT.3 with \(t_o=\sigma^4d^{-3}\). The original finite cap occupies
\(|q_{\infty,o}|<\delta\); hence its overlap has large nonzero
\(\sigma\). On logarithmic sectors set
\[
s_o=\frac{\log q_{\infty,o}}{2\pi i}
       =3\ell_d-4v_\sigma,\qquad
v_\sigma=\frac{\log\sigma}{2\pi i}.
                                                               \tag{OT.7}
\]
The quarter-turn sends \(s_o\) to \(s_o+1\). Its original source
point and genuine point-line coefficient are unchanged. The actual
K96 reference cochains, transported without changing their reference,
are
\[
\begin{split}
\Phi_\alpha&=\operatorname{Exp}
 (ns_\alpha f_\alpha+s_\alpha c_\lambda\delta+h_\alpha)I_{z_\alpha},\\
f_\beta&=D_*^k f_\alpha+\Pi_{\alpha\beta},\qquad
s_\beta=s_\alpha+k,\\
h_\beta-D_*^k h_\alpha
 &=-ns_\alpha\Pi_{\alpha\beta}
       +j_{\alpha\beta}\operatorname{Log}_\beta B
       +\Lambda_{\alpha\beta}.
\end{split}                                                   \tag{OT.8}
\]
Their extending maps obey
\[
\Phi_\beta=A^kB^{j_{\alpha\beta}}\Phi_\alpha,
\quad \Phi_\alpha B=B\Phi_\alpha,
\quad A^m=B^n.                                             \tag{OT.9}
\]
Here A includes its scalar root, finite character and line lift.
Thus the graph quarter-turn on the root groupoid is
\(AB^{j_\gamma}\), and the four-step word is
\(A^4B^{\sum j_\gamma}\), with the four actual sector integers.
Its inverse is the endpoint-to-initial arrow. The original cap
quotient identifies these deck words, while its root atlas retains
them literally. These formulas prove the closing square for OT.1--6;
they do not replace the word by the bare root-coordinate deck.

The complete gluing has the following finite charts and faces.

| Regions | Full map on their common face |
|---|---|
| Native finite source and complementary source | IA.3--13, including \((a,\epsilon b_0,\epsilon^2)=(b_0,\epsilon)^2\), both Rees charts, and the reciprocal chord map |
| Native and complementary line chain | OT.6 and its inverse, with the unchanged coefficient V |
| Ordinary O/T graph and selected graph | FO's common 38-cone interface, its 238- and 39-cone extensions, with every source unit and normal monomial |
| Selected factor chart and genuine ordinary point frame | \(X_k=\psi^{-1}q^{j_{\rm per}}s_r\), \(Y_k=\psi q^{-j_{\rm per}}t_r\), \(k=4j_{\rm per}+r-1\) |
| The two source graph charts | \(p=1/v\), \(\eta=\sigma p\), the full point-module map, and the actual additive central reset O:p to T:p-b and T:p to O:p-b |
| Complementary graph and old exterior | OT.3--5 in the original variables, with the genuine Cartier map and its inverse |
| Old exterior and finite cap | OT.8--9 on the actual old cap domain |
| Ordinary finite quotient strata | The 238 quotient charts and the separate two-torsion fixed-ideal blowups, with their original volume characters and \(\gamma^{-1}B\) squares |

All unit functions in this table are the full analytic functions
specified in EI/FO/IA. For example the selected coefficient is
\(C=\lambda\beta/\kappa\), and
\(\beta=\mathcal B\,\psi(T_bp)/\psi(p)\), while \(q=\kappa H\).
This is the square relating the selected and ordinary normal maps.
The monomial \(q^{j_{\rm per}}\) is retained also at q zero. On the
representatives used by the compact normal stars \(j_{\rm per}=0\),
and the full divided-difference calculation CS.10a proves
\(\psi=1\) on each component even at its point/O intersections.
The internal four sigma factors keep their distinct labels.

The common subdivisions are proper: their primitive cones have
the same support as their factor parents, and the monomial maps
are the charts of the closed projective graph of all consecutive
factor ratios. The source graph is proper by its displayed Rees
ideals. The finite quotient resolutions are proper equivariant
modifications. Each map is an isomorphism on the prescribed outer
punctured-parameter family. On triple overlaps the full source,
line and cap morphisms agree on their dense ordinary domains;
their holomorphic extensions in the written regular charts give
the same equality everywhere on those overlaps.

Here is the compactness check retaining the period action. On the
selected bidisc the logarithmic norm matrix is
\[
\begin{pmatrix}L_q&-bL_P\\aL_P&4L_\sigma+L_q+L_C\end{pmatrix},
\qquad
\det=L_q(4L_\sigma+L_q+L_C)+abL_P^2>0.                 \tag{OT.10}
\]
Choose the fixed nonzero original scalar small enough for the
uniform strict contraction in IA.1, on the closed chosen charts.
Putting the two real period coefficients in \([0,1]\) bounds
\(Z,q/Z,V,\sigma^4q/V\) by the explicit constants IA.2. The
angles are compact. The projective factor graphs are proper over
these bounded coordinate boxes. On the ordinary chart the source
is the compact elliptic source atlas, and the line period shifts
four consecutive chain labels with the full bounded unit in OT.5.
At a vanishing source or line coordinate the consecutive source
and line charts in the table retain that same index change.
No nonzero index word stabilizes one of these bounded chart cells.
At the original exterior and cap this is the already extending
K96 quotient on its actual domain. These finite local fundamental
regions cover the compact projective source-base graph. Their
closures, with the proper source and factor exceptional fibres,
are compact. The same norm bounds and index changes show that a
compact chart meets only finitely many period translates. Hence
the glued cut is Hausdorff and proper, and no artificial cut face
is left unpaired.

Denote by W the resulting oriented real eight-dimensional cut
over a small closed epsilon disc, with its corners rounded using
invariant collars. Its only outer boundary is the original
fixed-scalar epsilon family, through OT.1--9. Its circle fixed set
is precisely the minimal-face orbit list FL/CS/SS, together with
the moving surface MC.5. The O/T labels are kept separately:
\(B:(C,j)\mapsto(\operatorname{other}C,j+4)\) has two orbits
for every j modulo four. The two-torsion fixed-ideal resolution is
included once through its actual \(\gamma^{-1}B\) map. Thus the
two ordinary copies and the four global strict surfaces have the
different multiplicities recorded by their actual period orbits.

## OT.3. The selected tube and the physical reference cap

The moving surface is the actual
\(F=\operatorname{Bl}_{(O,0),(T,0)}(\mathbb P^1\times D)\)
of MC.1. Its normal charts are
\[
q=Za_Nc_N,\quad Z'=Z^{-1},\quad (a'_N,c'_N)=Z(a_N,c_N),
\quad (a_N,c_N)=(\sigma^{-4}t_N,\sigma^4s_N).
                                                               \tag{OT.11}
\]
In the q-factor representative the first factor in the last
pair is instead \(Z^{-1}\sigma^{-4}t_N\), with overlap
\(t_y=Z^{-1}t_q\), \(s_y=s_q\). These equations retain q
literally and retain the complete source derivative of Z.
The full completed-point to original-tensor normal map is
\[
(\overline{t_N},s_N)\longmapsto
\left(
 \overline{\epsilon^4d^{-3}H_o^{-1}\sigma^{-4}}\,
          \overline{t_N},
 H_o\sigma^4s_N
\right),\qquad
H_o=\frac{\epsilon^{-a}d^{a-1}}{C_a(\epsilon)}.          \tag{OT.12}
\]
The q-factor first entry also has \(\overline Z^{-1}\).
For a=6 the two phase windings in OT.12 are -6 and -2,
and their determinant winding is -8. Their entire unit factors
remain in the map. The determinant extension over the reference
cap keeps this integer by extending \(e^{in\theta}\) along its
S1 factor; it does not extend that phase across a parameter disc.

The fixed-sphere base map is MC.2, \(S=(\epsilon/d)s\).
On the actual cap \(C_0=-D^3\times S^1\), its extension is
\[
Y\longmapsto AYA^*/\operatorname{tr}(AYA^*),\qquad
A=\operatorname{diag}(\epsilon/d,1),                  \tag{OT.13}
\]
on trace-one positive semidefinite Hermitian matrices. Its inverse
uses \(A^{-1}\). This map acts on the fixed-sphere base. In this
product extension hold the transported Cox quaternion fixed and
apply the written physical Hopf phase of OT.11--12. On the normal
Hopf sphere use the actual K68 map
\(Q(a,c)=(\overline c,-\overline a)\) and its stated inverse.
The resulting normal-sphere-bundle map covers OT.13. Its fibre
map and base map concern these two specified spheres. In
particular this construction uses the displayed product map,
not the derivative of the Möbius map on the fixed base.

Attach the resulting \(C_0\times D^4\) bundle along the fixed
tube on the outer boundary. Equivalently replace
\(S^2\times D^4\) by \(D^3\times S^3\) there using exactly
OT.11--13 and the K68 Hopf lift. This closes F to MC's \(F_c\)
and makes the outer circle action free. All other fixed components
remain in the interior. The determinant is zero integrally by
MC.18--21: the literal map
\(H^1(C_0)\to H^1(S^2\times S^1)\) is minus the identity,
and the restriction of \(c_1(E_c)\) to F is zero. Its entire
SU2 clutch is retained, defining the actual integer \(\kappa_c\).

For completeness the outer orbit hypotheses are carried by the
actual E6 reference maps EC.25a--c. The interval of full source,
Cartier, norm and cap maps connects each outer fibre to the F41
sphere. Its physical action has the single standard selected
fixed S2 and is free elsewhere: the primitive fan weights and
the strictly contracting primitive cap generator give that
statement on every original chart. Removing the fixed tube E
gives \(H_*(E)=H_*(S^3)\), \(\pi_1E=0\). The explicit normal
Hopf boundary \(S^2\times S^3\to S^2\times S^2\) has primitive
fibre integration; Gysin and the actual boundary H3 isomorphism
give \(H^2(E/S^1)=\mathbb Ze\) and zero H3,H4. The displayed
base/meridian Mayer--Vietoris matrix for adjoining the orbit tube
has determinant minus one. Thus it gives the same S5 with its
unknotted fixed S2 and the same conifold orbit \(Y=S^2\times S^3\)
as the proved F8/K68 construction. The Euler line is the physical
line carried by OT.12--13.

Choose an invariant horizontal connection that is product in
this specified selected tube, using the explicit tube products
and a partition of unity followed by circle averaging. This
selects the actual return f on Y and its full physical-circle
lift \(\widetilde f\). The global Euler class preserves H2;
the orientation and its dual pairing preserve H3. Therefore
f lies in the group used by F22. The Hopf lift on the complement
is exactly \(\widetilde f\), and the extension on the selected
tube is the same identity from the chosen product connection.
All endpoint maps in this connection are those of OT.9 and
OT.11--13; no independent normal twist is added.

## OT.4. Weighted Stokes with the actual physical line

Delete small invariant tubes of all closed fixed components from
the completed real eight-manifold. On its locally free quotient Z
the actual principal circle line is M, and the stable tangent map
is
\[
TW|_{\rm lf}\simeq\pi^*TZ\oplus\mathbb R\langle\delta\rangle.
                                                               \tag{OT.14}
\]
It is induced by an invariant connection. On each finite
stabilizer chart choose that connection and the tangent connection
on its finite cover, average over the finite group, and transport
them through the complete derivatives and line maps in OT.2--3.
Partitions of unity give global orbifold connections with these
boundary values. Integrals on a chart of stabilizer order d are
divided by d. Stokes on each finite cover cancels every common
face with the same multiplicity, because both sides use the same
transported forms. This proves Stokes for the closed form
\[
\mathcal P_M=\frac{4x^3-p_1(TZ)x}{24},\qquad x=c_1(M),   \tag{OT.15}
\]
and separately for its two characteristic summands. No Spin
extension on W is required by this differential-form argument.

The local fixed-link convention is fixed by the complex normal
coordinates and the positive physical circle. Write U for the
positive hyperplane line in the weighted normal-link calculation.
The nonzero-vector map of K68 gives \(M=U^*\), with inverse the
Hermitian reciprocal map. Hence on that same oriented link both
odd characteristic integrals for M are the negatives of those
for U. Negative normal weights are retained in the weighted
denominator of SZ.57--59, including the finite-chart factor.

The numerical ledger uses only the complete compact components
and actual normal clutches already proved in FL/SS/CS/MC. It is
useful to retain its full pair without evaluating \(\kappa_c\):

| Components | Multiplicity | U pair \((\int u^3,\int p_1u)\) |
|---|---:|---:|
| Strict source surfaces | one global set of four | \((42,108)\) |
| The four additional two-torsion isolated points | one global set | \((-2,-14)\) |
| Interior points and curves | two O/T copies | \((-18,-126)\) per copy |
| Four exceptional-source surfaces | two O/T copies | \((-20,-20)\) per copy |
| Ten refinement surfaces | two O/T copies | \((18,126)\) per copy |
| Twelve p-chart curves | two O/T copies | \((0,-18)\) per copy |
| Ten finite-base interface curves | two O/T copies | \((0,0)\) per copy |
| The single moving capped surface | once | \((\kappa_c,4\kappa_c+6)\) |

The complete compact part before the last row is \((0,18)\).
For the last row MC proves \(c_1(E_c)=0\) and
\(\int p_1(TF_c)=-6\); expanding the actual normal sphere-bundle
formula gives exactly its displayed pair. Thus the entire inner
pair, in the U convention, is
\[
\operatorname{Pair}_{U,\rm inner}=(\kappa_c,4\kappa_c+24),
\qquad \int_{\rm inner}\mathcal P_U=-1.                \tag{OT.16}
\]
The source, frame, period and base maps determining every row
are retained by OT.2. The symbolic cancellation in OT.16 does
not fix the moving bundle's second Chern number.

## OT.5. Both boundary orientations and the endpoint inverse

Let \(\theta=\arg\epsilon\) increase, and let Y carry the orbit
orientation determined by the original complex six-dimensional
fibre and its positive physical circle. Near the outer boundary
write the orientation as
\[
\operatorname{or}(W)=d\phi_\delta\wedge\operatorname{or}(Y)
                           \wedge dr\wedge d\theta.
                                                               \tag{OT.17}
\]
After the circle-first quotient the outward normal \(\partial_r\)
crosses the five Y directions. Its boundary is therefore
\(-\operatorname{or}(Y)\wedge d\theta\). At a removed fixed
tube the inward radial boundary and the circle-first quotient
contribute the two signs already used in SZ/IE/E102; their
product gives the physical inner-link orientation in OT.16.
Applying OT.15 with these actual boundaries gives
\[
\operatorname{Pair}_{M,+}(Q_f^+)
 =\operatorname{Pair}_{M,\rm inner}
 =(-\kappa_c,-4\kappa_c-24).                           \tag{OT.18}
\]

The passage to the Jin convention is the explicit map
\[
\begin{split}
Q_f^+&=(Y\times[0,1])/((y,1)\sim(f(y),0)),\\
M_f&=(Y\times[0,1])/((y,0)\sim(f(y),1)),\\
Q_f^+&\longrightarrow M_f,\qquad [y,t]\longmapsto[y,1-t].
\end{split}                                                   \tag{OT.19}
\]
Its physical-line map is \([v,t]\mapsto[v,1-t]\). The source
endpoint relation \((v,1)\sim(\widetilde f(v),0)\) maps to the
target relation \((v,0)\sim(\widetilde f(v),1)\), using the same
full lift and all the same cap/reference words. The inverse is
the identical formula. It reverses the parameter and preserves
the physical line. Therefore the actual Jin pair is
\[
\operatorname{Pair}_{M,\rm Jin}(f)
      =(\kappa_c,4\kappa_c+24),\qquad
A_M(f)=\frac{4\kappa_c-(4\kappa_c+24)}{24}=-1.          \tag{OT.20}
\]

Finally K68's physical Hopf transfer applies to this selected f
because OT.3 identified its complementary lift and its identity
tube extension. In its actual piece coordinates the first piece
\(D^4_u\times S^3_{y_*}\) maps to
\(-(S^3_y\times D^4_q)\), and the second piece
\(S^3_u\times D^4_{y_*}\) maps to
\(-(D^4_y\times S^3_q)\). Reordering the two pieces replaces
the clutch F by its inverse. Thus the literal relation is
\(\lambda_M(F)=-\Sigma_{F^{-1}}\). Cancelling the oppositely
oriented product collars gives
\(-\Sigma_{F^{-1}}=\Sigma_F\) in the actual sphere group.
It follows from the proved F22/K68 formula that the clutched
sphere of this full positive-epsilon return has class
\(-1\) in \(\mathbb Z/28\). This calculation uses the outer
source/line/cap family and both orientation maps; it assigns no
unproved value to \(\kappa_c\), no half-turn return, and no
other selected fan.

## OT.6. Exact verification and audit scope

The accompanying certificate recomputes the component-pair sum,
the polynomial cancellation with the symbolic moving c2, the
source and selected-height rescalings, the full Hom/chain scalar
identities, the four-sector integer cap word, the retained
normal phase windings, and the boundary permutation signs.
It supplements the full geometric proofs and independent normal
wall/star audits; these finite identities do not replace the
compactness, actual cap or endpoint arguments above. This is a
new working proof pending the parent's full outer-transfer read.
