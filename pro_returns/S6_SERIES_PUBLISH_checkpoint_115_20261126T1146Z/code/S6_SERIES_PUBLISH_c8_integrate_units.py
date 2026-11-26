"""Extract editable Paper III units and assemble a candidate without central writes.

Default execution reports actual source ranges and a lossless in-memory round
trip. --project-repairs also reports the sizes after currently admitted guards.
--extract writes only editable source fragments after the required admission
gate. --assemble writes one noncanonical candidate from those fragments. No
inventory, manifest, progress update, proof-reading credit or edit receipt is
created. Root retains all new titles, tags, and final-order decisions.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import contextlib
from dataclasses import dataclass
import io
from pathlib import Path
import re

import S6_SERIES_PUBLISH_c8_integrate_repairs as repairs

ROOT = repairs.ROOT
WORK = ROOT / "agents/continuation8_iii_integration/units"
FORMAL = "theorem|proposition|lemma|corollary|definition|remark|computed|cited|statement|auditrecord|test|refuted|question|openq|problem"
ANCHOR_LABEL = re.compile(r"\\hypertarget\{tag-([^}]+)\}\{\}\s*\\label\{([^}]+)\}")
ALL_TARGETS = re.compile(r"\\hypertarget\{([^}]+)\}")


@dataclass(frozen=True)
class Unit:
    key: str
    owner: str
    tags: tuple[str, ...]


def unit(key, owner, tags=""):
    return Unit(key, owner, tuple(tags.split()))


# This is editable source-application code, not a generated unit inventory.
# Section numbers deliberately do not occur in the fragment names or content.
# The root-owned order remains provisional: the observed body chain is
# J5 -> KD -> KC -> KB. Root must put its cyclic homology before framed B.
UNITS = [
    unit("preamble", "root"),
    unit("front_matter", "root"),
    unit("common_conventions", "root"),
    unit("radial_coordinates", "root", "02QB 039Y"),
    unit("quotient_core", "root", "02J3"),
    unit("cyclic_homology", "root", "02K7 02KB 02KC 02KD"),
    unit("framed_class", "root", "02J4 02J5"),
    unit("based_smoothing", "root"),
    unit("base_map", "root", "02J6"),
    unit("extension_homotopy", "root", "02Q8"),
    unit("quotient_maps", "root", "02J8 02J9"),
    unit("named_fibrations", "root", "02JA"),
    unit("cell_presentation", "root", "02JB 02JC"),
    unit("finite_band_homology", "root", "02QE"),
    unit("full_sphere_nullity", "root", "038X 038W"),
    unit("cusp_nullbordism", "root", "038S 03A6"),
    unit("retained_angle", "root", "03AE 03BD 03BC 02J7 03BE"),
    unit("carrier_extension", "root", "02Q7"),
    unit("local_kummer", "root", "02K2 02K3 02K4 02K5 02K6"),
    unit("kummer_extension", "root", "037X 0382 037Y"),
    unit("cyclic_invariants", "root", "02KE 02KF 02KG 02KH 02KI 02K8 02KA 02K9"),
    unit("elliptic_marked_data", "foundations", "02OG 02LK 02LO"),
    unit("elliptic_cohomology", "foundations", "02KU 02L5"),
    unit("elliptic_basic_families", "foundations", "02LR 02LW 02LX 02LY 02LZ"),
    unit("elliptic_finite_multiplicities", "foundations", "02KK 02KL"),
    unit("elliptic_poincare", "foundations", "02KM"),
    unit("elliptic_smooth_logs", "foundations", "02KN 02KO"),
    unit("elliptic_catalogue", "foundations", "02KT 02KX 02KY"),
    unit("elliptic_product_star", "foundations", "02KP 02KQ"),
    unit("elliptic_additive_profiles", "later", "02KR 02KS 02KV 02KW"),
    unit("elliptic_sphere_outputs", "later", "02KZ 02L0 02L1 02L2 02L3"),
    unit("finite_primitive_caps", "foundations", "02L4 02L6"),
    unit("original_cap_homology", "foundations", "02L7 02L8 02L9"),
    unit("positive_engel_weights", "foundations", "02LA"),
    unit("weighted_natural_profiles", "foundations", "02LD"),
    unit("weighted_odd_cap_kernels", "foundations", "02LH"),
    unit("weighted_integral_homology", "foundations", "02LI"),
    unit("whole_fibre_initial_pairs", "weighted", "02LN"),
    unit("canonical_star_logs", "weighted", "02LQ"),
    unit("vertical_corrections", "weighted", "02LS"),
    unit("invariant_chern_caps", "weighted", "02LT"),
    unit("height_integral_pairs", "weighted", "02LU"),
    unit("minimal_primary_types", "weighted", "02LB 02LC 02LE"),
    unit("three_primary_types", "weighted", "02LF 02LJ"),
    unit("residual_even_types", "weighted", "02LL 02LM"),
    unit("weighted_engel_types", "weighted", "02LP"),
    unit("weighted_os45", "weighted", "02LV"),
    unit("os49_construction", "later", "02S2 02S3 02S4 02S5"),
    unit("os49_graph_caps", "later", "02S8 02S9 02SA 02SB"),
    unit("conifold_constructions", "later", "02M0 02M2 02M1 02M3 02MK"),
    unit("regular_quotients", "root", "039U"),
    unit("sphere_smash_pairing", "root", "038V 038T"),
    unit("carrier_wedge_recognition", "root", "02QC"),
    unit("further_cusp_carriers", "later", "0370 035X 0365 036A 037N 036W 0374 0375 036J 035Z 036E 036V 036Z 037K 036O 037M 036N"),
    unit("fixed_target_metrics", "later", "03DG 03D6 03DC 03DH 03DF 037J"),
    unit("limits_and_open_points", "later", "02LG"),
    unit("bibliography", "root"),
]
BY_KEY = {u.key: u for u in UNITS}
BY_TAG = {tag: u for u in UNITS for tag in u.tags}
if sum(len(u.tags) for u in UNITS) != len(BY_TAG):
    raise ValueError("A statement has two editing owners")


def group_end(text: str, start: int, opening="{", closing="}") -> int:
    """Return the index after one balanced TeX group, respecting escapes."""
    if start >= len(text) or text[start] != opening:
        raise ValueError(f"Expected {opening!r} at character {start}")
    depth = 1
    cursor = start + 1
    while cursor < len(text):
        if text[cursor] == "\\":
            cursor += 2
            continue
        if text[cursor] == opening:
            depth += 1
        elif text[cursor] == closing:
            depth -= 1
            if depth == 0:
                return cursor + 1
        cursor += 1
    raise ValueError("Unclosed TeX group")


@dataclass
class Piece:
    key: str
    start: int
    end: int
    kind: str
    tag: str = ""
    label: str = ""
    unit_key: str = ""


def parse_pieces(text: str, extra_owners=None) -> list[Piece]:
    begin = text.index(r"\begin{document}")
    convention_label = text.index(r"\label{sec:III:conventions}", begin)
    body = text.rfind(r"\section{", begin, convention_label)
    if body < 0:
        raise ValueError("The permanent convention label has no preceding section")
    owners = dict(BY_TAG)
    for tag, spec in (extra_owners or {}).items():
        if tag in owners and owners[tag].key != spec.key:
            raise ValueError(f"Conflicting current statement owner: {tag}")
        owners[tag] = spec
    bibliography = text.index(r"\begin{thebibliography}", body)
    boundaries = {
        0: Piece("preamble", 0, begin, "fixed", unit_key="preamble"),
        begin: Piece("front_matter", begin, body, "fixed", unit_key="front_matter"),
        bibliography: Piece("bibliography", bibliography, len(text), "fixed", unit_key="bibliography"),
    }
    headings = re.compile(r"(?m)^\\(?:part|section|subsection)\*?(?:\[[^\n]*\])?\{")
    for n, match in enumerate(headings.finditer(text, body, bibliography), 1):
        end = group_end(text, match.end() - 1)
        title = text[match.end():end - 1]
        key = "heading:" + title
        boundaries[match.start()] = Piece(key, match.start(), 0, "heading")
    declarations = re.compile(r"\\begin\{(" + FORMAL + r")\}|\\paragraph\*?\{")
    environment_changes = list(re.compile(r"\\(begin|end)\{([^}]+)\}").finditer(text, body, bibliography))
    environment_cursor = 0
    environment_stack = []
    for match in declarations.finditer(text, body, bibliography):
        while (environment_cursor < len(environment_changes)
               and environment_changes[environment_cursor].start() < match.start()):
            change = environment_changes[environment_cursor]
            if change[1] == "begin":
                environment_stack.append(change[2])
            elif environment_stack and environment_stack[-1] == change[2]:
                environment_stack.pop()
            else:
                raise ValueError("Unbalanced source environment at a unit boundary")
            environment_cursor += 1
        if "proof" in environment_stack:
            # Tagged proof steps retain their enclosing proof and editing owner.
            # They are not separate extractable statements or publication units.
            continue
        cursor = match.end()
        if match[1]:
            while cursor < len(text) and text[cursor].isspace():
                cursor += 1
            if text[cursor:cursor + 1] == "[":
                cursor = group_end(text, cursor, "[", "]")
        else:
            cursor = group_end(text, cursor - 1)
        while cursor < len(text) and text[cursor].isspace():
            cursor += 1
        identity = ANCHOR_LABEL.match(text, cursor)
        if not identity:
            # An untagged local substatement remains in its containing proof.
            continue
        tag, label = identity.groups()
        if tag not in owners:
            raise ValueError(f"Unassigned permanent statement: {tag} / {label}")
        boundaries[match.start()] = Piece("statement:" + tag, match.start(), 0,
                                          "statement", tag, label, owners[tag].key)
    pieces = sorted(boundaries.values(), key=lambda p: p.start)
    keys = [p.key for p in pieces]
    if len(keys) != len(set(keys)):
        raise ValueError("Duplicate extraction boundary identity")
    for n, piece in enumerate(pieces):
        piece.end = pieces[n + 1].start if n + 1 < len(pieces) else len(text)
        if piece.kind != "heading":
            continue
        if piece.start == body:
            piece.unit_key = "common_conventions"
        else:
            following = next((p for p in pieces[n + 1:] if p.kind == "statement"), None)
            if following is None:
                raise ValueError(f"Heading without a following owned statement: {piece.key}")
            piece.unit_key = following.unit_key
    present = {p.tag for p in pieces if p.tag}
    if not set(BY_TAG).issubset(present):
        raise ValueError(f"Statement boundary mismatch: missing {sorted(set(BY_TAG) - present)}")
    return pieces


def unit_pieces(pieces: list[Piece], spec: Unit) -> list[Piece]:
    owned = [p for p in pieces if p.unit_key == spec.key]
    scaffolding = [p for p in owned if p.kind != "statement"]
    statements = {p.tag: p for p in owned if p.kind == "statement"}
    return scaffolding + [statements[tag] for tag in spec.tags]


def fragments(text, pieces):
    return {u.key: "".join(text[p.start:p.end] for p in unit_pieces(pieces, u)) for u in UNITS}


def range_text(text: str, selected: list[Piece]) -> str:
    ranges = []
    for p in sorted(selected, key=lambda p: p.start):
        if ranges and p.start == ranges[-1][1]:
            ranges[-1] = (ranges[-1][0], p.end)
        else:
            ranges.append((p.start, p.end))
    return ",".join(f"{text.count(chr(10), 0, a) + 1}-{text.count(chr(10), 0, b - 1) + 1}" for a, b in ranges)


def check_permanent_identifiers(original, candidate, allowed_labels=(), allowed_targets=()):
    for name, regex, allowed in (("labels", repairs.LABEL, set(allowed_labels)),
                                 ("hypertargets", ALL_TARGETS, set(allowed_targets))):
        old, new = Counter(regex.findall(original)), Counter(regex.findall(candidate))
        lost = old - new
        unauthorized = {key: count for key, count in (new - old).items() if key not in allowed}
        duplicate_new = {key: new[key] for key in allowed if new[key] > max(1, old[key])}
        if lost or unauthorized or duplicate_new:
            raise ValueError(f"{name}: lost={dict(lost)}, unauthorized={unauthorized}, new duplicates={duplicate_new}")


def report(original, pieces, projected=None, projected_pieces=None):
    joined = "".join(original[p.start:p.end] for p in pieces)
    if joined != original:
        raise ValueError("Original-order source round trip changed text")
    candidate = "".join(fragments(original, pieces)[u.key] for u in UNITS)
    check_permanent_identifiers(original, candidate)
    print("ORIGINAL_ORDER_ROUND_TRIP exact text equality")
    print("PROPOSED_UNIT_ORDER_IDENTIFIERS exact label and all-hypertarget multiset equality")
    print("ROOT_ORDER_PENDING J5 -> KD -> KC -> KB; cyclic homology before framed class")
    print("SCOPE_RELOCATIONS_PENDING KY input table; LD/LH local maps; closing scope remarks; A-C overlap")
    print("OWNER | UNIT | ORIGINAL SOURCE LINES | ORIGINAL LINE COUNT | PROJECTED LINE COUNT | STATEMENT IDS")
    counts = defaultdict(lambda: [0, 0])
    for spec in UNITS:
        chosen = unit_pieces(pieces, spec)
        old_n = sum(original[p.start:p.end].count("\n") for p in chosen)
        new_n = old_n
        if projected is not None:
            new_n = sum(projected[p.start:p.end].count("\n") for p in unit_pieces(projected_pieces, spec))
        counts[spec.owner][0] += old_n
        counts[spec.owner][1] += new_n
        identities = "; ".join(p.tag + ":" + p.label for p in chosen if p.tag) or "scaffolding"
        print(" | ".join((spec.owner, spec.key, range_text(original, chosen), str(old_n), str(new_n), identities)))
    for owner, (old_n, new_n) in counts.items():
        print("GROUP_LINES", owner, old_n, new_n)
    print("PUBLICATION_CRITERIA_CLOSED", 0)
    print("PROOF_READING_CREDIT", 0)
    print("CANONICAL_AND_CENTRAL_RECORD_WRITES", 0)


def admission_gate():
    rows = repairs.table(repairs.PROGRESS)
    if any(r["status"] != "done" for r in rows):
        raise ValueError("Unit extraction/assembly awaits root's completed required-check admission")
    # Actual extraction starts only from the integrated source, which contains
    # LT's new equation labels. No old guard is rerun on an already edited source.
    source = repairs.read(repairs.SOURCE)
    if r"\label{maps:eq:IC_local_43b}" not in source:
        raise ValueError("Extract the actually integrated manuscript after root applies the packets")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-repairs", action="store_true")
    parser.add_argument("--extra-packet", action="append", default=[])
    parser.add_argument("--extract", action="store_true")
    parser.add_argument("--assemble", action="store_true")
    parser.add_argument("--allow-new-label", action="append", default=[])
    parser.add_argument("--allow-new-target", action="append", default=[])
    args = parser.parse_args()
    if args.extract and args.assemble:
        raise ValueError("Extraction and candidate assembly are separate actions")
    source = repairs.read(repairs.SOURCE)
    if args.assemble:
        admission_gate()
        candidate = "".join(repairs.read(WORK / u.owner / (u.key + ".tex")) for u in UNITS)
        check_permanent_identifiers(source, candidate, args.allow_new_label, args.allow_new_target)
        path = WORK.parent / "S6_SERIES_PUBLISH_III_units_candidate.tex"
        path.write_text(candidate, encoding="utf-8", newline="\n")
        print("NONCANONICAL_CANDIDATE_WRITTEN", repairs.relative(path))
        print("Existing labels and targets compared directly against the current canonical source.")
        print("SEMANTIC_UNIT_AND_WHOLE_PROOF_REVIEW_REQUIRED; no criterion closure")
        return
    pieces = parse_pieces(source)
    projected = projected_pieces = None
    if args.project_repairs:
        extras = dict(repairs.EXTRA_ADMITTED)
        for item in args.extra_packet:
            tag, folder = item.split("=", 1)
            extras[tag] = folder
        with contextlib.redirect_stdout(io.StringIO()):
            _, packets, edits, _ = repairs.collect(source, extras)
            projected, _ = repairs.simulate(source, packets, edits)
        projected_pieces = parse_pieces(projected)
    report(source, pieces, projected, projected_pieces)
    if args.extract:
        admission_gate()
        prepared = fragments(source, pieces)
        paths = {u.key: WORK / u.owner / (u.key + ".tex") for u in UNITS}
        existing = [str(path) for path in paths.values() if path.exists()]
        if existing:
            raise ValueError("Refusing to overwrite existing editable unit fragments: " + ", ".join(existing))
        for key, path in paths.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(prepared[key], encoding="utf-8", newline="\n")
        print("EDITABLE_SOURCE_UNITS_WRITTEN", len(paths))


if __name__ == "__main__":
    main()
