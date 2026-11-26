"""Admit a fully compared bounded text package into the central manuscript.

The input substitutions are exact old/new passages. Defect and actual-reading
rows are appended to their existing tables; unit statuses retain global gates.
No derived record, manifest, seal or edit-level snapshot is produced.
"""
from S6_SERIES_PUBLISH_c4_edit import *
import sys
import json
import hashlib


def protected_statement(text, label):
    position = text.index(r"\label{" + label + "}")
    matches = list(re.finditer(r"\\begin\{([^}]+)\}", text[:position]))
    opening = matches[-1]
    ending = r"\end{" + opening[1] + "}"
    end = text.index(ending, position) + len(ending)
    return text[opening.start():end]


def main():
    prefix = Path(sys.argv[1])
    if not prefix.is_absolute():
        prefix = ROOT / prefix
    replacement_file = Path(str(prefix) + "_replacements.tsv")
    if replacement_file.exists():
        _, replacements = read_tsv(replacement_file)
    else:
        guards = json.loads(Path(str(prefix) + "_guards.json").read_text())
        selected = set(sys.argv[2].split(",")) if len(sys.argv) > 2 else {r["key"] for r in guards}
        replacements = [dict(statement_id=r["key"], old_text=r["old"], new_text=r["new"])
                        for r in guards if r["key"] in selected]
        if len(replacements) != len(selected):
            raise ValueError("Not every requested replacement key was found")
    _, defects = read_tsv(str(prefix) + "_defects.tsv")
    _, events = read_tsv(str(prefix) + "_CHECK_EVENTS.tsv")
    _, incoming = read_tsv(str(prefix) + "_unit_status.tsv")
    if defects and "change_id" not in defects[0]:
        units_in_package = set()
        labels_in_package = set()
        for row in replacements:
            labels_in_package.update(identifiers(row["new_text"])[0])
            heading = re.search(r"\\subsection\{[^\n]+?\}\\label\{([^}]+)\}", row["new_text"])
            if heading:
                units_in_package.add(heading[1])
        converted = []
        for row in defects:
            if row["unit_id"] not in units_in_package:
                continue
            digest = hashlib.sha256("\0".join(row[k] for k in
                ("unit_id", "defect_type", "old_text", "new_text")).encode()).hexdigest()[:16]
            converted.append(dict(change_id="II-C4-REDUCTION-" + digest,
                type=row["defect_type"], statement_id=row["unit_id"],
                old_location=row["unit_id"], old_page="checkpoint44 source; old PDF page concordance pending",
                new_location=row["unit_id"], new_page="final integrated build pending",
                old_text=row["old_text"], new_text=row["new_text"], reason=row["reason"],
                review_status="Complete old/new proof comparison by the reductions reader; root read the complete receiving proofs and exact application maps. Admitted with all inherited identifiers preserved."))
        defects = converted
        events = [r for r in events if r["statement_id"] in labels_in_package]
        # Some inherited ledger units use their first statement label. Keep
        # that stable identity when the selected subsection contains it.
        incoming = [r for r in incoming if r["unit_id"] in units_in_package
                    or r["unit_id"] in labels_in_package
                    or (r["unit_id"] == "sec:II:11" and
                        "cdp:st:C.2.UN.82" in labels_in_package)]
        for row in events:
            row.setdefault("evidence_group", row["event_id"])
            row.setdefault("source_event_type", row["type"])
            row.setdefault("source_file", str(prefix.relative_to(ROOT)) + "_comparison.md")
    before = SOURCE.read_text()
    after = before
    for row in replacements:
        old, new = row["old_text"], row["new_text"]
        count = after.count(old)
        if count != 1:
            raise ValueError((row.get("statement_id"), "old passage matches", count))
        after = after.replace(old, new, 1)
    old_ids, new_ids = identifiers(before), identifiers(after)
    for old, new in zip(old_ids, new_ids):
        if any(new[k] != v for k, v in old.items()):
            raise ValueError(("Changed identifier multiplicity", old - new, new - old))
        if any(new[k] != 1 for k in new.keys() - old.keys()):
            raise ValueError("A new identifier is duplicated")
    for label in ("push:src:E.5.2", "push:src:E.5.3"):
        if protected_statement(before, label) != protected_statement(after, label):
            raise ValueError(("Protected statement changed", label))
    for row in defects:
        row["review_status"] = row.get("review_status", "").replace(
            "prepared for root admission", "admitted after exact current-source guard and identifier checks"
        )
    fields, units = read_tsv(ROOT / "S6_SERIES_PUBLISH_unit_progress.tsv")
    key = lambda r: (r["paper"], r["unit_id"], r["defect_type"] or r["row_kind"])
    by_key = {key(r): r for r in units}
    if len(by_key) != len(units):
        raise ValueError("Duplicate pre-existing unit key")
    closures = []
    new_keys = []
    for row in incoming:
        if row["paper"] != "II":
            raise ValueError("Only Paper II is being admitted")
        if (row["defect_type"] == "D14" or row["row_kind"] == "structure") and row["status"] == "done":
            raise ValueError("Whole-paper placement must be closed by the global review")
        if row["defect_type"] in ("D10", "D16") and row["status"] != "done":
            raise ValueError("Inherited header/title gate requires a concrete recorded new defect to reopen")
        k = key(row)
        if k in by_key:
            previous = by_key[k]
            if previous["status"] == "done" and row["status"] != "done":
                raise ValueError(("Would reopen completed row without a found instance", k))
            if previous["status"] != "done" and row["status"] == "done":
                closures.append(k)
            previous.update({field: row.get(field, "") for field in fields})
        else:
            new_keys.append(k)
            units.append({field: row.get(field, "") for field in fields})
            by_key[k] = units[-1]
    # All dependent validation is complete before the shared files are changed.
    SOURCE.write_text(after, newline="\n")
    print("Exact substitutions:", len(replacements))
    print("Defect rows:", append_rows(ROOT / "S6_SERIES_PUBLISH_defects_II.tsv", defects, "change_id"))
    print("Actual-reading events:", append_rows(ROOT / "CHECK_EVENTS.tsv", events, "event_id"))
    write_tsv(ROOT / "S6_SERIES_PUBLISH_unit_progress.tsv", fields, units)
    print("Existing open rows closed:", len(closures))
    print("New unit rows:", len(new_keys), "(no movement credit)")
    print("Old labels/tags and protected E.5.2/E.5.3 statements preserved exactly.")


if __name__ == "__main__":
    main()
