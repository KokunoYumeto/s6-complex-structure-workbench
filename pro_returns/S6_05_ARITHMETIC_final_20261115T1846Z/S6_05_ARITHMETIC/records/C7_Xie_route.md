# Arithmetic algebraicity-criterion route

Date: 15 November 2026. This is a new attack on C.7(c), audited after the CM eigencoordinate calculation.

## Primary source opened

Xie, J. (2024). Algebraicity criteria, invariant subvarieties and transcendence problems from arithmetic dynamics. Peking Mathematical Journal, 7, 345–398. https://doi.org/10.1007/s42543-022-00059-9

Full author preprint: https://arxiv.org/pdf/2202.09032 (version dated 21 February 2022, 50 pages). Publisher metadata: https://link.springer.com/article/10.1007/s42543-022-00059-9. Full preprint saved as `C_Xie2024_preprint.pdf` and extracted text. Theorem numbers below are those of that opened preprint.

## The exact candidate theorem

Theorem 1.3 requires a projective variety X over a global field K, a K-rational center o, a local analytic subspace V at o whose **formal germ is defined over K**, and a sequence x_n in X(K) on V converging to o for which liminf(-log d_v(o,x_n)/h(x_n)) is positive. It concludes that the relevant intersection of the Zariski closure with V is K-algebraic. The definition of a K-defined formal germ appears immediately before the theorem on page 3. The proof's more general Theorem 2.3 (pages 12–13) replaces the center by a K-defined closed subscheme but retains the formal-definition hypothesis. The branch-at-infinity form, Theorem 2.5 (page 14), retains that hypothesis as well.

## Applying it to the actual compact leaf

On the conductor-361 curve, C.7.9 proves that the real compact leaf in the diagonal extension G_Q has tangent line v=c*u with c=zeta(u)-eta_1*u/omega_1 transcendental. Therefore this germ is not defined over any number field. Indeed a one-dimensional smooth formal germ defined over Qbar has a Qbar-defined tangent line, whereas the first coordinate of this tangent is nonzero and its slope is c. Translating by an algebraic point or changing algebraic local coordinates cannot fix this obstruction; their differentials are invertible over Qbar. Nor can an algebraic isogeny fix it, since its differential is an invertible Qbar matrix in characteristic zero.

If N(P) were algebraic, C.7.9 would provide an algebraic compact point R on the leaf and hence the algebraic multiples nR in one number field. This still does not supply the theorem's formal-definition hypothesis. Thus the theorem cannot be invoked to make the leaf algebraic.

Trying inverse division does not repair the argument. If Q_n are successive elliptic division points with [2]^n Q_n=Q and all Q_n belonged to one fixed number field, their canonical heights would be 4^-n times the positive height of Q. Their ordinary ample heights are consequently bounded. They are distinct, so Northcott finiteness gives a contradiction. The corresponding inverse division lifts cannot all be rational over a fixed number field. Forward [2]^n iteration cannot tend to the identity from a nontorsion point either: in a sufficiently small exponential chart its logarithms would satisfy z_(n+1)=2*z_n, which precludes convergence to zero except for an eventually zero orbit.

No assertion about a precise Diophantine rate for arbitrary subsequences nR is needed or made. The formal-germ obstruction already rules out this application; it is not an unproved lower bound for elliptic logarithms.

## Change in status

The arithmetic criterion is a genuinely different tool from the analytic subgroup theorem and functional Ax–Schanuel. Its hypotheses were checked, and the failed formal-definition implication is proved impossible in this model. It gives no unconditional decision about N(P). The remaining main question is still whether a nontorsion algebraic compact point can exist on this transcendental-slope leaf in the **diagonal** extension. The explicit antisymmetric compact witness in C.7.10 does not answer that question.
