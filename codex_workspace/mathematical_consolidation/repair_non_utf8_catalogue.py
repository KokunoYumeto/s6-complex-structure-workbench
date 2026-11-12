import hashlib
import json
import pathlib
import re
import sqlite3


ROOT = pathlib.Path(__file__).resolve().parent
DB_PATH = ROOT / "CORPUS_CATALOGUE.sqlite"
RECEIPT_PATH = ROOT / "CATALOGUE_RECEIPT.json"
OUT_PATH = ROOT / "ENCODING_RECOVERY_RECEIPT.json"

RECOVERIES = {
    "18d7f1a808d0a73f89b655095afd895b66ddc58ba26c4ab8c48b792c64b86d76": {
        "encoding": "cp932",
        "evidence": "the only non-ASCII byte pair is 81 40, which decodes to U+3000 and round-trips exactly",
        "lanes": ["lattice_jordan", "quaternionic_gauge"],
        "routing_basis": "decoded title and contents: Exceptional Lie groups, Cayley algebra, triality, and the groups G2 through E8",
    },
    "ce87e34046d5dee45d8ca604276c8d70b5bdf4b571767f0ff84a4801ec089038": {
        "encoding": "cp1252",
        "evidence": "the only non-ASCII byte is B0 in the bibliographic abbreviation n-degree-sign; decoding and re-encoding round-trip exactly",
        "lanes": ["rh_heat_crossrefs"],
        "routing_basis": "decoded title and author fields: From Physics to Number Theory via Noncommutative Geometry, Connes and Marcolli",
    },
}


def line_at(text, offset):
    return text.count("\n", 0, offset) + 1


def extract_tex(db, digest, text, encoding):
    counts = {"display": 0, "statement_or_note": 0, "proof": 0, "heading": 0, "references": 0}
    unmatched_end = 0
    stack = []
    for match in re.finditer(r"\\(begin|end)\s*\{([^{}]+)\}", text):
        action, environment = match.groups()
        if action == "begin":
            stack.append((environment, match.start()))
        elif stack and stack[-1][0] == environment:
            environment, start = stack.pop()
            if re.search(
                r"theorem|lemma|proposition|corollary|definition|remark|proof|counterexample|auditrecord|sourcequote|equation|eqnarray|displaymath|align|gather|multline",
                environment,
                re.I,
            ):
                span = text[start : match.end()]
                if re.search("proof", environment, re.I):
                    kind = "proof"
                elif re.search("equation|eqnarray|displaymath|align|gather|multline", environment, re.I):
                    kind = "display"
                else:
                    kind = "statement_or_note"
                db.execute(
                    "insert into spans(sha256,kind,name,start_line,end_line,start_offset,end_offset,span_sha256,status) values(?,?,?,?,?,?,?,?,?)",
                    (
                        digest,
                        kind,
                        environment,
                        line_at(text, start),
                        line_at(text, match.end()),
                        start,
                        match.end(),
                        hashlib.sha256(span.encode("utf-8")).hexdigest(),
                        f"lexical span decoded losslessly as {encoding}; not independently audited",
                    ),
                )
                counts[kind] += 1
        else:
            unmatched_end += 1

    for match in re.finditer(
        r"\\(section|subsection|subsubsection|paragraph|chapter)\*?\s*(?:\[[^\]]*\])?\s*\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}",
        text,
    ):
        db.execute(
            "insert into spans(sha256,kind,name,start_line,end_line,start_offset,end_offset,span_sha256,status) values(?,?,?,?,?,?,?,?,?)",
            (
                digest,
                "heading",
                match.group(2),
                line_at(text, match.start()),
                line_at(text, match.end()),
                match.start(),
                match.end(),
                hashlib.sha256(match.group().encode("utf-8")).hexdigest(),
                f"literal heading decoded losslessly as {encoding}; topic routing only",
            ),
        )
        counts["heading"] += 1

    manual_pattern = re.compile(
        r"\{\\bf\s+(Theorem|Proposition|Lemma|Corollary|Definition|Remark|Proof)\b([^\n]{0,300})",
        re.I,
    )
    for match in manual_pattern.finditer(text):
        heading_type = match.group(1).lower()
        kind = "manual_proof_locator" if heading_type == "proof" else "manual_statement_locator"
        db.execute(
            "insert into spans(sha256,kind,name,start_line,end_line,start_offset,end_offset,span_sha256,status) values(?,?,?,?,?,?,?,?,?)",
            (
                digest,
                kind,
                match.group().strip(),
                line_at(text, match.start()),
                line_at(text, match.end()),
                match.start(),
                match.end(),
                hashlib.sha256(match.group().encode("utf-8")).hexdigest(),
                f"manual {heading_type} heading located after lossless {encoding} decoding; body boundary not inferred and claim not audited",
            ),
        )
        counts[kind] = counts.get(kind, 0) + 1

    for match in re.finditer(
        r"\\(label|ref|eqref|cref|Cref|input|include|cite[a-zA-Z]*)\*?\s*(?:\[[^\]]*\]\s*)*\{([^{}]+)\}",
        text,
    ):
        kind, target = match.groups()
        targets = [target] if kind in ["input", "include"] else target.split(",")
        for part in targets:
            db.execute(
                "insert into references_found(sha256,kind,target,line) values(?,?,?,?)",
                (digest, kind, part.strip(), line_at(text, match.start())),
            )
            counts["references"] += 1
    counts["unclosed_begin"] = len(stack)
    counts["unmatched_end"] = unmatched_end
    return counts


db = sqlite3.connect(DB_PATH)
records = []
for digest, specification in RECOVERIES.items():
    row = db.execute(
        "select corpus_file,bytes,suffix,lexical_status from versions where sha256=?", (digest,)
    ).fetchone()
    if row is None:
        raise RuntimeError(f"catalogue version missing: {digest}")
    corpus_file, expected_bytes, suffix, prior_status = row
    path = pathlib.Path(corpus_file)
    raw = path.read_bytes()
    if len(raw) != expected_bytes or hashlib.sha256(raw).hexdigest() != digest:
        raise RuntimeError(f"exact-byte verification failed: {path}")
    encoding = specification["encoding"]
    text = raw.decode(encoding)
    if text.encode(encoding) != raw:
        raise RuntimeError(f"lossless encoding round trip failed: {path}")
    db.execute("delete from spans where sha256=?", (digest,))
    db.execute("delete from references_found where sha256=?", (digest,))
    db.execute(
        "update versions set lines=?,lexical_status=? where sha256=?",
        (
            len(text.splitlines()),
            f"losslessly decoded as {encoding}; source bytes unchanged; exact round trip verified",
            digest,
        ),
    )
    extracted = extract_tex(db, digest, text, encoding)
    db.execute("delete from topics where sha256=? and lane='unclassified'", (digest,))
    for lane in specification["lanes"]:
        db.execute(
            "insert or replace into topics(sha256,lane,basis) values(?,?,?)",
            (digest, lane, specification["routing_basis"]),
        )
    records.append(
        {
            "sha256": digest,
            "source_file": str(path),
            "bytes": len(raw),
            "lines": len(text.splitlines()),
            "suffix": suffix,
            "encoding": encoding,
            "encoding_evidence": specification["evidence"],
            "prior_status": prior_status,
            "source_bytes_changed": False,
            "exact_round_trip": True,
            "lexical_extraction": extracted,
        }
    )

db.commit()
integrity = db.execute("pragma integrity_check").fetchone()[0]
if integrity != "ok":
    raise RuntimeError(integrity)
undecoded = db.execute("select count(*) from versions where lines is null").fetchone()[0]
if undecoded != 0:
    raise RuntimeError(f"unexpected undecoded versions remain: {undecoded}")

receipt = json.loads(RECEIPT_PATH.read_text(encoding="utf-8"))
counts = receipt["counts"]
counts["unique_versions"] = db.execute("select count(*) from versions where lines is not null").fetchone()[0]
counts["unique_versions_including_undecoded"] = db.execute("select count(*) from versions").fetchone()[0]
counts["tex_versions"] = db.execute("select count(*) from versions where suffix='.tex' and lines is not null").fetchone()[0]
counts["undecoded_text_versions"] = undecoded
counts["spans_display"] = db.execute("select count(*) from spans where kind='display'").fetchone()[0]
counts["spans_statement_or_note"] = db.execute("select count(*) from spans where kind='statement_or_note'").fetchone()[0]
counts["spans_proof"] = db.execute("select count(*) from spans where kind='proof'").fetchone()[0]
counts["spans_manual_statement_locator"] = db.execute("select count(*) from spans where kind='manual_statement_locator'").fetchone()[0]
counts["spans_manual_proof_locator"] = db.execute("select count(*) from spans where kind='manual_proof_locator'").fetchone()[0]
counts["catalogue_spans"] = db.execute("select count(*) from spans").fetchone()[0]
counts["literal_reference_records"] = db.execute("select count(*) from references_found").fetchone()[0]
for lane in receipt["overlapping_routing_lanes"]:
    receipt["overlapping_routing_lanes"][lane] = db.execute(
        "select count(*) from topics where lane=?", (lane,)
    ).fetchone()[0]
receipt["sqlite_integrity"] = integrity
receipt["encoding_recovery"] = {
    "receipt": OUT_PATH.name,
    "recovered_non_utf8_versions": len(records),
    "undecoded_versions_remaining": undecoded,
    "source_bytes_changed": False,
}
RECEIPT_PATH.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

recovery_receipt = {
    "scope": "the two exact TeX byte versions rejected by strict UTF-8 decoding",
    "method": "explicit encoding identification, exact decode/encode round trip, literal TeX extraction, and routing-only manual heading locators for non-environment theorem styles",
    "records": records,
    "sqlite_integrity": integrity,
    "undecoded_versions_remaining": undecoded,
}
OUT_PATH.write_text(json.dumps(recovery_receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
db.close()
print(json.dumps(recovery_receipt, ensure_ascii=False))
