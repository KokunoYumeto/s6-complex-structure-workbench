from __future__ import annotations

import argparse
from contextlib import closing
import gzip
import hashlib
import json
from pathlib import Path
import shutil
import sqlite3
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parent


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        while block := handle.read(1024 * 1024):
            value.update(block)
    return value.hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    parser = argparse.ArgumentParser(description="Verify this publication's file identities, catalogue, and optional mathematical replay.")
    parser.add_argument("--math-replay", action="store_true")
    arguments = parser.parse_args()
    manifest = json.loads((ROOT / "PUBLICATION_MANIFEST.json").read_text(encoding="utf-8"))
    for item in manifest["files"]:
        path = ROOT / item["path"]
        require(path.resolve().is_relative_to(ROOT.resolve()), "Manifest path escapes the publication directory")
        require(path.is_file(), f"Missing file: {item['path']}")
        require(path.stat().st_size == item["bytes"], f"Wrong byte length: {item['path']}")
        require(digest(path) == item["sha256"], f"Wrong SHA-256: {item['path']}")

    receipt = json.loads((ROOT / "catalogue" / "CATALOGUE_V2_PUBLIC_RECEIPT.json").read_text(encoding="utf-8"))
    database_record = receipt["database"]["public_database"]
    catalogue_counts = receipt["database"]["table_counts"]
    with tempfile.TemporaryDirectory(prefix="s6-publication-check-") as folder:
        temporary = Path(folder)
        database = temporary / "catalogue.sqlite"
        with gzip.open(ROOT / database_record["gzip_file"], "rb") as incoming, database.open("wb") as outgoing:
            shutil.copyfileobj(incoming, outgoing, 1024 * 1024)
        require(database.stat().st_size == database_record["uncompressed_bytes"], "Unpacked database byte length failed")
        require(digest(database) == database_record["uncompressed_sha256"], "Unpacked database SHA-256 failed")
        with closing(sqlite3.connect(database.as_uri() + "?mode=ro", uri=True)) as connection:
            require(connection.execute("PRAGMA integrity_check").fetchone()[0] == "ok", "SQLite integrity failed")
            require(not list(connection.execute("PRAGMA foreign_key_check")), "SQLite foreign keys failed")
            for table, count in catalogue_counts.items():
                actual = connection.execute(f'SELECT COUNT(*) FROM "{table}"').fetchone()[0]
                require(actual == count, f"Wrong row count: {table}")

        coverage_record = receipt["direct_member_coverage"]["public_file"]
        coverage_digest = hashlib.sha256()
        coverage_rows = 0
        with gzip.open(ROOT / coverage_record["file"], "rb") as handle:
            for line in handle:
                coverage_digest.update(line)
                json.loads(line)
                coverage_rows += 1
        require(coverage_digest.hexdigest() == coverage_record["uncompressed_sha256"], "Coverage stream SHA-256 failed")
        require(coverage_rows == receipt["direct_member_coverage"]["records"], "Coverage stream row count failed")

        mathematical_replay = {"executed": False}
        if arguments.math_replay:
            replay = temporary / "mathematical-replay"
            replay.mkdir()
            script = replay / "verify_consolidation_v2.py"
            shutil.copy2(ROOT / script.name, script)
            result = subprocess.run([sys.executable, str(script)], cwd=replay, capture_output=True, text=True, check=True)
            summary = json.loads(result.stdout.strip())
            fresh = json.loads((replay / "checks" / "MATHEMATICAL_CHECKS_V2.json").read_text(encoding="utf-8"))
            supplied = json.loads((ROOT / "checks" / "MATHEMATICAL_CHECKS_V2.json").read_text(encoding="utf-8"))
            for key in ("exact_checks", "numerical_checks", "integer_residual_moments_p_1_through_6"):
                require(fresh[key] == supplied[key], f"Fresh mathematical evidence differs: {key}")
            require(
                json.loads((replay / "checks" / "TOMOGRAPHY_DESIGN_MATRICES.json").read_text(encoding="utf-8"))
                == json.loads((ROOT / "checks" / "TOMOGRAPHY_DESIGN_MATRICES.json").read_text(encoding="utf-8")),
                "Fresh exact tomography matrices differ",
            )
            mathematical_replay = {"executed": True, **summary}

    report = {
        "status": "passed",
        "scope": "Payload identities, lossless decompression, database integrity and row counts, coverage stream, and the explicitly recorded mathematical replay. Complete arguments remain in the note and appendix.",
        "manifest_sha256": digest(ROOT / "PUBLICATION_MANIFEST.json"),
        "manifest_files_verified": len(manifest["files"]),
        "manifest_bytes_verified": sum(item["bytes"] for item in manifest["files"]),
        "sqlite_integrity": "ok",
        "foreign_key_errors": 0,
        "database_tables_checked": len(catalogue_counts),
        "direct_coverage_records_checked": coverage_rows,
        "mathematical_replay": mathematical_replay,
        "compiled_pdf_claimed": False,
    }
    (ROOT / "PUBLIC_VALIDATION.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
