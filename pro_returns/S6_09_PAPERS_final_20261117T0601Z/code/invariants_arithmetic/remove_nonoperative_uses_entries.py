#!/usr/bin/env python3
"""Remove only five explicitly nonoperative comparisons from three I Uses lines."""
from pathlib import Path
import argparse
import hashlib
import json
import re

PACKAGE = Path(__file__).resolve().parents[2]
TARGET = PACKAGE / "S6_09_PAPERS_I.tex"
WORK = PACKAGE / "work/invariants_arithmetic"
CHANGES = [
    {
        "statement": "ari:C.6.4",
        "remove": [
            r"\citep{tate1983variation}",
            r"\citet{silverman1983specialization}",
        ],
        "body_scope": "Printed proof paragraphs beginning 'We spell out the comparison with the opened primary author sources' through the end of the proof; read in full, current lines6314–6343.",
        "application_check": (
            "The bounded remainder and local normalization are proved using the fully opened "
            "DeMarco–Mavraki Theorems1.1,2.2,2.3. Call–Silverman1993 Theorem4.1 and its following "
            "remark, and Silverman's2006 slides21–22, supply explicit author reproductions for "
            "the historical comparison. The original Tate1983 and Silverman1983 scans were not "
            "read; neither original is an operative proof dependency."
        ),
        "read_anchor_start": "We spell out the comparison with the opened primary author sources.",
        "read_anchor_end": "remain the cited proof.",
    },
    {
        "statement": "ari:C.6.R4",
        "remove": [r"\citep{CrRubin1991}"],
        "body_scope": "Complete paragraph group 'The scope of Rubin's theorem', current lines6767–6804; the exact three leading factors are separately derived from Miller2011.",
        "application_check": (
            "Rubin1991 is an attribution and bibliographic comparison only: the complete original "
            "theorem text was unavailable, and the paragraph expressly bases no additional "
            "hypothesis-free claim on it. The opened formulations are BDP2012 Theorem1 and "
            "Castella2025 TheoremA, with their ordinary-prime and conductor restrictions. The "
            "three exact Sha/leading-factor cases use Miller2011 Theorem1.2 and Table9; the "
            "remaining analytic quotient uses the separate denominator proof."
        ),
        "read_anchor_start": r"\paragraph{The scope of Rubin's theorem.}",
        "read_anchor_end": "remains a separate arithmetic question in that row.",
    },
    {
        "statement": "ari:C.7.7",
        "remove": [
            r"\citet[Corollary 3]{bertrand1984}",
            r"\citet{pham2025sigma}",
        ],
        "body_scope": "Complete theta-lift qualification current lines9406–9440; current-source paragraph9540–9550; complete operative appendix proof of C.7.7, plus attribution distinction in C.7.8.",
        "application_check": (
            "The C.7.7 assertions use Waldschmidt1979 Theorem1/Corollary1 and Huber–Wüstholz2022 "
            "Theorem6.1, with the full receiving derivation in the appendix. The unrestricted-lift "
            "inference attributed to Bertrand1984 Corollary3 is explicitly withdrawn; neither "
            "direction is used. Pham2025 has only opened metadata/abstract/reference list and "
            "no checked theorem, so is expressly a potentially relevant unverified comparison. "
            "The separate ordinary p-adic theorem attributes Bertrand via the actually opened "
            "Rubin appendix to Agboola2006, TheoremA.1/LemmaA.2; that body attribution is retained."
        ),
        "read_anchor_start": r"\paragraph{A theta criterion requiring its original normalization.}",
        "read_anchor_end": "source: we make no claim either that it settles the Gaussian\nnorm question or that its results are inapplicable to it.",
    },
]


def sha(s):
    return hashlib.sha256(s.encode()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    before = TARGET.read_text()
    after = before
    records = []
    for item in CHANGES:
        marker = r"\label{" + item["statement"] + "}"
        start = after.index(marker) + len(marker)
        match = re.search(r"^\\Uses\{[^\n]*\}$", after[start:], re.M)
        if not match:
            raise ValueError("Uses line absent for " + item["statement"])
        a, b = start + match.start(), start + match.end()
        old = after[a:b]
        new = old
        states = []
        for citation in item["remove"]:
            n = new.count(citation)
            if n == 1:
                atom = "; " + citation
                if new.count(atom) != 1:
                    raise ValueError("Unexpected Uses delimiter: " + citation)
                new = new.replace(atom, "", 1)
                states.append("removed")
            elif n == 0:
                states.append("already absent")
            else:
                raise ValueError("Ambiguous citation multiplicity: " + citation)
        begin = before.index(item["read_anchor_start"])
        end = before.index(item["read_anchor_end"], begin) + len(item["read_anchor_end"])
        scope = before[begin:end]
        records.append({
            **item, "before": old, "after": new, "states": states,
            "Uses_line_before": before[:before.index(old)].count("\n")+1,
            "opened_printed_scope_sha256": sha(scope),
            "opened_printed_scope_start_line": before[:begin].count("\n")+1,
            "opened_printed_scope_end_line": before[:end].count("\n")+1,
        })
        after = after[:a] + new + after[b:]
    # Stronger than a formula-only check: every byte outside Uses is unchanged.
    mask = lambda s: re.sub(r"^\\Uses\{[^\n]*\}$", "@@USES@@", s, flags=re.M)
    if mask(before) != mask(after):
        raise ValueError("Text outside Uses changed")
    old_uses = re.findall(r"^\\Uses\{[^\n]*\}$", before, re.M)
    new_uses = re.findall(r"^\\Uses\{[^\n]*\}$", after, re.M)
    changed = sum(a != b for a, b in zip(old_uses, new_uses))
    if len(old_uses) != len(new_uses) or changed not in {0,3}:
        raise ValueError("Unexpected number of Uses changes")
    keys = ["tate1983variation","silverman1983specialization","CrRubin1991",
            "bertrand1984","pham2025sigma"]
    remaining = [
        line for line in new_uses
        if any(re.search(r"\{[^}]*\b" + re.escape(key) + r"\b[^}]*\}", line) for key in keys)
    ]
    if remaining:
        raise ValueError("Nonoperative key still present in a Uses line")
    if TARGET.read_text() != before:
        raise RuntimeError("I.tex changed concurrently; rerun")
    report = {
        "reviewer": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
        "effort": "Pro", "date_utc": "2026-11-17",
        "scope": "Exact five nonoperative citation removals from three dependency-only Uses lines",
        "target": "S6_09_PAPERS_I.tex", "applied": args.apply,
        "before_sha256": sha(before), "after_sha256": sha(after),
        "changed_Uses_lines": changed, "citation_entries_removed": 5 if changed else 0,
        "every_byte_outside_Uses_unchanged": True,
        "body_comparisons_bibliography_statements_proofs_preserved": True,
        "remaining_nonoperative_Uses_entries": [], "records": records,
    }
    WORK.mkdir(parents=True, exist_ok=True)
    if args.apply:
        temp = TARGET.with_suffix(".tex.tmp")
        temp.write_text(after)
        temp.replace(TARGET)
    (WORK / "paper_I_nonoperative_Uses_corrections.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2)+"\n"
    )
    print(json.dumps({
        "applied": args.apply, "changed_Uses_lines": changed,
        "citation_entries_removed": report["citation_entries_removed"],
        "all_other_text_byte_preserved": True,
    }))


if __name__ == "__main__":
    main()
