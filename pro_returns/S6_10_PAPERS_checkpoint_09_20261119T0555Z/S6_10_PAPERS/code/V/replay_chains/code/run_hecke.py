"""Run a recorded Julia program in the pinned, disposable Hecke runtime.

The runtime is created by setup_integral_conjugacy_runtime.py and
setup_hecke_runtime.py; no user's Julia environment is modified.
"""
from pathlib import Path
import os
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
cache = root.parent / 'external_cache/integral_conjugacy_runtime'
env = os.environ.copy()
env.update(TMPDIR=str(cache / 'tmp'), JULIA_DEPOT_PATH=str(cache / 'depot'),
           JULIA_NUM_THREADS='1', JULIA_NUM_PRECOMPILE_TASKS='1')
command = [str(cache / 'julia-1.10.10/bin/julia'), '--startup-file=no',
           '--heap-size-hint=1G', '--project=' + str(cache / 'env'), *sys.argv[1:]]
raise SystemExit(subprocess.run(command, env=env, cwd=root).returncode)
