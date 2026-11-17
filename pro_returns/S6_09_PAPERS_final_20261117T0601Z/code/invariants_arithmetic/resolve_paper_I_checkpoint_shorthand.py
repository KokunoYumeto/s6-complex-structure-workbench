#!/usr/bin/env python3
"""Resolve historical prompt shorthand in the assembled Paper I only.

Default: produce a reviewable candidate and exact before/after manifest.
--apply: atomically replace the assembled I.tex after all guards pass.
No inventory, source original, assembler or mathematical display is changed.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from pathlib import Path

PACKAGE = Path(__file__).resolve().parents[2]
WORK = PACKAGE / "work/invariants_arithmetic"
TARGET = PACKAGE / "S6_09_PAPERS_I.tex"

# Literal substitutions prevent one run's K/Lead register being mistaken for
# another. The operative checkpoint table is specific to ARITHMETIC.
REPLACEMENTS = [
    ("fam:A4.1",
     "Thus the full generic Albanese cross-check of Lead 3 holds independently of the centralizer calculation.",
     "Thus the generic Albanese invariants recover the parameter modulo its exact period subgroup, independently of the centralizer calculation."),
    ("fam:D1.3",
     "The assertion in Lead 6 that",
     "The proposed assertion that"),
    ("inv:A2.3",
     "Thus the formula in Lead 3 is",
     "Thus the displayed Eichler--Zagier integral formula is"),
    ("inv:A2.4",
     r"\begin{proposition}[The global rank and Lead 2]",
     r"\begin{proposition}[The global rank and the decisive scalar]"),
    ("inv:D4.2",
     "and the integer $r$ in\nLead 5 equals one there.",
     "and the cusp nilpotence exponent $r$ equals one there."),
    ("ari:C1.1",
     "This also checks the precise normalization in checkpoint K1;\nits kernel, Laplacian and mean-zero argument are all valid.",
     r"This also checks the precise normalization of the special-value calculation in Proposition~\ref{push:src:D.4.5};"
     "\nits kernel, Laplacian and mean-zero argument are all valid."),
    ("ari:C1.2",
     "We use the checked K1 calculation, rather than treat its modulus as an\nopen question: multiplication by",
     r"The special-value calculation in Proposition~\ref{push:src:D.4.5}"
     "\nuses multiplication by"),
    ("ari:C2.1a",
     "We checked checkpoint K2's step giving $q_2=iw/216$: its factor\n$1/2$ is exactly the Albanese projection just computed. Its\nnatural-boundary proof uses modular invariance at rational boundary\npoints and is valid.",
     r"The identity $q_2=iw/216$ in Proposition~\ref{push:src:D.1.1} has"
     "\nfactor $1/2$ precisely because of the Albanese projection just computed."
     "\nIts natural-boundary proof uses modular invariance at rational boundary"
     "\npoints."),
    ("ari:C2.1b",
     "same rational-cusp argument checked in K2.",
     r"rational-cusp argument proved in Proposition~\ref{push:src:D.1.1}."),
    ("ari:C3.1a",
     "In particular the leading terms of K3 and Lead 9 are correct.",
     r"In particular the leading terms agree with the boundary expansion in Lemma~\ref{push:src:D.2.1}."),
    ("ari:C3.1b",
     "The exact coefficients checked in K3 are",
     r"The exact half-period coefficients used in Lemma~\ref{push:src:D.2.1} are"),
    ("ari:C3.2a",
     "We use K4 after checking its differentiation: put",
     r"We rederive the differentiation in Proposition~\ref{push:src:D.4.4}: put"),
    ("ari:C3.2b",
     "These equations are equivalent to K4's factored formula and verify\nits normalizations.",
     r"These equations give the factored formula of Proposition~\ref{push:src:D.4.4}"
     "\nwith its stated normalizations."),
    ("ari:C8.local",
     "The identity of K3, checked by differentiating $e$ and using\nthe theta heat equation, reads",
     r"The half-period identity used in Lemma~\ref{push:src:D.2.1},"
     "\nobtained by differentiating $e$ and using the theta heat equation, reads"),
    ("ari:C8.9a",
     "Thus the form $da\\wedge db$ in Lead 15(b) has the wrong sign.",
     "Thus the proposed form $da\\wedge db$ has the wrong sign."),
    ("ari:C8.9b",
     "At $t=1$ put $h=\\mu-(1-\\tau)/2$. The checked K3 expansion\nand the modular $j$ expansion give",
     r"At $t=1$ put $h=\mu-(1-\tau)/2$. The expansion in Proposition~\ref{ari:C.3.1}"
     "\nand the modular $j$ expansion give"),
    ("ari:C8.10",
     "Thus the probability-limit assertion\nin Lead 15(b) requires the factor $12$.",
     "Thus the probability limit requires the factor $12$."),
    ("ari:C8.11a",
     "The critical-point factors in K4 follow with their stated\nnormalization after multiplying by $6/\\pi$.",
     r"Multiplication by $6/\pi$ gives the critical-point factorization for"
     "\n" + r"$D_{\rm part}$ in Proposition~\ref{push:src:D.4.4}."),
    ("ari:C8.11b",
     "These computations also independently verify the K4 step\nused in C.3; its apparent singularity at a half-period is",
     r"These computations independently verify the differential formula used in Proposition~\ref{ari:C.3.2};"
     "\nits apparent singularity at a half-period is"),
    ("ari:C7.CM",
     "The holomorphic theta normalization in Lead 16(e) differs from the",
     "The holomorphic theta normalization proposed for the CM interpolation approach differs from the"),
    ("ari:C7.interpolation",
     "The generic finite-order interpolation approach in Lead 16(e)",
     "The generic finite-order interpolation approach"),
    ("push:A3.3",
     r"The assertion in Lead 3, or \ref{push:section:A.3}(iii), that the two natural",
     "The assertion that the two natural"),
    ("push:A4.3",
     r"\begin{proposition}[pointwise correction to Lead 1]",
     r"\begin{proposition}[the pointwise nearby Euler function]"),
    ("push:B1.1",
     "The product assertion in Lead 4 is false on the whole root\ndisc.",
     "The assertion that the filling is the product of the smooth elliptic\n"
     "family with a twelve-gon Tate model is false on the whole root disc."),
    ("push:B3.1a",
     r"\begin{theorem}[counterexample; Lead 5]",
     r"\begin{theorem}[counterexample to simultaneous gluing]"),
    ("push:B3.1b",
     "neighbourhoods. In particular Lead 5's asserted\nsimultaneous gluing is false.",
     "neighbourhoods. In particular the proposed simultaneous gluing is false."),
    ("push:D1.3",
     r"\begin{theorem}[Lead 8]",
     r"\begin{theorem}[nonextension across the parameter boundary]"),
    ("push:D2.1",
     "quadratic coefficient that the first-order Lead~9 omitted.",
     "quadratic coefficient omitted by the proposed first-order approximation."),
    ("push:D2.2a",
     r"\begin{proposition}[counterexample; Lead 9]",
     r"\begin{proposition}[nonseparation beyond the rank-drop line]"),
    ("push:D2.2b",
     "The assertion in Lead~9 that total-space nonseparation is confined to",
     "The assertion that total-space nonseparation is confined to"),
    ("ari:C5.boundary",
     "This proves Lead 11, including its\ntwist and boundary qualifications.",
     "This proves the CM-torsion assertion, including its\n"
     "twist and smooth-boundary-model qualifications."),
    ("program:ab_push_fan",
     "Exact enumeration of the no-new-ray triangulations in Lead 2.",
     "Exact enumeration of the no-new-ray triangulations of the prescribed periodic prism fan."),
    ("ari:open:norm",
     "Further attempts and the\nCM theta comparison are recorded below as they are tested.",
     r"The attempted approaches and the exact CM theta comparison are printed in the preceding period and CM-normalization sections;"
     "\ntheir source checks and computational records are retained in the audit files."
     "\nThese arguments do not resolve the stated exclusion."),
]


def sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def displays(s: str) -> list[str]:
    # Preserve every complete mathematical display byte for byte.
    pattern = (
        r"\\\[.*?\\\]|"
        r"\\begin\{(equation\*?|align\*?|gather\*?|multline\*?|displaymath)\}"
        r".*?\\end\{\1\}"
    )
    return [m[0] for m in re.finditer(pattern, s, re.S)]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    before = TARGET.read_text()
    current = before
    changes = []
    for key, old, new in REPLACEMENTS:
        n = current.count(old)
        if n == 1:
            line = current[:current.index(old)].count("\n") + 1
            current = current.replace(old, new, 1)
            state = "replaced"
        elif n == 0 and current.count(new) == 1:
            line = current[:current.index(new)].count("\n") + 1
            state = "already applied"
        else:
            raise ValueError(f"{key}: old count={n}, new count={current.count(new)}")
        changes.append({
            "scope_id": key, "state": state, "line_at_application": line,
            "before": old, "after": new,
        })
    if displays(before) != displays(current):
        raise ValueError("A mathematical display changed")
    oldlabels = re.findall(r"\\label\{([^}]+)\}", before)
    newlabels = re.findall(r"\\label\{([^}]+)\}", current)
    if oldlabels != newlabels:
        raise ValueError("A label changed")
    proofpat = r"\\(?:begin|end)\{proof\}"
    if re.findall(proofpat, before) != re.findall(proofpat, current):
        raise ValueError("The proof environments changed")
    leftovers = []
    for n, line in enumerate(current.splitlines(), 1):
        if re.search(r"\bLead(?:\s|~)*\d+|checkpoint\s+K\d+", line):
            leftovers.append({"line": n, "text": line})
    if leftovers:
        raise ValueError(f"Historical Lead/checkpoint aliases remain: {leftovers}")
    labels = set(newlabels)
    introduced_refs = sorted({
        lab for _, _, new in REPLACEMENTS
        for group in re.findall(r"\\(?:ref|cref|eqref)\{([^}]+)\}", new)
        for lab in group.split(",")
    })
    missing = [lab for lab in introduced_refs if lab not in labels]
    if missing:
        raise ValueError(f"Introduced references absent from I: {missing}")
    if TARGET.read_text() != before:
        raise RuntimeError("I.tex changed during review; rerun without applying")
    WORK.mkdir(parents=True, exist_ok=True)
    candidate = WORK / "paper_I_checkpoint_shorthand_candidate.tex"
    candidate.write_text(current)
    report = {
        "prepared_by": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
        "effort": "Pro", "date_utc": "2026-11-17",
        "target": "S6_09_PAPERS_I.tex",
        "source_before_sha256": sha(before),
        "candidate_after_sha256": sha(current),
        "applied": args.apply,
        "literal_substitutions": changes,
        "all_displayed_mathematics_byte_preserved": True,
        "display_count": len(displays(before)),
        "all_labels_in_order_preserved": True,
        "complete_proof_environments_preserved": True,
        "introduced_refs_found": introduced_refs,
        "operative_original_alias_sources": [
            "sources/prompts/S6_01_INVARIANTS/history_and_work/PROMPT_before_audit_20261112.md: Leads 2,3,5",
            "sources/prompts/S6_02_FAMILY/history_and_work/PROMPT_before_audit_20261112.md: Leads 3,6",
            "sources/prompts/S6_02_PUSH/PROMPT.md: Leads 1-5,8-9",
            "sources/prompts/S6_05_ARITHMETIC/PROMPT.md: Leads 9,11,15(b),16(e)",
            "sources/per_prompt/S6_05_ARITHMETIC/S6_CHECKPOINT_01_20261115.md: K1-K4",
        ],
        "deliberately_retained": [
            "Chen's published hypothesis (K1), Definition 2.3; not a checkpoint alias",
            "K3 surfaces in bibliography titles; not a checkpoint alias",
        ],
    }
    if args.apply:
        temp = TARGET.with_suffix(".tex.tmp")
        temp.write_text(current)
        temp.replace(TARGET)
    (WORK / "paper_I_checkpoint_shorthand_changes.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    )
    print(json.dumps({
        "changes": len(changes), "applied": args.apply,
        "math_displays_preserved": report["display_count"],
        "labels_preserved": len(oldlabels),
        "candidate": str(candidate),
    }))


if __name__ == "__main__":
    main()
