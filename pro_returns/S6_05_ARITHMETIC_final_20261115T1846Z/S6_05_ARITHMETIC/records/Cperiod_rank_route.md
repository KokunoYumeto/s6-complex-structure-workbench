# Exact primary period-rank criterion: scope test

Checked 15 November 2026, 18:35--18:37 UTC. This is a source and hypothesis audit, not a new unconditional decision of C.7(c).

## Primary theorem

Waldschmidt (1988), *On the transcendence methods of Gelfond and Schneider in several variables*, in A. Baker (Ed.), *New Advances in Transcendence Theory*, Chapter24, pp.375--398. Full author-public scan retrieved and printed pp.385--386 visually checked. Theorem4.1 treats a complex subspace V of dimension n<d in Lie(G), an algebraic subspace W of dimension t contained in V, and a finitely generated subgroup Y of V whose exponential is algebraic. Put m=rank(Y), kappa=rank(Y intersect ker exp). With a decomposition G=Ga^d0 x Gm^d1 x G2, d2=dim G2, the nontrivial-subgroup threshold (4.2) is

    m > (d1+2d2-kappa)*(n-t)/(d-n).

Corollary4.3 gives, when exp(V) is Zariski dense, the density bound

    mu(Y,V) <= (d1+2d2-kappa)/(d-n).

For n=1, mu(Y,V)=m. Equality at the threshold never suffices for the strict conclusion.

Roy and Waldschmidt (1993), *Autour du theoreme du sous-groupe algebrique*, CMB36(3),358--367, DOI10.4153/CMB-1993-049-8. Full publisher PDF retrieved, pp.358--365 read, main theorem printed363 visually checked. Define d0(G),d1(G) as maximal additive and multiplicative QUOTIENT dimensions and alpha(G)=2dimG-2d0-d1. Their general number-field theorem uses alpha_K(G), not automatically alpha(G). For K=Q, Psi=identity and a subspace V containing no nonzero algebraic Lie subspace, it yields

    dim_Q(V intersect Lambda_Q(G))
      <= (alpha(G)-kappa)*dim_C(V/W),

where kappa=dim_Q(V intersect Omega_Q(G)), W is algebraic and contained in V, Lambda_Q is the Q-span of logarithms of algebraic points, and Omega_Q is the Q-span of periods. The statement is an equivalence with finiteness and absence of obstructing subspaces. A line containing no nonzero algebraic vector satisfies the hypothesis, with W=0.

## Application to the original nonsplit G_Q

Take Q=(4,-2) on E361, with real logarithm 0<u<omega1/2. The extension G_Q of E by Gm has dimension2. Any character G_Q->Gm restricts to an integer n on its torus. The existence of that character forces the pushed-forward extension nQ to vanish. Since Q is nontorsion, n=0, after which the character factors through E and is zero. A semiabelian variety has no additive quotient. Thus d0=d1=0 and alpha(G_Q)=4. Counting its torus SUBGROUP as d1=1 would give an incorrect threshold.

By C.7.9, the compact line V={(z,cz)} has transcendental c, so W=0 and V has no nonzero algebraic vector. The period vectors are (omega_j,zeta(u)*omega_j-eta_j*u), together with (0,2*pi*i). A rational combination is in V precisely when the coefficient q2 of the second elliptic period and the torus coefficient q3 obey q2*u/omega1+q3=0, by Legendre's relation. Since u/omega1 is irrational (Q is nontorsion), q2=q3=0. Hence kappa=1 exactly.

Under the norm algebraicity hypothesis, C.7.9 constructs an algebraic point R with logarithm u(1,c). Together with omega1(1,c), it gives a rank2 group Y. The point is independent of the period because its projection Q is nontorsion. The exact theorem permits rank at most (4-1)*1=3. Thus the known rank2 data do not contradict it. The Zariski closure of exp(V) is all of G_Q as well: a proper positive-dimensional closure projecting nontrivially to E would be an elliptic subgroup and split an isogeny pullback of the nontorsion extension.

## Larger CM enlargement: only a qualified test

C.7.10 proves that the dimension3 group G_Q x_E G_{beta Q} has no multiplicative quotient. Consequently its unrefined Q-coefficient is alpha=6, despite a torus subgroup of dimension2. Granting a proposed two-dimensional analytic plane with period rank2 and two additional independent algebraic-point logarithms, the W=0 coarse threshold would be total rank8, not4: (6-2)*2/(3-2)=8. If an algebraic line W were separately established inside that plane, the threshold would become4, with strict excess still required. Neither assertion about that plane is being imported without proof, and no coefficient alpha_K for this nonsplit enlargement has been established in this record. In particular, the CM value alpha_K(E)=1 for the abelian quotient cannot simply be assigned to the extension.

## Source access and preservation

Access script/output: code/C7_period_rank_fetch.py and .out. Its initial execution encountered unavailable optional bs4; it was revised to use the Python standard-library HTMLParser and then completed. No source claim depends on an AI-generated secondary account. That search hit was used only to identify these older primary references.

Full third-party source files are outside the artifact directory, under ../research_downloads/C7_division/:

* C_Waldschmidt1988_period_rank.pdf, 767740 bytes, SHA256 d4615aec78b11a4d4dfb0795e103c256df52f4bf4140f9d3990802d79a04017e. URL https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/Durham1986TMGSSV.pdf . Render pages06--08 retain the source images; pages06--07 visually inspected for the exact theorem.
* C_RoyWaldschmidt1993.pdf, 969866 bytes, SHA256 6c71e58c55a258d96e42231562a789f0cdccb7d85db54a3e34bdddbcd57fb2ef. Publisher PDF URL https://www.cambridge.org/core/services/aop-cambridge-core/content/view/A1E35F3798690D084664ACD83D1557E8/S0008439500013138a.pdf/div-class-title-autour-du-theoreme-du-sous-groupe-algebrique-div.pdf . Extracted text and renders are alongside it. The final visual check was produced by `pdftoppm -f 6 -l 6 -png -r 130 research_downloads/C7_division/C_RoyWaldschmidt1993.pdf research_downloads/C7_division/C_RoyWaldschmidt1993_render/page`, exit0 with no console output, then page-06.png visually inspected; it confirms the weak inequality <=.

One short unnumbered scope paragraph was appended to C_division_values.tex at root's explicit request, with references_Cperiod_rank.bib. No global decision of N(Q)'s algebraicity or transcendence is claimed.
