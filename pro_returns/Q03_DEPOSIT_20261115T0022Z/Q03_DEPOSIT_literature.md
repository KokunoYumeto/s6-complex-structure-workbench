# Q03 literature search

**Date:** 15 November 2026, Europe/Berlin. **Researcher:** GPT-6 Astra (OpenAI), effort ChatGPT Pro mode. The task date is the local Berlin date; the clock was 14 November in UTC during part of this session.

## Result that controls novelty language

The search found an existing public all-fixed-machine exact-algorithm statement: Klaus Jansen, [arXiv:2611.09392v1](https://arxiv.org/abs/2611.09392v1), dated 6 November 2026. Theorem 1.1 and the linear leaf budgets in Lemma 7.15 were opened and compared. The precise machine models, exponents and budgets are recorded once in `Q03_DEPOSIT_sources.md`, S-J. That source was checked for its statements, not independently certified by a complete proof audit.

The exact drbh commit already contains a complete four-machine release-theorem adaptation; its scope is S-D. [David Niedbala Giraudin’s Hexagon 2611.00060v1](https://hexagonmath.org/pdf/2611.00060v1) supplies a separate three-machine exponent refinement (S-G). The public course’s lessons 9–11 explicitly derive from Q03; they are recorded as derivative material, not independent verification.

The revised post should say what this Q03 manuscript proves and how its construction/accounting is derived. It must remove “new here for m≥4” and unqualified novelty for linear leaf budgets. A different displayed numeric budget is not by itself a novelty or priority proof. No priority is claimed. New authors found in the search are cited as prior literature; they are not credited as producers of Q03.

The searches below did not locate a source establishing hardness for any one fixed m≥4 in the exact explicit-job/unit-length/arbitrary-acyclic-precedence model. This records a finite search result, not a universal theorem of nonexistence. In particular, Ullman’s unit-job reduction has variable processor count. Approximation and exact scheduling are related by the integral-optimum argument in S-A; the approximation bound under that substitution does not establish polynomial time.

## Search method and limits

The search covered arXiv, general web, STOC, FOCS, SODA, ICALP, IPCO, ESA, APPROX, author publication pages, Hexagon, the exact OpenAI title, source-name combinations and linear-leaf terminology. Both exposed search engines were used; weak venue coverage was checked with the stronger engine. Recency90days was used on current-result/citation queries where recorded below. Existing primary papers and official metadata were opened to compare the actual model and statement. Search snippets alone were used to identify leads, not to certify a theorem.

“Everything that cites the OpenAI preprint” was approached through exact-title, author/source-name, repository, course and revised-preprint searches. Search indexing is incomplete, and no complete forward-citation database for this GitHub preprint was obtained. The resulting known citing/derived items are listed below. The record does not assert an exhaustive census of every published or unindexed citation. The full focused query set and returned-source headings are retained to make that limitation reviewable.

The initial four search batches were transcribed from the session record; their selected relevant result URLs are listed. Subsequent batches preserve every returned title/URL heading from the saved tool output. Results within a batch were returned merged, so no unsupported one-to-one query/result attribution is invented. Direct source opens, failed opens and recovery methods are also recorded in the source report.

## Coverage and opened leads

| Requested direction | Queries/batches | Opened result used |
|---|---|---|
| Exact polynomial for every fixed m≥4 | early 1–2; arXiv and fixed-machine batches | Jansen v1, Theorem 1.1; primary arXiv PDF |
| Exact polynomial for m=4 | drbh/title and fixed-four queries | Exact drbh bbd3013 source release theorem |
| Hardness for fixed m≥4 | lit_venues_0, lit_venues_3, lit_fixed | No matching claim found; Ullman parameter scope checked directly |
| Linear leaf structure | 12m/25, leaf/description and final linear-leaf queries | Jansen Lemma 7.15; OpenAI constant-budget construction; Q03 derivative lessons |
| STOC | lit_venues_1 and lit_venues_3 | Levey–Rothvoss approximation paper, official journal record |
| FOCS | lit_venues_1 and lit_venues_3 | Official FOCS 2020 list; returned communication-delay paper treated only as a lead |
| SODA | early 4 and lit_venues_1 | Nederlof–Swennenhuis–Węgrzycki 2025, official proceedings and full text |
| ICALP | lit_venues_1 | Garg 2018, official DROPS record |
| IPCO | lit_venues_2 and lit_venues_3 | Returned single-machine/other-objective leads; no exact target-model theorem established |
| ESA | early 4 and lit_venues_2 | Das–Wiese 2022, official full proceedings paper |
| APPROX | lit_venues_2 | Returned flow-time and other scheduling leads; no exact target-model theorem established |
| Authors’ pages | lit_fixed, lit_citations | Nederlof publication page; MPI publications; Kiel query yielded no useful target |
| Hexagon | early1, lit_venues_0, lit_final | Giraudin 2611.00060v1, full PDF |
| OpenAI citing/derived work | exact-title/source-name batches | Jansen, Giraudin, drbh adaptation, course, mathcommunity revision activity |

## Known citing or derived items encountered

| Item | Evidence and role |
|---|---|
| drbh adaptation | Exact pinned repository is explicitly derived from OpenAI scheduling files; full m=4 release scope, S-D. |
| Course lessons 1–11 | Course source metadata and lesson bylines; chapters 9–11 identify Q03 as their basis, S-L. |
| Jansen | Opening relation-to-OpenAI discussion and references in the opened PDF; exact all-fixed-m statement, S-J. |
| Giraudin | OpenAI structure is invoked in the opened three-page paper; three-machine exponent refinement, S-G. |
| mathcommunity revised-preprint activity | [Activity log](https://mathcommunity.github.io/oai-math-revised/activity/), 27 October 2026 entry: bibliography and cross-reference maintenance. It is a separate community revision; the byte comparison in S-P uses the official OpenAI repository. |
| AI Proved What episode | [Opened episode](https://aiprovedwhat.com/episodes/124-three-machine-scheduling/), directly citing OpenAI; its old episode URL redirects here. Logged as exposition, not as verification of mathematical claims. |
| Plectis Atlas | [Opened statement page](https://wcook04.github.io/plectis-atlas/statements/ThreeMachine.html), linking the OpenAI theorem and comparator. Logged as a source index, not as an independent theorem proof. |

## Every query and what it found

All following batches were run on 15 November 2026 Europe/Berlin. Query spelling, including exploratory terms or guessed page ranges, is preserved; a query is not a factual assertion. The complete metadata counterpart is `code/C_search_history_complete.json`.


### Batch 1: early_1

Engine: `system1`. Initial-batch queries and selected returned sources recorded from the session transcript; merged search output does not identify which query returned each source.

Queries:

- `"A polynomial-time algorithm for three-machine unit-job scheduling" OpenAI`
- `"scheduling-proof-exploration" drbh`
- `"unit jobs" "four machines" polynomial 2026`

**Outcome:** Located the supplied preprint/repository and the later all-fixed-machine and three-machine refinement papers. Their actual statements were subsequently opened.

Returned source headings/URLs:

- [OpenAI scheduling preprint](https://github.com/openai/math/tree/main/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026)
- [drbh repository](https://github.com/drbh/scheduling-proof-exploration)
- [Jansen full-text mirror](https://borowiecki.dev/pdf/2611.09392)
- [Giraudin three-machine refinement](https://hexagonmath.org/pdf/2611.00060v1)

### Batch 2: early_2

Engine: `system1`. Initial-batch queries and selected returned sources recorded from the session transcript; merged search output does not identify which query returned each source.

Queries:

- `"2611.09392" Jansen`
- `"Precedence Constraint Scheduling on a Fixed Number of Machines"`
- `"scheduling-proof-exploration" "bbd3013"`

**Outcome:** Verified official arXiv author/title/submission identity. The exact drbh commit was not usefully indexed; the GitHub API and exact archive were then used.

Returned source headings/URLs:

- [Jansen arXiv metadata](https://arxiv.org/abs/2611.09392)
- [Jansen full-text mirror](https://borowiecki.dev/pdf/2611.09392)

### Batch 3: early_3

Engine: `system2`. Initial-batch queries and selected returned sources recorded from the session transcript; merged search output does not identify which query returned each source.

Queries:

- `"Optimal sequencing of two equivalent processors" Fujii Kasami Ninomiya 1969 erratum`
- `"Optimal scheduling for two-processor systems" 1972 Coffman Graham pdf`
- `"NP-complete scheduling problems" Ullman 1975 pdf`
- `"Garey" "Johnson" "OPEN8" "PREC" 1979`

**Outcome:** Found original-paper/book scans and the omitted FKN erratum. Original FKN full text remained behind the access page; all other listed scans were retrieved.

Returned source headings/URLs:

- [FKN original publisher entry](https://epubs.siam.org/doi/10.1137/0117070)
- [FKN erratum publisher entry](https://epubs.siam.org/doi/10.1137/0120018)
- [Coffman–Graham author-hosted scan](https://fanchung.ucsd.edu/ron/papers/72_04_two_processors.pdf)
- [Ullman original scan](https://www.cs.montana.edu/bhz/classes/fall-2021/csci460/paper4.pdf)
- [Garey–Johnson book scan](https://perso.limos.fr/~palafour/PAPERS/PDF/Garey-Johnson79.pdf)

### Batch 4: early_4

Engine: `system1`. Initial-batch queries and selected returned sources recorded from the session transcript; merged search output does not identify which query returned each source.

Queries:

- `"A simpler QPTAS" ESA 2022 40:1 40:15`
- `"A subexponential" "Nederlof" "535" "552" SODA 2025`

**Outcome:** Checked original proceedings metadata: ESA article 40 has eleven pages (40:1–40:11), and SODA pages 535–552. The page-range query was a search hypothesis, not a bibliographic assertion.

Returned source headings/URLs:

- [Das–Wiese official ESA proceedings record](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2022.40)
- [Nederlof–Swennenhuis–Węgrzycki official SODA record](https://epubs.siam.org/doi/10.1137/1.9781611978322.16)

### Batch 5: literature_batch_1

Engine: `system1`. Results were returned as a merged batch. No per-query attribution is inferred.

Queries:

- `"unit jobs" "fixed number" machines polynomial scheduling 2026` (recency: 90 days)
- `"precedence" "four machines" polynomial scheduling` (recency: 90 days)
- `"A polynomial-time algorithm for three-machine unit-job scheduling" -site:github.com/openai -site:sites.pitt.edu -site:proofweave.org -site:wcook04.github.io` (recency: 90 days)
- `"scheduling" "12m" "25" machines` (recency: 90 days)

**Outcome:** Returned OpenAI, its scope file, the course, indexes and historical open-question material. No additional exact theorem beyond the sources later identified. The literal 12m/25 query did not establish an earlier publication of that exact Q03 constant.

Returned source headings/URLs:

- [A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling](https://github.com/openai/math/tree/main/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026)
- [math/lean/docs/124.md at main · openai/math · GitHub](https://github.com/openai/math/blob/main/lean/docs/124.md)
- [Optimal three-machine unit-job scheduling (Lean) | Plectis Atlas](https://wcook04.github.io/plectis-atlas/statements/ThreeMachine.html)
- [Proceedings of the 2025 Annual ACM-SIAM Symposium on Discrete Algorithms (SODA) | SIAM Publications Library](https://epubs.siam.org/doi/book/10.1137/1.9781611978322)
- [A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling · oai-math-revised](https://mathcommunity.github.io/oai-math-revised/papers/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/)
- [Open Mathematics Courses](https://kokunoyumeto.github.io/open-math-courses-public/)
- [Unit-job scheduling on three identical machines](https://lowrank.github.io/latent-seminar/OpenAI-Math/124-three-machine-scheduling)
- [Unit jobs on three machines can be scheduled in polynomial time — Math singularity](https://math.coolsoftwaretools.org/proofs/124/)
- [List of open questions](https://a3nm.net/work/research/questions/)
- [Polynomial-time scheduling on three identical machines — Open Math Atlas](https://open-math-atlas.com/famille/124-polynomial-time-scheduling-on-three-identical-machines)
- [Proofweave](https://proofweave.org/publications/openai-math/124)
- [All papers — OpenAI Math index](https://kisonecat.github.io/openai-math/all.html)
- [math/overview.tex at main · openai/math · GitHub](https://cdn.hddj.top/openai/math/blob/main/overview.tex)

### Batch 6: lit_venues_0

Engine: `system2`. Results were returned as a merged batch. No per-query attribution is inferred.

Queries:

- `site:arxiv.org "scheduling" "fixed" "machines" "polynomial" "2026"`
- `"unit jobs" "four machines" "NP-hard"`
- `"unit jobs" "fixed" "leaf" "description"`
- `site:hexagonmath.org scheduling machines`

**Outcome:** Official arXiv metadata identified Jansen arXiv:2611.09392. Hexagon search identified Giraudin 2611.00060v1. Other results concerned differing processing assumptions or objectives; only statements opened and compared were used for the conclusion.

Returned source headings/URLs:

- [Precedence Constraint Scheduling on a Fixed Number of Machines](https://arxiv.org/abs/2611.09392)
- [Scheduling with Mandatory Breaks: NP-Hardness and an Additive-One Approximation](https://arxiv.org/abs/2609.34254)
- [Approximation algorithms for identical parallel machine scheduling with assignment costs](https://arxiv.org/abs/2610.33666)
- [Similar Papers for Cross-Shift Analysis for Unrelated-Machine Weighted Completion Time A (1.3168+epsilon)-Approximation | Arxiv - DeepPaper](https://arxiv.deeppaper.ai/papers/2608.15496v1/similar)
- [A minimum witness for the 3/2 configuration-linear-program gap in two-weight graph balancing, unique at its size](https://www.researchgate.net/publication/412249235_A_minimum_witness_for_the_32_configuration-linear-program_gap_in_two-weight_graph_balancing_unique_at_its_size)
- [From Estimates to Schedules: Learning-Augmented Restricted Assignment](https://arxiv.org/abs/2606.08377)
- [Open shop scheduling games](https://www.academia.edu/128616483/Open_shop_scheduling_games?force_claim_to_highlight=true)
- [Four decades of research on the open-shop scheduling problem to minimize the makespan](https://www.researchgate.net/publication/350365917_Four_decades_of_research_on_the_open-shop_scheduling_problem_to_minimize_the_makespan)
- [Constructing an instance of the cutting stock problem of minimum size which does not possess the integer round-up property](https://www.researchgate.net/publication/340932245_Constructing_an_instance_of_the_cutting_stock_problem_of_minimum_size_which_does_not_possess_the_integer_round-up_property)
- [Minimizing the makespan in open-shop scheduling problems with a convex resource consumption function](https://www.academia.edu/102086845/Minimizing_the_makespan_in_open_shop_scheduling_problems_with_a_convex_resource_consumption_function)
- [Advanced search · Hexagon](https://hexagonmath.org/search?advanced=1&msc=68Q25)
- [Graph-Based Modeling in Shop Scheduling Problems: Review and Extensions](https://www.mdpi.com/2076-3417/11/11/4741)
- [Dfhack | PDF | Command Line Interface | Linux Distribution](https://de.scribd.com/document/475462775/dfhack)
- [RSS feeds · Hexagon](https://hexagonmath.org/feeds)
- [Preemptive Online Scheduling: Optimal Algorithms for All Speeds](https://www.researchgate.net/publication/225837914_Preemptive_Online_Scheduling_Optimal_Algorithms_for_All_Speeds)
- [All works · Hexagon](https://hexagonmath.org/search?cursor=eyJ2IjoxLCJzb3J0RGF0ZSI6IjIwMjYtMTEtMDZUMTg6MTI6MjQuNzQ1WiIsImlkZW50aWZpZXIiOiIyNjExLjAwMTU3In0&direction=next&page=2&per_page=100)
- [Graph-Based Modeling in Shop Scheduling Problems: Review and Extensions](https://www.researchgate.net/publication/351790337_Graph-Based_Modeling_in_Shop_Scheduling_Problems_Review_and_Extensions)
- [Abstract of Doctoral Thesis Combinatorial algorithms for online](https://paperzz.com/doc/7802637/abstract-of-doctoral-thesis-combinatorial-algorithms-for-...)
- [Three-machine unit-job scheduling in time O((L+2)^276) — Valency Hub™](https://hub.valency.io/works/W_85n9vepa)
- [# THREE-MACHINE UNIT-JOB SCHEDULING IN TIME \(O((L+2)^{276})\)](https://hexagonmath.org/pdf/2611.00060v1)
- [A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling | Plectis Atlas](https://wcook04.github.io/plectis-atlas/papers/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026.html)
- [Advanced search · Hexagon](https://hexagonmath.org/search?advanced=1&msc=11Y16)
- [Graph Modeling of Shop Schedulings | Encyclopedia MDPI](https://encyclopedia.pub/entry/history/show/23696)
- [# Upper bounds for the Chvátal–Sankoff constants \(\gamma_k\), \(k \geq 3\)](https://hexagonmath.org/pdf/2610.00709v1)
- [Graph Modeling of Shop Schedulings | Encyclopedia MDPI](https://encyclopedia.pub/entry/10017)

### Batch 7: lit_venues_1

Engine: `system2`. Results were returned as a merged batch. No per-query attribution is inferred.

Queries:

- `site:dl.acm.org STOC "unit" "precedence" scheduling`
- `site:ieeexplore.ieee.org FOCS "unit" "precedence" scheduling`
- `site:epubs.siam.org SODA "unit jobs" scheduling`
- `site:drops.dagstuhl.de ICALP "scheduling" "precedences"`

**Outcome:** SODA 2025 returned the cited exact subexponential algorithm; ICALP 2018 returned Garg’s approximation scheme. STOC/FOCS domain coverage was sparse and was supplemented by system1 in lit_venues_3.

Returned source headings/URLs:

- [Proceedings of the 2025 Annual ACM-SIAM Symposium on Discrete Algorithms (SODA) | SIAM Publications Library](https://epubs.siam.org/doi/book/10.1137/1.9781611978322)
- [Proceedings of the 2025 Annual ACM-SIAM Symposium on Discrete Algorithms (SODA) | A Subexponential Time Algorithm for Makespan Scheduling of Unit Jobs with Precedence Constraints](https://epubs.siam.org/doi/abs/10.1137/1.9781611978322.16)
- [Quasi-PTAS for Scheduling with Precedences](https://drops.dagstuhl.de/storage/00lipics/lipics-vol107-icalp2018/LIPIcs.ICALP.2018.59/LIPIcs.ICALP.2018.59.pdf)
- [Quasi-PTAS for Scheduling with Precedences using LP Hierarchies](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2018.59)
- [Proceedings of the 2025 Annual ACM-SIAM Symposium on Discrete Algorithms (SODA): Front Matter](https://epubs.siam.org/doi/pdf/10.1137/1.9781611978322.fm?download=true)
- [Non-Clairvoyant Precedence Constrained Scheduling](https://drops.dagstuhl.de/storage/00lipics/lipics-vol132-icalp2019/LIPIcs.ICALP.2019.63/LIPIcs.ICALP.2019.63.pdf)
- [Nearly-Linear Time LP Solvers and Rounding Algorithms for Scheduling Problems](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2023.86)
- [45th International Colloquium on Automata, Languages, and Programming (ICALP 2018)](https://drops.dagstuhl.de/entities/volume/LIPIcs-volume-107)
- [Learning Precedences for Scheduling Problems with Graph Neural Networks](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CP.2024.30)
- [A Simpler QPTAS for Scheduling Jobs with Precedence Constraints](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2022.40)
- [30th International Conference on Principles and Practice of Constraint Programming (CP 2024)](https://drops.dagstuhl.de/entities/volume/LIPIcs-volume-307)
- [Understanding the Impact of Value Selection Heuristics in Scheduling Problems](https://drops.dagstuhl.de/storage/00lipics/lipics-vol340-cp2025/html/LIPIcs.CP.2025.27/LIPIcs.CP.2025.27.html)
- [Multi-Objective Multi-Drone Collaborative Routing Problem With Heterogeneous Delivery and Pickup Service | IEEE Journals & Magazine | IEEE Xplore](https://ieeexplore.ieee.org/document/10937313/)
- [An Efficient Constraint Programming Approach to Preemptive Job Shop Scheduling](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CP.2023.19)
- [Understanding the Impact of Value Selection Heuristics in Scheduling Problems](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CP.2025.27)
- [An Improved Approximation Algorithm for Scheduling Under Arborescence Precedence Constraints](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2020.84)
- [$\text{D}^{\textit{over}}$: An Optimal On-Line Scheduling Algorithm for Overloaded Uniprocessor Real-Time Systems](https://epubs.siam.org/doi/abs/10.1137/S0097539792236882?mobileUi=0)
- [System Level LET: Mastering Cause-Effect Chains in Distributed Systems | IEEE Conference Publication | IEEE Xplore](https://ieeexplore.ieee.org/abstract/document/8591550)
- [Scheduling Graphs on Two Processors](https://epubs.siam.org/doi/10.1137/0205005)
- [Single Machine Scheduling with Release Dates](https://epubs.siam.org/doi/abs/10.1137/S089548019936223X?download=true&journalCode=sjdmec)
- [Technical and Organizational Facilitating Conditions — The Antecedent Factors and Impact on the Intention to Use ERP System in Libyan Universities | IEEE Conference Publication | IEEE Xplore](https://ieeexplore.ieee.org/abstract/document/9377305/)
- [eGRAP: Graph-Based Adaptive Planning for Dual-arm Robotic Disassembly of Electronic Devices | IEEE Conference Publication | IEEE Xplore](https://ieeexplore.ieee.org/abstract/document/11658063/similar)

### Batch 8: lit_venues_2

Engine: `system2`. Results were returned as a merged batch. No per-query attribution is inferred.

Queries:

- `IPCO "unit jobs" "precedence" scheduling`
- `site:drops.dagstuhl.de ESA "unit" "precedence" scheduling`
- `site:drops.dagstuhl.de APPROX "unit" "precedence" scheduling`
- `"Klaus Jansen" "Precedence Constraint Scheduling"`

**Outcome:** ESA returned Das–Wiese 2022. APPROX returned related flow-time/other scheduling objectives. IPCO results concerned other objective/model settings; none of the returned titles supplied an exact arbitrary-precedence fixed-m≥4 polynomial theorem or a fixed-m hardness theorem. Jansen’s exact title was independently returned.

Returned source headings/URLs:

- [Precedence Constraint Scheduling on a Fixed Number of Machines](https://arxiv.org/abs/2611.09392)
- [Precedence Constraint Scheduling on a Fixed Number of Machines](https://borowiecki.dev/abs/2611.09392)
- [A Subexponential Time Algorithm for Makespan Scheduling of Unit Jobs with Precedence Constraints](https://doi.org/10.1145/3785365)
- [Quasi-PTAS for Scheduling with Precedences](https://drops.dagstuhl.de/storage/00lipics/lipics-vol107-icalp2018/LIPIcs.ICALP.2018.59/LIPIcs.ICALP.2018.59.pdf)
- [Flow-time Optimization for Concurrent](https://drops.dagstuhl.de/opus/volltexte/2018/9420/pdf/LIPIcs-APPROX-RANDOM-2018-16.pdf)
- [Precedence Constraint Scheduling on a Fixed Number of Machines](https://accelresearching.com/accel-zinc-picolinate-50mg/?_=%2Fpdf%2F2611.09392%23nLw79nwZb1b3uPkZUsgpm5M%3D)
- [Open-shop scheduling for unit jobs under precedence constraints](https://www.sciencedirect.com/science/article/pii/S0304397519306164)
- [Top arXiv papers](https://scirate.com/?date=2026-12-10&page=121&range=56)
- [A note on on-line scheduling with precedence constraints on identical machines](https://www.sciencedirect.com/science/article/pii/S0020019000001411)
- [Search | arXiv e-print repository](https://www.tempodimare.com/?_=%2Fsearch%2F%23nIKhFiPUZajrdh0GkGynKZM%3D&query=Jansen%2C+K&searchtype=author)
- [Proceedings of the 2025 Annual ACM-SIAM Symposium on Discrete Algorithms (SODA) | A Subexponential Time Algorithm for Makespan Scheduling of Unit Jobs with Precedence Constraints](https://epubs.siam.org/doi/10.1137/1.9781611978322.16)
- [Scheduling Under Non-Uniform Job and Machine Delays](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2023.98)
- [Approximation, Randomization,](https://drops.dagstuhl.de/storage/00lipics/lipics-vol317-approx-random2024/LIPIcs.APPROX-RANDOM.2024/LIPIcs.APPROX-RANDOM.2024.pdf)
- [A Subexponential Time Algorithm for Makespan Scheduling of Unit Jobs with Precedence Constraints](https://research-portal.uu.nl/ws/portalfiles/portal/254249631/1.9781611978322.16.pdf)
- [A Subexponential Time Algorithm for Makespan Scheduling of Unit Jobs with Precedence Constraints](https://research-portal.uu.nl/en/publications/a-subexponential-time-algorithm-for-makespan-scheduling-of-unit-j/)
- [A Simpler QPTAS for Scheduling Jobs with Precedence Constraints](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2022.40)
- [130  Scheduling of Precedence Constrained Unit Jobs in \(O(1.995^n)\) Time](https://pure.tue.nl/ws/files/228924206/20221202_Swennenhuis_hf.pdf)
- [Karol Wegrzycki — papers and venues](https://cs-conference-ranking.org/author/karol-wegrzycki)
- [A Subexponential Time Algorithm for Makespan Scheduling of Unit Jobs with Precedence Constraints](https://research.tue.nl/en/publications/a-subexponential-time-algorithm-for-makespan-scheduling-of-unit-j/)
- [Search | arXiv e-print repository](https://accelresearching.com/accel-zinc-picolinate-50mg/?_=%2Fsearch%2F%23nLw79nwZb1b3uPkZUsgpm5M%3D&query=Jansen%2C+K&searchtype=author)
- [Quasi-PTAS for Scheduling with Precedences using LP Hierarchies](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2018.59)
- [A Subexponential Time Algorithm for Makespan Scheduling of Unit Jobs with Precedence Constraints](https://research.tue.nl/nl/publications/a-subexponential-time-algorithm-for-makespan-scheduling-of-unit-j/)
- [30th Annual European Symposium on Algorithms (ESA 2022)](https://drops.dagstuhl.de/entities/volume/LIPIcs-volume-244)
- [Parameterized Complexity of Scheduling Unit-Time Jobs with Generalized Precedence Constraints](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.IPEC.2025.7)
- [Andreas S. Schulz — papers and venues](https://cs-conference-ranking.org/author/andreas-s-schulz)
- [Note on on-line scheduling with precedence constraints on identical machines](https://cris.haifa.ac.il/en/publications/note-on-on-line-scheduling-with-precedence-constraints-on-identic/)
- [A note on on-line scheduling with precedence constraints on identical machines](https://www.sciencedirect.com/science/article/pii/S0020019000001411/pdf?md5=94749f4ffb11c8d837edd04e334e2b57&pid=1-s2.0-S0020019000001411-main.pdf)
- [dblp: Andreas S. Schulz](https://dblp.org/pid/66/5251.html)
- [Scheduling with Communication Delay in Near-Linear Time](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2022.47)
- [20th International Symposium on Parameterized and Exact Computation (IPEC 2025)](https://drops.dagstuhl.de/entities/volume/LIPIcs-volume-358)
- [Monaldo MASTROLILLI | Università della Svizzera italiana, Lugano | USI | IDSIA | Research profile](https://www.researchgate.net/profile/Monaldo-Mastrolilli)
- [45th International Symposium on Mathematical Foundations of Computer Science (MFCS 2020)](https://drops.dagstuhl.de/entities/volume/LIPIcs-volume-170)
- [Packing and Scheduling Algorithms for Information and Communication Services (Dagstuhl Seminar 11091).](https://www.researchgate.net/publication/220608105_Packing_and_Scheduling_Algorithms_for_Information_and_Communication_Services_Dagstuhl_Seminar_11091)
- [A Subexponential Time Algorithm for Makespan Scheduling of Unit Jobs with Precedence Constraints](https://arxiv.org/abs/2312.03495)
- [dblp: Monaldo Mastrolilli](https://dblp.org/pid/m/MonaldoMastrolilli.html)
- [Computational Complexity: new papers, page 2 — ReadSearch](https://readsearch.ai/topics/computer-science-and-ai/computational-complexity?page=2)
- [Data Structures and Algorithms](https://arxiv.cnoctave.top/list/cs.DS/recent?show=50&skip=71)
- [Makespan Scheduling of Unit Jobs with Precedence Constraints in $O(1.995^n)$ time](https://arxiv.org/abs/2208.02664)
- [Computational Complexity](https://arxiv.cnoctave.top/list/cs.CC/recent?show=50&skip=14)
- [Parameterized Complexity of a Parallel Machine Scheduling Problem](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.IPEC.2022.21)
- [On the Fine-Grained Parameterized Complexity of Partial Scheduling to Minimize the Makespan](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.IPEC.2020.25)
- [24th Annual European Symposium on Algorithms (ESA 2016)](https://drops.dagstuhl.de/entities/volume/LIPIcs-volume-57)
- [Parameterized Complexity of Scheduling Chains of Jobs with Delays](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.IPEC.2020.4)
- [dblp: Encyclopedia of Algorithms 2016](https://einstein.dagstuhl.de/db/reference/algo/algo2016.html)
- [15th International Symposium on Parameterized and Exact Computation (IPEC 2020)](https://drops.dagstuhl.de/entities/volume/LIPIcs-volume-180)
- [dblp: Ola Svensson](https://dblp.org/pid/11/6945.html)
- [33rd Annual European Symposium on Algorithms (ESA 2025)](https://drops.dagstuhl.de/entities/volume/LIPIcs-volume-351)

### Batch 9: lit_venues_3

Engine: `system1`. Results were returned as a merged batch. No per-query attribution is inferred.

Queries:

- `STOC "precedence constraints" "unit" "Levey"`
- `FOCS "scheduling" "unit" "precedence"`
- `IPCO "precedence" "unit" scheduling`
- `"P4" "prec" "NP-hard" scheduling`

**Outcome:** Stronger-engine follow-up found Levey–Rothvoss STOC 2016/journal 2019, FOCS 2020 work with communication delay, and IPCO scheduling results for other settings. No returned source established the requested fixed-m≥4 hardness claim. This is a search outcome, not a proof that no mathematical connections exist.

Returned source headings/URLs:

- [A (1+epsilon)-Approximation for Makespan Scheduling with Precedence Constraints Using LP Hierarchies](https://epubs.siam.org/doi/abs/10.1137/16M1105049)
- [A (1+epsilon)-Approximation for Makespan Scheduling with Precedence Constraints Using LP Hierarchies](https://www.researchgate.net/publication/336794624_A_1epsilon-Approximation_for_Makespan_Scheduling_with_Precedence_Constraints_Using_LP_Hierarchies)
- [Hierarchy-Based Algorithms for Minimizing Makespan under Precedence and Communication Constraints](https://www.microsoft.com/en-us/research/publication/hierarchy-based-algorithms-for-minimizing-makespan-under-precedence-and-communication-constraints/)
- [FOCS 2020](https://ieee-focs.org/FOCS-2020-Papers/)
- [Scheduling with Precedence Constraints of Low Fractional Dimension](https://www.researchgate.net/publication/221316727_Scheduling_with_Precedence_Constraints_of_Low_Fractional_Dimension)
- [Complexity of Scheduling under Precedence Constraints](https://pubsonline.informs.org/doi/abs/10.1287/opre.26.1.22)
- [Parameterized Complexity of Scheduling Unit-Time Jobs with Generalized Precedence Constraints](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.IPEC.2025.7)
- [A (1+epsilon)-approximation for Makespan Scheduling with Precedence Constraints Using LP Hierarchies](https://simons.berkeley.edu/talks/1epsilon-approximation-makespan-scheduling-precedence-constraints-using-lp-hierarchies)
- [Fine-Grained Parameterized Complexity of Scheduling and](https://research.tue.nl/files/228924206/20221202_Swennenhuis_hf.pdf)
- [A Subexponential Time Algorithm for Makespan Scheduling of Unit Jobs with Precedence Constraints](https://doi.org/10.1145/3785365)
- [A Simpler QPTAS for Scheduling Jobs with Precedence Constraints](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2022.40)
- [‘Strong’–‘weak’ precedence in scheduling: Extensions to series–parallel orders](https://www.academia.edu/33523333/_Strong_weak_precedence_in_scheduling_Extensions_to_series_parallel_orders)

### Batch 10: lit_bib_extra

Engine: `system1`. Results were returned as a merged batch. No per-query attribution is inferred.

Queries:

- `"Garey" "Johnson" "OPEN8" "238"`
- `"Computers and Intractability" "1979" "Freeman" ISBN`
- `"Optimal Sequencing of Two Equivalent Processors" filetype:pdf`

**Outcome:** Confirmed Garey–Johnson bibliographic metadata and surfaced FKN original/erratum. A CMU PDF opened as a possible book route was lecture material with a bibliography, so it was not used to check the book entry.

Returned source headings/URLs:

- [openai/math: 372 claimed theorems, 26 million lines of Lean, and what the green tick means](https://ai.satyajit.si/articles/openai-math)
- [Computers and Intractability](https://en.wikipedia.org/wiki/Computers_and_Intractability)
- [Computers and Intractability](https://books.google.com/books/about/Computers_and_Intractability.html?id=fjxGAQAAIAAJ)
- [dblp: Computers and Intractability: A Guide to the Theory of NP-Completeness.](https://dblp.org/rec/books/fm/GareyJ79.html)
- [Optimal Sequencing of Two Equivalent Processors](https://epubs.siam.org/doi/10.1137/0117070)
- [Erratum “Optimal Sequencing of Two Equivalent Processors”](https://epubs.siam.org/doi/10.1137/0120018)
- [Polynomial time approximation algorithms for machine scheduling: ten open problems](https://onlinelibrary.wiley.com/doi/pdf/10.1002/%28SICI%291099-1425%28199909/10%292%3A5%3C203%3A%3AAID-JOS26%3E3.0.CO%3B2-5)
- [Two-Processor Scheduling with Start-Times and Deadlines](https://epubs.siam.org/doi/10.1137/0206029)
- [# Computers and Intractability](https://iiif.library.cmu.edu/file/Traub_box00020_fld00024_bdl0001_doc0001/Traub_box00020_fld00024_bdl0001_doc0001.pdf)

### Batch 11: lit_fixed

Engine: `system1`. Results were returned as a merged batch. No per-query attribution is inferred.

Queries:

- `"P4" "prec,p" scheduling polynomial`
- `"fixed" "four" "unit-time" "precedence" NP-hard`
- `site:arxiv.org "fixed number of machines" "scheduling" "precedence"`
- `site:informatik.uni-kiel.de "Jansen" "2026" "Precedence"`

**Outcome:** Returned Jansen’s exact all-fixed-m theorem and older small-height results; no new fixed-four hardness theorem. The Kiel author-domain query had no useful relevant match. A search hit concerning compactly represented jobs was not treated as the explicit-vertex input theorem.

Returned source headings/URLs:

- [Precedence Constraint Scheduling on a Fixed Number of Machines](https://arxiv.org/abs/2611.09392)
- [Precedence Constraint Scheduling on a Fixed Number of Machines](https://borowiecki.dev/abs/2611.09392)
- [Scheduling unit-length jobs with precedence constraints of small height](https://www.sciencedirect.com/science/article/pii/S0167637714000182)
- [A polynomial algorithm for some preemptive multiprocessor task scheduling problems](https://www.sciencedirect.com/science/article/pii/S0377221705005837)
- [Handbook on Scheduling: From Theory to Practice (2nd ed.) 978-3-319-99848-0;978-3-319-99849-7 - DOKUMEN.PUB](https://dokumen.pub/handbook-on-scheduling-from-theory-to-practice-2nd-ed-978-3-319-99848-0978-3-319-99849-7.html)
- [Multiprocessor scheduling with communication delays](https://www.academia.edu/79062027/Multiprocessor_scheduling_with_communication_delays)
- [Scheduling of Precedence Constrained Un](https://pure.tue.nl/ws/files/228924206/20221202_Swennenhuis_hf.pdf)
- [A Subexponential Time Algorithm for Makespan Scheduling of Unit Jobs with Precedence Constraints](https://research-portal.uu.nl/en/publications/a-subexponential-time-algorithm-for-makespan-scheduling-of-unit-j/)
- [Chap. 3 / Parallel Machine Scheduling](https://ikucukkoc.baun.edu.tr/lectures/EMM4129/Algorithms_for_Sequencing_and_Scheduling.pdf)

### Batch 12: lit_citations

Engine: `system1`. Results were returned as a merged batch. No per-query attribution is inferred.

Queries:

- `"A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling" "references"` (recency: 90 days)
- `"OpenAI" "scheduling" "leaf" "fixed" machines` (recency: 90 days)
- `"Jesper Nederlof" publications scheduling 2026`
- `"Klaus Jansen" "2611.09392" -site:borowiecki.dev -site:themoonlight.io`

**Outcome:** Exact-title and source-name searches found a mathcommunity revised-preprint activity record (27 October 2026 bibliography/cross-reference maintenance), the official OpenAI item, Jansen and author publication lists. This does not certify a complete forward-citation index.

Returned source headings/URLs:

- [A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling](https://github.com/openai/math/tree/main/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026)
- [math/lean/docs/124.md at main · openai/math · GitHub](https://github.com/openai/math/blob/main/lean/docs/124.md)
- [Activity · oai-math-revised](https://mathcommunity.github.io/oai-math-revised/activity/)
- [A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling · oai-math-revised](https://mathcommunity.github.io/oai-math-revised/papers/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/)
- [A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling | Plectis Atlas](https://wcook04.github.io/plectis-atlas/papers/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026.html)
- [OpenAI Mathematics — Searchable Preprint Catalogue](https://sites.pitt.edu/~hajlasz/OpenAI_Math_Catalogue.html)
- [Homepage of Jesper Nederlof](https://webspace.science.uu.nl/~neder003/publications.html)
- [Jesper Nederlof - Utrecht University](https://research-portal.uu.nl/en/persons/jesper-nederlof/)
- [Precedence Constraint Scheduling on a Fixed Number of Machines](https://accelresearching.com/accel-zinc-picolinate-50mg/?_=%2Fabs%2F2611.09392%23nLw79nwZb1b3uPkZUsgpm5M%3D)
- [Optimal three-machine unit-job scheduling (Lean) | Plectis Atlas](https://wcook04.github.io/plectis-atlas/statements/ThreeMachine.html)
- [124 · Math Release Atlas](https://jkbennitt.github.io/math-release-atlas/f/124/)

### Batch 13: lit_final

Engine: `system1`. Results were returned as a merged batch. No per-query attribution is inferred.

Queries:

- `site:hexagonmath.org "scheduling" "machines"` (recency: 90 days)
- `"precedence" scheduling "linear" "leaf" machines` (recency: 90 days)
- `"four-machine" "scheduling-proof-exploration"` (recency: 90 days)

**Outcome:** Rechecked Hexagon, linear-leaf terminology and four-machine repository wording. Returned Giraudin, Jansen and related older material; direct opens verified original ESA/SODA texts and CG metadata. No additional exact result beyond the identified sources was established.

Returned source headings/URLs:

- [Advanced search · Hexagon](https://hexagonmath.org/search?advanced=1&msc=68Q25)
- [Hexagon](https://hexagonmath.org/)
- [All works · Hexagon](https://hexagonmath.org/search?cursor=eyJ2IjoxLCJzb3J0RGF0ZSI6IjIwMjYtMTEtMDZUMTg6MTI6MjQuNzQ1WiIsImlkZW50aWZpZXIiOiIyNjExLjAwMTU3In0&direction=next&page=2&per_page=100)
- [Scheduling unit-length jobs with precedence constraints of small height](https://www.sciencedirect.com/science/article/pii/S0167637714000182)
- [Precedence Constraint Scheduling on a Fixed Number of Machines](https://borowiecki.dev/pdf/2611.09392)
- [Precedence Constraint Scheduling on a Fixed Number of Machines](https://arxiv.org/abs/2611.09392)
- [Scheduling with Communication Delay in Near-Linear Time](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2022.47)
- [Scheduling identical jobs with chain precedence constraints on two uniform machines](https://research.utwente.nl/en/publications/60924dc7-f0af-47c1-9ec5-936b32f957e4/)
- [Optimal Sequencing of Two Equivalent Processors | SIAM Journal on Applied Mathematics](https://epubs.siam.org/doi/epdf/10.1137/0117070)
- [Optimal scheduling for two-processor systems | Acta Informatica | Springer Nature Link](https://link.springer.com/article/10.1007/BF00288685)
- [A Simpler QPTAS for Scheduling Jobs with Precedence Constraints](https://drops.dagstuhl.de/storage/00lipics/lipics-vol244-esa2022/LIPIcs.ESA.2022.40/LIPIcs.ESA.2022.40.pdf)
- [A Subexponential Time Algorithm for Makespan Scheduling of Unit Jobs with Precedence Constraints](https://research-portal.uu.nl/ws/portalfiles/portal/254249631/1.9781611978322.16.pdf)

Direct opens bundled with this batch: https://epubs.siam.org/doi/epdf/10.1137/0117070, https://link.springer.com/article/10.1007/BF00288685, https://drops.dagstuhl.de/storage/00lipics/lipics-vol244-esa2022/LIPIcs.ESA.2022.40/LIPIcs.ESA.2022.40.pdf, https://research-portal.uu.nl/ws/portalfiles/portal/254249631/1.9781611978322.16.pdf.

### Batch 14: lit_closing

Engine: `system1`. Closing date-matched pass; merged batch output. Returned secondary commentary is recorded as citing material, not mathematical verification.

Queries:

- `"A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling" -site:github.com/openai` (recency: 90 days)
- `"Precedence Constraint Scheduling on a Fixed Number of Machines" "2026"` (recency: 90 days)
- `"unit jobs" "fixed" "machines" "polynomial" November 2026` (recency: 90 days)
- `"scheduling" "leaf" "4m+5"` (recency: 90 days)

**Outcome:** Closing pass on 15 November 2026 with four current-result/exact-title queries reconfirmed Jansen and the OpenAI scope, and found the Plectis Atlas statement catalogue, mathcommunity revised paper and AI Proved What episode. These were opened as citing/expository items, not proof verification. The original episode URL redirects to its updated episode page; the page reports a 30 October 2026 last check and an October 26 remake. No additional all-fixed-m exact theorem or fixed-m hardness claim was established by this closing batch.

Returned source headings/URLs:

- [A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling](https://github.com/openai/math/tree/main/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026)
- [math/lean/docs/124.md at main · openai/math · GitHub](https://github.com/openai/math/blob/main/lean/docs/124.md)
- [OpenAI Mathematics — Searchable Preprint Catalogue](https://sites.pitt.edu/~hajlasz/OpenAI_Math_Catalogue.html)
- [Precedence Constraint Scheduling on a Fixed Number of Machines](https://arxiv.org/abs/2611.09392)
- [Precedence Constraint Scheduling on a Fixed Number of Machines](https://arxiv.cnoctave.top/pdf/2611.09392)
- [Optimal three-machine unit-job scheduling (Lean) | Plectis Atlas](https://wcook04.github.io/plectis-atlas/statements/ThreeMachine.html)
- [math/overview.tex at main · openai/math · GitHub](https://cdn.hddj.top/openai/math/blob/main/overview.tex)
- [A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling · oai-math-revised](https://mathcommunity.github.io/oai-math-revised/papers/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/)
- [Three machines, polynomial? Scheduling unit jobs with precedence | AI Proved What?](https://aiprovedwhat.com/episodes/124-polynomial-time-scheduling-three-identical/)
- [Three machines, polynomial? Scheduling unit jobs with precedence | AI Proved What?](https://aiprovedwhat.com/episodes/124-three-machine-scheduling/)
- [math/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/build/lists.tex at main · openai/math · GitHub](https://github.com/openai/math/blob/main/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/build/lists.tex)

## Deposit-language recommendation

“A focused literature search on 15 November 2026 found Jansen’s existing all-fixed-machine theorem and linear description budgets, drbh’s complete four-machine source adaptation, and Giraudin’s three-machine exponent refinement. This manuscript gives its own checked Q03 proof and accounting; it makes no priority claim. The finite search did not locate a fixed-m≥4 hardness result in the stated model. External theorem statements were source-checked; the complete external proofs were not independently audited.”

The exact extent to which the Q03 proof is confirmed is determined by the separate F/D audit, not by this search paragraph.
