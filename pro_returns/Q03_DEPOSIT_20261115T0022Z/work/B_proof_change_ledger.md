# Sections 2–8 proof-layout and dependency change ledger

Date: 15 November 2026. Editor/checker: GPT-6 Astra (OpenAI), effort ChatGPT Pro mode.

The reproducible script is `code/B_revise_proof.py`; the output is `work/B_proof_revised.tex`. It reads the supplied original without modifying it. Exactly 40 numbered statements and all their statement texts and numbered displays are retained byte for byte within the normalized Python text read. There are 39 proofs and one definition.

- Original extract SHA-256: `258e258cae2700b5899b5759ec665b5e5b38f1671945070a1a065ddaa9962cfa`
- Revised extract SHA-256: `6e1c2f7b562a5e0638348953f2792e113036ffdf2817f9b0e0b74e539c3c8aa1`
- Numbered proof steps after revision: 104
- Uses lines after revision: 40

The supplied step layouts of 3.3 and 5.5 are retained. The choice domain in 5.5 is made explicit as K∩W′. The assumptions on G in (5.3) remain standing hypotheses of the switched update; its Uses line introduces no forward reference to Lemma 6.4. Proposition 7.3 validates the construction order.

## 2.1 — Uses line

**Before:**

no numbered statement is cited in the proof.

**After:**

definitions only.

## 2.1 — Numbered step layout

**Before:**

unnumbered proof

**After:**

3 claim-first steps with bracketed direct uses

## 2.2 — Uses line

**Before:**

no numbered statement is cited in the proof.

**After:**

Lemma 2.1; definitions of a unit-job schedule and machine assignment.

## 2.2 — Induction clarification

**Before:**

Induction in the topological order gives

**After:**

For the induction on position in the topological order, a vertex with no incoming arc has \(s'=0\leq s\); assume \(s'(u)\leq s(u)\) for earlier vertices. The recurrence then gives

## 2.2 — Numbered step layout

**Before:**

unnumbered proof

**After:**

3 claim-first steps with bracketed direct uses

## 2.3 — Uses line

**Before:**

no numbered statement is cited in the proof.

**After:**

definitions only.

## 2.3 — Numbered step layout

**Before:**

unnumbered proof

**After:**

2 claim-first steps with bracketed direct uses

## 2.4 — Uses line

**Before:**

no numbered statement is cited in the proof.

**After:**

definitions only.

## 2.4 — Numbered step layout

**Before:**

unnumbered proof

**After:**

2 claim-first steps with bracketed direct uses

## 2.5 — Uses line

**Before:**

no numbered statement is cited in the proof.

**After:**

definitions only.

## 2.6 — Uses line

**Before:**

no numbered statement is cited in the proof.

**After:**

definitions only.

## 2.6 — Explicit structural induction

**Before:**

Complement each leaf and interchange union with intersection at every internal vertex. Induction on the tree, using the two De Morgan identities, proves that the new evaluation is \(J\setminus[F]\). No leaf is created or deleted.

**After:**

Complement each leaf and interchange union with intersection at every internal vertex. Induct on the number of vertices of the formula tree. At a leaf, the allowed complement flag gives exactly the complementary set, and both formulas have one leaf. At an internal vertex, assume that the transformed child formulas give the complements of their old evaluations and preserve their leaf counts. The corresponding De Morgan identity then gives the complementary evaluation at this vertex. Both trees have the sum of their child leaf counts. Thus the new evaluation is \(J\setminus[F]\), with no leaf created or deleted.

## 2.6 — Numbered step layout

**Before:**

unnumbered proof

**After:**

2 claim-first steps with bracketed direct uses

## 2.7 — Uses line

**Before:**

no numbered statement is cited in the proof.

**After:**

Lemma 2.1; definitions of the atomic alphabet and formula evaluation.

## 2.7 — Constant derivation

**Before:**

Counting both frames and complements, the leaf alphabet has at most \(64N^m\) elements for \(N\geq m\geq3\); this generous constant includes the \(O(N)\) thresholds and constants.

**After:**

Counting both frames and complements, the leaf alphabet has at most \[4+8(N+2)+20\binom Nm\leq64N^m\] elements for \(N\geq m\geq3\): the constants contribute four choices, the thresholds contribute \(8(N+2)\), and the five subset/cone types contribute \(20\binom Nm\). The inequality follows from \(8N+20\leq16N\leq16N^m\) and \(\binom Nm\leq N^m\).

## 2.7 — Numbered step layout

**Before:**

unnumbered proof

**After:**

3 claim-first steps with bracketed direct uses

## 2.8 — Uses line

**Before:**

no numbered statement is cited in the proof.

**After:**

definitions of the state graph, compatibility, and acceptance in Section 2.2; induction on set cardinality.

## 2.8 — Induction clarification

**Before:**

Induct on \(|W|\).

**After:**

Induct on \(|W|\). The base \(W=\varnothing\) has the empty schedule. Assume that every accepted smaller set has a full schedule.

## 2.8 — Numbered step layout

**Before:**

unnumbered proof

**After:**

3 claim-first steps with bracketed direct uses

## 2.9 — Uses line

**Before:**

(missing)

**After:**

definitions of full schedules, open intervals, and global and relative descriptions.

## 2.10 — Uses line

**Before:**

no numbered statement is cited in the proof.

**After:**

Definition 2.9; state and acceptance definitions in Section 2.2.

## 2.10 — Induction clarification

**Before:**

Induct on a node's size.

**After:**

Induct on the number of slots \(|W|/m\) of a node. For one slot, that slot is marked and all gaps are empty, so it is an initial and final state. For a larger node assume the claim for its smaller children.

## 2.10 — Numbered step layout

**Before:**

unnumbered proof

**After:**

2 claim-first steps with bracketed direct uses

## 3.1 — Uses line

**Before:**

Lemma 2.5.

**After:**

Lemma 2.5; separator definition and (3.1).

## 3.1 — Numbered step layout

**Before:**

unnumbered proof

**After:**

2 claim-first steps with bracketed direct uses

## 3.2 — Uses line

**Before:**

no numbered statement is cited in the proof.

**After:**

definitions of frame reversal, cutoff, and separator.

## 3.2 — Numbered step layout

**Before:**

unnumbered proof

**After:**

2 claim-first steps with bracketed direct uses

## 3.4 — Uses line

**Before:**

Lemma 3.3.

**After:**

Lemma 3.3; definitions of domain, priority prefix, exception, and separator.

## 3.4 — Numbered step layout

**Before:**

unnumbered proof

**After:**

4 claim-first steps with bracketed direct uses

## 3.6 — Uses line

**Before:**

Lemma 3.4.

**After:**

Lemmas 3.4 and 3.5.

## 3.6 — Numbered step layout

**Before:**

unnumbered proof

**After:**

3 claim-first steps with bracketed direct uses

## 3.7 — Uses line

**Before:**

Lemma 3.6.

**After:**

Lemma 3.6; definitions of cutoff and normalization.

## 3.7 — Numbered step layout

**Before:**

unnumbered proof

**After:**

2 claim-first steps with bracketed direct uses

## 4.1 — Uses line

**Before:**

no numbered statement is cited in the proof.

**After:**

definitions only.

## 4.2 — Uses line

**Before:**

invariant (I1).

**After:**

invariant (I1); frame and cone definitions.

## 4.2 — Numbered step layout

**Before:**

unnumbered proof

**After:**

3 claim-first steps with bracketed direct uses

## 4.3 — Uses line

**Before:**

Lemma 4.1; Lemma 4.2; invariant (I1).

**After:**

Lemmas 4.1 and 4.2; invariant (I1).

## 4.3 — Numbered step layout

**Before:**

unnumbered proof

**After:**

2 claim-first steps with bracketed direct uses

## 4.4 — Uses line

**Before:**

Lemma 3.6.

**After:**

Lemmas 3.6 and 4.3; the center and side-walk construction.

## 4.4 — Numbered step layout

**Before:**

unnumbered proof

**After:**

2 claim-first steps with bracketed direct uses

## 4.5 — Uses line

**Before:**

Lemma 4.4.

**After:**

Lemmas 4.3 and 4.4; Definition 2.9 and the child construction.

## 4.5 — Numbered step layout

**Before:**

unnumbered proof

**After:**

2 claim-first steps with bracketed direct uses

## 5.1 — Uses line

**Before:**

no numbered statement is cited in the proof.

**After:**

definitions only.

## 5.1 — Exhaustive cases stated first

**Before:**

Let \(j\) be a qualifier's largest old entry index.

**After:**

Let \(j\) be a qualifier's largest old entry index. Exactly one of \(j>d\), \(j=d\), and \(j<d\) holds.

## 5.1 — Numbered step layout

**Before:**

unnumbered proof

**After:**

2 claim-first steps with bracketed direct uses

## 5.2 — Uses line

**Before:**

no numbered statement is cited in the proof.

**After:**

definitions only.

## 5.2 — Numbered step layout

**Before:**

unnumbered proof

**After:**

2 claim-first steps with bracketed direct uses

## 5.3 — Uses line

**Before:**

Lemma 4.2; Lemma 5.1; invariant (I1).

**After:**

Lemmas 4.2, 4.3, 4.5, and 5.1; invariant (I1); the stipulated switch-upset property (5.3).

## 5.3 — Numbered step layout

**Before:**

unnumbered proof

**After:**

3 claim-first steps with bracketed direct uses

## 5.4 — Uses line

**Before:**

no numbered statement is cited in the proof.

**After:**

definitions of carry, pruning, and a run.

## 5.4 — Explicit history induction

**Before:**

Subsequent operations keep or delete an entry, or intersect it with a rank suffix.

**After:**

Induct on the number of same-side updates since an entry was created in its run. At creation the entry is its initial or injection set, with no additional suffix. Assume that every current entry has the stated form. Subsequent operations keep or delete an entry, or intersect it with a rank suffix.

## 5.4 — Numbered step layout

**Before:**

unnumbered proof

**After:**

2 claim-first steps with bracketed direct uses

## 5.5 — Uses line

**Before:**

Lemma 4.5; Lemma 5.1; Lemma 5.3; Lemma 5.4; invariant (I1).

**After:**

Lemmas 4.5, 5.1, 5.3, and 5.4; invariant (I1); injection definition (5.2).

## 5.5 — Selection-domain clarification

**Before:**

$x_K$ be its job of least rank.

**After:**

$x_K$ be the least-rank job of $K\cap W'$.

## 6.1 — Uses line

**Before:**

no numbered statement is cited in the proof.

**After:**

Lemmas 5.1 and 5.4; the pruning and run definitions; switch pair (5.4).

## 6.1 — Numbered step layout

**Before:**

unnumbered proof

**After:**

2 claim-first steps with bracketed direct uses

## 6.2 — Uses line

**Before:**

Lemma 5.3.

**After:**

Lemmas 2.6, 5.3, 5.4, 5.5, and 6.1; the edge-cutoff construction.

## 6.2 — Equivalent explanatory wording

**Before:**

This construction has eliminated the old switch formula, rather than embedding its historical expression.

**After:**

The displayed extension uses the replacement initial contribution from (6.1), with the stated leaf count independent of earlier depth.

## 6.2 — Numbered step layout

**Before:**

unnumbered proof

**After:**

4 claim-first steps with bracketed direct uses

## 6.3 — Uses line

**Before:**

Lemma 4.5.

**After:**

Lemma 4.5; the frame-reversal map.

## 6.3 — Numbered step layout

**Before:**

unnumbered proof

**After:**

2 claim-first steps with bracketed direct uses

## 6.4 — Uses line

**Before:**

Lemma 2.5; Lemma 4.3; Lemma 4.4.

**After:**

Lemmas 2.5, 4.3, 4.4, 4.5, 6.2, and 6.3; definition (6.8).

## 6.4 — Numbered step layout

**Before:**

unnumbered proof

**After:**

6 claim-first steps with bracketed direct uses

## 6.5 — Uses line

**Before:**

Lemma 5.4.

**After:**

Lemmas 2.6, 5.4, 5.5, and 6.2; definitions (5.2), (5.4), and (6.8).

## 6.5 — Numbered step layout

**Before:**

unnumbered proof

**After:**

2 claim-first steps with bracketed direct uses

## 7.1 — Uses line

**Before:**

Lemma 3.4; Lemma 3.6; Lemma 5.1; Lemma 5.3; Lemma 6.4; invariants (I1), (I2), (I3).

**After:**

Lemmas 2.5, 3.4, 3.6, 4.3, 4.4, 5.1, 5.3, and 6.4; invariants (I1), (I2), and (I3).

## 7.1 — Updated local step references

**Before:**

item 1; item 3

**After:**

Step 6; Step 8

## 7.1 — Step layout

**Before:**

two cases and a four-item numbered subproof

**After:**

one eleven-step proof; all subproof sentences retained

## 7.1 — Numbered step layout

**Before:**

unnumbered proof

**After:**

11 claim-first steps with bracketed direct uses

## 7.2 — Uses line

**Before:**

Lemma 2.4; Lemma 2.5; Lemma 3.3; Lemma 5.1; Lemma 5.2; Lemma 5.3; invariants (I1), (I3).

**After:**

Lemmas 2.4, 2.5, 3.3, 5.1, 5.2, 5.3, and 6.4; invariants (I1) and (I3).

## 7.2 — Numbered step layout

**Before:**

unnumbered proof

**After:**

3 claim-first steps with bracketed direct uses

## 7.3 — Uses line

**Before:**

Lemma 2.4; Corollary 3.7; Lemma 4.3; Lemma 4.4; Lemma 4.5; Lemma 5.3; Lemma 5.5; Lemma 6.1; Lemma 6.2; Lemma 6.3; Lemma 6.4; Lemma 6.5; Lemma 7.1; Lemma 7.2; invariants (I1), (I2), (I3).

**After:**

Lemma 2.4; Corollary 3.7; Lemmas 4.3--4.5, 5.3, 5.5, 6.1--6.5, 7.1, and 7.2; the root invariants.

## 7.3 — Induction-variable clarification

**Before:**

Induct from the root.

**After:**

Induct from the root on node depth.

## 7.3 — Numbered step layout

**Before:**

unnumbered proof

**After:**

4 claim-first steps with bracketed direct uses

## 8.1 — Uses line

**Before:**

Lemma 5.1; Lemma 6.5.

**After:**

Lemmas 2.6, 4.3, 5.1, and 6.5; definitions (8.1) and (8.2).

## 8.1 — Numbered step layout

**Before:**

unnumbered proof

**After:**

2 claim-first steps with bracketed direct uses

## 8.2 — Uses line

**Before:**

Lemma 2.5; Lemma 4.4; Lemma 5.3; invariant (I2).

**After:**

Lemmas 2.5, 4.3, 4.4, 4.5, 5.3, 7.1, and 8.1; the center-separator property.

## 8.2 — Numbered step layout

**Before:**

unnumbered proof

**After:**

3 claim-first steps with bracketed direct uses

## 8.3 — Uses line

**Before:**

Lemma 2.6; Lemma 3.1; Lemma 4.4.

**After:**

Lemmas 2.6, 3.1, 4.4, and 8.1; the center-cutoff definition.

## 8.3 — Numbered step layout

**Before:**

unnumbered proof

**After:**

3 claim-first steps with bracketed direct uses

## 8.4 — Uses line

**Before:**

no numbered statement is cited in the proof.

**After:**

Lemmas 2.6, 6.5, 8.1, 8.2, and 8.3; the atomic formula alphabet.

## 8.4 — Numbered step layout

**Before:**

unnumbered proof

**After:**

2 claim-first steps with bracketed direct uses

## 8.5 — Uses line

**Before:**

Definition 2.9; Proposition 7.3; Lemma 8.2; Lemma 8.3; Lemma 8.4.

**After:**

Definition 2.9; Proposition 7.3; Lemmas 8.2, 8.3, and 8.4.

## 8.5 — Numbered step layout

**Before:**

unnumbered proof

**After:**

2 claim-first steps with bracketed direct uses

## exposition — Equivalent explanatory wording

**Before:**

The replacement means rescheduling the jobs of the interval subject to precedence. It does \textbf{not} mean that every arbitrary permutation of its slots is feasible.

**After:**

The replacement ranges over full schedules of the interval job set, each respecting its restricted transitive precedence order.

## exposition — Equivalent explanatory wording

**Before:**

These are agreement predicates, not global descriptions of the cutoffs as standalone sets. Their behavior outside \(W\) is not assumed.

**After:**

The equalities (8.3) specify these predicates on \(W\); subsequent uses first restrict membership to \(W\).

## exposition — Equivalent explanatory wording

**Before:**

The localization in this proof is a logical order of justification. Boolean intersections commute; no assertion about a required operational evaluation order is being made. In particular, the parent description is not silently inserted into (8.5).

**After:**

The proof of (8.5) first derives membership in the parent from its cone factors, which permits the use of (8.3). Its formula therefore uses exactly the five displayed factors.

## Verification output

PASS: 40 numbered statement texts preserved exactly.
PASS: every numbered display and its equation number preserved exactly.
PASS: 39 proof environments balanced.
PASS: all 40 statements/definition have Uses lines.
PASS: Sections 2–8 only; no Section 9 content included.
PASS: all scripted anchor transformations matched their original text.
