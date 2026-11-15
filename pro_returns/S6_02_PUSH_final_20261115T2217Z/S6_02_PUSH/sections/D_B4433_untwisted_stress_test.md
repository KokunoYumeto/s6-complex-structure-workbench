# Stress test against the proper untwisted Engel filling

**Purpose:** root requested an explicit comparison with the known proper untwisted filling in Part A, to test B.4.33 against an actual positive construction. This note records the check; it does not introduce another theorem or numerical certificate.

**Conclusion:** the linear monodromy and the trace/Hartogs arguments are compatible with the untwisted filling. The nonzero affine radial clutching class used in the last step of B.4.33 is absent for that family.

## 1. The ordinary period matrices coincide

Use the R8 comparison and the common parameter cover u=r^12, c=−12v with v=(2πi)^−1 log r. On the ordinary marked base the same Jacobian period matrix is

    Π_c = [[6μ, τ, 1, 0],
           [β_part+c, μ, 0, 1]].

The finite logarithmic transformations change affine gluing and the fillings at the finite places; they do not change this ordinary linear period family. In particular the homology matrices A1,A2 in B.4.31 are the same, and their quotient matrices on Λ_Q/Qδ remain

    Ā1=[[1,0,0],[6,0,1],[−6,−1,−1]],
    Ā2=[[1,0,0],[0,0,−1],[−6,1,0]].

Their common invariant space is zero in both calculations. Thus the distinction is not that the fixed-space computation fails for the untwisted family.

## 2. The actual parameter closings are different affine maps

The genuine untwisted Engel family is constructed by varying the scalar linearization u itself. Around u=r^12, the additive parameter changes c↦c−12 and the period lattice is the same, since its γ column changes by −12δ. The actual closing on the additive universal cover is the identity:

    b_untwisted=0.

In homogeneous affine Lie coordinates (ζ1,ζ2,1), its closing matrix is I3. Its lattice basis still has the unipotent return I−12δ⊗γ; identity on the Lie space must not be confused with identity on the marked homology.

For the twisted six-sphere family, C.3.5 and B.4.19 give instead

    b_twisted = Π_c γ̂ − (k+6)e ≡ −k e modulo periods,
    e=(0,1),   k=(2πi)^−1 log K,
    K(x)=x^4/(x−1)^3.

Its scalar affine representative has homogeneous matrix

    [[1,0,0],[0,1,−k],[0,0,1]].

This is the actual difference in the parameter family, not a change in a matrix convention.

The finite places explain why the scalar K cannot simply be discarded. The twisted root-to-ordinary connector is σ_j,c=w_jΠ_c v_j, and its c-shift contributes −12ε_j w_j e. An identity comparison on the ordinary core would require the opposite logarithmic correction on the smooth root torus family. Its nonzero δ winding around the root-disc centre cannot extend as a comparison of smooth torus families over that contractible disc. The finite scalar representatives K s_1^(−12) and K s_2^12 are precisely the units that cancel this defect in the actual coherent closing. The untwisted family has no such logarithmic-transform connectors; its identity closing is the one in its direct u-linearization construction.

## 3. The local logarithmic Jacobian is the same, but its affine torsor is not

Both ordinary cusp Jacobians have the multiplicative period pairing

    [[q a0, a1^6],
     [a1^(−1), q r^12 a2]],

with the same holomorphic units. The plain two-parameter fan in Part A is a model of this group family. On both punctured axes the identity (Z,W)=(1,1) is an extending origin. The identity cocharacter lies in the relevant base-face cones, so this statement is also visible directly in the displayed toric charts.

For this untwisted family the actual cusp origin can be taken to be

    σ_untwisted=0,

and the transition between the two axial identity origins is

    F_untwisted=0.

It has zero γ radial-loop evaluation. Fan subdivisions may change the proper model but do not change this associated group origin or period pairing.

For the twisted family, the cusp unit representative of the actual closing is

    b_twisted=(6μ, C−12v−12κ0−6).

It is the exact v-difference of

    σ_twisted=(6μv, −6v²+v(C−12κ0)).

The rotating r-axis origin and this actual cusp origin differ by the explicit F in B.4.24, whose positive radial difference is γ̂ (up to δ). This nonzero affine class is the indispensable final premise of B.4.33.

## 4. Consequence for the proof audit

Applying the cap-trace construction to the known untwisted proper model gives an associated A-torsor with a global origin, consistently with H¹(S,A)=0. Its global normalized loop defect is zero, consistently with the same fixed-space calculation. Both axial comparisons then have γ radial value zero. The last equation is 0=0, not 0=Dn.

The positive Part A filling therefore does not violate any reduction, saturation, primitive, trace, norm, or Hartogs step. It fails the specific nonzero actual affine-clutching premise (B.4.33.14), because its affine closing is the identity. No general noncompletion theorem for the untwisted family, for arbitrary two-parameter torus families, or for all logarithmic-torus models is being claimed.
