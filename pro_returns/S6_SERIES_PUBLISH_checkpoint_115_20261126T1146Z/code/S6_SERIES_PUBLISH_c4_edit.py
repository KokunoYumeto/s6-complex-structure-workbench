"""Fourth-continuation text and event helpers; existing TSVs are the records."""
from S6_SERIES_PUBLISH_c3_edit import *


def apply_edit(old, new, change_id, types, statement_id, location, reason,
               review="Complete old and new context read by root.",
               old_page="checkpoint44 or subsequent working source; final concordance pending",
               new_page="final integrated build pending"):
    text = SOURCE.read_text()
    if text.count(old) != 1:
        raise ValueError(f"{change_id}: expected one old passage, found {text.count(old)}")
    preserve_identifiers(old, new)
    SOURCE.write_text(text.replace(old, new, 1), newline="\n")
    rows = [dict(change_id=f"{change_id}-{i:02}", type=kind,
        statement_id=statement_id, old_location=location, old_page=old_page,
        new_location=location, new_page=new_page, old_text=old, new_text=new,
        reason=reason, review_status=review) for i, kind in enumerate(types, 1)]
    print(change_id, "defect rows", append_rows(ROOT / "S6_SERIES_PUBLISH_defects_II.tsv", rows, "change_id"))


def add_event(statement, event_id, kind, outcome, where, group="", source=""):
    stamp = now()
    row = {
        "statement_id": statement, "date": stamp[:10],
        "who": "GPT-6 Astra (OpenAI), ChatGPT Pro mode; effort setting not separately exposed; fourth-continuation root",
        "type": kind, "outcome": outcome, "event_id": event_id,
        "phase": "publication text and proof comparison", "source_file": source,
        "source_row": "", "source_event_type": kind,
        "evidence_group": group or event_id, "publish_input_file": "",
        "publish_input_row": "", "date_utc": stamp, "where": where,
    }
    return append_rows(ROOT / "CHECK_EVENTS.tsv", [row], "event_id")
