#!/usr/bin/env python3
"""Inspect, or explicitly apply, the reviewed Paper III provenance/deposit data.

Prepared only: the author has not executed this application program. Default
mode prints every proposed field, III row and appended section. --apply is
reserved for root after the complete code and proposal have been read.
No source, event ledger, count record or other-paper entry is edited.
"""

import argparse
import csv
import io
import json
from pathlib import Path
import re


BASE = Path(__file__).resolve().parent.parent
NOTE = BASE / "agents/continuation8_iii_later/S6_SERIES_PUBLISH_III_final_provenance_deposit_review.md"
SOURCE = BASE / "S6_SERIES_PUBLISH_III.tex"
COUNTS = BASE / "records/S6_SERIES_PUBLISH_III_current_check_counts.json"
TABLE = BASE / "S6_SERIES_PUBLISH_provenance_checks.tsv"
MARKDOWN = BASE / "S6_SERIES_PUBLISH_deposit_fields.md"
DEPOSIT = BASE / "S6_SERIES_PUBLISH_deposit_fields_III.json"
SCHEMA = [
    "claim_id", "paper", "locations", "claim", "against_records",
    "by_recomputation", "against_primary_source", "required_action", "evidence",
    "prior_claim", "prior_records_assessment", "prior_recomputation_assessment",
    "prior_primary_assessment", "current_paper_location", "current_deposit_location",
    "resolution_status", "remaining_gate", "old_HEXAGON_disposition", "current_resolution",
]
FIELD_NAMES = [
    "title", "subject", "crossListSubjects", "tags", "mscCodes", "authorshipMode",
    "license", "abstract", "comments", "provenance", "aiSystems",
]
RECORDS_URL = "https://github.com/KokunoYumeto/s6-complex-structure-workbench/blob/main/RECORDS.md#paper-iii"
COMMIT_IN_SOURCE = "a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7"
EXPECTED_COUNTS = {
    "targeted proof check": 421,
    "independent re-proof": 2,
    "computation or formal certificate": 50,
    "used and rechecked in this run": 473,
    "carried as background without fault found": 90,
    "refuted, with the refined statement's id": 30,
}
REVIEW_EVIDENCE = (
    "agents/continuation8_iii_later/S6_SERIES_PUBLISH_III_final_provenance_deposit_review.md; "
    "FR=agents/continuation8_iii_later/S6_SERIES_PUBLISH_III_frontmatter_publication_review.md; "
    "BR=agents/continuation8_iii_later/S6_SERIES_PUBLISH_III_bibliography_publication_review.md"
)
ACCESS_EVIDENCE = (
    "code/S6_SERIES_PUBLISH_c8_III_provenance_links.py and its .stdout.txt/.stderr.txt; "
    "code/S6_SERIES_PUBLISH_c8_III_provenance_primary.py and its .stdout.txt/.stderr.txt; "
    "code/S6_SERIES_PUBLISH_c8_III_provenance_primary_msc_v002.stdout.txt and .stderr.txt"
)
PDF_GATE = (
    "Final PDF visual agreement at the listed source passage: complete readable text, "
    "mathematical signs and scope, resolved supplying references, and no clipped table/display. "
    "No final-PDF reading is asserted by this application."
)
JOINT_GATE = (
    "Five-together series/table/cross-paper comparison remains pending. "
    "This III-only application preserves the other papers' entries without adjudicating them."
)
LIVE_GATE = (
    "At submission the live Paper III records section must be updated from checkpoint 34 "
    "to the actually submitted source/records/programs, and its source commit must be set "
    "there. No external publication or live-page update is performed."
)
STATUS_SOURCE_COMPLETE = "complete: three-way source/deposit provenance"

# The data below are literal reviewed data, not a new ledger/count computation.
DEPOSIT_DATA = json.loads(r'''
{
  "title": "The $(3,4,\\infty)$ family of complex six-spheres. III. Maps and the resulting manifolds",
  "subject": "math.CV",
  "crossListSubjects": [
    "math.GT",
    "math.AT",
    "math.AG"
  ],
  "tags": [
    "complex six-spheres",
    "homotopy classes",
    "torus fibrations",
    "compact complex threefolds",
    "integral cohomology",
    "smooth classification",
    "elliptic surfaces",
    "Kummer covers",
    "conifold smoothing",
    "AI-authored mathematics"
  ],
  "mscCodes": [
    "32Q55",
    "32J17",
    "55Q40",
    "57R55",
    "14J27"
  ],
  "authorshipMode": "no-human-author-claimed",
  "license": "CC0 1.0",
  "abstract": "We compute the homotopy classes of three maps associated with the $(3,4,\\infty)$ family of complex six-spheres. The torus quotient represents the element of order two in $\\pi_6(S^3)$, the holomorphic map to $\\mathbb P^1$ is null-homotopic, and the cusp map that keeps the angular coordinate represents the nonzero element of $\\pi_6(S^4)$. Normal framings and integral attaching maps give these classes and a finite cell model. For every cyclic universal cover we calculate the integral cohomology ring and the complete smooth classification invariant. We classify the natural section-line sphere fillings over twenty-one elliptic profiles: there are $59$ marked patterns on $50$ initial data, with twelve profiles admitting unbounded multiplicity. We also determine weighted smooth types and the homology of every free OS49 affine cap, including its additional three-primary torsion. A weighted OS45 member has zero refined Pontryagin class, as follows from an embedded Hopf sphere and its critical-cycle linking number. The local Kummer cover has no smooth compact global extension at degree greater than one; an explicit finite flat normal extension has additional components above the cusp. Finally, moving the zero of the line-bundle linearization gives a conifold smoothing diffeomorphic to $S^3\\times S^3$, of algebraic dimension one.",
  "comments": "Paper III of the five-paper series \"The (3,4,∞) family of complex six-spheres\". The main results determine the three sphere-map classes, compute integral and smooth invariants of the cyclic and elliptic constructions, and construct an algebraic-dimension-one conifold smoothing on S³×S³. The original complex six-sphere family is due to Claude and L. Alpöge (https://alpo.ge/s6.pdf). Principal construction inputs include Engel's elliptic-surface model (arXiv:2609.38442v1), Yang's toroidal fillings (arXiv:2609.29666v1), and Viaclovsky's two-parameter and logarithmic-transformation families (arXiv:2609.33785v1 and arXiv:2610.39102v1). Smooth recognition uses Zhubr's marked classification of simply connected spin six-manifolds and the oriented surgery theorem recorded by Burklund, Hahn and Senger (arXiv:1910.14116v3). Exact source statements and pages are given in the paper. The standing address for the records and programs is https://github.com/KokunoYumeto/s6-complex-structure-workbench/blob/main/RECORDS.md#paper-iii.",
  "provenance": "Text: AI-authored; none of it was written by a human. The submitter takes responsibility for the veracity of the text.\n\nHow it was produced. GPT-5.6 Sol (OpenAI), in Codex at reasoning effort ultra, produced the working edition on 24 August–9 September 2026. GPT-6 Astra (OpenAI), in ChatGPT Pro mode, carried out the research of 12–16 November 2026, independent re-derivations during 16–18 November, writing during 16–20 November, and publication work during 20–25 November. Its numerical reasoning-effort setting was not separately exposed. GPT-6 Astra Pro (OpenAI), in ChatGPT Pro mode, continued the publication work on 25 November 2026; a numerical reasoning-effort setting was not separately exposed. Claude Fable 5.2 (Anthropic), at effort high and at effort max, and Claude Opus 5.5 (Anthropic), at effort max, performed readings, intake checks and recomputations during 12–20 November 2026. Claude Opus 5.5 at effort max also rewrote Paper V's abstract and introduction on 20 November, read all of Paper I on 21–22 November and adjusted its deposited text and links, read all of Paper II on 24 November, and checked publication material received during 23–25 November. These historical activities retain the specific scopes recorded for them.\n\nHow it was checked. The records associate 1,066 entries with the current statements of this paper: 421 examinations of proof steps, 2 independent re-derivations, 50 computations or formal certificates, 473 readings of proofs and applications, 90 uses of background results without a fault found, and 30 refutation records associated with their corrected statements. These entries belong to 799 recorded evidence groups. Each event is counted once; entries sharing an evidence group retain that common group. One argument or calculation can be associated with several statements and kinds of examination. Each outcome specifies its scope and prior proof exposure.\n\nThe models compared explicit statements, marked geometric data, proposed proofs and computations with the cited primary sources. The work includes derivations written before consulting earlier proofs, independent proofs, exact arithmetic and certified rational bounds. Geometric comparisons retain their coordinate maps, inverse maps, normal orientations and exceptional parameter values. Existing proofs were read in full against their replacements during publication work. These readings record use and rechecking of existing arguments; they do not by themselves add an independent derivation. Each recorded outcome states the passage or computation examined and its prior proof exposure. The rational Rouché certificates verify entire continuation segments, and the finite arithmetic checks have the mathematical purposes stated where they are used.\n\nHuman understanding. No human has checked the mathematics. The paper credits the literature at its supplying statements and pages, and states the exact domains of its own constructions and calculations.\n\nRecords. The standing address for Paper III's source editions, programs, outputs and check records is https://github.com/KokunoYumeto/s6-complex-structure-workbench/blob/main/RECORDS.md#paper-iii. The text, programs and check records are dedicated to the public domain under CC0 1.0 Universal (https://creativecommons.org/publicdomain/zero/1.0/).",
  "aiSystems": [
    {
      "provider": "OpenAI",
      "model": "GPT-6 Astra Pro (ChatGPT Pro mode)",
      "version": null
    },
    {
      "provider": "OpenAI",
      "model": "GPT-6 Astra (ChatGPT Pro mode)",
      "version": null
    },
    {
      "provider": "OpenAI",
      "model": "GPT-5.6 Sol (Codex, reasoning effort ultra)",
      "version": null
    },
    {
      "provider": "Anthropic",
      "model": "Claude Fable 5.2 (effort high and max)",
      "version": null
    },
    {
      "provider": "Anthropic",
      "model": "Claude Opus 5.5 (effort max)",
      "version": null
    },
    {
      "provider": "Python",
      "model": "SymPy and exact integer/rational arithmetic",
      "version": null
    }
  ]
}
''')
SOURCE_GUARDS = json.loads(r'''
{
  "title": "\\title{The $(3,4,\\infty)$ family of complex six-spheres\\\\[.5em]III. Maps and the resulting manifolds}",
  "abstract": "\\begin{abstract}\nWe compute the homotopy classes of three maps associated with the\n$(3,4,\\infty)$ family of complex six-spheres. The torus quotient\nrepresents the element of order two in $\\pi_6(S^3)$, the holomorphic\nmap to $\\mathbb P^1$ is null-homotopic, and the cusp map that keeps\nthe angular coordinate represents the nonzero element of $\\pi_6(S^4)$.\nNormal framings and integral attaching maps give these classes and a\nfinite cell model. For every cyclic universal cover we calculate the\nintegral cohomology ring and the complete smooth classification\ninvariant. We classify the natural section-line sphere fillings over\ntwenty-one elliptic profiles: there are $59$ marked patterns on $50$\ninitial data, with twelve profiles admitting unbounded multiplicity.\nWe also determine weighted smooth types and the homology of every free\nOS49 affine cap, including its additional three-primary torsion. A\nweighted OS45 member has zero refined Pontryagin class, as follows\nfrom an embedded Hopf sphere and its critical-cycle linking number.\nThe local Kummer cover has no smooth compact global extension at\ndegree greater than one; an explicit finite flat normal extension\nhas additional components above the cusp. Finally, moving the zero\nof the line-bundle linearization gives a conifold smoothing\ndiffeomorphic to $S^3\\times S^3$, of algebraic dimension one.\n\\end{abstract}",
  "series": "\\subsection{The series and this paper}\nThe five papers study the periods, complex structures, maps and\ndegenerations of the $(3,4,\\infty)$ torus-fibred family and the\nmanifolds obtained from its elliptic-surface construction. This paper\ndetermines sphere-map classes, integral attachment invariants and\nsmooth types. The constructions include an ordered period lattice,\nfinite affine twists, positive normal circles and a cusp fan. The\ntable lists the principal results and their cross-paper inputs;\nfor Paper~III, the indicated uses are the quotient construction,\nthe section-line family and the return-map identification.\n\\begin{center}\\small\n\\begin{tabularx}{\\textwidth}{@{}lXX@{}}\\toprule\nPaper & Main result & Cross-paper inputs\\\\\\midrule\nI & Periods, moduli, fibre strata and the two ends of the family & ---\\\\\nII & Cotangent obstruction and the sign theorem for degenerations & I, IV\\\\\nIII & Sphere-map classes, integral covers and elliptic smooth types &\nI: \\SeriesRef{mapsI:src:A.2.1}; II: \\SeriesRef{push:src:A.1.2},\n\\SeriesRef{push:src:E.5.2}; IV: \\SeriesRef{iv:correction:P3K.6},\n\\SeriesRef{night:P3K.7}\\\\\nIV & Smooth return maps in $\\Theta_7$ and cusp-fan calculations & I, II, III, V\\\\\nV & Resolved fibre products and the marked rank-six fourfold family & I, III, IV\\\\\n\\bottomrule\\end{tabularx}\\end{center}",
  "methodology": "\\subsection{Methodology}\nThis text is AI-authored. GPT-5.6 Sol (OpenAI), in Codex at\nreasoning effort ultra, produced the working edition during\n24 August--9 September 2026. GPT-6 Astra (OpenAI), in ChatGPT Pro\nmode, carried out the research of 12--16 November, independent\nre-derivations during 16--18 November, writing during 16--20 November,\nand publication work during 20--25 November 2026. Its numerical\nreasoning-effort setting was not separately exposed. GPT-6 Astra Pro\n(OpenAI), in ChatGPT Pro mode, continued the publication work on\n25 November 2026, also without a separately exposed numerical\neffort setting.\n\nClaude Fable 5.2 (Anthropic), at effort high and at effort max,\nand Claude Opus 5.5 (Anthropic), at effort max, performed readings,\nintake checks and recomputations during 12--20 November 2026.\nClaude Opus 5.5 at effort max rewrote Paper~V's abstract and\nintroduction on 20 November, read all of Paper~I on 21--22 November\nand adjusted its deposited text and links, and read all of\nPaper~II on 24 November. It also checked the publication material\nreceived during 23--25 November, including arithmetic and\nsource-scope questions.\n\nThe models worked from explicit statements, marked geometric data\nand primary sources. Proposed proofs and computations were passed\nbetween them for comparison; disagreements were resolved at the\naffected statement, map or parameter range. The checks include\nderivations written before consulting earlier proofs, independent\nproofs, exact arithmetic, certified rational bounds and comparison with\nthe cited literature. Each computation is described mathematically\nwhere it is used, and the programs are listed at the end of the paper.\nDuring the publication work, existing proofs were reread in full\nagainst their replacements, with coordinate maps, inverse maps and\nexceptional parameters checked explicitly. Those readings record\ntheir use and rechecking of existing arguments. The records state\nthe scope of each check and preserve every corrected assertion.\nThe records associate 1,066 entries with the current statements of this\npaper: 421 examinations of proof steps, 2 independent re-derivations, 50\ncomputations or formal certificates, 473 readings of proofs and\napplications, 90 uses of background results without a fault found, and 30\nrefutation records associated with their corrected statements. These entries\nbelong to 799 recorded evidence groups. Each event is counted once; entries\nsharing an evidence group retain that common group. One argument or\ncalculation can be associated with several statements and kinds of\nexamination. Each outcome specifies its scope and prior proof exposure.\n\nNo human has checked the mathematics.\n\nWe dedicate this text to the public domain under\n\\href{https://creativecommons.org/publicdomain/zero/1.0/}{CC0 1.0 Universal}.\nThe standing address for statement checks, provenance and programs\nis the \\href{\\SsixPublishRecords}{records page for Paper~III}.\nThe repository commit is \\texttt{\\SsixRepositoryCommit}.",
  "main:A": "\\label{series:III:A}",
  "status:A": "\\textit{Literature status.} New relative realization for the quotient\nof \\cite[Remark~8.3, pp.~22--23]{E26}.",
  "known:A": "A & New relative realization for Engel's quotient\n\\cite[Remark~8.3, pp.~22--23]{E26}.\\\\",
  "main:B": "\\label{series:III:B}",
  "status:B": "\\textit{Literature status.} New computations for these maps, using\n\\cite[Theorem~4.1 and Corollaries~4.2--4.3, pp.~76--77]{mapsToda52}\nand \\cite[Theorem~4.14, p.~423]{mapsAPS2}.",
  "known:B": "B & New map classes; unstable suspension and the real Adams\nformula are \\cite[Theorem~4.1, pp.~76--77]{mapsToda52} and\n\\cite[Theorem~4.14, p.~423]{mapsAPS2}.\\\\",
  "main:C": "\\label{series:III:C}",
  "status:C": "\\textit{Literature status.} New framing and cell calculations for\nthe sphere construction of \\cite[Theorem~4.1, p.~12]{E26}.",
  "known:C": "C & New cusp framing and marked cell presentation;\nthe sphere construction is \\cite[Theorem~4.1, p.~12]{E26}.\\\\",
  "main:D": "\\label{series:III:D}",
  "status:D": "\\textit{Literature status.} New obstruction and completion for this\ncusp, using the covering classification in\n\\cite[Theorem~1.38, pp.~67--68]{Hatcher2002}.",
  "known:D": "D & New full-fan obstruction and normal extension;\ncovering classification is \\cite[Theorem~1.38, pp.~67--68]{Hatcher2002}.\\\\",
  "main:E": "\\label{series:III:E}",
  "status:E": "\\textit{Literature status.} New cover invariants for the family of\n\\cite[Theorems~7.17 and~7.22, pp.~57, 60]{AC26}, recognized by\n\\cite[Theorem~3, p.~795; \\S4.1, p.~809]{manZhubr75}.",
  "known:E": "E & New complete cover invariant; marked smooth recognition uses\n\\cite[Theorems~3 and~5, pp.~795--796; \\S4.1, p.~809]{manZhubr75}.\\\\",
  "main:F": "\\label{series:III:F}",
  "status:F": "\\textit{Literature status.} New classifications for these explicit\ndata within the section-line construction of\n\\cite[Remark~8.5, p.~24]{E26}.",
  "known:F": "F & New natural-line and weighted classifications within\n\\cite[Remark~8.5, p.~24]{E26}.\\\\",
  "main:G": "\\label{series:III:G}",
  "status:G": "\\textit{Literature status.} New moving-zero family from\n\\cite[Proposition~2.4 and Propositions~2.7--2.8, pp.~5--7]{E26},\nwith smooth recognition by \\cite[Theorem~2.6, p.~8]{BHS19}.",
  "known:G": "G & New moving-zero family and its smooth type; the surgery\nclassification is \\cite[Theorem~2.6, p.~8]{BHS19}.\\\\",
  "series:2": "I & Periods, moduli, fibre strata and the two ends of the family & ---\\\\",
  "series:3": "II & Cotangent obstruction and the sign theorem for degenerations & I, IV\\\\",
  "series:4": "III & Sphere-map classes, integral covers and elliptic smooth types &\nI: \\SeriesRef{mapsI:src:A.2.1}; II: \\SeriesRef{push:src:A.1.2},\n\\SeriesRef{push:src:E.5.2}; IV: \\SeriesRef{iv:correction:P3K.6},\n\\SeriesRef{night:P3K.7}\\\\",
  "series:6": "IV & Smooth return maps in $\\Theta_7$ and cusp-fan calculations & I, II, III, V\\\\",
  "series:7": "V & Resolved fibre products and the marked rank-six fourfold family & I, III, IV\\\\",
  "series:1": "\\subsection{The series and this paper}\nThe five papers study the periods, complex structures, maps and\ndegenerations of the $(3,4,\\infty)$ torus-fibred family and the\nmanifolds obtained from its elliptic-surface construction. This paper\ndetermines sphere-map classes, integral attachment invariants and\nsmooth types. The constructions include an ordered period lattice,\nfinite affine twists, positive normal circles and a cusp fan. The\ntable lists the principal results and their cross-paper inputs;\nfor Paper~III, the indicated uses are the quotient construction,\nthe section-line family and the return-map identification.",
  "series:5": "III & Sphere-map classes, integral covers and elliptic smooth types &\nI: \\SeriesRef{mapsI:src:A.2.1}; II: \\SeriesRef{push:src:A.1.2},\n\\SeriesRef{push:src:E.5.2}; IV: \\SeriesRef{iv:correction:P3K.6},\n\\SeriesRef{night:P3K.7}\\\\",
  "production": "\\subsection{Methodology}\nThis text is AI-authored. GPT-5.6 Sol (OpenAI), in Codex at\nreasoning effort ultra, produced the working edition during\n24 August--9 September 2026. GPT-6 Astra (OpenAI), in ChatGPT Pro\nmode, carried out the research of 12--16 November, independent\nre-derivations during 16--18 November, writing during 16--20 November,\nand publication work during 20--25 November 2026. Its numerical\nreasoning-effort setting was not separately exposed. GPT-6 Astra Pro\n(OpenAI), in ChatGPT Pro mode, continued the publication work on\n25 November 2026, also without a separately exposed numerical\neffort setting.",
  "other_models": "Claude Fable 5.2 (Anthropic), at effort high and at effort max,\nand Claude Opus 5.5 (Anthropic), at effort max, performed readings,\nintake checks and recomputations during 12--20 November 2026.\nClaude Opus 5.5 at effort max rewrote Paper~V's abstract and\nintroduction on 20 November, read all of Paper~I on 21--22 November\nand adjusted its deposited text and links, and read all of\nPaper~II on 24 November. It also checked the publication material\nreceived during 23--25 November, including arithmetic and\nsource-scope questions.",
  "methods": "The models worked from explicit statements, marked geometric data\nand primary sources. Proposed proofs and computations were passed\nbetween them for comparison; disagreements were resolved at the\naffected statement, map or parameter range. The checks include\nderivations written before consulting earlier proofs, independent\nproofs, exact arithmetic, certified rational bounds and comparison with\nthe cited literature. Each computation is described mathematically\nwhere it is used, and the programs are listed at the end of the paper.\nDuring the publication work, existing proofs were reread in full\nagainst their replacements, with coordinate maps, inverse maps and\nexceptional parameters checked explicitly. Those readings record\ntheir use and rechecking of existing arguments. The records state\nthe scope of each check and preserve every corrected assertion.",
  "counts": "The records associate 1,066 entries with the current statements of this\npaper: 421 examinations of proof steps, 2 independent re-derivations, 50\ncomputations or formal certificates, 473 readings of proofs and\napplications, 90 uses of background results without a fault found, and 30\nrefutation records associated with their corrected statements. These entries\nbelong to 799 recorded evidence groups. Each event is counted once; entries\nsharing an evidence group retain that common group. One argument or\ncalculation can be associated with several statements and kinds of\nexamination. Each outcome specifies its scope and prior proof exposure.",
  "human": "No human has checked the mathematics.",
  "licence": "We dedicate this text to the public domain under\n\\href{https://creativecommons.org/publicdomain/zero/1.0/}{CC0 1.0 Universal}.",
  "records": "The standing address for statement checks, provenance and programs\nis the \\href{\\SsixPublishRecords}{records page for Paper~III}.\nThe repository commit is \\texttt{\\SsixRepositoryCommit}.",
  "bib:manYang26": "\\bibitem[Yang(2026)]{manYang26}\nXiufan Yang.\n\\newblock Compact complex threefolds fibred by two-dimensional complex tori.\n\\newblock arXiv:2609.29666v1, 13 September 2026.\n\\newblock \\url{https://arxiv.org/abs/2609.29666v1}.",
  "bib:manViaclovskyTwo26": "\\bibitem[Viaclovsky(2026{\\natexlab{b}})]{manViaclovskyTwo26}\nJeff Viaclovsky.\n\\newblock A two-parameter family of complex structures on $S^6$.\n\\newblock arXiv:2609.33785v1, 27 September 2026.\n\\newblock \\url{https://arxiv.org/abs/2609.33785v1}.",
  "bib:manViaclovskyLogs26": "\\bibitem[Viaclovsky(2026{\\natexlab{a}})]{manViaclovskyLogs26}\nJeff Viaclovsky.\n\\newblock Logarithmic transformations on the six-sphere.\n\\newblock arXiv:2610.39102v1, 29 October 2026.\n\\newblock \\url{https://arxiv.org/abs/2610.39102v1}."
}
''')
CLAIMS = json.loads(r'''
[
  {
    "id": "III-C8-AB01",
    "review_heading": "## Abstract: every mathematical claim",
    "review_index": 0,
    "claim": "AB1. The torus quotient represents the order-two element of pi6(S3).",
    "records": "FR B; FE B; `maps:src:B.1.1` and `maps:src:B.1.2` fix the admissible sphere member, based target, ordered normal frame and 6 nu-prime. The current root framing review retains the complete proof.",
    "recomputation": "The equality 6 nu-prime = eta3 eta4 eta5 and stabilization 12 nu are the admitted homotopy/framing calculation, with real Adams value 1/2. No event-count inference is used.",
    "primary": "Toda, Theorem 4.1 and Corollaries 4.2–4.3, printed 76–77; APS II, Theorem 4.14, printed 423, were opened in FR.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "abstract"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/abstract; S6_SERIES_PUBLISH_deposit_fields.md > Paper III > Abstract; descriptive Comments where applicable"
  },
  {
    "id": "III-C8-AB02",
    "review_heading": "## Abstract: every mathematical claim",
    "review_index": 1,
    "claim": "AB2. The holomorphic map to P1 is null-homotopic.",
    "records": "FR B and the whole `base_map.tex` proof, `maps:src:B.2.1`. Root applied the all-admissible sphere-member scope clarification on 25 November at 20:36:05 UTC.",
    "recomputation": "The actual factorization is M f = [a^3:b^4] homotopic to eta2 P3,4 G. M and its inverse, the compatible divisor frames and degree twelve are retained. No identification of G with the quotient map is assumed.",
    "primary": "The marked family and the divisor multiplicities belong to the cited family construction; the null-homotopy is proved in III. The covering/sphere facts have their body citations.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "abstract"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/abstract; S6_SERIES_PUBLISH_deposit_fields.md > Paper III > Abstract; descriptive Comments where applicable"
  },
  {
    "id": "III-C8-AB03",
    "review_heading": "## Abstract: every mathematical claim",
    "review_index": 2,
    "claim": "AB3. The retained-angle cusp map is nonzero in pi6(S4).",
    "records": "FR C; FE C; `maps:src:B.3.1` with the full defined retained-angle datum. The current retained-angle proof supplies all original and defined admissible sphere members.",
    "recomputation": "The regular two-torus has the explicit Lie framing, Arf value one and class eta4 eta5. The cell-count datum below is separately fixed and does not enlarge this map's domain.",
    "primary": "Engel, Theorem 4.1, p.12 supplies the source construction; Johnson, Theorem 3A, p.371, is supported by the wholly read predecessor source record; Debray–Gunningham Theorems 3.2/3.6 and Remark 3.3, preprint p.6, were newly opened in BR.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "abstract"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/abstract; S6_SERIES_PUBLISH_deposit_fields.md > Paper III > Abstract; descriptive Comments where applicable"
  },
  {
    "id": "III-C8-AB04",
    "review_heading": "## Abstract: every mathematical claim",
    "review_index": 3,
    "claim": "AB4. Normal framings and integral attachments give a finite cell model.",
    "records": "FR C and the bounded cell premises stated there; formal owners `maps:src:B.5.1`–`maps:src:B.5.2`. The numerical tuple belongs to the p=-1, zero-cusp-drift three-filling datum.",
    "recomputation": "The exact counts (5,20,45,56,42,17,3), two killed circle generators, attaching maps and alternating sum two remain in the body. This review does not rerun their mathematical program.",
    "primary": "Waldhausen, Theorem 6.1, p.77 was opened at the actual boundary-relative product-collar application; the cell maps and sphere conclusion are III's proof.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "abstract"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/abstract; S6_SERIES_PUBLISH_deposit_fields.md > Paper III > Abstract; descriptive Comments where applicable"
  },
  {
    "id": "III-C8-AB05",
    "review_heading": "## Abstract: every mathematical claim",
    "review_index": 4,
    "claim": "AB5. Every cyclic universal cover has its integral ring and complete smooth invariant calculated.",
    "records": "FR E; current full Q146/K9 and the recorded bounded homology/product inputs. `maps:src:D.1.4`, `.6`, `.8`–`.11`. The admissible domain is d=abs(p), coprime to six.",
    "recomputation": "The group, Cartan products, zero integral cubic, finite coordinates Cij,-12,0 and all zero coordinates determine the complete invariant. The actual constructed Q145 model realizes it.",
    "primary": "AC26, Theorems 7.17/7.22, pp.57,60; Zhubr English Theorems 3/5, pp.795–796 and §4.1 p.809, were opened at their actual application scopes.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "abstract"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/abstract; S6_SERIES_PUBLISH_deposit_fields.md > Paper III > Abstract; descriptive Comments where applicable"
  },
  {
    "id": "III-C8-AB06",
    "review_heading": "## Abstract: every mathematical claim",
    "review_index": 5,
    "claim": "AB6. There are 59 natural sphere patterns on 50 initial rows over 21 profiles; 12 have unbounded multiplicity.",
    "records": "FR F(a); full L3 proof and the completed spheres review; `maps:src:D.2.28`, HY3–HY5. Natural section line, original/Mumford fillings, allowed affine twists and all stated logarithms are explicit.",
    "recomputation": "The exact 59/50 and 12/4/5 conclusions belong to the proved cap classification and already-run catalogue. LG's admitted history comparison gives exact maps from historical tuples; enumeration does not independently prove the inherited geometry formulas.",
    "primary": "Engel, Remark 8.5 p.24, supplies the wider degree-zero-line setting. The natural-line finite catalogue and integral all-order criteria belong to III's named proofs.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "abstract"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/abstract; S6_SERIES_PUBLISH_deposit_fields.md > Paper III > Abstract; descriptive Comments where applicable"
  },
  {
    "id": "III-C8-AB07",
    "review_heading": "## Abstract: every mathematical claim",
    "review_index": 6,
    "claim": "AB7. Weighted smooth types and every free OS49 affine cap, including extra three-primary torsion, are determined.",
    "records": "FR F(b),(d); LP's full positive-weight domain; SA/SB's full free affine domain including n=0. Owners `maps:src:D.2.48`, `night:P3F.33` and `night:P3F.34`.",
    "recomputation": "For nonzero n, g=gcd(3k,n,3d) lies in {1,3}; (9,3,1) gives g=3 in the full free sector. The coprime sector has g=1. The n=0 free and torsion summands remain explicit.",
    "primary": "Engel Remark 8.5 p.24 gives the construction setting; the complete marked invariant and signed cap maps are the admitted III calculations. No new SB refutation is asserted.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "abstract"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/abstract; S6_SERIES_PUBLISH_deposit_fields.md > Paper III > Abstract; descriptive Comments where applicable"
  },
  {
    "id": "III-C8-AB08",
    "review_heading": "## Abstract: every mathematical claim",
    "review_index": 7,
    "claim": "AB8. The specified OS45 member has refined Pontryagin class zero, from an embedded Hopf sphere and critical linking.",
    "records": "FR F(c); full c8 02LV comparison and root admission; `maps:src:D.2.53`. The exact datum is P=2G,Q=8G, the displayed weights, triangular Mumford caps and ordinary clutch e=1.",
    "recomputation": "The actual source-line sphere, reference parity 1 and complete critical-cycle linking -1 give zero. The source graph sphere is retained with its explicit maps; equality with a different embedding is not inferred.",
    "primary": "The Zhubr/Brown/Kaplan framed-construction sources retain the exact c7/c8 source-check scopes in BR and the LV records. This is the particular geometric evaluation proved in III.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "abstract"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/abstract; S6_SERIES_PUBLISH_deposit_fields.md > Paper III > Abstract; descriptive Comments where applicable"
  },
  {
    "id": "III-C8-AB09",
    "review_heading": "## Abstract: every mathematical claim",
    "review_index": 8,
    "claim": "AB9. No smooth compact global extension of the local Kummer map exists for N>1; a finite flat normal completion has extra cusp components.",
    "records": "FR D and whole K2–K6 unit, `maps:src:C.1.1`–`.5`. Absolute kappaN, relative QN and global YN→X keep their individual domains.",
    "recomputation": "Degrees are respectively N3, N2 and N2 times abs(GN). The free semigroup basis proves local flatness of the normal construction; the global orbit/group index gives the global degree. N=1 is retained as the identity endpoint.",
    "primary": "Hatcher Theorem 1.38 pp.67–68 was opened with inverse lifts and basepoint transport. The full-fan, monodromy and completion arguments are III's established proofs.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "abstract"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/abstract; S6_SERIES_PUBLISH_deposit_fields.md > Paper III > Abstract; descriptive Comments where applicable"
  },
  {
    "id": "III-C8-AB10",
    "review_heading": "## Abstract: every mathematical claim",
    "review_index": 9,
    "claim": "AB10. Moving the line-linearization zero gives an algebraic-dimension-one conifold smoothing on S3×S3.",
    "records": "FR G and the complete conifold publication review; `maps:src:D.3.1`–`.3`. The source surface, directed line, sphere twists, sufficiently small fixed nonzero u and punctured s-disc are retained.",
    "recomputation": "The literal equation xy=u(zv-s), primitive boundary map, skew middle form, normal invariant and actual quadric/TS3 map supply the oriented smooth type. No rank-only recognition is used.",
    "primary": "Engel Proposition 2.4 and Propositions 2.7–2.8, pp.5–7; BHS v3 Recollection 2.2/Theorem 2.6 pp.7–8, were opened.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "abstract"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/abstract; S6_SERIES_PUBLISH_deposit_fields.md > Paper III > Abstract; descriptive Comments where applicable"
  },
  {
    "id": "III-C8-ST01",
    "review_heading": "## A–G status sentences and every §1.4 row",
    "review_index": 0,
    "claim": "A: new relative realization for Engel's quotient.",
    "records": "FR A and the complete J3 proof preserve original sphere members, outer collar, designated solid torus and all twelve locally inserted classes.",
    "recomputation": "No check total establishes novelty; the twelve classes come from the actual pi6(S3) action and the explicit supported product homotopy.",
    "primary": "Engel Remark 8.3 pp.22–23 was opened. The paper supplies the stated relative realization and retains the precise source relationship. The bounded search record supports no broader priority assertion.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "main:A",
      "status:A",
      "known:A"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/comments; Paper III > Comments gives descriptive contributions without an additional priority claim"
  },
  {
    "id": "III-C8-ST02",
    "review_heading": "## A–G status sentences and every §1.4 row",
    "review_index": 1,
    "claim": "B: new computations of these quotient and base-map classes.",
    "records": "FR B, J4/J5/J6, and the exact repaired frame/factorization correspondence.",
    "recomputation": "The event selector may count examinations attached to these owners; it cannot turn the old incorrect factorization into a proved map. Only the current explicit correspondence is used.",
    "primary": "Toda Theorem 4.1/Corollaries 4.2–4.3 pp.76–77 and APS II Theorem 4.14 p.423 supply the classical homotopy and real Adams inputs. III computes their values on its marked maps.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "main:B",
      "status:B",
      "known:B"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/comments; Paper III > Comments gives descriptive contributions without an additional priority claim"
  },
  {
    "id": "III-C8-ST03",
    "review_heading": "## A–G status sentences and every §1.4 row",
    "review_index": 2,
    "claim": "C: new cusp framing and marked cell calculation.",
    "records": "FR C and the current retained-angle/cell owners keep the two precise domains.",
    "recomputation": "Arf, frame and attachment computations retain their admitted scopes. The count program is independent of the mathematical cell enumeration.",
    "primary": "Engel Theorem 4.1 p.12 supplies the sphere construction. The actual ordered-frame contraction and marked cell model are III's displayed arguments.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "main:C",
      "status:C",
      "known:C"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/comments; Paper III > Comments gives descriptive contributions without an additional priority claim"
  },
  {
    "id": "III-C8-ST04",
    "review_heading": "## A–G status sentences and every §1.4 row",
    "review_index": 3,
    "claim": "D: new full-fan obstruction and normal extension.",
    "records": "FR D; full local Kummer proof and current normal extension.",
    "recomputation": "N3/N2/N2 abs(GN), monodromy orbit and N=1 tests are proof conclusions, not event totals.",
    "primary": "Hatcher Theorem 1.38 pp.67–68 supplies covering correspondence. III supplies the fan/lattice obstruction and explicitly defined completion for the fixed cusp.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "main:D",
      "status:D",
      "known:D"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/comments; Paper III > Comments gives descriptive contributions without an additional priority claim"
  },
  {
    "id": "III-C8-ST05",
    "review_heading": "## A–G status sentences and every §1.4 row",
    "review_index": 4,
    "claim": "E: new complete invariant of the cyclic covers.",
    "records": "FR E; Q145/Q146 and complete K9. The full zero-coordinate data and b3=0 construction are retained.",
    "recomputation": "No summary of ordinary p1 or group orders replaces the marked invariant. The selector preserves the exact retained historical statement associations under current owners.",
    "primary": "AC26 Theorems 7.17/7.22 pp.57,60 supply the family; Zhubr Theorems 3/5 pp.795–796 and §4.1 p.809 supply recognition. The English rank clauses concern H2.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "main:E",
      "status:E",
      "known:E"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/comments; Paper III > Comments gives descriptive contributions without an additional priority claim"
  },
  {
    "id": "III-C8-ST06",
    "review_heading": "## A–G status sentences and every §1.4 row",
    "review_index": 5,
    "claim": "F: new natural-line and weighted classifications for the explicit data.",
    "records": "FR F; L3, LP, LV, SA/SB. The full natural-line and weighted/free-cap scopes remain as stated.",
    "recomputation": "59/50, 12/4/5 and the weighted/OS49 formulas are the already-established mathematical outputs. The final check totals enumerate the associated recorded work.",
    "primary": "Engel Remark 8.5 p.24 permits arbitrary fibrewise degree-zero lines. III's exact classified sector is the one stated in F; broader remaining questions stay in the final part.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "main:F",
      "status:F",
      "known:F"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/comments; Paper III > Comments gives descriptive contributions without an additional priority claim"
  },
  {
    "id": "III-C8-ST07",
    "review_heading": "## A–G status sentences and every §1.4 row",
    "review_index": 6,
    "claim": "G: new moving-zero family and its smooth type.",
    "records": "FR G and full conifold review preserve properness/flatness over both bases, the marked source and the punctured parameter range.",
    "recomputation": "The primitive boundary and normal-invariant proof owns S3×S3 recognition; no numerical test is substituted for it.",
    "primary": "Engel Propositions 2.4/2.7/2.8 pp.5–7 are the construction inputs; BHS v3 Theorem 2.6 p.8 is the oriented surgery-recognition input.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "main:G",
      "status:G",
      "known:G"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/comments; Paper III > Comments gives descriptive contributions without an additional priority claim"
  },
  {
    "id": "III-C8-S01",
    "review_heading": "## §1.1: series paragraph and all table entries",
    "review_index": 0,
    "claim": "The series has five papers about the periods, complex structures, maps, degenerations and elliptic-surface outputs.",
    "records": "The controlling prompt and attached publication/deposit records define this series; III's current paragraph agrees with its actual body.",
    "recomputation": "Five listed rows I–V, with one III row. This is documentary correspondence, not a check-event count.",
    "primary": "The individual other-paper manuscripts are deliberately left for the authorized joint phase.",
    "gate_keys": [
      "pdf",
      "joint"
    ],
    "source_keys": [
      "series:1"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/comments (five-paper series sentence); other-paper result/input table rows are not exported into III deposit claims"
  },
  {
    "id": "III-C8-S02",
    "review_heading": "## §1.1: series paragraph and all table entries",
    "review_index": 1,
    "claim": "I: periods, moduli, fibre strata and two ends; input cell is an em dash.",
    "records": "Retained from the series table and historical publication record.",
    "recomputation": "No input-absence theorem is inferred from III's citation search.",
    "primary": "The complete Paper I table/claim comparison remains root's joint gate; no rereading of I is claimed here.",
    "gate_keys": [
      "pdf",
      "joint"
    ],
    "source_keys": [
      "series:2"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/comments (five-paper series sentence); other-paper result/input table rows are not exported into III deposit claims",
    "status": "open: joint-source provenance verification",
    "resolution": "The recorded other-paper entry is preserved without a new proof reading, dependency census or absence claim; joint verification remains open."
  },
  {
    "id": "III-C8-S03",
    "review_heading": "## §1.1: series paragraph and all table entries",
    "review_index": 2,
    "claim": "II: cotangent obstruction and sign theorem; inputs I and IV.",
    "records": "Retained from the prescribed existing table and attached II reading record.",
    "recomputation": "No dependency census of II is made in this lane.",
    "primary": "Root's joint table verification remains open here; this is not a new II source or proof review.",
    "gate_keys": [
      "pdf",
      "joint"
    ],
    "source_keys": [
      "series:3"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/comments (five-paper series sentence); other-paper result/input table rows are not exported into III deposit claims",
    "status": "open: joint-source provenance verification",
    "resolution": "The recorded other-paper entry is preserved without a new proof reading, dependency census or absence claim; joint verification remains open."
  },
  {
    "id": "III-C8-S04",
    "review_heading": "## §1.1: series paragraph and all table entries",
    "review_index": 3,
    "claim": "III: sphere-map classes, integral covers and elliptic smooth types.",
    "records": "A–G and the formal body owners above supply each phrase.",
    "recomputation": "Exact wording is consistent with the scoped abstract, main statements and final open problems.",
    "primary": "III's current admitted mathematical proofs are the primary manuscript evidence.",
    "gate_keys": [
      "pdf",
      "joint"
    ],
    "source_keys": [
      "series:4"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/comments (five-paper series sentence); other-paper result/input table rows are not exported into III deposit claims"
  },
  {
    "id": "III-C8-S05",
    "review_heading": "## §1.1: series paragraph and all table entries",
    "review_index": 4,
    "claim": "III uses I, II and IV through the positively named inputs.",
    "records": "`mapsI:src:A.2.1`; `push:src:A.1.2`, `push:src:E.5.2`; `iv:correction:P3K.6`, `night:P3K.7` are the explicit table labels. FR records the current III use and the OS49 return comparison.",
    "recomputation": "Final SeriesRef expansion must use the actual posted/retained statement numbers and tags. A positive input list supplies no assertion that V is unused.",
    "primary": "The supplying cross-paper statements remain their already-admitted exact owners; no other-paper proof is newly read in this review.",
    "gate_keys": [
      "pdf",
      "joint"
    ],
    "source_keys": [
      "series:5"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/comments (five-paper series sentence); other-paper result/input table rows are not exported into III deposit claims"
  },
  {
    "id": "III-C8-S06",
    "review_heading": "## §1.1: series paragraph and all table entries",
    "review_index": 5,
    "claim": "IV: smooth return maps in Theta7 and cusp-fan calculations; inputs I,II,III,V.",
    "records": "Retained from the current series table and attached work history.",
    "recomputation": "No IV dependency census is performed.",
    "primary": "Complete IV verification and common table agreement are root's later joint work.",
    "gate_keys": [
      "pdf",
      "joint"
    ],
    "source_keys": [
      "series:6"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/comments (five-paper series sentence); other-paper result/input table rows are not exported into III deposit claims",
    "status": "open: joint-source provenance verification",
    "resolution": "The recorded other-paper entry is preserved without a new proof reading, dependency census or absence claim; joint verification remains open."
  },
  {
    "id": "III-C8-S07",
    "review_heading": "## §1.1: series paragraph and all table entries",
    "review_index": 6,
    "claim": "V: resolved fibre products and marked rank-six fourfold family; inputs I,III,IV.",
    "records": "The authorized V v3 metadata gives its actual construction/recognition scope; the table retains the recorded entry.",
    "recomputation": "No numerical count or absence of II dependency is asserted from this row. The prompt explicitly records V's indirect II chain.",
    "primary": "No V manuscript is opened. The joint phase must reconcile the exact direct/indirect table convention across the five papers.",
    "gate_keys": [
      "pdf",
      "joint"
    ],
    "source_keys": [
      "series:7"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/comments (five-paper series sentence); other-paper result/input table rows are not exported into III deposit claims",
    "status": "open: joint-source provenance verification",
    "resolution": "The recorded other-paper entry is preserved without a new proof reading, dependency census or absence claim; joint verification remains open."
  },
  {
    "id": "III-C8-P01",
    "review_heading": "## §1.5: every historical and checking claim",
    "review_index": 0,
    "claim": "AI-authored text; no human authored the text.",
    "records": "The controlling prompt and supplied V field schema expressly require this authorship mode; current III says AI-authored.",
    "recomputation": "Draft `authorshipMode` is exactly `no-human-author-claimed`; required provenance opening is copied exactly.",
    "primary": "This is the submitter's supplied production declaration, not an inference about all unobserved human activity.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "production"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/authorshipMode and #/provenance; S6_SERIES_PUBLISH_deposit_fields.md > Paper III > Provenance and Subjects and classification"
  },
  {
    "id": "III-C8-P02",
    "review_heading": "## §1.5: every historical and checking claim",
    "review_index": 1,
    "claim": "GPT-5.6 Sol, OpenAI, Codex, effort ultra, working edition 24 August–9 September 2026.",
    "records": "Prompt §4.1 and the attached GRIND III deposit paragraph record these dates and effort.",
    "recomputation": "The current III date span and name agree literally; it is not reassigned to the current model.",
    "primary": "Supplied historical record is the documentary authority.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "production"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/provenance; S6_SERIES_PUBLISH_deposit_fields.md > Paper III > Provenance; aiSystems where applicable"
  },
  {
    "id": "III-C8-P03",
    "review_heading": "## §1.5: every historical and checking claim",
    "review_index": 2,
    "claim": "Historical GPT-6 Astra, OpenAI, ChatGPT Pro, research 12–16 November.",
    "records": "Prompt §4.1; `../S6_GRIND_5_research_runs_tex/returns/S6_04_MAPS_MANIFOLDS/S6_04_MAPS_MANIFOLDS_report.md` records the 15–16 November III research and explicit model attribution.",
    "recomputation": "Current III uses 12–16 November for the series research span. The bounded III report supplies actual activity within it.",
    "primary": "Its lines 1–35 were read; no complete re-verification of the historical report is inferred.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "production"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/provenance; S6_SERIES_PUBLISH_deposit_fields.md > Paper III > Provenance; aiSystems where applicable"
  },
  {
    "id": "III-C8-P04",
    "review_heading": "## §1.5: every historical and checking claim",
    "review_index": 3,
    "claim": "Historical Astra independent re-derivations 16–18 November.",
    "records": "Prompt §4.1 and `../S6_GRIND_3_night_run_cp36/S6_06_BLIND_report.md` provenance at line 232/date at 246. The retained exposure exclusions remain explicit.",
    "recomputation": "The final selector preserves the actual event types and scope; a historical run name does not automatically make every row independent.",
    "primary": "This review read the specific attribution/exposure statement and date, not the entire long audit or its proofs.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "production"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/provenance; S6_SERIES_PUBLISH_deposit_fields.md > Paper III > Provenance; aiSystems where applicable"
  },
  {
    "id": "III-C8-P05",
    "review_heading": "## §1.5: every historical and checking claim",
    "review_index": 4,
    "claim": "Historical Astra writing 16–20 November; publication work 20–25 November.",
    "records": "Prompt §4.1 gives the writing range and every publication continuation; the attached GRIND report records its 20 November checkpoint.",
    "recomputation": "Current III condenses the listed publication continuations into the same inclusive date span. No current-Pro event is relabelled as historical Astra.",
    "primary": "Prompt and recorded production chronology are the documentary owners.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "production"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/provenance; S6_SERIES_PUBLISH_deposit_fields.md > Paper III > Provenance; aiSystems where applicable"
  },
  {
    "id": "III-C8-P06",
    "review_heading": "## §1.5: every historical and checking claim",
    "review_index": 5,
    "claim": "Numerical effort not separately exposed for historical Astra.",
    "records": "Current methodology follows the supplied historical schema's distinction between ChatGPT Pro mode and an unexposed numerical setting.",
    "recomputation": "The older GRIND shorthand “effort Pro” is not converted into an invented numerical value.",
    "primary": "No independent interface setting for those past sessions is claimed by the current reviewer.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "production"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/provenance; S6_SERIES_PUBLISH_deposit_fields.md > Paper III > Provenance; aiSystems where applicable"
  },
  {
    "id": "III-C8-P07",
    "review_heading": "## §1.5: every historical and checking claim",
    "review_index": 6,
    "claim": "GPT-6 Astra Pro, OpenAI, ChatGPT Pro, publication work on 25 November, numerical effort not separately exposed.",
    "records": "Current session attribution and all c8 local events identify this model exactly.",
    "recomputation": "The distinct `aiSystems` entry and chronology preserve “Astra Pro”; the historical Astra name is not substituted.",
    "primary": "Actual current session identity is the documentary authority.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "production"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/provenance; S6_SERIES_PUBLISH_deposit_fields.md > Paper III > Provenance; aiSystems where applicable"
  },
  {
    "id": "III-C8-P08",
    "review_heading": "## §1.5: every historical and checking claim",
    "review_index": 7,
    "claim": "Claude Fable 5.2 at high/max and Opus 5.5 at max: readings/intakes/checks/recomputations 12–20 November.",
    "records": "Prompt §4.1; attached provenance schema and intakes preserve both models and effort settings.",
    "recomputation": "The final event counts select admitted III subjects and their actual event rows.",
    "primary": "The historical series credit is retained at its stated dates, without asserting a new whole reading of every intake.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "other_models"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/provenance; S6_SERIES_PUBLISH_deposit_fields.md > Paper III > Provenance; aiSystems where applicable"
  },
  {
    "id": "III-C8-P09",
    "review_heading": "## §1.5: every historical and checking claim",
    "review_index": 8,
    "claim": "Opus rewrote V's abstract and introduction on 20 November.",
    "records": "Prompt §4.1 and the authorized V v3 metadata explicitly assign that wording.",
    "recomputation": "The III credit identifies Paper V; no III authorship contribution is inferred from it.",
    "primary": "V's manuscript was not read or edited here.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "other_models"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/provenance; S6_SERIES_PUBLISH_deposit_fields.md > Paper III > Provenance; aiSystems where applicable"
  },
  {
    "id": "III-C8-P10",
    "review_heading": "## §1.5: every historical and checking claim",
    "review_index": 9,
    "claim": "Opus read all of I on 21–22 November and adjusted its deposited text/links.",
    "records": "`../CLAUDE_READING_LOG_PAPER_I.md` title, opening and actual completion entry at line 36; prompt §§0.2/4.1.",
    "recomputation": "Completion is recorded at 22 November 00:35 UTC; the header begins 21 November. The exact changes remain attributed to that log/prompt.",
    "primary": "Only the provenance portions of this log were newly read here. The III sentence reports that prior reading; it is not new I proof credit.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "other_models"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/provenance; S6_SERIES_PUBLISH_deposit_fields.md > Paper III > Provenance; aiSystems where applicable"
  },
  {
    "id": "III-C8-P11",
    "review_heading": "## §1.5: every historical and checking claim",
    "review_index": 10,
    "claim": "Opus read all of II on 24 November.",
    "records": "`../CLAUDE_READING_LOG_PAPER_II.md` title and opening state 14:30–16:57 UTC on that date; prompt §4.1.",
    "recomputation": "Current III date agrees. Page totals in that historical log are not inserted as current III counts.",
    "primary": "No II manuscript was reopened.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "other_models"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/provenance; S6_SERIES_PUBLISH_deposit_fields.md > Paper III > Provenance; aiSystems where applicable"
  },
  {
    "id": "III-C8-P12",
    "review_heading": "## §1.5: every historical and checking claim",
    "review_index": 11,
    "claim": "Opus checked received publication material on 23–25 November, including arithmetic and source scope.",
    "records": "The four exact attached intake files named below contain the dated model/effort and bounded outcomes.",
    "recomputation": "These records have both checked and expressly unchecked clauses. Final selection must not promote the latter into checks.",
    "primary": "Headers and the bounded III examples were read; the source scopes stay with the actual intake rows.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "other_models"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/provenance; S6_SERIES_PUBLISH_deposit_fields.md > Paper III > Provenance; aiSystems where applicable",
    "evidence": "../CLAUDE_INTAKE_CHECK_EVENTS_20261123.tsv; ../CLAUDE_INTAKE_CHECK_EVENTS_20261124.tsv; ../CLAUDE_INTAKE_CHECK_EVENTS_cp63_70.tsv; ../CLAUDE_INTAKE_CHECK_EVENTS_cp71_91.tsv; bounded header/III examples as recorded in the substantive review."
  },
  {
    "id": "III-C8-P13",
    "review_heading": "## §1.5: every historical and checking claim",
    "review_index": 12,
    "claim": "Models compared statements, marked data, proofs and primary sources and resolved disagreements at affected steps/maps/parameters.",
    "records": "FR and BR; the complete c8 LT/LV/LG comparisons and the exact OS49 boundary/period bridge are concrete examples already admitted.",
    "recomputation": "No count is inferred from the number of paragraphs, messages or repaired files.",
    "primary": "The explicit forward/inverse maps and actual source comparisons in those records supply this methodological description.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "methods"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/provenance; S6_SERIES_PUBLISH_deposit_fields.md > Paper III > Provenance"
  },
  {
    "id": "III-C8-P14",
    "review_heading": "## §1.5: every historical and checking claim",
    "review_index": 13,
    "claim": "Checks include derivations written before earlier proofs and independent proofs.",
    "records": "Exact fresh input-scope/freeze/release records and admitted event types are the evidence. LG's root fresh review is a concrete chronology record.",
    "recomputation": "The final selector preserves independent and targeted types; the present publication reading creates neither.",
    "primary": "The actual release records, not a generic model label, establish when original proofs were available.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "methods"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/provenance; S6_SERIES_PUBLISH_deposit_fields.md > Paper III > Provenance"
  },
  {
    "id": "III-C8-P15",
    "review_heading": "## §1.5: every historical and checking claim",
    "review_index": 14,
    "claim": "Checks include exact arithmetic and certified rational bounds.",
    "records": "The admitted c5 KM comparison records its rational whole-segment Rouche certificates; current residual/LV code exhibits exact SymPy identities.",
    "recomputation": "Root applied “certified rational bounds” in place of “interval computations” with the final counts at 21:18:50.551077 UTC. The actual current methodology was read again. No new mathematical execution is claimed here.",
    "primary": "Exact software/source scope is detailed below. The V-specific Normaliz/Arb/SciPy declarations are not copied without III evidence.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "methods"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/provenance; S6_SERIES_PUBLISH_deposit_fields.md > Paper III > Provenance"
  },
  {
    "id": "III-C8-P16",
    "review_heading": "## §1.5: every historical and checking claim",
    "review_index": 15,
    "claim": "Computations are described where used and programs are listed at the end.",
    "records": "The substantive unit reviews and root's single programs-table work give the mathematical/program relationship.",
    "recomputation": "Root/lv_compare own final path selection and the final records table; this note makes no path-count claim.",
    "primary": "Every printed historical path must occur in the attached repository path list, and every current path must exist in code, under the prescribed prompt rule.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "methods"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/provenance; S6_SERIES_PUBLISH_deposit_fields.md > Paper III > Provenance",
    "evidence": "Root-reported completed program review: agents/continuation8_iii_weighted_units/S6_SERIES_PUBLISH_III_programs_table_review.md; code/S6_SERIES_PUBLISH_c8_III_program_records_final.out and .err. Root wholly read 181 rows, 50 HTTP200 accesses and 42 stored-digest agreements; eight cases retain unavailable prior digests. This reviewer adds no old-execution credit.",
    "extra_gate": "Final PDF program-table/path agreement; retain the eight bounded prior-digest unknowns and every prior execution limit.",
    "status": "open: final-PDF program-table visibility",
    "resolution": "The source and root-admitted program/path records are complete at their stated scope. Actual visibility and placement of the full program table in the final PDF remain unverified in this provenance row."
  },
  {
    "id": "III-C8-P17",
    "review_heading": "## §1.5: every historical and checking claim",
    "review_index": 16,
    "claim": "Existing proofs were reread in full against their replacements with inverse maps and exceptional parameters.",
    "records": "The exact whole-read attribution in the completed unit reviews establishes the readings actually performed, including scoped parent/peer admission.",
    "recomputation": "These are use/rechecking events. They are not automatically independent, fresh or formal-verification events.",
    "primary": "Full proof readings retain their particular owners; source parsing alone is not credited.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "methods"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/provenance; S6_SERIES_PUBLISH_deposit_fields.md > Paper III > Provenance"
  },
  {
    "id": "III-C8-P18",
    "review_heading": "## §1.5: every historical and checking claim",
    "review_index": 17,
    "claim": "Records preserve scope and corrected assertions.",
    "records": "Local defects retain exact old/new text; comparisons preserve rejected premises, replacements and bounded reasons.",
    "recomputation": "The final selector excludes the one exact wholly withdrawn row; it retains the replacement and the other rows discussing withdrawn premises with their actual scope.",
    "primary": "Current records and their actual fields supply this claim; a failed old assertion is not erased from the historical record.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "methods"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/provenance; S6_SERIES_PUBLISH_deposit_fields.md > Paper III > Provenance"
  },
  {
    "id": "III-C8-P19",
    "review_heading": "## §1.5: every historical and checking claim",
    "review_index": 18,
    "claim": "The final paragraph reports 1,066 event associations in 799 evidence groups, with counts 421/2/50/473/90/30.",
    "records": "The final `records/S6_SERIES_PUBLISH_III_current_check_counts.json` and the complete count-selection review give the exact current subjects, six types and withdrawal rule.",
    "recomputation": "The wholly read 320-line selector and actual 27-line inspection output have these counts. Root's final run retained the exact selected ID sequence, and the sum of the six counts is 1,066.",
    "primary": "The primary evidence is the admitted event ledger selected by current formal statement ownership. The complete current §1.5 and embedded JSON retain the final record's paragraph verbatim, including its association and prior-exposure qualifications.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "counts"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/provenance; S6_SERIES_PUBLISH_deposit_fields.md > Paper III > Provenance",
    "evidence": "code/S6_SERIES_PUBLISH_c8_III_check_counts.py; agents/continuation8_iii_weighted_units/S6_SERIES_PUBLISH_III_check_counts_selection_review.md; final records/S6_SERIES_PUBLISH_III_current_check_counts.json (summary read through line 82; no new count regeneration)."
  },
  {
    "id": "III-C8-P20",
    "review_heading": "## §1.5: every historical and checking claim",
    "review_index": 19,
    "claim": "No human has checked the mathematics.",
    "records": "This exact declaration is explicitly required in the controlling prompt and retained in current III and the proposed provenance.",
    "recomputation": "The count program enumerates recorded automated work only; it cannot independently establish an assertion about unrecorded human activity.",
    "primary": "It remains the submitter's stated human-understanding declaration.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "human"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/provenance; S6_SERIES_PUBLISH_deposit_fields.md > Paper III > Provenance"
  },
  {
    "id": "III-C8-P21",
    "review_heading": "## §1.5: every historical and checking claim",
    "review_index": 20,
    "claim": "CC0 1.0 Universal dedication.",
    "records": "Prompt and current III authorize this dedication; draft `license` is exactly `CC0 1.0`.",
    "recomputation": "Name and canonical URL agree across the proposed field and current text.",
    "primary": "The actual Creative Commons deed was opened in this review and identifies CC0 1.0 Universal. No rights certification is inferred.",
    "gate_keys": [
      "pdf"
    ],
    "source_keys": [
      "licence"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/license and #/provenance; S6_SERIES_PUBLISH_deposit_fields.md > Paper III > Provenance and Subjects and classification",
    "evidence": "code/S6_SERIES_PUBLISH_c8_III_provenance_links.stdout.txt; code/S6_SERIES_PUBLISH_c8_III_provenance_primary.stdout.txt; both actual empty stderrs.",
    "extra_gate": "Final PDF CC0 hyperlink target and visible licence name."
  },
  {
    "id": "III-C8-P22",
    "review_heading": "## §1.5: every historical and checking claim",
    "review_index": 21,
    "claim": "The standing records page and prescribed repository commit.",
    "records": "Prompt §0.3; current III preamble has the prescribed macro definitions. Root applied D18 correction III-C8-RECORDS-STANDING-ADDRESS at 21:45:45.737825 UTC; the actual new source clause was read.",
    "recomputation": "The source now states the standing address, uses each macro once, and retains the prescribed source-only commit. The deposit fields retain the address and omit the commit sentence. The count paragraph is unchanged.",
    "primary": "HTTP 200 located the exact Paper III section and its current checkpoint-34 links. This verifies the standing address. Updating the live section and source commit at submission remains a separate outstanding action; no current-edition delivery or publishing is claimed.",
    "gate_keys": [
      "pdf",
      "live"
    ],
    "source_keys": [
      "records"
    ],
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/comments and #/provenance; S6_SERIES_PUBLISH_deposit_fields.md > Paper III > Comments/Provenance: standing records URL only; source commit intentionally omitted (see III-C8-D15)",
    "evidence": "code/S6_SERIES_PUBLISH_c8_III_provenance_links.stdout.txt; code/S6_SERIES_PUBLISH_c8_III_provenance_primary.stdout.txt; both actual empty stderrs.",
    "extra_gate": "Final PDF clickable destination must resolve to the exact Paper III anchor; inspect the source-only commit display.",
    "resolution": "The standing destination and prescribed source-only commit are verified after the actual D18 correction. Submission-time records delivery and commit reset remain separate open actions; no publication is performed."
  },
  {
    "id": "III-C8-D01",
    "claim": "The deposit title is the current Paper III title with its display line break represented by sentence punctuation.",
    "records": "Current source title and the authorized V v3 field schema; the frozen review retains the III-specific title.",
    "recomputation": "Exact text correspondence: the source display break \\\\[.5em] between the series and paper number is represented by a period and space; all mathematical title tokens and the III subtitle are retained.",
    "primary": "The current III title is the primary documentary source; no other-paper title is imported.",
    "source_keys": [
      "title"
    ],
    "paper_location": "Deposit-only field; supplying current III source/body claims are identified in the records and primary columns.",
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/title; S6_SERIES_PUBLISH_deposit_fields.md > Paper III corresponding field",
    "gate_keys": [
      "pdf"
    ],
    "extra_gate": "Final PDF title rendering and final deposit/title agreement."
  },
  {
    "id": "III-C8-D02",
    "claim": "The deposit abstract retains the complete 195-word current III abstract.",
    "records": "The complete current abstract and AB01–AB10 supplying records, with the final read-only validation in the substantive review.",
    "recomputation": "The field equals the source abstract after whitespace joining alone and has 195 whitespace-separated words, within the prescribed 250-word limit; this is not an event-count computation.",
    "primary": "The primary mathematical claims and source loci are recorded individually in III-C8-AB01–AB10.",
    "source_keys": [
      "abstract"
    ],
    "paper_location": "Deposit-only field; supplying current III source/body claims are identified in the records and primary columns.",
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/abstract; S6_SERIES_PUBLISH_deposit_fields.md > Paper III corresponding field",
    "gate_keys": [
      "pdf"
    ],
    "extra_gate": "Final PDF abstract rendering, including mathematical symbols and complete last sentence."
  },
  {
    "id": "III-C8-D03",
    "claim": "Comments describe the five-paper series and the actual sphere-map, invariant and conifold contributions without an additional first/priority claim.",
    "records": "The seven current main statements, FR and the claim-by-claim final review.",
    "recomputation": "The comments retain the reviewed contribution sentence; no new count or novelty search is used.",
    "primary": "The exact supplying body owners and opened literature are the AB/ST rows; bounded novelty scope is preserved.",
    "source_keys": [
      "series",
      "main:A",
      "main:B",
      "main:C",
      "main:D",
      "main:E",
      "main:F",
      "main:G"
    ],
    "paper_location": "Deposit-only field; supplying current III source/body claims are identified in the records and primary columns.",
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/comments; S6_SERIES_PUBLISH_deposit_fields.md > Paper III corresponding field",
    "gate_keys": [
      "pdf",
      "joint"
    ],
    "extra_gate": "Final source/deposit contribution agreement; five-together series comparison remains open."
  },
  {
    "id": "III-C8-D04",
    "claim": "Comments credit the original complex six-sphere family to Claude and L. Alpöge at https://alpo.ge/s6.pdf.",
    "records": "FR/BR record the 108-page author manuscript, its bibliographic identity and the actual family input.",
    "recomputation": "The author names and URL are copied from the admitted current credit; no priority beyond the stated original family construction is inferred.",
    "primary": "AC26 author manuscript; Theorems 7.17 and 7.22, printed pages 57 and 60; exact source identity/opening limits in FR/BR.",
    "source_keys": [
      "status:E"
    ],
    "paper_location": "Deposit-only field; supplying current III source/body claims are identified in the records and primary columns.",
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/comments; S6_SERIES_PUBLISH_deposit_fields.md > Paper III corresponding field",
    "gate_keys": [
      "pdf"
    ],
    "extra_gate": "Final rendered AC26 citation and deposit-credit agreement."
  },
  {
    "id": "III-C8-D05",
    "claim": "Comments credit Engel’s elliptic-surface construction using arXiv:2609.38442v1.",
    "records": "FR/BR and the current A,C,F,G source relationships identify the supplied construction.",
    "recomputation": "The exact v1 identifier is retained; no theorem of III is reassigned to the source.",
    "primary": "E26 v1 Proposition 2.4 and Propositions 2.7–2.8, pages 5–7; Theorem 4.1 page 12; Remarks 8.3 and 8.5, pages 22–24, at the bounded scopes recorded in FR/BR.",
    "source_keys": [
      "status:A",
      "status:C",
      "status:F",
      "status:G"
    ],
    "paper_location": "Deposit-only field; supplying current III source/body claims are identified in the records and primary columns.",
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/comments; S6_SERIES_PUBLISH_deposit_fields.md > Paper III corresponding field",
    "gate_keys": [
      "pdf"
    ],
    "extra_gate": "Final rendered supplying citations and deposit-credit agreement."
  },
  {
    "id": "III-C8-D06",
    "claim": "Comments credit Yang’s toroidal fillings using arXiv:2609.29666v1.",
    "records": "BR and the complete admitted KL/OS49 period-and-cap correspondence preserve the exact supplying role.",
    "recomputation": "The v1 identifier and construction scope are retained; the actual parameter/meridian maps remain with their admitted proofs.",
    "primary": "Yang v1 Proposition 3.1 page 11, Proposition 3.4 page 13 and Proposition 3.6 page 14 were opened in BR; no broader whole-paper reading is claimed.",
    "source_keys": [
      "bib:manYang26"
    ],
    "paper_location": "Deposit-only field; supplying current III source/body claims are identified in the records and primary columns.",
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/comments; S6_SERIES_PUBLISH_deposit_fields.md > Paper III corresponding field",
    "gate_keys": [
      "pdf"
    ],
    "extra_gate": "Final rendered supplying Yang citations and deposit-credit agreement."
  },
  {
    "id": "III-C8-D07",
    "claim": "Comments credit Viaclovsky’s two-parameter family using arXiv:2609.33785v1.",
    "records": "BR records the exact v1 and bounded complete printed-page readings.",
    "recomputation": "The version is retained literally; the source and III conclusions keep their exact domains.",
    "primary": "Viaclovsky v1 printed pages 1–2,6–9,19–20 were read: Theorem 1.1, Proposition 3.1/Lemma 3.2 and Proposition 6.4 at their recorded scopes. The exact existing digest is in BR; no new retrieval is performed here.",
    "source_keys": [
      "bib:manViaclovskyTwo26"
    ],
    "paper_location": "Deposit-only field; supplying current III source/body claims are identified in the records and primary columns.",
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/comments; S6_SERIES_PUBLISH_deposit_fields.md > Paper III corresponding field",
    "gate_keys": [
      "pdf"
    ],
    "extra_gate": "Final rendered supplying source/version citations and deposit-credit agreement."
  },
  {
    "id": "III-C8-D08",
    "claim": "Comments credit Viaclovsky’s logarithmic-transformation family using arXiv:2610.39102v1.",
    "records": "BR and the bounded Q109 attribution correction preserve the integral H2 cap-map cokernel scope.",
    "recomputation": "The exact v1 identifier is retained; the H2 source statement is not expanded into all integral homology.",
    "primary": "Viaclovsky Logs v1 data (2.11)–(2.12) page 4, Proposition 2.3 pages 5–6, Proposition 4.1 page 9 and Corollary 4.6 page 14 were read in BR.",
    "source_keys": [
      "bib:manViaclovskyLogs26"
    ],
    "paper_location": "Deposit-only field; supplying current III source/body claims are identified in the records and primary columns.",
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/comments; S6_SERIES_PUBLISH_deposit_fields.md > Paper III corresponding field",
    "gate_keys": [
      "pdf"
    ],
    "extra_gate": "Final rendered source-scope sentence/citations and deposit-credit agreement."
  },
  {
    "id": "III-C8-D09",
    "claim": "Comments credit Zhubr’s marked recognition of simply connected spin six-manifolds.",
    "records": "FR/BR and complete current K9/Q145/Q146 retain the constructed manifold and full marked invariant.",
    "recomputation": "The full finite-coordinate invariant and zero-free-H3 construction remain with the supplying proof; no group-order-only recognition is asserted.",
    "primary": "English 1975 Theorems 3 and 5, pages 795–796, and section 4.1 page 809; both English rank clauses in sections 1.1–1.2 concern H2, as recorded in the exact primary review.",
    "source_keys": [
      "status:E",
      "known:E"
    ],
    "paper_location": "Deposit-only field; supplying current III source/body claims are identified in the records and primary columns.",
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/comments; S6_SERIES_PUBLISH_deposit_fields.md > Paper III corresponding field",
    "gate_keys": [
      "pdf"
    ],
    "extra_gate": "Final rendered classification citation/scope and deposit-credit agreement."
  },
  {
    "id": "III-C8-D10",
    "claim": "Comments credit oriented surgery recognition to Burklund, Hahn and Senger, arXiv:1910.14116v3.",
    "records": "FR records the exact opened v3 theorem scope; BR separately identifies the 2023 journal publication metadata.",
    "recomputation": "The comments retain the explicitly named opened preprint; the journal metadata are not silently used to change its page locator.",
    "primary": "BHS v3 Recollection 2.2 and Theorem 2.6, pages 7–8, were opened for the conifold application; BR’s journal title-page opening retains its metadata-only scope.",
    "source_keys": [
      "status:G",
      "known:G"
    ],
    "paper_location": "Deposit-only field; supplying current III source/body claims are identified in the records and primary columns.",
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/comments; S6_SERIES_PUBLISH_deposit_fields.md > Paper III corresponding field",
    "gate_keys": [
      "pdf"
    ],
    "extra_gate": "Final rendered surgery citation and deposit-credit agreement."
  },
  {
    "id": "III-C8-D11",
    "claim": "The proposed subject is math.CV, with cross-lists math.GT, math.AT and math.AG.",
    "records": "The current III results and the bounded attachment search in the final review support these classification choices; no pre-existing III choices were found in the named searched attachments.",
    "recomputation": "The four exact category strings are retained; this is a classification choice for the actual contributions, not a check count or an assertion of disjoint subject matter.",
    "primary": "Official https://arxiv.org/category_taxonomy opened, then retrieved HTTP200 at 2026-11-25T21:30:26 UTC: exact CV/GT/AT/AG labels found; raw response address/headers/bytes/SHA are in code/S6_SERIES_PUBLISH_c8_III_provenance_primary.stdout.txt.",
    "source_keys": [],
    "paper_location": "Deposit-only field; supplying current III source/body claims are identified in the records and primary columns.",
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/subject; crossListSubjects; S6_SERIES_PUBLISH_deposit_fields.md > Paper III corresponding field",
    "gate_keys": [],
    "extra_gate": "Final deposit classification review; no PDF-specific classification assertion is made.",
    "evidence": "code/S6_SERIES_PUBLISH_c8_III_provenance_primary.stdout.txt and .stderr.txt; code/S6_SERIES_PUBLISH_c8_III_provenance_primary_msc_v002.stdout.txt and .stderr.txt; exact addresses/versions/pages/actual digests retained there."
  },
  {
    "id": "III-C8-D12",
    "claim": "The proposed MSC codes are 32Q55 (primary), 32J17, 55Q40, 57R55 and 14J27.",
    "records": "The final review maps each code to III’s actual mathematical contribution and records the bounded search scope.",
    "recomputation": "The exact five strings are retained in order; the raw-byte retrieval supplies source identity, not a new mathematical classification proof.",
    "primary": "Official MSC2020 PDF: exact code entries at printed/PDF pages 79,77,148,153,37, respectively. HTTP200,667318 bytes,224 pages and actual SHA/headers are recorded in the initial access stdout. The same-PDF v002 output preserves the initial false 57R55 match and records U+FB00 to ff and U+FB01 to fi; all five tests pass. No PDF copy is saved.",
    "source_keys": [],
    "paper_location": "Deposit-only field; supplying current III source/body claims are identified in the records and primary columns.",
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/mscCodes; S6_SERIES_PUBLISH_deposit_fields.md > Paper III corresponding field",
    "gate_keys": [],
    "extra_gate": "Final deposit classification review; no final-PDF page reading is required for a deposit-only MSC field.",
    "evidence": "code/S6_SERIES_PUBLISH_c8_III_provenance_primary.stdout.txt and .stderr.txt; code/S6_SERIES_PUBLISH_c8_III_provenance_primary_msc_v002.stdout.txt and .stderr.txt; exact addresses/versions/pages/actual digests retained there."
  },
  {
    "id": "III-C8-D13",
    "claim": "The ten deposit tags describe the actual III constructions and methods.",
    "records": "The exact tag list in the reviewed JSON is tied to A–G and the existing mathematical program/source record.",
    "recomputation": "No fourfold, Oka-theory or other V-specific tag is imported; the listed III words are retained literally.",
    "primary": "The current III mathematical statements supply the subject descriptions; the official taxonomy/MSC openings support the associated classification scope.",
    "source_keys": [],
    "paper_location": "Deposit-only field; supplying current III source/body claims are identified in the records and primary columns.",
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/tags; S6_SERIES_PUBLISH_deposit_fields.md > Paper III corresponding field",
    "gate_keys": [],
    "extra_gate": "Final deposit-field review against the actual III scope; no printed tag list is asserted."
  },
  {
    "id": "III-C8-D14",
    "claim": "The six aiSystems entries retain the five named model identities and the evidenced Python/SymPy exact-arithmetic software entry, with version null.",
    "records": "Prompt section 4.1, authorized V v3 documentary chronology, current session identity, FE/BE and actual III code imports retain their exact attribution scopes.",
    "recomputation": "The schema has provider/model/version for each entry; null version does not invent a model-release or software-version value. Historical Astra and current Astra Pro remain distinct named entries.",
    "primary": "The supplying historical reports and current identity are documentary primary evidence. Actual code/S6_SERIES_PUBLISH_c8_residual_wall_arithmetic.py and c8_lv_character_transport_v001.py imports support Python/SymPy; no Normaliz/Arb/SciPy usage is inferred from V.",
    "source_keys": [
      "production",
      "other_models"
    ],
    "paper_location": "Deposit-only field; supplying current III source/body claims are identified in the records and primary columns.",
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/aiSystems; provenance; S6_SERIES_PUBLISH_deposit_fields.md > Paper III corresponding field",
    "gate_keys": [
      "pdf"
    ],
    "extra_gate": "Final PDF model/effort/date wording and deposit agreement; software scope remains the actual code evidence."
  },
  {
    "id": "III-C8-D15",
    "claim": "Deposit provenance omits the repository-commit sentence; the source retains its prescribed commit macro and the deposit retains the standing III records URL.",
    "records": "Root’s whole-note review required exactly this field-only correction. The substantive note records the exact removed sentence outside the JSON; all other provenance words and all ten other fields were preserved.",
    "recomputation": "The application compares the corrected JSON exactly, rejects every 40–64 hexadecimal-character commit/digest-like string in JSON and the appended section, and checks the source macro without editing it. Counts are read from the admitted record, never regenerated.",
    "primary": "The prescribed source macro is the documentary authority for the current source commit. The actual HTTP200 standing-page opening locates Paper III and its historical checkpoint-34 links; it does not establish submission of the current files.",
    "source_keys": [
      "records"
    ],
    "paper_location": "Deposit-only field; supplying current III source/body claims are identified in the records and primary columns.",
    "deposit_location": "S6_SERIES_PUBLISH_deposit_fields_III.json#/provenance; comments; Paper III > Remaining publication gates; S6_SERIES_PUBLISH_deposit_fields.md > Paper III corresponding field",
    "gate_keys": [
      "pdf",
      "live"
    ],
    "extra_gate": "Final PDF source-only commit display and exact records-link target; submission-time live update remains pending.",
    "resolution": "Exactly the source-commit sentence was removed from deposit provenance. The corrected field keeps every other word and the exact final count paragraph; the source macro is untouched. Live publication and final PDF agreement remain pending."
  }
]
''')


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def whitespace_pattern(text):
    """Preserve every nonwhitespace token; permit only source line/space changes."""
    return r"\s+".join(re.escape(token) for token in text.split())


def locate_claim(source, front_start, front_end, text):
    matches = list(re.finditer(whitespace_pattern(text), source[front_start:front_end]))
    require(len(matches) == 1, f"Expected one source-claim occurrence: {text[:90]!r}")
    start = front_start + matches[0].start()
    end = front_start + matches[0].end()
    return source.count("\n", 0, start) + 1, source.count("\n", 0, end) + 1


def review_rows(note):
    result = {}
    for heading in (
        "## Abstract: every mathematical claim",
        "## A–G status sentences and every §1.4 row",
        "## §1.1: series paragraph and all table entries",
        "## §1.5: every historical and checking claim",
    ):
        require(note.count(heading) == 1, f"Review heading changed: {heading}")
        block = note.split(heading, 1)[1].split("\n## ", 1)[0]
        lines = [line for line in block.splitlines() if line.startswith("|")][2:]
        result[heading] = [[cell.strip() for cell in line.strip("|").split("|")] for line in lines]
    return result


def deposit_section():
    d = DEPOSIT_DATA
    parts = ["", "## Paper III", ""]
    for field, title in (("title", "Title"), ("abstract", "Abstract"),
                         ("comments", "Comments"), ("provenance", "Provenance")):
        parts.extend([f"### {title}", "", d[field], ""])
    parts.extend([
        "### Subjects and classification", "",
        "- Primary subject: " + d["subject"],
        "- Cross-lists: " + "; ".join(d["crossListSubjects"]),
        "- MSC codes: " + "; ".join(d["mscCodes"]),
        "- Tags: " + "; ".join(d["tags"]),
        "- Authorship mode: " + d["authorshipMode"],
        "- Licence: " + d["license"], "", "### AI systems", "",
    ])
    for system in d["aiSystems"]:
        parts.append(f"- {system['provider']}: {system['model']}; version: null")
    parts.extend([
        "", "### Remaining publication gates", "",
        "The final PDF's printed front matter and hyperlinks still require their actual "
        "visual/destination checks. The five-together series and cross-paper comparison "
        "remains pending. The standing Paper III records section presently links to "
        "historical checkpoint 34 and must be updated at submission. The repository "
        "commit is stated in the paper's methodology; no commit is included in these "
        "deposit fields. This section records no external publication or live-page update.", "",
    ])
    return "\n".join(parts)


def prepare():
    source_bytes = SOURCE.read_bytes()
    source = source_bytes.decode("utf-8")
    note = NOTE.read_text()
    blocks = re.findall(r"```json\n(.*?)\n```", note, re.S)
    require(len(blocks) == 1 and json.loads(blocks[0]) == DEPOSIT_DATA,
            "Corrected review JSON differs from the literal proposal")
    require(list(DEPOSIT_DATA) == FIELD_NAMES, "Eleven-field schema/order changed")
    require(all(set(x) == {"provider", "model", "version"} and x["version"] is None
                for x in DEPOSIT_DATA["aiSystems"]), "AI-system schema changed")
    require(DEPOSIT_DATA["provenance"].startswith(
        "Text: AI-authored; none of it was written by a human. "
        "The submitter takes responsibility for the veracity of the text."),
        "Required authorship opening changed")
    payload = json.dumps(DEPOSIT_DATA, ensure_ascii=False, indent=2) + "\n"
    section = deposit_section()
    require(COMMIT_IN_SOURCE not in payload and COMMIT_IN_SOURCE not in section,
            "A source commit entered the deposit data")
    require(not re.search(r"(?<![0-9a-f])[0-9a-f]{40,64}(?![0-9a-f])", payload + section, re.I),
            "A commit/digest-like string entered the deposit fields")
    front_start = source.index(r"\begin{document}")
    front_end = source.index(r"\section{Conventions and the marked family}", front_start)
    positions = {
        key: locate_claim(source, 0 if key.startswith("bib:") else front_start,
                          len(source) if key.startswith("bib:") else front_end, value)
        for key, value in SOURCE_GUARDS.items()
    }
    require(source.count(r"\newcommand{\SsixRepositoryCommit}{" + COMMIT_IN_SOURCE + "}") == 1,
            "Prescribed source commit macro changed")
    require(source.count(r"\newcommand{\SsixPublishRecords}{" + RECORDS_URL.replace("#", r"\#") + "}") == 1,
            "Prescribed source records macro changed")
    method = SOURCE_GUARDS["methodology"]
    require(method.count(r"\SsixPublishRecords") == 1 and method.count(r"\SsixRepositoryCommit") == 1,
            "Methodology macro multiplicity changed")
    abstract = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", source, re.S)
    require(abstract is not None, "Missing source abstract")
    require(" ".join(abstract.group(1).split()) == DEPOSIT_DATA["abstract"],
            "Abstract differs beyond whitespace")
    require(len(DEPOSIT_DATA["abstract"].split()) == 195, "Reviewed abstract length changed")
    count_record = json.loads(COUNTS.read_text())
    require(count_record["counts"] == EXPECTED_COUNTS
            and count_record["selected_event_associations"] == 1066
            and count_record["declared_evidence_groups"] == 799,
            "Final admitted count record changed; this program does not regenerate it")
    count_paragraph = count_record["proposed_section_1_5_paragraph"]
    require(DEPOSIT_DATA["provenance"].count(count_paragraph) == 1
            and count_paragraph in " ".join(method.split()), "Final count paragraph differs")
    reviewed = review_rows(note)
    rows = []
    for claim in CLAIMS:
        if claim.get("review_heading"):
            actual = reviewed[claim["review_heading"]][claim["review_index"]]
            expected = [claim[key] for key in ("claim", "records", "recomputation", "primary")]
            require(actual == expected, f"Reviewed claim data changed: {claim['id']}")
        paper_locations = []
        for key in claim["source_keys"]:
            start, end = positions[key]
            paper_locations.append(f"S6_SERIES_PUBLISH_III.tex:{start}–{end} ({key})")
        paper_location = "; ".join(paper_locations) or claim["paper_location"]
        gates = {"pdf": PDF_GATE, "joint": JOINT_GATE, "live": LIVE_GATE}
        gate = " ".join(gates[key] for key in claim.get("gate_keys", []))
        gate = " ".join(part for part in (gate, claim.get("extra_gate", "")) if part)
        row = dict.fromkeys(SCHEMA, "")
        row.update({
            "claim_id": claim["id"], "paper": "III", "locations": paper_location,
            "claim": claim["claim"], "against_records": claim["records"],
            "by_recomputation": claim["recomputation"],
            "against_primary_source": claim["primary"],
            "required_action": gate, "evidence": REVIEW_EVIDENCE + "; " + claim.get("evidence", ""),
            "current_paper_location": paper_location,
            "current_deposit_location": claim["deposit_location"],
            "resolution_status": claim.get("status", STATUS_SOURCE_COMPLETE),
            "remaining_gate": gate,
            "old_HEXAGON_disposition": claim.get("old_disposition",
                "Authorized V v3 schema and documentary declarations retained at their stated scope; "
                "III mathematics and metadata supplied from the current III evidence; V is unchanged."),
            "current_resolution": claim.get("resolution",
                "The reviewed current claim is preserved in the listed paper/deposit locations. "
                "This application adds no proof, independent-check or final-PDF credit."),
        })
        rows.append(row)
    require(len({row["claim_id"] for row in rows}) == len(rows), "Duplicate proposed claim ID")
    old_table = TABLE.read_bytes()
    old_markdown = MARKDOWN.read_bytes()
    require(old_table.endswith(b"\n") and b"\r" not in old_table, "Existing TSV is not LF-terminated")
    reader = csv.DictReader(io.StringIO(old_table.decode("utf-8")), delimiter="\t")
    old_rows = list(reader)
    require(reader.fieldnames == SCHEMA, "Existing provenance schema changed")
    require(not any(row["paper"] == "III" for row in old_rows), "III rows already exist; do not overwrite")
    require(not ({row["claim_id"] for row in old_rows} & {row["claim_id"] for row in rows}),
            "A proposed claim ID already exists")
    require(not re.search(rb"(?m)^## Paper III\s*$", old_markdown), "III deposit section already exists")
    require(not DEPOSIT.exists(), "III JSON already exists; do not overwrite")
    out = io.StringIO(newline="")
    writer = csv.DictWriter(out, fieldnames=SCHEMA, delimiter="\t", lineterminator="\n")
    writer.writerows(rows)
    tsv_append = out.getvalue().encode("utf-8")
    md_append = (("" if old_markdown.endswith(b"\n") else "\n") + section).encode("utf-8")
    return source_bytes, old_table, old_markdown, payload.encode("utf-8"), tsv_append, md_append, rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Root-only explicit application after whole review")
    args = parser.parse_args()
    source_bytes, old_table, old_markdown, payload, tsv_append, md_append, rows = prepare()
    if not args.apply:
        print("PROPOSED_JSON", DEPOSIT.name)
        print(payload.decode("utf-8"), end="")
        print("PROPOSED_III_PROVENANCE_ROWS", len(rows))
        print("\t".join(SCHEMA))
        print(tsv_append.decode("utf-8"), end="")
        print("PROPOSED_APPEND_ONLY_III_SECTION", MARKDOWN.name)
        print(md_append.decode("utf-8"), end="")
        print("INSPECT_ONLY: no file written; no count regenerated; no source or event edited.")
        return
    require(SOURCE.read_bytes() == source_bytes, "Source changed during preflight")
    require(TABLE.read_bytes() == old_table and MARKDOWN.read_bytes() == old_markdown,
            "Shared metadata changed during preflight")
    require(not DEPOSIT.exists(), "III JSON appeared during preflight")
    DEPOSIT.write_bytes(payload)
    TABLE.write_bytes(old_table + tsv_append)
    MARKDOWN.write_bytes(old_markdown + md_append)
    require(DEPOSIT.read_bytes() == payload, "JSON write/read mismatch")
    require(TABLE.read_bytes() == old_table + tsv_append, "TSV write/read mismatch")
    require(MARKDOWN.read_bytes() == old_markdown + md_append, "Markdown write/read mismatch")
    require(SOURCE.read_bytes() == source_bytes, "Source changed during application")
    print("WROTE", DEPOSIT.name, "with the exact reviewed eleven fields")
    print("APPENDED", len(rows), "III provenance rows; every prior TSV byte is preserved")
    print("APPENDED one Paper III deposit section; every prior Markdown byte is preserved")
    print("FIELD_CORRECTION: source-commit sentence omitted from deposit provenance; source macros unchanged")
    print("GATES_PENDING: final PDF agreement, five-together checks, submission-time live records update")
    print("NO source/event/count-record edits, count regeneration, external publication, or hash generation")


if __name__ == "__main__":
    main()
