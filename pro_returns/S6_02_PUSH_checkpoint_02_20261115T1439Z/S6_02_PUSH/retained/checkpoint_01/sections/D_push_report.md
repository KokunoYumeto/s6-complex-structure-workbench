# Part D working report

| Prompt item | Statements | Outcome |
|---|---|---|
| D.1; Lead 8 | D.1.1–D.1.3 | Proved: the modular invariant has a natural boundary; every proposed flat proper extension, including fibrewise-isomorphic extensions, is impossible. |
| D.2; Lead 9 | D.2.1–D.2.4 | Lead 9 false: second-order escaping periods also identify the imaginary transverse direction. The fixed-parameter total-space Hausdorff reflection has a circle (rational a) or a point (irrational a) at the centre. |
| D.3 | D.3.1–D.3.2 | All local Chabauty limits classified by primitive sublattices and real homomorphisms; no path-independent local limit. |
| D.4 | D.4.1–D.4.6 | Local supercritical shape, regular-manifold locus, rank-three group closures, and exact equianharmonic crossing height (3/2π) log 48 proved. Full global level-set topology remains unsettled. |

## Sources read and exact inherited steps checked

Read the complete supplied prompt. Read the return's AB.tex A.1.1 canonical evaluation calculation and A.4.1 full translation-lattice Albanese computation; CD.tex C.1–C.3, including the local theta-polydisc calculation. The canonical evaluation gives h0(K^-1)=1 and divisor 2S2. The Albanese lattice requires the half-period translations, not merely the fixed eigenspace. The local calculation supplies an analytic coordinate h=mu-(1-tau)/2, a nonzero derivative of e2, and log N=log sqrt2-(pi/2)|h|²+O(|h|⁴); the coefficients needed below have been rederived.

Opened Buchdahl (1999), Theorem 11, pp. 296–297, from the original journal PDF; Grauert (1960), §6 Hauptsatz I and §7 Sätze 1–2 (the last is not used after the erratum check), from the original journal PDF; Cornulier's author PDF, Theorem 3.1 and its proof, pp. 10–11. The final direct-image argument in D.1 proves base change over the smooth base curve by the long exact cohomology sequence and the closed discrete torsion support of R1π_*L; it does not invoke the originally stated generic base-change theorem.

## Corrections

An initial draft cited Grauert (1960), §7 Satz 2 for a closed analytic base-change exceptional set. The foundations audit found that Grauert's 1963 erratum corrects precisely this assertion. The final proof removes this citation: coherence alone plus 0→L --t→L→i_*L_b→0 yields the exact canonical base-change sequence, and the torsion of the coherent R1π_*L on a smooth curve has closed discrete support. The mathematical theorem remains supported by the repaired argument.

Lead 8's outline becomes a proof only after removing the proper images of the nonsmooth loci, then the base-change exceptional set, then the reduced anticanonical divisor's singular and critical loci. Each exclusion is closed discrete in its then-current open curve; the final complement is at most countable, sufficient to leave a boundary-circle point in an open good locus. A global closed-discrete-union assertion is unnecessary and has been removed. The latter reduction avoids treating the nonreduced divisor 2S2 as a smooth surface. The fibrewise-isomorphic variant needs no family isomorphism or Kuranishi calculation.

Lead 9's first-order period direction is correct but its conclusion is false. For a=0, h=1/n and the integral vector n²(gamma+3u−3w)−6n w+3n delta, the period tends to (eta,xi)=(0,−3i). This is outside the asserted moving complex line modulo the central period group. The overlooked scale is n²: the quadratic term survives after the linear moving period has been cancelled. Exact model arithmetic is in code/d_push_exact.py. The actual analytic period differs by O(n^-2), proved in D.2.1. The central fibre's own Hausdorffization, the leaf-space Hausdorffization and the Hausdorffization of the entire root family are three different objects.

## Computation record

`d_push_exact.py` uses exact SymPy arithmetic to check the transformed period determinant, the entire dual-lattice formula, the cancellation responsible for the quadratic degeneration, the counterexample lattice vector, the theta-derivative constants and the rational central-circle period. Output is `d_push_exact.out`. An initial expected determinant sign was wrong; the failed assertion and correction are preserved in `d_push_exact_initial_error.out`. No theorem rests on floating-point arithmetic. `d_push_numeric.py` evaluates the equianharmonic crossing height in 110-digit mpmath arithmetic by two distinct expressions (theta series divided by eta, and the cancelled theta/eta product); both give 1.848362329764999227374945515886084283435696822219612834750098356396585750079055814438, differing by 6.6530623e-111. Equality with the proposed closed form was not inferred from these numerical comparisons; it is now proved independently by D.4.5. The two methods share arbitrary-precision arithmetic but do not share the expression being summed.

## Literature search record

Queries run on 15 November 2026: "Buchdahl even first Betti number compact complex surfaces Kähler 1999 pdf"; "Chabauty topology Pontryagin duality annihilator closed subgroups R n continuity"; "Grauert 1960 Ein Theorem analytischen Garbentheorie proper direct image theorem pdf"; "Remmert proper mapping theorem Satz 1957 Holomorphe und meromorphe Abbildungen komplexer Räume"; "Chabauty Pontryagin annihilator homeomorphism Cornulier theorem pdf"; "complex structures S6 boundary Albanese natural boundary 2026 Engel Alpoge". The last search found Engel's preprint and contemporary seminars, but no publication establishing the Part-D boundary results. We make no novelty or priority claim. The first-order lead and modular invariant are already in the supplied AI return/review; the correction and deductions here are independent calculations from their periods.

Opened URLs: https://www.numdam.org/article/AIF_1999__49_1_287_0.pdf ; https://www.numdam.org/article/PMIHES_1960__5__5_0.pdf ; https://www.normalesup.org/~cornulier/pontri.pdf . A guessed 1963 erratum PDF URL failed; it is not cited. A Remmert paper surfaced by search concerned compact images and was not used for the proper mapping theorem, which is explicitly stated in Grauert §7 Satz 1.

## Remaining D.4 work

For arbitrary supercritical height H, the zero set is exactly the modular-norm level set displayed in D.4.2. We have not classified its number of components or every possible critical level. The possible approach via the differential identity for D gives strict superharmonicity and connectedness of sublevel sets, but does not exclude additional local maxima and hence does not finish global level-set classification. The proposed equianharmonic height (3/(2pi))log48 was initially retained only as numerical evidence. The independent analytic identity in D.4.5, recorded below, now proves it exactly. The remaining step is a rigorous global critical-point and level-topology analysis of the modular-norm function.

## Final primary-source verification

The correct Grauert erratum URL https://www.numdam.org/item/PMIHES_1963__16__35_0.pdf was opened and its item 2 on printed p. 36 read: the non-bijectivity locus in original §7 Satz2 need not be closed. This confirms the repair recorded above. Cornulier's publisher PDF https://msp.org/agt/2011/11-4/agt-v11-n4-p06-p.pdf was opened; Theorem3.1 remains numbered 3.1 and its proof is on pp.2017–2018. Bibliographic details: Algebraic & Geometric Topology 11(4), 2007–2035 (2011), DOI 10.2140/agt.2011.11.2007.

## Additional global-level-set approach

The exact modulus derivative is ∂τD=iZ(3Zwp′−2g2)/(4π²wp′), where Z=∂μlogθ1+2πi Imμ/Imτ. The heat-equation derivation is D.4.4. `d_push_gradient.py` checks it against an independent symmetric difference of the product expression at three moduli in 80-digit arithmetic; discrepancies are below 9e-25 at step 1e-12. This is not a critical-point certificate. The residual precise problem is determining zeros of both factors away from elliptic ramification. Searches for "Weierstrass zeros Green function theta norm critical points modular function" and related terms led to Lin–Wang (2010), whose Theorem1.3 and introduction were opened. That result counts critical points in the elliptic-curve variable at fixed modulus, whereas our problem differentiates in modulus; it therefore does not exclude either residual factor-zero locus. URL: https://www.math.purdue.edu/~eremenko/Pdf/Lin/lin-annals.pdf .


## Exact equianharmonic crossing completed

D.4.5 now proves N((2−rho)/3,rho)=3^(1/4) and hence Dpart=−(3/(2π))log48. The proof first determines the zero mean of log N directly from the horizontal average of the Jacobi product. Multiplication by alpha=1+rho has matrix [[1,−1],[1,2]], degree3, and kernel {0,±mu}. The functions log N(alpha z) and the sum of log N(z+v) over this kernel have identical distributional Laplacians. Their difference is harmonic and its mean is zero, so it is identically zero. Taking z→0 gives N(mu)^2=|alpha|=sqrt3. The R3 normalization then supplies the exact crossing height. This is a complete analytic argument, not a numerical conjecture or an assumed closed form for beta. The lattice, mean integral and logarithm coefficients are checked in code/d_push_equianharmonic.py/.out. The remaining open statement was renumbered D.4.6; the registry now has15 Part-D rows. No novelty or priority is claimed.

## Supplemental independent reviews and the closing cocycle

The parent requested independent review of the virtual Euler obstruction and of the mapping-torus orientation. These checks are saved separately in sections/D_referee_AB_C.md, with two primary references in sections/D_referee_references.bib and exact checks in code/d_push_referee.py/.out. Both A.3.1 and A.3.2 validate; the analytic specialization proof was sharpened using the codimension-three singular set in the inverse image of a radial segment. The review also checked the global core/node plumbing, the two normalization modifications and the degree-12 component-cover obstruction for literal Lead5.

The investigation of the proposed monodromy order bound produced an explicit affine lift of R2 and a source comparison with the known v1 lift. Its durable output is the fully proved Proposition C.3.5 in sections/C_closing_cocycle.tex, with a separate registry row. The exact scalar t^4/(t−1)^3 has finite orders4,−3 and cusp order−1; its actual cusp map also has a two-coordinate holomorphic unit representative. The latter distinction prevents the scalar pole from being treated as an intrinsic obstruction to an arbitrary quotient isotopy. Patching the scalar and cusp-unit isotopies remains unproved, and no order bound is asserted. Both the earlier lift and the clean known normalization were checked in code/d_push_monodromy.py/.out and code/d_push_closing.py/.out. The audit trail and corrected intermediate gamma coefficient are retained in sections/D_monodromy_order_note.md.
