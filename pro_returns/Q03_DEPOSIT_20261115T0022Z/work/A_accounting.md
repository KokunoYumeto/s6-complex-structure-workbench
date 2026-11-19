# Part A and Section 9: independent audit

Audit date: 15 November 2026 (Europe/Berlin). Auditor: GPT-6 Astra, effort ChatGPT Pro mode.

## Verdict and scope

The finite enumeration algorithm of Section 2 admits the padded running-time bound in Proposition 9.2. An itemized sequential-tape implementation is given below. The calculation proves the input-length exponent **60m²+129m+2** for the stated procedure that tests at most n deadlines. The previously printed +8 is a weaker bound; no extra six powers are required by this accounting. The bound in N starts from the parsed, canonically numbered padded instance. Reading an arbitrary original input is charged separately in L.

The accounting applies to the actual finite computation, including its witness on every accepted instance. Its running time does not require a conclusion about the completeness of the description family. The proof composition used in Theorem 9.1 is audited in §7 below; the independent audit of Theorem 8.5 supplies the structural part of that composition.

## 1. Machine, encoding, symbols, and constants

Use one deterministic multitape Turing machine with a fixed finite alphabet and a fixed finite number of tapes (32 suffice for the files, copied records, stacks, unary scan counters, binary loop counters, and output described below). The number of tapes is independent of m, K, n, and N. The program receives m and computes K; its formula stack is encoded on a tape, rather than being implemented by K separate tapes.

An explicit instance contains a canonical self-delimiting binary integer m, a canonical signed binary deadline T, n, an explicit list of the n vertices numbered 1,...,n, and a list of distinct arcs with endpoints in that list. All separators and length fields count towards the bit length L. Vertex identities are these canonical integers. There is at least one bit per explicit vertex, hence n≤L. The graph is promised acyclic; the preprocessing can also reject malformed encodings, repeated arcs, and cycles within the preprocessing bound below. Alternative finite binary vertex names are supported by a first renaming pass charged to L, using repeated scans and comparisons; they do not enter the N-only padded bound.

In a nontrivial padded call, m≥3, K≥1, 1≤T<n, n≤mT, J=[N], and N=mT≥m. The padded DAG is presented in canonical form; isolated padding vertices have consecutive new labels. Set

- C=K·512^K;
- B=C·N^(mK), an integer upper bound on the number of syntactic formulas with at most K leaves;
- S=B·N^m, an integer upper bound on the number of states for one described set;
- h=⌈log₂(N+1)⌉;
- q=64(m+1)(K+1).

The actual formula, set, and state counts may be smaller; all loops run over the actual counts. The displayed B and S are bounds, not instructions to materialize unused records.

For explicit hidden constants, the implementation below has all table-row costs bounded by D times the expression in its row, where D=2²⁰q². The coarse final envelope

A(m,K)=2⁴⁰(m+1)⁴(K+1)⁴(K·512^K)⁵

bounds the coefficient of N^(5mK+4m+1). The fixed numerical slack covers at most 32 tape heads, delimiters, returning to the beginning of scanned files, stack management, and the sum of the listed rows. A basic full scan/copy/compare operation uses a bounded number of moves per symbol; the loop and record descriptions below give at most 64 such elementary passes per row operation after counters and stack words have been included. Thus D, and consequently A, are effective bounds depending only on the displayed parameters. These constants have no claim to sharpness.

The useful length inequality is

⌈log₂(S+1)⌉ ≤ 2+10K+(mK+m)h ≤ qh/8 ≤ qN/8.

Here log₂K≤K for K≥1, so log₂C≤10K; and h≤N for N≥3. The same bound applies to a formula number or a described-set number. An individual formula code uses at most O(K(m+1)h) bits, also covered by qN. All index comparisons and binary increment operations are charged at their full bit cost.

## 2. Tape layout and scan costs

1. **Graph files.** Store adjacency and transitive-closure matrices in row-major order, as N² bits with row separators. Use a separate length-N active-vertex vector and rank map. A requested matrix location is reached with a unary distance scratch word. Constructing that word and scanning to the location cost at most a constant times N². The counter is moved in parallel with the matrix head, so an N² scan does not incur a binary counter increment at every bit.

2. **Formula file.** Each record has a formula code, its evaluated N-bit set, and an index. Its length is at most qN. Formula evaluation uses a delimited postorder stack on one tape. A stack access can scan its O(KN) bits; this cost is included in the formula-evaluation bound.

3. **Described-set file.** After duplicate removal, each record has an N-bit set, its cardinality, an ordinal, and an acceptance bit. Pad records to the same length, at most qN. A query set is kept on a separate tape. Comparing it against every record costs at most D·BN; the deliberately looser D·BN² bound accommodates seeking and copying a matching witness as well.

4. **Witness file.** Store a set ordinal and the full schedule of each accepted set. A schedule is an ordered list of at most N canonical job identifiers, each at most h bits, with slot separators. One record has at most qN² bits. The whole witness file has at most qBN² bits. The witness file is separate from the state file; its longer records do not increase state-access cost.

5. **Current-state file.** For the current W, each state record has L,Z,R as three N-bit vectors, its ordinal, a reached bit, an initial bit, and a predecessor ordinal or a null symbol. A final bit may be stored as well. Its length is at most qN. There are at most S records. Fetching or updating a record by its ordinal scans at most qSN bits. The scan compares the query ordinal with the ordinal field of each record, charging all bits; no constant-time indexed access is used. A bounded number of such scans costs at most D·SN.

6. **Work files.** A fixed collection of auxiliary tapes holds W, two states, a transition-gap vector, counters, and a predecessor path. Variable-length lists and the formula stack are ordinary delimited records. Nothing in this layout allocates a new tape when m or K increases.

## 3. Itemized padded-call cost table

Every expression in the following table counts deterministic multitape steps up to the common coefficient D. B and S have the meanings fixed above.

| Subroutine | Bound for the entire padded call | Construction giving the bound |
|---|---:|---|
| Canonical padded input to adjacency; reachability; deterministic rank | N⁵ | At most N² arc insertions with N² scans; N³ Floyd–Warshall iterations with O(N²) matrix accesses; repeated scans for deterministic topological order. |
| Generate and evaluate all formulas | B N³ | At most K leaves per formula; at most mN reachability queries per cone leaf; each query costs O(N²); fixed-parameter factors fit D. Postorder Boolean vector operations fit the same bound. |
| Pairwise deduplication | B³ N | At most B² record pairs; fetch/compare/mark by complete scans of a file of length at most qBN. Compact surviving records afterwards. |
| Cardinalities and cardinality ordering | B³ N² | Compute each cardinality by scanning its N bits. Repeated selection scans or pair comparisons with full record retrieval give this deliberately loose bound. Equal-cardinality records use their ordinal as a deterministic tie-breaker. |
| Enumerate and initialize all current-state files | B S (B N²+N⁴) | For each of at most B sets and S candidates, fetch W and F, form L,Z,R, test compatibility, and perform the initial/final acceptance queries. |
| Reachability dynamic program on state graphs | 3 B S⁴ N | At most S passes over at most S² ordered state pairs for each of B sets; each pair costs at most 3D SN. |
| Reconstruct and store all accepted witnesses | B S N²+B²N³ | Every predecessor path has at most N/m states; fetch its records and at most N/m+1 smaller accepted schedules, then concatenate the disjoint pieces. |
| Produce the selected padded witness | N³ | Scan the saved schedule and rank-to-label map; delimit slots; output at most N identifiers. The preceding row already includes storing the witness. |

Here are the details proving each row.

### 3.1 Reachability and rank

Initialize the N×N adjacency matrix. There are at most N² distinct arcs; writing each one by a complete matrix seek gives O(N⁴). Floyd–Warshall maintains the invariant that, after processing vertices 1,...,k, the matrix indicates paths whose internal vertices are in that set. The usual recurrence uses three matrix locations for each triple (i,j,k), and every matrix access, including a possible update, costs O(N²) using the unary scratch distance. N³ triples therefore cost O(N⁵). A nonzero diagonal detects a cycle. For the DAG case, select the smallest active vertex having no active predecessor, remove it, and append it to the rank map. Scanning candidate rows and the active vector with repeated complete seeks costs at most O(N⁵) over all removals. Lemma 2.1 proves that the resulting rank respects reachability. Reverse-frame ranks and cones use the same matrix and the map i↦N+1−i.

### 3.2 Formula count and generation

The exact overcount of leaf choices is 4+8(N+2)+20·binom(N,m). For N≥m≥3 this is at most 64N^m. The four terms for constants include complements, the threshold count includes the two frames and complements, and each of the five slot/cone atom types has two frames and two complement choices. A full ordered binary tree with ℓ leaves has at most 4^ℓ shapes and at most 2^(ℓ−1) assignments of union/intersection labels. Thus each ℓ contributes at most (512N^m)^ℓ; summing ℓ=1,...,K gives at most K512^K N^(mK)=B.

Enumerate only valid Dyck (balanced-parenthesis) words of length 2(ℓ−1), by depth-first extension through valid prefixes. The search visits O(K) prefix-tree edges per output and each update/scan costs O(K), giving O(K²) delay. These words encode the full ordered binary-tree shapes with ℓ leaves. Then enumerate their internal labels and leaf parameters. Enumeration is by finite counter loops; the total code and counter length for one formula is at most qN. A cone atom is evaluated by considering each job x and each of at most m members y of its slot subset and retrieving the appropriate reachability bit. At most mN queries, each costing O(N²), give O(mN³) per cone. The membership vector for a slot or rank threshold and its complement costs less. Evaluate the whole tree in postorder; each internal operation combines two N-bit vectors. Even scanning the O(KN)-bit stack at every node costs O(K²N). K cone evaluations and all stack scans fit D N³. Multiplying by the formula count gives D B N³.

### 3.3 Deduplication and sorting

Compare each pair of evaluated formula records. A complete fetch of each indexed record scans at most qBN bits; comparing N-bit vectors and marking the later equal record are charged to those scans. There are at most B² pairs. This gives D B³N, including the final compaction pass. Every distinct set retains a representative formula, so no set is lost. A cardinality pass scans each bit vector and stores its count in a field of at most h bits. A selection-sort implementation repeatedly scans the unselected records, compares cardinality/ordinal pairs, and copies the selected record into a second set file. Even the more wasteful implementation that obtains every compared record by a full seek uses at most D B³N². Thus no unproved bound on random-access sorting is used.

### 3.4 State enumeration and compatibility

Fix W. A representative described set F and an m-element subset Z determine L=W∩F and R=W\(L∪Z). There are at most B·binom(N,m)≤S choices. Reject Z outside W, intersections Z∩L, non-antichains, and the forbidden precedence pairs specified in Section 2. These checks are finite tests over the N-bit vectors and the N² reachability bits. The deliberately slow implementation considers every ordered job pair, fetches its relation with an O(N²) matrix scan, and checks the relevant membership bits; the complete check is O(N⁴). Fetching the set records and checking acceptance of L and R costs at most D BN². This gives D BS(BN²+N⁴) over all W. Accepted smaller-set schedules are not fetched during every state test; only their acceptance bits are needed.

### 3.5 State-graph propagation

Initialize reached flags on the initial states, with null predecessor. During each pass through ordered pairs (u,v), fetch both records, test reached(u), unreached(v), and L_u∪Z_u⊆L_v, then test acceptance of L_v\(L_u∪Z_u). On the first successful transition to v, set reached(v) and its predecessor to u. Do not replace the predecessor of an already reached state. This makes predecessor links point to states reached earlier and prevents a spurious predecessor cycle.

Fetching/updating state records takes at most D SN. A complete acceptance query takes at most D BN². Any compatibility recheck is at most D N⁴. Since m≥3,

BN²≤BN^(m+1)=SN, and N⁴≤BN^(m+1)=SN.

Thus a complete pair test is at most 3D SN. Every reachable vertex has a simple path of at most S−1 edges. Induction on path length shows that after S full pair passes every reachable vertex is marked, including for the asynchronous within-pass updates used here. The cost is therefore at most

B · S · S² · 3D SN = 3D B S⁴ N = 3D B⁵ N^(4m+1).

The strict inclusion |L_v|≥|L_u|+m also shows that this graph is acyclic. That fact provides the sharper witness-path bound used next, but is not needed for the deliberately generous S-pass time bound.

### 3.6 Witness reconstruction and output

Backtrack from a reached final state until an initial state is found. Each transition increases |L| by at least m; hence the path has at most |W|/m≤N/m states. Retrieve each record by scanning the state file, costing at most D SN² for W. Reverse the path records on a work tape. The first left part, each transition gap, and the final right part are accepted smaller sets. There are at most N/m+1 such pieces. Their saved schedules can each be retrieved by scanning at most qBN² symbols, costing at most D BN³ in total for W. Proposition 2.8's disjoint-partition identity proves that the concatenation contains exactly |W| jobs, each once. Append this schedule to the separate witness file, retaining the just-constructed schedule on its work tape. Over B sets this gives the stated D(BSN²+B²N³) row. This argument avoids recursively recomputing smaller witnesses.

For the selected J schedule, use the retained work-tape copy from its reconstruction (J is the unique described set of cardinality N), delete padded identifiers, translate any rank indices back to their original canonical labels, and assign the at most m jobs in a slot to machines in increasing-identifier order. Repeated map scans cost O(N³); output itself uses O(N log(N+1)+N log(m+1)) bits and costs no more. An optimum is written only after the first accepted deadline is found.

## 4. Domination and exact N exponent

Put P=B⁵N^(4m+1). Since m≥3, K≥1, N≥3, and B≥1, every non-DP row is bounded by a fixed small multiple of P. In particular,

- BS(BN²+N⁴)=B³N^(m+2)+B²N^(m+4);
- BSN²+B²N³=B²N^(m+2)+B²N³;
- N⁵, BN³, B³N, and B³N² all have B-exponent at most 5 and N-exponent at most 4m+1.

The largest elementary N exponent outside propagation is m+4, and m+4≤4m+1 for m≥1. This proves all the domination inequalities explicitly. Summing the row coefficients fits the envelope A(m,K) above, because q²=2¹²(m+1)²(K+1)² and the numerical slack in A exceeds 256D after removing the factor C⁵.

Finally,

P=(K512^K)⁵ N^(5mK+4m+1).

This proves Proposition 9.2 with an effective fixed-parameter coefficient and with its witness cost included. The factor accounting is: one B for all described W; one S for graph-propagation passes; S² for ordered pairs; one SN for sequential state-file access. Since S=BN^m, the product B·S·S²·SN is B⁵N^(4m+1). Lemma 2.7 gives B, the state definition in Section 2 and the counting step in Proposition 9.2 give S, and the file layout above gives the final N.

## 5. Input-length accounting and the corrected exponent

Parse the canonical input once. Repeated full scans suffice to validate identifiers, detect repeated arcs, construct the canonical graph, compare the signed binary deadline against 1 and n, and calculate mT for the nontrivial branch. This takes at most P_m(L+2)⁴ steps for P_m=2³⁰(m+1)⁴. For instance, at most L² pairs of tokens are compared, each by at most O(L) scans, and all unary/binary conversions and adjacency writes fit another factor L. This is deliberately coarser than necessary. Noncanonical large identifiers can be renamed within the same bound. The original input is never assumed to have length bounded by N.

For T<1, reject the nonempty instance. For T≥n, produce the topological schedule of n jobs one per slot directly from the original arc list. There are at most n removal stages and n candidate vertices per stage. For one candidate, scan the original arc list; endpoint comparison and lookup of a predecessor in the length-n active vector cost at most O(L²) over that scan. Thus this direct topological procedure takes O(n²L²)≤O(L⁴), without invoking the padded N⁵ preprocessing. Both elementary branches cost at most P_m(L+2)⁴, including their O(n(log n+log m)) output. For 1≤T<n reject n>mT; otherwise N=mT≤mn≤mL. This avoids expanding a large binary deadline.

Set K_m=12m+25 and

e_m=5mK_m+4m+1=60m²+129m+1.

The actual padded call takes at most A(m,K_m)N^e_m. The prescribed optimization procedure tries T=1,...,n, stopping at the first acceptance. Each trial has N≤mn and there are at most n≤L trials. Its padded work is at most

A(m,K_m)·n·(mn)^e_m ≤ A(m,K_m)m^e_m(L+2)^(e_m+1).

Input handling and the final witness cost have degree at most 4; e_m+1≥929 for m≥3. Thus all three tasks fit

G(m)(L+2)^(60m²+129m+2),

where G(m)=A(m,12m+25)m^(60m²+129m+1)+2³¹(m+1)⁴ is one effective coefficient bound. The +2 exponent comes from the +1 in e_m and one further factor L for the deadline trials. For a single already specified nontrivial deadline, the same accounting gives input exponent e_m; the common bound covering optimization is e_m+1. This is an upper bound established by the specified algorithm, not an assertion of optimality of that exponent.

The corrected table is:

| m | K_m | padded N exponent | common input L+2 exponent |
|---:|---:|---:|---:|
| 3 | 61 | 928 | 929 |
| 4 | 73 | 1477 | 1478 |
| 5 | 85 | 2146 | 2147 |
| 6 | 97 | 2935 | 2936 |

Equation (1.1), Corollary 9.3, the abstract, the Status table, the record block, and the small-m table must use +2 consistently. Equation (1.2) remains +1. The phrase “after padding” should explicitly say that its N-only accounting starts from the parsed canonical padded DAG; the complete input-reading cost belongs to the L bound.

## 6. Compact-isolated input (Proposition 9.4)

Use a compact encoding with n and T in binary and an explicit arc list whose endpoint labels are binary integers in [n]. Let d be the number of distinct endpoints. List and rename them by repeated input scans, in polynomial time in this encoding length. Every nonisolated vertex is among them, hence d≤2|E|. Reject n>mT or T<1 for the nonempty input.

For T≥d, topologically schedule the d incident vertices one per slot. There are mT−d unused machine-slot positions and n−d isolated jobs, and mT−d≥n−d. Assign the isolated jobs injectively to unused positions. This gives a complete existence proof; the decision machine need not enumerate those jobs.

For T<d, n≤mT<md≤2m|E|. Therefore explicitly enumerating all n vertices and padding to N=mT produces a graph polynomial in the compact input length for fixed m. The Section 9 decision computation then applies to that canonical expansion. The implication from the expanded decision answer back to the compact instance is exactly the deletion/insertion correspondence of Lemma 2.3. Each input-label comparison costs at most the compact input length, already charged in the input preprocessing. Outputting an explicit schedule may require Ω(n) identifiers; Proposition 9.4 claims decision time only.

## 7. Section 9: step-by-step logical audit and Uses corrections

### Theorem 9.1

**Step 1: acceptance and witness.** The state path stored by the finite computation gives the ordered disjoint partition (2.3). Proposition 2.8 concatenates the saved schedules of its accepted smaller gaps and the path's m-element slots. Its compatibility checks exclude every precedence directed from a later piece to an earlier one. This proves soundness and the returned witness claim.

**Step 2: completeness composition.** Theorem 8.5 produces a hierarchy with the same globally enumerated atomic language and the same budget K_m. Lemma 2.10 sends each marked slot to a state and sends its intervening child gaps to accepted smaller sets. At the root this is an accepting state path for J. The formulas and parameter K are identical on both sides of this composition; there is no extra promise on the actual finite search.

**Step 3: padding.** Lemma 2.3 inserts isolated jobs into all vacant machine-slot positions and deletes them in the reverse direction. The maps preserve each original precedence pair because they change none of the original slot indices. Thus acceptance of padded J has exactly the deadline meaning used in the theorem.

**Step 4: elementary deadlines.** A nonempty schedule needs a positive slot, so T<1 fails. Lemma 2.1 supplies a topological order, and its one-job-per-slot schedule finishes in n slots. Hence T≥n is answered without constructing mT padding jobs. The capacity inequality n≤mT is necessary for the remaining branch.

**Step 5: optimization.** Lemma 2.1 guarantees a feasible deadline n. The integer slot convention and Lemma 2.2 put the optimum among 1,...,n even when real starts were originally allowed. Testing all these deadlines in increasing order and returning the first accepted witness therefore returns an optimum. Assigning distinct machine indices within each slot changes no slot or precedence inequality.

**Uses line.** Explicitly list Lemmas 2.1, 2.3, 2.10, Proposition 2.8, and Theorem 8.5. Include Lemma 2.2 when the theorem is presented as covering the original real-start scheduling convention. The current line omits the elementary topological-order reference.

### Proposition 9.2

**Step 1: finite formula count.** The full binary-tree and leaf-alphabet count in §3.2 yields B=K512^K N^(mK). This is Lemma 2.7 with every multiplicative factor accounted for.

**Step 2: state count.** Choosing a represented left-set formula and an m-element subset Z uniquely specifies L and R for fixed W; the tests only discard candidates. Hence S=BN^m bounds all retained candidates, including duplicates. The computation never guesses any further boundary data.

**Step 3: storage and access.** The separate files in §2 have exact length envelopes qBN, qSN, and qBN². Full scan access, including ordinal comparison, has the costs used by the propagation calculation. The bit length of each ordinal is bounded before it is treated as part of a record.

**Step 4: graph propagation.** S complete passes suffice by induction on simple-path length. The pair test is charged to the actual sequential data access and acceptance-query routine. The product B·S·S²·SN is exactly B⁵N^(4m+1), as §3.5 proves.

**Step 5: all remaining operations.** The eight rows of §3 cover preprocessing, formula generation and evaluation, deduplication, ordering, state construction, propagation, backtracking, and output. §4 proves every domination inequality. No unspecified “lower-degree polynomial” remains.

**Uses line.** Lemmas 2.1, 2.7, and Proposition 2.8; definitions of the state/transition procedure in Section 2. Lemma 2.1 supplies rank preprocessing; Proposition 2.8 supplies the disjoint witness concatenation. The syntactic and table cost derivations themselves use no structural theorem.

### Corollary 9.3

**Step 1: parameter substitution.** K_m=12m+25 is the budget established in Lemma 8.4 and Theorem 8.5. Substitution gives 5mK_m+4m+1=60m²+129m+1 by distributivity, with terms 60m²,125m,4m,1.

**Step 2: encoding bound.** Explicitly listing every vertex gives n≤L. The only padded branch satisfies N=mT≤mn≤mL. Replacing N by mL introduces m^e_m into the coefficient, which is a function of fixed m.

**Step 3: all deadlines and input costs.** At most n≤L trials introduce one additional power of L. The parser and output costs have degree at most 4, below e_m+1. The coefficient G(m) and the resulting +2 exponent are displayed in §5.

**Uses line.** Proposition 9.2, Theorem 9.1 (deadline procedure), Lemma 2.3 (padding bound), and Lemma 8.4/Theorem 8.5 (value of K_m). The current “no numbered statement” line should be replaced.

### Proposition 9.4

**Step 1: early capacity test.** n≤mT is necessary because there are mT available machine-slot positions. T≥1 is necessary for a nonempty job set.

**Step 2: large deadline.** The incident-vertex count d and topological order give a schedule using one slot per incident vertex. Every remaining job is isolated, and the explicit inequality mT−d≥n−d proves that distinct vacant positions suffice.

**Step 3: short deadline.** T<d and d≤2|E| yield N=mT<2m|E|. The early capacity check also gives n≤N, so the compact job universe can be expanded completely in polynomial time before invoking the padded decision procedure.

**Step 4: output qualification.** A literal list of n scheduled vertices contains at least n symbols. Thus the polynomial compact-input claim here concerns the Boolean decision computation. Its proof does not promise the compact input can always be accompanied by a short explicit output list.

**Uses line.** Lemma 2.1, Lemma 2.3, Theorem 9.1, and Proposition 9.2 (or Corollary 9.3 after canonical expansion). The current “no numbered statement” line should be replaced.

## 8. Program record

`code/A_check_accounting.py` verifies the exponent expansion, the small-m table, and the algebraic dominance of every table row over all integer m≥3 and K≥1 by checking the resulting nonnegative coefficient expressions. Its output is `code/A_check_accounting.out`. The program checks arithmetic and the symbolic inequalities; the tape implementation and the logical proof are the arguments above.
