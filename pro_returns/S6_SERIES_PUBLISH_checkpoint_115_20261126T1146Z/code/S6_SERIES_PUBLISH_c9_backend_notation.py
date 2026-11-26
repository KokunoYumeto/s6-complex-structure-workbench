"""Bounded, reversible notation proposals owned by the backend/source reviewer.

This distinct module restores the Packet interface after a shared filename
collision. S6_NOTATION_SOURCE and S6_NOTATION_EXPECTED_CANDIDATE allow an
outside-tree reconstruction check; S6_NOTATION_VERIFY_ONLY suppresses all writes.
The helper never writes the canonical manuscript or canonical event/defect files.
"""
from pathlib import Path
import csv
import difflib
import hashlib
import os
import re


def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()


class Packet:
    def __init__(self, tag, sid, expected_sha, pages, description,
                 image_reader="this reviewer"):
        self.root = Path(__file__).resolve().parents[1]
        self.tag, self.sid, self.pages = tag, sid, pages
        self.description, self.image_reader = description, image_reader
        self.source_path = Path(os.environ.get(
            "S6_NOTATION_SOURCE", self.root / "S6_SERIES_PUBLISH_III.tex"))
        self.source_bytes = self.source_path.read_bytes()
        assert b"\r" not in self.source_bytes
        self.source = self.source_bytes.decode()
        anchor = self.source.index(r"\hypertarget{tag-" + tag + "}")
        self.start = self.source.rfind(r"\begin{theorem}", 0, anchor)
        assert self.start >= 0
        self.end = self.source.index(r"\end{proof}", anchor) + len(r"\end{proof}")
        self.old = self.source[self.start:self.end]
        assert sha(self.old) == expected_sha, (tag, "bounded baseline", sha(self.old))
        assert r"\label{" + sid + "}" in self.old
        self.new = self.old
        self.operations = []

    def literals(self, pairs):
        def change(text):
            details = []
            for pair in pairs:
                old, new = pair[:2]
                count = text.count(old)
                assert count > 0, (self.tag, "missing literal", old)
                if len(pair) == 3:
                    assert count == pair[2], (self.tag, old, count, pair[2])
                text = text.replace(old, new)
                details.append((count, old, new))
            change.details = details
            return text
        change.details = []
        return change

    def symbols(self, pairs, indexed=False):
        def change(text):
            details = []
            for old, new in pairs:
                suffix = r"(?![A-Za-z])" if indexed else r"(?![A-Za-z_])"
                pattern = re.compile(r"(?<![A-Za-z\\])" + re.escape(old) + suffix)
                protected = re.compile(r"(\\(?:label|hypertarget|[A-Za-z]*ref|cite[A-Za-z]*)\*?(?:\[[^]]*\])?\{[^}]+\})")
                parts = protected.split(text)
                count = 0
                for index in range(0, len(parts), 2):
                    parts[index], number = pattern.subn(lambda m: new, parts[index])
                    count += number
                text = ''.join(parts)
                assert count > 0, (self.tag, "missing symbol", old)
                details.append((count, old, new))
            change.details = details
            return text
        change.details = []
        return change

    def _record(self, name, old, new, reason, kind, details):
        assert old != new, (self.tag, name, "empty change")
        assert self.new.count(old) == 1, (self.tag, name, "old operation guard")
        self.new = self.new.replace(old, new, 1)
        assert self.new.count(new) == 1, (self.tag, name, "new operation guard")
        changed_old, changed_new = [], []
        aa, bb = old.splitlines(), new.splitlines()
        for op, a, b, c, d in difflib.SequenceMatcher(a=aa, b=bb, autojunk=False).get_opcodes():
            if op != "equal":
                changed_old.extend(aa[a:b])
                changed_new.extend(bb[c:d])
        self.operations.append(dict(name=name, old=old, new=new, reason=reason,
                                    kind=kind, details=details,
                                    changed_old=changed_old, changed_new=changed_new))

    def exact(self, name, old, new, reason, kind="D20"):
        self._record(name, old, new, reason, kind, [(1, old, new)])

    def scope(self, name, first, last, transform, reason, kind="D20"):
        a = self.new.index(first)
        b = self.new.index(last, a) if last is not None else len(self.new)
        old = self.new[a:b]
        new = transform(old)
        self._record(name, old, new, reason, kind, transform.details)

    def finish(self):
        back = self.new
        for op in reversed(self.operations):
            assert back.count(op["new"]) == 1, (self.tag, op["name"], "inverse")
            back = back.replace(op["new"], op["old"], 1)
        assert back == self.old
        for pattern in [r"\\label\{[^}]+\}", r"\\hypertarget\{[^}]+\}",
                        r"\\(?:[A-Za-z]*ref|cite[A-Za-z]*)\*?(?:\[[^]]*\])?\{[^}]+\}"]:
            assert re.findall(pattern, self.old) == re.findall(pattern, self.new), pattern
        assert b"\r" not in self.new.encode()
        assert self.source_path.read_bytes() == self.source_bytes
        expected = os.environ.get("S6_NOTATION_EXPECTED_CANDIDATE")
        if expected:
            assert self.new.encode() == Path(expected).read_bytes(), (self.tag, "candidate replay")
        print("Theorem", self.tag, "baseline", len(self.old.splitlines()), sha(self.old))
        print("Candidate", len(self.new.splitlines()), sha(self.new))
        if os.environ.get("S6_NOTATION_VERIFY_ONLY") == "1":
            print("VERIFY ONLY: every scoped operation, complete reverse, identifiers and exact candidate bytes passed; no files written.")
            return

        # Keep fragments unique in the complete source in both directions.
        old_lines, new_lines = self.old.splitlines(True), self.new.splitlines(True)
        complete_new = self.source[:self.start] + self.new + self.source[self.end:]
        for context in range(2, 13):
            groups = list(difflib.SequenceMatcher(
                a=old_lines, b=new_lines, autojunk=False).get_grouped_opcodes(n=context))
            fragments = []
            for group in groups:
                a, b = group[0][1], group[-1][2]
                c, d = group[0][3], group[-1][4]
                old, new = ''.join(old_lines[a:b]), ''.join(new_lines[c:d])
                fragments.append((old, new))
            if all(self.source.count(old) == 1 and complete_new.count(new) == 1
                   for old, new in fragments):
                break
        else:
            raise AssertionError((self.tag, "no unique reversible fragment context"))

        rows = []
        for number, (old, new) in enumerate(fragments, 1):
            relevant = [op for op in self.operations
                        if any(line.strip() and line in old for line in op["changed_old"])
                        or any(line.strip() and line in new for line in op["changed_new"])]
            assert relevant, (self.tag, number, "no operation reason")
            reasons = list(dict.fromkeys(op["reason"] for op in relevant))
            kinds = list(dict.fromkeys(op["kind"] for op in relevant))
            rows.append(dict(
                change_id=f"CLAUDE-III-C9-PDF-{self.tag}-{number:03}",
                type=";".join(kinds), statement_id=self.sid,
                old_location=f"{self.tag} full statement/proof; exact pre-edit fragment",
                old_page=f"candidate02 physical {self.pages}",
                new_location="same theorem/proof and permanent identifiers",
                new_page="pending rebuilt image review", old_text=old, new_text=new,
                reason=" ".join(reasons),
                review_status=f"Full {len(self.old.splitlines())}-line theorem/proof read and compared; exact reverse application recovers all baseline bytes. Root admission and rebuilt image review pending."))
        forward = self.source
        for row in rows:
            assert forward.count(row["old_text"]) == 1
            forward = forward.replace(row["old_text"], row["new_text"], 1)
        assert forward == complete_new
        for row in reversed(rows):
            assert forward.count(row["new_text"]) == 1
            forward = forward.replace(row["new_text"], row["old_text"], 1)
        assert forward == self.source

        folder = self.root / "agents" / f"continuation9_{self.tag}_notation"
        folder.mkdir(exist_ok=True)
        stem = f"S6_SERIES_PUBLISH_c9_{self.tag}_notation"
        with (folder / (stem + "_defects.tsv")).open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
        (folder / (stem + ".diff")).write_text(''.join(difflib.unified_diff(
            old_lines, new_lines, fromfile=self.tag + " before", tofile=self.tag + " proposed", n=5)))
        temporary = self.root.parents[1] / "tmp" / f"c9_{self.tag}_notation"
        temporary.mkdir(exist_ok=True)
        candidate = temporary / f"S6_SERIES_PUBLISH_c9_{self.tag}_proposed.tex"
        candidate.write_text(self.new)

        # A packet is a review proposal. Preserve its already established event
        # identity and authorship; changing this helper creates no new event.
        event_path = folder / (stem + "_CHECK_EVENTS.tsv")
        assert event_path.exists(), (self.tag, "existing proposal event required")
        with event_path.open(newline="") as handle:
            reader = csv.DictReader(handle, delimiter="\t")
            fields = reader.fieldnames
            events = list(reader)
        assert len(events) == 1
        event = events[0]
        assert event["event_id"] == f"publish:c9:III:{self.tag}:full-notation-context"
        event["where"] = event["where"].replace(
            "code/S6_SERIES_PUBLISH_c9_scoped_notation.py",
            "code/S6_SERIES_PUBLISH_c9_backend_notation.py")
        event["outcome"] = (
            f"Read the complete {len(self.old.splitlines())}-line statement/proof following actual candidate02 physical {self.pages} image reading by {self.image_reader}. "
            + self.description + f" Prepared {len(rows)} exact guarded fragments; reversing the explicit scoped operations recovers every baseline byte. "
            + "Permanent labels, tags, references and citations are unchanged. This exposed context review adds no independent re-proof credit. Root admission and rebuilt image review remain pending.")
        with event_path.open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
            writer.writeheader()
            writer.writerows(events)
        print("Scoped operations", len(self.operations), "exact fragments", len(rows), "context", context)
        for op in self.operations:
            print(op["name"], "|", op["kind"], "|", op["reason"])
            for count, old, new in op["details"]:
                print("  exact target count", count, repr(old), "→", repr(new))
        print("Full reverse comparison passed; labels/tags/references/citations and canonical source bytes unchanged.")
        print("Staged output", folder.relative_to(self.root))
        print("Temporary candidate", candidate)
        assert self.source_path.read_bytes() == self.source_bytes
