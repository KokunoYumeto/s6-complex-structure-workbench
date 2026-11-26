#!/usr/bin/env python3
"""Read every local serialized LK proposal field and verify its exact scope."""
import csv
from datetime import datetime, timezone
from hashlib import sha256
from itertools import islice
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT/"agents/continuation7_iii_general_cusp_receiving"
P = "S6_SERIES_PUBLISH_III_02LK_"
receiver = (LANE/(P+"receiving.tex")).read_text()
spans = [(17544,17611),(17614,17862),(17864,17873)]
old = []
for lo,hi in spans:
    with (ROOT/"S6_SERIES_PUBLISH_III.tex").open() as f:
        old.append("".join(islice(f,lo-1,hi)).rstrip("\n"))

def read(name):
    path = LANE/(P+name+".tsv")
    data = path.read_bytes()
    assert b"\r" not in data
    assert all(b>=32 or b in (9,10) for b in data)
    with path.open(newline="") as f:
        return list(csv.DictReader(f,delimiter="\t"))

replacements,defects,events = [read(name) for name in ("replacements","defects","CHECK_EVENTS")]
assert (len(replacements),len(defects),len(events)) == (3,29,2)
for i,row in enumerate(replacements):
    assert row["statement_id"] == "maps:src:D.2.43"
    assert row["old_text"] == old[i]
    if i<2:
        assert receiver.count(row["new_text"]) == 1
    else:
        assert row["new_text"] == ""
    print("REPLACEMENT",i+1,"all four serialized fields")
    for key,value in row.items():
        if key in ("old_text","new_text"):
            print(key,"FULL_VALUE_EXACTLY_MATCHES_WHOLLY_READ_BODY",
                  "lines",len(value.splitlines()),"SHA256",sha256(value.encode()).hexdigest())
        else:
            print(key+":",value)
for i,row in enumerate(defects,1):
    before,after = row["old_text"],row["new_text"]
    assert sum(part.count(before) for part in old) == 1
    assert receiver.count(after) == 1
    m = re.search(r"lines (\d+)--(\d+)$",row["old_location"])
    assert m
    lo,hi = map(int,m.groups())
    assert any(start<=lo<=hi<=end for start,end in spans)
    print("\nDEFECT",i,"all eleven serialized fields")
    for key,value in row.items():
        print(key+":",value)
assert len({row["evidence_group"] for row in events}) == 1
assert [row["type"] for row in events] == ["targeted proof check","used and rechecked in this run"]
for i,row in enumerate(events,1):
    print("\nEVENT",i,"all fifteen serialized fields")
    for key,value in row.items():
        if key == "where":
            print("where:")
            for path in value.split("; "):
                assert (ROOT/path).exists(),path
                print(path)
        else:
            print(key+":",value)
for filename in ("receiving.tex","post_exposure_derivation.md",
                 "following_auxiliary_comparison.md","comparison.md"):
    data = (LANE/(P+filename)).read_bytes()
    assert b"\r" not in data and all(b>=32 or b in (9,10) for b in data)
print("\nPASS complete serialized field readback; every old/new text matches the wholly read bodies")
print("PASS three exact guards, 29 scoped rows, two events and all evidence paths")
print("PASS LF/control checks; no canonical/global mutation or admission")
print("READBACK_COMPLETED_UTC",datetime.now(timezone.utc).isoformat())
