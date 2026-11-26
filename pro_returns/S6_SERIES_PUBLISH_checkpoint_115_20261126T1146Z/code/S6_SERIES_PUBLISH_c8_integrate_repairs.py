"""Audit, then explicitly apply admitted Paper III repair packets.

Default execution is read-only apart from the caller's stdout/stderr capture.
It never prints any manuscript passage. Closed 02LG target files are not read.
The authoritative comparison path in required_progress_III selects the packet;
lexically newer files do not override that recorded admission.

After all required checks and the two support admissions, root can explicitly
run --apply, supplying --extra-packet 02LV=agents/<its admitted directory>.
That writes the manuscript, admitted defect rows, and missing historical check
events. Mechanical source application earns no mathematical check event. Every
applied proof remains pending the current-source whole reading and page review.
"""
from __future__ import annotations

import argparse
from collections import Counter
import csv
from dataclasses import dataclass
from datetime import datetime, timezone
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "S6_SERIES_PUBLISH_III.tex"
PROGRESS = ROOT / "S6_SERIES_PUBLISH_required_progress_III.tsv"
EXTRA_ADMITTED = {
    "02LT": "agents/continuation8_iii_lt",
}
NO_GUARDED_CHANGE = {"02J4", "02J6", "02K5", "02QC", "02QE", "02Q8"}
ALLOWED_EVENT_TYPES = {
    "targeted proof check", "independent re-proof",
    "computation or formal certificate", "used and rechecked in this run",
    "carried as background without fault found",
    "refuted, with the refined statement's id",
}
# Root may supply exact classifications for a packet whose original guards
# contain no defect kinds. An empty mapping makes those rows review-pending;
# source application refuses to invent a classification.
ROOT_REVIEWED_APPLICATION_TYPES = {
    # Root wholly read all three guards and their complete comparison in c8.
    # The first adds the missing regular-ring reason for the singular location;
    # the other two replace rhetorical source-category clauses with the already
    # proved existence and singular-locus statements. No D26 or new error credit.
    "02K6:S6_SERIES_PUBLISH_III_02K6_guards.json:1": "D22",
    "02K6:S6_SERIES_PUBLISH_III_02K6_guards.json:2": "D02",
    "02K6:S6_SERIES_PUBLISH_III_02K6_guards.json:3": "D02",
}
DEFECT_FIELDS = ["change_id", "type", "statement_id", "old_location", "old_page",
                 "new_location", "new_page", "old_text", "new_text", "reason",
                 "review_status"]
LABEL = re.compile(r"\\label\{([^}]+)\}")
TAG = re.compile(r"\\hypertarget\{(tag-[^}]+)\}")
BIB = re.compile(r"\\bibitem(?:\[[^\n]*?\])?\{([^}]+)\}")
CITE = re.compile(r"\\cite(?:t|p|alp|author|year|yearpar)?\*?(?:\[[^\]]*\]){0,2}\{([^}]+)\}")


def read(path: Path) -> str:
    with path.open(encoding="utf-8", newline="") as handle:
        return handle.read()


def table(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


@dataclass
class Edit:
    tag: str
    statement_id: str
    packet: Path
    row: int
    old: str
    new: str
    reason: str = ""
    defect_type: str = ""
    disposition: str = "selected"

    @property
    def key(self) -> str:
        return f"{self.tag}:{self.packet.name}:{self.row}"


def packet_edits(tag: str, directory: Path, statement_id: str, source: str) -> list[Edit]:
    # No globs or reads into LG until its live required row says done.
    prefix = f"S6_SERIES_PUBLISH_III_{tag}"
    replacements = sorted(directory.glob(prefix + "*replacements.tsv"))
    result = []
    if replacements:
        for path in replacements:
            for n, row in enumerate(table(path), 1):
                result.append(Edit(tag, row.get("statement_id", statement_id), path, n,
                                   row["old_text"], row["new_text"], row.get("reason", "")))
        return result
    guards = [path for path in sorted(directory.glob(prefix + "*.json"))
              if path.name.endswith(("_guards.json", "_guard.json", "_orientation_repair.json"))]
    if guards:
        for path in guards:
            data = json.loads(read(path))
            for n, row in enumerate(data if isinstance(data, list) else [data], 1):
                result.append(Edit(tag, statement_id, path, n, row["old"], row["new"],
                                   row.get("reason", ""), row.get("type", "")))
        return result
    for old_path in sorted(directory.glob(prefix + "*_old.tex")):
        new_path = old_path.with_name(old_path.name.replace("_old.tex", "_new.tex"))
        if not new_path.exists():
            continue
        old = read(old_path).rstrip("\n")
        new = read(new_path).rstrip("\n")
        if tag == "02K2" and old_path.name.endswith("_statement_old.tex"):
            # The supplied pair omits precisely this one existing metadata line.
            # Root explicitly approved including the actual line in the old guard.
            token = "\\StatementRecord{maps:src:C.1.1}"
            start = source.index(token)
            stop = source.index("\n", start)
            metadata = source[start:stop]
            assert source.count(metadata) == 1
            first, rest = old.split("\n", 1)
            assert rest.startswith("\n")
            old = first + "\n" + metadata + rest
            # The new statement retains its permanent label and target and prints
            # the small tag where the removed process header formerly stood.
            first_new, rest_new = new.split("\n", 1)
            new = first_new + "\n{\\normalfont\\scriptsize tag 02K2}\\par" + rest_new
        result.append(Edit(tag, statement_id, old_path, 1, old, new,
                           "Apply the admitted complete old/new pair; " + relative(new_path)))
    return result


def bibliography_entries(text: str) -> dict[str, str]:
    matches = list(BIB.finditer(text))
    return {match[1]: text[match.start():matches[n + 1].start() if n + 1 < len(matches) else len(text)].strip()
            for n, match in enumerate(matches)}


def collect(source: str, extras: dict[str, str]):
    progress = table(PROGRESS)
    packets = {}
    edits = []
    unguarded = []
    for row in progress:
        if row["status"] != "done":
            print("CLOSED_TARGET_SKIPPED", row["tag"], row["status"])
            continue
        tag = row["tag"]
        comparison = ROOT / row["proof_comparison_evidence"]
        if not comparison.is_file():
            raise ValueError(f"Missing authoritative comparison for {tag}: {comparison}")
        directory = comparison.parent
        packets[tag] = (directory, row["label"], row["proof_comparison_evidence"])
        selected = packet_edits(tag, directory, row["label"], source)
        if not selected:
            unguarded.append(tag)
        edits.extend(selected)
    for tag, location in extras.items():
        directory = (ROOT / location).resolve()
        if not directory.is_relative_to(ROOT):
            raise ValueError("External packet directory")
        paths = sorted(directory.glob(f"S6_SERIES_PUBLISH_III_{tag}*replacements.tsv"))
        if not paths:
            raise ValueError(f"No explicit replacements for extra admitted tag {tag}")
        first = table(paths[0])[0]
        statement_id = first["statement_id"]
        admission = sorted(directory.glob(f"*{tag}*admission*review*.md"))
        if not admission:
            raise ValueError(f"Extra tag {tag} requires its root admission note")
        packets[tag] = (directory, statement_id, relative(admission[0]))
        edits.extend(packet_edits(tag, directory, statement_id, source))
    unexpected = set(unguarded) - NO_GUARDED_CHANGE
    if unexpected:
        raise ValueError("Completed packets without a known application route: " + ", ".join(sorted(unexpected)))
    return progress, packets, edits, unguarded


def scoped_occurrences(text: str, old: str, tag: str) -> list[int]:
    positions = [m.start() for m in re.finditer(re.escape(old), text)]
    if tag == "02KB" and old == r"\cite[Theorem~7.17]{AC26}":
        anchor = text.index(r"\hypertarget{tag-02KB}")
        # Both occurrences belong to the admitted 02KB proof. The next numbered
        # statement begins with this following permanent statement tag.
        end = text.index(r"\hypertarget{tag-02KC}", anchor)
        if len(positions) != 2 or not all(anchor < pos < end for pos in positions):
            raise ValueError("02KB citation's two authorized occurrences changed scope")
    return positions


def simulate(source: str, packets, edits: list[Edit]):
    text = source
    applications = []
    # The full admitted 02KM repair replaces the entire Fukae entry and supplies
    # the author correction proposed separately by 02OG. Keep other 02OG edits.
    km = [e for e in edits if e.tag == "02KM" and r"\bibitem[Fukae(2002)]{manFukae02}" in e.old]
    og = [e for e in edits if e.tag == "02OG" and e.statement_id == "bib:manFukae02"]
    if km and og:
        assert len(km) == len(og) == 1
        assert og[0].old in km[0].old
        assert "Mitsuaki Fukae." in km[0].new and "Kazuki Fukae." not in km[0].new
        assert og[0].old.replace("Kazuki Fukae.", "Mitsuaki Fukae.") == og[0].new
        og[0].disposition = "subsumed by 02KM full Fukae entry"
    for edit in edits:
        if edit.disposition != "selected":
            print("SUBSUMED", edit.key, edit.disposition)
            continue
        positions = scoped_occurrences(text, edit.old, edit.tag)
        expected = 2 if edit.tag == "02KB" and edit.old == r"\cite[Theorem~7.17]{AC26}" else 1
        if len(positions) != expected:
            raise ValueError(f"{edit.key}: expected {expected} exact occurrences, found {len(positions)}")
        missing_labels = Counter(LABEL.findall(edit.old)) - Counter(LABEL.findall(edit.new))
        missing_tags = Counter(TAG.findall(edit.old)) - Counter(TAG.findall(edit.new))
        if missing_labels or missing_tags:
            raise ValueError(f"{edit.key}: permanent identifiers removed: {missing_labels}, {missing_tags}")
        old_lines = [text.count("\n", 0, pos) + 1 for pos in positions]
        text = text.replace(edit.old, edit.new, expected)
        applications.append((edit, old_lines))
    # Both bibliographic keys identify the same 1963 article: the source entry
    # and the admitted references record have identical authors, journal,
    # volume, pages and DOI 10.2307/1970128. Keep the existing manuscript entry
    # and map only citation key tokens, retaining each optional page locator.
    if "KervaireMilnor1963" in text:
        existing_km = bibliography_entries(text[text.index(r"\begin{thebibliography}"):])["manKM63"]
        assert "10.2307/1970128" in existing_km
        references = read(ROOT / "S6_SERIES_PUBLISH_references.bib")
        km_start = references.index("@article{KervaireMilnor1963,")
        km_end = references.find("\n@", km_start + 1)
        km_record = references[km_start:km_end if km_end >= 0 else len(references)]
        assert "10.2307/1970128" in km_record
        matches = [m for m in CITE.finditer(text) if "KervaireMilnor1963" in m[1].split(",")]
        for n, match in enumerate(reversed(matches), 1):
            old = match[0]
            new = old[:match.start(1) - match.start()] + ",".join(
                "manKM63" if k.strip() == "KervaireMilnor1963" else k
                for k in match[1].split(",")) + old[match.end(1) - match.start():]
            owner = next((e.tag for e, _ in applications if old in e.new), "02S8")
            edit = Edit(owner, "bib:manKM63", ROOT / "S6_SERIES_PUBLISH_references.bib", n,
                        old, new, "Map the two exact aliases of the same DOI 10.2307/1970128 to the existing manuscript key; retain the cited page locator.", "D18")
            line = text.count("\n", 0, match.start()) + 1
            text = text[:match.start()] + new + text[match.end():]
            applications.append((edit, [line]))
        print("EXACT_BIBLIOGRAPHIC_ALIAS", "KervaireMilnor1963 -> manKM63", len(matches))
    # Add only cited, missing entries from the admitted packet's explicit bib
    # proposals. Existing entries change solely through the guards above.
    cited = {key.strip() for match in CITE.finditer(text) for key in match[1].split(",")}
    present = set(BIB.findall(text))
    missing = cited - present
    candidates = {}
    for tag, (directory, statement_id, evidence) in packets.items():
        for path in sorted(directory.glob(f"*{tag}*.tex")):
            if not any(word in path.name.lower() for word in ("bib_proposal", "bibliography", "_bibitem")):
                continue
            for key, entry in bibliography_entries(read(path)).items():
                if key in missing:
                    candidates.setdefault(key, []).append((tag, path, entry, evidence))
    staged = ROOT / "agents/continuation8_iii_integration/S6_SERIES_PUBLISH_III_bibliography_additions.tex"
    for key, entry in bibliography_entries(read(staged)).items():
        if key in missing:
            owner = next(e.tag for e in edits if key in e.new)
            candidates.setdefault(key, []).append((owner, staged, entry,
                "Existing attached bibliography and admitted staged bibliography metadata; exact origins are recorded in the integration note."))
    for key in sorted(candidates):
        values = candidates[key]
        unique = {value[2] for value in values}
        if len(unique) != 1:
            raise ValueError(f"Competing explicit bibliography proposals for {key}")
        tag, path, entry, evidence = values[0]
        old = r"\end{thebibliography}"
        assert text.count(old) == 1
        edit = Edit(tag, "bib:" + key, path, 1, old, entry + "\n\n" + old,
                    "Add the cited exact bibliography proposal from the admitted packet; " + evidence, "D18")
        pos = text.index(old)
        line = text.count("\n", 0, pos) + 1
        text = text.replace(old, edit.new, 1)
        applications.append((edit, [line]))
        print("BIBLIOGRAPHY_ADDITION", key, relative(path))
    old_labels = Counter(LABEL.findall(source))
    new_labels = Counter(LABEL.findall(text))
    old_tags = Counter(TAG.findall(source))
    new_tags = Counter(TAG.findall(text))
    assert not (old_labels - new_labels), "Global label loss"
    assert not (old_tags - new_tags), "Global tag-anchor loss"
    new_duplicate_labels = {key: n for key, n in new_labels.items() if n > 1 and n > old_labels[key]}
    new_duplicate_tags = {key: n for key, n in new_tags.items() if n > 1 and n > old_tags[key]}
    if new_duplicate_labels or new_duplicate_tags:
        raise ValueError(f"New duplicate permanent identifiers: {new_duplicate_labels}, {new_duplicate_tags}")
    final_missing = cited - set(BIB.findall(text))
    print("CITATION_KEYS_WITHOUT_BIBITEM", ",".join(sorted(final_missing)) or "none")
    new_missing = final_missing - ({k.strip() for m in CITE.finditer(source) for k in m[1].split(",")} - set(BIB.findall(source)))
    if new_missing:
        raise ValueError("Repairs introduce bibliography keys with no admitted entry: " + ",".join(sorted(new_missing)))
    print("PERMANENT_LABELS_PRESERVED", len(old_labels))
    print("PERMANENT_TAG_ANCHORS_PRESERVED", len(old_tags))
    print("NEW_LABELS", ",".join(sorted(set(new_labels) - set(old_labels))) or "none")
    return text, applications


def defect_packet_rows(tag: str, directory: Path):
    prefix = f"S6_SERIES_PUBLISH_III_{tag}"
    preferred = [directory / (prefix + suffix) for suffix in
                 ("_defects.tsv", "_defect_drafts.tsv", "_defect_proposals.tsv", "_defect_proposal.tsv")]
    for path in preferred:
        if path.is_file():
            return path, table(path)
    path = directory / (prefix + "_defects.csv")
    if path.exists():
        with path.open(encoding="utf-8", newline="") as handle:
            return path, list(csv.DictReader(handle))
    return None, []


def write_table(path: Path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fields, delimiter="\t", lineterminator="\n", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def prepare_records(packets, applications, timestamp: str):
    defects_path = ROOT / "S6_SERIES_PUBLISH_defects_III.tsv"
    defects = table(defects_path)
    existing = {row["change_id"] for row in defects}
    for tag, (directory, statement_id, evidence) in packets.items():
        source_path, rows = defect_packet_rows(tag, directory)
        for n, row in enumerate(rows, 1):
            change_id = row.get("change_id") or row.get("proposal_id") or f"III-C8-{tag}-ADMITTED-FINDING-{n}"
            if change_id in existing:
                continue
            out = {field: row.get(field, "") for field in DEFECT_FIELDS}
            out["change_id"] = change_id
            out["statement_id"] = row.get("statement_id") or statement_id
            out["type"] = row.get("type") or row.get("criterion_ids", "")
            out["old_text"] = row.get("old_text") or row.get("old_span", "")
            out["new_text"] = row.get("new_text") or row.get("new_span", "")
            out["old_page"] = row.get("old_page") or "pending page concordance"
            out["new_page"] = "pending final build"
            out["review_status"] = (f"Admitted finding; packet edits applied {timestamp}. "
                                    f"Admission: {evidence}. Current-source whole reading, unit review, "
                                    "page concordance and rendered-page review pending.")
            out["reason"] = row.get("reason", "") + f" [Finding source: {relative(source_path)}, row {n}.]"
            defects.append(out)
            existing.add(change_id)
    # Exact edit rows supplement the fine-grained findings. They make every
    # literal source mutation reviewable without treating application as proof.
    unclassified = []
    for n, (edit, lines) in enumerate(applications, 1):
        kinds = ROOT_REVIEWED_APPLICATION_TYPES.get(edit.key) or edit.defect_type or ";".join(sorted(set(re.findall(r"\bD\d{2}\b", edit.reason))))
        if not kinds:
            directory = packets[edit.tag][0]
            _, findings = defect_packet_rows(edit.tag, directory)
            # These are the packet's documented types, not new findings inferred
            # from successful source application. Legacy packets use criterion_ids.
            documented = " ".join(r.get("type") or r.get("criterion_ids", "") for r in findings)
            kinds = ";".join(sorted(set(re.findall(r"\bD\d{2}\b", documented))))
        if not kinds:
            unclassified.append(edit.key)
        for occurrence, line in enumerate(lines, 1):
            change_id = f"III-C8-APPLY-{n:03d}-{edit.tag}-{occurrence}"
            if change_id in existing:
                raise ValueError("Application log ID already exists; refusing duplicate application")
            defects.append({"change_id": change_id, "type": kinds, "statement_id": edit.statement_id,
                            "old_location": f"{edit.tag}; exact guard {relative(edit.packet)} row {edit.row}; occurrence {occurrence}; application-source line {line}",
                            "old_page": "pending page concordance", "new_location": edit.statement_id,
                            "new_page": "pending final build", "old_text": edit.old, "new_text": edit.new,
                            "reason": edit.reason or "Apply the exact admitted replacement packet; fine-grained defect findings retain its justification.",
                            "review_status": f"Applied {timestamp}; whole rewritten-proof reading and final unit/page review pending. No mathematical check credit for text application."})
            existing.add(change_id)
    events_path = ROOT / "CHECK_EVENTS.tsv"
    with events_path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        event_fields = reader.fieldnames
        events = list(reader)
    event_ids = {row["event_id"] for row in events}
    added_events = 0
    for tag, (directory, statement_id, evidence) in packets.items():
        path = directory / f"S6_SERIES_PUBLISH_III_{tag}_CHECK_EVENTS.tsv"
        if not path.exists():
            continue
        for row in table(path):
            if not row.get("event_id"):
                raise ValueError(f"Admitted event without an ID: {path}")
            if row["event_id"] in event_ids:
                # Keep the current global row verbatim. In particular root's
                # authorized LF/LI/LN type corrections are not overwritten by
                # their older packet-local event versions.
                continue
            if row.get("type") not in ALLOWED_EVENT_TYPES:
                raise ValueError(f"Missing event has a type outside prompt section 4.3: {row['event_id']}: {row.get('type')}")
            if not row.get("who") or not (row.get("date") or row.get("date_utc")):
                raise ValueError(f"Missing event lacks original attribution or chronology: {row['event_id']}")
            unrepresented = {key for key, value in row.items() if value and key not in event_fields}
            if unrepresented:
                raise ValueError(f"Import would discard event fields: {row['event_id']}: {sorted(unrepresented)}")
            events.append({field: row.get(field, "") for field in event_fields})
            event_ids.add(row["event_id"])
            added_events += 1
    return defects, event_fields, events, added_events, unclassified


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Explicit root authorization to mutate canonical III and its records")
    parser.add_argument("--extra-packet", action="append", default=[], metavar="TAG=RELATIVE_DIRECTORY")
    args = parser.parse_args()
    extras = dict(EXTRA_ADMITTED)
    for item in args.extra_packet:
        tag, directory = item.split("=", 1)
        if tag not in {"02LT", "02LV"}:
            raise ValueError("Only the two declared support packets use --extra-packet")
        extras[tag] = directory
    source = read(SOURCE)
    progress, packets, edits, unguarded = collect(source, extras)
    print("SELECTED_LITERAL_ROWS", len(edits))
    print("TAGS_WITH_LITERAL_ROWS", len({e.tag for e in edits}))
    print("NO_GUARDED_CHANGE_TAGS", ",".join(unguarded))
    result, applications = simulate(source, packets, edits)
    per_tag = Counter(edit.tag for edit, _ in applications)
    for tag, count in per_tag.items():
        print("APPLICATIONS", tag, count, packets[tag][2])
    print("APPLICATION_ROWS", len(applications))
    print("LITERAL_OCCURRENCES", sum(len(lines) for _, lines in applications))
    print("PAPER_III_REQUIRED_DONE", sum(r["status"] == "done" for r in progress), len(progress))
    timestamp = datetime.now(timezone.utc).isoformat()
    defects, event_fields, events, added_events, unclassified = prepare_records(packets, applications, timestamp)
    print("PLANNED_DEFECT_ROWS", len(defects))
    print("MISSING_ADMITTED_HISTORICAL_EVENTS", added_events)
    print("NEW_CHECK_CREDIT_FOR_APPLICATION", 0)
    print("APPLICATION_TYPES_PENDING_ROOT_REVIEW", ",".join(unclassified) or "none")
    if not args.apply:
        print("READ_ONLY_AUDIT_COMPLETE; canonical source and all central records unchanged")
        return
    if any(row["status"] != "done" for row in progress) or not {"02LT", "02LV"} <= set(extras):
        raise ValueError("Application gate remains open: all 128 required checks plus LT/LV admissions are required")
    if unclassified:
        raise ValueError("Source application awaits exact defect classification: " + ",".join(unclassified))
    # All transformations and global identifier/citation checks completed above.
    # Every record has also been prepared and validated before any central write.
    write_table(ROOT / "S6_SERIES_PUBLISH_defects_III.tsv", DEFECT_FIELDS, defects)
    if added_events:
        write_table(ROOT / "CHECK_EVENTS.tsv", event_fields, events)
    SOURCE.write_text(result, encoding="utf-8", newline="\n")
    print("APPLIED_CANONICAL_III", timestamp)


if __name__ == "__main__":
    main()
