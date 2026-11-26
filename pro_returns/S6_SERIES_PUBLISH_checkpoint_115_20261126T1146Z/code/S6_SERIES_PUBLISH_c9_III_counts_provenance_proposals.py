#!/usr/bin/env python3
"""Prepare exact III methodology/deposit/provenance replacements.

Run only after root declares the statement-event admissions count-ready.
Writes temporary proposals and the actual count result outside the working
tree; root admits the latter once at its canonical records path. This
program never writes the manuscript, shared tables, deposit or count master.
The separate final-layout generator remains held for the final PDF/aux.
"""
from pathlib import Path
import csv
import io
import json
import re
import sys
import textwrap

sys.dont_write_bytecode = True
import S6_SERIES_PUBLISH_c9_III_check_counts as counts

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "agents/continuation9_counts"
TEMP_PROPOSALS = ROOT.parent.parent / "tmp/c9_counts_provenance/S6_SERIES_PUBLISH_c9_III_counts_provenance_proposals.json"
TEMP_COUNT_RESULT = ROOT.parent.parent / "tmp/c9_counts_provenance/S6_SERIES_PUBLISH_III_current_check_counts.json"
SOURCE = "S6_SERIES_PUBLISH_III.tex"
DEPOSIT = "S6_SERIES_PUBLISH_deposit_fields_III.json"
MARKDOWN = "S6_SERIES_PUBLISH_deposit_fields.md"
PROVENANCE = "S6_SERIES_PUBLISH_provenance_checks.tsv"
REPLAY_EVENT = "publish:c9:III:02KU:matrix-replay"
REVIEW = "agents/continuation9_counts/S6_SERIES_PUBLISH_III_count_provenance_review.md"
COUNT_FILE = "records/S6_SERIES_PUBLISH_III_current_check_counts.json"
MATRIX_REVIEW = "agents/continuation9_computation_method/S6_SERIES_PUBLISH_III_02KU_matrix_method_review.md"
SELECTOR = "code/S6_SERIES_PUBLISH_c9_III_check_counts.py"
REPLAY = "code/S6_SERIES_PUBLISH_c9_ku_matrix_replay.py"


def main():
    names = (SOURCE, DEPOSIT, MARKDOWN, PROVENANCE, "CHECK_EVENTS.tsv", "S6_SERIES_PUBLISH_tags.tsv")
    inputs = {name: (ROOT / name).read_bytes() for name in names}
    assert all(b"\r" not in body for body in inputs.values())
    source = inputs[SOURCE].decode("utf-8")
    deposit = json.loads(inputs[DEPOSIT])
    markdown = inputs[MARKDOWN].decode("utf-8")
    provenance = list(csv.DictReader(io.StringIO(inputs[PROVENANCE].decode("utf-8")), delimiter="\t"))
    by_claim = {row["claim_id"]: row for row in provenance}
    assert len(by_claim) == len(provenance)

    data = counts.current_data(ROOT)
    selected_ids = [event["event_id"] for event in data["selected"]]
    replay_rows = [event for event in data["selected"] if event["event_id"] == REPLAY_EVENT]
    assert len(replay_rows) == 1
    assert replay_rows[0]["statement_id"] == "maps:src:D.2.2"
    assert replay_rows[0]["type"] == "computation or formal certificate"
    assert "after reading the current complete 02KU statement/proof" in replay_rows[0]["outcome"]
    assert REPLAY in source, "Wait for the P14 program-table admission."

    paragraph = counts.count_prose(data)
    start = source.index("The records associate ")
    ending = "Each outcome specifies its scope and prior proof exposure."
    stop = source.index(ending, start) + len(ending)
    old_paragraph = source[start:stop]
    assert source.count(old_paragraph) == 1
    new_paragraph = textwrap.fill(paragraph, width=76)
    assert old_paragraph != new_paragraph

    abstract_start = source.index(r"\begin{abstract}") + len(r"\begin{abstract}")
    abstract_end = source.index(r"\end{abstract}", abstract_start)
    raw_abstract = source[abstract_start:abstract_end].strip()
    abstract = " ".join(raw_abstract.split())
    assert abstract.split() == raw_abstract.split()
    abstract_words = len(abstract.split())
    assert abstract_words <= 250

    method_start = source.index("This text is AI-authored.") + len("This text is AI-authored.")
    method_end = source.index("The models worked from explicit statements", method_start)
    raw_production = source[method_start:method_end].strip()
    production = " ".join(raw_production.split()).replace("~", " ").replace("--", "–")
    assert "\\" not in production
    assert production.count("GPT-6 Astra (OpenAI), in ChatGPT Pro mode") == 1
    assert "GPT-6 Astra Pro" not in production
    assert "20–26 November 2026" in production
    assert "Paper III reading and computations continued on 26 November" in production
    assert "numerical reasoning-effort" not in production

    parts = deposit["provenance"].split("\n\n")
    assert len(parts) == 6
    assert parts[0] == "Text: AI-authored; none of it was written by a human. The submitter takes responsibility for the veracity of the text."
    assert parts[1].startswith("How it was produced. ")
    assert parts[2] == "How it was checked. " + " ".join(old_paragraph.split())
    assert parts[3].startswith("The models compared explicit statements")
    assert parts[4].startswith("Human understanding. No human has checked the mathematics.")
    assert parts[5].startswith("Records. ")
    parts[1] = "How it was produced. " + production
    parts[2] = "How it was checked. " + paragraph
    parts[3] += (
        " For the fifty inputs of the finite filling family and eight additional clutch inputs, integral cohomology and the full fundamental groups were recalculated in SageMath from marked integer cochain pairs, restriction maps and peripheral presentations."
        " The calculation recomputed Smith normal forms and exact ranks of the assembled cone matrices after exposure to the proof and backend."
        " Its geometric input is the local filling identifications cited in the paper."
    )
    new_provenance = "\n\n".join(parts)
    assert "GPT-6 Astra Pro" not in new_provenance
    assert not re.search(r"\b[0-9a-f]{40}\b", new_provenance)

    old_systems = deposit["aiSystems"]
    assert len(old_systems) == 6
    assert old_systems[0] == {"provider": "OpenAI", "model": "GPT-6 Astra Pro (ChatGPT Pro mode)", "version": None}
    assert old_systems[1] == {"provider": "OpenAI", "model": "GPT-6 Astra (ChatGPT Pro mode)", "version": None}
    assert old_systems[-1] == {"provider": "Python", "model": "SymPy and exact integer/rational arithmetic", "version": None}
    new_systems = [dict(row) for row in old_systems[1:]]
    new_systems.append({"provider": "SageMath", "model": "SageMath", "version": "10.9"})
    replay_output = (ROOT / "code/S6_SERIES_PUBLISH_c9_ku_matrix_replay.out").read_text(encoding="utf-8")
    assert replay_output.startswith("Sage 10.9 pinned backend ")
    assert "ALL 58 PASSED: actual matrix-derived cohomology" in replay_output
    assert len(new_systems) == 6

    section_start = markdown.index("## Paper III\n")
    next_section = markdown.find("\n## Paper ", section_start + 1)
    section_stop = next_section if next_section >= 0 else len(markdown)
    old_section = markdown[section_start:section_stop]
    assert markdown.count(old_section) == 1
    new_section = old_section
    old_ai = "\n".join(f"- {row['provider']}: {row['model']}; version: {row['version'] if row['version'] is not None else 'null'}" for row in old_systems)
    new_ai = "\n".join(f"- {row['provider']}: {row['model']}; version: {row['version'] if row['version'] is not None else 'null'}" for row in new_systems)
    for before, after in ((deposit["abstract"], abstract), (deposit["provenance"], new_provenance), (old_ai, new_ai)):
        assert old_section.count(before) == 1
        assert before != after
        new_section = new_section.replace(before, after, 1)

    changes = []

    def add(change_id, path, operation, reason, **content):
        changes.append(dict(change_id=change_id, path=path, operation=operation,
                            reason=reason, **content))

    count_reason = (
        "Recompute the six literal event categories and declared evidence groups from the final admitted ledger. "
        "The c8 formal-owner/historical-statement/tag and whole-withdrawal rules are unchanged. "
        "The eight root-reviewed intake associations verify full original subjects, exact event IDs, all five raw fields and unique current primary tags; each event enters once. "
        "The exposed 58-input replay contributes one computation event and no independent re-proof."
    )
    attribution_reason = (
        "The supplied Claude P7 explicitly identifies the recorded names GPT-6 Astra and GPT-6 Astra Pro as one publication setup. "
        "Both names map to the prompt section 4.1 and admitted methodology form GPT-6 Astra (OpenAI), ChatGPT Pro mode. "
        "The deposit uses that one declaration and the admitted 20–26 November span; all historical who fields remain verbatim. "
        "Claude's III reading began on 25 November and continued with computations on 26 November, as the supplied reading-log header records."
    )
    add("C9-III-METHODOLOGY-COUNTS", SOURCE, "text_replace", count_reason,
        type="D15", statement_id="methodology", old_text=old_paragraph, new_text=new_paragraph)
    add("C9-III-DEPOSIT-ABSTRACT", DEPOSIT, "json_field_replace",
        "Match the admitted P1 abstract exactly by joining its existing whitespace-separated tokens. The two fibre configurations are already defined by the source correction; no mathematical assertion changes here.",
        type="D15;D22", field="abstract", old_value=deposit["abstract"], new_value=abstract)
    add("C9-III-DEPOSIT-PROVENANCE", DEPOSIT, "json_field_replace",
        attribution_reason + " " + count_reason + " The additional Sage calculation is described at its exposed algebraic scope; the local geometric identifications remain cited inputs.",
        type="D15", field="provenance", old_value=deposit["provenance"], new_value=new_provenance)
    add("C9-III-DEPOSIT-SYSTEMS", DEPOSIT, "json_field_replace",
        attribution_reason + " Preserve the existing Python/SymPy declaration and add the actual SageMath 10.9 runtime evidenced by the completed 58-input run. Its version is observed; the four AI declarations keep version null.",
        type="D15", field="aiSystems", old_value=old_systems, new_value=new_systems)
    add("C9-III-DEPOSIT-MARKDOWN", MARKDOWN, "text_replace",
        "Apply the same source-matching abstract, production/count/method provenance and actual system/software declarations to Paper III's Markdown section only. Other paper sections remain byte-for-byte unchanged.",
        type="D15", old_text=old_section, new_text=new_section)

    common_evidence = f"{REVIEW}; {SELECTOR}; {COUNT_FILE}; ../CLAUDE_READING_LOG_PAPER_III.md (P7 and dated header); {MATRIX_REVIEW}; {REPLAY}; code/S6_SERIES_PUBLISH_c9_ku_matrix_replay.out"
    mapping = "Supplied P7 identifies the two recorded names GPT-6 Astra and GPT-6 Astra Pro as one setup; its instructed publication name is GPT-6 Astra, the prompt section 4.1 name. Raw CHECK_EVENTS who fields remain exactly as recorded."

    def claim(identifier, claim_text, records, recomputation, primary, paper_location, resolution=None):
        before = by_claim[identifier]
        assert before["paper"] == "III"
        after = dict(before)
        for old_key, prior_key in (("claim", "prior_claim"), ("against_records", "prior_records_assessment"),
                                   ("by_recomputation", "prior_recomputation_assessment"), ("against_primary_source", "prior_primary_assessment")):
            if not after[prior_key]:
                after[prior_key] = before[old_key]
        after.update(claim=claim_text, against_records=records, by_recomputation=recomputation,
                     against_primary_source=primary, locations=paper_location, current_paper_location=paper_location,
                     evidence=before["evidence"].rstrip("; ") + "; " + common_evidence,
                     current_resolution=resolution or "Current source and matching deposit declarations agree at the stated scope; the retained final-PDF gate remains open. This record adds no independent proof-check or page-reading credit.")
        assert after["resolution_status"] == before["resolution_status"]
        assert after["remaining_gate"] == before["remaining_gate"]
        assert after["required_action"] == before["required_action"]
        add("C9-PROVENANCE-" + identifier, PROVENANCE, "tsv_row_replace",
            "Update the exact existing claim and its three assessments; preserve prior assessments, status and final-PDF gates.",
            key={"claim_id": identifier}, old_row=before, new_row=after)

    loc = SOURCE + " > section 1.5 Methodology > production paragraphs"
    claim("III-C8-P05", "GPT-6 Astra (OpenAI), ChatGPT Pro mode, writing during 16–20 November and publication work during 20–26 November 2026.",
          "Prompt section 4.1 lists the writing and publication continuations; the admitted P7 source correction extends the inclusive publication span through this continuation.",
          "The deposit production paragraph is derived from the admitted source paragraphs by the explicit whitespace, nonbreaking-space and date-dash substitutions in the proposal program. " + mapping,
          "Prompt section 4.1 and supplied P7 are the documentary owners of the production chronology and name mapping.", loc)
    claim("III-C8-P06", "The Astra production declaration states ChatGPT Pro mode, following prompt section 4.1 and supplied P7.",
          mapping,
          "The source and proposed deposit have one Astra mode declaration; the superseded numerical-effort sentences are absent. Model versions remain null.",
          "Supplied P7 expressly requests the mode wording used in prompt section 4.1.", loc)
    claim("III-C8-P07", "The recorded Astra and Astra Pro publication names use the one GPT-6 Astra (OpenAI), ChatGPT Pro mode declaration specified by supplied P7.",
          mapping,
          "The deposit's two OpenAI Astra entries map to the single already admitted Astra declaration. The program requires both complete old entries before producing that replacement; it does not alter any raw event field.",
          "The alias interpretation comes from the supplied P7, read with prompt section 4.1. The current raw event author remains the actual session attribution.", loc)
    claim("III-C8-P12", "Claude Opus 5.5 at effort max checked publication material received on 23–25 November; its Paper III reading began on 25 November and continued with computations on 26 November.",
          "The five supplied intake tables retain their dated and bounded outcomes. The supplied Paper III reading log opens with the 25 November start and continuation on 26 November.",
          "The exact eight cp92–100 intake rows are preserved in the ledger and associated only by the reviewed finite event/subject/tag map. The chronology is copied from the admitted source paragraphs.",
          "Prompt section 4.1, the dated Paper III reading-log header and the eight original intake rows supply this documentary scope.", loc)
    claim("III-C8-P15", "Checks include exact arithmetic, certified rational bounds and the exposed SageMath calculation of the 50 marked filling inputs plus eight additional clutch inputs.",
          "The admitted rational Rouché computation and exact SymPy calculations retain their earlier scope. The admitted 02KU replay event records actual SageMath 10.9 integer cochain, cone, Smith and peripheral calculations for all 58 inputs.",
          "The completed replay output records all 58 matches; every integral cohomology group is independently recomputed from incoming Smith factors and outgoing ranks. The full peripheral groups have integral centrality witnesses. Prior proof/backend exposure is explicit in the computation event.",
          "The retained source provenance pins the public Threefold Explorer backend and database supplying the local marked pairs. Their geometric identifications remain cited inputs; this event supplies algebraic recomputation credit.",
          SOURCE + " > section 1.5 Methodology; maps:src:D.2.2 (02KU) and its proof")
    claim("III-C8-P16", "Computations are described mathematically where used and the program table includes the actual 02KU matrix replay program.",
          "The P14 exposition and program-table admission give the cochain/cone/Smith/peripheral calculation and its authored replay path. Historical program paths keep their existing provenance checks.",
          "The proposal program verifies that the actual replay program path occurs in the current source. No new program-table page or visibility claim is made.",
          "The program exists in code and its completed output is retained; source/data primary URLs and exact locators remain in the cited computation review.",
          SOURCE + " > maps:src:D.2.2 (02KU) and proof; Programs and records",
          "The mathematical description and program path have current source evidence. The existing open final-PDF program-table visibility gate is preserved without page-reading credit.")
    six = "/".join(str(data["counts"][kind]) for kind in counts.TYPES)
    claim("III-C8-P19", f"The current paragraph reports {len(selected_ids):,} event associations in {len(data['groups']):,} evidence groups, with counts {six} in the six recorded categories.",
          "The final admitted event ledger is selected by the unchanged c8 formal-owner/historical-statement/exact-tag and whole-withdrawal rules, with exactly eight separately verified literal intake associations.",
          f"The delivered c9 program recomputes all six counts; their sum is {len(selected_ids):,}. Each event ID occurs once. The selected IDs and complete declared evidence-group set are retained in the computed count output. The exposed 58-input replay is one computation event.",
          "The primary evidence is the unchanged raw event ledger, the eight original five-field intake rows and the current formal-owner/tag map. The source and deposit paragraph both use the same computed prose.",
          SOURCE + " > section 1.5 Methodology > current-statement count paragraph")
    claim("III-C8-D02", f"The deposit abstract retains the complete {abstract_words}-word current Paper III abstract.",
          "The admitted P1 source correction identifies the two fibre configurations explicitly; the remaining abstract assertions retain their existing AB01–AB10 supplying records.",
          f"The field has exactly the source abstract's ordered whitespace-separated tokens, {abstract_words} in total, within the 250-word limit. Only paragraph whitespace is joined.",
          "The mathematical assertions and source loci remain those individually recorded in III-C8-AB01–AB10 and the admitted P1 correction.",
          SOURCE + " > abstract")
    claim("III-C8-D14", "The six aiSystems entries give the four named AI model/mode declarations, the evidenced Python/SymPy software declaration and SageMath version 10.9.",
          mapping + " The completed replay identifies Sage 10.9; the existing III exact-arithmetic code retains the Python/SymPy declaration.",
          "The proposal requires both complete old Astra entries, preserves the four canonical AI entries and Python/SymPy entry, and adds the observed SageMath 10.9 entry. Every entry uses provider/model/version; model versions stay null.",
          "Prompt section 4.1 and supplied P7 support the single Astra declaration. The attached V form supplies the schema including software entries. The actual III code and completed Sage replay supply this paper's software scope.",
          SOURCE + " > section 1.5 Methodology; maps:src:D.2.2 (02KU)")

    # Check the proposed text in memory without altering any source owner.
    candidate = source.replace(old_paragraph, new_paragraph, 1)
    old_structure = counts.C8.parse_statements(source)
    new_structure = counts.C8.parse_statements(candidate)
    assert old_structure[1:] == new_structure[1:]
    assert [(r.statement_id, r.kind, r.tag, r.labels, r.owned_labels) for r in old_structure[0]] == [(r.statement_id, r.kind, r.tag, r.labels, r.owned_labels) for r in new_structure[0]]
    assert markdown[:section_start] == (markdown[:section_start] + new_section + markdown[section_stop:])[:section_start]
    assert all((ROOT / name).read_bytes() == body for name, body in inputs.items()), "Inputs changed during preparation; rerun after admissions settle."

    result = counts.summary(data)
    result["selected_event_ids"] = selected_ids
    result["recorded_evidence_groups"] = sorted(data["groups"])
    result["interpretation"] = "Exact statement-event associations; unchanged six types and whole-withdrawal rule; eight literal intake associations verified against their full original five fields and unique current owner/tag. No raw event is rewritten or counted twice. Administrative and page records remain outside the selected current formal statement subjects."
    OUT.mkdir(parents=True, exist_ok=True)
    TEMP_COUNT_RESULT.parent.mkdir(parents=True, exist_ok=True)
    TEMP_COUNT_RESULT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    target = TEMP_PROPOSALS
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(changes, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print("Current formal owners:", len(data["statements"]))
    print("Current statement subject identifiers:", len(data["subjects"]))
    print("Base selected event associations:", data["base_selected_event_associations"])
    print("Exact added intake associations:", len(data["exact_intake_associations"]))
    print("Selected event associations:", len(selected_ids))
    print("Recorded evidence groups:", len(data["groups"]))
    for kind in counts.TYPES:
        print(kind, data["counts"][kind], sep="\t")
    print("Replay event:", REPLAY_EVENT, replay_rows[0]["type"])
    print("Source/deposit abstract whitespace-separated words:", abstract_words)
    print("Guarded proposal items:", len(changes), "including provenance claims:", sum(c["operation"] == "tsv_row_replace" for c in changes))
    print("Proposed methodology paragraph:\n" + new_paragraph)
    print("Temporary selected-ID/evidence-group result:", TEMP_COUNT_RESULT)
    print("Canonical count target for root admission:", COUNT_FILE)
    print("Temporary guarded replacements:", target)
    print("All inputs remained byte-identical. No master, raw event, final count record, inventory, tag table or final-layout output was written.")


if __name__ == "__main__":
    main()
