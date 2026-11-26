#!/usr/bin/env python3
"""Admit observed current candidate10 and legacy candidate09 build results.

This is a distinct successor to the historical, fixed-value build recorder.
It does not run TeX, the two inspectors, the extractor, a count refresh, or
the derived-record generator. Both inspector stdout files and their empty
sibling stderr files must already exist for each selected completed run.

First run inspect with --current-t1-output, --legacy-t1-output,
--current-anchor-output, and --legacy-anchor-output. Read its complete
diagnostics and the retained compiler/inspection outputs. Apply requires
--reviewed, --source-sha256, and each of --{current,legacy}-pdf-sha256,
--{current,legacy}-aux-sha256, and --{current,legacy}-final-log-sha256.
Use the exact hashes printed by the inspected artifacts, not historical ones.

The driver records the source/PDF identities and reaches its completion
marker only after consecutive aux/toc/out bytes agree. It does not print
the aux hash. This program therefore requires the separately reviewed aux
identity and recomputes all seven alias pairs and every formal-owner
comparison against those exact bytes. It does not claim that an earlier
driver output contained an aux hash or that convergence was replayed here.

Only the Paper III build-progress row and T1's observed programmatic
recheck/evidence are eligible for writes. Historical T1 image evidence is
preserved and explicitly scoped to its earlier PDF. Changed-page images,
D14, provenance and the joint-series gates remain open; count and derived
records remain untouched and receive no credit from this program.
"""
from __future__ import annotations

import argparse
import ast
from collections import Counter, defaultdict
import csv
from datetime import date, datetime, timezone
import hashlib
from io import BytesIO, StringIO
import os
from pathlib import Path
import re
import tempfile

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
STEM = "S6_SERIES_PUBLISH_III"
SOURCE = ROOT / (STEM + ".tex")
BUILD_TABLE = ROOT / "S6_SERIES_PUBLISH_build_progress.tsv"
FINDINGS_TABLE = ROOT / "S6_SERIES_PUBLISH_findings_III.tsv"
RUNS = {"current": "candidate10", "legacy": "candidate09"}
# These are the reviewed programs whose exact output schemas are used below.
# A program change requires a new schema review, not automatic acceptance.
PROGRAM_HASHES = {
    "code/S6_SERIES_PUBLISH_c9_build_III.py":
        "97f38a8053ba4506b0956b74d0d5fa35def2c514fff4e623e605dab437d8fa39",
    "agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_T1_current_inspect.py":
        "fbf34170eb0cbf0aeff70b0707e661149ba242d49b6636ec54b50fb229ffce52",
    "agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_formal_anchor_check.py":
        "178f9a986291da3b6b0bf727bc6d32c72eede8a7696148d7d5b1f4a6239ee901",
}
PAIRS = (
    ("wb:h24:ret:eq:M", "maps:eq:B.3.2", "tag-01V0"),
    ("wb:h24:ret:eq:derivative-on-M", "maps:eq:B.3.3", "tag-01V1"),
    ("wb:h24:ret:eq:normal-u", "maps:eq:B.3.4", "tag-01V2"),
    ("maps:eq:D.OF1", "maps:eq:D.OL1", "tag-021Q"),
    ("maps:eq:D.OF11", "maps:eq:D.OL2", "tag-021U"),
    ("maps:eq:D.OF16", "maps:eq:D.OL12", "tag-021T"),
    ("maps:eq:D.OF18", "maps:eq:D.OL3", "tag-021V"),
)
FORMAL_KINDS = (
    "maintheorem", "definition", "remark", "proposition", "theorem",
    "lemma", "corollary", "computed", "problem",
)
T1_ISSUE = re.compile(
    r"undefined|multiply.defined|destination with the same identifier|"
    r"has been referenced but does not exist|Missing character|"
    r"Rerun to get|Rerun LaTeX|Label\(s\) may have changed|"
    r"Use of .*label@optarg|^!|LaTeX Font Warning", re.I)
FATAL = re.compile(
    r"^!|Fatal error|Emergency stop|No pages of output|"
    r"(?:LaTeX|Package|pdfTeX) Error|pdfTeX error|"
    r"not loadable|Font .* not found|font .*not found", re.I | re.M)
DIAG_HEADER = re.compile(
    r"Warning|Overfull \\[hv]box|Underfull \\[hv]box|^!|"
    r"Fatal error|Emergency stop", re.I)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def one(pattern, text, description):
    hits = re.findall(pattern, text, re.M)
    require(len(hits) == 1, f"{description}: expected one record; got {hits!r}")
    return hits[0]


def relative(path):
    path = Path(path).resolve()
    require(path.is_relative_to(ROOT), f"Evidence must be inside this checkpoint: {path}")
    return str(path.relative_to(ROOT))


class Snapshot:
    """Actual byte snapshots in memory only; no side manifest is written."""

    def __init__(self):
        self.data = {}

    def read(self, path):
        path = Path(path).resolve()
        raw = path.read_bytes()
        if path in self.data:
            require(raw == self.data[path], f"Input changed while reading: {path}")
        else:
            self.data[path] = raw
        return raw

    def text(self, path):
        return self.read(path).decode("utf-8")

    def unchanged(self, excluding=()):
        excluded = {Path(p).resolve() for p in excluding}
        for path, raw in self.data.items():
            if path not in excluded:
                require(path.read_bytes() == raw, f"Input changed during admission: {path}")


class RawTable:
    """Change one TSV record while preserving every other physical byte."""

    def __init__(self, path, snapshot):
        self.path = path
        self.raw = snapshot.read(path)
        require(b"\r" not in self.raw, f"Expected LF: {path}")
        text = self.raw.decode("utf-8")
        physical = text.splitlines(keepends=True)
        reader = csv.reader(StringIO(text, newline=""), delimiter="\t")
        self.fields = next(reader)
        self.header = "".join(physical[:reader.line_num])
        self.records = []
        previous = reader.line_num
        for values in reader:
            require(len(values) == len(self.fields), f"Malformed TSV row in {path}")
            raw = "".join(physical[previous:reader.line_num])
            self.records.append((dict(zip(self.fields, values)), raw))
            previous = reader.line_num
        require(previous == len(physical), f"Unparsed TSV bytes in {path}")

    @property
    def rows(self):
        return [row for row, _ in self.records]

    def selected(self, key, value):
        matches = [row for row, _ in self.records if row[key] == value]
        require(len(matches) == 1, f"{self.path}: {key}={value} is not unique")
        return matches[0]

    def replace(self, key, value, updates):
        old = self.selected(key, value)
        require(set(updates) <= set(self.fields), f"Unknown TSV fields: {updates.keys()}")
        new = dict(old, **updates)
        stream = StringIO(newline="")
        csv.writer(stream, delimiter="\t", lineterminator="\n").writerow(
            [new[name] for name in self.fields])
        replacement = stream.getvalue()
        result = self.header + "".join(
            replacement if row[key] == value else raw for row, raw in self.records)
        require("\r" not in result, f"Replacement introduced CR in {self.path}")
        return result.encode("utf-8")


def driver_diagnostics(log):
    """Match the reviewed driver's five reported diagnostic quantities."""
    lines = log.splitlines()
    widths = []
    for line in lines:
        found = re.search(r"Overfull \\[hv]box \(([\d.]+)pt too (?:wide|high)\)", line)
        if found:
            widths.append(float(found[1]))
    unresolved = [line for line in lines if re.search(
        r"(?:Reference|Citation).*undefined|There were undefined|Rerun to get|"
        r"Rerun LaTeX|Label\(s\) may have changed", line)]
    fonts = [line for line in lines if re.search(
        r"Missing character|LaTeX Font Warning|not loadable|"
        r"Font .* not found|font .*not found", line)]
    anchors = [line for line in lines if re.search(
        r"destination with the same identifier|has been referenced but does not exist", line)]
    return (len(widths), sum(width > 2 for width in widths), len(unresolved),
            len(fonts), len(anchors)), widths


def diagnostic_blocks(log):
    """Return every final warning/box diagnostic, through its blank terminator."""
    lines = log.splitlines()
    blocks = []
    index = 0
    while index < len(lines):
        if not DIAG_HEADER.search(lines[index]):
            index += 1
            continue
        end = index + 1
        while end < len(lines) and lines[end].strip() and not DIAG_HEADER.search(lines[end]):
            end += 1
        blocks.append((index + 1, "\n".join(lines[index:end])))
        index = end
    return blocks


def groups(text):
    depth, start, result = 0, None, []
    for index, char in enumerate(text):
        if char == "{":
            if depth == 0:
                start = index + 1
            depth += 1
        elif char == "}":
            depth -= 1
            require(depth >= 0, "Unbalanced aux record")
            if depth == 0:
                result.append(text[start:index])
    require(depth == 0, "Unbalanced aux record")
    return result


def ordinary_fields(value):
    outer = groups(value)
    require(len(outer) == 1, f"Unexpected ordinary aux record: {value}")
    fields = groups(outer[0])
    require(len(fields) == 5, f"Expected all five ordinary aux fields: {value}")
    return fields


def read_inspection(path, snapshot):
    path = Path(path).resolve()
    relative(path)
    require(path.suffix == ".out", f"Expected the actual inspector stdout .out: {path}")
    output = snapshot.text(path)
    error_path = path.with_suffix(".err")
    require(snapshot.read(error_path) == b"", f"Inspector stderr is not empty: {error_path}")
    require("Traceback (most recent call last)" not in output, f"Failed inspector: {path}")
    return path, output


def read_build(kernel, source_hash, snapshot):
    run = RUNS[kernel]
    work = ROOT / "agents/continuation9_build_III" / kernel
    driver_path = ROOT / "code" / f"S6_SERIES_PUBLISH_c9_build_III_{kernel}_{run}.out"
    driver = snapshot.text(driver_path)
    require(snapshot.read(driver_path.with_suffix(".err")) == b"",
            f"Build driver stderr is not empty: {driver_path}")
    start = one(r"^UTC start (.+)$", driver, "build start")
    complete = one(r"^UTC complete (.+)$", driver, "completed build")
    require(datetime.fromisoformat(complete) >= datetime.fromisoformat(start),
            "Build completion precedes its start")
    require(driver.rstrip().endswith("No visual-page-reading credit follows from this build."),
            f"Missing final driver footer: {driver_path}")
    recorded_source, recorded_kernel = one(
        r"^Source SHA-256 ([0-9a-f]{64}) kernel (current|legacy)$", driver, "source identity")
    require((recorded_source, recorded_kernel) == (source_hash, kernel),
            f"Completed driver does not match the exact live source/kernel: {driver_path}")
    recorded_pdf, pdf_hash = one(
        r"^PDF (.+) SHA-256 ([0-9a-f]{64})$", driver, "completed PDF identity")
    pdf_path = work / (STEM + ".pdf")
    aux_path = work / (STEM + ".aux")
    require(Path(recorded_pdf).resolve() == pdf_path.resolve(), "Recorded PDF path differs")
    pdf_bytes, aux_bytes = snapshot.read(pdf_path), snapshot.read(aux_path)
    require(digest(pdf_bytes) == pdf_hash, f"Completed PDF hash differs: {pdf_path}")
    require(aux_bytes, f"Empty final aux: {aux_path}")
    # Snapshot the remaining convergence inputs without claiming earlier states
    # are available. Their earlier byte equality is the driver's observation.
    for suffix in (".toc", ".out"):
        require(snapshot.read(work / (STEM + suffix)), f"Empty final state {suffix}: {work}")

    passes = re.findall(r"^Pass (\d+) exit (-?\d+)$", driver, re.M)
    require(2 <= len(passes) <= 6, f"No reviewed convergence sequence: {passes}")
    require(passes == [(str(n), "0") for n in range(1, len(passes) + 1)],
            f"Nonconsecutive or failed compiler pass: {passes}")
    summaries = re.findall(
        r"^Pass (\d+) exit (-?\d+)\nDiagnostics: overfull (\d+) >2pt (\d+) "
        r"unresolved/rerun (\d+) fonts (\d+) anchors (\d+)$", driver, re.M)
    require(len(summaries) == len(passes), "Incomplete per-pass diagnostic summaries")
    logs = []
    for number, code, *reported in summaries:
        require((number, code) == passes[len(logs)], "Driver summary order differs")
        prefix = ROOT / "code" / f"S6_SERIES_PUBLISH_c9_III_{kernel}_{run}_pass{int(number):02}"
        raw_log = snapshot.read(prefix.with_suffix(".log"))
        stdout = snapshot.read(prefix.with_suffix(".out"))
        require(snapshot.read(prefix.with_suffix(".err")) == b"",
                f"Compiler stderr is not empty: {prefix}")
        log = raw_log.decode("utf-8", errors="replace")
        require("Output written on " in log and b"Output written on " in stdout,
                f"No actual compiler output completion: {prefix}")
        require(not FATAL.search(log), f"Fatal compiler diagnostic: {prefix}")
        quantities, widths = driver_diagnostics(log)
        require(quantities == tuple(map(int, reported)),
                f"Driver diagnostics differ from the full raw log: {prefix}")
        issues = sum(bool(T1_ISSUE.search(line)) for line in log.splitlines())
        logs.append(dict(path=prefix.with_suffix(".log"), raw=raw_log, text=log,
                         quantities=quantities, widths=widths, issues=issues))
        print(kernel, run, "pass", number, "diagnostics", quantities,
              "T1 relevant matches", issues, "log SHA-256", digest(raw_log))

    final = logs[-1]
    require(final["raw"] == snapshot.read(work / (STEM + ".log")),
            "Live final log differs from the exact selected completed pass")
    require(final["quantities"][1:] == (0, 0, 0, 0) and final["issues"] == 0,
            f"Final >2pt / unresolved / font / anchor / T1 gate failed: {final['quantities']}")
    kernel_records = re.findall(r"^(LaTeX2e <(\d{4}-\d{2}-\d{2})>.*)$",
                                final["text"], re.M)
    require(kernel_records and all(row == kernel_records[0] for row in kernel_records),
            f"Missing or inconsistent actual kernel records: {kernel_records!r}")
    kernel_line = kernel_records[0]
    actual_date = date.fromisoformat(kernel_line[1])
    require(actual_date >= date(2025, 11, 1) if kernel == "current"
            else actual_date == date(2024, 11, 1), f"Unexpected actual kernel: {kernel_line[0]}")
    blocks = diagnostic_blocks(final["text"])
    print(kernel, run, "actual kernel:", kernel_line[0])
    print(kernel, run, "identical actual kernel banner occurrences:", len(kernel_records))
    print(kernel, run, "all final warning/box diagnostic blocks:", len(blocks))
    for line_number, block in blocks:
        print(f"FINAL DIAGNOSTIC {relative(final['path'])}:{line_number}\n{block}\n")
    pages = int(one(r"^Pages:\s+(\d+)$", driver, "driver pdfinfo page count"))
    size = int(one(r"^File size:\s+(\d+) bytes$", driver, "driver pdfinfo byte count"))
    require(size == len(pdf_bytes), "pdfinfo byte size does not match the admitted PDF")
    output_records = re.findall(
        r"Output written on\s+(.*?)\s+\((\d+) pages?, (\d+) bytes\)\.",
        final["text"], re.S)
    require(len(output_records) == 1, "Missing unique final TeX output page/byte count")
    require((int(output_records[0][1]), int(output_records[0][2])) == (pages, size),
            "Final TeX and pdfinfo page/byte counts differ")
    font_table = one(
        r"(?s)^name\s+type\s+encoding\s+emb sub uni object ID\n-+\s+-+\s+-+\s+"
        r"-+\s+-+\s+-+\s+-+\n(.*?)\n\nPDF ", driver, "complete pdffonts table")
    font_rows = [line.split() for line in font_table.splitlines() if line.strip()]
    require(font_rows and all(len(row) >= 8 and row[-5] == "yes" for row in font_rows),
            "The completed pdffonts report contains an unembedded or malformed font row")
    return dict(kernel=kernel, run=run, work=work, driver_path=driver_path, driver=driver,
                complete=complete, passes=passes, logs=logs, final=final, pages=pages,
                pdf_path=pdf_path, pdf_bytes=pdf_bytes, pdf_hash=pdf_hash,
                aux_path=aux_path, aux_bytes=aux_bytes, aux_hash=digest(aux_bytes),
                log_hash=digest(final["raw"]), kernel_line=kernel_line[0],
                fonts=len(font_rows), warnings=sum("Warning" in b for _, b in blocks),
                underfull=sum(b.startswith("Underfull ") for _, b in blocks))


def inspect_artifacts(build, source, source_hash, t1_path, owner_path, snapshot):
    t1_path, t1 = read_inspection(t1_path, snapshot)
    owner_path, owner_output = read_inspection(owner_path, snapshot)
    kernel, run = build["kernel"], build["run"]
    require(one(r"^Completed (current|legacy) ([a-z0-9_]+) passes: (.+)$",
                t1, "T1 selected run") == (kernel, run, repr(build["passes"])),
            "T1 output is for a different run/pass sequence")
    require(Path(one(r"^Selected driver: (.+)$", t1, "T1 driver")).resolve()
            == build["driver_path"].resolve(), "T1 selected driver path differs")
    require(one(r"^Matched live source SHA-256: ([0-9a-f]{64})$", t1, "T1 source")
            == source_hash, "T1 output is for a different source")
    require(one(r"^Matched live PDF SHA-256: ([0-9a-f]{64})$", t1, "T1 PDF")
            == build["pdf_hash"], "T1 output is for a different PDF")
    require(t1.rstrip().endswith("T1 remains for root admission; no source change or visual-page credit."),
            "T1 inspector did not complete")
    for log in build["logs"]:
        expected = f"{log['path'].name} full-log relevant matches: {log['issues']}"
        require(t1.splitlines().count(expected) == 1, f"T1 raw-log report differs: {expected}")
    expected_engine = Counter("Final engine/package: " + line
        for line in build["final"]["text"].splitlines()
        if re.search(r"LaTeX2e <|Package: (amsmath|hyperref|cleveref) ", line))
    reported_engine = Counter(line for line in t1.splitlines()
                              if line.startswith("Final engine/package: "))
    require(reported_engine == expected_engine,
            "T1 engine/package report or multiplicity differs from the selected final log")

    records = defaultdict(list)
    for key, value in re.findall(
            r"^\\newlabel\{([^{}]+)\}(.*)$", build["aux_bytes"].decode("utf-8"), re.M):
        records[key].append(value)
    pdf = PdfReader(BytesIO(build["pdf_bytes"]))
    require(len(pdf.pages) == build["pages"], "Actual PDF page count differs")
    raw_names = []

    def walk_names(node):
        node = node.get_object()
        entries = node.get("/Names", [])
        require(len(entries) % 2 == 0, "Malformed PDF destination name tree")
        raw_names.extend(str(entries[i]) for i in range(0, len(entries), 2))
        for child in node.get("/Kids", []):
            walk_names(child)

    pdf_root = pdf.trailer["/Root"]
    names = pdf_root.get("/Names")
    if names is not None and "/Dests" in names.get_object():
        walk_names(names.get_object()["/Dests"])
    old_names = pdf_root.get("/Dests")
    if old_names is not None:
        raw_names.extend(str(key) for key in old_names.get_object())
    counts = Counter(raw_names)
    require(raw_names and all(number == 1 for number in counts.values()),
            "Duplicate or absent PDF named destinations")
    destinations = pdf.named_destinations
    require(set(raw_names) == set(destinations), "Raw destination tree differs from parsed mapping")

    def destination_page(name):
        require(name in destinations, f"Missing PDF destination: {name}")
        page = pdf.get_destination_page_number(destinations[name])
        require(0 <= page < len(pdf.pages), f"Invalid PDF destination page: {name}")
        return page + 1

    for name in destinations:
        destination_page(name)
    targets, direct = Counter(), 0
    for page in pdf.pages:
        for indirect in page.get("/Annots", []):
            annotation = indirect.get_object()
            target = None
            action = annotation.get("/A")
            if action is not None and action.get_object().get("/S") == "/GoTo":
                target = action.get_object().get("/D")
            if target is None and "/Dest" in annotation:
                target = annotation["/Dest"]
            if isinstance(target, str):
                targets[str(target)] += 1
            elif target is not None:
                direct += 1
    require(set(targets) <= set(destinations), "An internal named link has no destination")
    reported_pairs = re.findall(r"^PAIR (.+) = (.+)$", t1, re.M)
    require(reported_pairs == [(a, b) for a, b, _ in PAIRS], "T1 pair set/order differs")
    anchors, pair_pages = [], []
    for primary, alias, tag in PAIRS:
        keys = (primary, alias, primary + "@cref", alias + "@cref")
        require(all(len(records[key]) == 1 for key in keys),
                f"Ordinary/@cref multiplicity differs: {keys}")
        require(records[primary] == records[alias]
                and records[primary + "@cref"] == records[alias + "@cref"],
                f"Complete alias records differ: {primary}, {alias}")
        anchor = ordinary_fields(records[primary][0])[3]
        anchors.append(anchor)
        page = destination_page(anchor)
        require(counts[anchor] == counts[tag] == 1 and destination_page(tag) == page,
                f"Alias anchor/tag multiplicity or page differs: {anchor}, {tag}")
        pair_pages.append(page)
        block = (
            f"PAIR {primary} = {alias}\nordinary record: {records[primary][0]}\n"
            f"cref record: {records[primary + '@cref'][0]}\n"
            f"unique anchor {anchor} physical page {page} ordinary/alias shared target links "
            f"{targets[anchor]} unique permanent tag {tag} tag links {targets[tag]}")
        require(t1.count(block) == 1, f"T1 output does not match actual aux/PDF data: {primary}")
    require(len(set(anchors)) == len(PAIRS), "The seven equation anchors are not distinct")
    expected_summary = [
        f"PDF physical pages: {len(pdf.pages)}",
        f"Raw named destinations: {len(raw_names)} duplicate names: 0",
        f"Internal named links: {sum(targets.values())} distinct targets: {len(targets)} "
        f"missing targets: 0 direct destination links: {direct}",
        "PASS: all 28 ordinary/cref records occur once; seven pairs match exactly;",
        "all seven distinct shared anchors and their permanent tags occur once and resolve.",
    ]
    require(all(t1.splitlines().count(line) == 1 for line in expected_summary),
            "T1 summary differs from the actual artifact comparison")

    require(one(r"^Selected completed build: (current|legacy) ([a-z0-9_]+)$",
                owner_output, "owner inspector run") == (kernel, run),
            "Formal-owner inspector selected a different run")
    require(owner_output.rstrip().endswith(
        "This is a destination comparison; it does not assign visual reading credit."),
        "Formal-owner inspector did not complete")
    opening = re.compile(r"\\begin\{(" + "|".join(FORMAL_KINDS) + r")\}")
    owners = list(opening.finditer(source))
    require(owners, "No formal source owners")
    seen, exceptions = set(), []
    for match in owners:
        kind = match[1]
        end = source.index("\\end{" + kind + "}", match.end())
        block = source[match.start():end]
        label = re.search(r"\\label\{([^{}]+)\}", block)
        require(label is not None and label[1] not in seen, "Missing/duplicate formal owner")
        key = label[1]
        seen.add(key)
        require(len(records[key]) == 1, f"Formal owner aux occurrence differs: {key}")
        _, printed, _, anchor, _ = ordinary_fields(records[key][0])
        tag_match = re.search(r"\\hypertarget\{(tag-[^{}]+)\}", block)
        tag = tag_match[1] if tag_match else None
        anchor_page = destination_page(anchor)
        tag_page = destination_page(tag) if tag in destinations else None
        if int(printed) != anchor_page or (tag is not None and tag_page != anchor_page):
            exceptions.append((key, int(printed), anchor_page, tag_page))
    owner_count = int(one(r"^Completed read-only comparison: (\d+) formal owners\.$",
                          owner_output, "formal-owner count"))
    require(owner_count == len(owners), "Formal-owner inspector count differs from source")
    reported_kinds = ast.literal_eval(one(r"^Formal kinds: (.+)$", owner_output, "formal kinds"))
    require(reported_kinds == dict(Counter(match[1] for match in owners)),
            "Formal-owner kind counts differ from source")
    reported_count = int(one(
        r"^Owners with aux/anchor or tag/anchor page differences: (\d+)$",
        owner_output, "formal-owner exception count"))
    reported_exceptions = [
        (key, int(printed), int(anchor), None if tag == "None" else int(tag))
        for key, printed, anchor, tag in re.findall(
            r"^EXCEPTION (\S+) (\d+) (\d+) (None|\d+)$", owner_output, re.M)]
    require(len(re.findall(r"^EXCEPTION.*$", owner_output, re.M)) == len(reported_exceptions),
            "An inspector exception line was not parsed completely")
    require(reported_count == len(exceptions) and reported_exceptions == exceptions,
            f"Formal-owner exception content differs: reported={reported_exceptions}; actual={exceptions}")
    print(kernel, run, "formal-owner exceptions:", exceptions)
    require(not exceptions, "Actual anchor exceptions require source/image disposition; no admission")
    print(kernel, run, "T1 pair pages:", pair_pages, "formal owners:", len(owners),
          "raw destinations:", len(raw_names), "internal named links:", sum(targets.values()),
          "direct-destination links (count only):", direct)
    build.update(t1_path=t1_path, anchor_path=owner_path, owners=len(owners),
                 named_links=sum(targets.values()), destinations=len(raw_names),
                 pair_pages=pair_pages, direct_links=direct)


def add_evidence(existing, paths):
    values = [item.strip() for item in existing.split(";") if item.strip()]
    for path in paths:
        value = relative(path)
        if value not in values:
            values.append(value)
    return "; ".join(values)


def write_updates(updates, snapshot):
    """Stage only the two admitted row replacements; remove all temporary files."""
    require(set(updates) == {BUILD_TABLE, FINDINGS_TABLE}, "Unexpected output path")
    staged = {}
    committed = []
    try:
        for path, raw in updates.items():
            with tempfile.NamedTemporaryFile(dir=path.parent, prefix=path.name + ".",
                                             suffix=".tmp", delete=False) as stream:
                stream.write(raw)
                stream.flush()
                os.fsync(stream.fileno())
                staged[path] = Path(stream.name)
        snapshot.unchanged()
        for path, temporary in staged.items():
            os.replace(temporary, path)
            committed.append(path)
        for path, raw in updates.items():
            require(path.read_bytes() == raw, f"Written record differs: {path}")
        snapshot.unchanged(excluding=updates)
    except Exception:
        # Restore only this program's just-written rows after a local write
        # failure. No compiler, source, derived record or separate receipt exists.
        for path in reversed(committed):
            path.write_bytes(snapshot.data[path.resolve()])
        raise
    finally:
        for temporary in staged.values():
            temporary.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("inspect", "apply"))
    parser.add_argument("--reviewed", action="store_true",
                        help="Root has read the complete actual outputs and this exact program.")
    parser.add_argument("--source-sha256")
    for kernel in RUNS:
        parser.add_argument(f"--{kernel}-t1-output", required=True, type=Path)
        parser.add_argument(f"--{kernel}-anchor-output", required=True, type=Path)
        for field in ("pdf", "aux", "final-log"):
            parser.add_argument(f"--{kernel}-{field}-sha256")
    args = parser.parse_args()
    if args.mode == "apply":
        require(args.reviewed, "Apply requires root's completed output/program review")
    expected = {"source_sha256": args.source_sha256}
    expected.update({f"{k}_{f}_sha256": getattr(args, f"{k}_{f}_sha256")
                     for k in RUNS for f in ("pdf", "aux", "final_log")})
    for name, value in expected.items():
        require(value is not None or args.mode == "inspect", f"Apply requires --{name.replace('_', '-')}")
        require(value is None or re.fullmatch(r"[0-9a-f]{64}", value),
                f"Use the actual lowercase SHA-256 for {name}")

    csv.field_size_limit(100000000)
    snapshot = Snapshot()
    for name, expected_hash in PROGRAM_HASHES.items():
        require(digest(snapshot.read(ROOT / name)) == expected_hash,
                f"Reviewed driver/inspector schema changed: {name}")
    source_bytes = snapshot.read(SOURCE)
    require(b"\r" not in source_bytes, "Expected LF source")
    source, source_hash = source_bytes.decode("utf-8"), digest(source_bytes)
    if args.source_sha256:
        require(args.source_sha256 == source_hash, "Root-reviewed source identity differs")
    findings = RawTable(FINDINGS_TABLE, snapshot)
    build_table = RawTable(BUILD_TABLE, snapshot)
    require(all(row["status"] == "done" for row in findings.rows if row["id"] not in ("P4", "T1")),
            "Source findings must be settled before repaired-build admission")
    t1_row = findings.selected("id", "T1")
    require(t1_row["status"] == "done",
            "This program preserves the prior T1 disposition; it does not replace an open image review")
    build_table.selected("paper", "III")
    # Protect the other canonical tables/readings in memory. This does not
    # calculate, copy or refresh their derived content.
    protected = set(ROOT.glob("S6_SERIES_PUBLISH_*.tsv"))
    protected.update([
        ROOT / "CHECK_EVENTS.tsv", ROOT / "S6_SERIES_PUBLISH_reading_III.md",
        ROOT / "records/S6_SERIES_PUBLISH_III_current_check_counts.json",
    ])
    for path in sorted(protected - {BUILD_TABLE, FINDINGS_TABLE}):
        if path.exists():
            snapshot.read(path)
    builds = {}
    for kernel in RUNS:
        build = read_build(kernel, source_hash, snapshot)
        inspect_artifacts(build, source, source_hash,
                          getattr(args, f"{kernel}_t1_output"),
                          getattr(args, f"{kernel}_anchor_output"), snapshot)
        for field, actual in (("pdf", build["pdf_hash"]), ("aux", build["aux_hash"]),
                              ("final_log", build["log_hash"])):
            supplied = getattr(args, f"{kernel}_{field}_sha256")
            if supplied is not None:
                require(supplied == actual, f"Root-reviewed {kernel} {field} identity differs")
            print("REVIEW IDENTITY", f"--{kernel}-{field.replace('_', '-')}-sha256", actual)
        builds[kernel] = build
    print("REVIEW IDENTITY --source-sha256", source_hash)
    print("Convergence evidence: the exact reviewed driver completed after observed consecutive"
          " aux/toc/out equality in each run; this program did not rerun TeX.")

    current, legacy = builds["current"], builds["legacy"]
    evidence = [Path(__file__).resolve(), ROOT / "code/S6_SERIES_PUBLISH_c9_build_III.py"]
    for build in builds.values():
        evidence.extend([build["driver_path"], build["final"]["path"],
                         build["t1_path"], build["anchor_path"]])
    detail_parts = []
    for build in builds.values():
        detail_parts.append(
            f"{build['kernel']} {build['run']}: {build['kernel_line']}; "
            f"{len(build['passes'])} successful passes with driver-observed convergence; "
            f"{build['pages']} actual physical pages; PDF SHA-256 {build['pdf_hash']}; "
            f"aux SHA-256 {build['aux_hash']}; final log SHA-256 {build['log_hash']}; "
            f"{len(build['final']['widths'])} overfull boxes with actual widths "
            f"{build['final']['widths']}pt, none above2pt; "
            f"{build['underfull']} underfull and {build['warnings']} warning diagnostic blocks "
            f"retained for review; {build['fonts']} embedded-font rows. "
            f"Final unresolved/rerun, missing-font, duplicate/missing-destination and T1-error "
            f"counts are zero. All28 alias records occur once and all7 pairs agree completely; "
            f"{build['named_links']} internal named links resolve; "
            f"{build['owners']} source formal owners have zero actual aux/anchor/tag page exceptions.")
    gates = (
        "This records observed compiler, T1-record and destination comparisons only. "
        "Actual changed-page image reading, D14 layout, provenance/deposit "
        "and five-paper gates remain open. Count and derived records are untouched. "
        "No new mathematical-check or image-reading credit is assigned.")
    marker = f"Programmatic rebuild admission: current {RUNS['current']} and legacy {RUNS['legacy']}; source SHA-256 {source_hash}."
    require(marker not in t1_row["source_resolution"], "This exact repaired-build pair is already admitted")
    stamp = datetime.now(timezone.utc).isoformat()
    updated_build = build_table.replace("paper", "III", dict(
        status="done", date_utc=stamp, source_file=SOURCE.name,
        pdf_file=relative(current["pdf_path"]), pdf_sha256=current["pdf_hash"],
        log_files="; ".join(relative(b["final"]["path"]) for b in builds.values()),
        evidence=add_evidence("", evidence), detail=" ".join([marker, *detail_parts, gates])))
    updated_t1 = findings.replace("id", "T1", dict(
        date_utc=stamp,
        source_resolution=t1_row["source_resolution"] + " " + marker + " " +
            " ".join(detail_parts) + " The earlier image evidence above remains tied to its earlier PDF.",
        remaining_gate=gates,
        evidence=add_evidence(t1_row["evidence"], evidence)))
    snapshot.unchanged()
    if args.mode == "inspect":
        print("INSPECT ONLY: two exact canonical row replacements are ready for review; no file changed.")
        print("Build row detail:", " ".join([marker, *detail_parts, gates]))
        print("T1 retains its historical status and image evidence; fresh programmatic results append only.")
        return
    write_updates({BUILD_TABLE: updated_build, FINDINGS_TABLE: updated_t1}, snapshot)
    print("Admitted the Paper III build row and appended the observed T1/anchor recheck.")
    print("All protected canonical records remain byte-identical. Final image/D14/provenance gates remain open.")


if __name__ == "__main__":
    main()
