# Withdrawn source-zero end diagnostics

Recorded 17 November 2026, checks; neither diagnostic was promoted or used in a return value.

## 1. Old j label versus current vertical basis

An informal message substituted j=-1 from SZ.15 into the current shear expression and suggested a zero C2 right integer. This conflated two actual coordinate labels. SZ.15's rays form the positive square diagonal, which is the current T1 in its node coordinates (Z=S0,U), not current T_{-1}. Moreover, for the full single-loop winding matrix [[1,b],[-a,N-2]], direct conjugation by P_n=[[1,0],[n,1]] gives lower-left entry -a+(N-3)n-bn^2. The corresponding formal C2 right expression is a+(3-N)n+bn^2. The earlier expression a+3n+bn^2 had suppressed N without first constructing a constant-scalar split. Both omissions were caught before any proof or result mapping used them. The complete node-to-Tate Cartier/source map, including P's winding, remains necessary.

## 2. The proposed reset contraction does not follow from the central restriction

A proposed route was to use B^2/(4 lambda^2)=Id on v=0,T nonzero, then extend it as the identity on a compact R>0 arm and contract by v -> s v. That extension was not proved and is false as an inference from the displayed restriction. The first U arm can contain the other component, on which the next U has its contraction. The section 2G has a codimension-two base limit not determined by its restriction to v=0,T nonzero.

The actual normal-cone calculation SZ.32 retains the obstruction. In coordinates 2v=r(1-p), T=-r(1+p), the two-step source reset is w -> p w, with p the approach direction. At a generic nonzero w, distinct p give distinct limits as r tends to zero. Smoothness of the source projection at the point does not remove this dependence. Fourfold independently identified this obstruction in the exact saved source map. The proposed v-contraction is withdrawn.

The verified one-U common-graph arrow still fixes xi and F+, hence z=xi/F+. Its cyclic/source-period closure remains a separate actual map. No characteristic vanishing for the complete arm is inferred from the one-U arrow alone.

## 3. Corrected scalar-path amplitude

The first RT.12 draft wrote r(t)=r0 exp(2 pi i k t) while setting r0^m=lambda0. Root's audit caught the missing actual source-base amplitude. The corrected loop uses r_base=v_*^k r0, so r(t)^m=v(t)^(km)lambda0 exactly. The phase homotopy remains at that amplitude. A different scalar reference requires a separate zero-winding radial path in the common contracting range. No return value used the earlier amplitude.
