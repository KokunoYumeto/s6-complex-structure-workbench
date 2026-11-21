#!/usr/bin/env python3
"""Generate Paper V deposit fields from its current abstract and recomputed ledger.

Submission acknowledgments are not made by this file generator. The delivered
fields are the substantive metadata requested in the publication prompt.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT.parents[2]
COMMIT = "83d76022bcd442278b760db9ff438afceed6c6ea"
PIN = "https://github.com/KokunoYumeto/s6-complex-structure-workbench/tree/" + COMMIT


def main():
    source = BASE / "work/S6_SERIES_PUBLISH_V.tex"
    text = source.read_text()
    original = json.loads((BASE / "source/HEXAGON_METADATA_V.json").read_text())
    start, end = text.index(r"\begin{abstract}") + len(r"\begin{abstract}"), text.index(r"\end{abstract}")
    abstract = " ".join(text[start:end].split())
    stats = list(csv.DictReader((ROOT / "records_current_V/S6_SERIES_PUBLISH_check_counts.tsv").open(), delimiter="\t"))
    row = next(x for x in stats if x["paper"] == "V" and x["scope"] == "current_printed_statements_and_definitions")
    counts = {key:int(row[key]) for key in ["targeted proof check", "independent re-proof", "computation or formal certificate",
                                          "used and rechecked in this run", "carried as background without fault found",
                                          "event_associations", "statements", "subject_identifiers", "outline_step_associations_separate"]}
    events = list(csv.DictReader((ROOT / "records_current_V/CHECK_EVENTS.tsv").open(), delimiter="\t"))
    outline = [x for x in events if re.match(r"series:V:[A-F] step ", x["statement_id"])]
    outline_targeted = sum(x["type"] == "targeted proof check" for x in outline)
    outline_reproof = sum(x["type"] == "independent re-proof" for x in outline)
    assert len(outline) == counts["outline_step_associations_separate"]
    comments = (
        'Paper V of the five-paper series "The (3,4,∞) family of complex six-spheres". '
        'The main result constructs compact complex fourfolds diffeomorphic, with their complex orientation, '
        'to 3HP²#(−HP²). The series begins with the complex six-spheres of Claude and L. Alpöge '
        '(https://alpo.ge/s6.pdf). Principal related inputs used here are Engel’s elliptic-surface construction '
        '(arXiv:2609.38442v1), the weighted-base and direct-image method of Du, Guo, Kusakabe and Xie '
        '(arXiv:2610.00250v1), Yang’s toroidal fillings (arXiv:2609.29666v1), '
        'the smooth classification of Conway, Crowley, Powell and Sixt '
        '(doi:10.1017/S1446788722000167), and Kramer–Stolz sphere absorption. '
        f'Historical source editions, programs, outputs and check records are at {PIN}. '
        'The additional records and programs of the publication revision accompany its source distribution.'
    )
    provenance = (
        'Text: AI-authored; none of it was written by a human. The submitter takes responsibility for the veracity of the text.\n\n'
        'How it was produced. GPT-5.6 Sol (OpenAI), in Codex at reasoning effort ultra, wrote the working edition '
        'on 24 August–9 September 2026. GPT-6 Astra (OpenAI), in ChatGPT Pro mode, carried out the research '
        'of 12–16 November 2026, an independent derivation of 16–18 November, and the writing of 16–20 November. '
        'GPT-6 Astra undertook the publication revision and further checks on 20 November 2026. '
        'The reasoning-effort setting of this publication session was inherited; the interface exposed no '
        'separate numerical setting. Claude Fable 5.2 (Anthropic), at effort high and at effort max, and '
        'Claude Opus 5.5 (Anthropic), at effort max, undertook readings, intakes, checks and recomputations '
        'on 12–20 November 2026. Their recorded objections and calculations were compared with the '
        'statements, proofs and primary sources, and the resulting corrections were incorporated.\n\n'
        'How it was checked. For the statement scopes retained in the current paper, the merged record contains '
        f'{counts["targeted proof check"]} examinations of proof steps, '
        f'{counts["independent re-proof"]} independent re-derivations, and '
        f'{counts["computation or formal certificate"]} computations or formal certificates. '
        f'It records {counts["used and rechecked in this run"]} further readings and '
        f'{counts["carried as background without fault found"]} uses of previously examined background results. '
        f'Another {outline_targeted} proof examinations and {outline_reproof} re-derivations are associated '
        'specifically with steps of the introductory outlines. These totals count recorded links from a check '
        'to a statement: one calculation applied to several statements can contribute several links. '
        'Consolidated statements retain their historical identifiers, and each original association is counted once. '
        'Each outcome identifies the passage or computation examined. The 20 November Opus review followed '
        'selected period, rational-cohomology and smooth-classification arguments and the Oka-theoretic passage; '
        'its record identifies the integral-topology steps left unchecked. The Fable review compared the '
        'introductory statements and outlines for the resolved fourfold and parameter family with the body '
        'statements they cite. The current revision adds independent integer calculations and scoped proof '
        'checks. For the period minimum, the records specify the interval-certificate calculation, '
        'a separately implemented numerical comparison, and exact checks of finite coverage and sign inequalities. '
        'These current computations were performed under GPT-6 Astra.\n\n'
        'Human understanding. No human has checked the mathematics. The literature used as input is credited '
        'at its exact statements and pages; the new construction and its scope are stated separately in the paper.\n\n'
        f'Records. The historical source editions, programs, outputs and check records are available at {PIN}. '
        'The additional records and programs of this publication revision accompany its source distribution. '
        'The text and accompanying work are dedicated to the public domain under CC0 1.0 Universal '
        '(https://creativecommons.org/publicdomain/zero/1.0/).'
    )
    metadata = {key: original[key] for key in ["title", "subject", "crossListSubjects", "tags", "mscCodes",
                                             "authorshipMode", "authors", "humanUnderstanding", "license"]}
    metadata.update(abstract=abstract, comments=comments, provenance=provenance,
                    aiSystems=[
                        {"provider":"OpenAI", "model":"GPT-5.6 Sol (Codex, reasoning effort ultra)", "version":None},
                        {"provider":"OpenAI", "model":"GPT-6 Astra (ChatGPT Pro mode; current reasoning effort inherited, no separate numerical setting exposed)", "version":None},
                        {"provider":"Anthropic", "model":"Claude Fable 5.2 (effort high and max)", "version":None},
                        {"provider":"Anthropic", "model":"Claude Opus 5.5 (effort max)", "version":None},
                    ])
    (ROOT / "S6_SERIES_PUBLISH_deposit_fields_V.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n")
    md = ["## Paper V", "", "### Title", "", metadata["title"], "", "### Abstract", "", abstract,
          "", "### Comments", "", comments, "", "### Provenance", "", provenance,
          "", "### Subjects and classification", "",
          f'- Primary subject: {metadata["subject"]}',
          '- Cross-lists: ' + ", ".join(metadata["crossListSubjects"]),
          '- MSC codes: ' + ", ".join(metadata["mscCodes"]),
          '- Tags: ' + "; ".join(metadata["tags"]),
          '- Authorship mode: ' + metadata["authorshipMode"],
          '- Human understanding field: ' + metadata["humanUnderstanding"],
          '- Licence: CC0 1.0 Universal', ""]
    (ROOT / "S6_SERIES_PUBLISH_deposit_fields_V.md").write_text("\n".join(md))
    receipt = {
        "created_utc":datetime.now(timezone.utc).isoformat(), "source":str(source.relative_to(BASE)),
        "source_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
        "original_metadata_sha256":hashlib.sha256((BASE / "source/HEXAGON_METADATA_V.json").read_bytes()).hexdigest(),
        "merged_ledger_sha256":hashlib.sha256((ROOT / "records_current_V/CHECK_EVENTS.tsv").read_bytes()).hexdigest(),
        "merged_ledger_rows":len(events), "scope":row["scope"], "counts":counts,
        "outline_targeted":outline_targeted,"outline_reproof":outline_reproof,
        "abstract_transformation":"Whitespace join only; every mathematical character and word is taken from the current abstract.",
        "final_refresh_gate":"Regenerate after any later event or manuscript-scope change; this receipt identifies the exact current snapshot.",
        "submission_flags":"No correctness, community-interest, citation or rights confirmation is made by generating these substantive metadata fields."
    }
    (ROOT / "S6_SERIES_PUBLISH_deposit_fields_V_receipt.json").write_text(json.dumps(receipt,indent=2)+"\n")
    print(json.dumps(receipt,indent=2))


if __name__ == "__main__": main()
