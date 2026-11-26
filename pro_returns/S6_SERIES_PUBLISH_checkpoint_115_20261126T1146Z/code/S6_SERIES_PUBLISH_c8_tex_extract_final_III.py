#!/usr/bin/env python3
"""Extract Paper III's final source/aux/PDF reference data, after the final build.

This program is deliberately not a build driver or a records updater. It reads
only the caller's III source, its final auxiliary file and its final PDF, and
writes one explicitly selected JSON file. It reads no historical inventories,
tag registry, CHECK_EVENTS, progress table, or other paper. It creates no hashes,
receipt, certification, mathematical credit, or visual-page-reading claim.

Source spans are lexical TeX evidence, not expanded TeX or a dependency proof.
Every active literal label and hypertarget occurrence is retained separately.
Numbers/pages/anchors come from the actual aux; live destination positions come
from the actual PDF. In particular, aliases are never collapsed into one label.

Example, to be run only once root authorizes final derivation:
  python code/S6_SERIES_PUBLISH_c8_tex_extract_final_III.py \
    --aux <final-build>/S6_SERIES_PUBLISH_III.aux \
    --pdf <final-build>/S6_SERIES_PUBLISH_III.pdf \
    --output <chosen-final-metadata-path>.json
"""

from __future__ import annotations

import argparse
from bisect import bisect_right
from collections import Counter, defaultdict
import json
import os
from pathlib import Path
import re
import tempfile


ROOT = Path(__file__).resolve().parents[1]
CONTROL = re.compile(r"\\([A-Za-z@]+|[^\r\n])")
DISPLAY = {
    "equation", "equation*", "align", "align*", "alignat", "alignat*",
    "flalign", "flalign*", "gather", "gather*", "multline", "multline*",
    "eqnarray", "eqnarray*", "displaymath", "\\[",
}
REFERENCE = {
    "ref", "eqref", "pageref", "autoref", "Autoref", "nameref",
    "cref", "Cref", "cpageref", "Cpageref", "namecref", "nameCref",
    "lcnamecref", "namecrefs", "nameCrefs", "lcnamecrefs", "labelcref",
    "labelcpageref", "crefrange", "Crefrange", "cpagerefrange",
    "Cpagerefrange", "SeriesRef", "SeriesRefText", "hyperlink",
}
RANGES = {"crefrange", "Crefrange", "cpagerefrange", "Cpagerefrange"}
RAW_ENVS = {"verbatim", "verbatim*", "Verbatim", "lstlisting", "minted", "comment"}


def escaped(text: str, position: int) -> bool:
    count = 0
    while position > 0 and text[position - 1] == "\\":
        position -= 1
        count += 1
    return bool(count % 2)


def space(text: str, position: int) -> int:
    while position < len(text) and text[position].isspace():
        position += 1
    return position


def group(text: str, position: int, opener: str = "{") -> tuple[str, int]:
    position = space(text, position)
    closer = "}" if opener == "{" else "]"
    if position >= len(text) or text[position] != opener:
        raise ValueError(f"Expected {opener!r} at character {position}")
    start, depth, braces = position + 1, 1, 0
    position += 1
    while position < len(text):
        char = text[position]
        if not escaped(text, position):
            if opener == "[" and char == "{":
                braces += 1
            elif opener == "[" and char == "}":
                braces -= 1
            elif not braces and char == opener:
                depth += 1
            elif not braces and char == closer:
                depth -= 1
                if depth == 0:
                    return text[start:position], position + 1
        position += 1
    raise ValueError(f"Unclosed {opener!r} group starting at character {start - 1}")


def masked_tex(text: str) -> str:
    """Mask comments/verb material while preserving every offset and newline."""
    chars = list(text)
    position = 0
    while position < len(text):
        if text[position] == "%" and not escaped(text, position):
            end = text.find("\n", position)
            if end < 0:
                end = len(text)
            chars[position:end] = " " * (end - position)
            position = end
        elif text.startswith(r"\begin{", position) and not escaped(text, position):
            name, opening_end = group(text, position + len(r"\begin"))
            if name in RAW_ENVS:
                end = text.find(r"\end{" + name + "}", opening_end)
                if end < 0:
                    raise ValueError(f"Unclosed raw environment {name!r}")
                for index in range(opening_end, end):
                    if chars[index] != "\n":
                        chars[index] = " "
                position = end
            else:
                position = opening_end
        elif text.startswith(r"\verb", position) and not escaped(text, position):
            match = CONTROL.match(text, position)
            if match and match[1] == "verb":
                end = match.end()
                if end < len(text) and text[end] == "*":
                    end += 1
                if end >= len(text) or text[end].isspace():
                    raise ValueError(f"Invalid literal verb command at {position}")
                close = text.find(text[end], end + 1)
                if close < 0:
                    raise ValueError(f"Unclosed literal verb command at {position}")
                chars[position:close + 1] = " " * (close + 1 - position)
                position = close + 1
            else:
                position += 1
        else:
            position += 1
    return "".join(chars)


def location(newlines: list[int], offset: int) -> dict:
    index = bisect_right(newlines, offset)
    previous = newlines[index - 1] if index else -1
    return {"offset": offset, "line": index + 1, "column": offset - previous}


def literal(value: str) -> bool:
    return bool(value) and not any(char in value for char in "\\#{}\n\r")


def literal_reference_tokens(raw: str) -> str:
    """Token spelling for literal keys: endlines supply spaces; comments do not.

    Leading/trailing key spaces are deliberately retained. Pass 01 exposed
    three such actual cleveref failures, which str.strip() would have hidden.
    This handles ordinary literal keys only; it does not expand TeX macros.
    """
    output = []
    position = 0
    while position < len(raw):
        char = raw[position]
        if char == "%" and not escaped(raw, position):
            end = raw.find("\n", position)
            if end < 0:
                break
            position = end + 1
            while position < len(raw) and raw[position] in " \t":
                position += 1
        elif char in "\r\n":
            output.append(" ")
            position += 1
            while position < len(raw) and raw[position] in " \t":
                position += 1
        else:
            output.append(char)
            position += 1
    return re.sub(r"[ \t]+", " ", "".join(output))


def theorem_declarations(preamble: str) -> dict:
    declarations = {}
    for match in re.finditer(r"\\newtheorem\*?\s*\{", preamble):
        position = match.end() - 1
        name, position = group(preamble, position)
        counter = None
        position = space(preamble, position)
        if preamble[position:position + 1] == "[":
            counter, position = group(preamble, position, "[")
        title, position = group(preamble, position)
        parent_counter = None
        position = space(preamble, position)
        if preamble[position:position + 1] == "[":
            parent_counter, position = group(preamble, position, "[")
        declarations[name] = {
            "printed_kind_tex": title, "shared_counter_tex": counter,
            "reset_counter_tex": parent_counter,
            "starred": "*" in match[0],
        }
    return declarations


def series_definitions(preamble: str) -> dict:
    definitions = {}
    pattern = re.compile(r"\\expandafter\s*\\def\s*\\csname\s+SRef@([^\s]+)\\endcsname")
    for match in pattern.finditer(preamble):
        key = match[1]
        body, end = group(preamble, match.end())
        if key in definitions:
            raise ValueError(f"Repeated active SeriesRef definition: {key}")
        row = {"key": key, "definition_tex": body, "offset": match.start(), "end_offset": end}
        link = re.search(r"\\(href|hyperlink)\s*\{", body)
        if link:
            target, cursor = group(body, link.end() - 1)
            printed, cursor = group(body, cursor)
            row.update(link_command=link[1], target_tex=target, printed_tex=printed)
            if link[1] == "href":
                row["scope"] = "external"
                row["url"] = target.replace(r"\#", "#")
            else:
                row["scope"] = "local"
                local = re.search(r"\\ref\*?\s*\{", printed)
                if local:
                    row["local_label"], _ = group(printed, local.end() - 1)
        definitions[key] = row
    return definitions


def parse_source(text: str) -> dict:
    clean = masked_tex(text)
    begin = clean.index(r"\begin{document}") + len(r"\begin{document}")
    end = clean.index(r"\end{document}", begin)
    preamble = clean[:begin]
    declarations = theorem_declarations(preamble)
    newlines = [match.start() for match in re.finditer("\n", text)]
    result = {
        "theorem_declarations": declarations,
        "series_definitions": series_definitions(preamble),
        "labels": [], "hypertargets": [], "references": [],
        "environments": [], "headings": [], "source_issues": [],
    }
    stack = []
    current_headings = {}
    position = begin
    while True:
        match = CONTROL.search(clean, position, end)
        if not match:
            break
        command = match[1]
        position = match.end()
        loc = location(newlines, match.start())
        if command in {"input", "include"}:
            raise ValueError(f"Unexpanded source inclusion at line {loc['line']}")
        if command in {"newcommand", "renewcommand", "providecommand", "DeclareRobustCommand"}:
            cursor = space(clean, position)
            if clean[cursor:cursor + 1] == "*":
                cursor = space(clean, cursor + 1)
            if clean[cursor:cursor + 1] == "{":
                _, cursor = group(clean, cursor)
            else:
                name = CONTROL.match(clean, cursor)
                if not name:
                    raise ValueError(f"Unparsed macro definition at line {loc['line']}")
                cursor = name.end()
            for _ in range(2):
                cursor = space(clean, cursor)
                if clean[cursor:cursor + 1] == "[":
                    _, cursor = group(clean, cursor, "[")
            _, position = group(clean, cursor)
            continue
        if command in {"def", "gdef", "edef", "xdef"}:
            cursor = clean.find("{", position, end)
            if cursor < 0:
                raise ValueError(f"Unparsed TeX definition at line {loc['line']}")
            _, position = group(clean, cursor)
            continue
        if command in {"section", "subsection", "subsubsection", "part"}:
            cursor = space(clean, position)
            starred = clean[cursor:cursor + 1] == "*"
            cursor = space(clean, cursor + int(starred))
            if clean[cursor:cursor + 1] == "[":
                _, cursor = group(clean, cursor, "[")
            title, heading_end = group(clean, cursor)
            record = dict(loc, command=command, starred=starred, title_tex=title, end_offset=heading_end)
            result["headings"].append(record)
            levels = ["part", "section", "subsection", "subsubsection"]
            level = levels.index(command)
            current_headings = {key: value for key, value in current_headings.items() if levels.index(key) < level}
            current_headings[command] = len(result["headings"]) - 1
            # Continue through the title: references printed in it also matter.
        if command in {"begin", "end", "[", "]"}:
            if command in {"[", "]"}:
                name, cursor = r"\[", position
                opening = command == "["
            else:
                name, cursor = group(clean, position)
                opening = command == "begin"
                position = cursor
            if opening:
                title = None
                title_end = space(clean, cursor)
                if clean[title_end:title_end + 1] == "[":
                    title, title_end = group(clean, title_end, "[")
                row = dict(loc, id=len(result["environments"]), name=name,
                           parent=stack[-1] if stack else None, title_tex=title,
                           header_end_offset=title_end, end_offset=None,
                           heading_context=dict(current_headings))
                result["environments"].append(row)
                stack.append(row["id"])
            else:
                if not stack or result["environments"][stack[-1]]["name"] != name:
                    raise ValueError(f"Mismatched environment end {name!r} at line {loc['line']}")
                row = result["environments"][stack.pop()]
                row["end_offset"] = cursor
                row["end_line"] = location(newlines, max(row["offset"], cursor - 1))["line"]
            continue
        if command not in REFERENCE | {"label", "hypertarget"}:
            continue
        cursor = space(clean, position)
        starred = clean[cursor:cursor + 1] == "*"
        cursor = space(clean, cursor + int(starred))
        option = None
        if clean[cursor:cursor + 1] == "[":
            option, cursor = group(clean, cursor, "[")
        argument_start = space(clean, cursor)
        argument, cursor = group(clean, cursor)
        arguments = [argument]
        source_arguments = [text[argument_start + 1:cursor - 1]]
        if command in RANGES:
            argument_start = space(clean, cursor)
            argument, cursor = group(clean, cursor)
            arguments.append(argument)
            source_arguments.append(text[argument_start + 1:cursor - 1])
        row = dict(loc, command=command, starred=starred, option_tex=option,
                   argument_tex=arguments, argument_source_tex=source_arguments, end_offset=cursor,
                   environment_path=list(stack), heading_context=dict(current_headings))
        if command == "label":
            row["key"] = arguments[0]
            result["labels"].append(row)
        elif command == "hypertarget":
            row["name"] = arguments[0]
            row["content_tex"], row["end_offset"] = group(clean, cursor)
            result["hypertargets"].append(row)
            # Its second argument is executed TeX, so continue through it.
        else:
            row["keys"] = [key for value in source_arguments
                           for key in literal_reference_tokens(value).split(",")]
            result["references"].append(row)
        position = cursor
    if stack:
        raise ValueError(f"Unclosed body environments: {stack}")
    envs = result["environments"]
    formal = [row for row in envs if row["name"] in declarations]
    formal_by_id = {row["id"]: row for row in formal}
    for row in formal:
        row["proof_environment_ids"] = []
    for proof in [row for row in envs if row["name"] == "proof"]:
        owner, association = None, None
        preceding = [row for row in formal if row["end_offset"] <= proof["offset"]
                     and row["parent"] == proof["parent"]]
        if preceding:
            candidate = max(preceding, key=lambda row: row["end_offset"])
            if not clean[candidate["end_offset"]:proof["offset"]].strip():
                owner, association = candidate["id"], "literal-adjacent-proof"
        if owner is None:
            owner = proof["parent"]
            while owner is not None and owner not in formal_by_id:
                owner = envs[owner]["parent"]
            association = "enclosing-formal-environment" if owner is not None else None
        proof["formal_owner_environment_id"] = owner
        proof["association"] = association
        if owner is not None:
            formal_by_id[owner]["proof_environment_ids"].append(proof["id"])
        else:
            result["source_issues"].append({"severity": "warning", "kind": "unassigned-proof",
                                           "line": proof["line"], "environment_id": proof["id"]})
    for row in result["labels"] + result["hypertargets"] + result["references"]:
        path = row["environment_path"]
        owner = None
        for index in reversed(path):
            if index in formal_by_id:
                owner = index
                break
            if envs[index]["name"] == "proof" and envs[index]["formal_owner_environment_id"] is not None:
                owner = envs[index]["formal_owner_environment_id"]
                break
        row["formal_owner_environment_id"] = owner
        row["display_environment_id"] = next((index for index in path if envs[index]["name"] in DISPLAY), None)
    for row in formal:
        row["identity_labels"] = [item["key"] for item in result["labels"]
                                  if item["formal_owner_environment_id"] == row["id"]
                                  and item["display_environment_id"] is None
                                  and row["offset"] <= item["offset"] < row["end_offset"]]
        row["literal_formal_targets"] = [item["name"] for item in result["hypertargets"]
                                         if item["formal_owner_environment_id"] == row["id"]
                                         and item["display_environment_id"] is None
                                         and row["offset"] <= item["offset"] < row["end_offset"]]
        row["primary_label"] = row["identity_labels"][0] if row["identity_labels"] else None
    # Only empty hypertarget commands and whitespace may separate a literal
    # adjacent alias pair. An AMS row break or any mathematical text stops it.
    adjacent = []
    for left, right in zip(result["labels"], result["labels"][1:]):
        if left["display_environment_id"] is None or left["display_environment_id"] != right["display_environment_id"]:
            continue
        gap = clean[left["end_offset"]:right["offset"]]
        gap = re.sub(r"\\hypertarget\{[^{}]+\}\{\}", "", gap)
        if not gap.strip():
            adjacent.append({"labels": [left["key"], right["key"]],
                             "source_lines": [left["line"], right["line"]]})
    result["adjacent_display_alias_pairs"] = adjacent
    result["formal_environments"] = [row["id"] for row in formal]
    return result


def parse_aux(text: str) -> list[dict]:
    clean = masked_tex(text)
    if re.search(r"(?m)^\\@input\s*\{", clean):
        raise ValueError("The final standalone aux contains a child aux; do not silently omit it")
    result = []
    for match in re.finditer(r"(?m)^\\newlabel\s*\{", clean):
        key, cursor = group(clean, match.end() - 1)
        payload, cursor = group(clean, cursor)
        fields = []
        position = 0
        while payload[position:].strip():
            value, position = group(payload, position)
            fields.append(value)
        row = {"key": key, "aux_line": clean.count("\n", 0, match.start()) + 1,
               "fields_tex": fields, "is_cref_auxiliary": key.endswith("@cref")}
        if not row["is_cref_auxiliary"]:
            if len(fields) < 4:
                raise ValueError(f"Final hyperref aux label {key!r} has fewer than four fields")
            row.update(number_tex=fields[0], page_tex=fields[1], title_tex=fields[2], anchor=fields[3])
        elif fields:
            kind = re.match(r"\[([^\]]+)\]", fields[0])
            row["cref_kind"] = kind[1] if kind else None
        result.append(row)
    if not result:
        raise ValueError("No actual newlabel records in the supplied final aux")
    return result


def read_pdf(path: Path, needed: set[str]) -> dict:
    from pypdf import PdfReader
    pdf = PdfReader(path)
    destinations = pdf.named_destinations
    counts = Counter()

    def read_names(node):
        node = node.get_object()
        names = node.get("/Names", [])
        for index in range(0, len(names), 2):
            counts[str(names[index])] += 1
        for child in node.get("/Kids", []):
            read_names(child)

    root = pdf.trailer["/Root"]
    names = root.get("/Names", {})
    names = names.get_object() if hasattr(names, "get_object") else names
    if "/Dests" in names:
        read_names(names["/Dests"])
    legacy = root.get("/Dests", {})
    legacy = legacy.get_object() if hasattr(legacy, "get_object") else legacy
    for name in legacy:
        counts[str(name).lstrip("/")] += 1
    page_labels = pdf.page_labels
    result = {"physical_pages": len(pdf.pages), "destinations": {}, "unresolved_internal_links": []}
    for name in sorted(needed):
        row = {"name": name, "pdf_name_occurrences": counts[name], "present": name in destinations}
        if name in destinations:
            destination = destinations[name]
            index = pdf.get_destination_page_number(destination)
            row.update(physical_page=index + 1 if index >= 0 else None,
                       pdf_page_label=page_labels[index] if index >= 0 else None,
                       view=str(destination.get("/Type", "")),
                       left=str(destination.get("/Left", "")),
                       top=str(destination.get("/Top", "")),
                       zoom=str(destination.get("/Zoom", "")))
        result["destinations"][name] = row
    for page_index, page in enumerate(pdf.pages, 1):
        for indirect in page.get("/Annots", []):
            annotation = indirect.get_object()
            action = annotation.get("/A", {})
            action = action.get_object() if hasattr(action, "get_object") else action
            target = action.get("/D") if action.get("/S") == "/GoTo" else annotation.get("/Dest")
            if isinstance(target, str) and str(target) not in destinations:
                result["unresolved_internal_links"].append({"physical_page": page_index, "target": str(target)})
    return result


def assemble(source: dict, auxiliary: list[dict], pdf: dict) -> dict:
    issues = list(source.pop("source_issues"))
    ordinary, clever = defaultdict(list), defaultdict(list)
    for row in auxiliary:
        (clever if row["is_cref_auxiliary"] else ordinary)[row["key"]].append(row)
    source_labels = Counter(row["key"] for row in source["labels"])
    source_targets = Counter(row["name"] for row in source["hypertargets"])

    def issue(kind, severity="error", **detail):
        issues.append(dict(severity=severity, kind=kind, **detail))

    for key, count in source_labels.items():
        if not literal(key):
            issue("nonliteral-label-key", key=key)
        if count != 1 or len(ordinary[key]) != count:
            issue("source-aux-label-multiplicity", key=key, source_occurrences=count,
                  aux_occurrences=len(ordinary[key]))
    for key, entries in ordinary.items():
        if len(entries) != 1:
            issue("nonunique-aux-key", key=key, occurrences=len(entries))
        if key not in source_labels:
            issue("aux-label-without-literal-source", severity="warning", key=key)
    for row in source["labels"]:
        key = row["key"]
        row["aux_records"] = ordinary[key]
        row["cleveref_aux_records"] = clever[key + "@cref"]
        for record in ordinary[key]:
            target = pdf["destinations"].get(record["anchor"], {})
            if not target.get("present"):
                issue("label-anchor-missing-from-pdf", key=key, anchor=record["anchor"])
            elif target["pdf_page_label"] != record["page_tex"]:
                issue("aux-page-and-target-page-differ", severity="warning", key=key,
                      aux_page=record["page_tex"], target_page=target["pdf_page_label"],
                      physical_page=target["physical_page"])
    for name, count in source_targets.items():
        target = pdf["destinations"].get(name, {})
        if not literal(name):
            issue("nonliteral-hypertarget-name", name=name)
        if not target.get("present") or target.get("pdf_name_occurrences") != count:
            issue("source-pdf-target-multiplicity", name=name, source_occurrences=count,
                  pdf_name_occurrences=target.get("pdf_name_occurrences", 0))
    for row in source["hypertargets"]:
        row["pdf_destination"] = pdf["destinations"].get(row["name"])
    aliases = defaultdict(list)
    for row in source["labels"]:
        key = row["key"]
        records = ordinary[key]
        if len(records) != 1:
            continue
        record = records[0]
        kinds = [entry.get("cref_kind") for entry in clever[key + "@cref"]]
        if "equation" in kinds or record["anchor"].startswith("equation."):
            aliases[(record["number_tex"], record["page_tex"], record["anchor"])].append(key)
    equation_groups = [{"number_tex": key[0], "page_tex": key[1], "anchor": key[2], "labels": labels}
                       for key, labels in aliases.items()]
    for pair in source["adjacent_display_alias_pairs"]:
        records = [ordinary[key] for key in pair["labels"]]
        equal = all(len(rows) == 1 for rows in records) and len({
            (rows[0]["number_tex"], rows[0]["page_tex"], rows[0]["anchor"]) for rows in records
        }) == 1
        pair["same_final_number_page_anchor"] = equal
        if not equal:
            issue("adjacent-display-alias-mismatch", **pair)
    for key, row in source["series_definitions"].items():
        if row.get("scope") == "local":
            label = row.get("local_label")
            row["local_aux_records"] = ordinary.get(label, [])
            if len(row["local_aux_records"]) != 1:
                issue("local-SeriesRef-label-unresolved", key=key, label=label)
            if not pdf["destinations"].get(row.get("target_tex"), {}).get("present"):
                issue("local-SeriesRef-target-unresolved", key=key, target=row.get("target_tex"))
        elif row.get("scope") != "external":
            issue("SeriesRef-definition-unparsed", key=key)
    for row in source["references"]:
        row["resolved"] = []
        for key in row["keys"]:
            if key != key.strip():
                issue("literal-reference-key-has-edge-spaces", key=key, line=row["line"],
                      candidate_for_review_only=key.strip())
            if row["command"] in {"SeriesRef", "SeriesRefText"}:
                record = source["series_definitions"].get(key)
                row["resolved"].append({"key": key, "series_definition": record})
                if record is None:
                    issue("SeriesRef-key-unresolved", key=key, line=row["line"])
            elif row["command"] == "hyperlink":
                target = pdf["destinations"].get(key)
                row["resolved"].append({"key": key, "pdf_destination": target})
                if not target or not target["present"]:
                    issue("hyperlink-target-unresolved", key=key, line=row["line"])
            else:
                records = ordinary.get(key, [])
                row["resolved"].append({"key": key, "aux_records": records})
                if len(records) != 1:
                    issue("local-reference-unresolved", key=key, line=row["line"])
    for env_id in source["formal_environments"]:
        row = source["environments"][env_id]
        row["identity_aux_records"] = {key: ordinary[key] for key in row["identity_labels"]}
        if len(row["proof_environment_ids"]) > 1:
            issue("multiple-syntactically-attached-proofs", severity="warning", environment_id=env_id,
                  primary_label=row["primary_label"], proof_environment_ids=row["proof_environment_ids"])
    for row in pdf["unresolved_internal_links"]:
        issue("pdf-internal-link-unresolved", **row)
    return {"schema": "Paper-III-final-source-aux-reference-data-v1", "paper": "III",
            "scope": "Extracted source/aux/PDF data; no mathematical, provenance, build or visual-reading certification",
            "source": source, "auxiliary_records": auxiliary, "equation_number_groups": equation_groups,
            "pdf": pdf, "issues": issues}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=ROOT / "S6_SERIES_PUBLISH_III.tex")
    parser.add_argument("--aux", type=Path, required=True)
    parser.add_argument("--pdf", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    source_text = args.source.read_text(encoding="utf-8")
    if r"\newcommand{\CurrentPaper}{III}" not in source_text:
        raise ValueError("The supplied source is not the standalone Paper III source")
    source = parse_source(source_text)
    auxiliary = parse_aux(args.aux.read_text(encoding="utf-8"))
    needed = {row["anchor"] for row in auxiliary if not row["is_cref_auxiliary"]}
    needed.update(row["name"] for row in source["hypertargets"])
    needed.update(key for row in source["references"] if row["command"] == "hyperlink" for key in row["keys"])
    needed.update(row["target_tex"] for row in source["series_definitions"].values() if row.get("scope") == "local")
    pdf = read_pdf(args.pdf, needed)
    output = assemble(source, auxiliary, pdf)
    output["inputs"] = {"source": str(args.source.resolve()), "aux": str(args.aux.resolve()), "pdf": str(args.pdf.resolve())}
    destination = args.output.resolve()
    if destination in {args.source.resolve(), args.aux.resolve(), args.pdf.resolve()}:
        raise ValueError("Output must not overwrite an input")
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", newline="\n", dir=destination.parent,
                                     prefix=destination.name + ".", suffix=".tmp", delete=False) as stream:
        temporary = Path(stream.name)
        json.dump(output, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    os.replace(temporary, destination)
    errors = sum(row["severity"] == "error" for row in output["issues"])
    warnings = sum(row["severity"] == "warning" for row in output["issues"])
    print(json.dumps({"paper": "III", "output": str(destination), "source_label_occurrences": len(source["labels"]),
                      "source_hypertarget_occurrences": len(source["hypertargets"]),
                      "formal_environments": len(source["formal_environments"]), "errors": errors, "warnings": warnings}))
    return 2 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
