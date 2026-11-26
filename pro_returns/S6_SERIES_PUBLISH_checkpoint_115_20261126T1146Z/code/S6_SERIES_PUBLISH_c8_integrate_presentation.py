"""Callable, bounded Paper III presentation helpers; no manuscript writer.

Each helper returns its proposed text plus exact edits and unresolved cases.
No blanket vocabulary substitutions are made. The root preamble owns the
Return-to-results hook, equation counter configuration, fonts, and global
macros. This module never changes them or awards a publication criterion.
"""
from __future__ import annotations

from dataclasses import dataclass
import re

import S6_SERIES_PUBLISH_c8_integrate_units as units


@dataclass(frozen=True)
class Change:
    kind: str
    start: int
    end: int
    old: str
    new: str
    statement_label: str = ""
    tag: str = ""
    reason: str = ""


@dataclass(frozen=True)
class Unresolved:
    kind: str
    line: int
    token: str
    detail: str


def comments_masked(text: str) -> str:
    chars = list(text)
    cursor = 0
    while cursor < len(text):
        if text[cursor] == "\\":
            cursor += 2
            continue
        if text[cursor] == "%":
            end = text.find("\n", cursor)
            end = len(text) if end < 0 else end
            chars[cursor:end] = " " * (end - cursor)
            cursor = end
        cursor += 1
    return "".join(chars)


def braced_argument(text: str, mask: str, cursor: int):
    while cursor < len(mask) and mask[cursor].isspace():
        cursor += 1
    end = units.group_end(mask, cursor)
    return text[cursor + 1:end - 1], end


def apply_changes(text: str, changes: list[Change]) -> str:
    previous = len(text)
    for edit in sorted(changes, key=lambda x: x.start, reverse=True):
        if edit.end > previous or text[edit.start:edit.end] != edit.old:
            raise ValueError("Presentation edit overlaps or has a stale exact guard")
        text = text[:edit.start] + edit.new + text[edit.end:]
        previous = edit.start
    return text


def statement_records_to_small_tags(text: str):
    """Replace four balanced record arguments by the existing visible tag."""
    mask = comments_masked(text)
    beginnings = list(re.finditer(r"\\begin\{(?:" + units.FORMAL + r"|maintheorem)\}|\\paragraph\*?\{", mask))
    changes, unresolved = [], []
    for match in re.finditer(r"\\StatementRecord\b", mask):
        cursor = match.end()
        args = []
        for _ in range(4):
            argument, cursor = braced_argument(text, mask, cursor)
            args.append(argument)
        own_label = args[0].strip()
        preceding = [begin for begin in beginnings if begin.start() < match.start()]
        begin = preceding[-1].start() if preceding else 0
        identities = [identity for identity in units.ANCHOR_LABEL.finditer(mask, begin, match.start())
                      if identity[2] == own_label]
        if len(identities) != 1:
            unresolved.append(Unresolved("statement-record-owner", text.count("\n", 0, match.start()) + 1,
                                         own_label, "The current statement header does not identify exactly one matching tag and label."))
            continue
        tag = identities[0][1]
        replacement = "{\\normalfont\\scriptsize tag " + tag + "}\\par"
        changes.append(Change("D10", match.start(), cursor, text[match.start():cursor], replacement,
                              own_label, tag, "Replace the four-argument process record by its existing small visible tag; permanent anchors and labels remain outside the edit."))
    candidate = apply_changes(text, changes)
    units.check_permanent_identifiers(text, candidate)
    return candidate, changes, unresolved


def remove_manual_equation_tags(text: str, convert_single_displays=True):
    r"""Use automatic numbers, preserving the exact mathematical display body.

    A single manually tagged \[...\] becomes an equation environment. A single
    manually tagged equation* similarly becomes equation. The delimiter change
    and tag removal are returned as exact D19 edits. Multi-tag or other starred
    environments are left for the unit editor, because numbering their rows
    requires deciding which displays constitute separately cited equations.
    """
    mask = comments_masked(text)
    # A matrix row break \\[2pt] is not a display opener \[.
    transitions = list(re.finditer(r"(?<!\\)\\(begin|end)\{([^}]+)\}|(?<!\\)\\(\[|\])", mask))
    numbered = {"equation", "align", "gather", "multline", "flalign", "alignat", "eqnarray"}
    display = numbered | {name + "*" for name in numbered} | {"displaymath", "bracket-display"}
    changes, unresolved, aliases = [], [], []
    stack = []
    intervals = []
    for transition in transitions:
        if transition[1] == "begin" or transition[3] == "[":
            name = transition[2] if transition[1] else "bracket-display"
            stack.append((name, transition.start(), transition.end()))
            continue
        name = transition[2] if transition[1] else "bracket-display"
        if not stack or stack[-1][0] != name:
            line = text.count("\n", 0, transition.start()) + 1
            raise ValueError(f"Unbalanced environment at fragment line {line}: closing {name}; open stack {[entry[0] for entry in stack]}")
        opened = stack.pop()
        if name in display:
            intervals.append((name, opened[1], opened[2], transition.start(), transition.end()))
    tags = list(re.finditer(r"\\tag\*?(?=\s*\{)", mask))
    changed_displays = set()
    for match in tags:
        value, end = braced_argument(text, mask, match.end())
        aliases.append(value.strip())
        matches = [span for span in intervals if span[2] <= match.start() < span[3]]
        span = min(matches, key=lambda item: item[4] - item[1]) if matches else None
        enclosing = span[0] if span else None
        can_convert = (convert_single_displays and enclosing in {"bracket-display", "equation*"}
                       and sum(span[2] <= tag.start() < span[3] for tag in tags) == 1)
        if can_convert:
            if span[1] not in changed_displays:
                changes.append(Change("D19", span[1], span[2], text[span[1]:span[2]], r"\begin{equation}",
                                      reason="Give this single tagged display an automatic section equation number; its mathematical body is retained verbatim."))
                changes.append(Change("D19", span[3], span[4], text[span[3]:span[4]], r"\end{equation}",
                                      reason="Close the corresponding numbered display; all labels and anchors remain in their original relative positions."))
                changed_displays.add(span[1])
        elif enclosing not in numbered:
            unresolved.append(Unresolved("manual-tag-needs-numbered-display", text.count("\n", 0, match.start()) + 1,
                                         value, "Enclosing display: " + str(enclosing)))
            continue
        changes.append(Change("D19", match.start(), end, text[match.start():end], "", reason="Use the enclosing numbered display and root's section equation counter; retain every existing equation label and anchor."))
    candidate = apply_changes(text, changes)
    units.check_permanent_identifiers(text, candidate)
    return candidate, changes, unresolved, aliases


def unresolved_literal_equation_references(text: str, aliases=()):
    """Locate printed old equation tokens; do not infer their semantic targets."""
    mask = comments_masked(text)
    hidden = list(mask)
    for match in re.finditer(r"\\(?:label|hypertarget|eqref|ref|cref|Cref|SeriesRef|tag\*?)\s*\{", mask):
        cursor = match.end() - 1
        end = units.group_end(mask, cursor)
        hidden[match.start():end] = " " * (end - match.start())
    # Hyperref's optional target is also an identifier rather than printed text.
    for match in re.finditer(r"\\hyperref\[", mask):
        end = units.group_end(mask, match.end() - 1, "[", "]")
        hidden[match.start():end] = " " * (end - match.start())
    visible = "".join(hidden)
    found = {}
    tokens = {alias for alias in aliases if re.fullmatch(r"[A-Za-z0-9.*-]+", alias)}
    for token in tokens:
        for match in re.finditer(r"(?<![A-Za-z0-9:_])" + re.escape(token) + r"(?![A-Za-z0-9:_])", visible):
            found[(match.start(), token)] = "Manual-tag token appears as literal printed text."
    generic = re.compile(r"(?<![A-Za-z0-9:_])(?:[A-Z][A-Za-z]*\.)+[A-Za-z0-9.-]*\d[A-Za-z0-9.-]*(?![A-Za-z0-9:_])")
    for match in generic.finditer(visible):
        found.setdefault((match.start(), match[0]), "Possible inherited equation/statement number; resolve its actual referent during unit reading.")
    return [Unresolved("literal-reference", text.count("\n", 0, pos) + 1, token, reason)
            for (pos, token), reason in sorted(found.items())]


def main():
    source = units.repairs.read(units.repairs.SOURCE)
    pieces = units.parse_pieces(source)
    prepared = units.fragments(source, pieces)
    print("READ_ONLY_PRESENTATION_HELPER_AUDIT")
    print("Return hook, fonts, counters and bibliography remain root preamble/source work.")
    for spec in units.UNITS:
        if spec.key in {"preamble", "bibliography"}:
            continue
        original = prepared[spec.key]
        headers, header_edits, header_issues = statement_records_to_small_tags(original)
        try:
            candidate, equation_edits, equation_issues, aliases = remove_manual_equation_tags(headers)
        except ValueError as error:
            print("UNIT", spec.key, "HEADER_EDITS", len(header_edits), "EQUATION_EDITS", 0, "UNRESOLVED", 1)
            print("REVIEW", spec.key, 0, "unbalanced-environment", "source", str(error))
            continue
        literals = unresolved_literal_equation_references(candidate, aliases)
        print("UNIT", spec.key, "HEADER_EDITS", len(header_edits), "EQUATION_EDITS", len(equation_edits),
              "UNRESOLVED", len(header_issues) + len(equation_issues) + len(literals))
        for issue in header_issues + equation_issues + literals:
            print("REVIEW", spec.key, issue.line, issue.kind, issue.token, issue.detail)
    print("SOURCE_WRITES 0; CRITERIA_CLOSED 0; PROOF_READING_CREDIT 0")


if __name__ == "__main__":
    main()
