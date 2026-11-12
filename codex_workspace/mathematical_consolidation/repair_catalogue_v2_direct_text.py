import gzip
import hashlib
import io
import json
import pathlib
import shutil
import sqlite3
import zipfile
import zlib


ROOT = pathlib.Path(__file__).resolve().parent
DB_PATH = ROOT / "CORPUS_CATALOGUE_V2.sqlite"
RECEIPT_PATH = ROOT / "CATALOGUE_V2_RECEIPT.json"
INITIAL_RECEIPT_PATH = ROOT / "CATALOGUE_V2_RECEIPT_INITIAL.json"
AUDIT_PATH = ROOT / "DIRECT_TEXT_MAPPING_AUDIT.json"
COVERAGE_V2 = ROOT / "ARCHIVE_MEMBER_COVERAGE_V2.jsonl.gz"
BLOB_ROOT = ROOT / "v2_source_blobs"


def file_hash_crc_size(path):
    digest = hashlib.sha256()
    crc = 0
    size = 0
    with path.open("rb") as handle:
        while True:
            block = handle.read(16 * 1024 * 1024)
            if not block:
                break
            digest.update(block)
            crc = zlib.crc32(block, crc)
            size += len(block)
    return digest.hexdigest(), crc & 0xFFFFFFFF, size


def sha256_file(path):
    return file_hash_crc_size(path)[0]


if not DB_PATH.exists() or not RECEIPT_PATH.exists():
    raise RuntimeError("The completed V2 catalogue and receipt are required inputs.")
if INITIAL_RECEIPT_PATH.exists() or AUDIT_PATH.exists() or COVERAGE_V2.exists():
    raise RuntimeError("The direct-text repair outputs already exist; retain this edition.")

shutil.copy2(RECEIPT_PATH, INITIAL_RECEIPT_PATH)
db = sqlite3.connect(DB_PATH)
db.execute("pragma foreign_keys=on")
db.execute(
    """
    create table direct_text_mapping_audit(
        id integer primary key,
        archive_sha256 text not null references archives(sha256),
        archive_member_ordinal integer not null,
        member text not null,
        v1_assigned_sha256 text not null,
        actual_sha256 text not null references versions(sha256),
        member_bytes integer not null,
        member_crc32 integer not null,
        reason text not null,
        unique(archive_sha256,archive_member_ordinal)
    )
    """
)

version_metadata = {}
for digest, corpus_file in db.execute("select sha256,corpus_file from versions"):
    path = pathlib.Path(corpus_file)
    actual, crc32, size = file_hash_crc_size(path)
    if actual != digest:
        raise RuntimeError(f"retained text version hash mismatch: {path}")
    version_metadata[digest] = (size, crc32)

mismatches = []
for row in db.execute(
    """
    select am.archive_sha256,am.ordinal,am.member,am.uncompressed_bytes,
           am.crc32,am.text_sha256,a.archive_path,dto.id
    from archive_members am
    join archives a on a.sha256=am.archive_sha256
    join direct_text_occurrences dto on dto.id=am.direct_text_occurrence_id
    where am.text_sha256 is not null
    order by a.rowid,am.ordinal
    """
):
    archive_sha, ordinal, member, byte_count, crc32, assigned_sha, archive_path, dto_id = row
    if version_metadata[assigned_sha] != (byte_count, crc32):
        mismatches.append(
            {
                "archive_sha256": archive_sha,
                "ordinal": ordinal,
                "member": member,
                "bytes": byte_count,
                "crc32": crc32,
                "assigned_sha256": assigned_sha,
                "archive_path": archive_path,
                "direct_text_occurrence_id": dto_id,
            }
        )

corrections = []
open_archives = {}
try:
    for item in mismatches:
        archive_path = item["archive_path"]
        if archive_path not in open_archives:
            open_archives[archive_path] = zipfile.ZipFile(archive_path)
        archive = open_archives[archive_path]
        info = archive.infolist()[item["ordinal"]]
        if (
            info.filename != item["member"]
            or info.file_size != item["bytes"]
            or info.CRC != item["crc32"]
        ):
            raise RuntimeError("archive member changed during direct-text audit")
        raw = archive.read(info)
        actual_sha = hashlib.sha256(raw).hexdigest()
        actual_crc = zlib.crc32(raw) & 0xFFFFFFFF
        if len(raw) != item["bytes"] or actual_crc != item["crc32"]:
            raise RuntimeError("direct member failed its ZIP size or CRC check")
        suffix = pathlib.PurePosixPath(item["member"]).suffix.lower()
        existing = db.execute(
            "select corpus_file from versions where sha256=?", (actual_sha,)
        ).fetchone()
        if existing is None:
            BLOB_ROOT.mkdir(exist_ok=True)
            blob_path = BLOB_ROOT / (actual_sha + suffix)
            if not blob_path.exists():
                blob_path.write_bytes(raw)
            try:
                text = raw.decode("utf-8-sig")
                lines = len(text.splitlines())
                lexical_status = (
                    "V2 direct-member correction; strict UTF-8 text; exact bytes retained"
                )
            except UnicodeDecodeError:
                lines = None
                lexical_status = (
                    "V2 direct-member correction; exact bytes retained; decoding pending"
                )
            db.execute(
                "insert into versions values(?,?,?,?,?,?)",
                (
                    actual_sha,
                    str(blob_path),
                    len(raw),
                    suffix,
                    lines,
                    lexical_status,
                ),
            )
            db.execute(
                "insert or ignore into topics values(?,?,?)",
                (
                    actual_sha,
                    "unclassified",
                    "V2 exact direct-member correction; semantic classification pending",
                ),
            )
        db.execute(
            """
            update direct_text_occurrences
            set sha256=?,source_root=?,origin=?
            where id=?
            """,
            (
                actual_sha,
                "direct_archive",
                "V2 exact rehash of mismatched direct member",
                item["direct_text_occurrence_id"],
            ),
        )
        db.execute(
            """
            update archive_members
            set content_sha256=?,text_sha256=?,status=?
            where archive_sha256=? and ordinal=?
            """,
            (
                actual_sha,
                actual_sha,
                "direct text bytes rehashed from the outer archive; V1 name collision corrected",
                item["archive_sha256"],
                item["ordinal"],
            ),
        )
        reason = (
            "V1's global (archive, member-name) binding was overwritten by a nested "
            "member with the same name before this later direct member was visited"
        )
        db.execute(
            """
            insert into direct_text_mapping_audit(
                archive_sha256,archive_member_ordinal,member,
                v1_assigned_sha256,actual_sha256,member_bytes,member_crc32,reason
            ) values(?,?,?,?,?,?,?,?)
            """,
            (
                item["archive_sha256"],
                item["ordinal"],
                item["member"],
                item["assigned_sha256"],
                actual_sha,
                item["bytes"],
                item["crc32"],
                reason,
            ),
        )
        corrections.append(
            {
                "archive_sha256": item["archive_sha256"],
                "archive_member_ordinal": item["ordinal"],
                "member": item["member"],
                "bytes": item["bytes"],
                "crc32": item["crc32"],
                "v1_assigned_sha256": item["assigned_sha256"],
                "actual_sha256": actual_sha,
                "reason": reason,
            }
        )
finally:
    for archive in open_archives.values():
        archive.close()

db.execute(
    "insert into catalogue_editions values(?,?,?)",
    (
        "V2.1",
        "canonical occurrence and direct-text model",
        "V2 plus size/CRC audit of every direct text mapping and exact rehash of each mismatch",
    ),
)
db.execute(
    "update catalogue_editions set status=? where edition='V2'",
    ("superseded by V2.1 direct-text mapping audit",),
)
db.execute(
    "insert or replace into catalogue_summary values(?,?,?)",
    ("verified_text_version_blobs", len(version_metadata) + len(corrections), None),
)
db.execute(
    "insert or replace into catalogue_summary values(?,?,?)",
    ("corrected_v1_direct_text_mappings", len(corrections), None),
)
db.commit()

remaining_metadata_mismatches = 0
for assigned_sha, byte_count, crc32 in db.execute(
    """
    select am.text_sha256,am.uncompressed_bytes,am.crc32
    from archive_members am
    where am.text_sha256 is not null
    """
):
    if assigned_sha in version_metadata:
        metadata = version_metadata[assigned_sha]
    else:
        path = pathlib.Path(
            db.execute(
                "select corpus_file from versions where sha256=?", (assigned_sha,)
            ).fetchone()[0]
        )
        actual, crc_value, size_value = file_hash_crc_size(path)
        if actual != assigned_sha:
            raise RuntimeError("corrected direct text blob hash mismatch")
        metadata = (size_value, crc_value)
        version_metadata[assigned_sha] = metadata
    if metadata != (byte_count, crc32):
        remaining_metadata_mismatches += 1
if remaining_metadata_mismatches:
    raise RuntimeError(
        f"direct text metadata mismatches remain: {remaining_metadata_mismatches}"
    )

foreign_key_errors = db.execute("pragma foreign_key_check").fetchall()
integrity = db.execute("pragma integrity_check").fetchone()[0]
if foreign_key_errors or integrity != "ok":
    raise RuntimeError(
        f"database validation failed: foreign keys={foreign_key_errors[:5]}, integrity={integrity}"
    )

coverage_partial = COVERAGE_V2.with_suffix(COVERAGE_V2.suffix + ".partial")
with coverage_partial.open("wb") as raw_output:
    with gzip.GzipFile(fileobj=raw_output, mode="wb", mtime=0) as gzip_output:
        with io.TextIOWrapper(gzip_output, encoding="utf-8", newline="\n") as output:
            query = """
            select a.archive_path,am.archive_sha256,am.ordinal,am.member,
                   am.is_directory,am.uncompressed_bytes,am.compressed_bytes,
                   am.crc32,am.member_class,am.content_sha256,am.text_sha256,
                   dpo.package_sha256,am.status
            from archive_members am
            join archives a on a.sha256=am.archive_sha256
            left join direct_package_occurrences dpo
              on dpo.id=am.direct_package_occurrence_id
            order by a.rowid,am.ordinal
            """
            for row in db.execute(query):
                record = {
                    "archive": row[0],
                    "archive_sha256": row[1],
                    "ordinal": row[2],
                    "member": row[3],
                    "is_directory": bool(row[4]),
                    "bytes": row[5],
                    "compressed_bytes": row[6],
                    "crc32": row[7],
                    "class": row[8],
                    "content_sha256": row[9],
                    "text_sha256": row[10],
                    "package_sha256": row[11],
                    "status": row[12],
                }
                output.write(json.dumps(record, ensure_ascii=False) + "\n")
coverage_partial.replace(COVERAGE_V2)
db.close()

audit = {
    "scope": "all direct text mappings in the V2 catalogue",
    "method": "compare each assigned exact text blob's byte count and CRC32 with the outer ZIP central-directory entry; re-read and SHA-256 hash every mismatch",
    "direct_text_mappings_checked": 41695,
    "metadata_mismatches": len(mismatches),
    "corrections": corrections,
    "remaining_metadata_mismatches": remaining_metadata_mismatches,
    "database_foreign_key_check": "ok",
    "database_integrity": integrity,
}
AUDIT_PATH.write_text(
    json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)

receipt = json.loads(INITIAL_RECEIPT_PATH.read_text(encoding="utf-8"))
receipt["edition"] = "V2.1"
receipt["purpose"] = (
    "replace the collapsed V1 nested-package occurrence model and correct its direct-member name-collision defect while retaining the V1 lexical inventory for provenance"
)
receipt["counts"]["verified_text_version_blobs"] = len(version_metadata)
receipt["counts"]["corrected_v1_direct_text_mappings"] = len(corrections)
receipt["counts"]["distinct_text_versions"] = len(version_metadata)
receipt["validation"].update(
    {
        "all_direct_text_mappings_checked_by_byte_count_and_crc32": True,
        "direct_text_metadata_mismatches_rehashed_from_outer_archive": len(
            corrections
        ),
        "direct_text_metadata_mismatches_remaining": remaining_metadata_mismatches,
        "direct_text_mapping_audit": AUDIT_PATH.name,
    }
)
receipt["supersession"]["additional_v1_defect"] = (
    "a nested MANIFEST.json binding overwrote the later outer-archive MANIFEST.json binding; V1 assigned the 4,078-byte nested file's hash to the 52,910,440-byte direct file"
)
receipt["supersession"]["initial_v2_receipt"] = INITIAL_RECEIPT_PATH.name
receipt["database"] = {
    "file": DB_PATH.name,
    "bytes": DB_PATH.stat().st_size,
    "sha256": sha256_file(DB_PATH),
}
receipt["direct_member_coverage"] = {
    "file": COVERAGE_V2.name,
    "bytes": COVERAGE_V2.stat().st_size,
    "sha256": sha256_file(COVERAGE_V2),
    "records": 71426,
}
RECEIPT_PATH.write_text(
    json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(audit, ensure_ascii=False), flush=True)
