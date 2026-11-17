"""Checked editorial corrections for the fully expanded original MAPS D source.

The assembly imports ``transform`` before adding namespaces.  This module does
not assemble a paper or write any manuscript.  Every mathematical proof and
every original D result remains present.  The modular realization is printed
once by the root assembler, and is explicitly invoked here at D.2.1.

Evidence: work/invariants_arithmetic/maps_D_independent_audit.json;
work/invariants_arithmetic/maps_D_remaining_questions.json;
work/cdp_audit/modular_collision_review/independent_review.json.
"""
from __future__ import annotations

import re

BEGIN_MARKER = "% BEGIN checked MAPS D editorial corrections 2026-11-17\n"
END_MARKER = "% END checked MAPS D editorial corrections 2026-11-17\n"
HEAD = re.compile(
    r"\\paragraph\{(?:Theorem|Proposition|Lemma|Corollary|Computation|Remaining task) "
    r"(D\.[123]\.\d+)\b"
)


def _replace(s: str, old: str, new: str, *, count: int = 1) -> str:
    actual = s.count(old)
    if actual != count:
        raise ValueError(f"MAPS D correction anchor: expected {count}, got {actual}: {old!r}")
    return s.replace(old, new)


def _append_to_result(s: str, sid: str, addition: str) -> str:
    marks = list(HEAD.finditer(s))
    hits = [i for i, m in enumerate(marks) if m[1] == sid]
    if len(hits) != 1:
        raise ValueError(f"Expected one complete result {sid}; found {len(hits)}")
    i = hits[0]
    end = marks[i + 1].start() if i + 1 < len(marks) else len(s)
    # Keep the next subsection heading with the following result.
    raw = s[marks[i].start():end]
    tail = re.search(r"((?:\s*\\(?:sub)*section\*?\{[^\n]+\}\s*)+)$", raw)
    if tail:
        end = marks[i].start() + tail.start()
    return s[:end].rstrip() + "\n\n" + addition.strip() + "\n\n" + s[end:]


def _drop_priority_metadata(s: str) -> str:
    # These are editorial metadata, not mathematical assertions or proof steps.
    s = _replace(
        s,
        "The original cases are \\cite[Theorem 7.13]{manYang26}; no\n"
        "priority claim is made for them or for the extensions above.",
        "The original cases are proved in \\cite[Theorem~7.13]{manYang26}.",
    )
    s = _replace(
        s,
        "The current-source search is recorded in the report; this\n"
        "statement makes no priority claim.\n",
        "",
    )
    s = _replace(
        s,
        "The source search is recorded separately;\nno novelty or priority claim is made.",
        "The source comparison is recorded in the verification index.",
    )
    s, n = re.subn(r"\s*No\s+priority claim\s+is made\.", "", s)
    if n != 7:
        raise ValueError(f"Expected seven remaining metadata sentences, found {n}")
    return s


CHANGES = [
    dict(id="D-provider", results=["D.2.1"],
         reason="Supply the absent exact geometric/peripheral/section realization for profiles 50/II and 56/II.",
         evidence="work/cdp_audit/modular_collision_review/independent_review.json",
         content_change="Added explicit use of the separately printed complete provider; original configuration proof unchanged."),
    dict(id="D-archival", results=["D.2.2"],
         reason="Distinguish regenerated archived numerical replies from a fresh remote geometric verification.",
         evidence="work/invariants_arithmetic/maps_D_explorer_cache_runs.json; maps_D_explorer_fresh_probe.json",
         content_change="Added precise archival check scope; all source computations and qualifications retained."),
    dict(id="D-open-scope", results=["D.2.4", "D.2.28", "D.2.37", "D.2.40", "D.2.51"],
         reason="Separate historical gaps closed by subsequent results from the exact remaining cap columns and refined invariant.",
         evidence="work/invariants_arithmetic/maps_D_remaining_questions.json",
         content_change="Status prose corrected; every theorem, formula, complete proof, and example retained."),
    dict(id="D-source-shorthand", results=["D.1.7", "D.1.12", "D.2.3", "D.2.6", "D.2.20", "D.2.31", "D.2.34", "D.3.1"],
         reason="Replace checkpoint-only R1/K1/K11/K12/K13/K15/R4 references by exact FAMILY/PUSH labels or the already complete local argument.",
         evidence="sources/prompts/S6_04_MAPS_MANIFOLDS/PROMPT.md:44; sources/per_prompt/S6_04_MAPS_MANIFOLDS/S6_CHECKPOINT_01_20261115.md:22-26; original FAMILY/PUSH statements",
         content_change="References only, with no new hypothesis or mathematical strengthening."),
    dict(id="D-credit", results=["D.2.5", "D.2.6", "D.2.7", "D.2.8", "D.2.9", "D.2.10", "D.2.11", "D.3.1", "D.3.4"],
         reason="State known geometric antecedents at their opened original locators and remove prohibited priority narration.",
         evidence="work/invariants_arithmetic/maps_D_references_verified.json; maps_D_credit_comparison.json",
         content_change="Added scoped source credit and neutral wording; distinct complete derivations retained."),
]


def transform(s: str) -> str:
    """Return the corrected original D text; fail closed on a changed source."""
    if s.startswith(BEGIN_MARKER):
        if not s.endswith(END_MARKER):
            raise ValueError("Incomplete MAPS D correction marker")
        return s
    ids = [m[1] for m in HEAD.finditer(s)]
    expected = ([f"D.1.{i}" for i in range(1, 13)]
                + [f"D.2.{i}" for i in range(1, 54)]
                + [f"D.3.{i}" for i in range(1, 5)])
    if ids != expected:
        raise ValueError("MAPS D transform requires all 69 expanded original results in order")
    if re.search(r"\\input\{", s):
        raise ValueError("MAPS D transform requires recursively expanded input")

    s = _replace(s,
        "We use the all-twist comparison R1, whose sufficient step is the\n"
        "integral norm equation and analytic torsor gluing in S6\\_02,\nB.2.1.",
        r"We use the all-twist comparison in \cref{fam:src:B.2.1}, whose sufficient step is the "
        "integral norm equation and analytic torsor gluing.")
    s = _replace(s, "use R1's biholomorphism at this aligned parameter,",
        r"use the biholomorphism of \cref{fam:src:B.2.1} at this aligned parameter,")
    s = _replace(s, "R1 makes the map to $W$ an exact biholomorphic classification.",
        r"By \cref{fam:src:B.2.1,fam:src:C.2.3}, the map to $W$ is an exact biholomorphic classification.")
    s = _replace(s, "properness argument of S6\\_02 A.3.1 uses a bounded correction",
        r"properness argument of \cref{fam:src:A.3.1} uses a bounded correction")
    s = _replace(s,
        "the checked dictionary K1 and R4 instead give $2k\\ell$ at fixed\n"
        "$u$ for the pair $(3k,4\\ell)$. K12 supplies tangent cohomology\n"
        "$(1,1,1,0)$ and Kodaira dimension determined by the sign of",
        r"the dictionary in \cref{push:src:E.1.1} and the classification in \cref{fam:src:B.3.1} give $2k\ell$ at fixed "
        r"$u$ for the pair $(3k,4\ell)$. The tangent computation in \cref{push:src:E.2.1} gives "
        r"$(1,1,1,0)$, and \cref{push:src:E.2.2} determines the Kodaira dimension by the sign of")
    s = _replace(s,
        "Euler additivity gives the claim. This is K15's actual localization\nargument, applied to the present cells.",
        "Euler additivity gives the claim, applying the localization argument to the stated cells.")
    s = _replace(s, "construction of K11, with",
        r"construction of \cref{push:src:E.5.2,push:src:E.5.3}, with")
    s = _replace(s, "The geometric input is K11, checked against",
        r"The geometric input is the construction in \cref{push:src:E.5.2,push:src:E.5.3}, with the original geometric statements in")

    s = _replace(s, "untwisted K13 groups", r"untwisted groups of \cref{push:src:A.4.2}")
    s = _replace(s, "K13, including its integral freeness.",
        r"\cref{push:src:A.4.2}, including its integral freeness.")
    s = _replace(s, "independently recovering K13 and", r"independently recovering \cref{push:src:A.4.2} and")
    s = _replace(s, "At $d=1$ this is exactly K13;", r"At $d=1$ this is exactly \cref{push:src:A.4.2};")
    s = _replace(s, "with the direction of $T$ fixed in K13. We write $X^{\\log}(u)$ for\n"
        "the logarithmically transformed sphere, keeping it distinct from K13's\nuntwisted $X(u)$.",
        r"with the direction of $T$ fixed in \cref{push:src:A.1.2}. We write $X^{\log}(u)$ for "
        r"the logarithmically transformed sphere, and $X(u)$ for the untwisted fibre of \cref{push:src:A.1.2,push:src:A.2.2}.")
    s = _replace(s, "It is transverse to, and different from, K13's $u\\to0$ degeneration.",
        r"It is transverse to the $u\to0$ degeneration of \cref{push:src:A.1.2}.")
    s = _replace(s, "K13, A.1.2, against Engel's Lemma 2.1 and Corollary 2.2.",
        r"\cref{push:src:A.1.2}, using Engel's Lemma~2.1 and Corollary~2.2 \cite{manEngel26}.")
    s = _replace(s, "Its small resolution is the diagonal subdivision of\nK13.",
        r"Its small resolution is the diagonal subdivision of \cref{push:src:A.2.1,push:src:A.2.2}.")
    s = _replace(s, "The comparison with K13 identifies its small resolution with the",
        r"The comparison with \cref{push:src:A.1.2,push:src:A.2.2} identifies its small resolution with the")
    s = _replace(s, "are the precise comparison with K13.",
        r"are the precise comparison with \cref{push:src:A.1.2,push:src:A.2.2}.")

    s = _append_to_result(s, "D.2.1", r"""
The existence of the configurations is supplied by Miranda's list;
the exact geometric realization of the archived positive peripheral
matrices and primitive section cocycles for the profiles $50/II$ and
$56/II$ is supplied by \cref{mapsD:repair:collision-realization}.
That complete proof constructs the modular covers and rational elliptic
surfaces, fixes the peripheral loops before imposing cone relations,
and identifies the integral cocycles with actual sections.  The matrix
product and Smith checks in the preceding finite filtering are used
for their stated algebraic roles.
""")
    s = _append_to_result(s, "D.2.2", r"""
For the archived computation, all fifty exact request payloads and
saved API-v2 replies were regenerated and compared, giving the stated
$24$ simply connected outputs, $26$ other outputs and three outputs
with the integral cohomology of a sphere; the eight specified clutch
comparisons were checked as well.
This is an audit of the retained requests and responses.  The attempted
fresh remote request timed out, so it supplies no additional response
or geometric validation.  The independent geometric input for the two
collision profiles is \cref{mapsD:repair:collision-realization}.
""")

    s = _replace(s,
        "The full D.2 request remains open for nonprimitive-long-circle\n"
        "and other logarithmic star data, corrected original multiplicative\n"
        "caps, the remaining torsion-valued original additive markings,\n"
        "and the complete smooth invariants of the remaining weighted and\n"
        "additional-regular-log outputs.",
        "The full D.2 request remains open for nonprimitive-long-circle\n"
        "and other logarithmic star data, corrected original multiplicative\n"
        "caps, and the mixed elliptic--$\\gamma$ and second fixed-normal\n"
        "torsion columns of the original additive caps when $h>1$ in D.2.51.\n"
        "The complete smooth invariants of the remaining weighted and\n"
        "additional-regular-log outputs are also undetermined.")
    s = _replace(s,
        "its reference framing and critical-specialization linking remain\nunder examination.",
        "its embedded representative, reference framing and critical-specialization\nlinking are not computed here.")
    s = _replace(s,
        "The other active attacks compute the unresolved original-cap\n"
        "torsion markings and the smooth invariants of the new star-log\n"
        "families.",
        "The unresolved original-cap torsion markings and the complete smooth\n"
        "invariants of the remaining star-log families are separate open tasks.")
    s = _replace(s,
        "Nor does (D.ST13)\nclassify every nonsphere smooth output: the unrestricted\n"
        "nonprimitive finite-log homology and the general $c>1$ smooth\nclassification remain distinct tasks.",
        "Formula (D.ST13) concerns the sphere outputs. The unrestricted\n"
        "finite-log homology is supplied in D.2.29--33, and the entire specified\n"
        "minimal simply connected smooth sector is completed by D.2.35--36,\n"
        "D.2.38--39, D.2.42 and D.2.44--45. The remaining weighted and\n"
        "additional-regular-log smooth classification is scoped in D.2.4.")
    s = _append_to_result(s, "D.2.37",
        "The shared-even-factor case excluded from the stated formula is handled by the complete integral algorithm of D.2.41.")
    s = _append_to_result(s, "D.2.40",
        "The shared-even-factor case outside the odd-iterate statement is included in D.2.41.")
    s = _replace(s, "In particular it is not yet an\nunrestricted global gluing algorithm for those caps.",
        "In particular it does not supply an\nunrestricted global gluing algorithm for those caps.")

    for sid, paragraph in {
        "D.2.5": r"The logarithmic quotient and its marked local filling are those of \cite[Proposition~2.3]{manViaclovskyLogs26}; the original integral homology case is \cite[Proposition~4.1]{manViaclovskyLogs26}. The unrestricted determinant and torsion calculation above retains the complete integer boundary maps.",
        "D.2.7": r"The order-three geometric model and its original surgery calculation are given in \cite[Theorem~7.1 and Appendix~B]{manWang26}. The present comparison retains the primitive $I_2$ period $(2,1)$, which becomes $(1,0)$ under $(x,y)=(v,v^2/z)$; it is not replaced by the zero-weight $I_2$ archival API choice.",
        "D.2.9": r"The product type-$II$ cap and the original marked torus monodromy are established in \cite[Lemma~3.10 and Propositions~3.11, 3.13]{manLR26}. The proof above gives the full indicated $3k$ family in that marking.",
        "D.2.11": r"The local Type-C geometric input is supplied by \cite[Propositions~3.1, 3.4, 3.6, 4.4 and Appendix~B.4]{manYang26}; the product type-$II$ marking is supplied by \cite[Lemma~3.10 and Propositions~3.11, 3.13]{manLR26}. The unrestricted $3P$ calculations use the explicitly displayed boundary maps.",
        "D.3.1": r"Engel's general zero/pole construction is stated in \cite[Remark~8.5]{manEngel26}; his Remark~8.1 concerns the separate degeneration as $u$ tends to zero. The full moving-section plumbing and its geometric comparisons are proved above.",
    }.items():
        s = _append_to_result(s, sid, paragraph)
    s = _replace(s,
        "The smoothing's algebraic dimension one does not give a first\n"
        "existence result for complex structures with $a=1$ on $S^3\\times S^3$.\n"
        "Such examples occur in \\cite[Example~2.3]{manCDP98}. The present\n"
        "smoothing is nevertheless not biholomorphic to the displayed\n",
        "Complex structures with $a=1$ on $S^3\\times S^3$ are constructed in\n"
        "\\cite[Example~2.3]{manCDP98}. The present smoothing is not\n"
        "biholomorphic to the displayed\n")
    s = _drop_priority_metadata(s)
    if [m[1] for m in HEAD.finditer(s)] != ids:
        raise AssertionError("D result headings changed")
    if re.search(r"(?<!D\.)\b(?:K(?:1|11|12|13|15)|R1)\b", s):
        raise AssertionError("Unresolved checkpoint shorthand in corrected D source")
    return BEGIN_MARKER + s + "\n" + END_MARKER
