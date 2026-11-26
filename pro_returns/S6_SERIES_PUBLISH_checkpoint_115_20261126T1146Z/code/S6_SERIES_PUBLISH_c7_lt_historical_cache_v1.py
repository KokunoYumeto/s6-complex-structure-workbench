"""Decode exact connector results, check Git blobs, and retain LT inputs."""
from pathlib import Path
from hashlib import sha1, sha256
from datetime import datetime, timezone
from itertools import islice
import ast
import base64
import json

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT / "agents/continuation7_iii_invariant_chern_receiving"
P = "S6_SERIES_PUBLISH_III_02LT_"
calls = json.loads((ROOT / "code/S6_SERIES_PUBLISH_c7_lt_historical_fetch_v1.tool_result.json").read_text())
print("START", datetime.now(timezone.utc).isoformat())
for call in calls:
    assert call["status"] == "fulfilled"
    item = call["value"]
    response = item["response"]
    assert response["isError"] is False
    data = response["structuredContent"]
    assert data["encoding"] == "base64" and data["content"]
    raw = base64.b64decode(data["content"])
    blob = sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    assert blob == data["sha"]
    name = Path(item["request"]["path"]).name
    out = LANE / (P + "historical_" + name)
    assert not out.exists()
    out.write_bytes(raw)
    print("RETAINED", name, "bytes", len(raw), "lines", len(raw.splitlines()),
          "git_blob", blob, "SHA256", sha256(raw).hexdigest())
    if name.endswith(".py"):
        tree = ast.parse(raw.decode())
        imports = [node for node in tree.body if isinstance(node, (ast.Import, ast.ImportFrom))]
        print("IMPORT_METADATA", ast.unparse(ast.Module(body=imports, type_ignores=[])))
    else:
        obj = json.loads(raw)
        print("JSON_TOP_LEVEL", [(key, type(value).__name__, len(value) if hasattr(value, "__len__") else value)
                                 for key, value in obj.items()])
canonical = ROOT / "S6_SERIES_PUBLISH_III.tex"
assert sha256(canonical.read_bytes()).hexdigest() == "9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0"
with canonical.open() as stream:
    lines = list(islice(stream, 21275, 21291))
aux = "".join(lines).rstrip("\n")
out = LANE / (P + "released_following_auxiliary.tex")
assert not out.exists()
out.write_text(aux + "\n", newline="\n")
print("AUXILIARY_21276_21291_SHA_WITHOUT_FINAL_LF", sha256(aux.encode()).hexdigest())
print(aux)
print("PASS", datetime.now(timezone.utc).isoformat())
