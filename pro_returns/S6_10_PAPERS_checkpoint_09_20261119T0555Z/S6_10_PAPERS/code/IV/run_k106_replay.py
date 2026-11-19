"""Replay selected finite certificates with separate current execution receipts."""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess
import sys
import time

W = Path(__file__).resolve().parents[2]
T = W / "code/IV/replay_cp29_k106"
prepared = json.loads((T / "source_manifest.json").read_text())
original = {x["path"]: x["sha256"] for x in prepared["files"]}
logdir = T / "execution_logs"
logdir.mkdir(exist_ok=True)
results = []
def timestamp():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()
def save():
    out = {"source_checkpoint": 29, "checker": "GPT-6 Astra Pro (OpenAI, ChatGPT; current writing)",
           "scope": "Current unchanged-program execution only. Mathematical arguments and historical audits have separate records.",
           "updated_at": timestamp(), "results": results}
    (T / "current_results.json").write_text(json.dumps(out, indent=2) + "\n")

for rel in prepared["programs"]:
    p = T / rel
    before = hashlib.sha256(p.read_bytes()).hexdigest()
    assert before == original[rel], (rel, "source program modified")
    started = timestamp()
    tic = time.monotonic()
    logfile = logdir / (p.stem + ".log")
    print(json.dumps({"program": rel, "started_at": started}), flush=True)
    with logfile.open("w") as f:
        done = subprocess.run([sys.executable, str(p)], cwd=T, stdout=f, stderr=subprocess.STDOUT)
    row = {"program": rel, "source_sha256": before, "started_at": started,
           "completed_at": timestamp(), "seconds": round(time.monotonic() - tic, 3),
           "exit_code": done.returncode, "log": str(logfile.relative_to(T)),
           "log_sha256": hashlib.sha256(logfile.read_bytes()).hexdigest()}
    q = p.with_suffix(".json")
    if done.returncode == 0 and q.exists():
        x = json.loads(q.read_text())
        row.update(output=str(q.relative_to(T)), output_sha256=hashlib.sha256(q.read_bytes()).hexdigest())
        for k in ["status", "checks", "regular_cones", "surface_count", "compact_curve_count", "canonical_fans", "unimodular_inputs", "witness_max_depth", "distinct_target_fans"]:
            if k in x and isinstance(x[k], (str, int, float)):
                row[k] = x[k]
    assert hashlib.sha256(p.read_bytes()).hexdigest() == before
    results.append(row)
    save()
    print(json.dumps(row), flush=True)
    if done.returncode:
        print(logfile.read_text()[-9000:], flush=True)
        raise SystemExit(done.returncode)
print(json.dumps({"complete": True, "programs": len(results), "completed_at": timestamp()}), flush=True)
