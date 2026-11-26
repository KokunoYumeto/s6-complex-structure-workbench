#!/usr/bin/env python3
"""Run pdfLaTeX with the isolated, verified LaTeX 2026-11-01 runtime."""
from pathlib import Path
import os
import subprocess
import sys
r = Path(__file__).resolve().parents[1]
w = r / "agents" / "continuation9_current_tex"
e = os.environ.copy()
e["TEXMFVAR"] = str(w / "texmf-var")
e["TEXMFCONFIG"] = str(w / "texmf-config")
e["TEXMF"] = "{" + ",".join(str(w / x) for x in ("texmf-config", "texmf-var", "texmf")) + ",/etc/texmf,/usr/share/texmf,/usr/share/texlive/texmf-dist}"
e["TEXFORMATS"] = str(w / "texmf-var/web2c") + "//:"
e["TEXMFDBS"] = ""
e["MKTEXFMT"] = "0"
sys.exit(subprocess.call(["pdflatex", "-no-shell-escape", *sys.argv[1:]], env=e))
