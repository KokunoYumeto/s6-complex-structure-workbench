#!/usr/bin/env python3
"""Build and verify a workbench-only, byte-preserving TeX/Bib Markdown bundle."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import tempfile
from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence


DEFAULT_PROJECT_ROOT = Path(
    r"C:\Users\user\Documents\math\output\s6_consolidated_canonical_2026-08-26"
)
ROOT_RELATIVE_PATH = "workbench.tex"
DEFAULT_OUTPUT_NAME = "S6_WORKBENCH_FULL_TEX_FOR_AI.md"
SELECTED_SUFFIXES = {".tex", ".bib"}
FENCE = "~" * 128
BEGIN_TOKEN = "<!-- S6_WORKBENCH_SOURCE_BEGIN"
END_TOKEN = "<!-- S6_WORKBENCH_SOURCE_END"


class BundleError(RuntimeError):
    """Raised whenever the closure or byte-preservation proof cannot be certified."""


@dataclass(frozen=True)
class DependencySpec:
    position: int
    command: str
    argument: str
    import_directory: str | None = None


@dataclass(frozen=True)
class DependencyEdge:
    parent: str
    line: int
    command: str
    argument: str
    child: str


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
BARE_INPUT_RE = re.compile(
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
BEGIN_RE = re.compile(
    rb'<!-- S6_WORKBENCH_SOURCE_BEGIN path="([^"]+)" bytes="([0-9]+)" '
    rb'sha256="([0-9a-f]{64})" -->\n'
)
END_RE = re.compile(rb'<!-- S6_WORKBENCH_SOURCE_END path="([^"]+)" -->\n')


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def relative_posix(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def is_inside(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def strip_tex_comments(text: str) -> str:
    """Replace TeX comments with spaces while preserving offsets and line numbers."""

    output: list[str] = []
    for line in text.splitlines(keepends=True):
        if line.endswith("\r\n"):
            body, newline = line[:-2], "\r\n"
        elif line.endswith("\n") or line.endswith("\r"):
            body, newline = line[:-1], line[-1:]
        else:
            body, newline = line, ""

        comment_at: int | None = None
        for index, character in enumerate(body):
            if character != "%":
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


def parse_specs(raw: bytes, relative_path: str) -> tuple[str, list[DependencySpec]]:
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise BundleError(f"Source is not valid UTF-8: {relative_path}: {exc}") from exc
    searchable = strip_tex_comments(text)
    specs: list[DependencySpec] = []
    for match in IMPORT_RE.finditer(searchable):
        specs.append(
            DependencySpec(
                position=match.start(),
                command=match.group("command"),
                argument=match.group("argument"),
                import_directory=match.group("directory"),
            )
        )
    for regex in (INPUT_RE, BARE_INPUT_RE, BIBLIOGRAPHY_RE, ADDBIBRESOURCE_RE):
        for match in regex.finditer(searchable):
            specs.append(
                DependencySpec(
                    position=match.start(),
                    command=match.group("command"),
                    argument=match.group("argument"),
                )
            )
    specs.sort(key=lambda item: (item.position, item.command, item.argument))
    return searchable, specs


def literal_tokens(spec: DependencySpec, parent: str) -> list[str]:
    tokens = (
        [piece.strip() for piece in spec.argument.split(",")]
        if spec.command == "bibliography"
        else [spec.argument.strip()]
    )
    for token in tokens:
        if not token:
            raise BundleError(f"Empty dependency argument in {parent}")
        if any(character in token for character in ("\\", "#", "$", "{", "}")):
            raise BundleError(
                f"Dynamic or unsupported dependency in {parent}: "
                f"\\{spec.command}{{{spec.argument}}}"
            )
    return [token.replace("\\", "/") for token in tokens]


def candidate_names(token: str, command: str) -> tuple[str, ...]:
    token_path = Path(token)
    if command in {"bibliography", "addbibresource"}:
        return (token,) if token_path.suffix else (token + ".bib",)
    return (token,) if token_path.suffix else (token, token + ".tex")


def resolve_dependency(
    project_root: Path,
    parent_path: Path,
    spec: DependencySpec,
    token: str,
) -> Path:
    token_path = Path(token)
    if token_path.is_absolute():
        bases = (Path(),)
    elif spec.import_directory is not None:
        import_directory = Path(spec.import_directory.replace("\\", "/"))
        bases = (project_root / import_directory, parent_path.parent / import_directory)
    else:
        # The canonical workbench is compiled with the project root as cwd.
        # The parent directory fallback covers conventional neighbor includes.
        bases = (project_root, parent_path.parent)

    found: dict[str, Path] = {}
    for name in candidate_names(token, spec.command):
        for base in bases:
            candidate = (base / Path(name)).resolve(strict=False)
            if is_inside(candidate, project_root) and candidate.is_file():
                found[str(candidate).casefold()] = candidate
    if not found:
        raise BundleError(
            f"Unresolved dependency from {relative_posix(parent_path, project_root)}: "
            f"\\{spec.command}{{{spec.argument}}} (token {token!r})"
        )
    if len(found) != 1:
        raise BundleError(
            f"Ambiguous dependency from {relative_posix(parent_path, project_root)}: "
            + ", ".join(str(path) for path in sorted(found.values()))
        )
    resolved = next(iter(found.values()))
    if resolved.suffix.lower() not in SELECTED_SUFFIXES:
        raise BundleError(f"Dependency outside requested .tex/.bib closure: {resolved}")
    return resolved


def discover_closure(
    project_root: Path,
) -> tuple[list[str], dict[str, bytes], list[DependencyEdge]]:
    root_path = (project_root / ROOT_RELATIVE_PATH).resolve(strict=True)
    if not root_path.is_file():
        raise BundleError(f"Missing workbench root: {root_path}")

    selected: list[str] = [ROOT_RELATIVE_PATH]
    snapshots: dict[str, bytes] = {ROOT_RELATIVE_PATH: root_path.read_bytes()}
    queue: deque[str] = deque([ROOT_RELATIVE_PATH])
    processed: set[str] = set()
    edges: list[DependencyEdge] = []

    while queue:
        parent = queue.popleft()
        if parent in processed:
            continue
        processed.add(parent)
        parent_path = (project_root / parent).resolve(strict=True)
        searchable, specs = parse_specs(snapshots[parent], parent)
        for spec in specs:
            line = searchable.count("\n", 0, spec.position) + 1
            for token in literal_tokens(spec, parent):
                child_path = resolve_dependency(project_root, parent_path, spec, token)
                child = relative_posix(child_path, project_root)
                edges.append(
                    DependencyEdge(
                        parent=parent,
                        line=line,
                        command=spec.command,
                        argument=spec.argument,
                        child=child,
                    )
                )
                if child not in snapshots:
                    snapshots[child] = child_path.read_bytes()
                    selected.append(child)
                    queue.append(child)

    if len(selected) != len(set(selected)):
        raise BundleError("Duplicate selected paths after closure discovery")
    if len({path.casefold() for path in selected}) != len(selected):
        raise BundleError("Case-fold-colliding selected paths")

    edge_children = {edge.child for edge in edges}
    for path in selected[1:]:
        if path not in edge_children:
            raise BundleError(f"Selected dependency has no incoming edge: {path}")
    for forbidden_root in (
        "main.tex",
        "original_clean_transcription.tex",
        "workbench_and_manuscript_overview.tex",
    ):
        if forbidden_root in selected and forbidden_root not in edge_children:
            raise BundleError(f"Unreferenced non-workbench root selected: {forbidden_root}")
    for path in selected:
        raw = snapshots[path]
        if not raw.endswith((b"\n", b"\r")):
            raise BundleError(f"Source lacks a terminating newline: {path}")
        if BEGIN_TOKEN.encode("ascii") in raw or END_TOKEN.encode("ascii") in raw:
            raise BundleError(f"Reserved bundle marker occurs in source: {path}")
        if re.search(rb"(?m)^~{128,}", raw):
            raise BundleError(f"128-character tilde fence collision in source: {path}")

    return selected, snapshots, edges


def source_set_hash(selected: Sequence[str], snapshots: dict[str, bytes]) -> str:
    digest = hashlib.sha256()
    for path in selected:
        raw = snapshots[path]
        digest.update(path.encode("utf-8"))
        digest.update(b"\0")
        digest.update(str(len(raw)).encode("ascii"))
        digest.update(b"\0")
        digest.update(raw)
        digest.update(b"\0")
    return digest.hexdigest()


def build_bundle(
    project_root: Path,
    selected: Sequence[str],
    snapshots: dict[str, bytes],
    edges: Sequence[DependencyEdge],
) -> tuple[bytes, str]:
    set_hash = source_set_hash(selected, snapshots)
    total_bytes = sum(len(snapshots[path]) for path in selected)
    incoming: dict[str, DependencyEdge] = {}
    for edge in edges:
        incoming.setdefault(edge.child, edge)

    header = [
        "# S6 workbench — complete canonical TeX/Bib source bundle for AI",
        "",
        "This ingestion artifact contains only `workbench.tex` and its complete literal transitive local `.tex`/`.bib` dependency closure. It intentionally excludes the annotated manuscript, clean transcription, overview, and standalone draft roots unless the workbench itself depends on them. The original project files remain authoritative.",
        "",
        "## Bundle identity",
        "",
        "- Canonical project root: project directory containing this bundle (all locators below are project-relative)",
        f"- Root: `{ROOT_RELATIVE_PATH}`",
        "- Closure policy: breadth-first resolution of literal `\\input`, `\\include`, import-family, `\\bibliography`, and `\\addbibresource` references after TeX-comment removal.",
        f"- Root count: 1",
        f"- Dependency count: {len(selected) - 1}",
        f"- Selected source count: {len(selected)}",
        f"- Dependency-edge count: {len(edges)}",
        f"- Total embedded source bytes: {total_bytes}",
        f"- Source-set SHA-256: `{set_hash}`",
        "- Source-set hash framing: for each selected file in displayed order, UTF-8 relative path, NUL, ASCII byte count, NUL, exact source bytes, NUL; then SHA-256 over the concatenation.",
        "- Verification: `PASS` — one begin marker and one end marker per selected path; exact embedded byte equality and SHA-256 equality for every source; post-write source-stability check.",
        "",
        "## Root inventory",
        "",
        "| # | Project-relative path | Bytes | SHA-256 |",
        "|---:|---|---:|---|",
        f"| 1 | `{ROOT_RELATIVE_PATH}` | {len(snapshots[ROOT_RELATIVE_PATH])} | `{sha256_bytes(snapshots[ROOT_RELATIVE_PATH])}` |",
        "",
        "## Dependency inventory",
        "",
        "| # | Project-relative path | Bytes | SHA-256 | First incoming edge |",
        "|---:|---|---:|---|---|",
    ]
    for index, path in enumerate(selected[1:], start=1):
        raw = snapshots[path]
        edge = incoming[path]
        header.append(
            f"| {index} | `{path}` | {len(raw)} | `{sha256_bytes(raw)}` | "
            f"`{edge.parent}:{edge.line}` via `\\{edge.command}` |"
        )

    header.extend(
        [
            "",
            "## Complete dependency-edge inventory",
            "",
            "Edges are listed in closure-discovery order. Repeated references are retained as distinct edges even when they target an already selected file.",
            "",
            "| # | Parent and line | TeX command | Literal argument | Resolved project-relative child |",
            "|---:|---|---|---|---|",
        ]
    )
    for index, edge in enumerate(edges, start=1):
        escaped_argument = edge.argument.replace("|", "\\|").replace("`", "\\`")
        header.append(
            f"| {index} | `{edge.parent}:{edge.line}` | `\\{edge.command}` | "
            f"`{escaped_argument}` | `{edge.child}` |"
        )

    header.extend(
        [
            "",
            "## Embedded sources",
            "",
            "Each project-relative heading is followed by one 128-character tilde-fenced block containing the exact bytes of that source file.",
            "",
        ]
    )

    parts: list[bytes] = [("\n".join(header) + "\n").encode("utf-8")]
    for index, path in enumerate(selected, start=1):
        raw = snapshots[path]
        digest = sha256_bytes(raw)
        role = "root" if index == 1 else "transitive dependency"
        language = "bibtex" if path.lower().endswith(".bib") else "latex"
        preamble = (
            f"### Source {index:03d}/{len(selected):03d} — `{path}`\n\n"
            f"- Role: {role}\n"
            f"- Bytes: {len(raw)}\n"
            f"- SHA-256: `{digest}`\n\n"
            f'<!-- S6_WORKBENCH_SOURCE_BEGIN path="{path}" bytes="{len(raw)}" sha256="{digest}" -->\n'
            f"{FENCE}{language}\n"
        ).encode("utf-8")
        postamble = (
            f"{FENCE}\n"
            f'<!-- S6_WORKBENCH_SOURCE_END path="{path}" -->\n\n'
        ).encode("utf-8")
        parts.extend((preamble, raw, postamble))
    return b"".join(parts), set_hash


def verify_bundle(
    bundle: bytes,
    selected: Sequence[str],
    snapshots: dict[str, bytes],
    expected_set_hash: str,
) -> dict[str, int | str]:
    begins = list(BEGIN_RE.finditer(bundle))
    ends = list(END_RE.finditer(bundle))
    if len(begins) != len(selected) or len(ends) != len(selected):
        raise BundleError(
            f"Marker count mismatch: begins={len(begins)}, ends={len(ends)}, "
            f"selected={len(selected)}"
        )
    begin_paths = [match.group(1).decode("utf-8") for match in begins]
    end_paths = [match.group(1).decode("utf-8") for match in ends]
    if begin_paths != list(selected) or end_paths != list(selected):
        raise BundleError("Marker paths or order differ from selected closure")
    if len(set(begin_paths)) != len(selected):
        raise BundleError("A source marker path occurs more than once")

    for index, (path, match) in enumerate(zip(selected, begins), start=1):
        raw = snapshots[path]
        digest = sha256_bytes(raw)
        if int(match.group(2)) != len(raw) or match.group(3).decode("ascii") != digest:
            raise BundleError(f"Begin-marker metadata mismatch: {path}")
        language = b"bibtex" if path.lower().endswith(".bib") else b"latex"
        opening = FENCE.encode("ascii") + language + b"\n"
        content_start = match.end() + len(opening)
        if bundle[match.end():content_start] != opening:
            raise BundleError(f"Opening fence mismatch: {path}")
        content_end = content_start + len(raw)
        embedded = bundle[content_start:content_end]
        if embedded != raw or sha256_bytes(embedded) != digest:
            raise BundleError(f"Embedded bytes differ from current source: {path}")
        closing = FENCE.encode("ascii") + b"\n"
        if bundle[content_end:content_end + len(closing)] != closing:
            raise BundleError(f"Closing fence mismatch: {path}")
        end_marker = f'<!-- S6_WORKBENCH_SOURCE_END path="{path}" -->\n'.encode("utf-8")
        end_start = content_end + len(closing)
        if bundle[end_start:end_start + len(end_marker)] != end_marker:
            raise BundleError(f"End marker mismatch: {path}")
        heading = f"### Source {index:03d}/{len(selected):03d} — `{path}`\n".encode("utf-8")
        if bundle.count(heading) != 1:
            raise BundleError(f"Project-relative source heading is not unique: {path}")

    if source_set_hash(selected, snapshots) != expected_set_hash:
        raise BundleError("Source-set hash changed during verification")
    if bundle.count(expected_set_hash.encode("ascii")) != 1:
        raise BundleError("Source-set hash is absent or duplicated in bundle metadata")
    return {
        "begin_marker_count": len(begins),
        "end_marker_count": len(ends),
        "embedded_byte_equality_count": len(selected),
        "embedded_sha256_equality_count": len(selected),
    }


def assert_sources_unchanged(project_root: Path, snapshots: dict[str, bytes]) -> None:
    changed = [
        path
        for path, original in snapshots.items()
        if (project_root / path).read_bytes() != original
    ]
    if changed:
        raise BundleError("Sources changed during generation: " + ", ".join(changed))


def atomic_write(output_path: Path, data: bytes) -> None:
    temporary: str | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb",
            dir=output_path.parent,
            prefix=f".{output_path.name}.",
            suffix=".tmp",
            delete=False,
        ) as handle:
            temporary = handle.name
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, output_path)
        temporary = None
    finally:
        if temporary is not None:
            try:
                Path(temporary).unlink()
            except FileNotFoundError:
                pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=DEFAULT_PROJECT_ROOT)
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    project_root = args.project_root.resolve(strict=True)
    if not project_root.is_dir():
        raise BundleError(f"Not a project directory: {project_root}")
    output_path = (
        args.output.resolve(strict=False)
        if args.output is not None
        else project_root / DEFAULT_OUTPUT_NAME
    )
    if output_path.parent.resolve(strict=True) != project_root:
        raise BundleError("Output must be written directly in the canonical project root")

    selected, snapshots, edges = discover_closure(project_root)
    assert_sources_unchanged(project_root, snapshots)
    bundle, set_hash = build_bundle(project_root, selected, snapshots, edges)
    in_memory_verification = verify_bundle(bundle, selected, snapshots, set_hash)
    assert_sources_unchanged(project_root, snapshots)
    atomic_write(output_path, bundle)
    written = output_path.read_bytes()
    if written != bundle:
        raise BundleError("Written Markdown bytes differ from verified in-memory bundle")
    on_disk_verification = verify_bundle(written, selected, snapshots, set_hash)
    assert_sources_unchanged(project_root, snapshots)

    summary = {
        "status": "PASS",
        "canonical_project_root": str(project_root),
        "output_path": str(output_path),
        "output_bytes": len(written),
        "output_sha256": sha256_bytes(written),
        "root": ROOT_RELATIVE_PATH,
        "root_count": 1,
        "dependency_count": len(selected) - 1,
        "selected_source_count": len(selected),
        "dependency_edge_count": len(edges),
        "embedded_source_bytes": sum(len(snapshots[path]) for path in selected),
        "source_set_sha256": set_hash,
        "selected_sources": list(selected),
        "dependency_edges": [edge.__dict__ for edge in edges],
        "in_memory_verification": in_memory_verification,
        "on_disk_verification": on_disk_verification,
    }
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
