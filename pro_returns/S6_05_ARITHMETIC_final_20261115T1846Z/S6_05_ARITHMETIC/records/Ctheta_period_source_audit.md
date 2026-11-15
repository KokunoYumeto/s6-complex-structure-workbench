# Common-period refinement and exact theta source audit

## C.7.12 independent audit

Root independently opened the GMW, Herblot, and Gasbarri statements and passed the C.7.12 argument, requesting explicit explanations for the real CM hull and for fixed complex-shift heights. These are now included. Lattice independently passed the degree, height, scalar-descent, and translate-cap arguments, and correctly distinguished the complex analytic subgroup of the semiabelian extension from its compact real circle. The manuscript now makes that distinction explicitly.

## The common-period modification

The generators share the real period 2 omega1; after w=exp(pi i z/omega1) they are functions on a punctured plane with logarithmic-quadratic growth. GMW's printed p.102 mentions a possible common-period refinement without stating its complete criterion there. The informal annular optimization does not repair the displayed envelopes, but this is only a parameter heuristic and has not been promoted to a theorem or added to C.7.12.

A separate exact periodic functional-equation theorem was checked in Waldschmidt (1988), *Fonctions thêta et nombres transcendants*, Bordeaux seminar 1987–1988, no.15, printed p.15-05. It assumes a number field containing q=exp(i pi tau) and algebraic values of both the multiplicative coordinate and the periodic function; its displayed bound is s < (700/pi) Delta d² delta h(q)/Im(tau), under the further analytic-at-zero and algebraic-independence hypotheses printed there. The algebraicity of q is false for the CM tau in our problem, by Gelfond–Schneider. Thus this particular exact periodic-functional-equation application does not settle our metric norm. This does not assert that every common-period refinement is inapplicable.

The author-public 1988 scan also gives, on printed p.15-03, an explicit normalized statement of Bertrand's one-variable CM theorem: with algebraic Weierstrass invariants and an algebraic nontorsion point, sigma(u) exp(-s2(Lambda) u²/2) is transcendental. It defines s2 by the regularized lattice sum, without a suppressed lift convention. The cited original is Bertrand (1982), *Valeurs de fonctions thêta et hauteurs p-adiques*, Progress in Mathematics22. This recovers a precise published normalization for the holomorphic CM result; the real metric still has its separate Gaussian factor. It is a statement checked in a primary mathematical exposition, not a claim that Bertrand's original complete proof has been retrieved.

Bundschuh and Waldschmidt's 1996 one-page erratum was also opened. Their 1989 Theorem2.7 requires a smaller sampling radius r′<r and the replacement of r by r−r′ in the specified Cauchy estimate and limsup condition; Theorem3.8's proof also changes R(N). We have not used the uncorrected 1989 criterion.

New source PDFs and renders remain outside the deliverable root in research_downloads/C7_division/. Exact public URLs, paths, and hashes are preserved in code/C7_common_period_fetch.py,out.

## Reyssat's stronger independence statements

The full original 1982 Acta Arithmetica scan was downloaded and printed pp.291–297 were visually read. Theorem1 and Corollary2 give two independent numbers among the compact third-kind slope, the exponential of the real Betti coordinate, and the sigma value with eta/omega normalization (or its derivative). If the real metric value were algebraic, these statements force the slope and the Betti-coordinate exponential to be algebraically independent. They do not give a contradiction.

Theorem3 and Corollary4 add periods, quasiperiods, and the modular nome, and give transcendence degree at least three. The CM Corollary6 also contains the quadratic exponential arising from CM multiplication. These larger tuples retain enough unclassified numbers when the metric value is assumed algebraic; no algebraic-dependence consequence contradicting their lower bound has been derived. The introduction explicitly says that an auxiliary Lemma8 is not fully proved in this paper and is used only for Theorem3. We have not silently replaced that source scope with a claim of a fully self-contained proof.

A direct check of the tempting CM substitution avoids an OCR ambiguity in printed p.295. For pure imaginary CM beta and real u, let theta(z)=sigma(z)exp(-s2 z²/2) and b=eta1/omega1. CM multiplication gives

    sigma((beta-1)u)/(sigma(beta u)sigma(u)) exp(b beta u²)
      = a exp((b-s2) beta u²)
      = a exp(pi beta u²/A),  a in Qbar*.

This is because Norm(beta-1)=Norm(beta)+1. The final exponential is a pure phase. Algebraicity of all metric norms controls its modulus, not its phase, so this substitution does not turn Reyssat's third-kind value into an algebraic number.

## Original Bertrand1982 access

The author's public research page and public PDF-directory index were opened; neither exposes the 1982 chapter. A later mathematical bibliography cites a public full-volume URL on plouffe.fr. A single ordinary HTTPS request returned HTTP403, and that route was stopped without an access-control workaround. The attempted URL and result are preserved in code/C7_Bertrand1982_access.py,out. No full original Bertrand1982 proof has been claimed retrieved.
