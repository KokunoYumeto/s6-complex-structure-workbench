#!/usr/bin/env python3
"""Render the dated search record from retained query/result metadata.
No search-result abstracts or external full text are redistributed.
The initial batches were recorded from the session transcript; later batches
were saved directly from tool-result title/URL/reference metadata.
"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PATH=ROOT/'code/C_search_history.json'
data=json.loads(PATH.read_text())
closing=ROOT/'code/C_search_closing.json'
if closing.exists():data.append(json.loads(closing.read_text()))
early=[
 {'id':'early_1','engine':'system1','queries':[
  {'q':'"A polynomial-time algorithm for three-machine unit-job scheduling" OpenAI'},
  {'q':'"scheduling-proof-exploration" drbh'},
  {'q':'"unit jobs" "four machines" polynomial 2026'}],
  'result_sources':[
   {'title':'OpenAI scheduling preprint','url':'https://github.com/openai/math/tree/main/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026'},
   {'title':'drbh repository','url':'https://github.com/drbh/scheduling-proof-exploration'},
   {'title':'Jansen full-text mirror','url':'https://borowiecki.dev/pdf/2611.09392'},
   {'title':'Giraudin three-machine refinement','url':'https://hexagonmath.org/pdf/2611.00060v1'}],
  'outcome':'Located the supplied preprint/repository and the later all-fixed-machine and three-machine refinement papers. Their actual statements were subsequently opened.'},
 {'id':'early_2','engine':'system1','queries':[
  {'q':'"2611.09392" Jansen'},
  {'q':'"Precedence Constraint Scheduling on a Fixed Number of Machines"'},
  {'q':'"scheduling-proof-exploration" "bbd3013"'}],
  'result_sources':[{'title':'Jansen arXiv metadata','url':'https://arxiv.org/abs/2611.09392'},{'title':'Jansen full-text mirror','url':'https://borowiecki.dev/pdf/2611.09392'}],
  'outcome':'Verified official arXiv author/title/submission identity. The exact drbh commit was not usefully indexed; the GitHub API and exact archive were then used.'},
 {'id':'early_3','engine':'system2','queries':[
  {'q':'"Optimal sequencing of two equivalent processors" Fujii Kasami Ninomiya 1969 erratum'},
  {'q':'"Optimal scheduling for two-processor systems" 1972 Coffman Graham pdf'},
  {'q':'"NP-complete scheduling problems" Ullman 1975 pdf'},
  {'q':'"Garey" "Johnson" "OPEN8" "PREC" 1979'}],
  'result_sources':[
   {'title':'FKN original publisher entry','url':'https://epubs.siam.org/doi/10.1137/0117070'},
   {'title':'FKN erratum publisher entry','url':'https://epubs.siam.org/doi/10.1137/0120018'},
   {'title':'Coffman–Graham author-hosted scan','url':'https://fanchung.ucsd.edu/ron/papers/72_04_two_processors.pdf'},
   {'title':'Ullman original scan','url':'https://www.cs.montana.edu/bhz/classes/fall-2021/csci460/paper4.pdf'},
   {'title':'Garey–Johnson book scan','url':'https://perso.limos.fr/~palafour/PAPERS/PDF/Garey-Johnson79.pdf'}],
  'outcome':'Found original-paper/book scans and the omitted FKN erratum. Original FKN full text remained behind the access page; all other listed scans were retrieved.'},
 {'id':'early_4','engine':'system1','queries':[
  {'q':'"A simpler QPTAS" ESA 2022 40:1 40:15'},
  {'q':'"A subexponential" "Nederlof" "535" "552" SODA 2025'}],
  'result_sources':[
   {'title':'Das–Wiese official ESA proceedings record','url':'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2022.40'},
   {'title':'Nederlof–Swennenhuis–Węgrzycki official SODA record','url':'https://epubs.siam.org/doi/10.1137/1.9781611978322.16'}],
  'outcome':'Checked original proceedings metadata: ESA article 40 has eleven pages (40:1–40:11), and SODA pages535–552. The page-range query was a search hypothesis, not a bibliographic assertion.'}
]
for b in early:
 b.update(date='2026-11-15',timezone='Europe/Berlin',note='Initial-batch queries and selected returned sources recorded from the session transcript; merged search output does not identify which query returned each source.')
outcomes={
 'literature_batch_1':'Returned OpenAI, its scope file, the course, indexes and historical open-question material. No additional exact theorem beyond the sources later identified. The literal 12m/25 query did not establish an earlier publication of that exact Q03 constant.',
 'lit_venues_0':'Official arXiv metadata identified Jansen arXiv:2611.09392. Hexagon search identified Giraudin2611.00060v1. Other results concerned differing processing assumptions or objectives; only statements opened and compared were used for the conclusion.',
 'lit_venues_1':'SODA2025 returned the cited exact subexponential algorithm; ICALP2018 returned Garg’s approximation scheme. STOC/FOCS domain coverage was sparse and was supplemented by system1 in lit_venues_3.',
 'lit_venues_2':'ESA returned Das–Wiese2022. APPROX returned related flow-time/other scheduling objectives. IPCO results concerned other objective/model settings; none of the returned titles supplied an exact arbitrary-precedence fixed-m≥4 polynomial theorem or a fixed-m hardness theorem. Jansen’s exact title was independently returned.',
 'lit_venues_3':'Stronger-engine follow-up found Levey–Rothvoss STOC2016/journal2019, FOCS2020 work with communication delay, and IPCO scheduling results for other settings. No returned source established the requested fixed-m≥4 hardness claim. This is a search outcome, not a proof that no mathematical connections exist.',
 'lit_bib_extra':'Confirmed Garey–Johnson bibliographic metadata and surfaced FKN original/erratum. A CMU PDF opened as a possible book route was lecture material with a bibliography, so it was not used to check the book entry.',
 'lit_fixed':'Returned Jansen’s exact all-fixed-m theorem and older small-height results; no new fixed-four hardness theorem. The Kiel author-domain query had no useful relevant match. A search hit concerning compactly represented jobs was not treated as the explicit-vertex input theorem.',
 'lit_citations':'Exact-title and source-name searches found a mathcommunity revised-preprint activity record (27Oct2026 bibliography/cross-reference maintenance), the official OpenAI item, Jansen and author publication lists. This does not certify a complete forward-citation index.',
 'lit_final':'Rechecked Hexagon, linear-leaf terminology and four-machine repository wording. Returned Giraudin, Jansen and related older material; direct opens verified original ESA/SODA texts and CG metadata. No additional exact result beyond the identified sources was established.',
 'lit_closing':'Closing pass on15November2026 with four current-result/exact-title queries reconfirmed Jansen and the OpenAI scope, and found the Plectis Atlas statement catalogue, mathcommunity revised paper and AI Proved What episode. These were opened as citing/expository items, not proof verification. The original episode URL redirects to its updated episode page; the page reports a30October2026 last check and an October26 remake. No additional all-fixed-m exact theorem or fixed-m hardness claim was established by this closing batch.'
}
allb=early+data
for b in allb:
 if b['id'] in outcomes:b['outcome']=outcomes[b['id']]
(ROOT/'code/C_search_history_complete.json').write_text(json.dumps(allb,indent=2)+'\n')
intro='''# Q03 literature search

**Date:** 15 November 2026, Europe/Berlin. **Researcher:** GPT-6 Astra (OpenAI), effort ChatGPT Pro mode. The task date is the local Berlin date; the clock was 14 November in UTC during part of this session.

## Result that controls novelty language

The search found an existing public all-fixed-machine exact-algorithm statement: Klaus Jansen, [arXiv:2611.09392v1](https://arxiv.org/abs/2611.09392v1), dated6November2026. Theorem1.1 and the linear leaf budgets in Lemma7.15 were opened and compared. The precise machine models, exponents and budgets are recorded once in `Q03_DEPOSIT_sources.md`, S-J. That source was checked for its statements, not independently certified by a complete proof audit.

The exact drbh commit already contains a complete four-machine release-theorem adaptation; its scope is S-D. [David Niedbala Giraudin’s Hexagon2611.00060v1](https://hexagonmath.org/pdf/2611.00060v1) supplies a separate three-machine exponent refinement (S-G). The public course’s lessons9–11 explicitly derive from Q03; they are recorded as derivative material, not independent verification.

The revised post should say what this Q03 manuscript proves and how its construction/accounting is derived. It must remove “new here for m≥4” and unqualified novelty for linear leaf budgets. A different displayed numeric budget is not by itself a novelty or priority proof. No priority is claimed. New authors found in the search are cited as prior literature; they are not credited as producers of Q03.

The searches below did not locate a source establishing hardness for any one fixed m≥4 in the exact explicit-job/unit-length/arbitrary-acyclic-precedence model. This records a finite search result, not a universal theorem of nonexistence. In particular, Ullman’s unit-job reduction has variable processor count. Approximation and exact scheduling are related by the integral-optimum argument in S-A; the approximation bound under that substitution does not establish polynomial time.

## Search method and limits

The search covered arXiv, general web, STOC, FOCS, SODA, ICALP, IPCO, ESA, APPROX, author publication pages, Hexagon, the exact OpenAI title, source-name combinations and linear-leaf terminology. Both exposed search engines were used; weak venue coverage was checked with the stronger engine. Recency90days was used on current-result/citation queries where recorded below. Existing primary papers and official metadata were opened to compare the actual model and statement. Search snippets alone were used to identify leads, not to certify a theorem.

“Everything that cites the OpenAI preprint” was approached through exact-title, author/source-name, repository, course and revised-preprint searches. Search indexing is incomplete, and no complete forward-citation database for this GitHub preprint was obtained. The resulting known citing/derived items are listed below. The record does not assert an exhaustive census of every published or unindexed citation. The full focused query set and returned-source headings are retained to make that limitation reviewable.

The initial four search batches were transcribed from the session record; their selected relevant result URLs are listed. Subsequent batches preserve every returned title/URL heading from the saved tool output. Results within a batch were returned merged, so no unsupported one-to-one query/result attribution is invented. Direct source opens, failed opens and recovery methods are also recorded in the source report.

## Coverage and opened leads

| Requested direction | Queries/batches | Opened result used |
|---|---|---|
| Exact polynomial for every fixed m≥4 | early1–2; arXiv and fixed-machine batches | Jansen v1, Theorem1.1; primary arXiv PDF |
| Exact polynomial for m=4 | drbh/title and fixed-four queries | Exact drbh bbd3013 source release theorem |
| Hardness for fixed m≥4 | lit_venues0, lit_venues3, lit_fixed | No matching claim found; Ullman parameter scope checked directly |
| Linear leaf structure | 12m/25, leaf/description and final linear-leaf queries | Jansen Lemma7.15; OpenAI constant-budget construction; Q03 derivative lessons |
| STOC | lit_venues1 and lit_venues3 | Levey–Rothvoss approximation paper, official journal record |
| FOCS | lit_venues1 and lit_venues3 | Official FOCS2020 list; returned communication-delay paper treated only as a lead |
| SODA | early4 and lit_venues1 | Nederlof–Swennenhuis–Węgrzycki2025, official proceedings and full text |
| ICALP | lit_venues1 | Garg2018, official DROPS record |
| IPCO | lit_venues2 and lit_venues3 | Returned single-machine/other-objective leads; no exact target-model theorem established |
| ESA | early4 and lit_venues2 | Das–Wiese2022, official full proceedings paper |
| APPROX | lit_venues2 | Returned flow-time and other scheduling leads; no exact target-model theorem established |
| Authors’ pages | lit_fixed, lit_citations | Nederlof publication page; MPI publications; Kiel query yielded no useful target |
| Hexagon | early1, lit_venues0, lit_final | Giraudin2611.00060v1, full PDF |
| OpenAI citing/derived work | exact-title/source-name batches | Jansen, Giraudin, drbh adaptation, course, mathcommunity revision activity |

## Known citing or derived items encountered

| Item | Evidence and role |
|---|---|
| drbh adaptation | Exact pinned repository is explicitly derived from OpenAI scheduling files; full m=4 release scope, S-D. |
| Course lessons1–11 | Course source metadata and lesson bylines; chapters9–11 identify Q03 as their basis, S-L. |
| Jansen | Opening relation-to-OpenAI discussion and references in the opened PDF; exact all-fixed-m statement, S-J. |
| Giraudin | OpenAI structure is invoked in the opened three-page paper; three-machine exponent refinement, S-G. |
| mathcommunity revised-preprint activity | [Activity log](https://mathcommunity.github.io/oai-math-revised/activity/), 27October2026 entry: bibliography and cross-reference maintenance. It is a separate community revision; the byte comparison in S-P uses the official OpenAI repository. |
| AI Proved What episode | [Opened episode](https://aiprovedwhat.com/episodes/124-three-machine-scheduling/), directly citing OpenAI; its old episode URL redirects here. Logged as exposition, not as verification of mathematical claims. |
| Plectis Atlas | [Opened statement page](https://wcook04.github.io/plectis-atlas/statements/ThreeMachine.html), linking the OpenAI theorem and comparator. Logged as a source index, not as an independent theorem proof. |

## Every query and what it found

All following batches were run on15November2026 Europe/Berlin. Query spelling, including exploratory terms or guessed page ranges, is preserved; a query is not a factual assertion. The complete metadata counterpart is `code/C_search_history_complete.json`.

'''
lines=[intro]
for i,b in enumerate(allb,1):
 lines += [f"### Batch {i}: {b['id']}",'',f"Engine: `{b['engine']}`. {b['note']}",'','Queries:','']
 for q in b['queries']:
  rec=f" (recency: {q['recency']} days)" if 'recency' in q else ''
  lines.append(f"- `{q['q']}`{rec}")
 lines += ['',f"**Outcome:** {b.get('outcome','See returned sources. Verified relevant statements are in the source report.')}",'','Returned source headings/URLs:','']
 for r in b['result_sources']:
  title=r['title'].replace('[','(').replace(']',')')
  result_url=r['url'].split(' ; rewritten summary of ')[0]
  lines.append(f"- [{title}]({result_url})")
 if b.get('open_commands'):
  lines += ['','Direct opens bundled with this batch: '+', '.join(x['ref_id'] for x in b['open_commands'])+'.']
 lines.append('')
lines += ['## Deposit-language recommendation','',
 '“A focused literature search on15November2026 found Jansen’s existing all-fixed-machine theorem and linear description budgets, drbh’s complete four-machine source adaptation, and Giraudin’s three-machine exponent refinement. This manuscript gives its own checked Q03 proof and accounting; it makes no priority claim. The finite search did not locate a fixed-m≥4 hardness result in the stated model. External theorem statements were source-checked; the complete external proofs were not independently audited.”','',
 'The exact extent to which the Q03 proof is confirmed is determined by the separate F/D audit, not by this search paragraph.']
rendered='\n'.join(lines)+'\n'
spacing={
 'dated6November2026':'dated 6 November 2026','Theorem1.1':'Theorem 1.1',
 'Lemma7.15':'Lemma 7.15','Hexagon2611':'Hexagon 2611','Giraudin2611':'Giraudin 2611',
 'lessons9–11':'lessons 9–11','chapters9–11':'chapters 9–11','lessons1–11':'lessons 1–11',
 'recency90days':'recency 90 days','FOCS2020':'FOCS 2020','STOC2016':'STOC 2016',
 'journal2019':'journal 2019','SODA2025':'SODA 2025','Nederlof–Swennenhuis–Węgrzycki2025':'Nederlof–Swennenhuis–Węgrzycki 2025',
 'ICALP2018':'ICALP 2018','Garg2018':'Garg 2018','Das–Wiese2022':'Das–Wiese 2022',
 'on15November2026':'on 15 November 2026','on15November':'on 15 November',
 '27October2026':'27 October 2026','27Oct2026':'27 October 2026','pages535–552':'pages 535–552',
 'a30October2026':'a 30 October 2026','October26':'October 26',
 'early1–2':'early 1–2','early4':'early 4','lit_venues0':'lit_venues_0',
 'lit_venues1':'lit_venues_1','lit_venues2':'lit_venues_2','lit_venues3':'lit_venues_3',
}
for old,new in spacing.items():rendered=rendered.replace(old,new)
dest=ROOT/'Q03_DEPOSIT_literature.md';dest.write_text(rendered)
print(f'{len(allb)} batches, {sum(len(b["queries"]) for b in allb)} queries, {sum(len(b["result_sources"]) for b in allb)} recorded source headings')
print(f'{dest.name}: {len(dest.read_text().splitlines())} lines')
