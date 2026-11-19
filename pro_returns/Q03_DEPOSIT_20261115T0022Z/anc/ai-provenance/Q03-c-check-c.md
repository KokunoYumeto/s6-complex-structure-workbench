# Referee report for Q03-c (Claude Opus 5.5, effort max)

## Verdict
PROVED AS STATED. The argument is self-contained and I checked its key steps one by one: the exchange lemma for sorted $m$-tuples, the one-advance and shared-cutoff walks, the edge labels, the carry/prune lists, the injectivity bound of $m$ injections, the flattening that stops leaf counts from recursing, the switch upset, the exterior invariants (I2)/(I3), the global descriptions, and soundness and completeness of the one-slot dynamic program. None of these uses $m=3$ beyond the definitions and the injection count. The remaining defects are minor: an informally derived input-length exponent, and unverifiable bibliographic side-claims that the proof does not use.

## Claimed statements
1. **Theorem 1.1.** For every fixed $m\ge3$, deciding a deadline $T$ for $P_m\mid\mathrm{prec},p_j=1\mid C_{\max}$, constructing a witness, and constructing an optimal schedule take $O_m((L+2)^{60m^2+129m+8})$ deterministic multitape steps. For padded size $N=mT$ the bound is $O_m(N^{60m^2+129m+1})$. No bound uniform in $m$ is claimed.
2. **Theorem 8.5 (structure).** Every full schedule of the padded set $J$ admits a hierarchy (Definition 2.9) in which every node has a global description with at most $K_m=12m+25$ leaves. Every marked original-time prefix has a relative description with at most $6m+16$ leaves, at every depth.
3. **Lemma 5.5.** Every pruned list has at most $m$ injection entries and at most $m+2$ entries.
4. **Lemmas 6.2 and 6.5.** The following leaf bounds hold:
   - an earlier low set has a downset extension with at most $3m+3$ leaves;
   - each list entry has at most $3m+7$ leaves, and only the first initial entry of a switched run can need more than 3;
   - every list or carry union has at most $6m+9$ leaves.
5. **Theorem 9.1 and Proposition 9.2.** The dynamic program with $m$-element slots and $K=K_m$ is sound and complete and runs in $O_{m,K}(N^{5mK+4m+1})$.
6. **Proposition 9.4.** The decision problem is polynomial in the compact encoding (number of isolated jobs given in binary).
7. **Answers to Q1–Q3.**
   - The construction transfers with "triple" replaced by "$m$-antichain", padding $N=mT$, at most $m$ injections and at most $m+2$ entries, and leaf counts recomputed; the counts are linear in $m$.
   - No step fails for $m=4$, so the algorithm itself does not fail.

## Check of the argument

**§2 Foundations and the dynamic program.**
- Lemmas 2.1–2.6 are correct.
- In Lemma 2.4, exterior/interior relations are consistent with the interval placement in the original full schedule.
- Lemma 2.7: the leaf alphabet satisfies $\le 20N^m+8(N+2)+4\le 64N^m$. There are at most $4^\ell$ tree shapes and $2^{\ell-1}$ internal labellings, which gives $C_{m,K}=K\,512^K$. Correct.
- Proposition 2.8 (soundness), checked directly:
  - The decomposition $L_{i+1}=L_i\dot\cup Z_i\dot\cup A_i$ holds.
  - $A_j\subseteq R_j$, so a backward relation from $A_j$ or $Z_j$ into $L_j\cup Z_j$ is excluded by the two compatibility tests.
  - The argument is valid for any $m$ and any description family.
- Lemma 2.10 (completeness from a hierarchy) is correct. It needs each child to be in $\mathcal F_K$, which the hierarchy guarantees.

**§3 Separators and walks.**
- Lemma 3.3 is correct for all $m$. Replacing $\pi(y)$ by a smaller $\pi(x)$ weakly lowers every order statistic and strictly lowers the sum, so the first differing statistic decreases.
- Lemma 3.4(2): I checked the exchange feasibility, including the case $r=s$ with $y\in s$ and comparabilities with companions in the destination slots. Predecessors of $x$ lie strictly before $s$ by (1), successors of $x$ lie after $t$, and successors of $y$ lie after $t$ by the supposition. The iteration is correct because $M$ is a downset, so successors of high jobs stay high.
- Lemma 3.4(3) correctly treats $y$ before $s$ through (a) at $s$.
- Lemma 3.6 is correct. After the first move, exceptions lie strictly after the slot of $p$, so they belong to $S$, and Lemma 3.4 applies with both $M=S$ and $M=S^+$.
- Corollary 3.7 is correct.

**§4 Centers and edges.**
- (4.3) follows from Lemma 3.2: the complement of $W\cap P_{b}$ in the tag frame is $W\setminus D_a$ in the reversed frame.
- Lemma 4.3 is correct. The partition $W=S_0\dot\cup O\dot\cup Y$ holds, and the cutoff and precedence-extension checks go through.
- Normalizing $E$ keeps $v$ a separator, because the sets of jobs on the two sides of $v$ do not change.
- Lemma 4.4 is correct, including the claim that $v$ separates $S_q$ on $E$.
- Lemma 4.5 / (4.6) is correct.

**§5 Lists.**
- Lemmas 5.1–5.3 are correct. In particular $Y\cap(\text{carry})=\varnothing$ and $I\cap W=Y$. On a switched side the second index puts $W\cap D_a$ after $X\setminus S$ even where $G$ overlaps $D_a$.
- Lemma 5.5 is the only genuine use of capacity, and it generalizes correctly:
  - Surviving injections are pairwise disjoint on $W$. This uses (I1) at the creating node, in the same frame within one run. It also covers the injection appended at $W\to W'$ itself.
  - The least-rank high job of each entry has a successor in the genuine slot $b'\subseteq W$, and the entry contains it because entries are global upsets.
  - Distinct entries are disjoint on $W$, so the map into the $m$ jobs of $b'$ is injective.

**§6 Switching.**
- Lemma 6.1 is correct. While the first initial entry survives, the second is untrimmed, or it was pruned on a superset of $U$ and so is disjoint from $U$.
- Lemma 6.2 is correct: $H=(U\cap P_{b_U})\setminus\Phi$ with $\Phi\cap U=O_U\setminus S_i$. The essential point is that the flattened, local-only $\Phi'$ breaks the recursion of formula sizes; I checked that $H^*$ is used only after localization to $U$.
- Lemmas 6.3 and 6.4 are correct, including the three-case analysis for $z$ at or before $a$. The analysis uses:
  - the center separating $S_*\supseteq H$ on $U$;
  - $s_{i+1}$ separating $S_i$ on the old side;
  - the fact that positions outside $W$ are unchanged between $U$'s witness and the current one.

**§7 Invariants.**
- Lemma 7.1, Case 2, is correct:
  - all global predecessors of the first exception lie before $a$;
  - its key is below the carry threshold, which is at most the key of $y$;
  - parent (I3) forbids the swap, so $y$ has a successor at or before $t$;
  - Lemma 3.4(2) on normalized $E$, with vacuous (a) at the exterior boundary, carries the chain to $a'$;
  - the carry is an upset, so every job in the chain qualifies.
- Lemma 7.2 is correct. A child replacement changes only the suffix of normalized $E$ after $a'$, which is a special case of Lemma 3.3. The case $a'=a$ reduces to parent (I3) via Lemma 5.1.
- Lemma 5.2 is applied with the smaller-key job in $W'$, as it requires.
- Proposition 7.3: the induction order is non-circular.

**§8 Descriptions and counts.**
- Lemma 8.1 is correct.
- (8.4) and (8.5) are correct global equalities. The converse directions use child (I2), the center separator and Lemma 4.4.
- Lemma 8.3 is correct, including the conversion $(J\setminus F_z)\setminus z$ in the reverse frame.
- Arithmetic: $2(6m+9)+7=12m+25$ and $(6m+9)+7=6m+16$.

**§9 Running time.**
- (9.3) evaluates as $B\cdot S^3\cdot BN^{m+1}=B^5N^{4m+1}$, and $5m(12m+25)+4m+1=60m^2+129m+1$. The entries 928 and 1477 in the table are right.
- *Minor:* Corollary 9.3 justifies the exponent "+8" in (1.1) only informally ("input model conventions"). A correct derivation is short: $N\le mL$ and at most $L$ deadline trials give $O_m(L^{e+1})$ with $e=60m^2+129m+1$, so the stated bound holds a fortiori.
- Proposition 9.4 is correct.

**§11 Computations.** The code was not available to inspect. The proof does not rely on it.

## External results used
- **The 2026 three-machine preprint [P] and the lessons [L1]–[L8].** These are used only as the construction being generalized; every step is re-proved, so no claim from them is a premise.
  - The solution's figures about [P] (exponent 150020, a "257-leaf" total, a "25-leaf" per-entry estimate) could not be checked. They are irrelevant to correctness.
  - The cross-reference tables in §10 could not be checked against the sources. Their completeness is not needed, because the proof is self-contained.
  - The reference "SOURCES(4).zip" mislabels the supplied archive (minor).
- **drbh, *scheduling-proof-exploration* [D], and the formalization scope file [F].** Explicitly not used as premises; their content cannot be verified.
- **Nederlof–Swennenhuis–Węgrzycki, arXiv:2312.03495, Thm 1.1, $(1+n/m)^{O(\sqrt{nm})}$ [N], and Das–Wiese, arXiv:2501.09091 [A].** Background only. The solution correctly states that neither yields an exact polynomial bound for fixed $m$. Venue details are not checked and not needed.
- **Fujii–Kasami–Ninomiya, Coffman–Graham and Ullman.** Background only and not used.

## For integration
**Definitions needed:** full schedules and padding; formulas over the atoms rank threshold, $a$, $P_a$, $D_a$, $\widehat P_a$, $\widehat D_a$ (both frames); states $(L,Z,R)$; hierarchies; cutoffs and separators; normalized schedules; upset lists, keys and the invariants (I1)–(I3); carry, prune, injection and the switch pair.

**Outline in teaching order:**
1. Padding and interval replacement (Lemmas 2.3–2.4).
2. The dynamic program and its soundness (Proposition 2.8); a hierarchy implies acceptance (Lemma 2.10).
3. The lexicographic exchange for $m$-tuples (Lemma 3.3); the one-advance and shared-cutoff walks (Lemmas 3.4–3.6).
4. Centers, side priority orders and edge data (§4).
5. Carry and prune (Lemmas 5.1–5.3); at most $m$ injections via the injection into $b'$ (Lemma 5.5).
6. Flattening, the downset extension $H^*$ and the switch upset $G$ (Lemmas 6.1–6.4); leaf bounds $3m+7$ per entry and $6m+9$ per union (Lemma 6.5).
7. (I2)/(I3) for children (Lemmas 7.1–7.2).
8. Global and relative descriptions (Lemmas 8.2–8.4), giving $K_m=12m+25$.
9. Running time $N^{5mK_m+4m+1}$.

**Still to do:** replace the informal "+8" step in Corollary 9.3 with the explicit accounting above.
