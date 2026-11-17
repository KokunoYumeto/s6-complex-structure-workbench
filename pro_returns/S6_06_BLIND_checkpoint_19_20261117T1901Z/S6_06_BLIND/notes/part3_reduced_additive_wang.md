# The integral relative-Wang column for a reduced additive cap

Working chain comparison supplied to the source-cap calculation,
17 November 2026. This is a chain-level lemma; the specific cap
construction and its remaining Mayer--Vietoris maps are owned by
the source-classification agent.

Let \(V\) be the source surface with the selected singular-fibre
neighbourhood removed, and let \(T\) be the actual source translation
on \(V\) and its boundary. Use the mapping-cone convention
\[
 {\cal C}_j(V,T)=C_j(V)\oplus C_{j-1}(V),\qquad
 d(a,b)=(da+(T-1)b,-db).
\]
The inclusion of the boundary induces the literal componentwise
map of these cones.

Take the punctured zero section \(D\), so \(\partial D=q\) is the
marked source meridian. At the III* source under primitive
translation, \(Tq-q=\eta\) in boundary homology, where \(\eta\)
has order two. Choose an integral boundary two-chain \(C\) with
\[
                    \partial C=2(Tq-q).
\]
Then
\[
                         (-C,2q)
\]
is an integral two-cycle in the boundary cone. Its second component
is the invariant Wang class \(2q\). In the exterior cone,
\[
 (-C,2q)+d(0,2D)=\bigl(2(TD-D)-C,\,0\bigr).       \tag{RW.1}
\]
Thus the inclusion sends this class to the class of the explicit
integral two-cycle
\[
                         Z=2(TD-D)-C
\]
in \(\operatorname{coker}(T-1:H_2(V)\to H_2(V))\).
This proves the relative-Wang comparison with its sign, without
choosing a splitting of a rational exact sequence.

For the III* source write \(M=P_{2G}-O\), where \(P_{2G}\) is the
section twice the primitive generator. Let \(R_1\) be the E7 root
correction of \(G\), and \(\varphi\) its orthogonal Mordell--Weil
class. The marked identities are
\[
 G=O+F+\varphi-R_1,\qquad
 P_{2G}=O+F+2\varphi,\qquad M=F+2\varphi .
\]
The E7 discriminant class has order two, so \(2R_1\) is an
integral root combination. Closing the punctured section discs in
the removed source neighbourhood computes (RW.1) modulo this
integral vertical lattice. For positive translation,
\[
                    2(G-O)=M+F-2R_1 .
\]
For the actual negative-translation suspension,
\[
                 2(P_{-G}-O)=-M+3F-2R_1 .
\]
Consequently the exterior Wang column is respectively \(+[M]\)
or \(-[M]\). Its sign is selected by the actual suspension
convention; its primitivity is integral in both cases.

The choice of the correcting chain \(C\) causes no ambiguity in
this column. Two choices differ by a boundary two-cycle. The source
boundary has \(H_2=\mathbb ZF\), and this class maps to zero in the
exterior cokernel because \((T-1)M=\pm F\). This retains the full
relative boundary marking used by the cap.
