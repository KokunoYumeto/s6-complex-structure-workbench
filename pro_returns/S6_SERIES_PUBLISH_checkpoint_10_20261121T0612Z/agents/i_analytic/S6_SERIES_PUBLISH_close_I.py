#!/usr/bin/env python3
"""Read-only Paper I closure validator; optionally stage guarded updates for root.

All inputs are read without mutation. Outputs are confined to this agent folder.
No proof/check event is created. Human/agent review attestations remain explicitly
attributed to their hashed receipts: this program checks bindings, not proofs.
"""
from __future__ import annotations
import argparse
from collections import Counter
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

csv.field_size_limit(100_000_000)
HERE = Path(__file__).resolve().parent
TYPES = ["targeted proof check", "independent re-proof", "computation or formal certificate",
         "used and rechecked in this run", "carried as background without fault found",
         "refuted, with the refined statement's id"]
ORIGINAL_REQUIRED = {
    "mapsI:src:A.1.1", "mapsI:src:A.1.2", "mapsI:src:A.2.1", "night:P2.3", "night:P2.11",
    "push:src:D.1.3", "push:src:D.2.3", "push:src:D.3.2", "ari:C.6.4", "ari:C.8.9",
    "ari:C.8.10", "push:src:B.4.1", "push:src:B.5.1", "push:src:A.1.1", "push:src:A.1.2",
    "push:src:A.2.1", "push:src:A.2.2", "inv:B1.0", "night:P5.7"}
ENV = re.compile(r"\\begin\{(maintheorem|theorem|lemma|proposition|corollary|definition|remark|cited)\}")

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def invert_editorial_guards(current_block: str, prior_block: str, guards) -> str:
    """Reconstruct the complete old block by exact, unique inverse replacements.

    This verifies the archived coordinate/text map only.  The separate hashed
    comparison receipt attests to the exposed full-proof reading; neither
    operation supplies independent mathematical credit.
    """
    if not isinstance(current_block, str) or not isinstance(prior_block, str) or not current_block or not prior_block:
        raise ValueError("Both complete archived blocks must be nonempty strings")
    if not isinstance(guards, list) or not guards:
        raise ValueError("A nonempty ordered inverse-guard list is required")
    restored = current_block
    for index, guard in enumerate(guards, 1):
        if not isinstance(guard, dict):
            raise ValueError(f"Inverse guard {index} must be an object")
        old, new = guard.get("old"), guard.get("new")
        if not isinstance(old, str) or not old or not isinstance(new, str) or old == new:
            raise ValueError(f"Inverse guard {index} needs distinct literal strings and a nonempty old string")
        if guard.get("expected_occurrences") != 1 or restored.count(old) != 1:
            raise ValueError(f"Inverse guard {index} must match exactly once at its sequential application")
        restored = restored.replace(old, new, 1)
    if restored != prior_block:
        raise ValueError("Inverse guards do not reconstruct the complete archived prior block exactly")
    return restored

def walk_rows(obj):
    if isinstance(obj, dict):
        if {"page", "image_sha256", "pdf_sha256"} <= obj.keys():
            yield obj
        for value in obj.values():
            yield from walk_rows(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from walk_rows(value)

class Validator:
    def __init__(self, args):
        self.args, self.w = args, args.work_root.resolve()
        self.errors, self.passed, self.inputs = [], [], {}
        self.facts, self.cache = {}, {}
        self.tex, self.source_hash, self.ledger_hash, self.pdf_hash = "", "", "", ""
        self.pages = 0

    def path(self, name):
        p = Path(name)
        return p if p.is_absolute() else self.w / p

    def check(self, condition, code, detail):
        (self.passed if condition else self.errors).append({"code": code, "detail": detail})
        return bool(condition)

    def exists(self, name):
        p = self.path(name)
        if not self.check(p.is_file(), "file", str(p)):
            return None
        h = sha(p)
        self.inputs[str(p)] = h
        return p

    def read(self, name, default=None):
        p = self.exists(name)
        if p is None:
            return default
        try:
            if str(p) not in self.cache:
                self.cache[str(p)] = json.loads(p.read_text())
            return self.cache[str(p)]
        except (ValueError, OSError) as exc:
            self.check(False, "json", f"{p}: {exc}")
            return default

    def rows(self, name, delimiter="\t"):
        p = self.exists(name)
        if p is None:
            return []
        with p.open(newline="") as f:
            return list(csv.DictReader(f, delimiter=delimiter))

    def bound(self, obj, label, required=True):
        if not isinstance(obj, dict) or not obj.get("path") or not obj.get("sha256"):
            if required:
                self.check(False, "bound-file", label + ": path/SHA binding missing")
            return None
        p = self.exists(obj["path"])
        if p:
            self.check(sha(p) == obj["sha256"], "bound-file", label + ": exact file hash")
        return p

    def source_binding(self, obj, key="source_sha256", label="receipt"):
        self.check(isinstance(obj, dict) and obj.get(key) == self.source_hash,
                   "source-binding", label + ": current source hash")

    def basic(self):
        p = self.exists("S6_SERIES_PUBLISH_I.tex")
        if p:
            self.tex, self.source_hash = p.read_text(), sha(p)
        ledger = self.exists("CHECK_EVENTS.tsv")
        if ledger:
            self.ledger_hash = sha(ledger)
        copy = self.exists("records/CHECK_EVENTS.tsv")
        if copy:
            self.check(sha(copy) == self.ledger_hash, "ledger", "Root and records ledger bytes agree")
        original = self.exists(self.w.parent / "source/S6_SERIES_GRIND_I.tex")
        if original:
            old = original.read_text()
            identities = {}
            for name, regex, expected in [
                ("labels", r"\\label\{([^}]+)\}", 676),
                ("permanent_tag_targets", r"\\hypertarget\{(tag-[^}]+)\}", 520)]:
                before, after = set(re.findall(regex, old)), set(re.findall(regex, self.tex))
                self.check(len(before) == expected, "original-identities", f"{name}: original baseline {expected}")
                self.check(not before - after, "identity-preservation", f"{name}: lost {sorted(before-after)}")
                identities[name] = {"original": len(before), "current": len(after), "lost": sorted(before-after)}
            self.facts["identities"] = identities

    def rendered(self):
        final = self.read("records/S6_SERIES_PUBLISH_I_final_pdf_receipt.json", {})
        coverage = self.read("records/S6_SERIES_PUBLISH_I_page_coverage.json", {})
        # A candidate manifest supports diagnostics only; it never substitutes for a final receipt.
        manifest_name = self.args.manifest
        if not manifest_name and final.get("render_manifest_sha256"):
            matches = [p for p in (self.w / "render").glob("I_*/manifest.json")
                       if sha(p) == final["render_manifest_sha256"]]
            if len(matches) == 1:
                manifest_name = str(matches[0])
        if not self.check(bool(manifest_name), "render-manifest", "Exact final render manifest identified"):
            return
        mp = self.path(manifest_name)
        manifest = self.read(mp, {})
        self.pages = manifest.get("pages", 0)
        self.pdf_hash = manifest.get("pdf_sha256", "")
        self.check(isinstance(self.pages, int) and self.pages > 0, "page-count", "Positive exact page count")
        pdf = self.exists(manifest.get("pdf", "MISSING_PDF"))
        if pdf:
            self.check(sha(pdf) == self.pdf_hash, "pdf", "Render manifest identifies the exact PDF")
            build = self.read(pdf.parent / "build_summary.json", {})
            self.source_binding(build, label="build summary")
            self.check(build.get("pdf_sha256") == self.pdf_hash, "build", "Build/PDF hashes agree")
            for field in ["overfull_total", "overfull_above_2pt", "undefined_references", "undefined_citations",
                          "missing_characters", "missing_fonts", "multiply_defined", "duplicate_destinations"]:
                self.check(field in build and build[field] == 0, "build-zero", field)
            self.check(build.get("shell_escape") is False, "build", "Shell escape disabled")
            log = self.exists(pdf.with_suffix(".log"))
            if log:
                self.check(not re.search(r"^!|Fatal error|Emergency stop", log.read_text(errors="replace"), re.M),
                           "build-log", "No TeX error/fatal stop in final log")
            try:
                info = subprocess.run(["pdfinfo", str(pdf)], text=True, capture_output=True, check=True).stdout
                count = re.search(r"^Pages:\s*(\d+)", info, re.M)
                self.check(bool(count) and int(count[1]) == self.pages, "pdf-pages", "PDF page count agrees with manifest")
            except (OSError, subprocess.CalledProcessError) as exc:
                self.check(False, "pdf-pages", "Cannot verify actual PDF page count: " + str(exc))
        for name, obj in [("final PDF receipt", final), ("page coverage", coverage)]:
            self.source_binding(obj, label=name)
            self.check(obj.get("pdf_sha256") == self.pdf_hash, "pdf-binding", name)
            self.check(obj.get("render_manifest_sha256") == sha(mp), "manifest-binding", name)
            self.check(obj.get("certified") is True and obj.get("all_pages_read") is True,
                       "page-certification", name)
            self.check(obj.get("page_count") == self.pages and obj.get("covered_pages") == self.pages
                       and obj.get("missing_pages") == [], "page-coverage", name)
        self.check(final.get("reading_coverage_record") == "records/S6_SERIES_PUBLISH_I_page_coverage.json",
                   "page-coverage", "Final receipt names the checked coverage record")
        delivered = self.exists(final.get("final_pdf", "S6_SERIES_PUBLISH_I.pdf"))
        if delivered:
            self.check(sha(delivered) == self.pdf_hash, "final-delivery", "Delivery PDF equals certified build PDF")
        images = manifest.get("rendered_pages", [])
        self.check(len(images) == self.pages and {r.get("page") for r in images} == set(range(1,self.pages+1)),
                   "render-pages", "All complete page images present exactly once")
        imap = {r.get("page"): r for r in images}
        for r in images:
            ip = self.exists(r.get("image", "MISSING_IMAGE"))
            if ip:
                self.check(sha(ip) == r.get("image_sha256"), "image-hash", f"Page {r.get('page')}")
        read_pages = coverage.get("pages", [])
        self.check(len(read_pages) == self.pages and {r.get("page") for r in read_pages} == set(range(1,self.pages+1)),
                   "reading-pages", "One coverage row for every final page")
        for r in read_pages:
            page = r.get("page")
            self.check(r.get("image_sha256") == imap.get(page, {}).get("image_sha256"),
                       "reading-image", f"Page {page}: final whole-PNG equality")
            rp = self.bound({"path": r.get("reading_record"), "sha256": r.get("reading_record_sha256")}, f"Page {page} reading")
            if not rp:
                continue
            record = self.read(rp, {})
            actual = [x for x in walk_rows(record) if x.get("page") == r.get("reading_page")
                      and x.get("image_sha256") == r.get("image_sha256")
                      and x.get("pdf_sha256") == r.get("reading_pdf_sha256")]
            self.check(bool(actual), "reading-evidence", f"Page {page}: exact page/image/PDF tuple in hashed reading record")
            for x in actual:
                self.check(bool(x.get("finding")), "reading-finding", f"Page {page}: substantive reading finding recorded")
                self.check(x.get("viewed_complete_image", True) is not False and x.get("read_complete_page", True) is not False,
                           "actual-reading", f"Page {page}: no explicit incomplete/false reading flag")
        self.exists("S6_SERIES_PUBLISH_reading_I.md")
        self.facts["pages"] = self.pages

    def metadata_counts(self):
        meta = self.read("records/S6_SERIES_PUBLISH_I_current_metadata.json", {})
        sts = self.read("records/S6_SERIES_PUBLISH_I_current_statements.json", [])
        self.source_binding(meta, label="current metadata")
        self.check(meta.get("pdf_sha256") == self.pdf_hash and meta.get("certified_flag") is True,
                   "current-metadata", "Metadata certified against the final PDF")
        begin = self.tex.find(r"\begin{document}")
        actual_env = list(ENV.finditer(self.tex, max(0,begin)))
        self.check(len(sts) == len(actual_env), "environment-count", "Dynamic source environment count equals metadata")
        starts = {m.start() for m in actual_env}
        ids = set()
        for st in sts:
            region = self.tex[st.get("start",0):st.get("end",0)]
            self.check(st.get("start") in starts and st.get("id") in region, "statement-span", str(st.get("id")))
            ids.update(st.get("identities", []))
        self.check(meta.get("printed_environments") == len(sts) and meta.get("statement_identifiers") == len(ids),
                   "metadata-counts", "Counts match current extracted environments and identities")
        events = self.rows("CHECK_EVENTS.tsv")
        selected = [e for e in events if e["statement_id"] in ids]
        derived = {"statements": len(sts), "subject_identifiers": len(ids), "event_associations": len(selected),
                   "declared_evidence_groups": len({e["evidence_group"] or e["event_id"] for e in selected}),
                   "outline_step_associations_separate": len([e for e in events if e["statement_id"].startswith("step-I-")])}
        derived.update(Counter(e["type"] for e in selected))
        for t in TYPES:
            derived.setdefault(t, 0)
        self.check(set(e["type"] for e in selected) <= set(TYPES), "event-types", "Only declared canonical event types")
        rows = [r for r in self.rows("records/S6_SERIES_PUBLISH_check_counts.tsv")
                if r.get("paper") == "I" and r.get("scope") == "current_printed_statements_and_definitions"]
        self.check(len(rows) == 1, "count-row", "Unique current Paper I count row")
        if rows:
            for k,v in derived.items():
                self.check(str(v) == rows[0].get(k), "dynamic-count", f"{k}: recomputed {v}")
        report = self.read("records/S6_SERIES_PUBLISH_I_methodology_counts.json", {})
        self.source_binding(report, label="methodology counts")
        self.check(report.get("events_sha256") == self.ledger_hash, "count-ledger", "Methodology count ledger hash")
        self.check(report.get("counts_sha256") == sha(self.path("records/S6_SERIES_PUBLISH_check_counts.tsv")),
                   "count-table", "Methodology count TSV hash")
        self.check(bool(rows) and report.get("counts") == rows[0], "count-report", "Methodology report equals exact count row")
        self.facts["counts"], self.facts["merged_ledger_rows"] = derived, len(events)
        self.events = {r["event_id"]: r for r in events}

    def defects(self):
        edits = self.rows("S6_SERIES_PUBLISH_defects_I.tsv")
        mapping = self.read("records/S6_SERIES_PUBLISH_I_defect_page_mapping.json", {})
        self.source_binding(mapping, "current_source_sha256", "defect map")
        self.check(mapping.get("current_pdf_sha256") == self.pdf_hash and mapping.get("certified") is True,
                   "defect-map", "Certified current source/PDF page map")
        ids = [r["change_id"] for r in edits]
        details = mapping.get("details", [])
        mids = [r.get("change_id") for r in details]
        self.check(len(ids) == len(set(ids)) and len(mids) == len(set(mids)) and set(ids) == set(mids)
                   and mapping.get("rows") == len(edits), "defect-map-rows", "Every edit mapped exactly once")
        if mapping.get("baseline_page_receipt"):
            self.bound({"path": mapping["baseline_page_receipt"], "sha256": mapping.get("baseline_page_receipt_sha256")},
                       "Original PDF page-locus receipt")
        for d in details:
            for side in ["old", "new"]:
                loc = d.get(side, {})
                method, pages = loc.get("method", ""), loc.get("pages", [])
                self.check(bool(method) and bool(loc.get("location")), "edit-locus", f"{d.get('change_id')} {side}")
                if side == "new":
                    self.check(method != "source-only change", "unmapped-edit", str(d.get("change_id")))
                if pages:
                    # AUX-derived page numbers are decimal strings; SyncTeX emits integers.
                    normalized = [int(x) for x in pages if str(x).isdigit()]
                    self.check(len(normalized) == len(pages) and all(x > 0 and (side == "old" or x <= self.pages) for x in normalized),
                               "edit-pages", f"{d.get('change_id')} {side}: {pages}")
                else:
                    allowed = ("nonprinting", "shared bibliography", "removed uncited", "intermediate revision source-only",
                               "absent from", "not present in", "deleted")
                    self.check(any(token in method.lower() for token in allowed), "edit-page-disposition",
                               f"{d.get('change_id')} {side}: explicit nonprinting/removed/intermediate disposition")
        register = self.rows("S6_DEFECT_REGISTER.csv", ",")
        type_ids = {r["type_id"] for r in register}
        self.check(type_ids == {f"D{i:02d}" for i in range(1,26)}, "defect-register", "All25 declared defect types")
        typed = {t:{r["change_id"] for r in edits if t in re.findall(r"D\d{2}",r["type"])} for t in type_ids}
        receipt = self.read(self.args.defect_closure, {})
        self.source_binding(receipt, label="defect-type closure")
        self.check(receipt.get("pdf_sha256") == self.pdf_hash and receipt.get("final_certified") is True,
                   "defect-types-certified", "All-type closure is certified against final PDF")
        for field, expected in [("register","S6_DEFECT_REGISTER.csv"),("defect_log","S6_SERIES_PUBLISH_defects_I.tsv")]:
            p = self.bound(receipt.get(field), "Defect closure " + field)
            if p:
                self.check(p.resolve() == self.path(expected).resolve(), "defect-closure-input", field)
        types = receipt.get("types", [])
        self.check(len(types) == 25 and {r.get("type_id") for r in types} == type_ids,
                   "defect-types", "One explicit closure row per declared type")
        for r in types:
            t = r.get("type_id")
            self.check(r.get("status") == "closed" and r.get("remaining") == [], "defect-type-status", str(t))
            self.check(bool(r.get("inspected_scope")) and bool(r.get("evidence")), "defect-type-evidence", str(t))
            self.check(set(r.get("edit_ids", [])) == typed.get(t,set()), "defect-type-row-coverage", str(t))
            for e in r.get("evidence", []):
                self.bound(e, str(t)+" closure evidence")
                self.check(bool(e.get("scope")), "defect-evidence-scope", str(t))
        self.facts["logged_edits"], self.facts["defect_type_counts"] = len(edits), {k:len(v) for k,v in sorted(typed.items())}

    def required(self):
        manifest_name = "records/S6_SERIES_PUBLISH_required_check_completion_manifest.json"
        comp = self.read(manifest_name, {})
        rows = {k:v for k,v in comp.get("rows",{}).items() if v.get("paper") == "I"}
        self.check(ORIGINAL_REQUIRED <= rows.keys(), "required-original", "All19 originally required identifiers retained")
        for sid in ORIGINAL_REQUIRED:
            r = rows.get(sid,{})
            self.check(r.get("status") == "done" and bool(r.get("scope")), "required-complete", sid)
            self.bound({"path":r.get("evidence_path"),"sha256":r.get("evidence_sha256")}, sid)
        candidates_name = "records/S6_SERIES_PUBLISH_required_check_candidates.csv"
        candidates = [r for r in self.rows(candidates_name, ",") if r.get("paper") == "I"]
        self.check(not candidates, "required-current", f"Current I candidate rows: {len(candidates)}")
        freshness = self.read(self.args.dependency_binding, {})
        self.source_binding(freshness, label="current dependency closure")
        self.check(freshness.get("ledger_sha256") == self.ledger_hash and freshness.get("certified") is True,
                   "dependency-current", "Current-source/ledger dependency recomputation certified")
        self.check(freshness.get("pending_required_I") == [], "dependency-pending", "No pending current I required checks")
        for field,name in [("completion_manifest",manifest_name),("candidate_table",candidates_name),
                           ("current_statements","records/S6_SERIES_PUBLISH_I_current_statements.json")]:
            p = self.bound(freshness.get(field), "Dependency " + field)
            if p:
                self.check(p.resolve() == self.path(name).resolve(), "dependency-input", field)
        self.check(isinstance(freshness.get("current_main_dependency_environments"),int)
                   and freshness["current_main_dependency_environments"] > 0,
                   "dependency-scope", "Current main-theorem closure size explicitly recorded")
        self.facts["original_required_completed"] = sum(rows.get(s,{}).get("status") == "done" for s in ORIGINAL_REQUIRED)
        self.facts["current_required_candidates"] = len(candidates)

    def globals(self):
        aggregate = self.read(self.args.global_binding, {})
        self.source_binding(aggregate, label="A–G final binding")
        self.check(aggregate.get("ledger_sha256") == self.ledger_hash and aggregate.get("pdf_sha256") == self.pdf_hash,
                   "global-hashes", "A–G binding uses final ledger/PDF")
        if "headlines" in aggregate:
            # Current topology-owned aggregate transports the actual scoped ABC/DE/FG
            # receipts. Verify its archived bytes and event rows, rather than require
            # a redundant synthetic certificate or new mathematical credit.
            heads=aggregate.get("headlines",{})
            self.check(set(heads)==set("ABCDEFG"), "global-coverage", "A–G exact coverage")
            self.check(aggregate.get("status","").startswith("complete:")
                       and aggregate.get("actual_complete_headlines_read")==len(heads),
                       "global-certified", "Complete current global comparison receipt")
            self.check(aggregate.get("actual_complete_outline_items_read")==sum(x.get("outline_items",0) for x in heads.values()),
                       "global-outline-count", "All actual outline items accounted")
            for letter,r in heads.items():
                self.check(r.get("actual_current_statement_read") is True and r.get("actual_current_complete_outline_read") is True,
                           "global-actual-reading", letter)
                for part in ["statement","outline"]:
                    text=r.get(part,"")
                    self.check(bool(text) and text in self.tex and hashlib.sha256(text.encode()).hexdigest()==r.get(part+"_sha256"),
                               "global-exact-text", letter+" "+part)
            for r in aggregate.get("input_receipts",[]):
                self.bound(r,"Prior scoped global receipt")
            evidence=aggregate.get("prior_evidence_event_rows",[])
            self.check({"series:I:"+x for x in "ABCDEFG"} <= {r.get("statement_id") for r in evidence},
                       "global-event-coverage", "Existing global event associations cover A–G")
            for r in evidence:
                self.check(self.events.get(r.get("event_id"))==r,"global-existing-event",str(r.get("event_id")))
            blocks=aggregate.get("block_comparisons",[])
            self.check(bool(blocks) and len(blocks)==aggregate.get("archived_block_associations"),
                       "global-body-coverage", "Archived supplying proof-block association count")
            marker_maps=aggregate.get("exact_marker_maps",[])
            editorial_maps=aggregate.get("explicit_editorial_maps",[])
            marker_labels={r.get("label") for r in marker_maps}
            editorial_labels={r.get("label") for r in editorial_maps}
            self.check(not marker_labels & editorial_labels, "global-map-kinds",
                       "Marker-only maps and exposed editorial proof comparisons are separate")
            editorial_keys=set()
            for mapping in editorial_maps:
                label=str(mapping.get("label"))
                matches=[b for b in blocks if all(b.get(k)==mapping.get(k) for k in
                         ["label","prior_block_sha256","current_block_sha256"])]
                unique_pairs={(b.get("prior_block",""),b.get("current_block","")) for b in matches}
                exact=self.check(len(unique_pairs)==1, "global-editorial-owner",
                                 label+": exact full-block hash pair occurs in supplying-block archive")
                self.check(mapping.get("actual_complete_old_and_current_statement_and_proof_read") is True,
                           "global-editorial-reading",label+": complete before/after proof comparison attested")
                self.check(mapping.get("new_math_event_rows") == 0,
                           "global-editorial-credit",label+": no new mathematical event from this transport")
                self.bound(mapping.get("comparison_receipt"),label+": exposed editorial comparison receipt")
                if exact:
                    prior,current=next(iter(unique_pairs))
                    try:
                        invert_editorial_guards(current,prior,mapping.get("inverse_guards"))
                    except ValueError as exc:
                        self.check(False,"global-editorial-inverse",label+": "+str(exc))
                    else:
                        self.check(True,"global-editorial-inverse",label+": inverse guards reconstruct the entire prior block")
                        editorial_keys.add((mapping.get("label"),mapping.get("prior_block_sha256"),mapping.get("current_block_sha256")))
            for r in blocks:
                text=r.get("current_block","")
                prior=r.get("prior_block","")
                self.check(bool(text) and text in self.tex and hashlib.sha256(text.encode()).hexdigest()==r.get("current_block_sha256"),
                           "global-proof-bytes",str(r.get("label")))
                self.check(bool(prior) and hashlib.sha256(prior.encode()).hexdigest()==r.get("prior_block_sha256"),
                           "global-prior-proof-bytes",str(r.get("label")))
                matching_markers=[m for m in marker_maps if all(m.get(k)==r.get(k) for k in
                                  ["label","prior_block_sha256","current_block_sha256"])]
                marker_ok=False
                for m in matching_markers:
                    marker_ok=(m.get("mapped_bytes_equal_current") is True and m.get("proof_bytes_identical") is True
                               and "\\begin{proof}" in prior and "\\begin{proof}" in text
                               and prior[prior.index("\\begin{proof}"):]==text[text.index("\\begin{proof}"):]
                               and hashlib.sha256(text[text.index("\\begin{proof}"):].encode()).hexdigest()==m.get("proof_sha256"))
                    if marker_ok:
                        break
                key=(r.get("label"),r.get("prior_block_sha256"),r.get("current_block_sha256"))
                self.check((r.get("bytes_identical") is True and prior==text) or marker_ok or key in editorial_keys,
                           "global-proof-transport",str(r.get("label")))
            self.check(aggregate.get("counterexample_presentation_comparison",{}).get("actual_complete_old_and_current_statement_and_proof_read") is True,
                       "global-changed-proof-reading","Changed counterexample presentation fully compared")
            return
        self.check(aggregate.get("certified") is True and aggregate.get("remaining") == [],
                   "global-certified", "All current main-theorem comparison scopes closed")
        ts = aggregate.get("theorems", {})
        self.check(set(ts) == set("ABCDEFG"), "global-coverage", "A–G exact coverage")
        for letter,r in ts.items():
            self.check(r.get("statement_and_outline_compared") is True and r.get("body_dependencies_compared") is True
                       and bool(r.get("scope")), "global-scope", str(letter))
            p = self.bound(r.get("receipt"), f"Theorem {letter} current binding")
            if p:
                sub = self.read(p,{})
                h = sub.get("source_sha256", sub.get("current_source_sha256"))
                self.check(h == self.source_hash, "global-receipt-source", letter)
            ev = r.get("event_ids", [])
            self.check(bool(ev) and all(x in self.events for x in ev), "global-events", letter)
            self.check(bool(r.get("evidence_groups")) and set(r.get("evidence_groups",[])) <=
                       {self.events[x]["evidence_group"] for x in ev if x in self.events}, "global-groups", letter)

    def provenance(self):
        prefix = "agents/i_provenance/S6_SERIES_PUBLISH_I_"
        binding = self.read(prefix+"final_source_count_binding.json", {})
        claims = self.read(prefix+"three_way_claim_table_final.json", {})
        self.source_binding(claims, label="42-claim table")
        for field in ["source","root_count_report","counts_file","statement_counts_file","ledger",
                      "completion_manifest","deposit_json","deposit_md","claim_table","claim_tsv","final_coverage"]:
            self.bound(binding.get(field), "Provenance " + field)
        self.check(binding.get("source",{}).get("sha256") == self.source_hash
                   and binding.get("ledger",{}).get("sha256") == self.ledger_hash, "provenance-hashes", "Final source and ledger")
        self.check(binding.get("candidate_pdf",{} if binding.get("candidate_pdf") else {}).get("sha256") == self.pdf_hash
                   if isinstance(binding.get("candidate_pdf"),dict) else False, "provenance-pdf", "Final PDF bound")
        self.check(binding.get("pdf_review_status") == "certified" and binding.get("claim_count") == 42,
                   "provenance-certified", "42 claims with certified PDF binding")
        self.check(isinstance(claims.get("final_pdf"),dict) and claims["final_pdf"].get("sha256") == self.pdf_hash,
                   "claim-table-pdf", "Final PDF bound inside the42-claim table")
        for name,obj in [("provenance binder",binding),("42-claim table",claims)]:
            fc=obj.get("final_coverage")
            self.check(isinstance(fc,dict) and fc.get("sha256") == sha(self.path("records/S6_SERIES_PUBLISH_I_page_coverage.json")),
                       "provenance-final-coverage", name)
        rs = claims.get("claims", [])
        self.check(len(rs) == 42 and {r.get("id") for r in rs} == {f"I-P{i:02d}" for i in range(1,43)},
                   "provenance-claims", "All42 original and supplementary claim IDs")
        for r in rs:
            self.check(r.get("remaining_gate") == "None for the source/count/PDF metadata binding."
                       and all(r.get(k) for k in ["attached_record_comparison","primary_or_check_evidence","disposition","status"]),
                       "provenance-disposition", str(r.get("id")))
        exact = claims.get("exact_main_status_binding", {})
        self.check(sum(len(g) for g in exact.values()) == 21, "main-status-count", "All21 main status/mechanism/table bindings")
        for group in exact.values():
            for r in group.values():
                self.check(r.get("source_occurrences") == 1, "main-status-binding", "Unique recorded status occurrence")
                if r.get("text"):
                    self.check(self.tex.count(r["text"]) == 1, "main-status-text", "Exact bound text occurs once")
        shared = [r for r in self.rows("S6_SERIES_PUBLISH_provenance_checks.tsv") if r.get("paper") == "I"]
        own = self.rows(prefix+"provenance_checks.tsv")
        self.check(shared == own and len(shared) == 42, "shared-provenance", "Final42 rows applied to shared table")
        deposit = self.exists(prefix+"deposit_fields.md")
        shared_deposit = self.exists("S6_SERIES_PUBLISH_deposit_fields.md")
        if deposit and shared_deposit:
            own_text = deposit.read_text(); i = own_text.find("## Paper I\n")
            section = own_text[i:] if i >= 0 else ""
            self.check(bool(section) and section.strip() in shared_deposit.read_text(), "shared-deposit", "Exact Paper I deposit section applied")
        review = self.read("records/S6_SERIES_PUBLISH_I_root_42_claim_review.json", {})
        self.check(review.get("input_sha256") == sha(self.path(prefix+"three_way_claim_table_final.json")),
                   "root-42-review-hash", "Root review bound to final claim table")
        self.check(set(review.get("claims_actually_read",[])) == {f"I-P{i:02d}" for i in range(1,43)}
                   and review.get("all_claims_finally_closed") is True and not review.get("required_rebinding",[]),
                   "root-42-review", "Root42 review completed with no outstanding rebinding")

    def run(self):
        for name in ["basic","rendered","metadata_counts","defects","required","globals","provenance"]:
            try:
                getattr(self,name)()
            except Exception as exc:
                self.check(False,"validator-section",f"{name}: {type(exc).__name__}: {exc}")
        # Prevent a concurrent root edit from passing against mixed snapshots.
        for p,h in self.inputs.items():
            self.check(Path(p).is_file() and sha(Path(p)) == h, "snapshot-stability", p)
        return {"schema":1,"paper":"I","checked_utc":datetime.now(timezone.utc).isoformat(),
                "closed":not self.errors,"source_sha256":self.source_hash,"pdf_sha256":self.pdf_hash,
                "ledger_sha256":self.ledger_hash,"facts":self.facts,"failures":self.errors,
                "passed_checks":len(self.passed),"input_hashes":self.inputs,
                "scope":"Read-only binding validation. No proof, check event, or human-verification claim is created."}

def write_outputs(result, out, stage, work):
    out.mkdir(parents=True,exist_ok=True)
    report = out / "S6_SERIES_PUBLISH_I_closure_validation.json"
    report.write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n")
    lines = ["# Paper I closure validation", "", "Status: **"+("all required bindings pass" if result["closed"] else "OPEN")+"**.",
             "", "Source: `"+result["source_sha256"]+"`.", "PDF: `"+result["pdf_sha256"]+"`.",
             "Ledger: `"+result["ledger_sha256"]+"`.", "", "No shared files were changed; no mathematical event was added.", "", "## Remaining gates", ""]
    lines += [f"- **{x['code']}**: {x['detail']}" for x in result["failures"]] or ["All machine-checkable receipt bindings pass."]
    (out/"S6_SERIES_PUBLISH_I_closure_validation.md").write_text("\n".join(lines)+"\n")
    if not stage:
        return
    if not result["closed"]:
        raise SystemExit("Cannot stage closure updates: one or more gates remain open.")
    gate = {k:v for k,v in result.items() if k not in ["failures","passed_checks","input_hashes"]}
    gate["validation_receipt"] = {"path":str(report),"sha256":sha(report)}
    gate["remaining_series_gate"] = "Complete the remaining papers and the final cross-paper consistency review."
    proposed_gate = out/"S6_SERIES_PUBLISH_I_complete_gate_proposed.json"
    proposed_gate.write_text(json.dumps(gate,indent=2,ensure_ascii=False)+"\n")
    f=result["facts"];c=f["counts"]
    block=("\n## Paper I completed — "+result["checked_utc"]+"\n\n"
           f"The exact {f['pages']}-page source/PDF snapshot passes the recorded closure gates: all25 defect types, "
           f"{f['logged_edits']} mapped edits,42 provenance claims, all19 original required rows, no current required candidate, "
           "and current A–G comparison bindings. Original labels and permanent tag targets remain.\n\n"
           f"Current scope: {c['statements']} printed environments; {c['subject_identifiers']} statement identities; "
           f"{c['event_associations']} associations in {c['declared_evidence_groups']} declared evidence groups. "
           "These retain the exact scopes and types in CHECK_EVENTS; closure creates no mathematical event.\n\n"
           f"Source SHA-256: `{result['source_sha256']}`. PDF SHA-256: `{result['pdf_sha256']}`. "
           f"Ledger SHA-256: `{result['ledger_sha256']}`. The full series task remains incomplete.\n")
    updates=[{"target":str(work/"records/S6_SERIES_PUBLISH_I_complete_gate.json"),
              "expected_sha256":sha(work/"records/S6_SERIES_PUBLISH_I_complete_gate.json") if (work/"records/S6_SERIES_PUBLISH_I_complete_gate.json").exists() else None,
              "replacement":{"path":str(proposed_gate),"sha256":sha(proposed_gate)}}]
    for name in ["PROGRESS_LEDGER.md","S6_SERIES_PUBLISH_report.md"]:
        target=work/name
        if not target.is_file():
            raise SystemExit("Missing root review target: "+str(target))
        proposed=out/("S6_SERIES_PUBLISH_I_"+name.replace(".md","_proposed.md"))
        proposed.write_text(target.read_text().rstrip()+"\n"+block)
        updates.append({"target":str(target),"expected_sha256":sha(target),"replacement":{"path":str(proposed),"sha256":sha(proposed)}})
    (out/"S6_SERIES_PUBLISH_I_closure_update_guards.json").write_text(json.dumps({"source_sha256":result["source_sha256"],
        "ledger_sha256":result["ledger_sha256"],"updates":updates,"scope":"Staged only. Root must review and apply; historical report text remains intact."},indent=2)+"\n")

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--work-root",type=Path,default=HERE.parents[1])
    p.add_argument("--manifest",help="Candidate/final manifest for diagnostics; certification still required")
    p.add_argument("--output-dir",type=Path,default=HERE/"S6_SERIES_PUBLISH_I_closure_draft")
    p.add_argument("--defect-closure",default="agents/i_provenance/S6_SERIES_PUBLISH_I_defect_type_closure_evidence.json")
    p.add_argument("--dependency-binding",default="records/S6_SERIES_PUBLISH_I_main_dependency_dispositions.json")
    p.add_argument("--global-binding",default="agents/i_topology/S6_SERIES_PUBLISH_I_final_AG_current_binding.json")
    p.add_argument("--stage-updates",action="store_true",help="Only after all gates pass; write proposals in agent directory, never apply")
    a=p.parse_args();out=a.output_dir.resolve()
    if not out.is_relative_to(HERE):
        p.error("Outputs must stay inside this agent directory; shared mutations are forbidden")
    v=Validator(a);r=v.run();write_outputs(r,out,a.stage_updates,a.work_root.resolve())
    print(json.dumps({"closed":r["closed"],"failures":len(r["failures"]),"passed_checks":r["passed_checks"],
                      "report":str(out/"S6_SERIES_PUBLISH_I_closure_validation.json"),"facts":r["facts"]},indent=2))
    return 0 if r["closed"] else 2

if __name__=="__main__":
    sys.exit(main())
