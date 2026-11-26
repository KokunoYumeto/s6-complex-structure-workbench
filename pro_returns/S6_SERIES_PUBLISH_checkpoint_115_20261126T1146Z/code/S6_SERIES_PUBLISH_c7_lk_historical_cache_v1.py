#!/usr/bin/env python3
"""Retain exact pinned LK source/output bytes; expose only imported helpers."""
import ast
import base64
from datetime import datetime, timezone
from hashlib import sha1, sha256
from itertools import islice
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT / "agents/continuation7_iii_general_cusp_receiving"
P = "S6_SERIES_PUBLISH_III_02LK_"
calls = ROOT / "code/S6_SERIES_PUBLISH_c7_lk_historical_fetch_calls_v1.out"
rows = json.loads(calls.read_text())
assert len(rows) == 4
for item in rows:
    response = item["response"]
    assert response["isError"] is False
    data = response["structuredContent"]
    assert data["encoding"] == "base64"
    content = base64.b64decode(data["content"], validate=False)
    assert sha1(b"blob "+str(len(content)).encode()+b"\0"+content).hexdigest() == data["sha"]
    assert item["request"]["ref"] == "a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7"
    name = Path(item["request"]["path"]).name
    target = LANE / (P+"historical_"+name)
    assert not target.exists()
    target.write_bytes(content)
    assert target.read_bytes() == content
    print("RETAINED", target.name, "bytes", len(content), "lines", len(content.splitlines()))
    print("GIT_BLOB", data["sha"], "SHA256", sha256(content).hexdigest())
    if name in ("manifolds_rankone_families.py", "manifolds_weighted_profiles.py"):
        wanted = "wedge" if "rankone" in name else "group"
        source = content.decode()
        tree = ast.parse(source)
        definition = next(node for node in tree.body
                          if isinstance(node, ast.FunctionDef) and node.name == wanted)
        text = "\n".join(source.splitlines()[definition.lineno-1:definition.end_lineno])+"\n"
        helper = LANE / (P+"historical_helper_"+wanted+".py")
        helper.write_text(text)
        print("HELPER", name, wanted, definition.lineno, definition.end_lineno)
        print(text, end="")
        print("IMPORT_METADATA", ast.unparse(ast.Module(
            body=[node for node in tree.body if isinstance(node, (ast.Import, ast.ImportFrom))],
            type_ignores=[])))
can = ROOT / "S6_SERIES_PUBLISH_III.tex"
assert sha256(can.read_bytes()).hexdigest() == "9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0"
with can.open() as f:
    auxiliary = "".join(islice(f, 17863, 17873)).rstrip("\n")
assert len(auxiliary.splitlines()) == 10
assert auxiliary.startswith("The complete Laurent-unimodular operations,")
assert auxiliary.endswith(r"the actual cap torsion $\mathbb Z/s$.")
(LANE/(P+"released_auxiliary.tex")).write_text(auxiliary+"\n")
print("AUXILIARY_GUARD", 17864, 17873, sha256(auxiliary.encode()).hexdigest())
print(auxiliary)
(ROOT / "code/S6_SERIES_PUBLISH_c7_lk_historical_fetch_calls_v1.err").write_bytes(b"")
print("PASS all four complete connector payloads decoded and Git-blob verified")
print("READ_SCOPE complete main source next; helper definitions printed; full helper bodies not printed")
print("COMPLETED_UTC", datetime.now(timezone.utc).isoformat())
