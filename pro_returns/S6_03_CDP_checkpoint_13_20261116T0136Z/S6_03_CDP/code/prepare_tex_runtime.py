"""Fetch missing public CTAN runtime files into the reproducible local TeX tree.

The installed TeX distribution has no filename database, lualibs or luaotfload.
No mathematical assertion depends on this repair. Downloads are dependencies,
not source material supplied by the user.
"""
from pathlib import Path
from urllib.request import urlopen
from zipfile import ZipFile
import hashlib
import os
import subprocess

root = Path(__file__).resolve().parents[1]
target = root / "build" / "texmf" / "tex" / "luatex"
target.mkdir(parents=True, exist_ok=True)
for name in ("luaotfload", "lualibs", "luatexbase", "lua-uni-algos", "lualatex-math"):
    subtree = "latex" if name == "lualatex-math" else "generic"
    url = f"https://mirror.ox.ac.uk/sites/ctan.org/macros/luatex/{subtree}/{name}.zip"
    path = root / "build" / f"{name}.zip"
    if not path.exists():
        with urlopen(url, timeout=45) as response:
            data = response.read()
            print("download", name, response.url, len(data))
        path.write_bytes(data)
    print("sha256", name, hashlib.sha256(path.read_bytes()).hexdigest())
    with ZipFile(path) as archive:
        archive.extractall(target)
    print("extracted", name)

env = os.environ.copy()
env["TEXMF"] = "{/usr/share/texmf,/usr/share/texlive/texmf-dist}"
fmt = root / "build" / "plain.fmt"
if not fmt.exists():
    subprocess.run(["luahbtex", "-ini", "-interaction=nonstopmode",
                    "-jobname=plain", "-output-directory=build",
                    r"\input plain \dump"], cwd=root, env=env, check=True)
for name, source in (("lualibs", "lualibs.dtx"),
                     ("luatexbase", "luatexbase.ins"),
                     ("lualatex-math", "lualatex-math.ins")):
    subprocess.run(["luahbtex", f"-fmt={fmt}", "-interaction=nonstopmode", source],
                   cwd=target/name, env=env, check=True)
print("Runtime preparation complete")
