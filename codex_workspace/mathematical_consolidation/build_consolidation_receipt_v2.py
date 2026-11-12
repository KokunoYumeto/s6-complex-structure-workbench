from __future__ import annotations

import gzip
import hashlib
import json
import pathlib
import sqlite3


ROOT = pathlib.Path(__file__).resolve().parent
MATH_ROOT = ROOT.parents[2]
OUTPUT = ROOT / "CONSOLIDATION_RECEIPT_V2.json"

PRINCIPAL_FILES = [
    ROOT / "README.md",
    ROOT / "MASTER_MAP.md",
    ROOT / "MATHEMATICAL_NOTE.md",
    ROOT / "TOMOGRAPHY_DESIGN.md",
    ROOT / "CONSOLIDATION.tex",
    ROOT / "CLAIM_LEDGER.md",
    ROOT / "AUDIT_LIMITATIONS.md",
    ROOT / "UNMINED_QUEUE.md",
    ROOT / "CATALOGUE_GUIDE.md",
    ROOT / "BUILD_STATUS.md",
    ROOT / "REVIEW_2026-09-30.md",
    ROOT / "WORKFLOW.md",
    ROOT / "MATHEMATICAL_CHECKS_V2.json",
    ROOT / "TOMOGRAPHY_DESIGN_MATRICES.json",
    ROOT / "CATALOGUE_V2_RECEIPT.json",
    ROOT / "DIRECT_TEXT_MAPPING_AUDIT.json",
    ROOT / "UNCLASSIFIED_TRANCHE_2026-09-30.json",
    ROOT / "UNCLASSIFIED_TRANCHE_2026-09-30.md",
    ROOT / "ARCHIVE_MEMBER_COVERAGE_V2.jsonl.gz",
    ROOT / "CORPUS_CATALOGUE_V2.sqlite",
    ROOT / "literature" / "SOURCE_ACQUISITION.json",
    ROOT.parent / "ledgers" / "actual_source_readings.jsonl",
    MATH_ROOT / "research_index" / "RESULTS_BULLETIN_2026-09-30.md",
    MATH_ROOT
    / "work"
    / "s6_main_01a0ea06-5fdc-7a60-97f3-4f4347467d95"
    / "LOGBOOK.md",
    MATH_ROOT
    / "work"
    / "s6_main_01a0ea06-5fdc-7a60-97f3-4f4347467d95"
    / "CONTINUITY.md",
    ROOT / "build_catalogue_v2.py",
    ROOT / "repair_catalogue_v2_direct_text.py",
    ROOT / "classify_unclassified_tranche_2026_09_30.py",
    ROOT / "verify_consolidation_v2.py",
    ROOT / "prepare_note.py",
]


def sha256_file(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def relative_path(path: pathlib.Path) -> str:
    return path.relative_to(MATH_ROOT).as_posix()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    for path in PRINCIPAL_FILES:
        require(path.is_file(), f"Missing required artifact: {path}")

    catalogue_receipt = json.loads(
        (ROOT / "CATALOGUE_V2_RECEIPT.json").read_text(encoding="utf-8")
    )
    mathematical_receipt = json.loads(
        (ROOT / "MATHEMATICAL_CHECKS_V2.json").read_text(encoding="utf-8")
    )
    tomography_receipt = json.loads(
        (ROOT / "TOMOGRAPHY_DESIGN_MATRICES.json").read_text(encoding="utf-8")
    )
    tranche_receipt = json.loads(
        (ROOT / "UNCLASSIFIED_TRANCHE_2026-09-30.json").read_text(
            encoding="utf-8"
        )
    )

    database_path = ROOT / "CORPUS_CATALOGUE_V2.sqlite"
    database_sha = sha256_file(database_path)
    require(
        database_sha == catalogue_receipt["database"]["sha256"],
        "Catalogue database hash differs from its receipt",
    )
    require(
        database_sha == tranche_receipt["database"]["sha256"],
        "Classification receipt database hash differs from the catalogue",
    )

    connection = sqlite3.connect(database_path)
    scalar_queries = {
        "direct_archive_entries": "SELECT COUNT(*) FROM archive_members",
        "direct_package_occurrences": "SELECT COUNT(*) FROM direct_package_occurrences",
        "unique_package_versions": "SELECT COUNT(*) FROM package_versions",
        "unique_package_file_definitions": (
            "SELECT COUNT(*) FROM package_members WHERE is_directory=0"
        ),
        "unique_package_containment_edges": "SELECT COUNT(*) FROM package_edges",
        "logical_nested_entry_occurrences": (
            "SELECT COUNT(*) FROM expanded_package_member_occurrences"
        ),
        "logical_nested_text_occurrences": (
            "SELECT COUNT(*) FROM logical_nested_text_occurrences"
        ),
        "direct_text_occurrences": "SELECT COUNT(*) FROM direct_text_occurrences",
        "distinct_text_versions": "SELECT COUNT(*) FROM versions",
        "decoded_tex_versions": (
            "SELECT COUNT(*) FROM versions WHERE lower(suffix)='.tex'"
        ),
        "structural_spans_or_locators": "SELECT COUNT(*) FROM spans",
        "literal_reference_records": "SELECT COUNT(*) FROM references_found",
        "remaining_unclassified_versions": (
            "SELECT COUNT(*) FROM topics WHERE lane='unclassified'"
        ),
        "classification_evidence_rows": (
            "SELECT COUNT(*) FROM classification_evidence "
            "WHERE tranche_id='largest-unclassified-tex-2026-09-30'"
        ),
    }
    database_counts = {
        name: connection.execute(query).fetchone()[0]
        for name, query in scalar_queries.items()
    }
    lane_counts = {
        row[0]: row[1]
        for row in connection.execute(
            "SELECT lane, COUNT(*) FROM topics GROUP BY lane ORDER BY lane"
        )
    }
    integrity = connection.execute("PRAGMA integrity_check").fetchone()[0]
    foreign_key_rows = list(connection.execute("PRAGMA foreign_key_check"))
    connection.close()

    expected_counts = {
        "direct_archive_entries": 71426,
        "direct_package_occurrences": 214,
        "unique_package_versions": 56,
        "unique_package_file_definitions": 12822,
        "unique_package_containment_edges": 37,
        "logical_nested_entry_occurrences": 29324,
        "logical_nested_text_occurrences": 24564,
        "direct_text_occurrences": 41695,
        "distinct_text_versions": 7637,
        "decoded_tex_versions": 1282,
        "structural_spans_or_locators": 55659,
        "literal_reference_records": 87272,
        "remaining_unclassified_versions": 4228,
        "classification_evidence_rows": 40,
    }
    require(database_counts == expected_counts, "Unexpected final database counts")
    require(integrity == "ok", f"SQLite integrity failed: {integrity}")
    require(not foreign_key_rows, f"Foreign-key defects: {foreign_key_rows}")
    require(
        lane_counts == catalogue_receipt["counts"]["topic_lane_counts"],
        "Topic lane counts differ from the catalogue receipt",
    )

    coverage_path = ROOT / "ARCHIVE_MEMBER_COVERAGE_V2.jsonl.gz"
    coverage_records = 0
    with gzip.open(coverage_path, "rt", encoding="utf-8") as coverage:
        for line_number, line in enumerate(coverage, 1):
            json.loads(line)
            coverage_records = line_number
    require(coverage_records == 71426, "Direct coverage record count is wrong")
    require(
        sha256_file(coverage_path)
        == catalogue_receipt["direct_member_coverage"]["sha256"],
        "Direct coverage hash differs from the catalogue receipt",
    )

    require(
        mathematical_receipt["exact_check_groups_passed"] == 20,
        "Unexpected exact-check total",
    )
    require(
        mathematical_receipt["numerical_evidence_groups_passed"] == 5,
        "Unexpected numerical-evidence total",
    )
    require(
        tomography_receipt["full_design"]["determinant"] == -4096,
        "Full tomography determinant is wrong",
    )
    require(
        tomography_receipt["observed_design"]["determinant"] == -16,
        "Observed tomography determinant is wrong",
    )

    figure_records = mathematical_receipt["figures"]
    require(len(figure_records) == 12, "Expected twelve figure files")
    for record in figure_records:
        figure_path = ROOT / record["file"]
        require(figure_path.is_file(), f"Missing figure: {figure_path}")
        require(
            figure_path.stat().st_size == record["bytes"]
            and sha256_file(figure_path) == record["sha256"],
            f"Figure differs from verification receipt: {figure_path}",
        )

    ledger_path = ROOT.parent / "ledgers" / "actual_source_readings.jsonl"
    ledger_rows = [
        json.loads(line)
        for line in ledger_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    tranche_ledger_rows = [
        row
        for row in ledger_rows
        if row.get("receiving_work") == "largest-unclassified-tex-2026-09-30"
    ]
    require(
        len(tranche_ledger_rows) == 40
        and len({row["source_file_sha256"] for row in tranche_ledger_rows}) == 40,
        "Classification reading ledger does not contain forty unique records",
    )

    bulletin = (
        MATH_ROOT / "research_index" / "RESULTS_BULLETIN_2026-09-30.md"
    ).read_text(encoding="utf-8")
    for number in range(5, 9):
        require(
            f"SZ-20260930-{number:03d}" in bulletin,
            f"Missing daily result ID SZ-20260930-{number:03d}",
        )

    file_records = [
        {
            "path": relative_path(path),
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
        }
        for path in PRINCIPAL_FILES
    ]
    figure_paths = [ROOT / record["file"] for record in figure_records]
    file_records.extend(
        {
            "path": relative_path(path),
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
        }
        for path in figure_paths
    )
    require(
        len({record["path"] for record in file_records}) == len(file_records),
        "Receipt artifact list contains a duplicate path",
    )

    receipt = {
        "edition": "V2 independent correction and continuation",
        "date": "2026-09-30",
        "scope": (
            "independent redo of the 2026-09-29 consolidation, corrected "
            "recursive custody catalogue, repaired mathematics R6-R7, new R8, "
            "and first evidence-backed unclassified-source tranche"
        ),
        "supersedes": {
            "consolidation_receipt": "CONSOLIDATION_RECEIPT.json",
            "mathematical_checks": "MATHEMATICAL_CHECKS.json",
            "catalogue_receipt": "CATALOGUE_RECEIPT.json",
            "database_for_occurrence_claims": "CORPUS_CATALOGUE.sqlite",
        },
        "catalogue": database_counts,
        "topic_lane_counts": lane_counts,
        "mathematics": {
            "proved_results": [f"R{number}" for number in range(1, 9)],
            "exact_check_groups_passed": 20,
            "numerical_evidence_groups_passed": 5,
            "maximum_relative_cubic_stress_error": mathematical_receipt[
                "maximum_relative_cubic_stress_error"
            ],
            "full_tomography_determinant": -4096,
            "observed_tomography_determinant": -16,
            "figure_files": 12,
            "novelty_claim": False,
        },
        "classification_tranche": {
            "versions_routed": 40,
            "remaining_unclassified": 4228,
            "source_reading_ledger_rows": 40,
            "group_counts": tranche_receipt["group_counts"],
        },
        "validation": {
            "sqlite_integrity": integrity,
            "foreign_key_check_rows": len(foreign_key_rows),
            "direct_coverage_records": coverage_records,
            "outer_archive_sha256_values_recomputed": True,
            "all_direct_text_mappings_checked_by_byte_count_and_crc32": True,
            "pandoc_latex_parse": "passed separately after final TeX generation",
            "builtin_latex_compile": "unavailable",
            "builtin_diagnostic": "Unable to find standard directories for platform",
            "compiled_pdf_claimed": False,
        },
        "files": sorted(file_records, key=lambda record: record["path"]),
        "remote_publication": False,
        "new_task_thread_fork_or_agent": False,
    }
    OUTPUT.write_text(
        json.dumps(receipt, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "file": OUTPUT.name,
                "artifacts_hashed": len(file_records),
                "database_counts": database_counts,
                "topic_lane_counts": lane_counts,
                "coverage_records": coverage_records,
                "exact_checks": 20,
                "numerical_evidence_groups": 5,
                "figures": 12,
            }
        )
    )


if __name__ == "__main__":
    main()
