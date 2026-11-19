# Referee report for Q03 (Claude Opus 5.5, effort max)

## Verdict
PROVED WITH FIXABLE GAPS. The structural argument is self-contained and checks line by line for general $m$: the sorted-tuple exchange, the walks, centers, carries, the injection count $\le m$, the switch upset $G$, the boundary invariants (I1)–(I3) and the global child descriptions. Together these give the hierarchy with $K_m=12m+25$, so the description DP is complete and Theorem 9.1 holds. The remaining problems are minor and in the periphery: the advertised input-length exponent in (1.1) is asserted rather than derived, and several claims about the sources and the literature are unverified, though none of them carries weight in the proof.

## Claimed statements
1. **Thm 1.1.** For every fixed $m\ge3$ there is one effective deterministic algorithm that does the following for an explicitly listed DAG on $n$ unit jobs and a deadline $T$:
   - it decides $P_m\mid\mathrm{prec},p_j=1\mid C_{\max}\le T$;
   - it constructs a schedule when one exists, and an optimal one;
   - it runs in time $O_m((L+2)^{60m^2+129m+8})$, and in $O_m(N^{60m^2+129m+1})$ after padding to $N=mT$.
2. **Thm 8.5 (structure).** Every full schedule of $J$ admits a hierarchy (Def. 2.9) with the following leaf bounds, independent of depth:
   - global child descriptions use $\le 12m+25$ leaves;
   - relative mark-prefix descriptions use $\le 6m+16$ leaves.
3. **Lemma 5.5.** Pruned lists have $\le m$ injections and $\le m+2$ entries.
4. **Lemmas 6.2 and 6.5.**
   - The earlier-low extension $H^*$ has $\le 3m+3$ leaves.
   - Each list entry has $\le 3m+7$ leaves.
   - Every list or carry union has $\le 6m+9$ leaves.
5. **Q3 answer.** No step fails for $m=4$, so no counterexample family exists for the algorithm.

## Check of the argument
**§2 (foundations, DP).**
- Lemmas 2.1–2.6 are correct.
- Lemma 2.7: there are $\binom Nm\le N^m$ slot atoms and at most Catalan$(\ell-1)\le4^\ell$ tree shapes, so $B\le K512^KN^{mK}$. Correct.
- Prop. 2.8 (soundness): the compatibility tests cover every backward relation. Each $A_j\subseteq R_j$, and every earlier piece lies in $L_j\cup Z_j$. Correct.
- Lemma 2.10: the gaps are children or empty, and the mark prefixes have relative descriptions. Correct.

**§3 (separators and walks).**
- Lemma 3.3: lowering one of $m$ values weakly lowers every order statistic and strictly lowers the sum, so the sorted tuple decreases lexicographically. This is valid for all $m$; it answers the Q2 bullet on normalization.
- Lemma 3.4: in (1), the predecessor $w$ is placed in $L$ via the prefix property. In (2), the exchange is checked against both slots' companions and exterior jobs. In (3), the chaining is correct.
- Lemma 3.6: after the first move every exception lies after $t_1$, so it lies in $S$. Applying Lemma 3.4 twice preserves condition (a) for both cutoffs. Correct.
- Cor. 3.7 is correct.

**§4 (centers, sides, edge cutoffs).**
- Lemma 4.3: the partition $S_0\dot\cup O\dot\cup Y$ is right, and the priority order extends precedence on both sides.
- Lemma 4.4: $s_q<v$ because walk positions lie in $E\cup\{a\}$.
- Lemma 4.5 gives (4.6). Correct.

**§5 (carried and pruned lists).**
- Lemma 5.1: since $O\cap S$ is a key prefix, $O\setminus S=\{\text{key}\ge(d,r)\}$. Correct.
- Lemma 5.2: the hypothesis $x\in W'$ is correctly required.
- Lemma 5.3: the switched-side ordering is correct. Jobs of $X\setminus S$ get index 1 and jobs of $W\cap D_a$ get index 2.
- Lemma 5.5, disjointness: older injections lie, inside $U$, in the carry, which is contained in $O_U\subseteq P_{b_U}$. The new injection lies outside $P_{b_U}$.
- Lemma 5.5, injectivity: $f(K)\in K\cap b'\subseteq K\cap W$, using the global upset property. Hence the count is $\le m$. This is the only capacity use, and it is correct.

**§6 (direction changes).**
- Lemma 6.1 (flattening): while the first initial entry survives, the second is untrimmed, or it was pruned and is then disjoint from $U$. In both cases (6.1) agrees with the carried initial entries on $U$. Correct.
- Lemma 6.2 checks:
  - (6.4) holds;
  - $\Phi'$ is an upset with $\le 3m+2$ leaves;
  - $H^*$ is a downset and needs only agreement on $U$.
  
  The switched-edge case (6.3) is correct.
- Lemma 6.3 correctly reverses the inequalities of the old side, giving (6.7).
- Lemma 6.4: $X\subseteq G$ follows from (4.6), Lemma 4.3 and Lemma 2.5. The localization $z\in U$ is done before (6.2) is used. The two cases ($z$ at or before $v_-$; $z$ between $v_-$ and $a$) correctly use the center separator and Lemma 4.4. The persistence of the witness outside $W$ is addressed.
- What (5.3) needs is only that $G$ is an upset with the two properties. So this $G$, with fewer factors than the source's (16 versus 25 leaves for $m=3$), suffices for the solution's own proof.
- Lemma 6.5:
  - per-entry count: $3+(3m+3)+1=3m+7$;
  - aggregate: $3m+(3m+7)+2=6m+9$.
  
  Correct.

**§7 (boundary invariants).**
- Lemma 7.1, Case 2: the first advance out of an exterior slot $a$ is handled through parent (I3), with these checks:
  - every global predecessor of $x$ is strictly before $a$;
  - $\mathrm{key}(x)<(d,r)\le\mathrm{key}(y)$;
  - the swap is feasible, giving a contradiction.
  
  Later advances use Lemma 3.4(2) on the normalized $E$. The carry qualifiers stay high because $\Phi\cap W=O\setminus S_i\subseteq W\setminus S_j$.
- Lemma 7.2, $a'>a$: Lemma 3.3 is applied on $E$ at $r=a'$.
- Lemma 7.2, $a'=a$: both jobs lie outside $D_a$, so neither qualifies through the injection, and parent (I3) applies. Correct.

**§8 (descriptions).**
- (8.4) and (8.5) are exact global identities. The localization through $D_{a'}\cap P_b$ precedes the use of (8.3), and the child's (I2) is used for (8.4).
- Leaf counts: $(A_m+2)+(A_m+5)=12m+25$ for children, and $A_m+7=6m+16$ for mark prefixes. Correct.

**§9 (running time).**
- (9.3) is a coarse but valid count: $B\cdot S^3\cdot BN^{m+1}=B^5N^{4m+1}$, and $5m(12m+25)+4m+1=60m^2+129m+1$.
- *Gap (minor):* the "+8" exponent in (1.1) is declared "conservative" without an explicit derivation. To fix it, use $N\le mL$, at most $L$ deadline trials, and polynomial preprocessing, which give exponent $60m^2+129m+2$ plus lower-order terms.

**§1.1, §9 table, §10 (claims about the sources).**
- *Gap (minor):* claims about the sources' contents cannot be verified from the proof itself and are not load-bearing. These include the preprint's $O((L+2)^{150020})$ bound, the 25/257 constants, the theorem labels, the drbh repository and the Lean scope file.
- The audit tables claim a one-to-one correspondence with the source lemmas. The solution actually re-proves its own versions, for example with a smaller $G$ and $H^*$. This proves the theorem but is not literally a line-by-line audit of the source text.

**§11 (computer checks).** These are evidence only and are not load-bearing.

## External results used
- **Load-bearing:** none. Only standard facts are used: topological sorting, De Morgan's laws, and the Catalan bound on tree shapes. These are applied correctly.
- **The 2026 preprint and lessons [P], [L1]–[L8]:** used as a template only. Every needed step is re-proved, so nothing depends on their correctness.
- **Background only, not used as premises:**
  - Nederlof–Swennenhuis–Węgrzycki, arXiv:2312.03495;
  - Das–Wiese, arXiv:2501.09091;
  - the drbh repository and the OpenAI Lean scope document.
  
  The solution correctly notes that NSW's bound is not polynomial for fixed $m$. Bibliographic details (pages, venue) were not verified.

## For integration
**Outline in teaching order.**
1. Padding and full schedules (Lemmas 2.3–2.4).
2. Formulas and the DP over $\mathcal F_K$, with soundness (Prop. 2.8) and completeness from a hierarchy (Lemma 2.10).
3. Separators, normalization by sorted $m$-tuples, the one-advance lemma and the shared-cutoff walk (§3).
4. Centers, sides and edge data (§4).
5. Carry and injection updates, and the injectivity into $b'$ that gives $\le m$ injections (§5).
6. Flattening, $H^*$ and the switch upset $G$, with linear leaf counts (§6).
7. (I2) and (I3) for children (§7).
8. Global child formulas (8.4)–(8.5) and relative mark formulas (§8), giving $K_m=12m+25$.
9. Running time (§9).

**Definitions needed.** Frames; cones; upsets and cutoffs; separators; priority orders and normalized schedules; lists, keys and qualifiers; invariants (I1)–(I3); runs; carry, prune, injection and switch pair.

**Still to do.** Give an explicit derivation of the input-length exponent. Either verify the source-comparison claims or remove them. Optionally, state that the proof uses its own (simpler) $G$ and $H^*$, so that the audit is of a reconstruction of the construction rather than of the literal source text.
