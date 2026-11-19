# Q03: Exact unit-job precedence scheduling for every fixed number of machines

**A complete extension and audit of the supplied three-machine construction**  
23 October 2026

## Abstract

For every fixed integer $m\geq3$, the problem $P_m\mid\mathrm{prec},p_j=1\mid C_{\max}$ is solvable in deterministic polynomial time. The construction supplied with the question extends to $m$ machines. Its separator walks, exchanges, switches of direction, and two exterior boundary invariants do not use a bound of three on a slot. The capacity argument bounds surviving injection entries by $m$, and the list length by $m+2$.

There is a small but necessary distinction in extending the numerical estimates: the supplied numerical derivation of the $25$-leaf bound must be replaced by an $m$-dependent estimate. We prove that an earlier low set has an extension with at most $3m+3$ leaves, a switch entry has at most $3m+7$ leaves, and the union of any list or carry has at most $6m+9$ leaves. Only one initial entry of a run can be complicated. Consequently, $K_m=12m+25$ leaves suffice for every global interval description, at every depth. The original finite description dynamic program, with an $m$-element slot in each state, is therefore complete as well as sound.

The proof below is self-contained. It restates and proves the generalized content of every lemma in the eight supplied lessons and every corresponding lemma in the supplied preprint. Section 10 gives an explicit cross-reference audit. The literature search found a publicly accessible four-machine adaptation, but none of its correctness claims is needed for the theorem proved here.

## 1. Result, model, and literature

### Theorem 1.1 (fixed-machine exact scheduling)

There is one effective deterministic algorithm with the following properties. Given an integer $m\geq3$, an explicitly listed directed acyclic graph $G=(V,E)$ on $n\geq1$ jobs, and an integer deadline $T$, it decides whether there is a function of finite sets
$$
\tau:V\longrightarrow\{1,\ldots,T\}
$$
such that
$$
|\tau^{-1}(\{t\})|\leq m
\quad\text{for every }t,
\qquad
\tau(u)<\tau(v)\quad\text{for every }(u,v)\in E.
$$
It constructs such a schedule whenever one exists. The same algorithm can construct a schedule of minimum makespan.

For each fixed $m$, both tasks take
$$
O_m\!\left((L+2)^{\,60m^2+129m+8}\right)
\tag{1.1}
$$
steps on a deterministic multitape Turing machine, where $L$ is the binary input length in the explicitly listed model. After padding to $N=mT$ jobs, a nontrivial deadline decision has the more specific bound
$$
O_m\!\left(N^{\,60m^2+129m+1}\right).
\tag{1.2}
$$
The constants implicit in $O_m$ are effective functions of $m$.

Here “one effective algorithm” means that the formulas and the leaf budget $K_m=12m+25$ can be generated from $m$. The exponent is allowed to depend on $m$. No polynomial bound uniform in an input-dependent $m$ is asserted.

**Proof.** Sections 2–8 prove soundness and completeness; Section 9 proves the running time and optimization statement. $\square$

In particular, for four machines one may use $K_4=73$, a padded deadline bound $O(N^{1477})$, and the conservative input-length bound $O((L+2)^{1484})$. These enormous exponents are existence bounds, not practical performance claims.

### 1.1. What was checked in the literature

The search was conducted on 23 October 2026. It covered the named OpenAI Math Release preprint and its formalization scope, arXiv, queries restricted to STOC, FOCS, SODA, ICALP and IPCO proceedings, authors' publication pages, and public discussion of fixed-machine unit-job scheduling. The search record is included in the artifacts.

The following are the relevant precise findings.

1. **The supplied preprint.** OpenAI, *A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling* (24 September 2026), Theorem 1.1, asserts the three-machine result with time $O((L+2)^{150020})$. Its structural theorem is Theorem 3.4, source label “thm:structure”; its finite search and conditional completeness are Proposition 3.1 and Lemma 3.3. The publicly accessible source/PDF is linked in [P]. The supplied source's introduction, model, main theorem and conclusion state a three-machine result. They do not state a theorem for every fixed $m$. This paper checks the construction itself rather than assuming its conclusion.

2. **Official formalization scope.** The OpenAI Math Release file *lean/docs/124.md*, section “Scope”, describes a three-machine algorithm and points to its comparator statement [F]. This is a description of formalization scope, not an independently used theorem in the present proof.

3. **A directly relevant four-machine exploration.** The publicly accessible repository by GitHub user “drbh”, *scheduling-proof-exploration*, README sections “upstream and building” and “could this work for other machine counts?”, and CHANGELOG entry for commit “bbd3013”, explicitly adapt the upstream development to four jobs per slot [D]. The README says that its extension covers $m=4$ and observes that general $m$ requires new leaf budgets. It reports a six-entry, 29-leaf-per-entry calculation. We inspected its scope and changes; we neither ran its Lean build nor use its advertised theorem as a premise. The argument here supplies the general-$m$ proof directly.

4. **An earlier exact structural algorithm.** Jesper Nederlof, Céline M. F. Swennenhuis and Karol Węgrzycki, *A Subexponential Time Algorithm for Makespan Scheduling of Unit Jobs with Precedence Constraints*, arXiv:2312.03495v1 (2023), Theorem 1.1, gives time $(1+n/m)^{O(\sqrt{nm})}$ [N]. In this freely accessible arXiv version, the proper-decomposition result is Theorem 3.2 following Definition 3.1, and assumes at most $m$ sources. The published version appeared in SODA 2025, pp. 535–552. The cited subexponential bound does not itself become polynomial by fixing $m$. Nor may its source-count hypothesis simply be dropped.

5. **Approximation is a different conclusion.** Syamantak Das and Andreas Wiese, *A Simpler QPTAS for Scheduling Jobs with Precedence Constraints*, Theorem 1 in arXiv:2501.09091v1 (freely accessible; conference version ESA 2022), gives a $(1+\varepsilon)$ approximation for fixed machine count and fixed $\varepsilon>0$ [A]. It does not decide exact deadline feasibility. The earlier works listed in the question are likewise background rather than premises needed here.

No all-fixed-$m$ polynomial theorem or hardness theorem for a fixed $m\geq4$ was located in these searches. This is a statement about the search, not a proof that no such publication exists. The positive conclusion of Theorem 1.1 rests entirely on the arguments below, including their full hypotheses.

The standard historical results about two machines and variable machine count are not used to infer any step of this extension. In particular, the distinction between a polynomial for each fixed $m$ and a single polynomial for variable $m$ is maintained throughout.

### 1.2. Conventions and proof scope

All job sets are finite. Maps between job sets, integer intervals, keys, bit vectors and formulas below are ordinary functions of sets; order-preservation is asserted and proved when needed. All restrictions of precedence use the transitive order on the full job set, not merely the arcs induced by a smaller set.

References [L1]–[L8] name the eight attached lessons. They are supplied as CC0 texts. Reference [P] is the supplied preprint source. Section 10 matches their individual lemma statements to the proofs here. Numerical constants from a three-machine statement are replaced by the bounds proved here; its logical assertion is otherwise retained. Assertions about simulations in the task are not used as proof.

## 2. Foundations, descriptions, and the finite search

### Lemma 2.1 (reachability and a rank order)

Let $G=(V,E)$ be a finite directed acyclic graph. Define $x\prec y$ if there is a directed path of positive length from $x$ to $y$.

1. The relation $\prec$ is irreflexive and transitive.
2. For a function $\tau:V\to\mathbb Z$, respecting every arc strictly is equivalent to respecting every pair $x\prec y$ strictly.
3. Repeatedly removing a vertex with no remaining predecessor produces a total order extending $\prec$. With the smallest identifier as a tie-breaker this order is deterministic.

**Proof.** Transitivity follows by concatenating paths; a positive-length path from a vertex to itself would be a directed cycle. Strict inequalities along a path imply the inequality between its endpoints, and every arc is a path. For the last claim, if a finite nonempty remaining set had no minimal element, following predecessors within it would eventually repeat a vertex and give a cycle. Thus a minimal element always exists. If $x\prec y$, vertex $y$ cannot be removed while $x$ remains. The removal order therefore extends $\prec$. $\square$

The reachability relation can be computed by a search from each vertex. For a padded set $J$ of $N$ jobs, write
$$
\lambda:J\longrightarrow[N]=\{1,\ldots,N\}
$$
for the bijection sending a job to its position in this deterministic total order. It is strictly order-preserving: $x\prec y$ implies $\lambda(x)<\lambda(y)$.

### Lemma 2.2 (integer start times)

Suppose a finite collection of unit jobs has nonnegative real start times and a machine-assignment function $\mu:V\to[m]$, with no overlap on a machine and with every precedence completed before its successor starts. There is a feasible integer-slot schedule whose makespan is no larger.

**Proof.** On each machine, order the jobs by their original start times and add an arc from each job to the next. Each original or added arc increases the original start time by at least one, so the augmented graph is acyclic. In a topological order of it, define
$$
s'(v)=\max\bigl(\{0\}\cup\{s'(u)+1:u\text{ is an augmented immediate predecessor of }v\}\bigr).
$$
This defines a function $s':V\to\mathbb Z_{\geq0}$. Induction in the topological order gives $s'(v)\leq s(v)$, since every term in the maximum is at most the original $s(v)$. Added machine-order arcs prevent overlap; original arcs enforce precedence. Setting $\tau(v)=s'(v)+1$ gives the required slot schedule, with completion time at most the original completion time for each job. Nothing depends on $m=3$. $\square$

### Lemma 2.3 (padding)

For a deadline $1\leq T\leq n$, reject if $n>mT$. Otherwise add $mT-n$ distinct isolated jobs. Let $J$ be the resulting set and $N=mT\leq mn$. A **full schedule** of $W\subseteq J$ is a finite sequence of $m$-element antichains partitioning $W$, with $x\prec y$ implying that the slot of $x$ occurs strictly earlier than that of $y$. The empty sequence is a full schedule of the empty set. The original deadline is feasible if and only if $J$ has a full schedule.

**Proof.** A deadline-feasible original schedule leaves exactly $mT-n$ positions among the $m$ machines and $T$ slots. Fill those positions with the distinct isolated jobs. Conversely, deleting isolated padding jobs from a full schedule leaves at most $m$ original jobs in each slot and preserves all original inequalities. Since $N\leq mn$, for fixed $m$ the padded instance has polynomial size. $\square$

### Lemma 2.4 (open-interval replacement)

In a full schedule of $J$, let $W$ consist of all jobs in the slots strictly between two boundary positions $a<b$, where a boundary can be the virtual position before the schedule or after it. Replacing these slots by any full schedule of $W$ preserves a full schedule of $J$.

**Proof.** Every full schedule of $W$ has exactly $|W|/m$ slots, so it fits the same positions. Relations with both endpoints in $W$ are respected by the replacement, and those with neither endpoint in $W$ are unchanged. An exterior job has a slot before the entire interval or after the entire interval. Its temporal relation with every interior job therefore remains the same. This verifies every relation with precisely one endpoint in $W$. $\square$

The replacement means rescheduling the jobs of the interval subject to precedence. It does **not** mean that every arbitrary permutation of its slots is feasible.

### 2.1. Frames, cones, and atomic formulas

There are two **frames**. The forward frame uses the given precedence, time and rank. The reverse frame uses
$$
x\prec_- y\iff y\prec x,\qquad
\lambda_-(x)=N+1-\lambda(x).
$$
For a schedule of $T$ slots its time-reversal map is the bijection $[T]\to[T]$, $t\mapsto T+1-t$. This reverses the sequence of slots and changes a full schedule for $\prec$ into one for $\prec_-$. Applying it twice is the identity. All terms such as “before”, “upset”, “rank” and “predecessor” in an argument refer to its stated frame.

For any $m$-element subset $a\subseteq J$, define
$$
P_a=\{x\in J:(\exists y\in a)\ x\prec y\},\qquad
D_a=\{x\in J:(\exists y\in a)\ y\prec x\},
$$
and $\widehat P_a=P_a\cup a$, $\widehat D_a=D_a\cup a$. These are defined for every $m$-element subset, although the construction uses them at antichain slots. A subset $K\subseteq J$ is an **upset** if $x\in K$ and $x\prec y$ imply $y\in K$; a **downset** satisfies the reversed implication. By transitivity, $D_a,\widehat D_a$ are upsets and $P_a,\widehat P_a$ are downsets. Complements interchange upsets and downsets; unions and intersections preserve either class. Rank suffixes are upsets and rank prefixes are downsets. Reversal exchanges $P$ with $D$, including weak cones.

For the virtual boundary before the schedule set
$$
D=\widehat D=J,\qquad P=\widehat P=\varnothing;
$$
for the virtual boundary after it set
$$
D=\widehat D=\varnothing,\qquad P=\widehat P=J.
$$
The virtual boundaries contain no jobs.

### Lemma 2.5 (cones and time)

At a genuine slot $a$ of a full schedule, jobs of $P_a$ occur strictly before $a$, jobs of $D_a$ strictly after $a$, and no job of $a$ belongs to either strict cone. In particular, no job at or after $a$ belongs to $P_a$, and no job at or before $a$ belongs to $D_a$.

**Proof.** A witness $x\prec y$ with $y\in a$ forces the slot of $x$ to precede $a$. The successor statement is identical with directions reversed. Members of $a$ are pairwise incomparable, and no job precedes itself. The virtual-boundary conventions satisfy the analogous temporal implications. $\square$

A **formula** is a finite full binary tree whose internal vertices are labelled intersection or union, and whose leaves are one of the following subsets or the complement of one of them:

- $J$ and $\varnothing$;
- a rank threshold $\{\lambda\leq k\}$ or $\{\lambda\geq k\}$, with $0\leq k\leq N+1$, in either frame;
- $a,P_a,D_a,\widehat P_a,\widehat D_a$ for an $m$-element subset $a$, in either frame.

Its size is its number of leaves. Evaluation is the function from the set of such formula trees to $2^J$ obtained by interpreting the leaves and internal operations. Write $[F]$ for the evaluated set. For $K\geq1$ let
$$
\mathcal F_K=\{[F]:F\text{ has at most }K\text{ leaves}\}.
$$
A global description of $W$ means $W\in\mathcal F_K$. A relative description of $L\subseteq W$ means $L=W\cap[F]$ for some such $F$; it does not require the intersection with $W$ to have a short global description.

### Lemma 2.6 (complements)

Every formula has a complement formula of exactly the same size.

**Proof.** Complement each leaf and interchange union with intersection at every internal vertex. Induction on the tree, using the two De Morgan identities, proves that the new evaluation is $J\setminus[F]$. No leaf is created or deleted. $\square$

Thus set differences used below are formulas, with leaf counts equal to the sum of the counts of the two operands.

### Lemma 2.7 (finite formula enumeration)

For fixed $m\geq3$ and $K$, the number of formulas with at most $K$ leaves is at most
$$
B=C_{m,K}N^{mK}.
\tag{2.1}
$$
Their evaluated sets can be enumerated and deduplicated as bit vectors by a deterministic algorithm polynomial in $N$.

**Proof.** There are $\binom Nm\leq N^m$ slot subsets. Counting both frames and complements, the leaf alphabet has at most $64N^m$ elements for $N\geq m\geq3$; this generous constant includes the $O(N)$ thresholds and constants. For $\ell$ leaves there are at most $4^\ell$ full binary tree shapes, at most $2^{\ell-1}$ internal labellings, and at most $(64N^m)^\ell$ leaf labellings. Summing gives, for example, $C_{m,K}=K\,512^K$. Enumerate these finite choices, evaluate each using the reachability table, and compare evaluated $N$-bit vectors in pairs to remove duplicates. For fixed $m,K$, every loop has polynomially many iterations. $\square$

### 2.2. The dynamic program

Process the sets of $\mathcal F_K$ in increasing cardinality. A boolean function
$$
\mathsf A:2^J\longrightarrow\{\mathrm{false},\mathrm{true}\}
$$
is initialized as false outside $\mathcal F_K$, and $\mathsf A(\varnothing)=\mathrm{true}$. A set whose size is not divisible by $m$ is false.

For nonempty $W\in\mathcal F_K$ with $m\mid |W|$, a **state** is a disjoint decomposition
$$
W=L\mathbin{\dot\cup}Z\mathbin{\dot\cup}R
$$
such that $Z$ is an $m$-element antichain, $L$ has a relative description in $W$, and the following compatibility tests hold:

- no job in $Z\cup R$ precedes a job in $L$;
- no job in $R$ precedes a job in $Z$.

The state is initial when $\mathsf A(L)$ is true and final when $\mathsf A(R)$ is true. There is a directed transition to $(L',Z',R')$ exactly when
$$
L\cup Z\subseteq L',
\qquad
\mathsf A\bigl(L'\setminus(L\cup Z)\bigr)=\mathrm{true}.
\tag{2.2}
$$
Declare $W$ accepted when an initial state reaches a final state, allowing a path with one state. Every acceptance lookup in this computation concerns a smaller set: $L$ and $R$ omit $Z$, while a transition gap omits at least the nonempty $Z$. Thus the procedure is well-defined.

### Proposition 2.8 (soundness and witnesses)

For any $m\geq1$ and any description family used in this procedure, an accepted set $W$ has a full schedule. Such a schedule can be reconstructed from the accepted states.

**Proof.** Induct on $|W|$. The empty case is immediate. For a path of states $(L_i,Z_i,R_i)$, $1\leq i\leq k$, from initial to final, put
$$
A_0=L_1,\quad
A_i=L_{i+1}\setminus(L_i\cup Z_i)\ (1\leq i<k),\quad
A_k=R_k.
$$
The inclusion in (2.2), together with disjointness of each state, gives the ordered disjoint partition
$$
W=A_0\mathbin{\dot\cup}Z_1\mathbin{\dot\cup}A_1
\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}Z_k\mathbin{\dot\cup}A_k.
\tag{2.3}
$$
For completeness of this set identity, induction on $i$ gives
$L_{i+1}=A_0\dot\cup Z_1\dot\cup A_1\dot\cup\cdots\dot\cup Z_i\dot\cup A_i$; adding the last state's $Z_k,R_k$ proves (2.3).

Each $A_i$ is accepted and smaller than $W$, so it has a full schedule by induction. Concatenate these schedules and the individual slots $Z_i$ in the displayed order. A backward precedence from $Z_j$ into an earlier piece would run from $Z_j$ into $L_j$, violating its state's compatibility. A backward precedence from $A_j$, $j\geq1$, into an earlier piece would run from $R_j$ into $L_j\cup Z_j$, again violating compatibility. These cover every relation between different pieces. Relations inside pieces are respected by their schedules. The concatenation is full.

Store the predecessor of each reached state and the schedule of each accepted smaller set. Backtracking from a reached final state yields the path and hence the displayed schedule. This uses only one $m$-element slot in each state. $\square$

### Definition 2.9 (description hierarchy)

A hierarchy consists of nonempty job sets organized in a rooted tree, together with full-schedule witnesses, as follows.

- The root is $J$ between the two virtual boundaries.
- A node $W$ is the job set of an open interval in its witness schedule of $J$. Its interval may be rescheduled, and then at least one slot is marked.
- Its children are exactly the nonempty gaps between consecutive marks or between a boundary and its nearest mark. Each child receives a copy of the parent's current witness schedule.
- Every node has a global description using at most $K$ leaves. For each mark $z$, the set of jobs of $W$ before $z$ in original time has a relative description using at most $K$ leaves.

Copies separate the witnesses for distinct branches; they are not algorithmic state variables. Every child omits at least one marked slot, so the tree has finite depth.

### Lemma 2.10 (hierarchy implies acceptance)

If $J$ has such a hierarchy, the dynamic program accepts $J$.

**Proof.** Induct on a node's size. List its marked slots in original time as $z_1,\ldots,z_k$. Let $L_i$ and $R_i$ be its jobs before and after $z_i$. Each $(L_i,z_i,R_i)$ is a state: the relative description is part of the hierarchy, and compatibility follows from the witness schedule. The first $L_1$, the last $R_k$, and each gap $L_{i+1}\setminus(L_i\cup z_i)$ are empty or are smaller children. They are accepted by induction. Hence the first state is initial, the last final, and successive states are connected by (2.2). The node is accepted. Apply this at the root. $\square$

The rest of the structural proof constructs a hierarchy with $K=K_m=12m+25$.

## 3. Separators and the shared-cutoff walk

Fix one frame. A **domain** $U$ is the job set of an open interval of a full schedule of $J$. A **cutoff** $S\subseteq U$ is a downset relative to $U$: if $x\in S$, $y\in U$ and $y\prec x$, then $y\in S$. Jobs in $S$ are called low and those in $U\setminus S$ high.

A slot $z$ in the domain is a **separator at $S$** when

(a) every high job before $z$ belongs to $P_z$; and

(b) every low job after $z$ belongs to $D_z$.

Nothing is required of the jobs at $z$ itself. The boundary $a$ immediately before the domain is a separator if all low jobs of $U$ belong to $D_a$; its condition (a) is empty. Put
$$
B_z(H)=P_z\cup(H\setminus\widehat D_z)
\quad(H\subseteq J).
\tag{3.1}
$$

### Lemma 3.1 (separator descriptions)

If $z$ is a slot of $U$ separating $S$, and $H\subseteq J$ satisfies $H\cap U=S$, then $B_z(H)\cap U$ is exactly the set of jobs of $U$ before $z$.

**Proof.** A high job before $z$ belongs to $P_z$ by (a). A low job before $z$ belongs to $H$ and, by Lemma 2.5, not to $\widehat D_z$. This proves inclusion of the prefix. Conversely, a job of $P_z$ is before $z$. A job of $U\cap H\setminus\widehat D_z$ is low, is not in slot $z$, and cannot be after $z$, because condition (b) would put it in $D_z$. Thus it too is before $z$. $\square$

### Lemma 3.2 (reversal of a separator)

A slot $z$ of $U$ separates $S$ in one frame if and only if it separates $U\setminus S$ in the reverse frame.

**Proof.** The complement of a relative downset is a relative upset, hence a cutoff in the reversed order. In the reverse frame, high jobs are the original low jobs, “before” means original “after”, and $P_z$ is original $D_z$. Thus the reversed condition (a) is exactly original (b). Similarly reversed (b) is original (a). Reversing again proves both directions. $\square$

### 3.1. Normalization

A **priority order** on $U$ is a total order extending its precedence restriction. Let $\pi:U\to[|U|]$ be the bijection giving its positions, smaller meaning better priority. Encode a full schedule of $U$ by sorting each slot increasingly by $\pi$ and concatenating the resulting $m$-tuples in time order. A **normalized** full schedule minimizes this finite integer sequence lexicographically among all full schedules of $U$. Such a schedule exists whenever $U$ is schedulable. Normalized schedules are existence witnesses, not schedules that the finite search must compute.

### Lemma 3.3 (no improving exchange, including suffix rearrangements)

Let a normalized schedule of $U$ and one of its slots $r$ be fixed. Replace the slots strictly after $r$ by any full schedule of the same suffix job set, keeping a full schedule of $U$. A job $y$ at $r$ cannot then be exchanged with a later job $x$ satisfying $\pi(x)<\pi(y)$ so that a full schedule of $U$ results.

**Proof.** All slots before $r$ would agree with the normalized schedule. At $r$, the multiset of priority values replaces the value $\pi(y)$ by the strictly smaller distinct value $\pi(x)$. For completeness, lowering one of $m$ values makes every increasing order statistic weakly smaller: for every threshold $q$, the number of values at most $q$ can only increase, which is equivalent to that assertion about order statistics. The sum of the $m$ values decreases strictly. Hence at least one order statistic decreases strictly; the first differing one decreases. The sorted $m$-tuple, and therefore the full encoded schedule, is lexicographically smaller than the normalized one. This is a contradiction. It applies for every $m$, without an exchange involving the other $m-1$ jobs of a slot. $\square$

An exchange in all following proofs swaps two jobs between their slots. It preserves the size of both slots. Feasibility will always be checked through predecessors and successors of those two jobs; all other pairs retain their order.

### Lemma 3.4 (one advance)

Let $U$ have a normalized full schedule for a priority order, and let $M\subseteq L$ be two prefixes of this order. A position is either a slot of $U$ or the boundary $a$ before $U$. Suppose position $s$ satisfies separator condition (a) for $M$.

An **exception for $L$ at $s$** is a job $x\in L$ after $s$ with $x\notin D_s$. Suppose exceptions exist, let $t$ be their earliest slot, and choose an exception $x$ at $t$. If $x\in M$, then:

1. every predecessor of $x$ belonging to $U$ is strictly before $s$;
2. for every $y\in U\setminus M$ at a slot $r$ of $U$ with $s\leq r<t$, some job of $U\setminus M$ at $t$ is a strict successor of $y$;
3. $t$ satisfies condition (a) for $M$.

**Proof.** A predecessor $w\in U$ of $x$ belongs to $L$ because $L$ is a prefix of an order extending precedence. It is before $t$. If it were in $s$, then $x\in D_s$. If it were strictly between $s$ and $t$, the minimality of $t$ would give $w\in D_s$ and hence $x\in D_s$ by transitivity. Both are contradictions. This proves (1), including the case when $s$ is exterior and contains no job of $U$.

For (2), suppose $y$ has no successor in $U$ at or before $t$. Exchange $x$ and $y$. All predecessors of $x$ in $U$ are before $s\leq r$ by (1), and all its successors were after $t$. Thus moving $x$ to $r$ violates no relation involving $x$. The predecessors of $y$ were before $r$ and its successors in $U$ are after $t$ by the supposition, so moving $y$ to $t$ violates none involving $y$. In particular, there is no forbidden relation with another job occupying either new slot. Exterior predecessors of an interior job are before the whole interval, and exterior successors are after it, by the original full schedule. Thus the exchange is feasible in $U$ and also in its full-schedule witness.

But $x\in M$ and $y\notin M$, so $x$ has better priority. Lemma 3.3 forbids the exchange. Therefore $y$ has a successor $y_1\in U$ at some time $r<r_1\leq t$. This successor is outside $M$, since $M$ is a cutoff. If $r_1<t$, apply the same argument to $y_1$. The times strictly increase in a finite interval. The process reaches a successor at $t$, still outside $M$. This proves (2).

For (3), let $y\in U\setminus M$ be before $t$. If its slot is at or after $s$, use (2). Otherwise $s$ must be a slot of $U$, and condition (a) at $s$ gives a job $w$ in $s$ with $y\prec w$. This $w$ is outside $M$, so (2) gives $w\prec w'$ for a job $w'$ at $t$. Hence $y\prec w'$ and $y\in P_t$. $\square$

### Lemma 3.5 (fixed-cutoff walk)

Let $L$ be a priority prefix and suppose $s$ satisfies (a) for $L$. Repeatedly move from the current position to the earliest slot with an exception for $L$, stopping when none exists. The process terminates at a separator for $L$, never moves backward, and does not move from a position already separating $L$.

**Proof.** Lemma 3.4 with $M=L$ preserves (a) at each target. Every move strictly increases the position. There are only finitely many positions. At termination the absence of exceptions is exactly (b). If the starting position already separates $L$, there is no first exception. $\square$

### Lemma 3.6 (shared-cutoff walk)

Let $S$ and $S^+=S\cup\{p\}$ be consecutive priority prefixes. From a separator $s$ for $S$, run the fixed-cutoff walk for $L=S^+$. Its final position $t\geq s$ separates both $S$ and $S^+$.

**Proof.** Condition (a) for $S^+$ already holds at $s$, because the high set shrinks. If there is no exception for $S^+$, then $s$ separates both and there is no move.

Otherwise every old low job after $s$ belongs to $D_s$, so the only possible first exception is $p$. The first target $t_1$ is the slot of $p$. By Lemma 3.4 with $M=L=S^+$, it satisfies (a) for $S^+$. It also satisfies (a) for $S$: the only difference between the two high sets is $p$, which is at $t_1$, not before it.

At each subsequent move, the exception is after $t_1$, and hence is a job of $S^+$ other than $p$, that is, a job of $S$. Apply Lemma 3.4 once with $M=S$ and once with $M=S^+$ to preserve (a) for both cutoffs. At the final position, no exception for $S^+$ remains. This proves (b) for $S^+$ and for its subset $S$. $\square$

The same result applies if the priority order and prefixes are on a larger set $W\supseteq U$, with normalization on the restriction to $U$. The intersection of a priority prefix with $U$ is a prefix of the restricted order. Promoting a job outside $U$ leaves that intersection unchanged, so the walk does not move.

### Corollary 3.7 (a separator can be created)

Let nonempty $U$ be a domain with a full schedule, and let $S$ be any cutoff in it. Some full schedule of $U$ has a slot separating $S$.

**Proof.** Order $S$ first, then $U\setminus S$, each by rank. A relation from the second group into the first would contradict that $S$ is a cutoff, so this is a priority order. Normalize a full schedule for it. The first slot separates the empty cutoff. Promote the members of $S$ in that order, applying Lemma 3.6 each time. The final position is a slot and separates $S$. $\square$

## 4. Centers, sides, and the hierarchy data

Every node $W$ has a full-schedule witness, a tag consisting of one frame, and boundaries $a,b$ in that frame. It carries an ordered list
$$
\mathcal K=(K_1,\ldots,K_\ell)
$$
of upsets of the whole set $J$ in its tag frame. Its **qualifier set** is
$$
\mathcal Q(\mathcal K)=\bigcup_{j=1}^{\ell}K_j,
$$
and its **old high set** is $O=W\cap\mathcal Q(\mathcal K)$. On $\mathcal Q(\mathcal K)$ define the function
$$
\operatorname{key}_{\mathcal K}:
\mathcal Q(\mathcal K)\longrightarrow[\ell]\times[N],
\qquad
x\longmapsto\bigl(\max\{j:x\in K_j\},\lambda(x)\bigr),
\tag{4.1}
$$
with lexicographic order in the target. For an empty list there are no qualifiers and no keys. Keys of distinct qualifiers are distinct, because $\lambda$ is injective.

Each $K_j$ is a fixed subset given by a formula in fixed job subsets and rank thresholds. Changing a witness schedule later does not change that subset.

### Lemma 4.1 (keys respect precedence)

If $x$ qualifies and $x\prec y$, then $y$ qualifies and $\operatorname{key}_{\mathcal K}(x)<\operatorname{key}_{\mathcal K}(y)$.

**Proof.** Every upset entry containing $x$ contains $y$. The largest entry index of $y$ is therefore at least that of $x$. If it is larger, the first coordinate proves the claim; if equal, $\lambda(x)<\lambda(y)$ proves it. $\square$

### 4.1. The three invariants

Every node is required to satisfy the following statements in its tag frame.

**(I1)** $O\subseteq P_b$ and $W\setminus O\subseteq D_a$.

**(I2)** Every qualifier scheduled at or before $a$ belongs to $\widehat P_a$.

**(I3)** After replacing the interval of $W$ by *any* full schedule of $W$, no exchange of a job $x\in W\setminus D_a$ with a qualifier $y$ in slot $a$, satisfying $\operatorname{key}_{\mathcal K}(x)<\operatorname{key}_{\mathcal K}(y)$, gives a full schedule of $J$.

The key of $x$ in (I3) is defined: (I1) implies $W\setminus D_a\subseteq O$. When $a$ is virtual, (I2) and (I3) are empty assertions.

At the root, use the forward frame, virtual boundaries, and $\mathcal K=(J)$. Then $O=J$, (I1) holds by the virtual conventions, and the other two invariants are vacuous.

### Lemma 4.2 (cover and two cutoffs)

In either frame, writing $a,b$ for the node's boundaries in that frame and
$$
X=W\setminus D_a,\qquad Y=W\setminus P_b,
$$
one has
$$
W\subseteq D_a\cup P_b,\qquad X\subseteq P_b,\qquad Y\subseteq D_a.
\tag{4.2}
$$
Both $X$ and $W\cap P_b$ are cutoffs in $W$.

**Proof.** In the tag frame, (I1) puts the two parts $O,W\setminus O$ in $P_b,D_a$ respectively. Thus a job outside $D_a$ is in $O\subseteq P_b$, and a job outside $P_b$ is in $W\setminus O\subseteq D_a$. Reversal interchanges the boundary names and the predecessor/successor cones; it exchanges the roles of $X,Y$ and leaves the assertions equivalent. Finally $J\setminus D_a$ and $P_b$ are downsets, and their intersections with $W$ are relative downsets. $\square$

### 4.2. Choosing the center and treating the two sides

In the tag frame, use Corollary 3.7 to reschedule $W$ so that a slot $v$ separates $W\cap P_b$ on the whole domain $W$. Mark this **center**. At the root use its last slot as the center: with cutoff $J$, (a) has no high job and (b) has no later job.

Treat each side of $v$ as the part before $v$ in a **working frame**. The side before $v$ in the tag frame is the **same side**; the side after it uses the reversed frame and is the **switched side**. On either side let $a,b$ be the node boundaries in that working frame and let $E$ be the open part between $a$ and $v$.

The center separates, on $W$, the cutoff
$$
S_*=
\begin{cases}
W\cap P_b,&\text{same side},\\
X=W\setminus D_a,&\text{switched side}.
\end{cases}
\tag{4.3}
$$
The second assertion follows from Lemma 3.2: the new cutoff is the complement of the old one in $W$, with old $P_b$ becoming new $D_a$.

On a same side set $S_0=(W\setminus O)\cap P_b$, order $S_0$ by rank, then $O$ by key, then $Y$ by rank; promote all jobs of $O$ in key order. On a switched side start with $S_0=\varnothing$, order $X$ by rank and then $W\cap D_a$ by rank; promote all jobs of $X$ in rank order. These orders are on all of $W$.

### Lemma 4.3 (priority orders and cutoff containment)

Both orders extend precedence. The successive low sets are prefixes
$$
S_0\subseteq S_1\subseteq\cdots\subseteq S_q=S_*,
$$
each addition being one promoted job. Every $S_i$ is contained in $P_b$, and $S_0\subseteq D_a$.

**Proof.** On the same side, $S_0,O,Y$ partition $W$ because $O\subseteq P_b$. If $w\prec x$ in $W$ with $x\in S_0$, down-closure gives $w\in P_b$. Also $w\notin O$: qualification of $w$ would force qualification of $x$. Thus $S_0$ is a cutoff. No job of $Y=W\setminus P_b$ precedes a job of $S_0\cup O=W\cap P_b$. Keys extend precedence in $O$ by Lemma 4.1; ranks do so in the other groups. This proves the priority property and the stated prefixes. Their final union is $W\cap P_b$. Invariant (I1) gives $S_0\subseteq D_a$.

On the switched side, $X$ is a cutoff by Lemma 4.2. Ordering it before its complement and using ranks within both groups therefore extends precedence. Its rank prefixes end at $X$, which lies in $P_b$ by (4.2), and its initial cutoff is empty. $\square$

Normalize the open part $E$ for the restricted priority order, independently on both sides. Lemma 2.4 preserves the full schedule. The center remains a separator, since the sets of jobs on its two sides do not change.

### 4.3. Side walks and children

The boundary $a$ separates $S_0$ on $E$, since $S_0\subseteq D_a$. Set $s_0=a$. For each promotion $S_{i-1}\to S_i$, apply Lemma 3.6 on $E$ and let $s_i$ be the walk's final position. Intermediate positions during a promotion are not necessarily marked. Set $s_{q+1}=v$. Then
$$
a=s_0\leq s_1\leq\cdots\leq s_q<s_{q+1}=v.
\tag{4.4}
$$

### Lemma 4.4 (common cutoffs of adjacent positions)

For $0\leq i<q$, both $s_i$ and $s_{i+1}$ separate $S_i$ on $E$. The position $s_q$ separates $S_q$ there, and every high job of $E$ for $S_q$ belongs to $P_v$.

**Proof.** The initial position separates $S_0$. For every promotion, Lemma 3.6 says its final position separates both the previous and the new cutoff. This proves all the paired assertions. For the final endpoint $v$, use that it separates $S_q=S_*$ on the larger domain $W$; its condition (a) covers all high jobs of $E$. $\square$

Mark the distinct $s_i$ that are slots of $E$, together with $v$. For each strict step $s_i<s_{i+1}$, the nonempty gap between them becomes a child $W'$ with working-frame tag and **edge data**
$$
a'=s_i,\qquad b'=s_{i+1},\qquad S=S_i.
\tag{4.5}
$$
Repeated positions do not create a gap. Consecutive distinct positions are separated by exactly one strict step in the nondecreasing sequence (4.4), so these children are exactly the nonempty gaps required by Definition 2.9.

### Lemma 4.5 (edge labels and shrinking)

For each such child, $b'$ is a slot of $W$, and $a'$ is the boundary $a$ or a slot of $E$. Moreover
$$
W'\cap S\subseteq D_{a'}\cap P_b,\qquad
W'\setminus S\subseteq P_{b'}.
\tag{4.6}
$$
The child has fewer jobs than $W$, and the root has no switched-side child.

**Proof.** The position claims follow from (4.4). A low job of the gap is after $a'$, so it lies in $D_{a'}$ by the separator property at $a'$. It lies in $P_b$ because $S\subseteq P_b$. A high job is before $b'$ and belongs to $P_{b'}$ by Lemma 4.4, including the case $b'=v$. The gap omits $v$, giving strict shrinkage. At the root $v$ is the last slot, so the switched side is empty. $\square$

The remaining task is to give each child a short list and to preserve (I1)–(I3). The induction order will be checked explicitly in Section 7.

## 5. Carried and pruned lists

### Lemma 5.1 (suffix carry)

For a nonempty list $\mathcal K=(K_1,\ldots,K_\ell)$, an index $1\leq d\leq\ell$, and $0\leq r\leq N+1$, define
$$
\operatorname{carry}_{d,r}(\mathcal K)
=
\bigl(K_d\cap\{\lambda\geq r\},K_{d+1},\ldots,K_\ell\bigr).
\tag{5.1}
$$
This is a function, for each permitted $d,r$, from lists of length at least $d$ of upsets of $J$ to lists of upsets of $J$. Its qualifiers are exactly those old qualifiers whose old key is at least $(d,r)$. On those qualifiers its new key order agrees with the old one.

**Proof.** Let $j$ be a qualifier's largest old entry index. If $j>d$, that entry survives unchanged, so the job qualifies. If $j=d$, it qualifies precisely when its rank is at least $r$. If $j<d$, no kept entry contains it. These three cases give exactly the threshold on the old key. For every surviving qualifier, its largest qualifying index is decreased by the same amount $d-1$, and its rank is unchanged. Hence every pairwise comparison is preserved. The first entry remains an upset because it is an intersection of two upsets; the other entries already are upsets. $\square$

**Pruning on $W'$** means deleting every entry disjoint from $W'$ and retaining the order of the others. It is a function from finite lists of subsets of $J$ to such lists. It preserves the union's intersection with $W'$.

### Lemma 5.2 (comparison after pruning)

Suppose a list is pruned on $W'$. Let $x\in W'$ and $y\in J$ both qualify after pruning. If the pruned key of $x$ is smaller than the pruned key of $y$, then their old keys have the same strict inequality.

**Proof.** Before renumbering the retained entries, let $M(z)$ be the largest old index containing $z$ and $R(z)$ the largest retained old index containing $z$. Every entry containing $x$ meets $W'$, so $R(x)=M(x)$; for $y$ one has $R(y)\leq M(y)$. Renumbering the retained indices preserves their order.

If $R(x)<R(y)$, then $M(x)<M(y)$. If $R(x)=R(y)$ and $\lambda(x)<\lambda(y)$, either $M(x)<M(y)$ or $M(x)=M(y)$, in which case the rank inequality decides. Both cases prove the assertion. The condition $x\in W'$ is essential to the equality $R(x)=M(x)$; we do not assert order preservation for arbitrary exterior pairs. $\square$

### 5.1. The two child updates

For an edge $W\to W'$ on a same side, with cutoff $S$, let the **carry** be empty if $O\setminus S=\varnothing$. Otherwise let $(d,r)$ be the least old key of a job of $O\setminus S$, and use (5.1). Append the **injection**
$$
I=D_a\setminus P_b
\tag{5.2}
$$
as the last entry, then prune on $W'$. The injection is an upset: it is the intersection of $D_a$ and the complement of the downset $P_b$.

On a switched side, discard the old list. Section 6 will construct an upset $G$ in the working frame satisfying
$$
X=W\setminus D_a\subseteq G,\qquad
G\cap\{x:x\text{ is scheduled at or before }a\}=\varnothing.
\tag{5.3}
$$
The cutoff $S$ is a rank prefix of $X$. Choose $h$ so that
$X\setminus S=X\cap\{\lambda\geq h\}$, taking $h=N+1$ if $X\subseteq S$. Use the **switch pair**
$$
\bigl(G\cap\{\lambda\geq h\},D_a\bigr)
\tag{5.4}
$$
and prune it on $W'$.

### Lemma 5.3 (qualifiers and child (I1))

For either update, the union before pruning intersects $W$ in exactly $W\setminus S$, and its key order on that set agrees with the side's priority order. After pruning, its qualifiers in $W'$ are exactly $W'\setminus S$. With this list, $W'$ satisfies (I1) in its tag frame.

**Proof.** On a same side, $O$ is promoted in key order. By Lemma 5.1, the carry selects exactly $O\setminus S$ within $W$ and preserves its old key order. By Lemma 4.2,
$$
W\cap I=(W\cap D_a)\setminus P_b=Y.
$$
The sets $Y$ and $O$ are disjoint, since $O\subseteq P_b$. Also $W=S_0\dot\cup O\dot\cup Y$, and $S$ is $S_0$ together with the promoted part of $O$. Thus the new qualifiers in $W$ are $(O\setminus S)\dot\cup Y=W\setminus S$. Placing the injection last puts $Y$ after the carry qualifiers, with rank order inside $Y$, exactly as in the priority order.

On a switched side, $G\supseteq X$ implies that the first entry selects exactly $X\setminus S$ within $X$. The second entry selects $W\cap D_a=W\setminus X$. Its larger index puts every job of this second group after those of $X\setminus S$, regardless of any overlap with the first entry. Keys use rank within each group, agreeing with the priority order. The union in $W$ is again $W\setminus S$.

Pruning changes no qualification within $W'$. Therefore the child's old high set is $O'=W'\setminus S$. Equation (4.6) gives $O'\subseteq P_{b'}$ and $W'\setminus O'=W'\cap S\subseteq D_{a'}$, exactly child (I1). $\square$

### 5.2. Runs and a capacity witness

A **run** is a chain along a branch with a fixed tag, starting at the root or at a child created by a switched update, and proceeding only through same-side updates. Its initial entries are the root entry or the two entries of its initial switch pair. Every other entry is descended from an injection appended during the run.

### Lemma 5.4 (entry shape)

Each entry is an initial entry of its run or an injection appended in that run, intersected with at most one rank suffix in the run's frame.

**Proof.** Subsequent operations keep or delete an entry, or intersect it with a rank suffix. Intersecting two suffixes gives the suffix at the maximum of their thresholds:
$$
\{\lambda\geq r\}\cap\{\lambda\geq r'\}
=\{\lambda\geq\max(r,r')\}.
$$
All thresholds in one run use the same rank. Thus at most one suffix is needed in the resulting expression. A switched update starts a new run and deletes the earlier list. $\square$

### Lemma 5.5 (at most $m$ injections and $m+2$ entries)

Every pruned list contains at most $m$ injections and at most $m+2$ entries.

**Proof.** A new run starts with at most two initial entries and no injection. Consider a same update $W\to W'$ and its surviving injection entries.

First, any two such entries are disjoint when restricted to $W$. Consider the earlier edge $U\to U'$ at which the later injection was appended. At that time the older entry belonged to the carry, whose qualifiers within $U$ were old qualifiers, hence belonged to $P_{b_U}$ by (I1). The later injection met $U$ only in $U\setminus P_{b_U}$. They were therefore disjoint on $U$. Afterwards entries could only shrink, and $W\subseteq U$, so they remain disjoint on $W$.

Let $\mathscr I$ be the finite set of surviving injection entries, distinguished by their times of creation. Each $K\in\mathscr I$ meets $W'$; choose the job $x_K\in K\cap W'$ of least rank. By Lemma 5.3 this is a high job of the child. By (4.6), $x_K\in P_{b'}$, so some job of slot $b'$ is a strict successor of $x_K$. Since $K$ is an upset of all of $J$, it contains that successor.

Define a function of finite sets
$$
f:\mathscr I\longrightarrow b'
$$
by choosing, for each $K$, the least-rank job in $b'$ which is a successor of $x_K$. It belongs to $K$. The slot $b'$ belongs to $W$ by Lemma 4.5. If $f(K)=f(K')$ for different injection entries, that job would belong to their intersection inside $W$, contradicting the disjointness just proved. Thus $f$ is injective, and $|\mathscr I|\leq|b'|=m$.

Adding at most two initial entries gives $m+2$. This argument uses the global upset property because the witness in $b'$ is outside $W'$. It uses no statement about formula size or deeper nodes. $\square$

Before pruning, a newly appended list may have $m+3$ entries. Every carry used in the estimates below comes from a pruned list and contains at most $m$ injections and at most two initial entries.

## 6. Direction changes and bounded formulas

### Lemma 6.1 (local flattening of the initial pair)

Suppose a run starts on a switched side of a node $Q_0$. In the run's frame its initial pair is
$$
G_0\cap\{\lambda\geq h_0\},\qquad D_{a_0},
$$
where $G_0$ is an upset containing $Q_0\setminus D_{a_0}$. Let $U\subseteq Q_0$ be a node in this run. Suppose a same-side carry out of $U$ still retains the first initial entry, now in the form $G_0\cap\{\lambda\geq k\}$. On $U$, the union of the carried descendants of the initial pair agrees with
$$
D_{a_0}\cup\{\lambda\geq k\}.
\tag{6.1}
$$

**Proof.** A carry retains a suffix and trims only its first entry. If it ever starts at the second initial entry or later, the first initial entry is permanently deleted. Therefore, as long as the first survives, the second has never been trimmed. The second either remains exactly $D_{a_0}$ or was deleted by pruning on an earlier node containing $U$, in which case it is disjoint from $U$.

Within $U\cap D_{a_0}$, the second entry, when relevant, selects every job. Within $U\setminus D_{a_0}$, all jobs belong to $G_0$ because $U\subseteq Q_0$; there the first entry selects exactly the rank suffix. This proves equality on $U$. Both terms in (6.1) are upsets. No equality outside $U$ is claimed or used. $\square$

### Lemma 6.2 (short extension of an earlier low set)

For an edge $U\to W$ with low cutoff $H\subseteq U$ in its working frame, there exists a downset $H^*\subseteq J$ in that frame such that
$$
H^*\cap U=H,
\tag{6.2}
$$
and $H^*$ has a formula of at most $3m+3$ leaves.

**Proof.** Use $a_U,b_U$ for the boundaries of $U$ in this edge's working frame.

If the edge is on a switched side, $H$ is a rank prefix of $U\setminus D_{a_U}$. Let $r$ be its largest rank, or $0$ for an empty prefix. Then
$$
H^*=(J\setminus D_{a_U})\cap\{\lambda\leq r\}
\tag{6.3}
$$
is a downset described with two leaves and has the required intersection.

For a same-side edge, let $\Phi$ be the carry union before the injection. By Lemma 5.3, or directly by its same-side calculation,
$$
H=(U\cap P_{b_U})\setminus\Phi.
\tag{6.4}
$$
The carry contains at most $m$ injection descendants. Each has at most three leaves: $D$, the complement of $P$, and at most one rank suffix.

Its initial contribution can be replaced on $U$ by an upset using at most two leaves, as follows. In a root run, the root entry with a suffix simplifies to a rank suffix (or a constant). In a switched run, if the first initial descendant survives, replace it and the second if present by (6.1). If the first does not survive, the only possible initial contribution is the second entry with at most one suffix, using two leaves. If no initial entry remains, omit that contribution. These cases exhaust the run's initial entries.

Thus there is an upset $\Phi'$ agreeing with $\Phi$ on $U$, with at most
$$
3m+2
\tag{6.5}
$$
leaves. If the carry is empty, the constant false is an allowed one-leaf substitute and also satisfies this bound. Set
$$
H^*=P_{b_U}\cap(J\setminus\Phi').
\tag{6.6}
$$
The complement of an upset is a downset, so this is a downset. Equations (6.4) and the agreement on $U$ prove (6.2). Its leaf count is at most $1+(3m+2)=3m+3$. This construction has eliminated the old switch formula, rather than embedding its historical expression. $\square$

### Lemma 6.3 (arrangement at a switch)

Suppose a switched side of $W$ produces a nonempty child. Then $W$ is not the root. Let $U$ be its parent. In the current, switched frame write $a_-,b_-$ for the boundaries of $U$, $v_-$ for its center, and $a,b$ for the boundaries of $W$. Then $a$ is a genuine slot and
$$
a_-<v_-\leq a<b\leq b_-.
\tag{6.7}
$$

**Proof.** The root has no switched-side child by Lemma 4.5. The edge $U\to W$ was taken in the tag frame of $W$, opposite to the current frame. In that old frame, $W$ is a gap before $U$'s center. Its old right boundary is a slot and is at or before that center; its old left boundary is at or after $U$'s left boundary. Reversal sends its old right boundary to $a$, its old left boundary to $b$, the old right boundary of $U$ to $a_-$, and the old left boundary to $b_-$. These inequalities give (6.7). $\square$

Let $H$ be the old cutoff of edge $U\to W$ and let $H^*$ be its extension from Lemma 6.2. It is a downset in that old frame, hence an upset in the current one. Define
$$
G
=
D_{a_-}
\cap(J\setminus\widehat P_a)
\cap(J\setminus\widehat P_{v_-})
\cap H^*.
\tag{6.8}
$$

### Lemma 6.4 (the switch upset)

The set (6.8) is an upset in the current frame, contains all of $X=W\setminus D_a$, and contains no job scheduled at or before $a$.

**Proof.** Each factor of (6.8) is an upset: a successor cone, two complements of downsets, and $H^*$.

Let $x\in X$. If $x$ had been high at the edge $U\to W$, (4.6) would put it in the old predecessor cone of that edge's right boundary. That boundary is current $a$, and its old predecessor cone is current $D_a$, contradicting $x\in X$. Thus $x\in H$. Every old edge cutoff lies in the old $P$-cone of $U$'s old right boundary, by Lemma 4.3. This cone is current $D_{a_-}$, so $x\in D_{a_-}$. It is after $a$ and hence after $v_-$; Lemma 2.5 excludes it from both weak predecessor cones in (6.8). Finally $x\in U$ and (6.2) give $x\in H^*$. This verifies every factor, proving $X\subseteq G$.

Now suppose $z\in G$ is at or before $a$. Its membership in $D_{a_-}$ puts it strictly after $a_-$. From (6.7) it is also before $b_-$. Therefore $z\in U$, and only after this localization may we use (6.2), obtaining $z\in H$.

If $z$ is at or before $v_-$ in the current frame, it is at or after the center in the old frame. At the center it belongs to $\widehat P_{v_-}$. Otherwise it is a low job after the old center: $H$ is contained in that side's center cutoff, and the center separates that cutoff on $U$. Thus it lies in old $D_{v_-}$, which is current $P_{v_-}$. Either possibility contradicts its exclusion from $\widehat P_{v_-}$.

If $z$ is strictly after $v_-$ and at or before $a$, in the old frame it is on the side before the center, at or after the old edge's right boundary $a$. At that boundary it belongs to its weak cone; after that boundary it is low for $H$ and belongs to old $D_a$ by Lemma 4.4. Hence in either event it is in current $\widehat P_a$, another contradiction.

These separator statements were established in the witness of $U$. Subsequent changes on this branch before constructing (6.8) occurred only inside $W$, strictly between $a,b$. Jobs at or before $a$, the boundary slots and center used here, and the fixed sets $H,H^*$ have not changed. Thus the separator information used for $z$ remains valid in the current witness. This proves all three assertions. $\square$

This supplies exactly (5.3), for the whole parent's $X$, not merely its intersection with a chosen child. It also proves that the switch pair has no qualifier at or before $a$: the first entry is contained in $G$, and the second in $D_a$.

### Lemma 6.5 (individual and aggregate leaf bounds)

Every list entry is described by at most $3m+7$ leaves. More particularly:

- an injection descendant has at most three leaves;
- the root's initial descendant has at most two leaves, and the second initial descendant of a switched run at most two;
- only the first initial descendant of a switched run may need $3m+7$ leaves.

Every pruned-list union and every carry union has a description with at most
$$
A_m=6m+9
\tag{6.9}
$$
leaves.

**Proof.** The first two bounds follow from Lemma 5.4 and their displayed definitions. Formula (6.8) has three cone factors in addition to $H^*$, so it has at most $3+(3m+3)=3m+6$ leaves. A first switch entry adds one rank suffix, giving $3m+7$. Further suffix intersections combine with that same suffix; they do not add indefinitely. A new run discards the old list.

For an aggregate union in a switched run, bound its at most $m$ injections by $3m$, its possible first initial entry by $3m+7$, and its possible second by $2$. Their sum is $6m+9$. If some entries are absent, omitting them only reduces the bound. For a root run, the bound is smaller. An empty union is the constant false and costs one leaf. The same reasoning applies to a carry from a pruned list, because it cannot increase the number of entries and only combines a suffix into its first entry. $\square$

This aggregate count is why the final leaf budget is linear in $m$. Multiplying the uniform per-entry bound by $m+2$ would give a valid but unnecessarily quadratic estimate. Keeping the old three-machine value $25$ unchanged for all $m$ would not be justified by the original calculation.

## 7. Preserving the exterior boundary invariants

The preparatory rescheduling of a node preserves its existing invariants. In (I1) its job set and all cone/list sets are fixed. In (I2) jobs at or before its left boundary and the boundary slot do not move. In (I3) the quantifier already includes every full replacement schedule of its interval. Thus choosing a center and normalizing the two sides does not invalidate the induction hypotheses.

Fix an edge $W\to W'$ with working-frame boundaries $a,b$, normalized side $E$, and data $a'=s_i$, $b'=s_{i+1}$, $S=S_i$. The child's tag is this working frame.

### Lemma 7.1 (child (I2))

Every qualifier of the child's pruned list scheduled at or before $a'$ belongs to $\widehat P_{a'}$.

**Proof.** Pruning can only remove qualifiers, so take a qualifier $z$ of the list before pruning at or before $a'$.

**Case 1: $z$ is after $a$.** The interval between $a$ and $a'$ lies in $E$, since $a'$ is before the center. Thus $z\in E\subseteq W$ and it is high for $S_i$ by Lemma 5.3. If it occupies $a'$, it belongs to $\widehat P_{a'}$. Otherwise it is a high job before the separator $a'$ and therefore belongs to $P_{a'}$.

**Case 2: $z$ is at or before $a$.** No injection qualifier can be here, since the injection is contained in $D_a$. Neither switch-pair entry can have a qualifier here, by Lemma 6.4 and the last paragraph following its proof. Therefore this is a same update, and $z$ qualifies through its carry. Lemma 5.1 implies that it was an old qualifier. Parent (I2) gives a job $y$ in slot $a$ with $z=y$ or $z\prec y$. The carry union is an upset, so $y$ also qualifies through the carry. In particular $a$ is genuine.

If $a'=a$, the old (I2) assertion is already the desired one. Suppose $a'>a$. Follow every actual advance of the walk between $a$ and $s_i=a'$, including positions within a promotion that were not marked. Such an advance uses a cutoff $S_j\subseteq S_i$. By Lemma 5.3, the carry at the final edge selects in $W$ exactly $O\setminus S_i$, so every carry qualifier in $E$ is high for every cutoff encountered in this part of the walk.

Let the first advance leave $a$ for the slot $t$ of an exception $x$, during promotion $j\leq i$. We verify the required boundary exchange carefully.

1. **Every predecessor of $x$ in $J$ is strictly before $a$.** Every predecessor is before $t$ by feasibility. A predecessor in slot $a$ would imply $x\in D_a$. A predecessor strictly between $a$ and $t$ would be a job of $E$ in $S_j$ (because $S_j$ is a priority prefix and $x\in S_j$). Since $t$ is the earliest exception slot, that predecessor would lie in $D_a$, again implying $x\in D_a$. Both contradict that $x$ is an exception. This checks the assertion globally, including exterior jobs.

2. **The old key of $x$ is smaller than that of $y$.** Since $x\notin D_a$, (I1) gives $x\in O$. It does not belong to $S_0\subseteq D_a$, so its presence in $S_j\subseteq S_i$ means it was promoted from $O$. The carry is nonempty in this case; let $(d,r)$ be its threshold, the least key in $O\setminus S_i$. The promotion order gives $\operatorname{key}(x)<(d,r)$, while Lemma 5.1 gives $\operatorname{key}(y)\geq(d,r)$.

3. **The exchange of $x$ with $y$ is forbidden by parent (I3).** The current schedule in $W$ is a full replacement of its old witness, $x\in W\setminus D_a$, and $y$ is an old qualifier at $a$ with the requisite key inequality.

4. **Consequently $y$ has a successor at or before $t$.** If it did not, swapping $x,y$ would be feasible: the global predecessors of $x$ are before $a$ by item 1, and its successors are after $t$; the predecessors of $y$ are before $a$ by the old schedule, and its successors would be after $t$ by the supposition. These facts also exclude comparabilities between a moved job and any companion in either destination slot. All other relations are unchanged. This would contradict item 3.

Such a successor $y_1$ of $y$ is after $a$ and at or before $t$, hence in $E$, and qualifies through the upset carry. If it is at $t$, the first advance has propagated a carry qualifier from $a$ to $t$. If it is strictly before $t$, apply Lemma 3.4(2) with $M=L=S_j\cap E$, starting at boundary $a$; the order and cutoff restrictions are as in the paragraph after Lemma 3.6. Its hypotheses hold: condition (a) at the exterior boundary is empty, $x$ is the earliest exception and is low, and $y_1$ is high. The lemma gives a successor of $y_1$ at $t$. The upset carry contains it. Thus in all cases $y$ has a carry-qualifying successor at the first target. This target job cannot be $x$, which is low.

For a later advance from a genuine slot $s$ to $t'$, its cutoff is some $S_j\subseteq S_i$. A carry qualifier at $s$ is high for that cutoff. Lemma 3.4(2), with $M=L=S_j\cap E$, gives a strict successor at $t'$; it still qualifies through the carry because the union is an upset. Following all actual advances gives a job in $a'$ strictly above $y$. Since $z=y$ or $z\prec y$, it follows that $z\in P_{a'}$.

This proves (I2) in both cases. The sole use of the external exchange invariant was at the first advance; all later exchanges are internal to normalized $E$. $\square$

### Lemma 7.2 (child (I3))

Replace the interval of $W'$ by any full schedule of $W'$. Let $x\in W'\setminus D_{a'}$ and let $y$ be a qualifier of its pruned list in slot $a'$, with child's key of $x$ smaller than that of $y$. Exchanging $x,y$ cannot give a full schedule of $J$.

**Proof.** Child (I1), already proved in Lemma 5.3, makes $x$ a qualifier. Lemma 5.2 shows that the inequality between its key and that of $y$ holds already before pruning.

If $a'>a$, the slot $a'$ belongs to $E$, so both $x$ and $y$ belong to $W$. By Lemma 5.3 they are high for $S_i$, and their pre-pruning key order agrees with the side's priority order. Thus $x$ has better priority than $y$. The arbitrary replacement of $W'$ changes only slots of $E$ strictly after $a'$ and, by Lemma 2.4, gives a full schedule of $E$. If the exchange were feasible in $J$, its restriction would be a full schedule of $E$ violating Lemma 3.3 at $r=a'$. This is impossible.

If $a'=a$, a switched update has no qualifier at $a$, so that case has no $y$. In a same update, $x\notin D_a$ by hypothesis and $y\notin D_a$ by Lemma 2.5. Neither can qualify through the injection. They both qualify through the carry, and Lemma 5.1 transfers the strict key inequality to the old list. Also $x\in W\setminus D_a$, while $y$ is an old qualifier in $a$. The preparatory changes in $W$ followed by the chosen schedule of $W'$ form a full schedule of $W$ in its interval. Parent (I3) therefore forbids exactly this exchange. $\square$

### Proposition 7.3 (valid construction, with no circular induction)

Starting from any full schedule of $J$, every node and update described in Sections 4–7 is well-defined. Each pruned list has at most $m+2$ entries with the bounds of Lemma 6.5, each node satisfies (I1)–(I3), and every branch terminates.

**Proof.** Induct from the root. Its data and invariants were verified in Section 4. Assume the data of a node and all its ancestors have been constructed and validated. Corollary 3.7 and Lemma 2.4 supply its center and normalized sides. Lemmas 4.3–4.5 give the walks, marks and child edge data.

A same update uses only this node's existing list. A switched update uses the earlier edge from its parent: its cutoff and, for a same edge, its already formed carry. Lemma 6.1 uses that earlier run's initial entries, which likewise already exist. Lemma 6.2 gives the earlier low-set extension, and Lemmas 6.3–6.4 give the current $G$. None asks for a descendant's invariant or formula.

The new list is an upset list; Lemma 5.3 proves its qualifier identity and (I1). Lemma 5.5 proves its length using only that identity, global upsets, and existing edge labels. The leaf estimate of Lemma 6.5 uses the length bound and flattening, not an unproved boundary invariant. Finally Lemmas 7.1–7.2 establish (I2) and (I3) from the parent's corresponding hypotheses. This closes the induction.

Every child omits the center of its parent and has a full schedule; its number of slots is strictly smaller. Thus no branch can have more than $N/m$ nonempty nodes. Each node has finitely many children, so the resulting tree is finite. $\square$

## 8. Global descriptions and the structure theorem

Fix a node $W$ and a side, with working-frame boundaries $a,b$, center $v$, open part $E$ and cutoffs $S_i$.

For a same side, let $\Phi_i$ be the carry union determined by $O\setminus S_i$, before adding an injection, and put
$$
\widetilde S_i=P_b\setminus\Phi_i.
\tag{8.1}
$$
For a switched side, let $r_i$ be the last promoted rank in $X$, or $0$ before any promotion, and put
$$
\widetilde S_i=(J\setminus D_a)\cap\{\lambda\leq r_i\}.
\tag{8.2}
$$
These predicates are defined for all cutoffs, including those associated with empty gaps.

### Lemma 8.1 (cutoff predicates)

For every side and every $i$,
$$
\widetilde S_i\cap W=S_i.
\tag{8.3}
$$
The predicate has at most $A_m+1$ leaves, where $A_m=6m+9$.

**Proof.** On a same side, the carry selects $O\setminus S_i$ in $W$ by Lemma 5.1. Since $W\cap P_b=S_0\dot\cup O$ and $S_i$ consists of $S_0$ and the promoted part of $O$, subtracting that carry gives exactly $S_i$. Its union has at most $A_m$ leaves by Lemma 6.5, so adding the $P_b$ factor gives $A_m+1$. On a switched side (8.2) is exactly the promoted rank prefix of $X$ within $W$, and uses two leaves. This is below $A_m+1$. $\square$

These are agreement predicates, not global descriptions of the cutoffs as standalone sets. Their behavior outside $W$ is not assumed.

### Lemma 8.2 (global description of a child)

For a child $W'$ with edge data $a',b',S=S_i$ and pruned list $\mathcal K'$, one has the following equalities of subsets of **all** $J$:
$$
W'\setminus S
=
\mathcal Q(\mathcal K')
\cap P_{b'}
\cap(J\setminus\widehat P_{a'}),
\tag{8.4}
$$
and
$$
W'\cap S
=
D_{a'}
\cap P_b
\cap(J\setminus\widehat D_{b'})
\cap(J\setminus\widehat D_v)
\cap\widetilde S_i.
\tag{8.5}
$$

**Proof.** For (8.4), a high job of $W'$ qualifies by Lemma 5.3, belongs to $P_{b'}$ by (4.6), and is after $a'$, excluding membership in $\widehat P_{a'}$. Conversely, let a job satisfy the right-hand side. Its $P_{b'}$ membership puts it before $b'$. If it were at or before $a'$, child (I2) would put it in $\widehat P_{a'}$, contrary to the last factor. Hence it is strictly between $a',b'$, so in $W'$. The qualifier identity then makes it high.

For (8.5), first let $z$ satisfy the right-hand side. Membership in $D_{a'}$ puts it after $a'\geq a$, and membership in $P_b$ puts it before $b$. Thus $z\in W$. Now, and only now, (8.3) shows $z\in S_i$. Since $S_i\subseteq S_*$, a job in the center would belong to $\widehat D_v$ and a job after the center would belong to $D_v$ by the center's separator condition. Both are excluded. Therefore $z$ belongs to the side $E$. If it were in $b'$ or after it on that side, it would belong to $\widehat D_{b'}$ by its being low and by Lemma 4.4. For $b'=v$, the preceding center exclusion already handles this case. Thus $z$ lies strictly between $a',b'$, and belongs to $W'\cap S$.

Conversely, a low job of $W'$ is in $D_{a'}\cap P_b$ by (4.6), is in $\widetilde S_i$ by (8.3), and occurs before $b'$ and $v$. Lemma 2.5 excludes it from both indicated weak successor cones. It satisfies every factor of the right-hand side. $\square$

The localization in this proof is a logical order of justification. Boolean intersections commute; no assertion about a required operational evaluation order is being made. In particular, the parent description is not silently inserted into (8.5).

### Lemma 8.3 (relative descriptions at every mark)

For each mark $z$ of $W$, its original-time prefix inside $W$ has a relative description.

**Proof.** In the working frame of a side containing $z$, or either side for the center, put
$$
H_*=
\begin{cases}
P_b,&\text{same side},\\
J\setminus D_a,&\text{switched side}.
\end{cases}
$$
Then $H_*\cap W=S_*$. By Lemma 3.1 the formula
$$
F_v=B_v(H_*)
\tag{8.6}
$$
selects inside $W$ exactly the open side $E$ before the center.

For a side mark $z=s_i$ with $i\geq1$, Lemma 4.4 says $z$ separates $S_i$ on $E$. Set
$$
F_z=B_v(H_*)\cap B_z(\widetilde S_i).
\tag{8.7}
$$
Within $W$ the first factor selects $E$. Within $E$, (8.3) and Lemma 3.1 show that the second selects its jobs before $z$. These are all the jobs of $W$ before $z$ in the working frame.

If that is the forward frame, use $F_z$. If it is the reverse frame, the original-time prefix is described relatively by
$$
(J\setminus F_z)\setminus z.
\tag{8.8}
$$
Indeed the jobs of $W$ partition into its working-frame prefix, the slot $z$, and its working-frame suffix; the latter is the original-time prefix. Lemma 2.6 permits complementation without increasing the leaf count, and membership in $z$ is one atom. The same conversion works for the center formula (8.6). $\square$

### Lemma 8.4 (uniform leaf counts)

Every child has a global description with at most $12m+25$ leaves. Every marked prefix has a relative description with at most $6m+16$ leaves.

**Proof.** Use $A_m=6m+9$. The qualifier union in (8.4) has at most $A_m$ leaves, so that equation's right-hand side has at most $A_m+2$. The right-hand side of (8.5) adds four one-leaf cone tests to a cutoff predicate of at most $A_m+1$ leaves, giving at most $A_m+5$. Their union describes $W'$ globally and costs at most
$$
(A_m+2)+(A_m+5)=2A_m+7=12m+25.
\tag{8.9}
$$

The center formula $B_v(H_*)$ uses three leaves. The second factor in (8.7) uses at most $1+(A_m+1)+1=A_m+3$. Thus (8.7) uses at most $A_m+6$, and reversal (8.8) adds one leaf. This gives
$$
A_m+7=6m+16.
\tag{8.10}
$$
Every cone used is attached to a genuine $m$-element slot or is a constant for a virtual boundary. Every threshold is in one of the two permitted frames. These are formulas in exactly the alphabet of Section 2, rather than a more expressive language. $\square$

### Theorem 8.5 (the $m$-machine structure theorem)

Every full schedule of $J$ on $m$ machines admits a hierarchy in the sense of Definition 2.9 with
$$
K_m=12m+25.
\tag{8.11}
$$
Its root has the one-leaf description $J$, every other node has a global description of at most $K_m$ leaves, and every marked original-time prefix has a relative description of at most $6m+16\leq K_m$ leaves. These bounds are independent of the depth.

**Proof.** Apply the construction validated in Proposition 7.3. It marks at least the center of every nonempty node, and its children are exactly the nonempty gaps. Lemma 8.2 supplies their global descriptions without intersecting with any parent's description. Lemma 8.3 supplies all marked relative prefixes. Lemma 8.4 gives the bounds and Proposition 7.3 gives finiteness. These verify every item of Definition 2.9. $\square$

## 9. Correctness, running time, and answers to Q1–Q3

### Theorem 9.1 (correctness of the actual finite algorithm)

Run the dynamic program of Section 2 with $m$-element slots and $K=K_m$. It accepts the padded set $J$ if and only if $J$ has a full schedule. It returns a full schedule whenever it accepts. Consequently it exactly decides the original deadline and constructs an optimum by testing deadlines.

**Proof.** Acceptance implies a full schedule by Proposition 2.8. If a full schedule exists, Theorem 8.5 supplies a hierarchy, and Lemma 2.10 forces acceptance. Padding and its removal are correct by Lemma 2.3.

For a nonempty instance and an arbitrary integer $T$, reject if $T<1$. If $T\geq n$, use the topological order to schedule one job per slot and accept without padding to a possibly very large $mT$. For $1\leq T<n$, reject if $n>mT$; otherwise apply the padded algorithm. For optimization, test $T=1,\ldots,n$ and return the first accepted schedule. The last deadline is always feasible and the first accepted one is the optimum by the decision equivalence. Assign the at most $m$ original jobs of each slot to distinct machines, for example by identifier order. $\square$

The construction involving normalized schedules serves as a certificate of completeness. The algorithm does not need an oracle that computes those normalized schedules.

### Proposition 9.2 (explicit multitape time bound)

For fixed $m\geq3$ and leaf budget $K$, the padded dynamic program can be implemented on a deterministic multitape Turing machine in
$$
O_{m,K}\!\left(N^{\,5mK+4m+1}\right)
\tag{9.1}
$$
steps, including construction of a witness schedule.

**Proof.** Let $B=C_{m,K}N^{mK}$ be the formula bound from Lemma 2.7, so there are at most $B$ distinct described sets. For a fixed $W$, enumerate a formula for its relative left part and a set $Z$ of $m$ jobs. These determine $L=W\cap[F]$ and $R=W\setminus(L\cup Z)$, after rejecting candidates with $Z\not\subseteq W$, overlap, non-antichain $Z$, or invalid compatibility. Thus there are at most
$$
S=BN^m
\tag{9.2}
$$
candidate states. Duplicates are harmless; retaining them only respects this upper bound. No extra boundary slots need be stored to define a state.

Store described sets as $N$-bit vectors; store accepted schedules explicitly, with at most $N$ job identifiers of $O(\log N)$ bits. Store for the current $W$ each state's three parts, reachability bit, and predecessor-state number. For fixed $m,K$ a state record has $O_{m,K}(N)$ bits: its index needs $O_{m,K}(\log N)$ bits, in addition to the three bit vectors.

Use sequential scans only. Fetching or updating a state record costs
$O_{m,K}(SN)=O_{m,K}(BN^{m+1})$. An acceptance lookup can scan all $B$ bit vectors and costs at most $O_{m,K}(BN^2)$. Checking compatibility by repeated scans of the $N\times N$ reachability table costs at most $O(N^4)$. Because $m\geq3$, both of these costs fit within $O_{m,K}(BN^{m+1})$.

Initialize the reachable states, then make at most $S$ passes over all $S^2$ ordered pairs, marking a state whenever an already reached state has a transition to it. If a state is reachable, there is a simple path of fewer than $S$ edges to it; after $S$ passes every such state has been found. Each pair test, including set comparisons, acceptance lookup and record update, fits the preceding per-operation bound. Over all $B$ sets, the cost is at most
$$
\begin{aligned}
O_{m,K}\bigl(B\cdot S\cdot S^2\cdot BN^{m+1}\bigr)
&=O_{m,K}\bigl(B^5N^{4m+1}\bigr)\\
&=O_{m,K}\bigl(N^{5mK+4m+1}\bigr).
\end{aligned}
\tag{9.3}
$$

The other work fits this deliberately generous bound. Reachability is polynomial in $N$. Generating and evaluating $B$ bounded-size formulas, pairwise deduplication, ordering their bit vectors by cardinality, and enumerating compatible states require at most lower-degree polynomials in $B,N$. Acceptance data for smaller sets are already stored. Backtracking a reached path has at most $S$ records; its schedule contains only $N$ jobs because the pieces partition $W$, and sequential retrieval of their stored schedules likewise fits (9.3). These facts also show that no unit-cost random-access assumption is hidden in the bound. $\square$

### Corollary 9.3 (the bounds of Theorem 1.1)

With $K=12m+25$, (9.1) is $O_m(N^{60m^2+129m+1})$. For explicitly listed jobs $n\leq L$ and nontrivial deadlines $N=mT\leq mn\leq mL$. Trying at most $n$ deadlines, with input handling and witness output, fits (1.1).

**Proof.** Substitute:
$$
5m(12m+25)+4m+1=60m^2+129m+1.
$$
The factor $m^{60m^2+129m+1}$ is a constant for fixed $m$. The extra at most $L$ deadline trials could already be covered by exponent $60m^2+129m+2$ under the preceding accounting. The advertised exponent $60m^2+129m+8$ is a conservative larger integer exponent covering these operations and the input model conventions. The elementary branches $T<1$ and $T\geq n$ cost less. $\square$

For reference, the bounds actually used are:

| Fixed $m$ | List/carry union $6m+9$ | Global leaves $K_m=12m+25$ | Relative leaves $6m+16$ | Padded-deadline exponent | Advertised input exponent |
|---:|---:|---:|---:|---:|---:|
| 3 | 27 | 61 | 34 | 928 | 935 |
| 4 | 33 | 73 | 40 | 1477 | 1484 |
| 5 | 39 | 85 | 46 | 2146 | 2153 |
| 6 | 45 | 97 | 52 | 2935 | 2942 |
| $m$ | $6m+9$ | $12m+25$ | $6m+16$ | $60m^2+129m+1$ | $60m^2+129m+8$ |

The smaller three-machine constants compared with the supplied $257$-leaf estimate result from retaining the distinction between simple entries and the sole potentially complicated initial entry. They do not modify the underlying construction or its search transitions.

### Proposition 9.4 (the compact-isolated-jobs remark)

For fixed $m$, the decision version is also polynomial when the input gives the total number $n$ in binary and lists only the arcs, allowing many isolated jobs. This statement does not promise an explicitly listed output schedule of length polynomial in that compact encoding.

**Proof.** Reject when $n>mT$ or $T<1$ for $n>0$. Let $d$ be the number of jobs incident with at least one listed arc. If $T\geq d$, schedule those $d$ jobs one per slot in a topological order. The remaining positions number $mT-d\geq n-d$, enough for all isolated jobs, so accept. If $T<d$, then the padded size satisfies
$$
N=mT<md\leq2m|E|,
$$
since every arc has at most two endpoints. Thus the padded decision algorithm has polynomial size in the compact input for fixed $m$. Explicitly writing all $n$ scheduled jobs can of course take $\Omega(n)$ symbols; the decision assertion avoids that output-size issue. The empty instance is immediate. $\square$

### 9.1. Direct answers to the questions

**Q1.** Yes. Theorem 1.1 proves polynomial-time solvability for every fixed $m\geq3$. The logical construction transfers with “triple” replaced by “$m$-element antichain”, padding to $mT$, and the injection bound replaced by $m$. “Verbatim” must allow the derived numerical leaf bounds to be recomputed. The old per-entry constant is not a justified uniform bound for arbitrary $m$; Lemmas 6.2 and 6.5 give the needed replacement, and Lemma 8.4 proves a linear total leaf bound.

**Q2.** The complete proofs above verify the exchanges for sorted $m$-tuples, every walk step and shared cutoff, both center sides and edge labels, the switch pair and its globally valid upset, and the exterior (I2) and universally quantified (I3) invariants. The one-slot state in Section 2 remains sufficient; Proposition 2.8 and Lemma 2.10 prove this without a three-machine assumption. Section 10 lists every individual source lemma and its generalized proof.

**Q3.** The exact theorem and its effective dependence on $m$ are Theorem 1.1 and Proposition 9.2. There is no failed four-machine step to exhibit: the quantified structure theorem and algorithm correctness theorem both include $m=4$. In particular the conclusion concerns the actual description-enumerating algorithm, not merely an isolated lemma. A counterexample to that four-machine algorithm would contradict the proven equivalence in Theorem 9.1.

## 10. Lemma-by-lemma audit

The following tables are an index to **proved generalized statements**, not a replacement for their proofs. The proofs in Sections 2–9 give every hypothesis and every step of the transfer. “No capacity use” means that the proof applies to arbitrary slot cardinality once a full schedule is defined; capacity still occurs in the definition of a slot.

### 10.1. All numbered results in the eight lessons

| Supplied source and result | Generalized statement and proof here | Capacity audit |
|---|---|---|
| [L1] Lemma 1.1, paths versus arcs | Lemma 2.1(1–2) | Transitivity and strict inequalities only. |
| [L1] Lemma 1.2, linear extensions | Lemma 2.1(3) | Finite acyclicity only. |
| [L1] Lemma 1.3, integer times | Lemma 2.2 | Machine assignment has target $[m]$; augmented arcs give integer starts. |
| [L1] Lemma 2.1, padding | Lemma 2.3 | Exactly $mT-n$ isolated jobs and $N\leq mn$. |
| [L1] Lemma 2.2, interval replacement | Lemma 2.4 | Equal interval length $|W|/m$; exterior relations unchanged. |
| [L1] Theorem 3.1, scheduling theorem | Theorems 1.1 and 9.1; Corollary 9.3 | Proved for every fixed $m\geq3$, with an explicit exponent. |
| [L2] Lemma 1.1, cones and time | Lemma 2.5 | Antichain property, not the number of companions. |
| [L2] Lemma 2.1, complements | Lemma 2.6 | De Morgan transformation preserves leaves. |
| [L2] Lemma 2.2, finite family | Lemma 2.7 | $\binom Nm\leq N^m$ replaces $\binom N3$. |
| [L2] Proposition 3.1, soundness | Proposition 2.8 | One nonempty $m$-slot per state; compatibility checks all relations. |
| [L2] Lemma 4.2, hierarchy completeness | Lemma 2.10 | Actual marked slots form an accepting state path. |
| [L2] Theorem 4.3, structure | Theorem 8.5 | Global budget $K_m=12m+25$. |
| [L3] Lemma 1.2, separator prefix | Lemma 3.1 | The two separator conditions and weak-cone exclusion. |
| [L3] Lemma 1.3, reversal | Lemma 3.2 | Complement cutoff, reversed time and precedence. |
| [L3] Lemma 2.1, normalized exchange | Lemma 3.3 | Every sorted order statistic weakly decreases; one decreases strictly. |
| [L3] Lemma 3.1, one advance | Lemma 3.4 | Swapping two jobs and tracing increasing successor times. |
| [L3] Lemma 3.2, fixed cutoff | Lemma 3.5 | Strictly increasing finite sequence of positions. |
| [L3] Lemma 3.3, shared cutoff | Lemma 3.6 | Only the promoted job changes status; subsequent exceptions are old low jobs. |
| [L3] Corollary 3.4, existence | Corollary 3.7 | Priority-prefix promotions from a normalized schedule. |
| [L4] Lemma 1.1, keys | Lemma 4.1 | Global upsets and increasing rank. |
| [L4] Lemma 2.1, cover | Lemma 4.2 | (I1), complements and reversal. |
| [L4] Lemma 3.1, priorities | Lemma 4.3 | Downset blocks and key order. |
| [L4] Lemma 4.1, adjacent cutoffs | Lemma 4.4 | Shared walk plus center separator. |
| [L4] Lemma 4.2, edge labels | Lemma 4.5 | Genuine right boundary, low/high cone inclusions, strict shrinking. |
| [L5] Lemma 1.1, suffix carry | Lemma 5.1 | Three cases for the largest qualifying index, unrelated to capacity. |
| [L5] Lemma 1.2, pruning comparison | Lemma 5.2 | The smaller-key job must belong to the pruning domain. |
| [L5] Lemma 2.1, new qualifiers | Lemma 5.3 | Last injection index and ordered switch pair. |
| [L5] Lemma 3.1, entry shape | Lemma 5.4 | Suffix thresholds combine by their maximum. |
| [L5] Lemma 3.2, list length | Lemma 5.5 | Explicit injective function into a boundary with $m$ jobs. |
| [L6] Lemma 1.1, flattening | Lemma 6.1 | While the first entry survives, the second is untrimmed or locally absent. |
| [L6] Lemma 2.1, earlier low extension | Lemma 6.2 | $3m+3$ leaves; only equality on the earlier node is needed. |
| [L6] Lemma 3.1, arrangement | Lemma 6.3 | Reverse the old side inequalities. |
| [L6] Lemma 3.2, switch upset | Lemma 6.4 | Four upset factors; localize to the old node before using $H^*$. |
| [L6] Lemma 4.1, entry size | Lemma 6.5 | At most $3m+7$ leaves per entry; aggregate $6m+9$. |
| [L7] Lemma 2.1, distant qualifiers | Lemma 7.1 | First advance uses parent (I3); later advances use Lemma 3.4. |
| [L7] Lemma 3.1, universal exchanges | Lemma 7.2 | A child reordering changes only a suffix of normalized $E$. |
| [L7] Proposition 4.1, validity | Proposition 7.3 | Induction uses only node/ancestor data; no descendant assumption. |
| [L8] Lemma 2.1, global child | Lemma 8.2 | Exact global equalities (8.4)–(8.5), with no parent formula. |
| [L8] Lemma 3.1, mark prefixes | Lemma 8.3 | Relative separator descriptions and subtraction of the reversed slot. |
| [L8] Lemma 4.1, leaf count | Lemma 8.4 | Linear aggregate accounting: $12m+25$ and $6m+16$. |
| [L8] Proposition 5.1, running time | Proposition 9.2 and Corollary 9.3 | $B=C_{m,K}N^{mK}$, $S=BN^m$, sequential tape scans. |
| [L8] Remark 5.2, compact encoding | Proposition 9.4 | Decision only; bound $N<2m|E|$ when explicit expansion is needed. |

The two numbered source definitions are also restated: [L2] Definition 4.1 is Definition 2.9, and [L3] Definition 1.1 is the separator definition at the start of Section 3. The unnumbered cutoff predicates of [L8] Section 1 are proved as Lemma 8.1. Side normalization, root behavior, copying witnesses, cone/upset facts, and the order of construction are explicitly included in the corresponding sections above.

### 10.2. Every labelled theorem, lemma, proposition, corollary and remark in the preprint

Source labels refer to the attached TeX, so they identify the exact statements independently of PDF page numbering.

| File in the preprint's build directory | Exact source label | Proof here |
|---|---|---|
| paper.tex | thm:main | Theorems 1.1, 9.1 and Corollary 9.3 |
| paper.tex | lem:padding | Lemma 2.3 |
| paper.tex | lem:reorder | Lemma 2.4 |
| paper.tex | lem:family | Lemma 2.7 |
| paper.tex | prop:algorithm | Proposition 2.8; Proposition 9.2 and Corollary 9.3 |
| paper.tex | lem:hierarchy-dp | Lemma 2.10 |
| paper.tex | thm:structure | Theorem 8.5 |
| separators.tex | lem:separator-description | Lemmas 3.1–3.2 |
| separators.tex | lem:lex-prefix | Lemma 3.3 |
| separators.tex | lem:shared | Lemmas 3.4–3.6, including the internal one-advance argument |
| separators.tex | cor:any-ideal | Corollary 3.7 |
| construction.tex | lem:edge-labels | Lemmas 4.3–4.5, with the center and both sides defined in Section 4 |
| lists.tex | lem:carry | Lemma 5.1 |
| lists.tex | lem:prune | Lemma 5.2 |
| lists.tex | lem:update-labels | Lemma 5.3 |
| lists.tex | lem:list-length | Lemmas 5.4–5.5 |
| lists.tex | lem:flatten | Lemma 6.1 |
| lists.tex | lem:old-low | Lemma 6.2 |
| lists.tex | lem:G | Lemmas 6.3–6.4 |
| lists.tex | lem:entry-size | Lemma 6.5 |
| boundary.tex | lem:past | Lemma 7.1 |
| boundary.tex | lem:swap | Lemma 7.2 |
| boundary.tex | prop:construction-valid | Proposition 7.3 |
| descriptions.tex | lem:global-child | Lemmas 8.1–8.2 |
| descriptions.tex | lem:relative-splits | Lemma 8.3 |
| descriptions.tex | lem:final-count | Lemma 8.4 |
| paper.tex | rem:compact | Proposition 9.4 |

The unnumbered proof in preprint Section 9 is generalized in Proposition 9.2. Its definitions “def:hierarchy” and “def:separator” are covered as above. The conclusion and figure files state no additional lemma requiring another hypothesis. The original lexicographic exchange proof's reference to the smallest, middle and largest elements is replaced in Lemma 3.3 by a proof for all $m$ order statistics; this is a genuine checked generalization, not a silent replacement of notation.

## 11. Reproducible finite verification and artifact inventory

The theorem is proved for all finite instances by the preceding lemmas. The following finite computations are included as an independent check of the most exchange-sensitive part of the construction.

### 11.1. Exact coverage of the checker

The file *code/check_walk.py* uses only Python's standard library. It computes normalized schedules by subset recursion, enumerating every possible minimal-job first block in lexicographic priority order until it finds a feasible continuation. This exact routine uses no separator theorem.

It tests:

1. Every one of the $2^{16}=65{,}536$ distinct labelled two-layer posets on fixed layers $\{0,1,2,3\}$ and $\{4,5,6,7\}$, with any subset of the sixteen forward relations and no other relations, on four machines. Each case uses a graph-dependent topological priority obtained by choosing the first available job in the fixed template $(0,4,1,5,2,6,3,7)$.
2. Thirty-six deterministic three-layer input/priority cases at each of $m=4$ and $m=5$, using the pseudorandom seed $20261023$ and the densities specified in the code. These seventy-two cases are not an exhaustive enumeration of three-layer posets, and some repeat a poset with a different priority.
3. One explicitly constructed three-slot instance at each of $m=4,5$ for which a single promotion can require two advances. The code gives every arc and priority choice.

For each case, the program checks all consecutive priority-prefix pairs, all separating starting positions, and all contiguous interval domains of the exactly normalized schedule. Exterior starting positions use the successor cone $D$ of the actual preceding boundary, or the virtual convention at the beginning. It verifies that the earliest-exception walk ends at a separator for both prefixes. For every slot it also enumerates every full rescheduling of the suffix, retains the prefix, and tests every exchange with a better-priority later job for feasibility in the entire schedule. None is feasible.

Thus the enumerations verify all premises and conclusions for precisely this finite collection. They do not purport to run the enormous formula-enumerating algorithm or to exhaust all four-machine precedence instances.

### 11.2. Reported output

The unedited machine-readable output is *checks/check_walk_output.json*.

| Case collection | Input/priority cases | Shared-cutoff premises | Better-priority exchange candidates | Actual advances |
|---|---:|---:|---:|---:|
| All fixed-layer $4+4$ posets, $m=4$ | 65,536 | 2,495,601 | 132,816 | 29,822 |
| Deterministic three-layer cases, $m=4$ | 36 | 3,124 | 667 | 180 |
| Deterministic three-layer cases, $m=5$ | 36 | 4,177 | 471 | 142 |
| Forced multiple-advance case, $m=4$ | 1 | 73 | 4 | 9 |
| Forced multiple-advance case, $m=5$ | 1 | 89 | 5 | 9 |
| **Total** | **65,610** | **2,503,064** | **133,963** | **30,162** |

The output reports **zero violations** and “All asserted checks passed.” Shared-cutoff premises include walks with no advance. Suffix enumerations include identity and empty suffixes. Four checked walks have two advances; the others with advances have one.

To reproduce from the extracted artifact directory, run Python on *code/check_walk.py* and redirect standard output to a JSON file. The file's module documentation gives the exact command. A separate script, *code/validate_artifacts.py*, verifies all 21 source-file sizes and SHA-256 hashes against the supplied manifest, checks that the audit tables cover every numbered lesson result and every labelled preprint result, validates the reported totals and numerical exponent identities, and writes *checks/validation_output.json*.

### 11.3. Contents of the archive

*Q03-artifacts.zip* contains:

- this complete mathematical source, *Q03-solution.md*;
- all verification code and its reported output;
- the independent audit notes and precise literature search record;
- the supplied source archive, its manifest, and the input task text;
- a file manifest with sizes and SHA-256 hashes.

No PDF is needed for the proof; the requested machine-readable Markdown contains the complete solution. The proof does not depend on running these programs or on a Lean build.

## References

**[P]** OpenAI. *A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling*. OpenAI Math Release preprint, 24 September 2026. Main statement: Theorem 1.1; finite search: Proposition 3.1; hierarchy criterion: Lemma 3.3; structure: Theorem 3.4; structural proofs: Sections 4–8; running time: Section 9. Freely accessible [repository directory](https://github.com/openai/math/tree/main/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026) and [PDF](https://github.com/openai/math/blob/main/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/paper.pdf). The audited version is the attached source, whose exact hashes are in the supplied *SOURCES.txt*. Its main source *papers/openai-scheduling/build/paper.tex* has SHA-256 *38f8318c45e578108367b3e35d87575ff0c1c56fb203d68a2d3b24b193eb6e2d*. All individual theorem labels are listed in Section 10.2.

**[F]** OpenAI Math Release. *Polynomial-time scheduling on three identical machines*, formalization scope file *lean/docs/124.md*, “Scope” and “Comparator links”, accessed 23 October 2026. Freely accessible [scope document](https://github.com/openai/math/blob/main/lean/docs/124.md). This document is cited for what the formalization claims, not as a substitute for the proofs here.

**[D]** drbh. *scheduling-proof-exploration*. 2026. README, “what this repo is”, “upstream and building”, and “could this work for other machine counts?”; CHANGELOG, entry “bbd3013 — Adapt scheduling proof from three to four machines”. Freely accessible [repository and README](https://github.com/drbh/scheduling-proof-exploration) and [CHANGELOG](https://github.com/drbh/scheduling-proof-exploration/blob/main/CHANGELOG.md), accessed 23 October 2026. An exploratory four-machine adaptation, not a premise of Theorem 1.1.

**[N]** Jesper Nederlof, Céline M. F. Swennenhuis and Karol Węgrzycki. *A Subexponential Time Algorithm for Makespan Scheduling of Unit Jobs with Precedence Constraints*. arXiv:2312.03495v1, 6 December 2023. Exact locators in this version: Theorem 1.1; Definition 3.1 and Theorem 3.2. Freely accessible [arXiv HTML](https://arxiv.org/html/2312.03495v1) and [arXiv record](https://arxiv.org/abs/2312.03495). Published in *Proceedings of the 2025 Annual ACM-SIAM Symposium on Discrete Algorithms*, pp. 535–552; [DOI 10.1137/1.9781611978322.16](https://doi.org/10.1137/1.9781611978322.16).

**[A]** Syamantak Das and Andreas Wiese. *A Simpler QPTAS for Scheduling Jobs with Precedence Constraints*. ESA 2022; arXiv:2501.09091v1, 15 January 2025, Theorem 1. Freely accessible [arXiv HTML](https://arxiv.org/html/2501.09091v1) and [arXiv record](https://arxiv.org/abs/2501.09091). Cited only for the approximation background and the distinction from exact feasibility.

**[L1]–[L8]** Open Mathematics Courses, *Scheduling unit jobs on three machines*. The attached lessons identify their author as Claude Opus 5.5 (Anthropic), October 2026, and their license as CC0 1.0. The exact audited copies are supplied in *SOURCES(4).zip* under *lessons/three-machine-unit-job-scheduling/*. Their identifiers and filenames are:

| Reference | Filename |
|---|---|
| [L1] | unit-jobs-on-three-machines.md |
| [L2] | descriptions-and-a-dynamic-program.md |
| [L3] | separators-and-the-shared-cutoff-walk.md |
| [L4] | centers-sides-and-edge-cutoffs.md |
| [L5] | carried-and-pruned-lists.md |
| [L6] | changing-direction.md |
| [L7] | boundary-invariants.md |
| [L8] | global-descriptions-and-the-running-time.md |

The archive's supplied manifest gives the byte size, SHA-256, origin and license of each lesson and preprint file. Sections 10.1–10.2 supply exact internal locators; no unavailable course URL is assumed.

## Further consequences

**Proved consequence: approximation for the same model.** For each fixed $m$, the exact algorithm is also a polynomial-time $(1+\varepsilon)$-approximation for every $\varepsilon>0$: its returned makespan equals the optimum and therefore is at most $(1+\varepsilon)$ times the optimum. Its exponent is independent of $\varepsilon$, although its large magnitude gives no practical speed comparison with the approximation schemes.

**Idea: reduce the exponent.** The state graph has strictly increasing left-part cardinality along transitions. One can investigate replacing the repeated-pass reachability implementation and the enumeration of all Boolean trees by more economical searches over the structured formulas actually produced by the proof. No faster exponent is claimed here.

**Idea: time windows.** Release dates and individual deadlines would require a new interval-replacement and exchange analysis. A replacement schedule feasible for precedence alone can move a job outside its allowed time window, so Lemmas 2.4 and 3.3 do not by themselves establish such an extension. For example, take eight independent jobs on four machines, with one designated job released at slot 2 and all others at slot 1. A full two-slot schedule with that job in the second slot respects the releases; swapping it with any first-slot job preserves every precedence constraint but violates its release. An appropriate description family might need explicit time-window information.

**Idea: unequal machine speeds.** For $Q\mid\mathrm{prec},p_j=1\mid C_{\max}$, equal job requirements on machines of different speeds do not give common unit-duration slots. For example, four independent unit-work jobs finish by time 1 on machines of speeds $(1,1,2)$: one runs on each slow machine and two run consecutively on the fast one. A three-job-per-unit-slot capacity test would reject that deadline. The full-slot padding and two-job exchange model would need a new replacement argument. The present theorem makes no claim for that variant.
