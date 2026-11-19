# Independent step-by-step audit of Sections 5.5–8.5

Checker: GPT-6 Astra (OpenAI), effort ChatGPT Pro mode. Date: 15 November 2026. The arguments below were checked directly from the supplied post and its definitions, before reading the earlier checker verdicts. The supplied mathematical return was opened for the requested textual concordance of Lemma 5.5. No earlier checker verdict is used as a mathematical premise.

Each numbered paragraph below confirms the corresponding logical step with its hypotheses and set maps made explicit. The finite-program results at the end supplement these arguments. All assigned statements have been checked; no false mathematical step was found in Sections 5.5–8.5.

## Lemma 5.5 — at most m injection descendants

**Verdict: confirmed, with one wording clarification.** In Step 2 replace “let x_K be its job of least rank” by “let x_K be the least-rank job of K∩W′.” The latter states the chosen domain explicitly and is exactly the choice in the producing return.

1. Fix the child edge W→W′ and retain the injection entries with their creation-event identities, even when two evaluated subsets happen to be equal. Let K be older than K′ and let U→U′ be the edge that created K′. Survival of K to W′ implies that it was retained in the carry out of U. The carry is a list of subsets of the old qualifier union. On U that union is O_U⊆P_{b_U} by I1. The fresh K′ before later trimming is D_{a_U}∩(J\P_{b_U}); hence its intersection with K inside U is empty. Every later operation sends an entry E to itself, to E∩{λ≥r}, or deletes it. Thus the corresponding surviving sets K_final⊆K_then and K′_final⊆K′_then remain disjoint on W⊆U. This proves Step 1 without using a descendant invariant.

2. Pruning retains K precisely because K∩W′ is nonempty. The total rank gives a unique minimum x_K of this intersection. Lemma 5.3 puts this job in W′\S, and (4.6) puts it in P_{b′}. Consequently the set {y∈b′:x_K≺y} is nonempty. Its minimum-rank element f(K) exists and is unique. The entry is an upset of J, so x_K∈K and x_K≺f(K) imply f(K)∈K. This proves Step 2 using the global domain J of the upset; the witness f(K) is outside W′.

3. Lemma 4.5 gives b′⊆W and |b′|=m. For two distinct creation-event identities K,K′, equality f(K)=f(K′) would put this job in K∩K′∩W, contradicting paragraph 1. The specified function f therefore is an injection from the surviving injection identities into the m-element set b′.

4. Injection gives at most m surviving injection entries. A switched creation has only its two initial entries; the root has one. Lemma 5.4 assigns every other entry exactly one injection creation event and never duplicates an entry. Thus adding the possible initial descendants gives at most m+2 entries in every pruned list. A carry out of such a list deletes a prefix and may trim one entry, so it also has at most m injection descendants; the fresh appended injection is counted only after child pruning for the next invariant.

### Concordance with provenance/Q03-solution.md

The return's first proof paragraph (“A new run starts…”) is the post's setup. The return's paragraph beginning “First, any two such entries…” is exactly Step 1, including the containment W⊆U and monotonically shrinking entries. Its next paragraph choosing x_K∈K∩W′ and obtaining a boundary successor is Step 2. Its displayed map f, uniqueness argument, and |b′|=m are Steps 2–3 and the first sentence of Step 4. Its final paragraph adds at most two initial entries, emphasizes the global upset property, and excludes reliance on descendant formulas; these are the rest of Step 4 and the post's final explanatory paragraph. No hypothesis or inference has been removed. The post's antecedent “its job” should be made explicit as above to preserve the return's fully stated selection domain.

## Lemma 6.1 — local replacement of the initial pair

**Verdict: confirmed.**

1. Track the two creation-event identities of the initial pair. A carry retains a suffix of the current list; it trims only the first retained entry. The first initial identity remains earlier than the second at every stage at which both remain. Therefore a carry starting at the second or at an injection deletes the first permanently. Along the history ending at a carry that retains the first, the second has never been the trimmed first retained entry. It remains the original D_{a_0} until pruning deletes it. Pruning deletes it only after its intersection with a node is empty. All later nodes, including U, lie inside that node. A deleted second entry therefore has empty intersection with U.

2. The equality is verified by the inclusion map U→Q_0. On U∩D_{a_0}, the second identity is present whenever this intersection is nonempty, and selects the whole intersection. On U\D_{a_0}, containment Q_0\D_{a_0}⊆G_0 puts every job in G_0. Thus membership in the first surviving identity G_0∩{λ≥k} agrees there with λ≥k. Combining the two disjoint parts proves U∩(union of carried initial identities)=U∩(D_{a_0}∪{λ≥k}). Both displayed factors are upsets, so their union is an upset of J. No inference uses its value outside U.

## Lemma 6.2 — extension of an earlier low cutoff

**Verdict: confirmed.**

1. For a switched edge, H is exactly the initial rank segment of X_U=U\D_{a_U}. The maximum selected rank r (or r=0 for the empty segment) satisfies H=U∩(J\D_{a_U})∩{λ≤r}. The two global factors are downsets in that edge's frame, proving both downward closure and the two-leaf representation of H*.

2. For a same edge, the ordered partition of U is S_0, O_U, Y_U. The low cutoff consists of S_0 and the promoted prefix of O_U; the carry selects exactly the complementary suffix O_U\H. Since U∩P_{b_U}=S_0⊔O_U, subtracting the carry union Φ from U∩P_{b_U} gives H. This proves (6.4) from the actual qualifier identity, with no global assertion about H outside U.

3. Lemma 5.5 bounds the injection identities in the carry by m. Lemma 5.4 represents each by D_{a_V}∩(J\P_{b_V})∩{λ≥r_V}; the suffix may be absent. All three leaves are in the permitted alphabet, and all factors are upsets. Thus their union has a description with at most 3m leaves. A union of nonempty families adds leaf counts and creates no extra leaves at its internal binary union nodes.

4. The initial identities contribute at most two leaves after an equality-preserving replacement on U. In a root run the original J intersected with a rank suffix equals that suffix on all J. In a switched run retaining the first identity, Lemma 6.1 gives D_{a_0}∪{λ≥k} on U; this uses two leaves. When the first identity has disappeared, the second is D_{a_0} with at most one combined suffix, also two leaves. When both disappear there is no initial contribution. These four cases exhaust the ordered initial identities. The global expressions substituted in these cases are all upsets, so their union with the injection expressions is an upset Φ′ with U∩Φ′=U∩Φ and at most 3m+2 leaves. For an empty carry use the one-leaf empty set.

5. Put H*=P_{b_U}∩(J\Φ′). The complement map on formulas of Lemma 2.6 preserves the number of leaves. Thus H* uses at most 1+(3m+2)=3m+3 leaves. Both global factors are downsets, and their intersection with U is (U∩P_{b_U})\Φ=H. This proves all three assertions in the statement: global downward closure, exact restriction to U, and the bound independent of history depth.

## Lemma 6.3 — arrangement at a switch

**Verdict: confirmed.**

1. The root center is its last slot; its switched open side is empty, so a nonempty switched child has a parent W distinct from the root. Let U be W's parent. In the frame that created W, call U's boundaries A<B, its center V, and W's boundaries α<β. Lemma 4.5 and the side construction give A≤α<β≤V<B, with β a genuine slot. Under the explicit time reversal t↦T+1−t, the labels become a_-=rev(B), v_-=rev(V), a=rev(β), b=rev(α), b_-=rev(A). Applying this decreasing bijection to those inequalities gives a_-<v_-≤a<b≤b_- exactly. The image of a genuine slot is a genuine slot, proving the assertion about a.

## Lemma 6.4 — the switch upset

**Verdict: confirmed.**

1. In the current frame, D_{a_-} is an upset; the complements of the two weak predecessor cones are upsets; and H* is an upset because it was a downset in the opposite frame. The identity map on J with reversed order sends a downset in the old order to an upset in the current order. Hence the intersection G in (6.8) is an upset of J.

2. Fix x∈X=W\D_a. The preceding edge U→W was taken in the opposite frame. An old high x would belong by (4.6) to the old predecessor cone of its right boundary. That boundary is current a, and that cone is current D_a. This contradicts x∉D_a, so x is old low and belongs to H. Lemma 4.3 puts H in the old predecessor cone of U's old right boundary, which under reversal is current D_{a_-}. Since x lies strictly after a and a≥v_-, Lemma 2.5 excludes x from current weak predecessor cones at a and v_-. Finally x∈U and H*∩U=H give x∈H*. All four factors defining G have now been verified for x.

3. Let z∈G occur at or before a in the current schedule. The D_{a_-} factor puts it strictly after a_-. The arrangement a<b≤b_- puts z strictly before b_-. These strict inequalities prove z∈U. Therefore the equality H*∩U=H may be applied, yielding z∈H. This localization is essential because equality of H* and H is asserted only on U.

4. For z at or before v_- currently, time reversal puts z at or after U's old center. At the center the weak-cone exclusion directly fails. Strictly after the old center, z∈H⊆S_* and the center separator's low condition put z in the old successor cone of that center, hence in current P_{v_-}. This also contradicts the defining complement factor of G.

5. For v_-<time(z)≤a currently, time reversal puts z before the old center and at or after the old edge's right boundary a. At that boundary z belongs to the weak cone. Strictly after that boundary, z is old low for H, lies on the old side domain E, and Lemma 4.4 makes that boundary a separator for H; it therefore belongs to old D_a=current P_a. The final edge with right boundary at the center has no interval satisfying this strict subcase. In every possible subcase z lies in current widehat P_a, contrary to G's factor.

6. The witness of U supplied these center and separator facts. Between creating W and using its switched side, rescheduling is confined to the open interval W. Jobs at or before current a and all boundary/center slots involved in paragraphs 3–5 remain fixed. The sets H,H* and cones are functions of fixed job sets and precedence. Thus those arguments apply to the current witness. The first switch entry lies inside G, and the second inside D_a; consequently neither has a qualifier at or before a.

## Lemma 6.5 — leaf counts

**Verdict: confirmed.**

1. A surviving injection identity is (D∩(J\P)) intersected with zero or one rank suffix by Lemma 5.4; it therefore uses at most three leaves. A root initial identity is J with zero or one suffix and uses at most two. A switched second initial identity is D_a with zero or one suffix and uses at most two. Combining repeated suffixes is justified by their exact equality {λ≥r}∩{λ≥s}={λ≥max(r,s)} on all J.

2. Formula (6.8) contributes three cone leaves and an H* using at most 3m+3 leaves by Lemma 6.2. Hence G uses at most 3m+6 leaves. Intersecting G with the initial rank suffix adds one, for 3m+7. Later suffix intersections replace that same suffix by the maximum threshold, so the count remains 3m+7 throughout the run. A direction switch deletes these identities before introducing its own initial pair.

3. A pruned list has at most m injection identities and at most two initial identities by Lemma 5.5. Its union therefore has a formula using at most 3m+(3m+7)+2=6m+9 leaves in a switched run. In a root run the same bound covers 3m+2. Taking a carry only discards entries and combines one suffix as in paragraph 1. Empty unions are represented by the one-leaf empty-set atom. Thus A_m=6m+9 applies to every pruned-list union and every carry union, including carries attached to cutoffs whose gaps are empty.

## Lemma 7.1 — exterior qualifier invariant I2

**Verdict: confirmed.**

1. The parent's preparatory rescheduling preserves its three invariants: I1 concerns fixed subsets and fixed boundary slots; I2 concerns exterior jobs whose slots remain fixed; I3 already quantifies over every full schedule of the parent's interval. Pruning removes entries and thus qualifiers, so proving I2 for every qualifier of the pre-pruning list suffices. Fix such z at or before a′.

2. For time(z)>a, all possible positions up to a′ lie in the normalized side E, because a′ is a side position before the center. Lemma 5.3 says every such qualifier in W is high for S_i. A qualifier in slot a′ lies in widehat P_{a′} by membership; a qualifier strictly before a′ lies in P_{a′} by the high condition of the separator at s_i=a′. This proves the first case.

3. For time(z)≤a, an injection qualifier is impossible because its entry lies in D_a. A switch-pair qualifier is impossible by Lemma 6.4 and the successor-cone property for its second entry. Hence this is a same update and z qualifies through its carry. Lemma 5.1 makes z an old qualifier. Parent I2 supplies y∈a with z=y or z≺y. Since the carry union is an upset of J, y also belongs to it. This proves both the existence of a genuine boundary job and its survival through the carry. When a′=a the same witness immediately proves the desired conclusion.

4. Assume a′>a. Every actual advance from a through a′ uses a cutoff S_j⊆S_i, including intermediate unmarked steps. Lemma 5.1 gives carry∩W=O\S_i. Thus every carry qualifier in E is outside every such S_j. At the first advance a→t the chosen exception x∈S_j∩E satisfies x∉D_a. Every predecessor w of x occurs before t. Membership in slot a would directly put x in D_a. A predecessor with a<time(w)<t belongs to E and to the downset S_j. Earliest-exception minimality puts w in D_a, and transitivity then puts x in D_a. Both alternatives are impossible; all predecessors of x in J occur strictly before a.

5. Parent I1 puts x∈O because x∉D_a. Since S_0⊆D_a, x entered the low set by a promotion from O. The carry threshold (d,r) is the least old key in O\S_i; all promoted jobs in S_i∩O have smaller keys. Hence key_old(x)<(d,r). The qualifier y belongs to the carry, so Lemma 5.1 gives key_old(y)≥(d,r). Parent I3 applies to the currently chosen replacement schedule of W, x∈W\D_a, and y∈a, and prohibits their exchange.

6. If y had no successor at or before t, this exchange would preserve every precedence relation: x's predecessors are before a by paragraph 4, its successors are after its old time t, y's predecessors are before its old time a, and its successors would be after t. The sizes of both slots remain m. A companion at either destination slot cannot be comparable in the forbidden direction, because that would be one of the predecessor/successor relations just ruled out. Thus the exchange would be a full schedule, contradicting I3. Therefore y has a strict successor y_1 with a<time(y_1)≤t. The carry is an upset, so y_1 qualifies; it belongs to E and is high for S_j.

7. At time(y_1)=t, the desired successor at the first target is already present. For time(y_1)<t, apply Lemma 3.4(2) to the normalized E with M=L=S_j∩E and exterior position a. Restricting the total priority and prefix to E preserves their prefix relationship. Condition (a) at the exterior boundary has no E-job before it; x is still the earliest exception. The lemma gives a strict successor of y_1 in t, and the upset carry contains it. In either case there is a carry qualifier in t strictly above y. It cannot equal the low x.

8. At each subsequent genuine-slot advance s→t′, the carry qualifier already obtained at s is high for the currently used S_j. Lemma 3.4(2) with M=L=S_j∩E sends it to a strict successor at t′, again in the carry. The walk has finitely many advances and reaches a′. Transitivity gives a job of a′ strictly above y, hence also strictly above z when z=y or z≺y. Therefore z∈P_{a′}. This completes I2 for every pre-pruning qualifier and hence every pruned qualifier.

## Lemma 7.2 — exterior exchange invariant I3

**Verdict: confirmed.**

1. For x∈W′\D_{a′}, child I1 from Lemma 5.3 guarantees qualification. The hypothesis already gives qualification of y after pruning. Lemma 5.2 applies with x inside the pruning domain W′ and transfers key_child(x)<key_child(y) to the pre-pruning list, including the possibility that y belonged to deleted exterior entries.

2. For a′>a, the slot a′ lies in normalized E. Both x and y lie in W, so Lemma 5.3 transfers the pre-pruning comparison to the priority order of E. The arbitrary replacement of W′ lies entirely after a′ and is a full replacement by Lemma 2.4. It changes no job at or before a′ and preserves the set of E-jobs after a′. An exchange feasible in J would therefore produce a full E-schedule with an improved slot at a′, contradicting Lemma 3.3 with its allowed suffix rescheduling. This establishes I3 in this case.

3. For a′=a, a switched update has no boundary qualifier by Lemma 6.4, so it supplies no pair satisfying the statement's hypotheses. For a same update, neither x∉D_a nor the boundary job y can qualify through the injection D_a\P_b; for y this follows from Lemma 2.5. Both qualify through the carry. Lemma 5.1 therefore transfers their strict pre-pruning comparison to the old parent keys. The parent has x∈W\D_a and old qualifier y∈a. Its current preparatory schedule followed by the arbitrary child replacement is one full replacement of W. Parent I3 prohibits precisely the proposed exchange, proving this case too.

## Proposition 7.3 — construction and induction order

**Verdict: confirmed.**

1. At the root the entry J is an upset, both boundaries are virtual, I1 holds from P_b=J, and I2/I3 have no boundary job. The root count and leaf bounds hold directly. Assume the construction data and all three invariants are established through a node W. Lemma 2.4 and Corollary 3.7 allow the center preparation; normalization of each side is an existence choice over a finite nonempty family. Lemmas 4.3–4.5 then yield priority prefixes, terminating side walks, marks, and all nonempty gap children with their edge data.

2. A same update uses W's already constructed list. A switched update refers to the edge U→W, which exists strictly earlier in the induction. Lemma 6.2 computes its short extension from its rank prefix or its already recorded carry; the flattening equality of 6.1 refers only to initial entries of that earlier run. Lemma 6.4 then constructs G using the already fixed boundaries and center of U. Thus neither an unconstructed child's I2/I3 nor its leaf bound enters the switch construction.

3. New entries are global upsets. Lemma 5.3 proves the exact qualifier identity and child I1 before any further boundary invariant is invoked. Lemma 5.5 proves the pruned count from old I1, that identity, and known edge cones. Lemmas 6.1–6.5 prove leaf bounds using already existing earlier-run descriptions and the just proved count. Lemmas 7.1 and 7.2 then establish child I2 and I3 from parent I2/I3 and the current normalized sides. This order supplies all induction hypotheses for each child.

4. Each child omits its parent's center slot and consists of complete slots, so |W′|/m≤|W|/m−1. A branch has at most N/m nonempty nodes. Each side has only finitely many promoted jobs and marks, hence each node has finite degree. Induction on the remaining slot count gives a finite whole tree. Copies of witnesses at branching ensure that a modification below one child changes no witness used by another child.

## Lemma 8.1 — cutoff predicates

**Verdict: confirmed.**

1. On a same side, U=W is partitioned as S_0⊔O⊔Y, with W∩P_b=S_0⊔O. Lemma 5.1 makes Φ_i∩W exactly the unpromoted O\S_i. Thus W∩(P_b\Φ_i)=S_0∪(O∩S_i)=S_i. The carry union has A_m leaves by Lemma 6.5, complementation preserves them by Lemma 2.6, and the additional P_b factor adds one, giving A_m+1.

2. On a switched side, S_i is exactly the set of X=W\D_a jobs of rank at most the last promoted rank r_i, with r_i=0 for no promotions. Intersecting (J\D_a)∩{λ≤r_i} with W gives that set exactly. This expression has two leaves and is within A_m+1. Both cases include empty gaps because their cutoffs and carries are defined before selecting nonempty children.

## Lemma 8.2 — global descriptions

**Verdict: confirmed.**

1. For the high part, a job x∈W′\S qualifies by 5.3 and belongs to P_{b′} by 4.5. Its time lies strictly after a′, so 2.5 excludes it from widehat P_{a′}. Conversely, membership in the right side of (8.4) implies time(x)<b′. Were time(x)≤a′, child I2 (Lemma 7.1) would place this qualifier in widehat P_{a′}, contradicted by the last factor. Thus a′<time(x)<b′, giving x∈W′; 5.3 then puts it outside S. This proves equality as subsets of J without intersecting a parent formula.

2. Let z belong to the right side of (8.5). The D_{a′} and P_b factors give a′<time(z)<b, and a′≥a. Hence z∈W. The restriction equality of 8.1 is now applicable and yields z∈S_i. Since S_i⊆S_*, a low z at the center belongs to its weak successor cone; a low z after the center belongs to D_v by the center separator. The factor J\widehat D_v excludes both, so z lies in the side E before v.

3. Within E, z is low for S_i. At b′ it belongs to the weak successor cone. After b′, Lemma 4.4's common-cutoff separator puts it in D_{b′}; for the last edge b′=v this alternative was already excluded by paragraph 2. Thus the factor J\widehat D_{b′} forces time(z)<b′. Together with time(z)>a′ this yields z∈W′∩S_i.

4. Conversely, a low job z∈W′∩S_i lies in D_{a′}∩P_b by 4.5 and in the cutoff predicate by 8.1. It occurs before both b′ and v, so 2.5 excludes it from their weak successor cones. It satisfies all factors of (8.5). The two inclusions prove the exact global equality.

## Lemma 8.3 — relative descriptions at marks

**Verdict: confirmed.**

1. In the chosen working frame, H_*=P_b on a same side and H_*=J\D_a on a switched side satisfy H_*∩W=S_* by the center definitions. Lemma 3.1 at center v therefore gives W∩B_v(H_*) equal to the open side E before the center. This formula requires only a relative equality on W.

2. Every side mark has a representation z=s_i with i≥1. Lemma 4.4 (or directly 3.6 for the final promoted cutoff) makes z a separator for S_i on E. Lemma 8.1 gives E∩widetilde S_i=E∩S_i. Applying Lemma 3.1 on E yields its prefix before z. Intersecting with B_v(H_*) first restricts the formula to E within W, so W∩F_z is exactly all W-jobs before z in the working frame. Repeated positions cause no difficulty: a chosen occurrence i has the requisite separator property.

3. Under forward time this is the requested prefix. Under reversed time, the three disjoint sets (working prefix), slot z, (working suffix) partition W. The reversal map sends the working suffix to the original prefix. Hence W∩((J\F_z)\z) is exactly the original-time prefix. Lemma 2.6 gives a same-leaf complement formula, and intersecting with the complemented slot atom adds one leaf. The same argument covers the center's three-leaf formula.

## Lemma 8.4 — uniform leaf budget

**Verdict: confirmed.**

1. In (8.4), the qualifier union contributes at most A_m leaves by 6.5, and the two cone factors each contribute one. This high-part formula therefore uses A_m+2 leaves. In (8.5), 8.1 contributes A_m+1 leaves for the cutoff predicate and its four other cone factors contribute four; this low-part formula therefore uses A_m+5. Their union is exactly W′ by 8.2, and binary union adds their leaf counts. The result is 2A_m+7=2(6m+9)+7=12m+25.

2. The expression B_v(H_*)=P_v∪(H_*∩(J\widehat D_v)) has three leaves because H_* is a one-leaf cone or complemented cone. The second separator expression B_z(widetilde S_i) has 1+(A_m+1)+1=A_m+3. Equation (8.7) intersects the two expressions, giving A_m+6; reversal in (8.8) adds one for the complemented slot. Thus every original-time marked prefix uses at most A_m+7=6m+16 leaves.

3. Every genuine boundary slot has exactly m jobs, placing all cones and slot-membership tests in Section 2's atomic alphabet. At virtual boundaries the displayed definitions are J or the empty set and each uses one permitted constant atom. Reverse-frame ranks/cones are explicitly permitted in that alphabet. No uncounted node-membership atom or parent formula occurs in these expressions. Finally 6m+16≤12m+25 follows from 6m+9≥0, which holds for the stated m≥3.

## Theorem 8.5 — hierarchy

**Verdict: confirmed.** The earlier foundations are checked in the companion B_foundations audit; the derivation below identifies each use.

1. Proposition 7.3 supplies a finite construction starting from any full schedule of J. Every nonempty node retains a full-schedule witness of J by interval replacement and marks its center, so at least one slot is marked. Sorting the marks in original time gives exactly its gap children, because each side's nondecreasing walk positions create one gap per strict successive position; the center joins the two sides and the original external boundaries complete the list.

2. The root is J and has its one-leaf atom. Every nonroot node is one of these gaps; 8.2 and 8.4 give its global description with at most K_m=12m+25 leaves. Lemmas 8.3–8.4 give each marked original-time prefix a relative formula with at most 6m+16≤K_m leaves. Children inherit copies of their parent's current witness by the construction. These verify the four clauses of Definition 2.9 individually, proving the claimed hierarchy without any depth accumulation in descriptions.

## Direct dependency corrections for this portion

This list records genuine uses, including equation references that the existing literal-citation extractor omitted. A dependency on a set's definition is identified separately rather than replaced by an invented numbered lemma.

| Result | Direct numbered/invariant dependencies to record |
|---|---|
| 5.5 | 4.5, 5.1, 5.3, 5.4; I1; injection definition (5.2) |
| 6.1 | 5.1, 5.4; pruning/run definitions; switch-pair definition (5.4) |
| 6.2 | 2.6, 5.3, 5.4, 5.5, 6.1; cutoff construction |
| 6.3 | 4.5; frame reversal definition |
| 6.4 | 2.5, 4.3, 4.4, 4.5, 6.2, 6.3; equation (6.8) |
| 6.5 | 2.6, 5.4, 5.5, 6.2; equations (5.2), (5.4), (6.8) |
| 7.1 | 2.5, 3.4, 3.6, 4.3, 4.4, 5.1, 5.3, 6.4; I1, I2, I3 |
| 7.2 | 2.4, 2.5, 3.3, 5.1, 5.2, 5.3, 6.4; I1, I3 |
| 7.3 | 2.4, 3.7, 4.3–4.5, 5.3, 5.5, 6.1–6.5, 7.1, 7.2; root invariants |
| 8.1 | 2.6, 4.3, 5.1, 6.5; equations (8.1), (8.2) |
| 8.2 | 2.5, 4.3, 4.4, 4.5, 5.3, 7.1, 8.1; center separator |
| 8.3 | 2.6, 3.1, 4.4, 8.1; center cutoff definition |
| 8.4 | 2.6, 6.5, 8.1, 8.2, 8.3; atomic formula alphabet |
| 8.5 | Definition 2.9, 7.3, 8.2, 8.3, 8.4 |

The earlier “no numbered statement is cited” Uses line for 8.4 was a description of literal citation strings, not a sufficient dependency account: its proof uses the earlier proved meanings and size bounds of (8.4)–(8.8). The corrected line records these mathematical dependencies explicitly.

## Independent finite construction check

The program `code/B_hierarchy_check.py` and its complete output `code/B_hierarchy_check_output.json` are included. This newly written program constructs the whole hierarchy for 255 feasible DAGs using the seed 20261115 and the fully specified layered sampling families printed in the output. Machine counts 3, 4, and 5 and 3–6 original slots occur. Every normalization is obtained by exact recursion over minimal-job m-subsets in lexicographic priority order. It constructs and checks actual global entry sets, exact cutoff predicates, earlier-cutoff extensions, direction changes, capacity witnesses, and both parts of each global child formula. For each nonvacuous I3 pair it enumerates every feasible full replacement of that node interval and checks every prescribed exchange globally. All assertions passed.

| Measured item | Count |
|---|---:|
| Input DAGs | 255 |
| Constructed nodes / I1 and I2 checks | 754 |
| Actual switched children | 132 |
| Injection-to-boundary witness checks | 499 |
| Earlier-cutoff extensions | 499 |
| Cutoff restriction identities | 7069 |
| Global child formulas | 499 |
| Relative side-mark formulas | 978 |
| Nonvacuous I3 pairs | 11 |
| Full replacements enumerated for I3 | 8 |
| Globally checked exchanges | 12 |
| Qualifiers at their left boundary | 48 |
| Qualifiers strictly before their left boundary | 5 |
| Surviving-first initial-pair replacements encountered | 0 |

The run's maximum node depth is 5, maximum observed surviving injection count is 1, and maximum observed global-child formula leaf count is 10. It encountered zero surviving-first initial-pair replacements, so the audit of that exact history case is the arbitrary-history proof of Lemma 6.1 above. The finite family and these measured limits are stated precisely; the universal mathematical conclusions follow from the stepwise arguments, not an extrapolation of these measurements. Cases exercising a direction switch or a nonvacuous exterior exchange are printed completely with their arc lists in the output.
