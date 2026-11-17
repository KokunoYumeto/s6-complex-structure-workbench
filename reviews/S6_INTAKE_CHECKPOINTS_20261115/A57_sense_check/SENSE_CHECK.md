# Sense check of S6_05 Statement A.5.7: Biró's Conjecture 1 is false as printed

15 Nov 2026, main session (Claude Opus 5.5 at effort max), at the user's word ("download and check real quick as a
sense check"). Sources: the arXiv sources of both papers, in `src_biro_2604.11205/` and `src_louvel_1107.5282/`.
Biró's paper is at v1 (13 Apr 2026), the only version.

**Verdict: the run is right.** Conjecture 1 of Biró, *Local square mean in the hyperbolic circle problem and sums of
Salié sums* (arXiv:2604.11205), contradicts Theorem 1.1 of Louvel, *The first moment of Salié sums* (Monatsh. Math.
168 (2012); arXiv:1107.5282).

1. **The conjecture** (SQFI7.TEX, lines 172-187).
   - Take f supported in [C, 2C] with x^j f^(j)(x) ≪ C^(jδ), and 2 | L, gcd(L, Kr) = 1, LK(1+B) ≪ C^δ, m, n ≥ 1,
     α ∈ [−B, B].
   - It asserts (1/C) Σ_{c≡r (L), K|c} f(c) T(m, L̄n; c) e(√(mn)α/c) ≪ (mnC)^ε, with
     T(m,n;c) = Σ (x/c) e((m x̄ + n x)/c).
2. **The run's specialization.** Take L = 4, K = r = 1, m = 4, n = 1, α = 0 and f(x) = √(C/x) g(x/C).
   - Every hypothesis holds.
   - T(4, 4̄; c) = T(1,1;c), by x = 4y; checked numerically for all odd c < 400 (error 1.6e-14).
   - So the conjecture would give Σ_{c≡1 (4)} g(c/C) T(1,1;c)/√c ≪ C^(1/2+ε).
3. **Louvel's Theorem 1.1** (SalieSums.tex) with D = f = 1, χ trivial, m = n = 1 (t = s = m' = n' = 1) gives
   Σ_{c≤X odd} T(1,1;c) ε̄_c/√c = (8/π²) X + O(X^(3/4+ε)).
   - With m = n = −1 the main term vanishes, and T(−1,−1;c) = (−1/c) T(1,1;c).
   - Together these give the class c ≡ 1 (mod 4): (4/π²) X + O(X^(3/4+ε)), a linear main term. That contradicts the
     conjectured C^(1/2+ε).
4. **Independent numerical check** (`salie_first_moment_check.py`, direct summation, no closed formula; output in
   `salie_first_moment_check.out`). A_1(U) = Σ_{c≤U, c≡1 (4)} T(1,1;c)/√c gives A_1/U = 0.4007, 0.4010, 0.4026 and
   0.4034 at U = 750, 1500, 3000, 6000, against 4/π² = 0.4053; the full odd sum gives 0.8102 against 8/π² = 0.8106.
   - The growth is linear, as Louvel says. It is not O(U^(1/2+ε)), as the conjecture would need.
   - Heuristically, the roots v = ±1 of v² ≡ 1 (mod c) give about 2 per odd c, and the other roots lower that to
     ∏_{p odd}(1 − p^(−2)) = 8/π².

**What it does not show.** The run itself says that a version of the conjecture with the main term subtracted (the
contribution of the exceptional pole, i.e. of the theta function) is not refuted. Biró's Theorem 2 is conditional on
Conjecture 1. His Remark 2 says a weaker assumption suffices (his Lemma 13), so his result may well survive with a
corrected hypothesis. This note checks only the literal statement.

**Use.** S6_05 uses no implication from the false statement. The finding could go to Biró as a courteous note, through
the informing-authors practice; a draft would go to the user first.
