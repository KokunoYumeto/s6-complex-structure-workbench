# Independent proof audit: Sections 2–5.4

Checker: GPT-6 Astra (OpenAI), effort ChatGPT Pro mode. Date: 15 November 2026, Europe/Berlin. The checker had the post and original return; the three previous reports were available as provenance but were not used as premises. The arguments below were derived from the definitions. Section and equation numbers refer to the post, whose numbered statements retain the return's numbering.

## Lemma 2.1 — proved as stated

**Step 1, the strict order.** A positive directed closed walk contains a directed cycle: select a repeated vertex with a shortest positive segment between equal occurrences. Acyclicity therefore excludes x≺x. Concatenating the paths witnessing x≺y and y≺z gives a positive walk from x to z; deleting repeated segments gives a path. This proves transitivity on precisely the explicitly given vertex set.

**Step 2, preservation of inequalities.** For a path v₀,…,vₖ, the arc inequalities give τ(v₀)<…<τ(vₖ), hence the endpoint inequality. Conversely an arc is a path of length one. The identity map on schedules is therefore a bijection between schedules respecting all arcs and schedules respecting the transitive closure.

**Step 3, the rank map.** In every nonempty remaining induced order, following an alleged predecessor forever repeats a vertex, so a minimal vertex exists. Remove the least identifier among minimal vertices. A predecessor x of y cannot remain when y is removed, since otherwise y is not minimal in the transitive restriction. The removal-position map λ:V→[n] is a bijection with x≺y⇒λ(x)<λ(y). The tie rule makes the function deterministic. Padding adds isolated vertices, so the argument also produces the required λ:J→[N].

## Lemma 2.2 — proved as stated

**Step 1, augmented graph.** On a machine, unit processing and no overlap imply s(v)≥s(u)+1 for consecutive jobs in increasing real start time. Each precedence arc has the same inequality. Summing around a directed cycle would give s(u)≥s(u)+k for k>0, so the augmented graph is acyclic.

**Step 2, integer recurrence.** Process the augmented graph in topological order and define s′ by the maximum in the post. Every predecessor has already received an integer, so the recurrence is defined and integer valued. Induction gives s′(u)+1≤s(u)+1≤s(v) for every incoming arc; the zero term is ≤s(v) by nonnegative original starts. Hence s′(v)≤s(v).

**Step 3, explicit schedule transformation.** Preserve the original assignment μ and set τ(v)=s′(v)+1. Consecutive jobs on a machine are separated by at least one unit, and transitivity extends this to all pairs on that machine. Original precedence arcs are respected as well. Every new completion time is τ(v)≤s(v)+1. The transformation is explicit; it preserves feasibility and weakly decreases makespan. The reverse embedding of an integer-slot schedule uses start τ(v)−1 and any injective assignment of each slot's jobs to machine labels.

## Lemma 2.3 — proved as stated

**Step 1, capacity.** A map to T slots with at most m jobs per slot contains at most mT jobs. Thus n>mT is an exact rejection test.

**Step 2, extension.** Label the dummy vertices n+1,…,mT. Enumerate empty machine/time positions in lexicographic (time,machine) order and fill them with these dummy vertices in identifier order. The dummies have no order relations, so the resulting partition of J consists of T antichains of size m and respects every original relation.

**Step 3, restriction.** Restrict any full schedule of J to V. Every slot now contains at most m jobs, and each original arc still has increasing slot numbers. This gives both directions of the required feasibility equivalence. The bound N=mT≤mn follows from T≤n. An optimization implementation need only pad T<n, since a topological schedule handles T≥n.

## Lemma 2.4 — proved as stated

**Step 1, fixed interval length.** Every full schedule of W uses |W|/m slots, and W originally occupies exactly that many consecutive slots. Thus substitution has a well-defined position-preserving map outside the interval and a bijective assignment of W to the same interior slots.

**Step 2, every precedence case.** A relation with both endpoints inside W is respected by the substituted full schedule. A relation with both outside has unchanged times. With one endpoint outside, its time lies on one fixed side of the entire interval; every possible new time of the inside endpoint stays on the other side of that boundary. Feasibility of the original witness fixes the permitted direction. This checks all ordered pairs in the transitive relation, including those whose original graph paths leave W.

## Frames, cones, and the normalization selector

**Reversal map.** For a T-slot full schedule τ, define Rτ(x)=T+1−τ(x), reverse the strict relation, and replace λ by N+1−λ. The inequalities reverse exactly, slot sizes are preserved, and R² is the identity. Under this bijection P in one frame is D in the other, with the same equality for weak cones. No comparison of frames is used without these explicit transformations.

**Cone closure.** For x∈D_a and x≺y, a witness u∈a with u≺x also satisfies u≺y. The same proof includes x∈a for the weak cone. Reversing arrows proves closure of P_a and its weak version. Taking complements reverses the closure implication. A rank suffix is closed upwards because ranks increase on ≺. These arguments hold even for the m-subsets enumerated as atoms that are not antichains; Lemma 2.5 separately uses the antichain property for time.

**Exact selector used by the existence proof.** For each schedulable W and priority bijection π, the finite set of full schedules is nonempty. Map each schedule to the concatenation of its sorted priority tuples. Because π is injective, this encoding determines the ordered sequence of job sets uniquely. Select its lexicographically least element, then decode using π⁻¹. This defines the normalization map used in Section 3. It stays in the feasible set and changes the exterior only through the interval-replacement map of Lemma 2.4. The finite search of Section 2 does not evaluate this selector; the selector constructs its completeness certificate.

## Lemma 2.5 — proved as stated

**Step 1, strict cones.** Membership x∈P_a provides y∈a with x≺y, so τ(x)<τ(a); membership x∈D_a similarly gives τ(x)>τ(a). Equality of times would violate feasibility. Since the slot is an antichain, neither strict cone contains a member of a.

**Step 2, weak and virtual versions.** Adding the slot gives the corresponding weak temporal implications. For the virtual position 0, D=J and P=∅ satisfy them directly; for position T+1 the prescribed sets are reversed. These conventions are the ones used whenever a boundary in a subsequent formula is virtual.

## Lemma 2.6 — proved as stated

**Step 1, recursive map on formula trees.** Define c on leaves by toggling the permitted complement flag, and define c(F∩G)=c(F)∪c(G), c(F∪G)=c(F)∩c(G). Structural induction gives [c(F)]=J\[F]. Each leaf maps to one leaf, so the leaf-count function is preserved exactly. In particular, F\G is represented by F∩c(G) with the sum of the two leaf counts.

## Lemma 2.7 — proved as stated

**Step 1, alphabet.** Counting generously, the two constants, thresholds in both frames, five subset/cone types in both frames, and complement flags give at most 4+8(N+2)+20·binom(N,m) atoms. For N≥m≥3, this is ≤64N^m. Treating coincident evaluated atoms as different syntactic choices only increases the bound.

**Step 2, trees and labels.** An ordered full binary tree with ℓ leaves has ℓ−1 internal vertices; its count is the Catalan number C_(ℓ−1)≤4^(ℓ−1)≤4^ℓ. There are 2^(ℓ−1) operation assignments and at most (64N^m)^ℓ leaf assignments. Their product is ≤(512N^m)^ℓ. Summing for 1≤ℓ≤K gives B=K512^K N^(mK), exactly the constant used in the cost audit.

**Step 3, actual enumeration.** Enumerate the finite tree encodings and labels, evaluate each leaf from the reachability relation and rank, and combine bit vectors at internal vertices. Equality is bitwise equality on J; keeping the earliest representative for each vector preserves precisely the image of the evaluation function. The separate Part A analysis supplies tape costs for this construction and pairwise deduplication.

## Proposition 2.8 — proved as stated

**Step 1, well-founded acceptance.** Each state contains a nonempty m-slot Z. Its L and R omit Z. Each transition gap L′\(L∪Z) also omits Z, and therefore has size less than |W|. Processing cardinalities increasingly makes every lookup either an already computed value or the stipulated false value outside the family. The empty schedule starts the induction.

**Step 2, partition induced by a path.** The inclusion Lᵢ∪Zᵢ⊆Lᵢ₊₁ gives Lᵢ₊₁=(Lᵢ⊔Zᵢ)⊔Aᵢ by the definition of Aᵢ. Induction expands this into the prefix of (2.3). At the last state, W=L_k⊔Z_k⊔R_k closes the partition. These equalities prove that no job is repeated or omitted; successive left sets also have strictly increasing sizes, so a path cannot cycle.

**Step 3, precedence across the partition.** A later marked slot Zⱼ has every earlier piece inside Lⱼ, and state compatibility excludes Zⱼ≺Lⱼ. A later gap Aⱼ is contained in Rⱼ, whereas every earlier piece is contained in Lⱼ∪Zⱼ; the two compatibility conditions exclude all such backwards relations. Internal relations are respected by the inductively supplied schedules. Concatenation therefore gives a full schedule of W.

**Step 4, witness map.** Store a predecessor state only at its first successful discovery, together with the accepted smaller-set witnesses. Backtracking produces the finite state path; concatenate the stored gap schedules and the explicit Z slots in order. The established disjoint partition bounds its output by |W| job occurrences. This is an explicit decoding map from an accepting path to a schedule, requiring no selection from an unrecorded feasible set.

## Definition 2.9 — well-defined and used with its stated meaning

**Step 1, separate witnesses.** At each node the interval is a subset of the same global job universe J and inherits its full transitive relation. Children receive copies of the current full witness. Rescheduling a descendant in one copy does not change an ancestor's sets, labels, formulas, or another branch's witness. Every child omits a marked m-slot, reducing |W|/m by at least one. Finite branching and this integer depth bound give a finite tree.

## Lemma 2.10 — proved as stated

**Step 1, states from marks.** At mark zᵢ, use its actual original-time prefix Lᵢ and suffix Rᵢ. The hierarchy provides the required relative formula. Feasibility of the node witness excludes every backward relation in the state tests. Thus every such triple is among the candidates enumerated by the dynamic program.

**Step 2, acceptance by size induction.** The first prefix, final suffix, and gaps are exactly empty sets or child nodes. Their acceptance follows from the empty base value or the induction on smaller node sizes. Consecutive marks satisfy Lᵢ∪zᵢ⊆Lᵢ₊₁, with the accepted child as difference. These triples form an initial-to-final path. Induction therefore accepts the root J.

## Lemma 3.1 — proved as stated

**Step 1, prefix inclusion.** For a job before z, a high job is in P_z by separator clause (a); a low job is in H and outside the weak successor cone by its strict earlier time. Both cases enter B_z(H).

**Step 2, reverse inclusion.** A P_z job is strictly earlier by Lemma 2.5. A job in U∩H\widehat(D_z) is low and neither at z nor after z: the first is excluded by the weak cone and the second by separator clause (b). Therefore B_z(H)∩U equals the exact prefix. No membership information about H outside U is needed.

## Lemma 3.2 — proved as stated

**Step 1, explicit transformation.** Apply time reversal R, order reversal, and the cutoff map S↦U\S. Closure of S downwards makes its complement closed downwards in the reversed order. Original low-after/successor clause (b) becomes high-before/predecessor clause (a); original clause (a) becomes clause (b). Each transformation is an involution, proving the equivalence in both directions.

## Lemma 3.3 — proved as stated; rewritten layout preserves the argument

**Step 1, unchanged prefix.** Suffix replacement keeps all slots through r fixed. Swapping y at r with x in that suffix subsequently changes only r and the slot of x. Thus the encoded schedule agrees with the minimizing schedule in every coordinate preceding the r tuple.

**Step 2, sorted tuple comparison.** Let α=π(x)<β=π(y). Replacing β by α weakly increases the count of tuple entries ≤q for every q, since its change is 1_(α≤q)−1_(β≤q)≥0. For each order-statistic index k, the smallest threshold with at least k entries therefore weakly decreases. The sum decreases by β−α>0, so at least one coordinate decreases strictly. The first changed tuple coordinate consequently decreases. This proves the comparison for every m, with the concrete map on multisets and sorted coordinates given explicitly.

**Step 3, minimizing contradiction.** Feasibility of the hypothesized exchange would place the new encoded schedule inside the same finite comparison set, with the same earlier coordinates and a smaller first changed coordinate. That contradicts the selected minimum. Suffix reordering is already included in this comparison, so later uses retain precisely the lemma's quantifier.

**B.2 concordance.** The return's Lemma 3.3 has one paragraph: unchanged earlier slots; replace a larger priority by a smaller one; all order statistics weakly decrease and one strictly; contradict minimality. The post's Steps 1, 2, 3 are this same sequence. Its threshold-count and sum sentences supply a proof of the order-statistic assertion rather than changing its hypotheses or conclusion. The “where m enters” sentence only records that the tuple length is arbitrary. The report records this as a full semantic comparison, not a character-for-character identity.

## Lemma 3.4 — proved as stated

**Step 1, predecessors of the earliest exception.** For w≺x in U, precedence extension puts w in L, and feasibility puts w before t. A w at s would witness x∈D_s. A w between s and t would itself be an earlier L job; minimality of t forces w∈D_s, again giving x∈D_s by transitivity. Thus every such w is strictly before s. When s is the exterior boundary, the same alternatives exhaust the jobs of U before t.

**Step 2, first forced successor.** Take high y at r with s≤r<t. Absence of any successor of y through time t makes the swap x↦r,y↦t feasible: all predecessors of x are before s; all its original successors are after t; predecessors of y are before r; and its alleged successors are after t. These inequalities also exclude conflicts with companions in the destination slots. Exterior jobs remain on their original side of U. Because x∈M and y∉M, their priorities improve the earlier slot, contradicting Lemma 3.3. Thus y has a successor no later than t.

**Step 3, propagation to t.** A successor of a high job remains outside the prefix M. Repeat the preceding swap argument for that successor when it occurs before t. Its time increases strictly at each iteration, so the finite sequence reaches t. Transitivity gives a strict successor of the original y at t, proving conclusion (2).

**Step 4, all high jobs before t.** A high job at or after s uses conclusion (2). A high job before s has a successor w in the s slot by clause (a). Closure of the high set puts w outside M, and conclusion (2) moves its witness to t. Transitivity then puts the original job in P_t. An exterior s has no U jobs before it, so that alternative is vacuous. This proves clause (a) at t.

## Lemma 3.5 — proved as stated

**Step 1, invariant and termination.** Use Lemma 3.4 with M=L at each earliest-exception move. It preserves clause (a), and every target is strictly later. The number of positions is finite. At the last position absence of exceptions is exactly clause (b). An already separating position has no exception, so its image under the walk is itself.

## Lemma 3.6 — proved as stated

**Step 1, the first move.** Enlarging S to S∪{p} removes one high job, preserving clause (a). All old low jobs after s are already in D_s. Thus any first exception is exactly p; the first target is p's slot. Lemma 3.4 with M=L=S⁺ proves clause (a) for S⁺ there. Adding p back to the high set changes no before-target condition because p is at that target, proving clause (a) for S as well.

**Step 2, later moves and stopping.** Every later exception lies after p's slot, so it belongs to S. Lemma 3.4 applies with M=S,L=S⁺, and also with M=L=S⁺, preserving both versions of clause (a). At the terminal position clause (b) for S⁺ implies clause (b) for S by inclusion. The no-move case already satisfies both clauses. Restricting a priority prefix from W to U preserves its order-prefix property; promoting a vertex outside U changes no restricted set and therefore yields the identity walk.

## Corollary 3.7 — proved as stated

**Step 1, admissible priority.** Place S first and U\S second, ordering each by rank. A relation from the second block to the first contradicts the downset property of S. Within each block rank extends precedence. This is a legitimate total priority order.

**Step 2, separator construction.** Apply the explicitly defined normalization selector to a feasible schedule of U. Its first slot separates the empty cutoff because there are no earlier jobs and no low jobs. Promote S in priority order and apply Lemma 3.6 at each promotion. Positions stay genuine slots and never decrease, and the final one separates S. Nonemptiness of U guarantees a first slot.

## Lemma 4.1 — proved as stated

**Step 1, the order map.** Every entry containing x also contains y for x≺y. Hence the largest index M(y) is at least M(x). A strict index increase gives the lexicographic inequality, and equal indices give it from λ(x)<λ(y). The map x↦(M(x),λ(x)) is injective because λ is injective; this justifies every minimum-key choice.

## Lemma 4.2 — proved as stated

**Step 1, tag frame.** I1 partitions W into O⊆P_b and W\O⊆D_a. Thus W⊆D_a∪P_b. Removing D_a leaves X⊆P_b; removing P_b leaves Y⊆D_a. Both X=W∩(J\D_a) and W∩P_b are relative downsets by the cone closure argument above.

**Step 2, reversed frame.** Under reversal, the new a is old b and the new b is old a. New D_a=old P_b and new P_b=old D_a. Substitution in the displayed inclusions interchanges X and Y and leaves the cover unchanged. The same closure argument proves the new cutoffs. Thus the claim really holds in either working frame.

## Lemma 4.3 — proved as stated

**Step 1, same-side blocks.** Since O⊆P_b, the three sets S₀=(W\O)∩P_b, O, and Y=W\P_b are disjoint and cover W. A predecessor in W of x∈S₀ is in P_b, and qualification of that predecessor would force qualification of x; hence it lies in S₀. Also no Y vertex precedes a P_b vertex. These facts exclude relations backwards between blocks. Ranks order S₀,Y and Lemma 4.1 orders O.

**Step 2, same-side prefixes.** Adding O in increasing key order makes each Sᵢ an initial segment, ending at W∩P_b. Every Sᵢ is therefore contained in P_b. The initial S₀ lies in D_a by I1 because it contains no qualifier.

**Step 3, switched-side order.** X is a downset by Lemma 4.2, so placing it before W\X and sorting each by the working-frame rank respects precedence. Promotion by rank gives all and only the prefixes of X, ending at X⊆P_b. The initial cutoff ∅ is contained in D_a.

## Construction before Lemma 4.4

**Center and side maps.** Corollary 3.7 gives a separator for W∩P_b in the tag frame; Lemma 2.4 installs that schedule. Reversal sends its cutoff to W\D_a on the switched side by Lemma 3.2. Each open side E is then replaced by its normalization-selector output for the restricted priority order. Jobs on each side of the fixed center are unchanged as sets, and its separator clauses quantify exactly these sets, so its separator property survives. Root center selection at the last slot separates J directly and leaves no switched side.

## Lemma 4.4 — proved as stated

**Step 1, common endpoint labels.** The left boundary a separates S₀∩E because S₀⊆D_a. After promotion i, Lemma 3.6 makes sᵢ a separator for Sᵢ₋₁ and Sᵢ. Thus sᵢ and sᵢ₊₁ both separate Sᵢ. Repeated positions satisfy the same conclusions. The final center's separator clause (a) on W puts every high job of its earlier side E in P_v.

## Lemma 4.5 — proved as stated

**Step 1, exact gap enumeration.** A nondecreasing finite sequence has one transition between each pair of consecutive distinct values; take the last occurrence of the earlier value and the next index. These are precisely the strict steps sᵢ<sᵢ₊₁ used for children. Its right endpoint is always an actual side slot or the center, and its left endpoint is a side slot or a.

**Step 2, labels and shrinking.** A low child job lies after a′, so the separator clause (b) there puts it in D_a′. It also lies in Sᵢ⊆P_b by Lemma 4.3. A high child job lies before b′, so Lemma 4.4 puts it in P_b′, including the center endpoint. Every child omits the center's m jobs, proving strict decrease. At the root the center is last, so no switched child can occur.

## Lemma 5.1 — proved as stated

**Step 1, qualifier identity.** Let j be the greatest old entry containing a job. With j>d, that entry survives; with j=d, survival is exactly λ≥r; with j<d, all entries containing the job were deleted. These alternatives are equivalent to old key≥(d,r), including arbitrary exterior jobs.

**Step 2, order transfer.** For each surviving job the exact key map is (j,λ)↦(j−d+1,λ). Subtracting the same integer from the first coordinate preserves and reflects every lexicographic comparison. The trimmed entry stays upward closed because rank suffix and old entry are both upsets; the other entries are unchanged.

## Lemma 5.2 — proved as stated

**Step 1, effect of deletion.** Let M(z) and R(z) be respectively the largest old and retained old indices containing z. Because x∈W′, every entry containing x meets W′ and is retained, so R(x)=M(x). For exterior y only R(y)≤M(y) is guaranteed. The increasing relabeling of retained indices preserves the comparison of R values.

**Step 2, both key cases.** R(x)<R(y) yields M(x)<M(y). When R(x)=R(y) and λ(x)<λ(y), either M(y) exceeds that index or equals it; the first alternative decides by index and the second by rank. This proves exactly the one-way inequality needed in Lemma 7.2, with its required hypothesis x∈W′.

## Lemma 5.3 — proved as stated

**Step 1, same update.** By the cutoff promotion order and Lemma 5.1, the carry intersects W in O\S and preserves that group's keys. Lemma 4.2 gives W∩(D_a\P_b)=W\P_b=Y. Since Y∩O=∅, the appended injection contributes exactly the last priority block, with its last index overriding no carry job inside W. Hence the union is (O\S)⊔Y=W\S, with precisely the restricted side-priority order.

**Step 2, switched update.** On X, G contains every job, so G∩{λ≥h} selects exactly X\S. On W\X, the second entry D_a contains every job and its larger index determines their keys even when they also lie in G. Thus these two groups have the required order and union W\S. This uses exactly the G properties later constructed in Lemma 6.4; Proposition 7.3 establishes the induction order, so it is a proved update identity for that construction.

**Step 3, pruning and I1.** Deleting entries disjoint from W′ does not change qualification there. Therefore O′=W′\S. Lemma 4.5 puts that set in P_b′ and its complement in W′ in D_a′. These are precisely child I1. The original Uses line omitted Lemma 4.5, a genuine direct dependency.

## Lemma 5.4 — proved as stated

**Step 1, exact entry-history map.** Give each initial entry and each appended injection a persistent birth label. Same-side updates only delete such labels or intersect the surviving set with a rank suffix. For two suffixes the identity {λ≥r}∩{λ≥r′}={λ≥max(r,r′)} follows pointwise from the two integer inequalities. Hence a surviving birth set is intersected with at most one effective suffix. A switched update deletes all preceding birth labels and begins a new run, so all thresholds combined in this identity use one and the same rank map.

## Direct dependency corrections for Sections 2–5

The revised Uses lines name direct numbered results, plus definitions or invariants that are genuinely used. Lemma 2.2 uses Lemma 2.1 for the augmented topological order. Lemma 2.7 uses Lemma 2.1 and the Section 2.1 atom definitions. Proposition 2.8 uses only Section 2.2 definitions and size induction. Lemma 2.10 uses Definition 2.9 and Section 2.2. Lemma 3.5 uses Lemma 3.4. Lemma 3.6 uses Lemmas 3.4 and 3.5 for the specified finite walk. Lemma 4.4 uses Lemmas 3.6, 4.3 and the center construction. Lemma 4.5 uses Lemmas 4.3, 4.4 and Definition 2.9 for identification of gaps. Lemma 5.3 uses Lemmas 4.2, 4.3, 4.5 and 5.1, I1, and the expressly displayed property (5.3) of G. Its text need not cite the later Lemma 6.4 as a lemma available in the local proof order: Section 7.3 proves that property before applying the update. No forward logical dependency on a descendant is introduced.

## Present verdict

All numbered statements through 5.4 are proved with the stated definitions. No wrong mathematical step was found in this range. The missing Uses entries are documentation repairs. The explicit input model and running-time repairs are recorded separately in Part A. The independent review of 5.5–8.5 supplies the remaining structural checks.
