"""Execute the wholly read historical LT source without changing its bytes."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT / "agents/continuation7_iii_invariant_chern_receiving"
P = "S6_SERIES_PUBLISH_III_02LT_"
source = LANE / (P + "historical_III_invariant_chern_cone_fresh.py")
saved = LANE / (P + "historical_III_invariant_chern_cone_fresh.json")
runtime = ROOT / "code/S6_SERIES_PUBLISH_c7_lt_historical_runtime_v1"
assert not runtime.exists()
(runtime / "code/outputs").mkdir(parents=True)
script = runtime / "code/S6_SERIES_PUBLISH_III_02LT_historical_main.py"
raw = source.read_bytes()
assert sha256(raw).hexdigest() == "6e401c84a466445c4b4c377d0e7c9704090fd984222daf3d6507d8682b7a029e"
script.write_bytes(raw)
assert script.read_bytes() == raw
stdout = ROOT / "code/S6_SERIES_PUBLISH_c7_lt_historical_main_v1.out"
stderr = ROOT / "code/S6_SERIES_PUBLISH_c7_lt_historical_main_v1.err"
print("START", datetime.now(timezone.utc).isoformat(), flush=True)
print("SOURCE_BYTE_EQUAL", len(raw), sha256(raw).hexdigest(), flush=True)
print("ISOLATED_SOURCE", script.relative_to(ROOT), flush=True)
with stdout.open("wb") as out, stderr.open("wb") as err:
    result = subprocess.run([sys.executable, "-u", str(script)], cwd=runtime,
                            stdout=out, stderr=err, check=False)
print("ACTUAL_EXIT", result.returncode, flush=True)
assert result.returncode == 0
generated = runtime / "code/outputs/III_invariant_chern_cone_fresh.json"
generated_raw = generated.read_bytes()
saved_raw = saved.read_bytes()
assert generated_raw == saved_raw
print("SAVED_JSON_BYTE_EQUAL", len(generated_raw), sha256(generated_raw).hexdigest())
print("HISTORICAL_STDOUT", stdout.stat().st_size, sha256(stdout.read_bytes()).hexdigest())
print("HISTORICAL_STDERR", stderr.stat().st_size, sha256(stderr.read_bytes()).hexdigest())
obj = json.loads(generated_raw)
print("EXACT_RESULT", json.dumps({key: obj[key] for key in ("status", "assertions", "counts", "scope")}))
print("PASS", datetime.now(timezone.utc).isoformat())
