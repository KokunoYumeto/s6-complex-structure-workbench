"""Prepare an isolated, byte-identical checkpoint29 certificate replay tree."""
from pathlib import Path
import ast
import datetime
import hashlib
import json
import shutil

W = Path(__file__).resolve().parents[2]
R = W.parents[1]
SOURCE = R / "sources/newer_night/checkpoint29"
TARGET = W / "code/IV/replay_cp29_k106"
PROGRAMS = [
    "code/part3/e6_selected_i3_infinity_fan.py",
    "code/part3/e6_selected_i3_common_fan.py",
    "code/part3/e6_selected_i3_corner_lifts.py",
    "code/part3/e6_selected_i3_p_one_cayley.py",
    "code/part3/e6_selected_i3_generic_corner_index.py",
    "code/part3/e6_selected_i3_fixed_faces.py",
    "code/part3/e6_selected_i3_fixed_curve_normals.py",
    "code/part3/e6_selected_i3_fixed_surfaces.py",
    "code/part3/e6_selected_i3_moving_star.py",
    "code/part3/e6_selected_i3_p_one_lower.py",
    "code/part3/e6_selected_i3_lower_relative.py",
    "code/part3/e6_selected_i3_moving_cap.py",
    "code/part3/e6_selected_i3_outer_transfer.py",
    "code/part3/e6_selected_i3_first_flop.py",
    "code/part3/e6_selected_i3_vertical_fans.py",
    "code/part3_root/e6_selected_i3_moving_c2.py",
    "code/part3_root/e6_selected_i3_vertical_integer.py",
    "code/part3/e6_selected_i3_all_fans.py",
    "code/part3_root/e6_selected_i3_all28_peer.py",
    "code/part3/iv_star_complement.py",
    "code/part3/iii_star_good_complement.py",
    "code/part3/iv_star_iii_joint.py",
]

queue = [Path(p) for p in PROGRAMS]
seen = set()
manifest = []
while queue:
    rel = queue.pop(0)
    if rel in seen:
        continue
    seen.add(rel)
    p = SOURCE / rel
    assert p.is_file(), p
    data = p.read_bytes()
    q = TARGET / rel
    q.parent.mkdir(parents=True, exist_ok=True)
    if q.exists():
        assert q.read_bytes() == data, f"Refusing to overwrite an existing replay output: {q}"
    else:
        shutil.copyfile(p, q)
    manifest.append({"path": str(rel), "bytes": len(data),
                     "sha256": hashlib.sha256(data).hexdigest()})
    if rel.suffix != ".py":
        continue
    tree = ast.parse(data.decode())
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            s = node.value
            if len(s) > 300 or "\n" in s or not s.endswith((".py", ".json", ".md", ".tex", ".txt")):
                continue
            candidates = [Path(s)] if s.startswith(("code/", "notes/", "records/")) else [rel.parent / s]
            for dep in candidates:
                if (SOURCE / dep).is_file() and dep not in seen:
                    queue.append(dep)
    # The old symbolic programs import helpers from their own directory.
    for node in ast.walk(tree):
        names = []
        if isinstance(node, ast.Import):
            names = [a.name.split(".")[0] for a in node.names]
        elif isinstance(node, ast.ImportFrom) and node.module:
            names = [node.module.split(".")[0]]
        for name in names:
            dep = rel.parent / (name + ".py")
            if (SOURCE / dep).is_file() and dep not in seen:
                queue.append(dep)

(TARGET / "notes").mkdir(exist_ok=True)
out = {"prepared_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
       "source_checkpoint": 29, "source_root": str(SOURCE),
       "programs": PROGRAMS, "files": sorted(manifest, key=lambda x: x["path"]),
       "scope": "Preparation only; source historical JSON files are inputs, not current execution credit."}
(TARGET / "source_manifest.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps({"prepared_at": out["prepared_at"], "files": len(manifest),
                  "bytes": sum(x["bytes"] for x in manifest), "target": str(TARGET)}))
