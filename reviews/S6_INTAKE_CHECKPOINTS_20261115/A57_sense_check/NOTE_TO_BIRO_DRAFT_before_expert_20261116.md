# Draft note to András Biró (not sent)

**Status:** draft, 15 Nov 2026 (main session, Claude Opus 5.5 at effort max). The user's word: it goes out only after
the S6 expert (aa7b8224, Claude Fable 5.2 at effort max) has weighed in after the full S6 intake and agrees, on a
small check, with SENSE_CHECK.md. The user sends it. Before sending, add the expert's check to the third paragraph if
it agrees, and look for a newer arXiv version of 2604.11205 (v1 of 13 Apr 2026 was current on 15 Nov).

---

**Subject:** Conjecture 1 of arXiv:2604.11205 and Louvel's first moment of Salié sums

Dear Professor Biró,

This is Claude (Claude Opus 5.5 at effort max), an AI model made by Anthropic, writing on behalf of KokunoYumeto, who
runs a project that develops mathematics with AI models.

In one of the project's research runs, GPT-6 Astra (ChatGPT Pro mode) was looking for a published conjecture that
would give a square-root bound for a lattice-point count. Among other candidates, it checked Conjecture 1 of your
preprint *Local square mean in the hyperbolic circle problem and sums of Salié sums* (arXiv:2604.11205v1). It found
that the conjecture, as printed, conflicts with Theorem 1.1 of B. Louvel, *The first moment of Salié sums* (Monatsh.
Math. 168 (2012), 523–543; arXiv:1107.5282). I have checked the argument against both papers and by a direct
computation, and I thought you would want to know.

Take L = 4, K = r = 1, m = 4, n = 1, B = 1, α = 0 and f(x) = √(C/x) g(x/C), with a fixed nonnegative g ≠ 0 in
C_c^∞ supported in [1, 2]. The hypotheses of the conjecture hold. For odd c, the substitution x = 4y gives
T(4, 4̄; c) = T(1, 1; c), so the conjecture would give

  Σ_{c ≡ 1 (mod 4)} g(c/C) T(1, 1; c)/√c ≪ C^{1/2+ε}.

Louvel's theorem with D = f = 1, χ trivial and m = n = 1 gives the main term (8/π²)X for the sum of
T(1, 1; c) ε̄_c/√c over odd c ≤ X. With m = n = −1, where the main term vanishes, together with
T(−1, −1; c) = (−1/c) T(1, 1; c), this gives

  Σ_{c ≤ X, c ≡ 1 (mod 4)} T(1, 1; c)/√c = (4/π²) X + O(X^{3/4+ε}),

so the left side above is (4/π²) C ∫g + O(C^{3/4+ε}). A direct computation agrees. Over c ≡ 1 (mod 4), c ≤ U, the
sum divided by U is 0.4007, 0.4026 and 0.4034 at U = 750, 3000 and 6000, against 4/π² ≈ 0.4053.

The example does not touch a version of the conjecture in which this main term (the contribution of the exceptional
eigenvalue, that is, of the theta function) is subtracted, or in which the cases where it occurs are excluded. We have
not checked whether the proof of your Theorem 2 uses such cases; your Remark 2 suggests that a weaker assumption is
enough there.

The run's text is public: https://github.com/KokunoYumeto/s6-complex-structure-workbench/blob/main/pro_returns/S6_05_ARITHMETIC_final_20261115T1846Z/S6_05_ARITHMETIC/sections/A_conjecture_audit.tex.
I would be glad to send the short script as well. If I have misread the statement, I apologize for the trouble.

With best regards,
Claude (Claude Opus 5.5 at effort max), on behalf of KokunoYumeto
