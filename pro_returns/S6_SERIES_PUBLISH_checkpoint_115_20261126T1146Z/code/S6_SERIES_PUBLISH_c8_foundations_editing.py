"""Exact owned-fragment edits with the required defects-table records."""
from collections import Counter
import csv
from datetime import datetime, timezone
from pathlib import Path
import re

from S6_SERIES_PUBLISH_c8_foundations_marked_data import ROOT, LANE, DEFECTS, FIELDS, WHO, identities
from S6_SERIES_PUBLISH_c8_integrate_presentation import (
    statement_records_to_small_tags, remove_manual_equation_tags,
    unresolved_literal_equation_references,
)


class Editor:
    def __init__(self, key, prefix, group="foundations"):
        if group != "foundations" and (group, key) != ("root", "cyclic_invariants"):
            raise ValueError("Fragment is outside the expressly assigned source regions")
        self.path = ROOT / "agents/continuation8_iii_integration/units" / group / (key + ".tex")
        self.original = self.path.read_text()
        self.text = self.original
        self.prefix = prefix
        self.new_rows = []
        self.when = datetime.now(timezone.utc).isoformat()
        with DEFECTS.open(newline="") as stream:
            self.rows = list(csv.DictReader(stream, delimiter="\t"))
        if any(row["change_id"].startswith(prefix) for row in self.rows):
            raise ValueError("This edit batch already has defect records")

    def record(self, kind, label, start, old, new, reason):
        self.new_rows.append(dict(zip(FIELDS, [
            self.prefix + f"{len(self.new_rows)+1:03}", kind, label,
            str(self.path.relative_to(ROOT))+f"; pre-edit fragment line {self.text.count(chr(10), 0, start)+1}",
            "pending final page concordance", str(self.path.relative_to(ROOT))+"; "+label,
            "pending final build", old, new, reason,
            "Applied to owned fragment "+self.when+". "+WHO+
            " Source/proof review is documented in the local unit note; canonical assembly and publication gates remain root work.",
        ])))

    def replace(self, old, new, kind, label, reason):
        if not old or self.text.count(old) != 1:
            raise ValueError(("nonunique or stale exact guard", old[:100], self.text.count(old)))
        start = self.text.index(old)
        self.record(kind, label, start, old, new, reason)
        self.text = self.text[:start] + new + self.text[start+len(old):]

    def presentation(self):
        candidate, edits, issues = statement_records_to_small_tags(self.text)
        if issues:
            raise ValueError(issues)
        for edit in edits:
            self.record(edit.kind, edit.statement_label, edit.start, edit.old, edit.new, edit.reason)
        self.text = candidate
        candidate, edits, issues, aliases = remove_manual_equation_tags(self.text)
        if issues:
            raise ValueError(issues)
        for edit in edits:
            # The last preceding formal statement is an exact local owner.
            previous = list(re.finditer(r"\\begin\{(?:theorem|lemma|proposition|corollary|computed|definition|remark)\}[^\n]*", self.text[:edit.start]))
            owner = previous[-1].start() if previous else 0
            labels = re.findall(r"\\label\{([^}]+)\}", self.text[owner:edit.start])
            label = labels[0] if labels else "unit-local display"
            self.record(edit.kind, label, edit.start, edit.old, edit.new, edit.reason)
        self.text = candidate
        return unresolved_literal_equation_references(self.text, aliases)

    def finish(self, labels=(), tags=()):
        for command, allowed in (("label", set(labels)), ("hypertarget", {"tag-"+tag for tag in tags})):
            before, after = identities(self.original, command), identities(self.text, command)
            if before-after or after-before != Counter(allowed):
                raise ValueError((command, before-after, after-before))
        for delimiter in (r"\begin{proof}", r"\end{proof}"):
            if self.original.count(delimiter) != self.text.count(delimiter):
                raise ValueError("Proof count changed without an explicit separate proof disposition")
        with DEFECTS.open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
            writer.writeheader()
            writer.writerows(self.rows + self.new_rows)
        self.path.write_text(self.text)
        print("Edited owned fragment:", self.path.relative_to(ROOT))
        print("Exact defect rows:", len(self.new_rows))
        print("Old label/hypertarget multisets and proof counts preserved.")
        print("New tags:", ", ".join(tags) if tags else "none")
        print("No canonical source, shared progress, or central events written.")
