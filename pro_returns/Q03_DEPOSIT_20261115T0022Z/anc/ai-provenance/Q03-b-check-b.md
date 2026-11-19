# Referee report for Q03-b (Claude Opus 5.5, effort max)

## Verdict
PROVED AS STATED. The solution gives a self-contained proof that the hierarchy/description dynamic program works with $m$-element slots and leaf budget $K_m=12m+25$, which yields polynomial time for each fixed $m$. I re-derived every structural step: separators, the normalized exchange, walks, centers, carries and pruning, the capacity bound, flattening, the switch upset, (I1)–(I3) and the global and relative descriptions. I found no logical error. The remaining issues are minor and concern accounting and presentation.

## Claimed statements
1. **Theorem 1.1 / 9.1.** For every fixed $m\ge 3$, one effective deterministic algorithm decides $P_m\mid\mathrm{prec},p_j=1\mid C_{\max}$ with deadline $T$ for an explicitly listed DAG. It constructs a schedule when one exists and computes an optimum.
   - Time is $O_m((L+2)^{60m^2+129m+8})$.
   - After padding to $N=mT$, time is $O_m(N^{60m^2+129m+1})$.
2. **Theorem 8.5 (structure).** Every full schedule of the padded set $J$ admits a hierarchy (Def. 2.9) at every depth, in which:
   - every non-root node has a global description with at most $K_m=12m+25$ leaves;
   - every marked original-time prefix has a relative description with at most $6m+16$ leaves.
3. **Lemma 5.5.** Every pruned list has at most $m$ injection entries and at most $m+2$ entries.
4. **Lemmas 6.2 and 6.5.**
   - An earlier low set has a downset extension $H^*$ with at most $3m+3$ leaves.
   - Each list entry has at most $3m+7$ leaves.
   - Every list or carry union has at most $6m+9$ leaves.
5. **Proposition 9.2.** The DP with budget $K$ runs in $O_{m,K}(N^{5mK+4m+1})$ on a multitape Turing machine.
6. **Proposition 9.4.** The decision version is polynomial for fixed $m$ under a compact encoding of isolated jobs.
7. **Answers to Q1–Q3.**
   - The construction extends, with recomputed leaf counts.
   - There is no hidden use of $m=3$.
   - There is no failing $m=4$ step.

## Check of the argument
**§2 (foundations, DP).**
- Lemmas 2.1–2.6 are correct and elementary.
- Lemma 2.7: the count of leaf labels is about $20\binom Nm+O(N)\le 64N^m$. With Catalan $\le 4^\ell$ tree shapes and $2^{\ell-1}$ internal labellings, this gives $C_{m,K}=K\cdot512^K$. Correct.
- Proposition 2.8 (soundness): the identity (2.3) and the backward-precedence case analysis are complete. A piece $A_j\subseteq R_j$, and all earlier pieces lie in $L_j\cup Z_j$.
- Lemma 2.10: correct. Gaps are children, so they lie in $\mathcal F_K$, and prefixes have relative descriptions.

**§3 (separators, normalization, walks).**
- Lemma 3.3: the order-statistic argument is correct for every $m$. Lowering one element weakly lowers all order statistics and strictly lowers their sum, so the sorted tuple decreases lexicographically.
- Lemma 3.4: I checked each part.
  - In (2), the swap is feasible. The predecessors of $x$ lie before $s\le r$, and its successors after $t$. The predecessors of $y$ lie before $r$, and under the supposition its successors lie after $t$. Neither moved job is comparable with a companion in its new slot.
  - The successor chain is outside $M$ because $M$ is a downset.
  - Part (3) is correct, including the case of an exterior $s$.
- Lemma 3.6: after the first move, exceptions avoid $p$, which sits at $t_1$. Applying 3.4 with $M=S$ and $M=S^+$ is legitimate.
- Corollary 3.7 is correct.

**§4.**
- Lemma 4.3: the partition $S_0\,\dot\cup\, O\,\dot\cup\, Y$ holds and the priority orders extend precedence. The key fact is that qualification is upward closed, so no predecessor of an $S_0$ job is in $O$.
- Lemmas 4.4 and 4.5 are correct, including the case $b'=v$, which is handled through the center's separation on $W$.

**§5.**
- Lemma 5.1 (three-case threshold) and Lemma 5.2 ($R(x)=M(x)$ for $x\in W'$) are correct.
- Lemma 5.3: within $W$, carry qualifiers lie in $O\subseteq P_b$ and the injection meets $W$ exactly in $Y$, so the key order matches the priority order. The switched-pair indices give the correct order.
- Lemma 5.5, the only capacity use:
  - Disjointness on $W$ holds because, at the appending edge $U\to U'$, the older entry's $U$-part lies in $O_U\subseteq P_{b_U}$ and the new injection avoids $P_{b_U}$. Entries only shrink afterwards.
  - The map $f:\mathscr I\to b'$ is well defined because $x_K\in W'\setminus S\subseteq P_{b'}$ and $K$ is a global upset.
  - $f$ is injective by disjointness, since $b'\subseteq W$.
  - The bound $m$ is therefore correct.

**§6.**
- Lemma 6.1: while the first initial entry survives, every carry has $d=1$, so the second entry is untrimmed or pruned. Pruned means $U\cap D_{a_0}=\varnothing$. Agreement on $U$ follows from $U\subseteq Q_0$ and $Q_0\setminus D_{a_0}\subseteq G_0$. Correct.
- Lemma 6.2: the count is $m$ injections × 3 leaves, plus at most 2 for the flattened initial part, plus $P_{b_U}$, giving $3m+3$. The switched case gives 2 leaves. $\Phi'$ is an upset, so $H^*$ is a downset. Correct.
  - This flattening is what removes the recursive dependence on earlier switch formulas.
- Lemma 6.3: the order reversal (6.7) is correct.
- Lemma 6.4: I checked both directions.
  - $X\subseteq G$ via (4.6), Lemma 4.3 and Lemma 2.5.
  - The localization $z\in U$ uses $D_{a_-}$ and $a<b\le b_-$, and must come before (6.2) is used; the solution does it in that order.
  - The two cases use the center's (b) and Lemma 4.4 at $b'$. The case $b'=v$ is vacuous.
  - The stability of the witness is argued correctly.
- Lemma 6.5: $3+(3m+3)+1=3m+7$ per entry, and $3m+(3m+7)+2=6m+9$ for the aggregate. Correct.

**§7.**
- Lemma 7.1, Case 2:
  - Item 1 handles exterior predecessors at slot $a$.
  - Item 2: $\mathrm{key}(x)<(d,r)\le\mathrm{key}(y)$ because $S_i\cap O$ is a key-prefix of $O$.
  - The swap is feasible otherwise, which contradicts parent (I3).
  - Propagation through all advances, including unmarked intermediate positions, uses Lemma 3.4(2) with $M=L=S_j\cap E$. Carry qualifiers in $E$ lie in $O\setminus S_i$, so they are high for every $S_j$ with $j\le i$.
  - Correct.
- Lemma 7.2: both cases are correct.
  - For $a'>a$: Lemma 5.2, then the priority agreement from Lemma 5.3, then Lemma 3.3 on $E$.
  - For $a'=a$: neither job is in the injection, so Lemma 5.1 applies and then parent (I3).
- Proposition 7.3: there is no circularity. Each step uses only ancestor data.

**§8.**
- Equations (8.3), (8.4) and (8.5) hold as equalities in all of $J$.
  - (8.4) relies on child (I2), which is proved globally.
  - (8.5) localizes to $W$ before using (8.3).
- Lemma 8.3: the reversal step $(J\setminus F_z)\setminus z$ is correct.
- Leaf arithmetic: $(A_m+2)+(A_m+5)=12m+25$ and $A_m+7=6m+16$. Correct.

**§9.**
- Arithmetic: $5m(12m+25)+4m+1=60m^2+129m+1$, and $B\cdot S\cdot S^2\cdot BN^{m+1}=B^5N^{4m+1}$. Correct.

**Minor issues** (none affects correctness):
- **M1 (Cor. 9.3).** The exponent $+8$ in (1.1) is asserted as "conservative" without itemized accounting.
  - The argument actually supports $O_m(L^{60m^2+129m+2})$, since $N\le mL$ and there are at most $L$ deadlines.
  - The stated bound is weaker, hence true.
  - Repair: state $+2$, or itemize the input handling.
- **M2 (Prop. 9.2).** The multitape-TM accounting for formula generation, deduplication and backtracking is only sketched ("lower-degree polynomials").
  - Polynomiality is not in doubt.
  - The precise exponent (9.1) is plausible but not proved line by line for these subroutines.
- **M3 (§10, §9 table remark).** The lemma-by-lemma correspondence with the source numbering, and the remarks about the source's "25" and "257" leaf bounds, could not be checked against the sources from the text given.
  - The proof does not depend on them, because Sections 2–8 are self-contained.
  - The Q2 audit is therefore an audit of the construction as restated, which is sufficient for the theorem.

## External results used
- **No external theorem is a premise.** Only standard facts are used:
  - the Catalan bound $\le4^\ell$ on full binary trees with $\ell$ leaves;
  - De Morgan's laws;
  - existence of a lexicographic minimum over a finite set.
- **[P] OpenAI preprint (2026) and [L1]–[L8] lessons.** Used as the construction being generalized. Every needed lemma is re-proved, so their correctness is not assumed. Applies as used.
- **[N] Nederlof–Swennenhuis–Węgrzycki, arXiv:2312.03495, Thm 1.1.** Time $(1+n/m)^{O(\sqrt{nm})}$. Background only. The statement matches the arXiv abstract as I recall it; the venue and pages I could not confirm. Not used.
- **[A] Das–Wiese, arXiv:2501.09091 (ESA 2022).** QPTAS. Background only. Not used.
- **[F] OpenAI Lean scope file and [D] drbh repository.** Unverifiable here, and explicitly not used.

## For integration
**Outline in teaching order.**
1. Model and padding to $N=mT$; full schedules; interval replacement (Lemmas 2.1–2.4).
2. Cones, the two frames, the formula alphabet and the count $B=K\,512^K N^{mK}$ (Lemmas 2.5–2.7).
3. The DP with one $m$-antichain per state; soundness; hierarchy implies acceptance (Proposition 2.8, Lemma 2.10).
4. Separators; normalized schedules with the order-statistic exchange; one advance; fixed and shared walks; existence of a separator (Lemmas 3.1–3.7).
5. Node data:
   - keyed upset lists and invariants (I1)–(I3);
   - centers, the same and switched sides, walks and edge data (Lemmas 4.1–4.5).
6. Carry and pruning; qualifier identity and child (I1); capacity bound of $m$ injections and $m+2$ entries (Lemmas 5.1–5.5).
7. Flattening; the $3m+3$-leaf extension $H^*$; the switch upset $G$; leaf bounds $3m+7$ and $6m+9$ (Lemmas 6.1–6.5).
8. Child (I2) and (I3); validity of the construction (Lemmas 7.1–7.2, Proposition 7.3).
9. Global child descriptions and relative prefixes; $K_m=12m+25$ (Lemmas 8.1–8.4, Theorem 8.5).
10. Correctness and running time (Theorem 9.1, Proposition 9.2, Corollary 9.3).

**Definitions needed:**
- full schedule;
- frame and reversal;
- cones $P_a, D_a, \widehat P_a, \widehat D_a$;
- formula and leaf count; global and relative description;
- state and transition;
- hierarchy;
- separator;
- priority order and normalized schedule;
- list, qualifier and key;
- run, carry, pruning, injection and switch pair.

**Still to tighten (optional):**
- Itemize the multitape-TM costs in Proposition 9.2 (M2).
- Replace the "+8" exponent by the derived "+2" (M1).
- If a source-faithful audit is required, check the Section 10 correspondence directly against the source files (M3).
