#!/usr/bin/env python3
"""Run the unchanged LK main using its exact two imported helper definitions."""
import ast
from contextlib import redirect_stdout, redirect_stderr
from datetime import datetime, timezone
from hashlib import sha256
import io
from itertools import combinations
import json
from pathlib import Path
import runpy
import sys
import tempfile
from types import ModuleType

import sympy as s
from sympy.matrices.normalforms import smith_normal_form

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT / "agents/continuation7_iii_general_cusp_receiving"
P = "S6_SERIES_PUBLISH_III_02LK_"
source = LANE/(P+"historical_manifolds_general_cusp.py")
recorded = LANE/(P+"historical_manifolds_general_cusp.json")
assert sha256(source.read_bytes()).hexdigest() == "06b8549b00c488f327db06fe7891e070e32256810d29ce60106cc067347978e0"
assert sha256(recorded.read_bytes()).hexdigest() == "158174459afada4c5381235fc0bf64efa0a87e68267c360b9e3274fc2d5b84c6"

rank_source = (LANE/(P+"historical_manifolds_rankone_families.py")).read_text()
rank_tree = ast.parse(rank_source)
pair_node = next(node for node in rank_tree.body if isinstance(node, ast.Assign)
                 and any(isinstance(t, ast.Name) and t.id == "PAIRS" for t in node.targets))
assert ast.get_source_segment(rank_source, pair_node) == "PAIRS=list(combinations(range(4),2))"
helper_modules = {}
for module_name, function in (("manifolds_rankone_families", "wedge"),
                              ("manifolds_weighted_profiles", "group")):
    module = ModuleType(module_name)
    module.__dict__.update(s=s, combinations=combinations, smith_normal_form=smith_normal_form)
    if function == "wedge":
        exec(compile(ast.Module(body=[pair_node], type_ignores=[]),
                     "<retained original PAIRS assignment>", "exec"), module.__dict__)
        assert module.PAIRS == list(combinations(range(4), 2))
    helper = LANE/(P+"historical_helper_"+function+".py")
    exec(compile(helper.read_text(), str(helper), "exec"), module.__dict__)
    helper_modules[module_name] = module
    assert module_name not in sys.modules
    sys.modules[module_name] = module

# The main imports these function objects only. Their two complete bodies
# depend solely on the retained PAIRS assignment, sympy and smith_normal_form.
# No other top-level statement in either historical helper module is executed.
runtime = Path(tempfile.mkdtemp(prefix="S6_SERIES_PUBLISH_c7_lk_replay_v1_"))
entry = runtime/"manifolds_general_cusp.py"
entry.write_bytes(source.read_bytes())
assert entry.read_bytes() == source.read_bytes()
print("SCOPE unchanged 95-line historical main; exact wedge/group/PAIRS helper scope", flush=True)
print("RUNTIME", runtime, "SYMPY", s.__version__, flush=True)
out, err = io.StringIO(), io.StringIO()
try:
    with redirect_stdout(out), redirect_stderr(err):
        runpy.run_path(str(entry), run_name="__main__")
finally:
    (LANE/(P+"historical_replay_main.out")).write_text(out.getvalue())
    (LANE/(P+"historical_replay_main.err")).write_text(err.getvalue())
    for name in helper_modules:
        del sys.modules[name]
print(out.getvalue(), end="", flush=True)
assert err.getvalue() == ""
generated = (runtime/"manifolds_general_cusp.json").read_bytes()
(LANE/(P+"historical_replay_data.json")).write_bytes(generated)
same_bytes = generated == recorded.read_bytes()
same_values = json.loads(generated) == json.loads(recorded.read_bytes())
print("REPLAY_BYTEWISE_EQUAL", same_bytes, flush=True)
print("REPLAY_JSON_EQUAL", same_values, flush=True)
assert same_bytes and same_values
print("REPLAY_SHA256", sha256(generated).hexdigest(), flush=True)
print("PASS complete recorded JSON reproduced; no full dependency-module execution claimed", flush=True)
print("COMPLETED_UTC", datetime.now(timezone.utc).isoformat(), flush=True)
