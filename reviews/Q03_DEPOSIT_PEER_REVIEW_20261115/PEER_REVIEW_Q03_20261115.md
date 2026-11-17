# Peer review of the Q03 Hexagon post (P_m | prec, p_j = 1 | C_max, every fixed m >= 3)

Reviewer: Claude Fable 5.2 at effort max (independent peer reviewer; brief: BRIEF.md in this folder).
Object: `returns/Q03_DEPOSIT_20261115T0022Z_unzipped/Q03_DEPOSIT_post.tex` (GPT-6 Astra, ChatGPT Pro mode, return of 15 Nov 2026 00:22 UTC).

Status of this file: IN PROGRESS (written as the review goes; the last section written is the current state).

## Log

- Brief read. Reading the post (TeX) in full before anything else. Part A of the report, `code/A_check_accounting.*` and `anc/ai-provenance/` stay unopened until my own derivation of the exponent is written below.
- Post read in full (TeX, lines 1-1920). My own derivation of the budgets and exponents follows; it was written before I opened Part A of `Q03_DEPOSIT_report.md`, `code/A_check_accounting.*` or anything in `anc/ai-provenance/`.

## Target A. The budgets and the exponent: my own derivation (written first)

Inputs used: the construction of Sections 4-6 and 8 as the post states it, the dynamic program of Section 2.2, and the tape implementation described in Proposition 9.2. Nothing from the run's accounting.

### A.1 Leaf budgets

Leaf counts (a formula's size is its number of leaves; a complemented atom is one leaf; a union or intersection costs the sum; Lemma 2.6: a complement costs nothing).

1. Entries (Lemma 5.4: an initial entry or an injection, with at most one rank suffix).
   - Injection descendant: `D_a ∩ (J∖P_b) ∩ {λ ≥ r}`: 3 leaves.
   - Root entry with a suffix: `J ∩ {λ ≥ r}`: at most 2 (it is in fact the single leaf `{λ ≥ r}`).
   - Second entry of a switch pair with a suffix: `D_a ∩ {λ ≥ r}`: 2 leaves.
   - First entry of a switch pair: `G ∩ {λ ≥ h}` with `G = D_{a_-} ∩ (J∖P̂_a) ∩ (J∖P̂_{v_-}) ∩ H*` (6.8): `3 + |H*| + 1` leaves.
2. `H*` (Lemma 6.2), for the earlier edge `U → W`.
   - Switched edge: `(J∖D_{a_U}) ∩ {λ ≤ r}`: 2 leaves.
   - Same edge: `H* = P_{b_U} ∩ (J∖Φ')`, where `Φ'` replaces the carry union of `U` on `U`. The carry is a suffix of the pruned list of `U`, so it holds at most `m` injection descendants (Lemma 5.5): `3m` leaves. Its initial part is replaced on `U` by at most 2 leaves in each case: root run `{λ ≥ r}` (1 leaf); switched run with the first entry alive, `D_{a_0} ∪ {λ ≥ k}` by (6.1) (2 leaves, replacing both initial entries); switched run with only the second entry, `D_{a_0} ∩ {λ ≥ r}` (2 leaves); nothing (0). So `|Φ'| ≤ 3m + 2` and `|H*| ≤ 1 + (3m + 2) = 3m + 3`.
   - Hence the first switch entry has at most `3 + (3m + 3) + 1 = 3m + 7` leaves, at any depth: the next switch starts again from the two-leaf substitute (6.1), not from the `3m+7`-leaf entry. This is the step that keeps the count from growing with depth, and I checked that the substitute is only ever used on `U` (Lemma 6.1 claims equality on `U` only; (6.2) is used only for jobs first shown to lie in `U`).
3. Union of a pruned list, or of a carry out of a pruned list: at most `m` injection descendants, at most one first initial entry and at most one second:
   `A_m = 3m + (3m + 7) + 2 = 6m + 9`.
4. Cutoff predicate (8.1), same side: `P_b ∩ (J∖Φ_i)`: `1 + A_m` leaves; switched side (8.2): 2 leaves.
5. Global description of a child (Lemma 8.2): (8.4) is `Q(K') ∩ P_{b'} ∩ (J∖P̂_{a'})`: `A_m + 2`; (8.5) is four cone leaves and the cutoff predicate: `4 + (A_m + 1) = A_m + 5`. Their union:
   **global budget `K_m = 2A_m + 7 = 12m + 25`** (61, 73, 85, 97 for m = 3, 4, 5, 6).
6. Relative prefix at a mark (Lemma 8.3): `B_v(H_*) = P_v ∪ (H_* ∖ D̂_v)`: 3 leaves; `B_z(S̃_i) = P_z ∪ (S̃_i ∖ D̂_z)`: `1 + (A_m + 1) + 1 = A_m + 3`; their intersection (8.7): `A_m + 6`; in a reverse working frame (8.8) removes the slot `z`: one more leaf:
   **relative-prefix budget `A_m + 7 = 6m + 16`** (34, 40, 46, 52), which is at most `K_m`, so the single parameter `K = K_m` serves both in the dynamic program.

### A.2 Padded exponent

Counting the objects of the search for a padded instance with `N = mT` jobs and leaf parameter `K`:

- Leaf alphabet: `4 + 8(N+2) + 20·C(N,m)` (2 constants; 2 threshold shapes × (N+2) values × 2 frames; 5 slot/cone shapes × C(N,m) × 2 frames; all doubled by the complement flag). For `N ≥ m ≥ 3`: `8N + 20 ≤ 16N ≤ 16N^m`, so the alphabet is at most `36N^m ≤ 64N^m`.
- Formulas with `ℓ` leaves: at most `4^ℓ` shapes × `2^{ℓ-1}` labellings × `(64N^m)^ℓ`, i.e. at most `512^ℓ N^{mℓ}`; over `1 ≤ ℓ ≤ K`: at most `B = C·N^{mK}` with `C = K·512^K`. So at most `B` described sets `W`, and for each `W` at most `B·C(N,m) ≤ 𝒮 = B·N^m` candidate states `(W∩F, Z, rest)`.
- The implementation of Proposition 9.2 finds the reachable states of each `W` by at most `𝒮` full passes over at most `𝒮²` ordered pairs of states. One pair test fetches two state records from a file of at most `𝒮` records of at most `qN` bits (`O(q𝒮N)` steps), asks one acceptance question against the set file (`O(qBN)`, at most `BN²` in the post's units) and may recheck compatibility (`N⁴` with `O(N²)` matrix seeks). Because `BN² ≤ 𝒮N` and, for `m ≥ 3`, `N⁴ ≤ N^{m+1} ≤ 𝒮N`, a pair test costs `O(q𝒮N)`.
- Propagation over all sets: `B` sets × `𝒮` passes × `𝒮²` pairs × `𝒮N` = `B𝒮⁴N = B⁵N^{4m+1}`.
- Every other part is smaller in both exponents (B-exponent at most 5 and N-exponent at most 4m+1): graph preprocessing `N⁵` (and `5 ≤ 4m+1`); formula generation and evaluation `BN³`; deduplication `B³N`; ordering by cardinality at most `B³N²`; state enumeration `B·𝒮·(BN² + N⁴) = B³N^{m+2} + B²N^{m+4}` (`m+4 ≤ 4m+1`); witness reconstruction `B·(𝒮N² + BN³) = B²N^{m+2} + B²N³`; output `N³`. That is 12 monomials, each at most `B⁵N^{4m+1}`.
- With `B = C·N^{mK}`: total at most `(const)·C⁵·N^{5mK + 4m + 1}`.

**Padded exponent: `5mK + 4m + 1`, and with `K = 12m + 25`: `5m(12m+25) + 4m + 1 = 60m² + 129m + 1`** (928, 1477, 2146, 2935 for m = 3, 4, 5, 6).

Form of the coefficient: `(scan constant)·poly(m,K)·(K·512^K)^5`, that is `2^{45K + O(log mK)} = 2^{O(m)}` for `K = K_m`. The post's `A(m,K) = 2^{40}(m+1)^4(K+1)^4(K·512^K)^5` has this form; with `q = 64(m+1)(K+1)` and `D = 2^{20}q² = 2^{32}(m+1)²(K+1)²`, `16·D·C⁵ = 2^{36}(m+1)²(K+1)²C⁵ ≤ A(m,K)`.

No logarithmic factor is left over: every index, counter and ordinal is inside a record of at most `qN` bits (`⌈log₂(𝒮+1)⌉ ≤ 2 + 10K + (mK+m)h ≤ qh/8 ≤ qN/8`, `h = ⌈log₂(N+1)⌉ ≤ N`; I rechecked the three inequalities).

### A.3 Explicit-input exponent

The vertices are listed, so `n ≤ L`. Deadlines `T ≥ n` and `T < 1` and `n > mT` never reach the padded search. In the padded branch `N = mT ≤ m(n−1) < mL`. One deadline decision therefore costs at most `A(m,K_m)(mL)^{e_m}`, `e_m = 60m² + 129m + 1`; optimization tests at most `n ≤ L` deadlines: at most `A(m,K_m)·n·(mn)^{e_m} ≤ A(m,K_m)·m^{e_m}·L^{e_m+1}`. Parsing, renaming, the elementary branches, building each padded instance and the output are polynomial in `L` of degree far below `e_m + 1 ≥ 929`.

**Explicit-input exponent: `e_m + 1 = 60m² + 129m + 2`** (929, 1478, 2147, 2936). The one extra power is the loop over deadlines; a single deadline decision already fits the exponent `e_m` in `L`.

Form of the coefficient: `A(m,K_m)·m^{e_m}` plus a lower-order parsing term, that is `2^{O(m)}·m^{60m²+129m+1} = m^{O(m²)}`. The post's `G(m) = A(m,12m+25)·m^{60m²+129m+1} + 2^{31}(m+1)^4` has this form.

### A.4 My numbers

| quantity | my derivation |
|---|---|
| union of a list or carry | `A_m = 6m + 9` |
| global leaf budget | `12m + 25` |
| relative-prefix budget | `6m + 16` |
| padded exponent | `5mK_m + 4m + 1 = 60m² + 129m + 1` |
| explicit-input exponent | `60m² + 129m + 2` |
| coefficient | padded `2^{O(m)}` (`∝ (K·512^K)^5`); explicit `m^{O(m²)}` (`∝ A(m,K_m)·m^{e_m}`) |

Two remarks of mine on what these numbers are (made before reading the run's accounting):

- They are upper bounds for the deliberately simple tape implementation of Proposition 9.2, not properties of the method. The `𝒮` passes are an overcount inside the post's own text: Step 8 of Proposition 9.2 notes that every transition raises `|L|` by at least `m`, so a state path has at most `N/m` states and `N/m` passes already reach everything. With that one change the same implementation gives `B·(N/m)·𝒮²·𝒮N`, exponent `4mK + 3m + 2 = 48m² + 103m + 2`. The post disclaims optimality of the exponent, so this is not an error; it bears on how the exponent is compared with Jansen's (Target C).
- The exponents do not depend on the explicit constants. The explicit coefficients `A(m,K)` and `G(m)` rest on the asserted slack `D = 2^{20}q²` ("32 tapes suffice", "at most 64 primitive passes per operation"), which the post does not itemize down to tape moves. The slack is very large against what the scans need (a factor of order `2^{20}q` over a `q`-linear scan), so I regard the coefficients as credible, but only the `O_m` statements are proved to the standard of the rest of the post.

### A.5 Comparison with the run's accounting (read after A.1-A.4 were written)

Opened now: report Part A (`Q03_DEPOSIT_report.md`, lines 252-476), `code/A_check_accounting.py` and `.out`, and the cost passages of `anc/ai-provenance/Q03-solution.md` and of the three October reports.

| quantity | mine | post / run | |
|---|---|---|---|
| list or carry union `A_m` | `6m + 9` | `6m + 9` | agree |
| global leaf budget | `12m + 25` | `12m + 25` | agree |
| relative-prefix budget | `6m + 16` | `6m + 16` | agree |
| padded exponent | `60m² + 129m + 1` | `60m² + 129m + 1` | agree |
| explicit-input exponent | `60m² + 129m + 2` | `60m² + 129m + 2` | agree |
| padded coefficient | `16·D·C⁵ ≤ A(m,K)` | `A(m,K) = 2^{40}(m+1)^4(K+1)^4(K·512^K)^5` | agree |
| explicit coefficient | `A(m,K_m)·m^{e_m}` + parsing | `G(m) = A(m,12m+25)·m^{60m²+129m+1} + 2^{31}(m+1)^4` | agree |

**No difference to resolve.** The factorisation is the same on both sides: one `B` for the sets, `𝒮` passes, `𝒮²` pairs, `𝒮N` per pair, with `𝒮 = BN^m` and `B = K·512^K·N^{mK}`; then `N ≤ mL` and at most `L` deadline trials.

On the earlier `+8`: the October return (Q03-solution.md, Corollary 9.3) printed `(L+2)^{60m²+129m+8}` and called it "a conservative larger integer exponent"; the same paragraph already says the trials "could already be covered by exponent `60m²+129m+2`". All three October reports (Claude Opus 5.5 at effort max, Message Batches API) flagged the `+8` as underived and gave `+2`. So `+8` was a true but underived bound, and `+2` is the derived one. My derivation gives `+2` and nothing forces more: beyond the padded exponent the only extra power of `L` is the loop over deadlines.

What `code/A_check_accounting.py` does and does not show: it checks the arithmetic (`5m(12m+25)+4m+1`, the table for m = 3..6) and that each of ten listed monomials is dominated by `B⁵N^{4m+1}`. It does not check the rows themselves (that each subroutine costs what its row says); that is the prose of Proposition 9.2, which I followed row by row in A.2. The script's last line computes the slack `A/(D·C⁵) = 256(m+1)²(K+1)²`, which matches my `16·D·C⁵ ≤ A` with room to spare.

The run agrees with my two remarks: its §3.5 calls the `𝒮`-pass count "deliberately generous" and notes the acyclicity that would shorten it, and its §1 says the constants "have no claim to sharpness".

**Verdict on Target A: the budgets `12m+25` and `6m+16`, the padded exponent `60m²+129m+1`, the explicit-input exponent `60m²+129m+2` and the forms of `A(m,K)` and `G(m)` are confirmed by an independent derivation.**

## Target B. The rewritten layouts of Lemmas 3.3 and 5.5

Method: each step read against the definitions it cites and against the places where the lemma is used; then compared with the proofs in the October return (`anc/ai-provenance/Q03-solution.md`, lines 281-285 and 533-549) and with the source counterparts in the OpenAI preprint (fetched at the pinned commit 4eaee875: `separators.tex`, Lemma 4.3 `lem:lex-prefix`; `lists.tex`, Lemma 6.4 `lem:list-length`).

### Lemma 3.3 (post lines 632-654): correct, no step changed its meaning

- **Statement.** A normalized schedule `Σ` of `U`, a slot `r`; the slots strictly after `r` are replaced by a full schedule of the same suffix job set; then no exchange of a job `y` at `r` with a later job `x`, `π(x) < π(y)`, gives a full schedule of `U`. Identical to the return's statement.
- **Step 1** (`Σ'` and `Σ` agree before `r`). Holds: the replacement touches only slots after `r`, the exchange only `r` and one later slot. Full schedules of `U` all have `|U|/m` slots, so "slot `r`" is the same position in both.
- **Step 2** (the sorted `m`-tuple at `r` decreases lexicographically). The value set at `r` loses `π(y)` and gains `π(x) < π(y)`; `π(x)` is not already at `r` because `x` is later and `π` is a bijection. For every threshold `q` the count of values `≤ q` does not drop (if `π(y) ≤ q` then `π(x) ≤ q`), so the `k`-th smallest value, which is the least `q` with count `≥ k`, weakly decreases for every `k`. The sum drops strictly, so the two sorted tuples differ, and at the first coordinate where they differ the new one is smaller. Complete.
- **Step 3** (contradiction). Equal tuples before `r` and a smaller tuple at `r` make the encoded sequence of `Σ'` lexicographically smaller whatever follows; `Σ'` is a full schedule of `U`; this contradicts minimality. Complete.
- **Uses of the lemma checked.** Lemma 3.4, Step 2 applies it with the trivial replacement, `y ∉ M` at `r`, `x ∈ M` at the later slot `t`: the hypotheses hold (`M` is a priority prefix, so `π(x) < π(y)`). Lemma 7.2, Step 2 applies it on the normalized side `E` at `r = a'`: in the child's copy of the witness the part of `E` outside `W'` is untouched, so replacing `W'` is a replacement of the suffix after `a'`, and `x`, `y` are high for `S_i` with key order equal to the priority order (Lemma 5.3). The statement proved is the statement needed in both places.
- **Against the return and the source.** The three steps are the return's sentences in the same order (agreement before `r`; order statistics by threshold counts and the sum; lexicographic contradiction). The OpenAI lemma argues with a sorted triple; the order-statistic argument is the capacity-`m` replacement and is proved in full.
- **The remark "where `m` enters"** is accurate: only the slot size.

Optional wording (not required): the clause "keeping a full schedule of `U`" is automatic (a full schedule of the suffix set after `r` always concatenates to a full schedule of `U`); it reads as a hypothesis, which is harmless.

### Lemma 5.5 (post lines 1012-1043): correct, no step changed its meaning

- **Opening.** A switched update starts a run with at most two entries and no injection; so only a same-side update `W → W'` with edge data `a', b', S` needs the count. `𝓘` = the injection entries surviving in the pruned list of `W'`. Matches the return.
- **Step 1** (two entries of `𝓘` are disjoint on `W`). For `K` created before `K'`, let `U → U'` be the edge of the run where `K'` was appended (`U = W` is allowed; otherwise `W ⊆ U' ⊆ U`). Since `K` survives to `W'`, its then-current form is an entry of the carry formed at `U → U'`; carry qualifiers are old qualifiers of `U` (Lemma 5.1), and inside `U` those lie in `O_U ⊆ P_{b_U}` by (I1) at `U`. `K'` is created as `D_{a_U} ∖ P_{b_U}`, which misses `P_{b_U}`. So the two are disjoint on `U` at that moment; afterwards entries are only deleted or intersected with rank suffixes (Lemma 5.4), so they stay disjoint on `W ⊆ U`. Complete. The frames are consistent: a run has one tag, and on a same side the working frame is the tag frame, so `a_U, b_U`, (I1) and the injection all refer to the same frame.
- **Step 2** (every `K ∈ 𝓘` contains a job of `b'`). `K` survived pruning on `W'`, so `K ∩ W' ≠ ∅`; `x_K` is its least-rank job (a function, no arbitrary choice; this is the "choice domain" the run made explicit). `x_K` qualifies in `W'`, so it is high (Lemma 5.3: the qualifiers in `W'` are exactly `W' ∖ S`), so `x_K ∈ P_{b'}` by (4.6); `b'` is a genuine slot of `W` (Lemma 4.5), so some job of `b'` is a strict successor of `x_K`; `K` is an upset of all of `J` (an injection is `D_a ∩ (J∖P_b)`, a rank suffix is an upset), so that successor is in `K`. `f(K)` = the least-rank such job; `f(K) ∈ K ∩ b'`. Complete.
- **Step 3** (`f` injective). `b' ⊆ W`; a common value would lie in `K ∩ K' ∩ W`, excluded by Step 1. Complete.
- **Step 4** (the count). `|𝓘| ≤ |b'| = m`; a carry keeps each entry at most once, a run has at most two initial entries (one at the root), so a pruned list has at most `m + 2` entries. Complete.
- **Induction order.** The lemma uses (I1) at ancestors in the run and Lemma 5.3 at the child; neither uses a leaf count or a descendant. Proposition 7.3, Step 3 places it correctly in the depth induction (Lemma 5.3 depends on (5.3), i.e. Lemma 6.4, which depends on Lemma 6.2 and so on Lemma 5.5 for earlier nodes only).
- **Against the return and the source.** The four steps carry the return's four paragraphs in order: disjointness on `W`, the witness in `b'`, injectivity, the count. Nothing is added or dropped; the return's sentence "choose the job `x_K ∈ K ∩ W'` of least rank" is the same choice. The OpenAI lemma gives "at most five entries, at most three injections", which is `m + 2` and `m` at `m = 3`.
- **The remark "where `m` enters"** is accurate: only `|b'| = m`, and the witness lies outside `W'`, which is why global upsets are needed.

Optional wording (not required): in Step 2 cite Lemma 4.5 where the successor in `b'` is taken (it is cited one step later); in Step 1 say "the then-current form of `K`" for the entry that sits in the carry.

**Verdict on Target B: both layouts are correct step by step and say what the return says. No gap.**

What the finite check adds for Lemma 5.5: nothing beyond the trivial case. `code/B_hierarchy_check_output.json` records `max_injections: 1`, `max_pruned_entries: 1`, `flattenings: 0`, `max_global_formula_leaves: 10`. No tested list ever held two entries, so the injectivity argument, the flattening (6.1) and the leaf budget were never exercised beyond their smallest cases. The post says part of this (see Target C, C-7).

## Notes on Sections 2-8 outside the two lemmas (read as far as Targets A-C need)

I followed, without re-proving line by line, Lemmas 2.10, 3.1, 3.4-3.6, Corollary 3.7, 4.2-4.5, 5.1-5.4, 6.1-6.5, 7.1, 7.2, Proposition 7.3, 8.1-8.4 and Section 9. Points I checked because the budgets or the two lemmas depend on them, all of which hold:

- Lemma 6.1/6.2: the two-leaf substitute for the initial pair is claimed and used on `U` only; `Φ'` is an upset, so `H*` is a downset of `J`; the count `3m+3` does not depend on depth.
- Lemma 6.4, Steps 3-5: the localization `z ∈ U` comes from `D_{a_-}` and (6.7) before (6.2) is used; the two time ranges are exhaustive, and the range in Step 5 is empty when the old right boundary is the old center.
- Lemma 7.1, Steps 6-10: the first advance uses parent (I3) with the key inequality `key(x) < (d,r) ≤ key(y)`; the exchange feasibility check covers the companions in both slots; later advances use Lemma 3.4(2) with `M = L = S_j ∩ E`, and a carry qualifier in `E` is high for every `S_j ⊆ S_i`.
- Lemma 8.2: (8.4) needs child (I2) (Lemma 7.1) to exclude qualifiers at or before `a'`; (8.5) first places the job in `W` through `D_{a'} ∩ P_b`, then uses (8.3).
- Lemma 2.10: every lookup is a child or empty; children have global descriptions in `F_K`, the root is the leaf `J`.

I found no gap and no error in what I read. This is not a line-by-line re-proof of Sections 2-8.

[review continues below]
