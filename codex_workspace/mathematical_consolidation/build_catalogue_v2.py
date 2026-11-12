import collections
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
WORK = pathlib.Path(
    r"C:\Users\user\Documents\math\work\s6_main_01a0ea06-5fdc-7a60-97f3-4f4347467d95"
)
V1 = ROOT / "CORPUS_CATALOGUE.sqlite"
V2_PARTIAL = ROOT / "CORPUS_CATALOGUE_V2.sqlite.partial"
V2 = ROOT / "CORPUS_CATALOGUE_V2.sqlite"
COVERAGE = ROOT / "ARCHIVE_MEMBER_COVERAGE.jsonl.gz"
RECEIPT = ROOT / "CATALOGUE_V2_RECEIPT.json"
V2_BLOBS = ROOT / "v2_source_blobs"

TEXT_EXTENSIONS = {
    ".tex",
    ".bib",
    ".md",
    ".txt",
    ".py",
    ".json",
    ".jsonl",
    ".csv",
    ".tsv",
    ".sty",
    ".cls",
    ".lean",
    ".sage",
    ".jl",
    ".r",
    ".m",
    ".wl",
    ".c",
    ".cpp",
    ".h",
    ".js",
    ".ts",
    ".html",
    ".sh",
    ".ps1",
    ".bat",
}


def sha256_file(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while True:
            block = handle.read(16 * 1024 * 1024)
            if not block:
                break
            digest.update(block)
    return digest.hexdigest()


def sha256_crc_size_file(path):
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


def suffix_of(name):
    return pathlib.PurePosixPath(name).suffix.lower()


if V2.exists() or V2_PARTIAL.exists() or RECEIPT.exists():
    raise RuntimeError(
        "V2 output already exists. Retain it as an edition and choose a new edition name for later scope changes."
    )
if not V1.exists() or not COVERAGE.exists():
    raise RuntimeError("The retained V1 catalogue and direct-member coverage are required inputs.")

custody = json.loads((WORK / "FINAL_CUSTODY_AUDIT.json").read_text(encoding="utf-8"))[
    "archives"
]
shutil.copy2(V1, V2_PARTIAL)
db = sqlite3.connect(V2_PARTIAL)
db.execute("pragma foreign_keys=on")
db.executescript(
    """
    ALTER TABLE occurrences RENAME TO legacy_text_occurrences;
    ALTER TABLE opaque_members RENAME TO legacy_opaque_members;
    ALTER TABLE nested_packages RENAME TO legacy_nested_packages;

    CREATE TABLE catalogue_editions(
        edition TEXT PRIMARY KEY,
        status TEXT NOT NULL,
        description TEXT NOT NULL
    );
    CREATE TABLE archives(
        sha256 TEXT PRIMARY KEY,
        archive_path TEXT NOT NULL,
        archive_bytes INTEGER NOT NULL,
        expected_direct_entries INTEGER,
        verified_sha256 INTEGER NOT NULL
    );
    CREATE TABLE direct_text_occurrences(
        id INTEGER PRIMARY KEY,
        sha256 TEXT NOT NULL REFERENCES versions(sha256),
        archive_sha256 TEXT NOT NULL REFERENCES archives(sha256),
        archive_member_ordinal INTEGER NOT NULL,
        member TEXT NOT NULL,
        source_root TEXT,
        origin TEXT NOT NULL,
        UNIQUE(archive_sha256, archive_member_ordinal)
    );
    CREATE TABLE package_versions(
        sha256 TEXT PRIMARY KEY,
        package_bytes INTEGER NOT NULL,
        entry_count INTEGER,
        file_count INTEGER,
        directory_count INTEGER,
        status TEXT NOT NULL,
        first_seen TEXT NOT NULL
    );
    CREATE TABLE direct_package_occurrences(
        id INTEGER PRIMARY KEY,
        archive_sha256 TEXT NOT NULL REFERENCES archives(sha256),
        archive_member_ordinal INTEGER NOT NULL,
        member TEXT NOT NULL,
        package_sha256 TEXT NOT NULL REFERENCES package_versions(sha256),
        member_bytes INTEGER NOT NULL,
        crc32 INTEGER NOT NULL,
        UNIQUE(archive_sha256, archive_member_ordinal)
    );
    CREATE TABLE archive_members(
        id INTEGER PRIMARY KEY,
        archive_sha256 TEXT NOT NULL REFERENCES archives(sha256),
        ordinal INTEGER NOT NULL,
        member TEXT NOT NULL,
        is_directory INTEGER NOT NULL,
        uncompressed_bytes INTEGER NOT NULL,
        compressed_bytes INTEGER NOT NULL,
        crc32 INTEGER NOT NULL,
        suffix TEXT NOT NULL,
        member_class TEXT NOT NULL,
        content_sha256 TEXT,
        text_sha256 TEXT REFERENCES versions(sha256),
        direct_text_occurrence_id INTEGER REFERENCES direct_text_occurrences(id),
        direct_package_occurrence_id INTEGER REFERENCES direct_package_occurrences(id),
        status TEXT NOT NULL,
        UNIQUE(archive_sha256, ordinal)
    );
    CREATE TABLE package_members(
        id INTEGER PRIMARY KEY,
        package_sha256 TEXT NOT NULL REFERENCES package_versions(sha256),
        ordinal INTEGER NOT NULL,
        member TEXT NOT NULL,
        is_directory INTEGER NOT NULL,
        uncompressed_bytes INTEGER NOT NULL,
        compressed_bytes INTEGER NOT NULL,
        crc32 INTEGER NOT NULL,
        suffix TEXT NOT NULL,
        member_class TEXT NOT NULL,
        content_sha256 TEXT,
        text_sha256 TEXT REFERENCES versions(sha256),
        child_package_sha256 TEXT REFERENCES package_versions(sha256),
        status TEXT NOT NULL,
        UNIQUE(package_sha256, ordinal)
    );
    CREATE TABLE package_edges(
        parent_package_sha256 TEXT NOT NULL REFERENCES package_versions(sha256),
        parent_member_ordinal INTEGER NOT NULL,
        child_package_sha256 TEXT NOT NULL REFERENCES package_versions(sha256),
        PRIMARY KEY(parent_package_sha256, parent_member_ordinal)
    );
    CREATE TABLE expanded_package_member_occurrences(
        id INTEGER PRIMARY KEY,
        direct_package_occurrence_id INTEGER NOT NULL REFERENCES direct_package_occurrences(id),
        depth INTEGER NOT NULL,
        package_sha256 TEXT NOT NULL REFERENCES package_versions(sha256),
        package_member_ordinal INTEGER NOT NULL,
        member TEXT NOT NULL,
        logical_path TEXT NOT NULL,
        path_chain_json TEXT NOT NULL,
        member_class TEXT NOT NULL,
        content_sha256 TEXT,
        text_sha256 TEXT REFERENCES versions(sha256),
        child_package_sha256 TEXT REFERENCES package_versions(sha256)
    );
    CREATE TABLE expansion_anomalies(
        id INTEGER PRIMARY KEY,
        direct_package_occurrence_id INTEGER REFERENCES direct_package_occurrences(id),
        package_sha256 TEXT,
        logical_path TEXT,
        status TEXT NOT NULL
    );
    CREATE TABLE catalogue_summary(
        key TEXT PRIMARY KEY,
        integer_value INTEGER,
        text_value TEXT
    );

    CREATE INDEX direct_text_hash_v2 ON direct_text_occurrences(sha256);
    CREATE INDEX direct_package_hash_v2 ON direct_package_occurrences(package_sha256);
    CREATE INDEX archive_member_name_v2 ON archive_members(archive_sha256,member);
    CREATE INDEX package_member_name_v2 ON package_members(package_sha256,member);
    CREATE INDEX package_member_text_v2 ON package_members(text_sha256);
    CREATE INDEX expanded_root_v2 ON expanded_package_member_occurrences(direct_package_occurrence_id);
    CREATE INDEX expanded_text_v2 ON expanded_package_member_occurrences(text_sha256);
    CREATE INDEX expanded_package_v2 ON expanded_package_member_occurrences(package_sha256);

    CREATE VIEW logical_nested_text_occurrences AS
    SELECT id,direct_package_occurrence_id,depth,package_sha256,
           package_member_ordinal,member,logical_path,path_chain_json,
           content_sha256,text_sha256
    FROM expanded_package_member_occurrences
    WHERE text_sha256 IS NOT NULL;
    """
)
db.execute(
    "insert into catalogue_editions values(?,?,?)",
    (
        "V2",
        "canonical occurrence model",
        "V1 lexical inventory retained; package definitions, placements, containment edges, and recursively expanded logical occurrences represented separately",
    ),
)
db.execute(
    "insert into catalogue_editions values(?,?,?)",
    (
        "V1",
        "superseded occurrence model retained in legacy tables",
        "V1 expanded each distinct package byte version once and did not represent every package placement",
    ),
)

counts = collections.Counter()
verified_version_hashes = set()
verified_version_metadata = {}
for digest, corpus_file in db.execute("select sha256,corpus_file from versions"):
    path = pathlib.Path(corpus_file)
    if not path.is_file():
        raise RuntimeError(f"retained text blob is missing: {path}")
    actual, crc32, byte_count = sha256_crc_size_file(path)
    if actual != digest:
        raise RuntimeError(f"retained text blob hash mismatch: {path}")
    verified_version_hashes.add(digest)
    verified_version_metadata[digest] = (byte_count, crc32)
counts["verified_text_version_blobs"] = len(verified_version_hashes)

legacy_direct = {}
for digest, archive_sha, member, source_root, origin in db.execute(
    """
    select sha256,archive_sha256,member,source_root,origin
    from legacy_text_occurrences
    where container_chain=''
    order by id
    """
):
    legacy_direct.setdefault((archive_sha, member, digest), (source_root, origin))

package_members_by_sha = {}
package_status = {}
active_packages = set()


def ensure_version(raw, digest, suffix):
    row = db.execute("select corpus_file from versions where sha256=?", (digest,)).fetchone()
    if row is not None:
        return
    V2_BLOBS.mkdir(exist_ok=True)
    path = V2_BLOBS / (digest + suffix)
    if not path.exists():
        path.write_bytes(raw)
    try:
        text = raw.decode("utf-8-sig")
        lines = len(text.splitlines())
        status = "V2-discovered strict UTF-8 text; exact bytes retained; lexical extraction pending"
    except UnicodeDecodeError:
        lines = None
        status = "V2-discovered exact text-designated bytes; decoding and lexical extraction pending"
    db.execute(
        "insert into versions values(?,?,?,?,?,?)",
        (digest, str(path), len(raw), suffix, lines, status),
    )
    db.execute(
        "insert or ignore into topics values(?,?,?)",
        (digest, "unclassified", "V2 package scan; semantic classification pending"),
    )
    verified_version_hashes.add(digest)
    verified_version_metadata[digest] = (
        len(raw),
        zlib.crc32(raw) & 0xFFFFFFFF,
    )
    counts["v2_new_text_versions"] += 1


def scan_package(data, first_seen):
    digest = hashlib.sha256(data).hexdigest()
    if digest in package_status:
        counts["repeated_package_references"] += 1
        return digest
    if digest in active_packages:
        counts["package_identity_cycles"] += 1
        return digest
    active_packages.add(digest)
    db.execute(
        "insert into package_versions values(?,?,?,?,?,?,?)",
        (digest, len(data), None, None, None, "scan in progress", first_seen),
    )
    members = []
    try:
        with zipfile.ZipFile(io.BytesIO(data)) as package:
            infos = package.infolist()
            file_count = 0
            directory_count = 0
            for ordinal, info in enumerate(infos):
                member = info.filename
                suffix = suffix_of(member)
                content_sha = None
                text_sha = None
                child_sha = None
                if info.is_dir():
                    member_class = "directory"
                    status = "directory entry"
                    directory_count += 1
                else:
                    file_count += 1
                    if suffix == ".zip":
                        raw = package.read(info)
                        content_sha = hashlib.sha256(raw).hexdigest()
                        child_sha = scan_package(
                            raw, f"{first_seen}!{member} [entry {ordinal}]"
                        )
                        member_class = "nested_zip"
                        status = "child package byte identity and containment edge verified"
                    elif suffix in TEXT_EXTENSIONS:
                        raw = package.read(info)
                        content_sha = hashlib.sha256(raw).hexdigest()
                        text_sha = content_sha
                        ensure_version(raw, text_sha, suffix)
                        member_class = "text"
                        status = "exact text bytes hashed and linked to retained version"
                    else:
                        member_class = "opaque"
                        status = "exact ZIP metadata retained; member content not semantically read"
                db.execute(
                    """
                    insert into package_members(
                        package_sha256,ordinal,member,is_directory,
                        uncompressed_bytes,compressed_bytes,crc32,suffix,
                        member_class,content_sha256,text_sha256,
                        child_package_sha256,status
                    ) values(?,?,?,?,?,?,?,?,?,?,?,?,?)
                    """,
                    (
                        digest,
                        ordinal,
                        member,
                        int(info.is_dir()),
                        info.file_size,
                        info.compress_size,
                        info.CRC,
                        suffix,
                        member_class,
                        content_sha,
                        text_sha,
                        child_sha,
                        status,
                    ),
                )
                if child_sha is not None:
                    db.execute(
                        "insert into package_edges values(?,?,?)",
                        (digest, ordinal, child_sha),
                    )
                members.append(
                    {
                        "ordinal": ordinal,
                        "member": member,
                        "class": member_class,
                        "content_sha": content_sha,
                        "text_sha": text_sha,
                        "child_sha": child_sha,
                    }
                )
            db.execute(
                """
                update package_versions
                set entry_count=?,file_count=?,directory_count=?,status=?
                where sha256=?
                """,
                (
                    len(infos),
                    file_count,
                    directory_count,
                    "ZIP central directory read; every entry classified; text and child-package bytes hashed",
                    digest,
                ),
            )
            package_status[digest] = "ok"
            package_members_by_sha[digest] = members
    except (zipfile.BadZipFile, RuntimeError, NotImplementedError) as exc:
        message = f"{type(exc).__name__}: {exc}"
        db.execute(
            "update package_versions set status=? where sha256=?",
            (message, digest),
        )
        package_status[digest] = "unreadable"
        package_members_by_sha[digest] = []
        counts["unreadable_package_versions"] += 1
    finally:
        active_packages.remove(digest)
    return digest


archive_records = []
with gzip.open(COVERAGE, "rt", encoding="utf-8") as coverage_handle:
    for archive_record in custody:
        archive_path = pathlib.Path(archive_record["archive"])
        expected_sha = archive_record["sha256"]
        actual_sha = sha256_file(archive_path)
        if actual_sha != expected_sha:
            raise RuntimeError(f"custody archive hash mismatch: {archive_path}")
        archive_bytes = archive_path.stat().st_size
        db.execute(
            "insert into archives values(?,?,?,?,?)",
            (
                expected_sha,
                str(archive_path),
                archive_bytes,
                archive_record.get("members"),
                1,
            ),
        )
        counts["verified_custody_archives"] += 1
        with zipfile.ZipFile(archive_path) as archive:
            infos = archive.infolist()
            if archive_record.get("members") not in (None, len(infos)):
                raise RuntimeError(f"direct-entry count mismatch: {archive_path}")
            for ordinal, info in enumerate(infos):
                line = coverage_handle.readline()
                if not line:
                    raise RuntimeError("direct-member coverage ended early")
                coverage_row = json.loads(line)
                expected_tuple = (
                    expected_sha,
                    info.filename,
                    info.file_size,
                    info.CRC,
                )
                found_tuple = (
                    coverage_row["archive_sha256"],
                    coverage_row["member"],
                    coverage_row["bytes"],
                    coverage_row["crc32"],
                )
                if expected_tuple != found_tuple:
                    raise RuntimeError(
                        f"coverage/central-directory mismatch at {archive_path} entry {ordinal}"
                    )
                suffix = suffix_of(info.filename)
                coverage_text_sha = coverage_row.get("text_sha256")
                text_sha = coverage_text_sha
                content_sha = None
                direct_text_id = None
                direct_package_id = None
                if info.is_dir():
                    member_class = "directory"
                    status = "directory entry"
                elif suffix == ".zip":
                    raw = archive.read(info)
                    content_sha = hashlib.sha256(raw).hexdigest()
                    package_sha = scan_package(
                        raw,
                        f"{expected_sha}:{info.filename} [direct entry {ordinal}]",
                    )
                    cursor = db.execute(
                        """
                        insert into direct_package_occurrences(
                            archive_sha256,archive_member_ordinal,member,
                            package_sha256,member_bytes,crc32
                        ) values(?,?,?,?,?,?)
                        """,
                        (
                            expected_sha,
                            ordinal,
                            info.filename,
                            package_sha,
                            info.file_size,
                            info.CRC,
                        ),
                    )
                    direct_package_id = cursor.lastrowid
                    member_class = "nested_zip"
                    status = "direct package occurrence linked to its exact package byte version"
                    counts["direct_package_occurrences"] += 1
                elif text_sha is not None:
                    if text_sha not in verified_version_hashes:
                        row = db.execute(
                            "select corpus_file from versions where sha256=?", (text_sha,)
                        ).fetchone()
                        if row is None:
                            raise RuntimeError(
                                f"coverage names an absent text version: {text_sha}"
                            )
                    legacy_hit = legacy_direct.get(
                        (expected_sha, info.filename, text_sha)
                    )
                    expected_metadata = verified_version_metadata.get(text_sha)
                    if (
                        legacy_hit is None
                        or expected_metadata != (info.file_size, info.CRC)
                    ):
                        raw = archive.read(info)
                        actual_text_sha = hashlib.sha256(raw).hexdigest()
                        ensure_version(raw, actual_text_sha, suffix)
                        text_sha = actual_text_sha
                        if actual_text_sha != coverage_text_sha:
                            counts["corrected_v1_direct_text_mappings"] += 1
                        legacy_hit = legacy_direct.get(
                            (expected_sha, info.filename, text_sha)
                        )
                    source_root, origin = legacy_hit or (
                        "direct_archive",
                        "V2 exact direct-member reconstruction",
                    )
                    cursor = db.execute(
                        """
                        insert into direct_text_occurrences(
                            sha256,archive_sha256,archive_member_ordinal,
                            member,source_root,origin
                        ) values(?,?,?,?,?,?)
                        """,
                        (
                            text_sha,
                            expected_sha,
                            ordinal,
                            info.filename,
                            source_root,
                            origin,
                        ),
                    )
                    direct_text_id = cursor.lastrowid
                    content_sha = text_sha
                    member_class = "text"
                    status = "direct text occurrence linked to an exact verified text version"
                    counts["direct_text_occurrences"] += 1
                else:
                    member_class = "opaque"
                    status = coverage_row["status"]
                db.execute(
                    """
                    insert into archive_members(
                        archive_sha256,ordinal,member,is_directory,
                        uncompressed_bytes,compressed_bytes,crc32,suffix,
                        member_class,content_sha256,text_sha256,
                        direct_text_occurrence_id,direct_package_occurrence_id,status
                    ) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                    """,
                    (
                        expected_sha,
                        ordinal,
                        info.filename,
                        int(info.is_dir()),
                        info.file_size,
                        info.compress_size,
                        info.CRC,
                        suffix,
                        member_class,
                        content_sha,
                        text_sha,
                        direct_text_id,
                        direct_package_id,
                        status,
                    ),
                )
                counts["direct_archive_entries"] += 1
        db.commit()
        archive_records.append(
            {
                "archive": str(archive_path),
                "sha256": expected_sha,
                "bytes": archive_bytes,
                "direct_entries": len(infos),
            }
        )
        print(
            json.dumps(
                {
                    "phase": "archive verified and registered",
                    "archive": archive_path.name,
                    "direct_entries_total": counts["direct_archive_entries"],
                    "direct_packages_total": counts["direct_package_occurrences"],
                    "unique_package_versions": len(package_status),
                }
            ),
            flush=True,
        )
    if coverage_handle.readline():
        raise RuntimeError("direct-member coverage has trailing records")


def expand_occurrence(
    direct_id,
    package_sha,
    root_archive_member,
    depth,
    chain,
    active_path,
):
    if package_sha in active_path:
        logical_path = "!".join(chain)
        db.execute(
            """
            insert into expansion_anomalies(
                direct_package_occurrence_id,package_sha256,logical_path,status
            ) values(?,?,?,?)
            """,
            (
                direct_id,
                package_sha,
                logical_path,
                "package byte identity repeats along one containment path; recursion stopped",
            ),
        )
        counts["logical_cycle_stops"] += 1
        return
    next_active = active_path | {package_sha}
    for member in package_members_by_sha.get(package_sha, []):
        member_chain = chain + [member["member"]]
        logical_path = "!".join(member_chain)
        db.execute(
            """
            insert into expanded_package_member_occurrences(
                direct_package_occurrence_id,depth,package_sha256,
                package_member_ordinal,member,logical_path,path_chain_json,
                member_class,content_sha256,text_sha256,child_package_sha256
            ) values(?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                direct_id,
                depth,
                package_sha,
                member["ordinal"],
                member["member"],
                logical_path,
                json.dumps(member_chain, ensure_ascii=False),
                member["class"],
                member["content_sha"],
                member["text_sha"],
                member["child_sha"],
            ),
        )
        counts["logical_nested_entry_occurrences"] += 1
        counts[f"logical_nested_{member['class']}_occurrences"] += 1
        if member["child_sha"] is not None:
            expand_occurrence(
                direct_id,
                member["child_sha"],
                root_archive_member,
                depth + 1,
                member_chain,
                next_active,
            )


for direct_id, package_sha, member in db.execute(
    "select id,package_sha256,member from direct_package_occurrences order by id"
).fetchall():
    expand_occurrence(direct_id, package_sha, member, 1, [member], set())
db.commit()

counts["verified_text_version_blobs"] = len(verified_version_hashes)
counts["unique_package_versions"] = db.execute(
    "select count(*) from package_versions"
).fetchone()[0]
counts["unique_package_entry_definitions"] = db.execute(
    "select count(*) from package_members"
).fetchone()[0]
counts["unique_package_file_definitions"] = db.execute(
    "select count(*) from package_members where is_directory=0"
).fetchone()[0]
counts["unique_package_directory_definitions"] = db.execute(
    "select count(*) from package_members where is_directory=1"
).fetchone()[0]
counts["unique_package_text_definitions"] = db.execute(
    "select count(*) from package_members where text_sha256 is not null"
).fetchone()[0]
counts["unique_package_containment_edges"] = db.execute(
    "select count(*) from package_edges"
).fetchone()[0]
counts["logical_nested_text_occurrences"] = db.execute(
    "select count(*) from logical_nested_text_occurrences"
).fetchone()[0]
counts["expansion_anomalies"] = db.execute(
    "select count(*) from expansion_anomalies"
).fetchone()[0]

for key, value in sorted(counts.items()):
    db.execute(
        "insert into catalogue_summary(key,integer_value,text_value) values(?,?,?)",
        (key, int(value), None),
    )
db.execute(
    "insert into catalogue_summary values(?,?,?)",
    (
        "occurrence_model",
        None,
        "package byte versions, package placements, containment edges, and recursive logical member occurrences are separate relations",
    ),
)
db.commit()
foreign_key_errors = db.execute("pragma foreign_key_check").fetchall()
integrity = db.execute("pragma integrity_check").fetchone()[0]
if foreign_key_errors:
    raise RuntimeError(f"foreign-key errors: {foreign_key_errors[:5]}")
if integrity != "ok":
    raise RuntimeError(f"SQLite integrity failure: {integrity}")
db.execute("vacuum")
db.close()

V2_PARTIAL.replace(V2)
receipt = {
    "edition": "V2",
    "purpose": "replace the collapsed V1 nested-package occurrence model while retaining its lexical inventory for provenance",
    "counts": dict(sorted(counts.items())),
    "interpretation": {
        "unique_package_file_definitions": "files encountered while each distinct package byte version is opened once",
        "logical_nested_entry_occurrences": "entries reached after expanding every direct package placement and every containment edge with multiplicity",
        "direct_package_occurrences": "ZIP-suffixed members in the nine outer custody archives, one row per central-directory placement",
    },
    "archives": archive_records,
    "validation": {
        "all_outer_archive_sha256_values_recomputed": True,
        "all_retained_text_version_blobs_rehashed": True,
        "direct_coverage_matched_to_central_directories_in_order": True,
        "all_direct_package_occurrences_mapped": counts["direct_package_occurrences"]
        == 214,
        "foreign_key_check": "ok",
        "sqlite_integrity": integrity,
        "logical_cycle_stops": counts["logical_cycle_stops"],
    },
    "supersession": {
        "superseded_file": "CATALOGUE_RECEIPT.json",
        "superseded_claim": "12,822 nested member occurrences",
        "reason": "V1 counted members while distinct package byte versions were expanded once; it did not retain the multiplicity of every package placement",
        "retained_v1_database": "CORPUS_CATALOGUE.sqlite",
        "retained_v1_sha256": sha256_file(V1),
    },
    "database": {
        "file": V2.name,
        "bytes": V2.stat().st_size,
        "sha256": sha256_file(V2),
    },
    "source_bytes_changed": False,
}
RECEIPT.write_text(
    json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(receipt, ensure_ascii=False), flush=True)
