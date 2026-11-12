from __future__ import annotations

import hashlib
import json
import pathlib
import re
import sqlite3
from collections import Counter


ROOT = pathlib.Path(__file__).resolve().parent
DB = ROOT / "CORPUS_CATALOGUE_V2.sqlite"
CATALOGUE_RECEIPT = ROOT / "CATALOGUE_V2_RECEIPT.json"
TRANCHE_RECEIPT = ROOT / "UNCLASSIFIED_TRANCHE_2026-09-30.json"
TRANCHE_NOTE = ROOT / "UNCLASSIFIED_TRANCHE_2026-09-30.md"
SOURCE_READING_LEDGER = ROOT.parent / "ledgers" / "actual_source_readings.jsonl"
TRANCHE_ID = "largest-unclassified-tex-2026-09-30"

READING_SCOPE = (
    "Machine-assisted exact cue extraction with the cited line inspected; "
    "routing only, with no theorem, proof, or novelty claim accepted."
)
SELECTOR = (
    "The 40 largest distinct .tex versions carrying the unclassified lane, "
    "ordered by bytes descending and SHA-256 ascending."
)

GROUPS = {
    "navier_stokes_crossref": {
        "hashes": [
            "0b5b832e1845469b316b992880b4731a88681e018b58fd50f9f38e1c0a1ec263",
            "5069efa67392afec22071c53ebff691348895509a7b644449f0f16fed1ea6132",
        ],
        "cue": r"Finite-time Navier--Stokes construction",
        "routes": ["navier_stokes_crossref"],
        "basis": "The exact TeX title identifies a finite-time Navier--Stokes construction.",
    },
    "gct_bridge": {
        "hashes": [
            "809345c7a26f504c2f4a039deeaef2952875d9fc57823eced46b8cbd1bb82d9d",
            "f0186f2ae0f6460c8f32f15f4ca483726e6927d253f4b40bef87af9896a69a5d",
            "711fb66d8c7e746c07b150f0cc763872a910823710115dba3fec898c678aaea2",
            "85c33bd0d4698a6eee331395a709a7b1b63d8d5e0f5a21e725914aa40745f9b7",
            "8ad6ec76fccee67bd15c8d745622cdcd95dc7b3256abdec5a96e7570d752fcdd",
            "a484dfd6b90bb0fdece8d81db56894e174a17c779de3e846490849a47bfbca76",
        ],
        "cue": r"The nonstandard Riemann-hypothesis bridge in the original GCT sources",
        "routes": ["gct_arithmetic", "rh_heat_crossrefs"],
        "basis": (
            "An exact section heading identifies a nonstandard Riemann-hypothesis "
            "bridge in original GCT sources."
        ),
    },
    "gct_primary_source": {
        "hashes": [
            "5c5b990306c3b817d822df9f5088fdd42dda146fc3449155a0b2f6202d2ed49e",
        ],
        "cue": r"Geometric Complexity Theory IV: nonstandard quantum group for the Kronecker problem",
        "routes": ["gct_arithmetic"],
        "basis": (
            "The exact TeX title identifies Geometric Complexity Theory IV and the "
            "Kronecker problem; the source names Jonah Blasiak as author."
        ),
    },
    "s6_primary": {
        "hashes": [
            "618f89e57fc348363d736f1c7ed5d2180b366f7bd1d93aa11245378339ff83d9",
            "9f0f6ffd84958444b6dd917b9e3980b9433c0eba623ffc301058e0ed9349c9f4",
            "5337309a906f5755f07e23eb1a00219ed711bd6784d2487043b2e6dd716dde9f",
            "6c808fbe2e0c272bb03db9f36068d8a1fb6384f571695a21487dd06a83d6ce5e",
            "5360cbd3b765df3b72a43d3274cdf8926c3071b7a245ecf164d6c0582d5a0108",
            "0696b6b7fab83804dfec947d45607601e5d7f57d64c6148487969fccb6c67d2d",
            "6a4cfaf5cde8a4ee6a2258242a56602b25ed75e8b576c022961c7ddd8cb12cce",
            "5179236dd6b97a2b11a10335d9de31f01dfd563ec6e46c229c9ee15434fb6999",
            "5bf9b1ce68f88b8bad7f5ff27bde0bbce5f855aafa9220d324a737a91c206aa6",
            "79842421adf632fbc6b9e2b0af4126a60a0f8433d755a12beba44cb60140f77e",
            "c6b1527a0b6f01d81b08e02448b90edb2271d6a929a1875dc7464a4fcaeaaae0",
            "9e7a2edf8b95202033fb79bcdd1d69ae7b0edcf31e3605f9d538b72268233e63",
            "8d2a73b193729efd3fcfdb81e0c3a136ab4e967c5c4a60614cd001316877d2ff",
            "e73f6440c7dd387d2246867f813ac7dd57edb471d4340b51e1fd185ddd472eb1",
            "146271667491db204d193e26baabcf91c0ad83232cb49a9e70d0017ecf0e5fdd",
            "a616e01f953b736d38faa8fa7a1d25da0095ac34acc2bfe9cc5af6c49bf4bd66",
            "45775906d76e1bcc0672633db502172e35296287abbef48162b8453552ecf3bb",
            "161862bf54d9b85d36b571daf68b0568cc3237f9aa4125e861f4b1f8539bcc75",
            "0a29ad372e98c25a8d197d21fed939d8f693c3267ed193af755333e03d367bed",
            "a10f2c19bb98e66e06ba578e2c2dfcaa04684bc0e54bfaf29c3c5f0e3c8fd2c9",
            "af35f4ccb3b9459972767ef15e7347572688908be6c36234936f1f577b3c42f6",
            "a83f382d840521bf94edda4453b21394b0e0976a49df925a097dfa7f729ce0df",
            "c20f12fdaf68fe37ab9d19abc8c432f5c21f2974656cefed62e40307cc79841a",
        ],
        "cue": r"The period family over the thrice-punctured sphere",
        "routes": ["s6_primary"],
        "basis": (
            "The exact TeX contents identify the period family over the "
            "thrice-punctured sphere in the primary S6 construction."
        ),
    },
    "yang_mills_spectral": {
        "hashes": [
            "e035407b59854b77307ad1bb0021a4f834aa13231ca6028f2b8de5409ab5aba4",
            "a879df6e5730ad285a4227d288cf075e12a88199d0e6a75f62a120bdd7c60118",
            "cd50a03f474ca9355e9e68bd8a0c96941ac50934dbfd48b2b71f644d22f0637c",
            "6eb36d8f32c34722b18372fc6abe39e7399abbd1aa35c0b9d1ffc422eb944a70",
            "3473f6c98a1f28fde3cdf1a0cd84531d42202f12fbe4e832179a8dd5b1bfdec7",
            "d11ca5c215d88aae45dc771d12059f6f21c969e097e8c4425109ace41fa40d93",
            "97260f6d514849fa5611567d1997fc44a24ee8706737d26714a2b808da78e9f0",
            "b357a75da46d2f69199b23d5d2eb2e50f5c2074b278744f189b8d1429f2b2288",
        ],
        "cue": r"The retained cusp.*spatial refinement.*and the spectral measure",
        "routes": ["yang_mills_crossref", "cusp_spectral"],
        "basis": (
            "The exact TeX metadata identifies the retained cusp, spatial refinement, "
            "and spectral measure of the magnetic vacuum translation."
        ),
    },
}


def sha256_file(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def normalized_line(line: str) -> str:
    return " ".join(line.strip().split())


def first_occurrence(connection: sqlite3.Connection, sha256: str) -> dict[str, object]:
    query = """
        SELECT occurrence_kind, archive_sha256, archive_path, member_path, direct_ordinal
        FROM (
          SELECT 'direct' AS occurrence_kind,
                 a.sha256 AS archive_sha256,
                 a.archive_path AS archive_path,
                 d.member AS member_path,
                 d.archive_member_ordinal AS direct_ordinal
          FROM direct_text_occurrences AS d
          JOIN archives AS a ON a.sha256=d.archive_sha256
          WHERE d.sha256=?
          UNION ALL
          SELECT 'nested' AS occurrence_kind,
                 a.sha256 AS archive_sha256,
                 a.archive_path AS archive_path,
                 n.logical_path AS member_path,
                 d.archive_member_ordinal AS direct_ordinal
          FROM logical_nested_text_occurrences AS n
          JOIN direct_package_occurrences AS d
            ON d.id=n.direct_package_occurrence_id
          JOIN archives AS a ON a.sha256=d.archive_sha256
          WHERE n.text_sha256=?
        )
        ORDER BY archive_path, direct_ordinal, member_path
        LIMIT 1
    """
    row = connection.execute(query, (sha256, sha256)).fetchone()
    if row is None:
        raise RuntimeError(f"No custody occurrence found for {sha256}")
    return dict(row)


def all_expected_records() -> dict[str, dict[str, object]]:
    records: dict[str, dict[str, object]] = {}
    for group_name, group in GROUPS.items():
        for sha256 in group["hashes"]:
            if sha256 in records:
                raise RuntimeError(f"Duplicate configured hash: {sha256}")
            records[sha256] = {
                "group": group_name,
                "cue": group["cue"],
                "routes": list(group["routes"]),
                "basis": group["basis"],
            }
    if len(records) != 40:
        raise RuntimeError(f"Expected 40 configured versions, found {len(records)}")
    return records


def database_state_matches(
    connection: sqlite3.Connection, records: dict[str, dict[str, object]]
) -> bool:
    tables = {
        row[0]
        for row in connection.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        )
    }
    if not {"classification_tranches", "classification_evidence"} <= tables:
        return False
    tranche = connection.execute(
        "SELECT tranche_id, selector, reading_scope, version_count "
        "FROM classification_tranches WHERE tranche_id=?",
        (TRANCHE_ID,),
    ).fetchone()
    if tranche is None or tuple(tranche) != (TRANCHE_ID, SELECTOR, READING_SCOPE, 40):
        return False
    evidence_count = connection.execute(
        "SELECT COUNT(*) FROM classification_evidence WHERE tranche_id=?",
        (TRANCHE_ID,),
    ).fetchone()[0]
    if evidence_count != 40:
        return False
    for sha256, record in records.items():
        routes = {
            row[0]
            for row in connection.execute(
                "SELECT lane FROM topics WHERE sha256=?", (sha256,)
            )
        }
        if "unclassified" in routes or not set(record["routes"]) <= routes:
            return False
    return True


def main() -> None:
    records = all_expected_records()
    old_receipt = json.loads(CATALOGUE_RECEIPT.read_text(encoding="utf-8"))
    current_db_sha = sha256_file(DB)
    if current_db_sha != old_receipt["database"]["sha256"]:
        raise RuntimeError(
            "Catalogue receipt does not match the database before classification"
        )

    connection = sqlite3.connect(DB)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys=ON")

    selected = list(
        connection.execute(
            """
            SELECT v.sha256, v.bytes, v.lines, v.corpus_file
            FROM versions AS v
            JOIN topics AS t ON t.sha256=v.sha256
            WHERE t.lane='unclassified' AND lower(v.suffix)='.tex'
            ORDER BY v.bytes DESC, v.sha256 ASC
            LIMIT 40
            """
        )
    )
    already_applied = database_state_matches(connection, records)
    if not already_applied:
        selected_hashes = [row["sha256"] for row in selected]
        if selected_hashes != list(records):
            # The configuration is grouped semantically, while the selector is ordered by size.
            if set(selected_hashes) != set(records):
                missing = sorted(set(records) - set(selected_hashes))
                unexpected = sorted(set(selected_hashes) - set(records))
                raise RuntimeError(
                    f"Configured tranche differs from query: missing={missing}, "
                    f"unexpected={unexpected}"
                )
        if connection.execute(
            "SELECT COUNT(*) FROM topics WHERE lane='unclassified'"
        ).fetchone()[0] != 4268:
            raise RuntimeError("Unexpected unclassified baseline before first application")

    version_rows: list[dict[str, object]] = []
    for sha256, record in records.items():
        version = connection.execute(
            "SELECT sha256, bytes, lines, corpus_file FROM versions WHERE sha256=?",
            (sha256,),
        ).fetchone()
        if version is None:
            raise RuntimeError(f"Configured version is absent: {sha256}")
        path = pathlib.Path(version["corpus_file"])
        data = path.read_bytes()
        if hashlib.sha256(data).hexdigest() != sha256:
            raise RuntimeError(f"Source blob hash mismatch: {path}")
        text = data.decode("utf-8")
        cue_pattern = re.compile(str(record["cue"]), re.IGNORECASE)
        evidence = None
        for line_number, line in enumerate(text.splitlines(), 1):
            if cue_pattern.search(line):
                evidence = {
                    "line": line_number,
                    "text": normalized_line(line),
                }
                break
        if evidence is None:
            raise RuntimeError(f"Required cue missing from {sha256}: {record['cue']}")
        version_rows.append(
            {
                "sha256": sha256,
                "bytes": version["bytes"],
                "lines": version["lines"],
                "corpus_file": version["corpus_file"],
                "group": record["group"],
                "assigned_lanes": record["routes"],
                "basis": record["basis"],
                "evidence_pattern": record["cue"],
                "evidence_line": evidence["line"],
                "evidence_text": evidence["text"],
                "sample_occurrence": first_occurrence(connection, sha256),
            }
        )

    if not already_applied:
        with connection:
            connection.executescript(
                """
                CREATE TABLE IF NOT EXISTS classification_tranches(
                    tranche_id TEXT PRIMARY KEY,
                    selector TEXT NOT NULL,
                    reading_scope TEXT NOT NULL,
                    version_count INTEGER NOT NULL
                );
                CREATE TABLE IF NOT EXISTS classification_evidence(
                    tranche_id TEXT NOT NULL REFERENCES classification_tranches(tranche_id),
                    sha256 TEXT NOT NULL REFERENCES versions(sha256),
                    evidence_line INTEGER NOT NULL,
                    evidence_text TEXT NOT NULL,
                    evidence_pattern TEXT NOT NULL,
                    assigned_lanes_json TEXT NOT NULL,
                    PRIMARY KEY(tranche_id, sha256)
                );
                """
            )
            connection.execute(
                "INSERT INTO classification_tranches VALUES(?,?,?,?)",
                (TRANCHE_ID, SELECTOR, READING_SCOPE, 40),
            )
            for row in version_rows:
                connection.execute(
                    "DELETE FROM topics WHERE sha256=? AND lane='unclassified'",
                    (row["sha256"],),
                )
                for lane in row["assigned_lanes"]:
                    connection.execute(
                        "INSERT OR REPLACE INTO topics(sha256,lane,basis) VALUES(?,?,?)",
                        (row["sha256"], lane, row["basis"]),
                    )
                connection.execute(
                    "INSERT INTO classification_evidence VALUES(?,?,?,?,?,?)",
                    (
                        TRANCHE_ID,
                        row["sha256"],
                        row["evidence_line"],
                        row["evidence_text"],
                        row["evidence_pattern"],
                        json.dumps(row["assigned_lanes"], separators=(",", ":")),
                    ),
                )

    integrity = connection.execute("PRAGMA integrity_check").fetchone()[0]
    foreign_key_rows = list(connection.execute("PRAGMA foreign_key_check"))
    unclassified_after = connection.execute(
        "SELECT COUNT(*) FROM topics WHERE lane='unclassified'"
    ).fetchone()[0]
    lane_counts = {
        row[0]: row[1]
        for row in connection.execute(
            "SELECT lane, COUNT(*) FROM topics GROUP BY lane ORDER BY lane"
        )
    }
    evidence_count = connection.execute(
        "SELECT COUNT(*) FROM classification_evidence WHERE tranche_id=?",
        (TRANCHE_ID,),
    ).fetchone()[0]
    connection.close()

    if integrity != "ok" or foreign_key_rows:
        raise RuntimeError(
            f"Database validation failed: integrity={integrity}, fks={foreign_key_rows}"
        )
    if unclassified_after != 4228 or evidence_count != 40:
        raise RuntimeError(
            f"Unexpected final counts: unclassified={unclassified_after}, "
            f"evidence={evidence_count}"
        )

    size_order = {
        row["sha256"]: rank
        for rank, row in enumerate(
            sorted(version_rows, key=lambda item: (-item["bytes"], item["sha256"])), 1
        )
    }
    for row in version_rows:
        row["rank_in_tranche"] = size_order[row["sha256"]]
    version_rows.sort(key=lambda item: item["rank_in_tranche"])

    group_counts = Counter(row["group"] for row in version_rows)
    route_counts = Counter(
        lane for row in version_rows for lane in row["assigned_lanes"]
    )
    database_hash = sha256_file(DB)
    receipt = {
        "tranche_id": TRANCHE_ID,
        "selector": SELECTOR,
        "reading_scope": READING_SCOPE,
        "baseline_unclassified_versions": 4268,
        "routed_versions": 40,
        "remaining_unclassified_versions": unclassified_after,
        "group_counts": dict(sorted(group_counts.items())),
        "route_insert_counts": dict(sorted(route_counts.items())),
        "topic_lane_counts_after": lane_counts,
        "database": {
            "file": DB.name,
            "bytes": DB.stat().st_size,
            "sha256": database_hash,
            "integrity_check": integrity,
            "foreign_key_check_rows": len(foreign_key_rows),
        },
        "versions": version_rows,
    }
    TRANCHE_RECEIPT.write_text(
        json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    existing_ledger_keys: set[tuple[str, str]] = set()
    if SOURCE_READING_LEDGER.exists():
        for ledger_line in SOURCE_READING_LEDGER.read_text(encoding="utf-8").splitlines():
            if not ledger_line.strip():
                continue
            ledger_row = json.loads(ledger_line)
            existing_ledger_keys.add(
                (
                    str(ledger_row.get("canonical_source_id", "")),
                    str(ledger_row.get("receiving_work", "")),
                )
            )
    ledger_records = []
    for row in version_rows:
        key = (f"sha256:{row['sha256']}", TRANCHE_ID)
        if key in existing_ledger_keys:
            continue
        occurrence = row["sample_occurrence"]
        ledger_records.append(
            {
                "canonical_source_id": key[0],
                "source_task_id": "current-consolidation",
                "archive_sha256": occurrence["archive_sha256"],
                "member": occurrence["member_path"],
                "snapshot": row["corpus_file"],
                "source_file_sha256": row["sha256"],
                "read_lines": [[row["evidence_line"], row["evidence_line"]]],
                "coverage": (
                    "Exact classification cue line only; the remainder of this version "
                    "was not semantically read in this tranche."
                ),
                "receiving_work": TRANCHE_ID,
                "status": (
                    "actual bounded cue reading for routing only; no mathematical claim accepted"
                ),
                "recorded_date": "2026-09-30",
            }
        )
    if ledger_records:
        with SOURCE_READING_LEDGER.open("a", encoding="utf-8", newline="\n") as ledger:
            for ledger_record in ledger_records:
                ledger.write(json.dumps(ledger_record, ensure_ascii=False) + "\n")

    note_lines = [
        "# First evidence-backed tranche from the unclassified queue",
        "",
        f"**Tranche ID:** `{TRANCHE_ID}`  ",
        f"**Selector:** {SELECTOR}  ",
        f"**Audit boundary:** {READING_SCOPE}",
        "",
        "The tranche routes 40 distinct TeX byte versions and reduces the conservative "
        "unclassified lane from 4,268 to 4,228 versions. Classification preserves every "
        "hash and occurrence. It does not accept any source claim as proved.",
        "",
        "| Group | Distinct versions | Assigned lanes |",
        "|---|---:|---|",
    ]
    group_labels = {
        "navier_stokes_crossref": "Navier--Stokes construction",
        "gct_bridge": "GCT / nonstandard RH bridge",
        "gct_primary_source": "GCT primary source",
        "s6_primary": "Primary S6 construction",
        "yang_mills_spectral": "Yang--Mills cusp and spectral work",
    }
    for group_name in GROUPS:
        routes = ", ".join(f"`{x}`" for x in GROUPS[group_name]["routes"])
        note_lines.append(
            f"| {group_labels[group_name]} | {group_counts[group_name]} | {routes} |"
        )
    note_lines.extend(
        [
            "",
            "## Version-level evidence",
            "",
            "| Rank | SHA-256 | Bytes | Group | Cue line | Exact cue | Sample custody occurrence |",
            "|---:|---|---:|---|---:|---|---|",
        ]
    )
    for row in version_rows:
        occurrence = row["sample_occurrence"]
        cue = str(row["evidence_text"]).replace("|", "\\|")
        cue = cue if len(cue) <= 180 else cue[:177] + "..."
        archive_name = pathlib.Path(str(occurrence["archive_path"])).name
        member = str(occurrence["member_path"])
        custody = f"{archive_name} :: {member}".replace("|", "\\|")
        if len(custody) > 210:
            custody = custody[:207] + "..."
        note_lines.append(
            f"| {row['rank_in_tranche']} | `{row['sha256']}` | {row['bytes']:,} | "
            f"`{row['group']}` | {row['evidence_line']} | {cue} | {custody} |"
        )
    note_lines.extend(
        [
            "",
            "The JSON receipt retains the complete cue text, assigned lanes, source-blob "
            "path, and sample custody route for every version.",
            "",
        ]
    )
    TRANCHE_NOTE.write_text("\n".join(note_lines), encoding="utf-8")

    old_receipt["counts"]["unclassified_text_versions"] = unclassified_after
    old_receipt["counts"]["classification_tranche_versions"] = 40
    old_receipt["counts"]["topic_lane_counts"] = lane_counts
    old_receipt["validation"]["classification_evidence_rows"] = evidence_count
    old_receipt["validation"]["first_unclassified_tranche"] = TRANCHE_RECEIPT.name
    old_receipt["database"] = {
        "file": DB.name,
        "bytes": DB.stat().st_size,
        "sha256": database_hash,
    }
    CATALOGUE_RECEIPT.write_text(
        json.dumps(old_receipt, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "already_applied": already_applied,
                "routed_versions": 40,
                "remaining_unclassified": unclassified_after,
                "lane_counts": lane_counts,
                "database_sha256": database_hash,
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
