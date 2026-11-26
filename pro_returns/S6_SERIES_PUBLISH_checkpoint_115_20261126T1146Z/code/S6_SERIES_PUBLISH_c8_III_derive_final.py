#!/usr/bin/env python3
"""Prepare the final Paper III inventory, tags, check entries and derived rows.

The default mode is inspect. Both modes require the final source, PDF, aux and
the separately reviewed extractor JSON. Run neither mode before root's full
code review and final-input authorization. Only explicit write mode replaces
the eight named derived products. No manuscript, event, progress, required
disposition, program-record, provenance, deposit or other-paper file is written.

Non-III records in shared CSV/TSV products retain their exact original bytes,
including quoting, multiline fields and relative order. Existing III inventory
and tag rows are retained; current formal owners and literal new tags are added.
The approved c9 wrapper retains the c8 selection rules and adds only the
eight literal intake associations verified against their original rows.
This is records derivation, not a mathematical or page-reading check.

Future authorized use:
  python code/S6_SERIES_PUBLISH_c8_III_derive_final.py inspect \
    --extractor <final.json> --aux <final.aux> --pdf <final.pdf>
  Replace inspect by write only after the complete proposed output is approved.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import csv
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import re
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "S6_SERIES_PUBLISH_III.tex"
SCHEMA = "Paper-III-final-source-aux-reference-data-v1"
INVENTORY = "S6_SERIES_PUBLISH_inventory.csv"
TAGS = "S6_SERIES_PUBLISH_tags.tsv"
CHECKS = "S6_SERIES_PUBLISH_checks_III.md"
PRINTED = "records/S6_SERIES_PUBLISH_printed_statements.tsv"
GRAPH = "records/S6_SERIES_PUBLISH_reference_graph.tsv"
ALIASES = "records/S6_SERIES_PUBLISH_current_statement_aliases.tsv"
COUNTS = "records/S6_SERIES_PUBLISH_check_counts.tsv"
PER_STATEMENT = "records/S6_SERIES_PUBLISH_statement_check_counts.csv"
REQUIRED = "S6_SERIES_PUBLISH_required_progress_III.tsv"
FROZEN_COUNTS = "records/S6_SERIES_PUBLISH_III_current_check_counts.json"
# This uncounted section record belongs to II. Its bare heading label is also
# present in III. This exact source correspondence affects display only;
# the approved statement-event selection and the authoritative row are intact.
FOREIGN_SECTION_EVENT = ("publish:c4:outline:046", "sec:results", "S6_SERIES_PUBLISH_II.tex")
TABLES = {INVENTORY: ",", TAGS: "\t", PRINTED: "\t", GRAPH: "\t",
          ALIASES: "\t", COUNTS: "\t", PER_STATEMENT: ","}
csv.field_size_limit(100_000_000)
sys.dont_write_bytecode = True


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load_helper(filename, name):
    """Import reviewed pure helpers; never invoke either helper's main."""
    spec = importlib.util.spec_from_file_location(name, ROOT / "code" / filename)
    require(spec is not None and spec.loader is not None, filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class Inputs:
    def __init__(self):
        self.images = {}

    def read(self, path):
        path = Path(path).resolve()
        if path not in self.images:
            before = path.stat()
            value = path.read_bytes()
            after = path.stat()
            require((before.st_size, before.st_mtime_ns) ==
                    (after.st_size, after.st_mtime_ns), f"Input changed: {path}")
            self.images[path] = value
        return self.images[path]

    def unchanged(self):
        for path, value in self.images.items():
            require(path.read_bytes() == value, f"Input changed before write: {path}")


class RawTable:
    """Parse logical CSV records while retaining each exact physical byte span."""
    def __init__(self, raw, delimiter, name):
        self.raw, self.delimiter, self.name = raw, delimiter, name
        text = raw.decode("utf-8")
        physical = list(io.StringIO(text, newline=""))
        reader = csv.reader(physical, delimiter=delimiter, strict=True)
        self.fields = next(reader)
        require(len(self.fields) == len(set(self.fields)), f"Repeated field: {name}")
        require("paper" in self.fields, f"No paper field: {name}")
        previous = reader.line_num
        self.header = "".join(physical[:previous]).encode("utf-8")
        self.records = []
        for values in reader:
            end = reader.line_num
            exact = "".join(physical[previous:end]).encode("utf-8")
            previous = end
            require(not values or len(values) == len(self.fields), f"Malformed row: {name}")
            self.records.append((dict(zip(self.fields, values)) if values else None, exact))
        require(self.header + b"".join(raw for _, raw in self.records) == raw,
                f"Raw record coverage failed: {name}")

    @property
    def rows(self):
        return [row for row, _ in self.records if row is not None]

    @property
    def iii(self):
        return [dict(row) for row in self.rows if row["paper"] == "III"]

    def encode(self, row):
        require(not set(row) - set(self.fields), f"Unrecognized fields in {self.name}")
        stream = io.StringIO(newline="")
        writer = csv.DictWriter(stream, self.fields, delimiter=self.delimiter,
                                lineterminator="\n", extrasaction="raise")
        writer.writerow(row)
        return stream.getvalue().encode("utf-8")

    def replace_iii(self, replacement, key=None):
        """Keep inventory/tag row positions; rebuild other III rows in source order."""
        require(all(row.get("paper") == "III" for row in replacement), self.name)
        pieces = [self.header]
        if key is not None:
            by_key = {row[key]: row for row in replacement}
            require(len(by_key) == len(replacement), f"Repeated III key: {self.name}")
            last = max((i for i, (row, _) in enumerate(self.records)
                        if row is not None and row["paper"] == "III"), default=-1)
            for i, (row, exact) in enumerate(self.records):
                if row is None or row["paper"] != "III":
                    pieces.append(exact)
                else:
                    require(row[key] in by_key, f"Historical III row lost: {self.name} {row[key]}")
                    pieces.append(self.encode(by_key.pop(row[key])))
                if i == last:
                    pieces.extend(self.encode(r) for r in replacement if r[key] in by_key)
            if last == -1:
                pieces.extend(self.encode(r) for r in replacement)
        else:
            inserted = False
            for row, exact in self.records:
                if row is not None and row["paper"] == "III":
                    if not inserted:
                        pieces.extend(self.encode(r) for r in replacement)
                        inserted = True
                else:
                    pieces.append(exact)
            if not inserted:
                pieces.extend(self.encode(r) for r in replacement)
        result = b"".join(pieces)
        parsed = RawTable(result, self.delimiter, self.name + " (candidate)")
        other = lambda table: [exact for row, exact in table.records
                              if row is None or row["paper"] != "III"]
        require(parsed.header == self.header and other(parsed) == other(self),
                f"Non-III bytes changed: {self.name}")
        require(len(parsed.iii) == len(replacement), f"III row count changed: {self.name}")
        return result


def hidden_free(text, extractor):
    """c4 hidden-metadata removal, with the reviewed balanced-group helper."""
    text = extractor.masked_tex(text)
    arities = {"StatementRecord": 4, "Uses": 1, "UsedBy": 1}
    pattern = re.compile(r"\\(StatementRecord|Uses|UsedBy)\s*\{")
    while match := pattern.search(text):
        end = match.end() - 1
        for _ in range(arities[match[1]]):
            _, end = extractor.group(text, end)
        text = text[:match.start()] + text[end:]
    return text


def references(text, positions, extractor):
    """c4 literal reference/range map; no hidden metadata contributes edges."""
    text = hidden_free(text, extractor)
    groups = re.findall(r"\\(?:SeriesRef(?:Text)?|[Cc]ref|[Ee]qref|ref|[Aa]utoref|nameref)\*?\s*\{([^}]+)\}", text)
    refs = {key.strip() for group in groups for key in group.split(",") if key.strip()}
    refs.update(re.findall(r"\\hyperref\s*\[([^]]+)\]", text))
    refs.update("tag:" + tag for tag in re.findall(r"\\hyperlink\s*\{tag-([^}]+)\}", text))
    for left, right in re.findall(r"\\[Cc]refrange\*?\s*\{([^}]+)\}\s*\{([^}]+)\}", text):
        refs.update((left, right))
        if left in positions and right in positions:
            lo, hi = sorted((positions[left], positions[right]))
            refs.update(key for key, offset in positions.items() if lo <= offset <= hi)
    return refs


def input_model(args, inputs, selector, extractor):
    text = inputs.read(SOURCE).decode("utf-8")
    aux_text = inputs.read(args.aux).decode("utf-8")
    pdf_bytes = inputs.read(args.pdf)
    metadata = json.loads(inputs.read(args.extractor))
    require(metadata.get("schema") == SCHEMA and metadata.get("paper") == "III", "Wrong extractor schema")
    for key, path in (("source", SOURCE), ("aux", args.aux), ("pdf", args.pdf)):
        require(Path(metadata["inputs"][key]).resolve() == Path(path).resolve(), f"Extractor input mismatch: {key}")
    require(pdf_bytes.startswith(b"%PDF-"), "Final PDF is absent or invalid")
    errors = [row for row in metadata["issues"] if row["severity"] == "error"]
    require(not errors, f"Unresolved extractor errors: {errors}")
    # Re-evaluate pure structural maps and actual PDF destinations, without
    # invoking the extractor CLI or writing a second extraction product.
    parsed = extractor.parse_source(text)
    auxiliary = extractor.parse_aux(aux_text)
    needed = {row["anchor"] for row in auxiliary if not row["is_cref_auxiliary"]}
    needed.update(row["name"] for row in parsed["hypertargets"])
    needed.update(key for row in parsed["references"] if row["command"] == "hyperlink" for key in row["keys"])
    needed.update(row["target_tex"] for row in parsed["series_definitions"].values() if row.get("scope") == "local")
    actual_pdf = extractor.read_pdf(Path(args.pdf), needed)
    require(actual_pdf == metadata["pdf"], "PDF destinations changed after extraction")
    fresh = extractor.assemble(parsed, auxiliary, actual_pdf)
    require(fresh == {key: value for key, value in metadata.items() if key != "inputs"},
            "Source/aux/extractor correspondence changed")
    inputs.read(ROOT / "CHECK_EVENTS.tsv")
    inputs.read(ROOT / TAGS)
    inputs.read(ROOT.parent / "CLAUDE_INTAKE_CHECK_EVENTS_cp92_100.tsv")
    data = selector.current_data(ROOT)
    frozen = json.loads(inputs.read(ROOT / FROZEN_COUNTS))
    require(sorted(frozen["selected_event_ids"]) == sorted(e["event_id"] for e in data["selected"]),
            "Statement event selection changed after count freeze")
    require(frozen["current_formal_owners"] == len(data["statements"])
            and frozen["current_statement_subject_identifiers"] == len(data["subjects"])
            and frozen["selected_event_associations"] == len(data["selected"]),
            "The frozen count denominators changed")
    require(frozen["counts"] == {kind: data["counts"][kind] for kind in selector.TYPES},
            "Type counts changed after count freeze")
    require(frozen["selected_evidence_groups"] == sorted(data["groups"]),
            "Selected evidence-group IDs changed after count freeze")
    require(frozen["declared_evidence_groups"] == len(data["groups"]),
            "The frozen evidence-group count changed")
    require(frozen["literal_intake_associations"] == data["exact_intake_details"],
            "The eight verified intake associations changed after the count freeze")
    source = metadata["source"]
    environments = source["environments"]
    formal = [environments[i] for i in source["formal_environments"]]
    require([r["primary_label"] for r in formal] == [r.statement_id for r in data["statements"]],
            "Extractor and approved selector disagree on current owners")
    env_owner = {r["id"]: r["primary_label"] for r in formal}
    labels = {row["key"]: row for row in source["labels"]}
    require(len(labels) == len(source["labels"]), "Repeated source label")
    actual_owners = {key: env_owner[row["formal_owner_environment_id"]]
                     for key, row in labels.items() if row["formal_owner_environment_id"] is not None}
    require(actual_owners == data["owners"], "Extractor/selector ownership map differs")
    bindings = {}
    for key, row in labels.items():
        require(len(row["aux_records"]) == 1, f"Nonunique final aux label: {key}")
        bindings[key] = row["aux_records"][0]
    required_raw = inputs.read(ROOT / REQUIRED)
    required = list(csv.DictReader(io.StringIO(required_raw.decode("utf-8")), delimiter="\t"))
    require(len(required) == 128 and all(r["paper"] == "III" and r["status"] == "done" for r in required),
            "The admitted 128 III required dispositions are not intact")
    require(all(r["label"] in labels for r in required), "A required target lost its literal label")
    # Preserve the older I/II-only completion record as bytes, without deriving
    # any III status from it or refreshing it.
    inputs.read(ROOT / "records/S6_SERIES_PUBLISH_required_check_completion_manifest.json")
    return dict(text=text, metadata=metadata, source=source, formal=formal,
                labels=labels, bindings=bindings, data=data, required=required,
                source_sha=hashlib.sha256(inputs.read(SOURCE)).hexdigest(),
                pdf_sha=hashlib.sha256(pdf_bytes).hexdigest(),
                event_sha=hashlib.sha256(inputs.read(ROOT / "CHECK_EVENTS.tsv")).hexdigest())


def tag_rows(model, table, extractor):
    data, source, bindings = model["data"], model["source"], model["bindings"]
    ours = table.iii
    all_by_tag = {row["tag"]: row for row in table.rows}
    require(len(all_by_tag) == len(table.rows), "Existing permanent tags are not unique")
    current_targets = {row["name"][4:]: row for row in source["hypertargets"] if row["name"].startswith("tag-")}
    require(len(current_targets) == sum(row["name"].startswith("tag-") for row in source["hypertargets"]),
            "Repeated current permanent tag target")
    primary = {row.tag: row.statement_id for row in data["statements"]}
    clean = extractor.masked_tex(model["text"])
    ordered_labels = source["labels"]
    for tag, target in current_targets.items():
        if tag in all_by_tag:
            require(all_by_tag[tag]["paper"] == "III", f"Tag reused from another paper: {tag}")
            continue
        label = primary.get(tag)
        if label is None:
            after = [r for r in ordered_labels if r["offset"] >= target["end_offset"]]
            before = [r for r in ordered_labels if r["end_offset"] <= target["offset"]]
            following = after[0] if after else None
            preceding = before[-1] if before else None
            candidates = []
            if following and not clean[target["end_offset"]:following["offset"]].strip():
                candidates.append(following["key"])
            if preceding and not clean[preceding["end_offset"]:target["offset"]].strip():
                candidates.append(preceding["key"])
            require(candidates, f"New tag lacks an explicit adjacent literal label: {tag}")
            if len(set(candidates)) > 1:
                triples = {(bindings[k]["number_tex"], bindings[k]["page_tex"], bindings[k]["anchor"]) for k in candidates}
                require(len(triples) == 1, f"Ambiguous new tag label: {tag} {candidates}")
            label = candidates[0]  # Following label first; equivalent aux aliases were checked.
        require(label in bindings, f"New tag label has no final aux record: {tag}")
        display = model["labels"][label]["display_environment_id"]
        row = {key: "" for key in table.fields}
        row.update(tag=tag, paper="III", label=label,
                   kind="statement" if label in data["active"] else "equation" if display is not None else "reference target",
                   status="open" if any(r.statement_id == label and r.kind in ("problem", "question", "openq", "conjecture") for r in data["statements"]) else "proved" if label in data["active"] else "",
                   publication_disposition="Literal new target in the final III source; no event or proof credit is created.")
        ours.append(row)
        all_by_tag[tag] = row
    for row in ours:
        label = row["label"]
        if label in bindings:
            row["number"], row["page"] = bindings[label]["number_tex"], bindings[label]["page_tex"]
            row["current_owner"] = data["owners"].get(label, "")
            note = "Current III number/page from the final aux; structural owner from the source and its adjacent proof."
        else:
            note = "Historical registry target retained; no current literal III label was found, so its recorded historical number/page is unchanged."
        prior = row.get("publication_disposition", "")
        row["publication_disposition"] = prior if note in prior else prior + (" " if prior else "") + note
    require({r["tag"] for r in table.iii} <= {r["tag"] for r in ours}, "Historical III tag lost")
    return ours


def reference_model(model, tags, extractor):
    source, data, text = model["source"], model["data"], model["text"]
    positions = {key: row["offset"] for key, row in model["labels"].items()}
    by_id = {row.statement_id: row for row in data["statements"]}
    by_tag = {row["tag"]: row for row in tags}
    definitions = source["series_definitions"]
    external = {}
    def resolve(key):
        if key.startswith("tag:"):
            require(key[4:] in by_tag, f"Literal hyperlink has no permanent tag: {key}")
            row = by_tag[key[4:]]
            if row["paper"] == "III":
                return data["owners"].get(row["label"], row["label"])
            external[key] = row
            return key
        definition = definitions.get(key)
        if definition and definition.get("scope") == "local":
            key = definition["local_label"]
        elif definition and definition.get("scope") == "external":
            match = re.search(r"(?:\\?#)tag-([^/?#{}]+)", definition["target_tex"])
            require(match and match[1] in by_tag, f"External reference has no retained tag: {key}")
            row = by_tag[match[1]]
            # A tag identity avoids collapsing same-spelled labels of two papers.
            target = "tag:" + row["tag"]
            external[target] = row
            return target
        return data["owners"].get(key, key)
    refs = {row.statement_id: references(text[row.start:row.stop], positions, extractor)
            for row in data["statements"]}
    steps = defaultdict(set)
    outlines = [row for row in source["hypertargets"] if re.fullmatch(r"outline-III-[A-G]", row["name"])]
    require(len(outlines) == 7, "The seven main outlines are not intact")
    for outline in outlines:
        letter = outline["name"][-1]
        sid = "series:III:" + letter
        require(sid in by_id, f"Outline lacks its main owner: {sid}")
        lists = [row for row in source["environments"] if row["name"] == "enumerate" and row["offset"] > outline["end_offset"]]
        require(lists, f"Outline list absent: {sid}")
        listing = min(lists, key=lambda row: row["offset"])
        require(not any(outline["offset"] < other["offset"] < listing["end_offset"] for other in outlines), f"Overlapping outlines: {sid}")
        refs[sid].update(references(text[listing["offset"]:listing["end_offset"]], positions, extractor))
        parts = [row for row in source["hypertargets"] if row["name"].startswith("step-III-" + letter + "-")
                 and listing["offset"] <= row["offset"] < listing["end_offset"]]
        for index, part in enumerate(parts):
            end = parts[index + 1]["offset"] if index + 1 < len(parts) else listing["end_offset"]
            for key in references(text[part["end_offset"]:end], positions, extractor):
                steps[resolve(key)].add(part["name"])
    graph = {sid: {resolve(key) for key in targets} - {sid} for sid, targets in refs.items()}
    reverse = defaultdict(set)
    for sid, targets in graph.items():
        for target in targets:
            reverse[target].add(sid)
    main = {row.statement_id for row in data["statements"] if row.kind == "maintheorem"}
    reachable, todo = set(main), list(main)
    while todo:
        for target in graph[todo.pop()]:
            if target in by_id and target not in reachable:
                reachable.add(target)
                todo.append(target)
    return dict(refs=refs, graph=graph, reverse=reverse, steps=steps, main=main,
                reachable=reachable, external=external, by_id=by_id)


def event_map(data, selector):
    result = defaultdict(list)
    for event in data["events"]:
        result[selector.resolved_subject(data, event)].append(event)
    return result


def inventory_rows(model, table, refs, selector):
    data = model["data"]
    ours = table.iii
    by_label = {row["label"]: row for row in ours}
    require(len(by_label) == len(ours), "Repeated III inventory identifier")
    events = event_map(data, selector)
    selected = {e["event_id"] for e in data["selected"]}
    for owner in data["statements"]:
        if owner.statement_id not in by_label:
            entry = {key: "" for key in table.fields}
            entry.update(paper="III", label=owner.statement_id, tag=owner.tag, kind=owner.kind,
                         status="open" if owner.kind in ("problem", "question", "openq", "conjecture") else "proved",
                         main_or_supporting="main" if owner.statement_id in refs["main"] else "supporting",
                         source_run="Current Paper III publication owner", source_id=owner.statement_id,
                         check_record="{}", notes="Current formal owner. Exact events remain at their recorded subjects; structural ownership creates no independent credit.")
            ours.append(entry)
            by_label[owner.statement_id] = entry
    for entry in ours:
        sid = entry["label"]
        owner = data["owners"].get(sid, "")
        direct = events[sid]
        live = [e for e in direct if e["event_id"] in selected]
        prior = entry.get("check_record", "")
        try:
            record = json.loads(prior) if prior.strip().startswith("{") else {"retained_source_record": prior}
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid retained check_record: {sid}") from exc
        require(isinstance(record, dict), f"Non-object check_record: {sid}")
        record.update(canonical_check_events=direct,
                      current_ledger_sha256=model["event_sha"],
                      current_event_scope="Every event retains its exact original fields, including retained withdrawn records. The approved selector resolves exact tag aliases and eight individually verified intake associations. Only its selected IDs enter current statement counts; this association adds no independent-check credit.",
                      selected_current_event_ids=[e["event_id"] for e in live],
                      current_literal_label_present=sid in model["labels"],
                      current_owner_check_entry=(CHECKS + "#tag-" + refs["by_id"][owner].tag) if owner in refs["by_id"] else "")
        entry["check_record"] = json.dumps(record, ensure_ascii=False)
        counts = Counter(e["type"] for e in live)
        entry["check_summary"] = f"{len(direct)} retained event rows attached by the reviewed subject resolver; {len(live)} selected current statement associations; " + "; ".join(f"{kind}: {counts[kind]}" for kind in selector.TYPES)
        entry["current_statement_owner"] = owner
        entry["current_source_sha256"], entry["current_pdf_sha256"] = model["source_sha"], model["pdf_sha"]
        if sid in model["bindings"]:
            entry["current_number"], entry["current_page"] = model["bindings"][sid]["number_tex"], model["bindings"][sid]["page_tex"]
        if owner in refs["by_id"]:
            entry["uses"] = ";".join(sorted(refs["graph"][owner]))
            entry["used_by"] = ";".join(sorted(refs["reverse"][owner]))
            entry["outline_backlinks"] = ";".join(sorted(refs["steps"][owner]))
            entry["publication_review_status"] = "Current source/aux ownership and reference records; admitted unit comparisons and the separate reading log retain all mathematical and page-review scope."
        # Historical status, credit, literature, confidence and completion
        # fields are retained. This generator cannot close those assessments.
    return ours


def checks_document(model, tags, inventory, refs, selector):
    data, bindings = model["data"], model["bindings"]
    iii_tags = [row for row in tags if row["paper"] == "III"]
    by_label = {row["label"]: row for row in iii_tags}
    owner_tags = defaultdict(list)
    for row in iii_tags:
        owner_tags[data["owners"].get(row["label"], row["label"])].append(row)
    grouped_events = defaultdict(list)
    local_targets = set(model["labels"]) | set(by_label) | {row["label"] for row in inventory}
    selected = {e["event_id"] for e in data["selected"]}
    foreign_id, foreign_subject, foreign_source = FOREIGN_SECTION_EVENT
    foreign = [event for event in data["events"] if event["event_id"] == foreign_id]
    require(len(foreign) == 1 and foreign[0]["statement_id"] == foreign_subject
            and foreign[0]["source_file"] == foreign_source and foreign_id not in selected,
            "The reviewed cross-paper section-event correspondence changed")
    for event in data["events"]:
        if event["event_id"] == foreign_id:
            continue
        subject = selector.resolved_subject(data, event)
        if subject in local_targets:
            grouped_events[data["owners"].get(subject, subject)].append(event)
    displayed = set()
    def link(target):
        if target in refs["by_id"]:
            owner = refs["by_id"][target]
            return f"[III.{bindings[target]['number_tex']}](#tag-{owner.tag})"
        if target in refs["external"]:
            row = refs["external"][target]
            return f"[{row['paper']}.{row['number']}](S6_SERIES_PUBLISH_checks_{row['paper']}.md#tag-{row['tag']})"
        row = by_label.get(target)
        if row:
            return f"[III.{row['number']}](#tag-{row['tag']})"
        return "`" + target + "`"
    document = ["# Paper III: statements, references and check events\n\n",
                f"Source SHA-256: `{model['source_sha']}`. PDF SHA-256: `{model['pdf_sha']}`.\n\n",
                f"Authoritative event-table SHA-256: `{model['event_sha']}`. Numbers, pages and structural owners use the final extractor and aux.\n\n",
                selector.count_prose(data) + "\n\n",
                "Every event keeps its original subject, type, who, outcome and evidence group. Eight intake rows use the exact event-ID, full-subject and tag associations verified by S6_SERIES_PUBLISH_c9_III_check_counts.py; their original five intake fields remain verbatim. The designated withdrawn event is retained below and excluded from the counts. Structural ownership, citation extraction and tag aliases add no mathematical check or proof equivalence. Page inspection remains recorded separately in S6_SERIES_PUBLISH_reading_III.md. The admitted 128 required dispositions remain unchanged in S6_SERIES_PUBLISH_required_progress_III.tsv.\n\n"]
    subjects_by_owner = defaultdict(set)
    for subject in data["subjects"]:
        subjects_by_owner[data["owners"].get(subject, subject)].add(subject)
    formal = {row["primary_label"]: row for row in model["formal"]}
    owners = [row.statement_id for row in data["statements"]]
    extras = sorted((set(owner_tags) | set(grouped_events)) - set(owners))
    for sid in owners + extras:
        for row in owner_tags[sid]:
            document.append(f"<a id=\"tag-{row['tag']}\"></a>\n<a id=\"uses-{row['tag']}\"></a>\n")
        binding = bindings.get(sid)
        if sid in formal:
            env = formal[sid]
            document.append(f"\n## {env['name'].capitalize()} III.{binding['number_tex']}: {env['title_tex'] or ''}\n\n")
            document.append(f"Label: `{sid}`. Page {binding['page_tex']}. Permanent tag: `{refs['by_id'][sid].tag}`.\n\n")
            document.append("Retained statement identifiers: " + ", ".join("`" + x + "`" for x in sorted(subjects_by_owner[sid])) + ".\n\n")
            document.append("Uses: " + (", ".join(link(x) for x in sorted(refs["graph"][sid])) or "No literal numbered-result reference in this statement, immediate proof or own outline.") + "\n\n")
            document.append("Used by: " + (", ".join(link(x) for x in sorted(refs["reverse"][sid])) or "No current formal owner has a literal reference edge to this owner.") + "\n\n")
            document.append("Outline steps: " + (", ".join("`" + x + "`" for x in sorted(refs["steps"][sid])) or "None.") + "\n\n")
        else:
            document.append(f"\n## Retained target `{sid}`\n\n")
            document.append((f"Current literal target III.{binding['number_tex']}, page {binding['page_tex']}." if binding else "Historical registry target; no current literal source label was found.") + " This target has no formal statement owner in the current source map.\n\n")
        targets = [row["label"] for row in owner_tags[sid] if row["label"] != sid]
        if targets:
            document.append("Other exact tagged targets in this entry: " + ", ".join("`" + x + "`" for x in targets) + ". Their exact-subject events retain their own scope.\n\n")
        document.append("### Recorded events\n\n")
        for event in grouped_events[sid]:
            require(event["event_id"] not in displayed, "Event displayed twice")
            displayed.add(event["event_id"])
            counted = "Included in current statement totals." if event["event_id"] in selected else "Retained record outside current statement totals."
            document.append(f"#### {event['date']} — {event['type']}\n\nWho: {event['who']}\n\nEvent: `{event['event_id']}`. Subject: `{event['statement_id']}`. Evidence group: `{selector.group_key(event)}`. {counted}\n\n")
            document.append("Source: `" + event.get("source_file", "") + "`" + ("; locus: " + event["where"] if event.get("where") else "") + ".\n\n")
            document.append(event["outcome"] + "\n\n")
        if not grouped_events[sid]:
            document.append("No authoritative event is attached to this entry by the reviewed subject resolver. Its cited inputs retain their own records.\n\n")
    require(selected <= displayed, "A selected event is absent from the check document")
    require(data["withdrawn"]["event_id"] in displayed, "The withdrawn record was lost")
    return "".join(document).encode("utf-8")


def derived_rows(model, tables, refs, selector, inputs):
    data = model["data"]
    resolve = lambda event: selector.resolved_subject(data, event)
    printed = [dict(paper="III", source=str(SOURCE), statement_id=row.statement_id, kind=row.kind, tag=row.tag,
                    labels=";".join(row.labels), owned_labels=";".join(row.owned_labels),
                    refs=";".join(sorted(refs["refs"][row.statement_id])), line=row.line,
                    reference_scope="Literal references in the current statement, immediate proof and its own outline; hidden historical metadata excluded. Exact source/aux owner map, with no mathematical premise or independence inference.") for row in data["statements"]]
    graph = [dict(paper="III", **{"from": sid, "to": target}, within_current_paper=str(target in refs["by_id"]).lower(),
                  interpretation="Literal current reference resolved through its actual local owner or external permanent tag; admitted comparisons retain mathematical premise scope.")
             for sid in refs["graph"] for target in sorted(refs["graph"][sid])]
    aliases = [dict(paper="III", current_statement_id=data["owners"].get(sid, sid), retained_statement_identifier=sid,
                    scope="Exact current owner and retained eligible statement identifier; events retain their original subjects and are not duplicated or upgraded.") for sid in sorted(data["subjects"])]
    baseline = RawTable(inputs.read(ROOT.parent / "S6_SERIES_GRIND_tags.tsv"), "\t", "baseline tags")
    scopes = {
        "cp10_printed_statements": {r["label"] for r in baseline.iii if r["kind"] == "statement"},
        "cp10_all_tagged_targets": {r["label"] for r in baseline.iii},
        "current_primary_statement_identifiers": data["active"],
        "current_printed_statements_and_definitions": data["subjects"],
    }
    live = [event for event in data["events"] if event["event_id"] != data["withdrawn"]["event_id"]]
    step_names = {r["name"] for r in model["source"]["hypertargets"] if r["name"].startswith("step-III-")}
    step_events = 0
    for event in live:
        match = re.fullmatch(r"series:III:([A-G]) step ([1-9][0-9]*)", event["statement_id"])
        if match and f"step-III-{match[1]}-{match[2]}" in step_names:
            step_events += 1
    counts = []
    for scope, subjects in scopes.items():
        selected = [e for e in live if resolve(e) in subjects]
        if scope.startswith("current_"):
            authority = [e for e in data["selected"] if resolve(e) in subjects]
            require([e["event_id"] for e in selected] == [e["event_id"] for e in authority], "Scope disagrees with approved selector")
        kinds = Counter(e["type"] for e in selected)
        require(set(kinds) <= set(selector.TYPES), f"Unexpected exact recorded type: {scope}")
        counts.append(dict(paper="III", scope=scope, statements=len(data["statements"]) if scope.startswith("current_") else len(subjects),
                           subject_identifiers=len(subjects), event_associations=len(selected),
                           declared_evidence_groups=len({selector.group_key(e) for e in selected}),
                           outline_step_associations_separate=step_events if scope.startswith("current_") else 0,
                           **{kind: kinds[kind] for kind in selector.TYPES}))
    # This cp10-column table retains its historical row domain. New definition
    # owners do not create new required-check rows or candidate gates.
    per_statement = tables[PER_STATEMENT].iii
    by_subject = event_map(data, selector)
    selected_ids = {e["event_id"] for e in data["selected"]}
    for row in per_statement:
        sid = row["label"]
        exact = [e for e in by_subject[sid] if e["event_id"] in selected_ids]
        substantive = [e for e in exact if e["type"] in selector.TYPES[:3]]
        groups = {selector.group_key(e) for e in substantive}
        def checker_label(event):
            value = re.sub(r"\s*\(.*?\)", "", event["who"])
            return value.split(",")[0].strip() + " | " + (value.split(",")[-1].strip() if "," in value else "")
        checkers = {checker_label(e) for e in substantive}
        owner = data["owners"].get(sid, row.get("current_statement_owner") or sid)
        row.update(active_current_statement=str(sid in data["subjects"]).lower(), current_statement_owner=owner,
                   main_dependency_reference_closure=str(owner in refs["reachable"]).lower(),
                   substantive_associations=len(substantive), substantive_evidence_groups=len(groups),
                   distinct_checker_labels=len(checkers), all_associations=len(exact),
                   below_bar="yes" if len(groups) < 2 or len(checkers) < 2 else "two_only" if len(groups) < 3 else "no",
                   checker_labels=" || ".join(sorted(checkers)))
    return {PRINTED: printed, GRAPH: graph, ALIASES: aliases, COUNTS: counts, PER_STATEMENT: per_statement}


def prepare(args):
    inputs = Inputs()
    selector = load_helper("S6_SERIES_PUBLISH_c9_III_check_counts.py", "s6_iii_count_authority")
    extractor = load_helper("S6_SERIES_PUBLISH_c8_tex_extract_final_III.py", "s6_iii_final_extractor")
    model = input_model(args, inputs, selector, extractor)
    tables = {name: RawTable(inputs.read(ROOT / name), delimiter, name) for name, delimiter in TABLES.items()}
    iii_tags = tag_rows(model, tables[TAGS], extractor)
    tags = [row for row in tables[TAGS].rows if row["paper"] != "III"] + iii_tags
    refs = reference_model(model, tags, extractor)
    inventory = inventory_rows(model, tables[INVENTORY], refs, selector)
    replacements = derived_rows(model, tables, refs, selector, inputs)
    outputs = {ROOT / name: tables[name].replace_iii(rows) for name, rows in replacements.items()}
    outputs[ROOT / TAGS] = tables[TAGS].replace_iii(iii_tags, "tag")
    outputs[ROOT / INVENTORY] = tables[INVENTORY].replace_iii(inventory, "label")
    inputs.read(ROOT / CHECKS)
    outputs[ROOT / CHECKS] = checks_document(model, tags, inventory, refs, selector)
    require(set(outputs) == {ROOT / name for name in TABLES} | {ROOT / CHECKS}, "Unexpected output path")
    require(all(b"\r" not in content for content in outputs.values()), "A derived text candidate contains a non-LF line ending")
    inputs.unchanged()
    summary = dict(mode=args.mode, current_formal_owners=len(model["data"]["statements"]),
                   selected_statement_events=len(model["data"]["selected"]), evidence_groups=len(model["data"]["groups"]),
                   required_dispositions_preserved=len(model["required"]), iii_inventory_rows=len(inventory),
                   iii_tags=len(iii_tags), outputs=[str(path.relative_to(ROOT)) for path in outputs],
                   extractor_warnings=[row for row in model["metadata"]["issues"] if row["severity"] != "error"],
                   interpretation="Exact recorded events, raw non-III bytes and required dispositions preserved; no new mathematical or page-reading credit.")
    return inputs, outputs, summary


def write_outputs(inputs, outputs):
    """Validate everything before replacing; temporary candidates are removed."""
    inputs.unchanged()
    staged = {}
    try:
        for path, content in outputs.items():
            with tempfile.NamedTemporaryFile(dir=path.parent, prefix=path.name + ".", suffix=".tmp", delete=False) as stream:
                temporary = Path(stream.name)
                staged[path] = temporary
                stream.write(content)
        inputs.unchanged()
        for path, temporary in staged.items():
            os.replace(temporary, path)
        for path, content in outputs.items():
            require(path.read_bytes() == content, f"Written bytes differ: {path}")
        for path, original in inputs.images.items():
            if path not in outputs:
                require(path.read_bytes() == original, f"Read-only input changed: {path}")
    finally:
        for temporary in staged.values():
            if temporary.exists():
                temporary.unlink()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", nargs="?", choices=("inspect", "write"), default="inspect")
    parser.add_argument("--extractor", type=Path, required=True)
    parser.add_argument("--aux", type=Path, required=True)
    parser.add_argument("--pdf", type=Path, required=True)
    args = parser.parse_args()
    inputs, outputs, summary = prepare(args)
    if args.mode == "write":
        write_outputs(inputs, outputs)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print("DERIVED_PRODUCTS_WRITTEN" if args.mode == "write" else "INSPECT_ONLY; NO_FILES_WRITTEN")


if __name__ == "__main__":
    main()
