# P1.19 geometric comparison: exposure-qualified sign reconstruction

Saved UTC: 2026-11-20T01:46:18.494480+00:00

## Chronology and scope

The target new proof is audit_p119_fresh/comparison_09/GEOMETRIC_COMPARISON_02.md, SHA c5b7d4b21f94d941231013edf9eab19bc20d8569f91bd6049dcf81040c6b3f67. The author announced its freeze at01:37:26.612492UTC and already supplied the desired cusp boundary formula and density identity in the01:37 message. Thus the target formula/sign were exposed before the calculation below; there is no answer-unaware claim.

I opened the first14,500 characters, covering sections0–3 and most of4, before root requested a preliminary sign freeze. The cone, floor and finite-cap definitions and their printed arguments had therefore already been received. I independently recalculated their signs below after that reading. Before opening sections5–8, I derived the cusp boundary and floor-density identity from the supplied raw claim, and committed that derivation in a collaboration message to root before the01:40:21UTC clock reading. Filesystem writes were then held for checkpoint09. The remainder of the proof was opened read-only at01:42:59.152159UTC. This file was saved after root released that hold; its save time is not substituted for an earlier file freeze. No before-reading whole-P1.19 derivation is claimed.

Reviewer: GPT-6 Astra, ChatGPT Pro mode; reasoning effort inherited and not separately exposed.

## 1. Cylinder homotopy sign, recomputed after sections0–3

Use d(a,x)=(partial a+(M_*-I)x,-partial x) and numerical d(f,x)=((W-I)x,0). Put partial H=C-Ctilde and K=HW-M_*H. For Hcal(f,x)=(Hf,-Hx), direct differentiation gives

 d Hcal + Hcal d = ((C-Ctilde)f +(HW-M_*H)x, (C-Ctilde)x).

The minus in the second entry is required: the two terms -Hx and +Hx in the first component cancel, leaving exactly K. This matches PhiQ-PhiTilde in all degrees. No homology-matrix substitution for the geometric M_* is used.

The source exterior complex has zero differential. Consequently replacing H_5 by a prescribed six-chain with the same boundary leaves every other component equation unchanged. H_6=0 is valid because both actual maps send the product fundamental chain to det(Q) times that chain. This checks the claimed degree-five replacement as a chain homotopy, not only as a cycle-level statement.

## 2. Finite-cap top sign, after target formula exposure

The actual map q_i(t,y,theta)=[y,theta+mu_i t] fixes the based theta meridian at t=y=0. For the order-four cap mu=-4, its fibre top cell maps to -4E. The signed negative-coordinate suspension sigma has d sigma=-2z. The displayed correction adds one fibre top cell to sigma; thus its cap difference is -4E. Setting Hcap(z)=2E gives Hcap(d sigma)=-4E, with dE=0. The coefficient is therefore +2 in these exact conventions.

For a negative full circuit the norm uses the backwards iterates of R. Since R^m=I, their sum is the same cyclic norm as the forward iterates, with the orientation minus sign retained. This explains epsilon times the norm in the actual cap map. It does not replace any intermediate affine meridian map by a degree alone.

## 3. Cusp boundary sign, recomputed before opening its new proof sections

Let M be the actual determinant-one cusp matrix, l its supplied fixed coorientation, and D_l the supplied floor-density six-chain, with partial D_l=C(l)-H_l. The cylinder differential gives literally

 partial(0,-D_l)=((I-M_*)D_l,C(l)-H_l).

On the fundamental cube put k=floor(M^-1 x). Invariance M^-t l=l gives

 floor(l dot {M^-1 x})=floor(l dot x)-l dot k.

The left side is the density of M_*D_l, since det M=1. Therefore

 (I-M_*)D_l=D_M(l)

as integral polyhedral chains, after subdivision on the actual rational cuts. It follows that

 Phi0(0,x_j)-(0,H_lj)=partial(0,-D_lj).

This is an exact integral boundary, including its minus sign; there is no unspecified fibre multiple. The primitive actual columns and their interpretation as the marked b_j=0 tori remain receiving inputs to be checked against the full code/source packet.

## 4. First whole-cone sign comparison after opening sections5–8

For a cone with differential(d_D,F;0,-d_B), a diagram defect Phi_D F-Fgeom Phi_B=dZ+Zd_B gives the map(a,b)↦(Phi_D a+Zb,Phi_B b). In the finite cap component, F=(j,-b_i) and Fgeom=(jgeom,-q_i), so its defect is q_i Phi_i-e_i b_i and the plus Z in Section5 is correct.

For the separate generic comparison F'-F=dT+Td, the map Cone(F)→Cone(F') is(a,b)↦(a-Tb,b). Thus the generic rule in Section8 has the correct stated direction. The final receiving review will specify which actual cusp-square defect is assigned to T, so the two sign conventions are not conflated.

This is a sign/coherence reconstruction receipt. The complete geometric-diagram and code review is still in progress when this file is saved.
