#!/usr/bin/env python3
"""Prepare four reviewed candidate10 guards; never mutate canonical records."""
from pathlib import Path
import csv
import difflib
import hashlib
import json
import re
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "S6_SERIES_PUBLISH_III.tex"
EXPECTED = "5a95d62059fcaf7859df33f5793d9cd97462024d50a1f7ee59f9fae0b2704187"
OUT = ROOT / "agents/continuation9_candidate10_small_roles"
STEM = "S6_SERIES_PUBLISH_c9_candidate10_small_roles"
IMAGE_REVIEW = "agents/continuation9_reading_thirdquarter/S6_SERIES_PUBLISH_c9_candidate10_pages526_614_review.md"
REVIEW = f"agents/continuation9_candidate10_small_roles/{STEM}_review.md"
TMP = ROOT.parents[1] / "tmp/c9_candidate10_small_roles"
DEFECT_FIELDS = ["change_id", "type", "statement_id", "old_location", "old_page",
                 "new_location", "new_page", "old_text", "new_text", "reason",
                 "review_status"]
EVENT_FIELDS = ["statement_id", "date", "who", "type", "outcome", "event_id",
                "phase", "source_file", "source_row", "source_event_type",
                "evidence_group", "publish_input_file", "publish_input_row",
                "date_utc", "where"]

def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()

def tsv(path, rows, fields):
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        for row in rows:
            w.writerow({k: str(row[k]).replace("\\", "\\\\").replace("\t", "\\t").replace("\n", "\\n")
                        if k in {"old_text", "new_text"} else row[k] for k in fields})

def main():
    src = SOURCE.read_text()
    assert sha(src) == EXPECTED
    assert "\r" not in src
    start = src.index(r"\begin{theorem}[The full external smash pairing is zero]")
    stop = src.index(r"\end{proof}", start) + len(r"\end{proof}")
    baseline = src[start:stop] + "\n"
    blocks = re.findall(r"\x60{3}tex\n(.*?)\x60{3}", (ROOT / IMAGE_REVIEW).read_text(), re.S)
    assert len(blocks) == 6
    rows = []
    specs = [
        ("III-C9-CURRENT10-02SA-TYPE-01", "night:P3F.33", "590",
         "The adjoining relation n gamma=0 and quotient v->psi(v) modulo n, alpha->0, with inverse 1->[e_gamma], identify the prose gamma with the same marked surviving generator. The identity on that cyclic quotient and its inverse is retained; only mathematical typography changes."),
        ("III-C9-CURRENT10-02SB-TYPE-01", "night:P3F.34", "592",
         "The marked exterior H1(V)=Z coordinate is psi with inverse 1->[e_gamma]; the later pair sequence sends beta to -n gamma. Set the identical generator in mathematical typography, preserving the quotient, inverse and sign."),
        ("III-C9-CURRENT10-02SB-TYPE-02", "night:P3F.34", "592",
         "The displayed boundary basis binds v2=(psi+u)w and q=eta h/3; beta_{m,n,d}=m alpha-ell=-nu_+ is the clockwise normal action and m=3k. Set the same w, beta, q, k and d in mathematical typography. All four transfer formulas, the circle-parameter reversal and Thom sign remain identical.")
    ]
    for i, (cid, owner, page, reason) in enumerate(specs):
        old, new = blocks[2*i:2*i+2]
        assert src.count(old) == 1 and old != new
        lineno = src[:src.index(old)].count("\n") + 1
        rows.append(dict(change_id=cid, type="D23", statement_id=owner,
            old_location=f"Candidate10 complete actual page {page}; source line {lineno}, exact bound prose context",
            old_page=page, new_location="Same bound objects and full source context",
            new_page="pending successor build and actual changed-page reading",
            old_text=old, new_text=new,
            reason=reason + " Actual full-page reading and bounded source bindings: " + IMAGE_REVIEW,
            review_status="proposed; actual image and bounded source comparison complete; no mathematical event; root admission and changed-page reading pending"))
    old = ("Since $12[x]=0$ and $R_*$ is a homomorphism, writing\n"
           "$R_*[x]=a\\nu$ gives $24\\mid12a$, hence $2\\mid a$.\n")
    new = ("Since $12[x]=0$ and $R_*$ is a homomorphism, writing\n"
           "$R_*[x]=a_{\\rm cyc}\\nu$ gives $24\\mid12a_{\\rm cyc}$, hence $2\\mid a_{\\rm cyc}$.\n")
    assert baseline.count(old) == 1
    assert new.count(r"a_{\rm cyc}") == 3
    assert new.replace(r"a_{\rm cyc}", "a") == old
    lineno = src[:src.index(old)].count("\n") + 1
    rows.append(dict(change_id="III-C9-CURRENT10-038V-ROLE-01", type="D20",
        statement_id="wb:cusp-s12-full-carrier-null",
        old_location=f"Full 038V statement/proof; cyclic-coordinate clause at source {lineno}; root actual pages618–619 triggered review",
        old_page="618–619; root image reader",
        new_location="Same cyclic coordinate and divisibility clause; formal block dimensions retained",
        new_page="pending successor build and actual changed-page reading",
        old_text=old, new_text=new,
        reason="The earlier tau_{a,b} takes positive integer dimensions and swaps the ordered cube blocks, with inverse tau_{b,a}. The later a is the chosen integer representative of the cyclic coordinate of R_*[x] under [j]_24->j nu. Rename exactly its three coefficient/divisibility uses to a_cyc. The integer representative map a->a_cyc=a and inverse a_cyc->a preserve its class modulo24, 24|12a, 2|a, the even-subgroup coordinate and all smash/homotopy maps. Full original/proposed owner, Q253 and all three direct caller contexts were read; " + REVIEW,
        review_status="proposed; full exposed statement/proof and caller comparison; exact source reversal; no independent proof credit; root admission and successor-image gate pending"))
    candidate = src
    for row in rows:
        assert candidate.count(row["old_text"]) == 1
        candidate = candidate.replace(row["old_text"], row["new_text"], 1)
        assert candidate.count(row["new_text"]) == 1
    reverse = candidate
    for row in reversed(rows):
        reverse = reverse.replace(row["new_text"], row["old_text"], 1)
    assert reverse == src
    proposed = baseline.replace(old, new, 1)
    assert proposed.replace(r"a_{\rm cyc}", "a") == baseline
    target_re = r"\\(?:label|hypertarget|(?:c|eq|C|Series)?ref)\{[^}]+\}|\\(?:begin|end)\{[^}]+\}"
    assert re.findall(target_re, src) == re.findall(target_re, candidate)
    assert re.findall(r"\d+", src) == re.findall(r"\d+", candidate)
    assert sha(SOURCE.read_text()) == EXPECTED
    OUT.mkdir(parents=True, exist_ok=True)
    TMP.mkdir(parents=True, exist_ok=True)
    (TMP / f"{STEM}_038V_original.tex").write_text(baseline)
    (TMP / f"{STEM}_038V_proposed.tex").write_text(proposed)
    payload = dict(source_file=SOURCE.name, source_sha256=EXPECTED,
        proposed_source_sha256=sha(candidate),
        owner_scope={"statement_id": "wb:cusp-s12-full-carrier-null",
                     "containing_unit": "wb:cusp-s12-full-carrier-null",
                     "original_lines": len(baseline.splitlines()),
                     "proposed_lines": len(proposed.splitlines()),
                     "original_sha256": sha(baseline), "proposed_sha256": sha(proposed),
                     "original_path": str(TMP / f"{STEM}_038V_original.tex"),
                     "proposed_path": str(TMP / f"{STEM}_038V_proposed.tex")},
        proposals=rows)
    (OUT / f"{STEM}.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    tsv(OUT / f"{STEM}_defects.tsv", rows, DEFECT_FIELDS)
    (OUT / f"{STEM}.diff").write_text("".join(difflib.unified_diff(
        src.splitlines(keepends=True), candidate.splitlines(keepends=True),
        fromfile=SOURCE.name, tofile=SOURCE.name+".proposed", n=3)))
    now = datetime.now(timezone.utc).isoformat()
    eid = "publish:c9:III:038V:cyclic-coefficient"
    event = dict(statement_id="wb:cusp-s12-full-carrier-null", date=now[:10],
        who="GPT-6 Astra (OpenAI), ChatGPT Pro mode; continuation nine",
        type="used and rechecked in this run",
        outcome=f"Read the complete {len(baseline.splitlines())}-line current 038V statement/proof and its complete proposed scope, the ordered-cube definition Q253 and all three direct caller contexts. Rechecked the ordered smash factorization, right/left suspension transport, both pinch homomorphisms, cyclic coordinate and inverse, and the exact three-use coefficient qualification. The block-twist dimension inputs retain their actual positive-integer domains, coordinate permutation and inverse. All maps, entries, divisibility assertions, target identifiers and public conclusions are retained. This is exposed comparison following root's actual images618–619 and earlier source knowledge; no independent proof or new image credit. Root admission and successor changed-page reading remain pending.",
        event_id=eid, phase="publication continuation9", source_file=SOURCE.name,
        source_row="038V complete statement/proof; III-C9-CURRENT10-038V-ROLE-01",
        source_event_type="used and rechecked in this run", evidence_group=eid,
        publish_input_file="../CLAUDE_READING_LOG_PAPER_III.md",
        publish_input_row="P15; prompt0.8 complete proof scope; root candidate10 pages618–619",
        date_utc=now,
        where=f"code/{STEM}.py; code/{STEM}.out; {REVIEW}; agents/continuation9_candidate10_small_roles/{STEM}_defects.tsv; {IMAGE_REVIEW}")
    with (OUT / f"{STEM}_events.tsv").open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=EVENT_FIELDS,delimiter="\t",lineterminator="\n")
        w.writeheader();w.writerow(event)
    print(json.dumps({k:v for k,v in payload.items() if k!="proposals"}, indent=2))
    print("Four unique forward/reverse guards; whole-source literal reversal; ordered identifiers, environments and integers PASS.")
    print("038V coefficient occurrences: exactly3; inverse qualification recovers complete owner PASS.")
    print("D23 typography rows3, no events; D20 role row1, exposed owner event1.")
    print("Canonical source/defects/events/counts/statuses untouched.")
    for row in rows:
        print(row["change_id"], row["type"], row["statement_id"], row["old_location"])

if __name__ == "__main__":
    main()
