#!/usr/bin/env python3
"""Build and verify the current canonical S6 TeX/Bib Markdown bundle.

The generator is deliberately fail-closed.  It snapshots the documented current
roots, follows their literal TeX/Bib dependencies, embeds every selected source
exactly once, and verifies every embedded byte range against its source.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence


DEFAULT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT_NAME = "S6_CURRENT_FULL_TEX_FOR_AI.md"

PRINCIPAL_ROOTS = (
    "main.tex",
    "original_clean_transcription.tex",
    "workbench.tex",
    "workbench_and_manuscript_overview.tex",
)

# This is the numbered order in supporting_materials/project_documentation/
# PROJECT_README.md under "Shareable companion drafts".
PREPRINT_ROOTS = (
    "s6_spectral_degeneration_preprint.tex",
    "s6_cone_sphere_routes_preprint.tex",
    "s6_compact_link_gaussian_preprint.tex",
    "koide_arithmetic_preprint.tex",
    "s6_erdos_straus_koide_bridge_preprint.tex",
    "s6_higher_rung_su3_gram_cone_preprint.tex",
    "s6_worldline_presymplectic_reduction_preprint.tex",
)

ADDITIONAL_DRAFT_ROOTS = ("s6_koide_es_divisor_extension_audit.tex",
                        "s6_quaternionic_4441_reconciliation.tex",
                        "s6_homogeneous_quantum_confinement.tex",
                        "s6_higher_rung_24d_preprint.tex",
                        "s6_retained_cusp_nonlinear_draft.tex",
                        "s6_interacting_wilson_variation_draft.tex",
                        "s6_wilson_temporal_transfer_draft.tex",
                        "s6_spatial_vacuum_elimination_draft.tex",
                        "s6_adjacent_plaquette_quantum_draft.tex",
                        "s6_magnetic_translation_quantum_draft.tex",
                        "s6_volume_uniform_local_vacuum_draft.tex",
                        "s6_extensive_quantum_blocking_draft.tex",
                        "s6_spatial_continuum_draft.tex",
                        "s6_xi4_heat_transport_draft.tex",
                        "s6_weak_coupling_physical_draft.tex")
ORDERED_ROOTS = PRINCIPAL_ROOTS + PREPRINT_ROOTS + ADDITIONAL_DRAFT_ROOTS
SELECTED_SUFFIXES = {".tex", ".bib"}
FENCE = "~" * 96
BEGIN_TOKEN = "<!-- S6_SOURCE_BEGIN"
END_TOKEN = "<!-- S6_SOURCE_END"


class BundleError(RuntimeError):
    """Fail-closed bundle-generation error."""


@dataclass(frozen=True)
class DependencyReference:
    parent: str
    child: str
    command: str
    argument: str
    line: int


@dataclass(frozen=True)
class DependencySpec:
    position: int
    command: str
    argument: str
    import_directory: str | None = None


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def is_relative_to(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def relative_posix(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def strip_tex_comments(text: str) -> str:
    """Remove TeX comments while preserving newlines and character offsets.

    A percent sign preceded by an even number of consecutive backslashes starts
    a comment.  Removed bytes are replaced by spaces so regex-match offsets and
    line calculations remain stable.
    """

    output: list[str] = []
    for line in text.splitlines(keepends=True):
        body = line
        newline = ""
        if line.endswith("\r\n"):
            body, newline = line[:-2], "\r\n"
        elif line.endswith("\n") or line.endswith("\r"):
            body, newline = line[:-1], line[-1:]

        comment_at: int | None = None
        for index, char in enumerate(body):
            if char != "%":
                continue
            slash_count = 0
            cursor = index - 1
            while cursor >= 0 and body[cursor] == "\\":
                slash_count += 1
                cursor -= 1
            if slash_count % 2 == 0:
                comment_at = index
                break

        if comment_at is None:
            output.append(body + newline)
        else:
            output.append(body[:comment_at] + " " * (len(body) - comment_at) + newline)
    return "".join(output)


IMPORT_RE = re.compile(
    r"\\(?P<command>import|subimport|inputfrom|subinputfrom|includefrom|subincludefrom)"
    r"\s*\{(?P<directory>[^{}]*)\}\s*\{(?P<argument>[^{}]+)\}",
    re.DOTALL,
)
INPUT_RE = re.compile(
    r"\\(?P<command>input|include|InputIfFileExists)"
    r"(?![A-Za-z@])\s*(?:\[[^\]]*\]\s*)?\{(?P<argument>[^{}]+)\}",
    re.DOTALL,
)
INPUT_BARE_RE = re.compile(
    r"\\(?P<command>input)(?![A-Za-z@])\s+(?P<argument>[^\s{}%]+)"
)
BIBLIOGRAPHY_RE = re.compile(
    r"\\(?P<command>bibliography)(?![A-Za-z@])\s*\{(?P<argument>[^{}]+)\}",
    re.DOTALL,
)
ADDBIBRESOURCE_RE = re.compile(
    r"\\(?P<command>addbibresource)(?![A-Za-z@])"
    r"\s*(?:\[[^\]]*\]\s*)?\{(?P<argument>[^{}]+)\}",
    re.DOTALL,
)


def dependency_specs(raw: bytes, rel_path: str) -> list[DependencySpec]:
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise BundleError(f"Source is not valid UTF-8: {rel_path}: {exc}") from exc

    searchable = strip_tex_comments(text)
    matches: list[DependencySpec] = []

    for match in IMPORT_RE.finditer(searchable):
        matches.append(
            DependencySpec(
                position=match.start(),
                command=match.group("command"),
                argument=match.group("argument"),
                import_directory=match.group("directory"),
            )
        )

    for regex in (INPUT_RE, INPUT_BARE_RE, BIBLIOGRAPHY_RE, ADDBIBRESOURCE_RE):
        for match in regex.finditer(searchable):
            matches.append(
                DependencySpec(
                    position=match.start(),
                    command=match.group("command"),
                    argument=match.group("argument"),
                )
            )

    matches.sort(key=lambda item: (item.position, item.command, item.argument))
    return matches


def literal_tokens(spec: DependencySpec, parent: str) -> list[str]:
    if spec.command == "bibliography":
        tokens = [piece.strip() for piece in spec.argument.split(",")]
    else:
        tokens = [spec.argument.strip()]

    cleaned: list[str] = []
    for token in tokens:
        if not token:
            raise BundleError(
                f"Empty dependency argument in {parent}: \\{spec.command}{{{spec.argument}}}"
            )
        # A complete static closure cannot be certified for a dynamically built
        # filename.  Fail rather than silently omitting it.
        if any(character in token for character in ("\\", "#", "$", "{", "}")):
            raise BundleError(
                f"Dynamic or unsupported dependency in {parent}: "
                f"\\{spec.command}{{{spec.argument}}}"
            )
        cleaned.append(token.replace("\\", "/"))
    return cleaned


def candidate_names(token: str, command: str) -> list[str]:
    path = Path(token)
    if command in {"bibliography", "addbibresource"}:
        if path.suffix:
            return [token]
        return [token + ".bib"]
    if path.suffix:
        return [token]
    # TeX first tries the literal filename and then its normal .tex extension.
    return [token, token + ".tex"]


def resolve_dependency(
    project_root: Path,
    parent_path: Path,
    spec: DependencySpec,
    token: str,
) -> Path:
    token_path = Path(token)
    if token_path.is_absolute():
        search_bases = (Path(),)
    elif spec.import_directory is not None:
        import_dir = Path(spec.import_directory.replace("\\", "/"))
        search_bases = (
            project_root / import_dir,
            parent_path.parent / import_dir,
        )
    else:
        # These current roots are compiled from the project root.  Trying
        # the including-file directory too handles ordinary neighbor includes
        # without weakening the containment check.
        search_bases = (project_root, parent_path.parent)

    found: dict[str, Path] = {}
    for name in candidate_names(token, spec.command):
        name_path = Path(name.replace("\\", "/"))
        for base in search_bases:
            candidate = (base / name_path).resolve(strict=False)
            if not is_relative_to(candidate, project_root):
                continue
            if candidate.is_file():
                found[str(candidate).casefold()] = candidate

    if not found:
        raise BundleError(
            f"Unresolved dependency from {relative_posix(parent_path, project_root)}: "
            f"\\{spec.command}{{{spec.argument}}} (literal token {token!r})"
        )
    if len(found) != 1:
        options = ", ".join(str(path) for path in sorted(found.values()))
        raise BundleError(
            f"Ambiguous dependency from {relative_posix(parent_path, project_root)}: "
            f"{token!r} resolved to {options}"
        )

    resolved = next(iter(found.values()))
    if resolved.suffix.lower() not in SELECTED_SUFFIXES:
        raise BundleError(
            f"Dependency is outside the requested .tex/.bib closure: {resolved}"
        )
    return resolved


def validate_documented_roots(project_root: Path) -> list[Path]:
    root_paths = [(project_root / name).resolve(strict=True) for name in ORDERED_ROOTS]
    for path in root_paths:
        if not path.is_file():
            raise BundleError(f"Documented root is not a regular file: {path}")

    actual_top_level_tex = sorted(path.name for path in project_root.glob("*.tex"))
    expected_top_level_tex = sorted(ORDERED_ROOTS)
    if actual_top_level_tex != expected_top_level_tex:
        raise BundleError(
            "Top-level TeX roots changed. Expected "
            f"{expected_top_level_tex}; found {actual_top_level_tex}"
        )

    actual_preprints = sorted(path.name for path in project_root.glob("*_preprint.tex"))
    expected_preprints = sorted(name for name in ORDERED_ROOTS if name.endswith("_preprint.tex"))
    if actual_preprints != expected_preprints:
        raise BundleError(
            "Current preprint roots changed. Expected "
            f"{expected_preprints}; found {actual_preprints}"
        )
    return root_paths


def discover_closure(
    project_root: Path, root_paths: Sequence[Path]
) -> tuple[list[str], dict[str, bytes], list[DependencyReference]]:
    root_rels = [relative_posix(path, project_root) for path in root_paths]
    snapshots: dict[str, bytes] = {rel: path.read_bytes() for rel, path in zip(root_rels, root_paths)}
    dependency_order: list[str] = []
    queue: list[str] = list(root_rels)
    processed: set[str] = set()
    edges: list[DependencyReference] = []

    while queue:
        parent_rel = queue.pop(0)
        if parent_rel in processed:
            continue
        processed.add(parent_rel)
        parent_path = (project_root / parent_rel).resolve(strict=True)
        raw = snapshots[parent_rel]
        searchable = strip_tex_comments(raw.decode("utf-8"))

        for spec in dependency_specs(raw, parent_rel):
            line = searchable.count("\n", 0, spec.position) + 1
            for token in literal_tokens(spec, parent_rel):
                child_path = resolve_dependency(project_root, parent_path, spec, token)
                child_rel = relative_posix(child_path, project_root)
                edges.append(
                    DependencyReference(
                        parent=parent_rel,
                        child=child_rel,
                        command=spec.command,
                        argument=spec.argument,
                        line=line,
                    )
                )
                if child_rel not in snapshots:
                    snapshots[child_rel] = child_path.read_bytes()
                    dependency_order.append(child_rel)
                    queue.append(child_rel)

    selected = root_rels + dependency_order
    if len(selected) != len(set(selected)):
        raise BundleError("Duplicate selected source path after closure discovery")
    casefolded = [path.casefold() for path in selected]
    if len(casefolded) != len(set(casefolded)):
        raise BundleError("Case-fold-colliding selected source paths")

    # Historical files are permitted only if actually reached from a current
    # root.  Since every non-root selected path is created by an edge, this test
    # proves that no historical tree was swept in merely by enumeration.
    edge_children = {edge.child for edge in edges}
    for rel in selected:
        if "supporting_materials/workbench_history/" in rel and rel not in edge_children:
            raise BundleError(f"Unreferenced historical checkpoint selected: {rel}")

    for rel in selected:
        raw = snapshots[rel]
        if not raw.endswith(b"\n"):
            raise BundleError(
                f"Source is not LF-terminated, so an exact fenced block cannot be certified: {rel}"
            )
        for token in (BEGIN_TOKEN.encode("ascii"), END_TOKEN.encode("ascii")):
            if token in raw:
                raise BundleError(f"Reserved bundle marker occurs in source: {rel}")
        if re.search(rb"(?m)^~{96,}", raw):
            raise BundleError(f"Long tilde fence collision in source: {rel}")

    return selected, snapshots, edges


def source_set_sha256(selected: Sequence[str], snapshots: dict[str, bytes]) -> str:
    digest = hashlib.sha256()
    for rel in selected:
        raw = snapshots[rel]
        digest.update(rel.encode("utf-8"))
        digest.update(b"\0")
        digest.update(str(len(raw)).encode("ascii"))
        digest.update(b"\0")
        digest.update(raw)
        digest.update(b"\0")
    return digest.hexdigest()


def first_reference_map(edges: Iterable[DependencyReference]) -> dict[str, DependencyReference]:
    first: dict[str, DependencyReference] = {}
    for edge in edges:
        first.setdefault(edge.child, edge)
    return first


def build_bundle(
    project_root: Path,
    selected: Sequence[str],
    snapshots: dict[str, bytes],
    edges: Sequence[DependencyReference],
) -> tuple[bytes, str]:
    total_bytes = sum(len(snapshots[rel]) for rel in selected)
    set_hash = source_set_sha256(selected, snapshots)
    first_refs = first_reference_map(edges)

    header: list[str] = [
        "# S6 current canonical TeX/Bib source bundle for AI",
        "",
        "This is a byte-preserving Markdown bundle of the current canonical S6 TeX/Bib roots and their complete literal transitive source dependency closure. It is an ingestion artifact only; the mathematical source files remain authoritative.",
        "",
        "## Generated inventory",
        "",
        "- Canonical project root: project directory containing this bundle (all locators below are project-relative)",
        f"- Ordered root count: {len(ORDERED_ROOTS)}",
        f"- Selected source file count: {len(selected)}",
        f"- Dependency file count: {len(selected) - len(ORDERED_ROOTS)}",
        f"- Total original source bytes: {total_bytes}",
        f"- Source-set SHA-256: `{set_hash}`",
        "- Embedded-source verification: `PASS` — every selected path has exactly one source section, and every section's exact bytes and SHA-256 match its source file.",
        "- Selection policy: current roots plus literal transitive `.tex`/`.bib` dependencies only; historical checkpoints are excluded unless reached by such a dependency.",
        "",
        "### Ordered current roots",
        "",
    ]
    for index, rel in enumerate(ORDERED_ROOTS, start=1):
        root_kind = "principal root" if index <= len(PRINCIPAL_ROOTS) else "standalone preprint root"
        header.append(f"{index}. `{rel}` — {root_kind}")

    header.extend(
        [
            "",
            "### Complete selected-source inventory",
            "",
            "| # | Class | Relative path | Bytes | SHA-256 | First dependency edge |",
            "|---:|---|---|---:|---|---|",
        ]
    )

    root_index = {rel: index for index, rel in enumerate(ORDERED_ROOTS, start=1)}
    for index, rel in enumerate(selected, start=1):
        raw = snapshots[rel]
        digest = sha256_bytes(raw)
        if rel in root_index:
            classification = f"root {root_index[rel]}/{len(ORDERED_ROOTS)}"
            edge_description = "—"
        else:
            classification = "dependency"
            edge = first_refs[rel]
            edge_description = (
                f"`{edge.parent}:{edge.line}` via `\\{edge.command}`"
            )
        header.append(
            f"| {index} | {classification} | `{rel}` | {len(raw)} | `{digest}` | {edge_description} |"
        )

    header.extend(
        [
            "",
            "## Embedded sources",
            "",
            "Each block below contains the exact source bytes identified by its heading and SHA-256. The 96-character tilde fence is intentionally longer than any fence-like line in the selected sources.",
            "",
        ]
    )

    parts: list[bytes] = [("\n".join(header) + "\n").encode("utf-8")]
    for index, rel in enumerate(selected, start=1):
        raw = snapshots[rel]
        digest = sha256_bytes(raw)
        if rel in root_index:
            role = f"ordered root {root_index[rel]}/{len(ORDERED_ROOTS)}"
        else:
            edge = first_refs[rel]
            role = (
                f"transitive dependency; first referenced by {edge.parent}:{edge.line} "
                f"via \\{edge.command}"
            )
        language = "bibtex" if rel.lower().endswith(".bib") else "latex"
        preamble = (
            f"### File {index:03d}/{len(selected):03d} — `{rel}`\n\n"
            f"- Role: {role}\n"
            f"- Source bytes: {len(raw)}\n"
            f"- Source SHA-256: `{digest}`\n\n"
            f"<!-- S6_SOURCE_BEGIN path=\"{rel}\" bytes=\"{len(raw)}\" sha256=\"{digest}\" -->\n"
            f"{FENCE}{language}\n"
        ).encode("utf-8")
        postamble = (
            f"{FENCE}\n"
            f"<!-- S6_SOURCE_END path=\"{rel}\" -->\n\n"
        ).encode("utf-8")
        parts.extend((preamble, raw, postamble))

    return b"".join(parts), set_hash


BEGIN_RE = re.compile(
    rb'<!-- S6_SOURCE_BEGIN path="([^"]+)" bytes="([0-9]+)" '
    rb'sha256="([0-9a-f]{64})" -->\n'
)
END_RE = re.compile(rb'<!-- S6_SOURCE_END path="([^"]+)" -->\n')


def verify_bundle(
    bundle: bytes,
    selected: Sequence[str],
    snapshots: dict[str, bytes],
    expected_set_hash: str,
) -> None:
    begin_matches = list(BEGIN_RE.finditer(bundle))
    end_matches = list(END_RE.finditer(bundle))
    if len(begin_matches) != len(selected) or len(end_matches) != len(selected):
        raise BundleError(
            f"Marker count mismatch: {len(begin_matches)} begins, "
            f"{len(end_matches)} ends, {len(selected)} selected"
        )

    observed_paths = [match.group(1).decode("utf-8") for match in begin_matches]
    if observed_paths != list(selected):
        raise BundleError(
            f"Source-section order mismatch. Expected {list(selected)}; found {observed_paths}"
        )
    if len(set(observed_paths)) != len(selected):
        raise BundleError("A selected source section occurs more than once")

    for index, (rel, match) in enumerate(zip(selected, begin_matches), start=1):
        raw = snapshots[rel]
        stated_bytes = int(match.group(2))
        stated_hash = match.group(3).decode("ascii")
        actual_hash = sha256_bytes(raw)
        if stated_bytes != len(raw) or stated_hash != actual_hash:
            raise BundleError(f"Marker metadata mismatch for {rel}")

        language = b"bibtex" if rel.lower().endswith(".bib") else b"latex"
        opening_fence = FENCE.encode("ascii") + language + b"\n"
        opening_start = match.end()
        if bundle[opening_start : opening_start + len(opening_fence)] != opening_fence:
            raise BundleError(f"Opening fence mismatch for {rel}")
        content_start = opening_start + len(opening_fence)
        content_end = content_start + len(raw)
        embedded = bundle[content_start:content_end]
        if embedded != raw or sha256_bytes(embedded) != actual_hash:
            raise BundleError(f"Embedded bytes differ from source: {rel}")

        closing_fence = FENCE.encode("ascii") + b"\n"
        if bundle[content_end : content_end + len(closing_fence)] != closing_fence:
            raise BundleError(f"Closing fence mismatch for {rel}")
        expected_end = f'<!-- S6_SOURCE_END path="{rel}" -->\n'.encode("utf-8")
        end_start = content_end + len(closing_fence)
        if bundle[end_start : end_start + len(expected_end)] != expected_end:
            raise BundleError(f"End marker mismatch for {rel}")

        heading = f"### File {index:03d}/{len(selected):03d} — `{rel}`\n".encode("utf-8")
        if bundle.count(heading) != 1:
            raise BundleError(f"Explicit file heading is not unique for {rel}")

        inventory_fragment = (
            f"| {index} | ".encode("utf-8")
        )
        if inventory_fragment not in bundle:
            raise BundleError(f"Inventory row missing for {rel}")

    if source_set_sha256(selected, snapshots) != expected_set_hash:
        raise BundleError("Source-set SHA-256 changed during in-memory verification")
    if bundle.count(expected_set_hash.encode("ascii")) != 1:
        raise BundleError("Source-set SHA-256 inventory field is missing or duplicated")

    total_bytes = sum(len(snapshots[rel]) for rel in selected)
    required_fields = (
        f"- Ordered root count: {len(ORDERED_ROOTS)}".encode("utf-8"),
        f"- Selected source file count: {len(selected)}".encode("utf-8"),
        f"- Total original source bytes: {total_bytes}".encode("utf-8"),
    )
    for field in required_fields:
        if bundle.count(field) != 1:
            raise BundleError(f"Generated inventory field missing or duplicated: {field!r}")


def assert_snapshot_still_current(project_root: Path, snapshots: dict[str, bytes]) -> None:
    changed = [
        rel
        for rel, original in snapshots.items()
        if (project_root / rel).read_bytes() != original
    ]
    if changed:
        raise BundleError(
            "Source files changed during generation; rerun against a fresh snapshot: "
            + ", ".join(changed)
        )


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_name: str | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as handle:
            temporary_name = handle.name
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_name, path)
        temporary_name = None
    finally:
        if temporary_name is not None:
            try:
                Path(temporary_name).unlink()
            except FileNotFoundError:
                pass


def non_destructive_copy(source: Path, destination_directory: Path) -> tuple[str, Path, str]:
    destination_directory = destination_directory.resolve(strict=True)
    if not destination_directory.is_dir():
        raise BundleError(f"Copy destination is not a directory: {destination_directory}")
    destination = destination_directory / source.name
    source_bytes = source.read_bytes()
    source_hash = sha256_bytes(source_bytes)

    try:
        with destination.open("xb") as handle:
            handle.write(source_bytes)
            handle.flush()
            os.fsync(handle.fileno())
        status = "created"
    except FileExistsError:
        existing = destination.read_bytes()
        if existing != source_bytes:
            return "skipped_existing_different", destination, sha256_bytes(existing)
        status = "already_identical"

    copied_hash = sha256_bytes(destination.read_bytes())
    if copied_hash != source_hash:
        raise BundleError(
            f"Copied bundle hash mismatch: source {source_hash}, destination {copied_hash}"
        )
    return status, destination, copied_hash


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--copy-to", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    project_root = args.root.resolve(strict=True)
    if not project_root.is_dir():
        raise BundleError(f"Canonical root is not a directory: {project_root}")
    output = (
        args.output.resolve(strict=False)
        if args.output is not None
        else project_root / DEFAULT_OUTPUT_NAME
    )
    if output.parent.resolve(strict=True) != project_root:
        raise BundleError(f"Bundle output must be directly in the canonical root: {output}")

    root_paths = validate_documented_roots(project_root)
    selected, snapshots, edges = discover_closure(project_root, root_paths)
    assert_snapshot_still_current(project_root, snapshots)
    bundle, set_hash = build_bundle(project_root, selected, snapshots, edges)
    verify_bundle(bundle, selected, snapshots, set_hash)
    assert_snapshot_still_current(project_root, snapshots)
    atomic_write(output, bundle)

    written = output.read_bytes()
    if written != bundle:
        raise BundleError("On-disk bundle differs from verified in-memory bytes")
    verify_bundle(written, selected, snapshots, set_hash)
    assert_snapshot_still_current(project_root, snapshots)

    copy_status = "not_requested"
    copy_path: str | None = None
    copy_hash: str | None = None
    if args.copy_to is not None:
        copy_status, copied, copy_hash = non_destructive_copy(output, args.copy_to)
        copy_path = str(copied)

    summary = {
        "status": "PASS",
        "canonical_root": str(project_root),
        "output_path": str(output),
        "output_bytes": len(written),
        "output_sha256": sha256_bytes(written),
        "ordered_roots": list(ORDERED_ROOTS),
        "root_count": len(ORDERED_ROOTS),
        "source_file_count": len(selected),
        "dependency_file_count": len(selected) - len(ORDERED_ROOTS),
        "source_total_bytes": sum(len(snapshots[rel]) for rel in selected),
        "source_set_sha256": set_hash,
        "dependency_edge_count": len(edges),
        "selected_sources": list(selected),
        "copy_status": copy_status,
        "copy_path": copy_path,
        "copy_sha256": copy_hash,
    }
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
