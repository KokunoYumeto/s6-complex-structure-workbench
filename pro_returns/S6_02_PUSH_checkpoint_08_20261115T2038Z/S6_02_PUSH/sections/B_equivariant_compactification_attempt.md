# Compact third-component attempt: proved reductions and exact gaps

Owner: boundary_d. Date:2026-11-15. This note is an attempt record, not a compactification theorem.

## Proven part

B.4.11 contracts the elliptic axis in the explicit S8 and proves H²(Y,ThetaY)=0. B.4.12 globalizes the specified degree-eight Q-cone smoothing and obtains a proper smooth threefold over a disc with central surface S8 union_E Q. The total threefold is not compact.

The independent character calculation in B.4.14 proves H¹(Y,ThetaY)=C^8 with trivial C* action and H⁰=C trivial. For a compact associated Y-bundle Z_L→P1, it follows that R¹Theta_relative=O^8 and H²Theta_relative=0. The same vanishing holds after tensoring by the ideal of one whole fibre, since H¹(P1,O(−1))=0. AB's independent proof and exact verification are in `sections/ab_push_kato_weights_referee.md` and `code/ab_push_kato_weights.py/.out/.json`.

## First candidate: equivariant global smoothing

The genuine C* action x↦lambda x on S8 descends to radial homothety on Y. The local cone(Q) sweep has parameter of weight one. A convergent equivariant global-to-local deformation map would admit a compatible section over the weight-one parameter disc: after pullback its base is smooth, and compact-circle linearization of that smooth base gives an equivariant transverse section. A genuine weight-one family would be holomorphically trivial over the punctured disc, allowing gluing to a product over the outer P1 chart.

This candidate is **not established**. Rim's theorem is formal/algebraic, and convergence cannot be silently added. Doan's convergent Kuranishi theorem covers compact smooth manifolds, whereas Y is singular. Cathelineau's theorem deforms pairs (compact complex space, group) over a base on which the group acts trivially; that does not supply the required moving-base weight-one action.

Opened primary sources: Doan, *Equivariant Kuranishi family of complex compact manifolds*, arXiv2004.07014v2, introduction pp1–2 and Corollary4.1; Cathelineau1978 was independently opened by root/AB. The primary Doan preprint *Equivariant deformations of isolated singularities and applications*, arXiv2606.09199v1, was downloaded with urllib after the web parser returned DisabledError and read locally. Its pp5–6 explicitly retain the general equivariant analytic-object formalism as a problem: Bingener1987 Remark4.8(3) announced a possible extension whose promised details seem not to have appeared. This is a source limitation, not a proof that the desired action is impossible.

Doan2026 files are retained under `/workspace/scratch/20a906f0fadd/external_sources/D_elliptic_contraction/Doan2026.pdf` and `.txt`.

## Second candidate: relative globalization on a compact associated bundle

Take L=O(1) and glue copies of Y by radial homotheties with the transition functions of L. The singular points form a section Sigma=P1. The explicit cone(Q) smoothing has the same radial action, so it glues as a local family near Sigma after setting its local parameter equal to epsilon times a section sigma of L. A section sigma with one simple zero would yield, for fixed nonzero epsilon, a compact threefold with one cone(Q) vertex. Blowing up that vertex would insert Q.

To keep the compact strict transform exactly S8, the deformation must retain the whole fibre above the zero b0 of sigma, not only its isolated singular germ. This explains the proved vanishing for Theta_relative(−F_b0).

The missing step is a precise analytic local-to-global theorem for this nonisolated singular section with the prescribed transverse cone family and fixed whole fibre. H²Theta_relative=0 alone does not establish it. Local automorphisms on overlaps may fail to lift, and prescribing an entire non-Stein neighbourhood may add matching obstructions. The cotangent-complex spectral sequence suggests also controlling H¹(T¹); Pinkham's degree-eight weight data may make the relevant associated sheaf nonnegative. Even a formal lift must be made analytic while retaining the selected Q smoothing component. No isolated-singularity theorem or lci theorem is substituted for that missing argument.

Root independently opened Tziolas, arXiv0808.0436v2, §9 Theorem9.4, which identifies successive obstruction locations H⁰T², H¹T¹, H²Theta for nonisolated singularities. It is algebraic/formal and does not by itself supply the remaining analytic realization here.

## Conditional Euler budget for this particular arrangement

If the proposed compact C→P1 existed with exactly one S8 union_E Q fibre and all other compact fibres of Euler number12, then chi(C)=24. For A=Bl_E(P3) and B=S8×P1, chi(A)=4 and chi(B)=16. The three double surfaces have Euler numbers0,4,8, and the triple curve E has Euler number0. A proper reduced normal-crossings smoothing of exactly these compact components would therefore have

chi(smooth threefold)=4+16+24−2(0+4+8)+3·0=20.

This is a necessary conditional calculation, not an invariant assigned to an unconstructed space. It also shows that completion of this particular auxiliary three-piece arrangement would not by itself produce an S6 fibre of Euler number2. Additional modifications or an actual comparison with the prescribed punctured family would still be needed.

No novelty or completed compactification claim is made.
