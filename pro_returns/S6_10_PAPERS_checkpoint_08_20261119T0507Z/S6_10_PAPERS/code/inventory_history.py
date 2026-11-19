#!/usr/bin/env python3
"""Extract historical checker identities while retaining their exact records.

The extraction creates no current check event and does not certify the accuracy
of a historical check. Discussion records are emitted separately.
"""
from __future__ import annotations
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "sources"
JSON = json.JSONDecoder()


def embedded_json(text):
    pos = 0
    while pos < len(text):
        m = re.search(r"[\[{]", text[pos:])
        if not m:
            break
        start = pos + m.start()
        try:
            obj, n = JSON.raw_decode(text[start:])
        except json.JSONDecodeError:
            pos = start + 1
            continue
        yield obj
        pos = start + n


def objects(value):
    if isinstance(value, dict):
        yield value
        for x in value.values():
            if isinstance(x, (list, dict)):
                yield from objects(x)
    elif isinstance(value, list):
        for x in value:
            yield from objects(x)


def named_record(obj, origin):
    name = obj.get("checker") or obj.get("reviewer") or obj.get("reader") or obj.get("model")
    if not name or not isinstance(name, str):
        return None
    effort = obj.get("effort", "")
    effort_note = ""
    date = obj.get("date", "")
    if str(effort).lower() in ("not recorded", "unknown", "none"):
        effort = ""
    elif str(effort).startswith("Not separately stated"):
        effort_note, effort = str(effort), ""
    if str(date).lower() in ("not recorded", "unknown", "none"):
        date = ""
    scope = str(obj.get("scope", ""))
    kind = "source reading" if "scoped first assessment" in scope else "historical check record"
    return {"who": name, "effort": str(effort), "effort_note": effort_note,
            "date": str(date), "origin": origin, "record_kind": kind, "record": obj}


def pretty(r):
    prefix = "Source reading by " if r.get("record_kind") == "source reading" else ""
    return prefix + r["who"] + (", effort " + r["effort"] if r["effort"] else "") + (", " + r["date"] if r["date"] else "")


def main():
    rows = list(csv.DictReader((SOURCES / "s6_09/S6_09_PAPERS_inventory.csv").open()))
    ledgers = {(r["source_run"], r["source_id"]): r for r in csv.DictReader((SOURCES / "checks/S6_CHECK_LEDGER.tsv").open(), delimiter="\t")}
    source_history, label_history = {}, {}
    for r in rows:
        named, discussions, unparsed = [], [], []
        for field in ("recorded_checks", "your_check"):
            for obj in embedded_json(r[field]):
                for value in objects(obj):
                    rec = named_record(value, "S6_09 inventory: " + field)
                    if rec:
                        named.append(rec)
            for m in re.finditer(r"(GPT-[0-9.]+ (?:Astra|Sol)(?: \([^)]*\))?), effort (Pro|ultra|high|max), (?:writing run; )?([0-9]{1,2} November 2026|2026-[0-9]{2}-[0-9]{2})", r[field]):
                named.append({"who": m.group(1), "effort": m.group(2), "date": m.group(3), "origin": "S6_09 inventory: " + field, "record": r[field]})
        l = ledgers.get((r["source_run"], r["source_id"]), {})
        for text in l.get("checks", "").split(" || "):
            m = re.search(r"^(checked|discussed) in (.*?) \((Claude .*?) at effort (high|max)(?:, ([^)]+))?\)$", text)
            if m:
                record = {"who": m.group(3), "effort": m.group(4), "date": m.group(5) or "", "origin": m.group(2), "record": text}
                (discussions if m.group(1) == "discussed" else named).append(record)
            elif "re-derivation in S6_06_BLIND" in text:
                cp = re.search(r"checkpoint_(\d+)_(\d{8})T", text)
                date = (cp.group(2)[:4] + "-" + cp.group(2)[4:6] + "-" + cp.group(2)[6:]) if cp else ""
                named.append({"who": "GPT-6 Astra (OpenAI, ChatGPT Pro mode), S6_06_BLIND", "effort": "Pro", "date": date, "origin": "earlier-check ledger; effort supplied by controlling prompt", "record": text.replace("blind re-derivation", "re-derivation")})
            elif text:
                unparsed.append(text)
        # The inventory's comparison prose may name a checker beyond its JSON.
        for m in re.finditer(r"(Claude (?:Fable|Opus) [0-9.]+(?: \(Anthropic\))?), effort (high|max), ([0-9]{1,2} November 2026|2026-[0-9]{2}-[0-9]{2})", r["recorded_checks"]):
            named.append({"who": m.group(1), "effort": m.group(2), "date": m.group(3), "origin": "S6_09 recorded-check comparison prose", "record": m.group(0)})
        if not named and r["your_check"].strip():
            # This exact column is the S6_09 writing record. Its manuscript
            # declaration identifies the writing run, model, effort and date.
            # Keep that attribution source explicit instead of guessing a
            # checker from the event's wording.
            named.append({"who": "GPT-6 Astra (OpenAI, ChatGPT Pro mode), S6_09_PAPERS", "effort": "Pro", "date": "2026-11-17", "origin": "S6_09 writing-check column, attributed by manuscript POST-RECORD produced_by declaration", "record": r["your_check"]})
        # A generic internal-audit badge has no named checker. Retain its
        # exact record, but do not print an invented name in a check list.
        unattributed = [v for v in named if v["who"].lower().startswith(("unidentified", "unknown", "anonymous"))]
        named = [v for v in named if v not in unattributed]
        compact = []
        seen = set()
        for rec in named:
            identity = (rec["who"].replace(" (Anthropic)", ""), rec["effort"], rec["date"])
            if identity not in seen:
                seen.add(identity)
                compact.append(pretty(rec))
        record = {
            "source_run": r["source_run"], "source_id": r["source_id"], "label": r["printed_label"],
            "named_historical_checks": named, "historical_discussions": discussions,
            "historical_unattributed_reports": unattributed,
            "unparsed_ledger_records": unparsed,
            "compact_named_checks": "; ".join(compact),
            "raw_recorded_checks": r["recorded_checks"], "raw_s6_09_writing_check": r["your_check"],
            "current_check": "none created by this extraction",
        }
        source_history[r["source_run"] + ":" + r["source_id"]] = record
        label_history.setdefault(r["printed_label"], []).append(record)
    for r in csv.DictReader((OUT / "S6_10_PAPERS_inventory.csv").open()):
        key = r["source_run"] + ":" + r["source_id"]
        if key in source_history:
            continue
        if r["source_run"] == "S6_06_BLIND":
            who = "GPT-6 Astra (OpenAI, ChatGPT Pro mode), S6_06_BLIND"
            date = "16-18 November 2026 (checkpoint 25)"
            origin = "Checkpoint 25 source record, snapshot 2026-11-18T00:50:45Z; production range, not a newly asserted individual proof-check date"
        elif r["source_run"] == "S6_09_SUPPLEMENT":
            who = "GPT-6 Astra (OpenAI, ChatGPT Pro mode), S6_09_PAPERS"
            date = "16-17 November 2026"
            origin = "S6_09 manuscript writing declaration; supporting block absent from source row inventory"
        else:
            continue
        historical = r['check_record']
        try:
            parsed = json.loads(historical)
            if isinstance(parsed, dict):
                parsed.pop('current_writing_events', None)
                parsed.pop('current_writing_event_rule', None)
                historical = parsed.get('historical_source_record', parsed)
        except ValueError:
            pass
        named = {"who": who, "effort": "Pro", "date": date, "origin": origin, "record": historical}
        record = {"source_run":r["source_run"], "source_id":r["source_id"], "label":r["label"],
            "named_historical_checks":[named], "historical_discussions":[], "unparsed_ledger_records":[],
            "compact_named_checks":pretty(named), "raw_recorded_checks":historical,
            "raw_s6_09_writing_check":"", "current_check":"none created by this extraction"}
        source_history[key] = record
        label_history.setdefault(r["label"], []).append(record)
    (OUT / "analysis/inventory_history_by_source.json").write_text(json.dumps(source_history, indent=2, ensure_ascii=False))
    (OUT / "analysis/inventory_history_by_label.json").write_text(json.dumps(label_history, indent=2, ensure_ascii=False))
    print(json.dumps({"source_rows": len(source_history), "labels": len(label_history), "named_check_records": sum(len(v["named_historical_checks"]) for v in source_history.values()), "discussions": sum(len(v["historical_discussions"]) for v in source_history.values()), "rows_without_parsed_named_check": sum(not v["named_historical_checks"] for v in source_history.values())}, indent=2))


if __name__ == "__main__":
    main()
