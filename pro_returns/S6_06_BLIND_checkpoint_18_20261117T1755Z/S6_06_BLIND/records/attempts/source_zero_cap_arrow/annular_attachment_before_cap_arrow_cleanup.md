# Source-zero E-annulus: the exact component and normal deck

Working attachment record, 17 November 2026. The statements below concern
the actual E annulus and its chain charts. They supply boundary data; they
do not assert that the collision quotient and the cap have been attached
over the central collision point.

## EA.1. The component permutation and its full-cycle representative

Use the notation and actual theta/Cartier maps of K39 Sections 19–22 and
27. Thus (N=km), (n=\pm1), (c=nk), and the changed ordinary line
coordinate is (V_\eta). The positive (q_1)-deck, as an arrow on the
logarithmic base cover, is
\[
 S:(q_1\text{-sheet},V_\eta)\longmapsto
       (q_1\text{-sheet}+1,v^{-c}V_\eta).
\]
On the actual node charts
\[
 X_j=V_\eta/v^j,\qquad Y_j=v^{j+1}/V_\eta,
 \qquad X_jY_j=v,
\]
this is literally
\[
             S:(j,X_j,Y_j)\longmapsto(j-c,X_j,Y_j).       \tag{EA.1}
\]
Both normal coordinates are unchanged after the displayed index change.
This proves that the node components modulo the scalar period (N)
have (k) cycles of length (m), with the sign of (n) retained.

Write the full scalar period as
\[
 g:(Z,V_\eta)\longmapsto(g_ZZ,v^N g_0V_\eta).
\]
It sends chart (j) to chart (j+N), with

\[
        (Z,X_j,Y_j)\longmapsto(g_ZZ,g_0X_j,g_0^{-1}Y_j).
\]
After (m) positive (q_1)-deck arrows the index is (j-nN).
Returning to representative (j) by the *actual* period (g^n)
therefore gives the full-cycle arrow
\[
 C=g^nS^m:(Z,X,Y)\longmapsto
       (g_Z^nZ,g_0^nX,g_0^{-n}Y).                         \tag{EA.2}
\]
This is a forward-deck arrow on the chosen sheet. The
endpoint-to-initial closing in the associated mapping torus is its
inverse. No component reindexing has been discarded.

## EA.2. The central source and normal maps

On (v=0), (0<|T|<\epsilon), the exact central identities already
proved from the chord and Cartier maps are
\[
 P^2Q=1,\qquad h=(Q,P^a),\qquad
 g_Z=P^{-b},\qquad g_0=2(-1)^{b+1}\lambda_0P.             \tag{EA.3}
\]
Here the factor (v^N) has been removed only in writing the node-chart
unit (g_0). The scalar in the actual suspension remains

\[
                         \lambda=v^N\lambda_0.
\]
For (a=1,b=2), (EA.2) has source multiplier (P^{-2n}=Q^n).
Dividing by the literal source period (h^n), whose line multiplier
is (P^n), gives
\[
 C_{\mathrm{good}}:(Z,X,Y)\longmapsto
       (Z,(-2\lambda_0)^nX,(-2\lambda_0)^{-n}Y).          \tag{EA.4}
\]
For (a=2,b=1), the actual central line is trivial on this punctured
annulus in the frame (ZV_\eta): its factor under (h) is

\[
                            QP^2=1.
\]
Accordingly put (\widehat X=ZX),

\[
 \widehat Y=Z^{-1}Y,\qquad \widehat X\widehat Y=v.
\]
Then the same arrow is
\[
 C_{\mathrm{red}}:(Z,\widehat X,\widehat Y)\longmapsto
       (P^{-n}Z,(2\lambda_0)^n\widehat X,
                         (2\lambda_0)^{-n}\widehat Y).   \tag{EA.5}
\]
The source multiplier (P^{-n}) is the marked nonzero two-torsion
translation. Its square is (P^{-2n}=Q^n), an actual source period.
It is not itself a source period: the already established asymptotics

\[
               P\sim16/T,\qquad Q\sim T^2/256
\]
give the half-period valuation. Thus the reduced full-cycle arrow retains
an actual source translation, even though its displayed normal units
are constant.

Equations (EA.4) and (EA.5) retain the full central units, not only their
winding numbers. In particular the positive-weight normal determinant
gets the unit (c/\bar c) for the displayed constant (c), after
conjugating the negative-weight coordinate. This statement does not
choose a logarithm across (T=0).

## EA.3. The Cartier class and the remaining cap comparison

The flat frame (ZV_\eta) in (EA.5) is used only on the punctured
annulus. The source calculation of K39 Section 2 identifies the full
central Cartier line for (a=2) with (O(C_0)), and for (a=1)
with (O(G_0-O)), whose component degrees on ((C_0,C_1)) are

\[
                          (-1,+1).
\]
Consequently the punctured trivialization in (EA.5) is not declared to
extend as a nowhere-zero section across the (I_2) fibre. The vertical
Cartier divisor remains part of the attachment.

The finite cap has the actual generator

\[
 A=v^{kn}r_0^nA_0,\qquad A_0^m=B_0^n,
\]
and the ordinary-to-cap map is the full (F_0) fixed in RCZ.5–7,
after the explicitly displayed changed origins. It identifies the
forward (q_1)-deck with the inverse cap-root arrow, including the
source translation and the line character. It therefore transports
(EA.2) to the cap frame with its full source/line cocycle. No assertion
that this transported frame extends across (T=0) follows from the
constant normal units in (EA.4)–(EA.5).

For the good branch, the chosen division representative

\[
 R=(QP^2)^{1/m}
\]
and the identity-component representative (R_I=P^{2/m}) on a strict
I chart differ by (Q^{1/m}). Their (m)-norms differ by the source
period (Q), including its actual line factor (P). The alternative
strict-I representative has no component translation there, but using
it in the cap requires an actual affine source conjugacy and its line
lift, with the integral annular cochain carried. The finite-cap
equation to solve is the explicit one from AE.1–4:

\[
                       (1-D)T=Z,
\]
where (Z) is the exact difference of the two affine translation
terms and has zero *cyclic* norm. A pointwise (m)-division identity
alone does not establish that cyclic-norm condition. This is the next
comparison being computed, and no global filling or numerical return
is assigned in this record.

The finite exact certificate is
\path{code/part3_fourfold/source_zero_e_annular_deck.py}; it checks both
signs, the component cycles, the full-period reindexing and the two
central normal-unit cancellations.

## EA.4. The primitive chamber map on the actual finite cap

Here the primitive map is the *negative* source translation of SZ.7:

\[
 U_1:(p,w)\longmapsto(p-G,w/X(p-G)).
\]
For (a=2), retain the actual Cartier map

\[
 r(p)=X(p-G),\qquad
 r:O(2G-O)\longrightarrow O(G-O)^{\otimes2}.
\]
The primitive map in the original line is therefore

\[
 U_2^{\rm Cartier}=r_{\rm target}^{-1}
              U_2^{\rm tensor}r_{\rm source}.            \tag{EA.6}
\]
It is (EA.6), rather than an unlabelled tensor-power frame, that is
carried to the cap. In the common Cox coordinates of SZ.14–15 every

\[
                         U_a: \text{t-ruling}\longrightarrow
                                      \text{s-ruling}
\]
is the identity on the common nonzero coordinate (V). This is the
inverse direction to K23's s-ruling-to-t-ruling map

\[
                 \tau(h,q_H)=(q_H^{-1}h q_H,q_H).
\]
The degree-two case retains the actual residual (\mu_2) and line
charge two.

Write (q_\infty=z^m) on the cap and

\[
 q=q_\infty^{-1}h,qquad h=1-T_0(v)q_\infty.
\]
There is the following literal normalization of the primitive lift:

\[
  U_{\rm cap}=z^{-ma/2}U_a^{\rm Cartier},qquad
  B=2(-1)^{b+1}\lambda h\,U_{\rm cap}^{,b},qquad ab=2.
                                                               \tag{EA.7}
\]
The exponent (ma/2) is an integer in each admitted branch. To
verify the extending map, first take the good branch (m=4p,a=1).
The actual root coordinates have (X=z^{-2p}X'). Thus the primitive
target multiplier (1/X) is exactly (z^{2p}/X'). The root map

\[
        (p,w)\longmapsto(p-G',w/X'(p-G'))
\]
is an extending isomorphism of the actual degree-zero root line:
its horizontal divisor is the same Cartier identity as SZ.7, and at
the smooth central root fibre its generic coefficient is a nonzero
unit, so its possible whole-fibre divisor has coefficient zero.
This proves the first equality of (EA.7) in the good branch.

For the reduced branch (b=1,a=2), use (EA.6) before passing to the
actual corrected root line. The already constructed root suspension
is an everywhere invertible map (B_0); its full coefficient in
SZ.12 is retained. Since (h) is an extending nonzero unit,

\[
                        U_{\rm cap}=B_0/(2h)              \tag{EA.8}
\]
is an extending source/line map. Comparing with the exact ordinary
identity (B_0=2qU_2^{\rm Cartier}) gives

\[
                        U_{\rm cap}=z^{-m}U_2^{\rm Cartier}.
\]
This is the reduced equality in (EA.7). It incorporates the Cartier
correction of the reduced III source; the raw coefficient

\[
                       z^{-4p}/X'(p-G')^2
\]
on an uncorrected tensor frame is not used as its extension.
Finally (z^{mab/2}=z^m=q_\infty), so multiplying by the actual
selected factor (q) proves the second equality of (EA.7) with the
unit (h), rather than with a discarded base power.

The actual finite character is also determined. On the good root the
canonical deck sends (X'\) to (-X'), and preserves the marked
source divisor. Consequently

\[
 D U_{\rm cap}D^{-1}=-U_{\rm cap}.
\]
The translation lift in (A_0) commutes with (U_{\rm cap}) by the
literal constant-factor presentation of a degree-zero elliptic line.
The equality extends over the root line. Hence

\[
              U_{\rm cap}A_0U_{\rm cap}^{-1}=-A_0
                    \quad (a,b)=(1,2).                   \tag{EA.9}
\]
Equivalently the first primitive step carries the finite delta
character (d\) to (d+m/2); the second returns to (d).
On the reduced cap, (EA.8), the exact norm relation and the
deck-invariance of (h) instead give

\[
                 U_{\rm cap}A_0=A_0U_{\rm cap}
                    \quad (a,b)=(2,1).                   \tag{EA.10}
\]
Both statements retain (n=\pm1) and every original finite delta
character. Multiplication of (A_0) by the rescaled parameter factor

\[
                              v^{kn}r_0^n
\]
does not change either commutator.

On the chosen root sheet the full annular Cartier map carries

\[
            U_a^{\rm Cartier}\longmapsto z^{ma/2}U_{\rm cap}.
\]
Its root-deck character cancels exactly: in the good branch both

\[
                         \zeta_m^{ma/2}quad\text{and}quad -1
\]
are (-1), and in the reduced branch both characters are (1).
The translation part of the full (F_0) commutes with the displayed
primitive lift in the actual degree-zero-line group. Thus this is a
literal annular comparison with the full root/line map, not only a
comparison of source points. After (b) steps it is exactly the
actual suspension in (EA.7).

In particular, in the reduced branch the forward suspension retains
one t-ruling-to-s-ruling arrow; the cap inserts no second ruling
change. The inverse suspension has the opposite arrow. The
identification of this arrow with the oriented residual stable end of
the real collision bordism is still a separate map. No characteristic
number is inferred here solely from the number of primitive factors.
