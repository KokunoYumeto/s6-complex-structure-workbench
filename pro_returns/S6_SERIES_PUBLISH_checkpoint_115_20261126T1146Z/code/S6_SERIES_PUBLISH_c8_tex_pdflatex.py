#!/usr/bin/env python3
"""Run installed pdfLaTeX with the continuation's local format and font maps."""
from pathlib import Path
import os
import subprocess
import sys
r = Path(__file__).resolve().parents[1]
w = r / "agents" / "continuation8_tex_runtime"
e = os.environ.copy()
e["TEXMFVAR"] = str(w / "texmf-var")
e["TEXMFCONFIG"] = str(w / "texmf-config")
e["TEXMF"] = "{" + ",".join(str(w / x) for x in ("texmf-config", "texmf-var", "texmf")) + ",/etc/texmf,/usr/share/texmf,/usr/share/texlive/texmf-dist}"
e["TEXFORMATS"] = str(w / "texmf-var/web2c") + "//:"
e["TEXMFDBS"] = ""
e["MKTEXFMT"] = "0"
sys.exit(subprocess.call(["pdflatex", "-no-shell-escape", *sys.argv[1:]], env=e))
