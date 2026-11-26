"""Prepare a local pdfLaTeX runtime and compile a package-only smoke document.

This program does not modify a manuscript or read any mathematical body.
Run from any directory; all work paths derive from this program's location.
The installed TeX distribution is /usr/share/texlive/texmf-dist (Debian).
"""
from pathlib import Path
import json
import os
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "agents" / "continuation8_tex_runtime"
LOCAL = WORK / "texmf"
VAR = WORK / "texmf-var"
CONFIG = WORK / "texmf-config"
for path in (WORK, LOCAL / "web2c", LOCAL / "tex/generic/config", LOCAL / "fonts/map/pdftex", VAR, CONFIG):
    path.mkdir(parents=True, exist_ok=True)

env = os.environ.copy()
env["TEXMFVAR"] = str(VAR)
env["TEXMFCONFIG"] = str(CONFIG)
env["TEXMF"] = "{" + ",".join(map(str, (CONFIG, VAR, LOCAL))) + ",/etc/texmf,/usr/share/texmf,/usr/share/texlive/texmf-dist}"
env["TEXFORMATS"] = str(VAR / "web2c") + "//:"
env["TEXMFDBS"] = ""
env["MKTEXFMT"] = "0"

def write(path, text):
    path.write_text(text, encoding="utf-8", newline="\n")

def run(name, args, *, must=True):
    result = subprocess.run(args, env=env, cwd=WORK, capture_output=True, text=True)
    write(ROOT / "code" / f"S6_SERIES_PUBLISH_c8_tex_{name}.out", result.stdout)
    write(ROOT / "code" / f"S6_SERIES_PUBLISH_c8_tex_{name}.err", result.stderr)
    print(name, "exit", result.returncode, "command", json.dumps(args))
    if must and result.returncode:
        print(result.stdout[-4000:])
        print(result.stderr[-4000:])
        raise SystemExit(result.returncode)
    return result

write(LOCAL / "tex/generic/config/language.dat", "english hyphen.tex\n=usenglish\n=USenglish\n=american\n")
write(LOCAL / "web2c/fmtutil.cnf", "pdflatex pdftex language.dat -translate-file=cp227.tcx *pdflatex.ini\n")
maps = ["cm.map", "cmextra.map", "symbols.map", "euler.map", "latxfont.map", "rsfs.map", "lm.map"]
map_contents = []
for name in maps:
    found = subprocess.run(["kpsewhich", name], env=env, capture_output=True, text=True, check=True).stdout.strip()
    print("font-map", name, found)
    map_contents.append(Path(found).read_text(encoding="utf-8"))
write(LOCAL / "fonts/map/pdftex/pdftex.map", "\n".join(map_contents))

run("format", ["fmtutil-user", "--cnffile=" + str(LOCAL / "web2c/fmtutil.cnf"), "--byfmt", "pdflatex"])

sample = r"""\documentclass[11pt,a4paper]{article}
\usepackage[margin=25mm,headheight=15pt]{geometry}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage{amsmath,amssymb,amsthm,amscd,mathtools,mathrsfs}
\usepackage{microtype,booktabs,longtable,array,xcolor,graphicx,enumitem,needspace,fancyhdr}
\usepackage[round,authoryear]{natbib}
\usepackage[unicode,colorlinks=true,linkcolor=blue!40!black,citecolor=blue!40!black,urlcolor=blue!40!black]{hyperref}
\usepackage{xurl,listings,tabularx,tikz,tikz-cd,aliascnt}
\usetikzlibrary{arrows.meta,calc,patterns,positioning}
\usepackage[nameinlink,noabbrev]{cleveref}
\usepackage{etoolbox}
\begin{document}
\section{Package and font sample}\label{sec:sample}
Latin Modern: B\'ezout; \textbf{bold}; \textit{italic};
\texttt{plain/path.py}; \textbf{\texttt{bold mono}};
\textit{\texttt{italic mono}}. See \cref{sec:sample}.
\[
\mathbb Z\quad\mathscr F\quad\mathcal O\quad\sum_{j=1}^{n}x_j
\qquad
\begin{tikzcd}A\arrow[r,"f"]\arrow[d,"g"']&B\arrow[d,"h"]\\
C\arrow[r,"k"']&D\end{tikzcd}
\]
\begin{tabular}{ll}\toprule Font&Sample\\\midrule Roman&ABC xyz\\
Monospace&\texttt{ABC xyz}\\\bottomrule\end{tabular}
\end{document}
"""
tex = WORK / "S6_SERIES_PUBLISH_c8_tex_smoke.tex"
write(tex, sample)
for n in (1, 2):
    run(f"smoke_pass{n}", ["pdflatex", "-no-shell-escape", "-interaction=nonstopmode", "-halt-on-error", tex.name])
run("pdffonts", ["pdffonts", "S6_SERIES_PUBLISH_c8_tex_smoke.pdf"])
run("pdfinfo", ["pdfinfo", "S6_SERIES_PUBLISH_c8_tex_smoke.pdf"])

# The wrapper recomputes paths after every restore and supplies only TeX settings.
wrapper = r'''#!/usr/bin/env python3
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
'''
write(ROOT / "code" / "S6_SERIES_PUBLISH_c8_tex_pdflatex.py", wrapper)
log = (WORK / "S6_SERIES_PUBLISH_c8_tex_smoke.log").read_text()
issues = re.findall(r"^.*(?:Overfull|Missing character|undefined|LaTeX Font Warning|^!).*$", log, re.M)
print("SMOKE_LOG_ISSUES", json.dumps(issues))
print("READY_WRAPPER", ROOT / "code" / "S6_SERIES_PUBLISH_c8_tex_pdflatex.py")
