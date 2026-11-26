#!/usr/bin/env python3
"""Install the engine's Sage 10.9 in a task-local conda-forge environment."""
from pathlib import Path
from urllib.request import urlopen
import hashlib
import os
import subprocess

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT.parents[1] / "tmp/c9_sage_runtime"
WORK.mkdir(parents=True, exist_ok=True)
MAMBA = WORK / "micromamba"
URL = "https://github.com/mamba-org/micromamba-releases/releases/download/2.10.0-0/micromamba-linux-64"
SHA256 = "701f39c06f8e6a670a0e186c8479b9e5c0502a2f0cda6cef65d83bdd2875e8bd"
if not MAMBA.exists():
    with urlopen(URL, timeout=45) as response:
        MAMBA.write_bytes(response.read())
assert hashlib.sha256(MAMBA.read_bytes()).hexdigest() == SHA256
MAMBA.chmod(0o755)
print("Verified micromamba 2.10.0-0", URL, SHA256, flush=True)
env = os.environ.copy()
env["MAMBA_ROOT_PREFIX"] = str(WORK / "mamba")
result = subprocess.run([str(MAMBA), "--no-rc", "create", "--yes", "--prefix", str(WORK / "sage"),
                         "--override-channels", "--channel", "conda-forge", "sage=10.9"], env=env)
raise SystemExit(result.returncode)
