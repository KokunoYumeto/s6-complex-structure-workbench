#!/usr/bin/env python3
"""Build an isolated official LaTeX 2026-11-01 runtime for pdfLaTeX.

The pinned public GitHub release assets and published digests are in the
companion sources JSON. Downloaded software, generated formats and smoke
PDFs stay in agents/continuation9_current_tex and are omitted from returns.
No global TeX file is modified; no manuscript is read or edited.
"""
from __future__ import annotations

import concurrent.futures
import hashlib
import json
import os
import re
import shutil
import subprocess
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "agents/continuation9_current_tex"
LOCAL = WORK / "texmf"
VAR = WORK / "texmf-var"
CONFIG = WORK / "texmf-config"
SOFTWARE = WORK / "software"
for path in (WORK, LOCAL / "web2c", LOCAL / "tex/generic/config",
             LOCAL / "fonts/map/pdftex", VAR, CONFIG, SOFTWARE):
    path.mkdir(parents=True, exist_ok=True)


def write(path, text):
    path.write_text(text, encoding="utf-8", newline="\n")


def environment():
    env = os.environ.copy()
    env["TEXMFVAR"] = str(VAR)
    env["TEXMFCONFIG"] = str(CONFIG)
    env["TEXMF"] = "{" + ",".join(map(str, (CONFIG, VAR, LOCAL))) + ",/etc/texmf,/usr/share/texmf,/usr/share/texlive/texmf-dist}"
    env["TEXFORMATS"] = str(VAR / "web2c") + "//:"
    env["TEXMFDBS"] = ""
    env["MKTEXFMT"] = "0"
    return env


ENV = environment()


def run(name, args, *, must=True):
    result = subprocess.run(args, env=ENV, cwd=WORK, capture_output=True, text=True)
    write(ROOT / "code" / f"S6_SERIES_PUBLISH_c9_current_tex_{name}.out", result.stdout)
    write(ROOT / "code" / f"S6_SERIES_PUBLISH_c9_current_tex_{name}.err", result.stderr)
    print(name, "exit", result.returncode, "command", json.dumps(args), flush=True)
    if must and result.returncode:
        print(result.stdout[-5000:], flush=True)
        print(result.stderr[-1000:], flush=True)
        raise SystemExit(result.returncode)
    return result


def download(asset):
    path = SOFTWARE / asset["name"]
    if path.exists():
        data = path.read_bytes()
    else:
        request = urllib.request.Request(asset["url"], headers={"User-Agent": "S6-Publication-LaTeX-Verification"})
        with urllib.request.urlopen(request, timeout=45) as response:
            data = response.read()
        path.write_bytes(data)
    digest = hashlib.sha256(data).hexdigest()
    assert len(data) == asset["size"], (asset["name"], len(data), asset["size"])
    assert digest == asset["sha256"], (asset["name"], digest, asset["sha256"])
    return path, digest, len(data)


def main():
    sources = json.loads((ROOT / "code/S6_SERIES_PUBLISH_c9_current_tex_sources.json").read_text())
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        downloaded = list(pool.map(download, sources["assets"]))
    for path, digest, size in downloaded:
        print("verified-asset", path.name, size, digest, flush=True)
        with zipfile.ZipFile(path) as archive:
            members = [name for name in archive.namelist() if name.startswith("tex/") and not name.endswith("/")]
            assert members
            for name in members:
                assert ".." not in Path(name).parts
                target = LOCAL / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(archive.read(name))
        print("installed-runtime-files", path.name, len(members), flush=True)

    write(LOCAL / "tex/generic/config/language.dat", "english hyphen.tex\n=usenglish\n=USenglish\n=american\n")
    write(LOCAL / "web2c/fmtutil.cnf", "pdflatex pdftex language.dat -translate-file=cp227.tcx *pdflatex.ini\n")
    maps = ["cm.map", "cmextra.map", "symbols.map", "euler.map", "latxfont.map", "rsfs.map", "lm.map"]
    map_text = []
    for name in maps:
        found = subprocess.run(["kpsewhich", name], env=ENV, capture_output=True, text=True, check=True).stdout.strip()
        assert found
        map_text.append(Path(found).read_text(encoding="utf-8"))
        print("font-map", name, found, flush=True)
    write(LOCAL / "fonts/map/pdftex/pdftex.map", "\n".join(map_text))
    run("format", ["fmtutil-user", "--cnffile=" + str(LOCAL / "web2c/fmtutil.cnf"), "--byfmt", "pdflatex"])

    # Current aliascnt is required with the 2026 native theorem counter aliases.
    # Use its official, unmodified self-extracting source and documented route.
    for source in sources.get("extra_sources", []):
        assert source["name"] == "aliascnt.dtx"
        directory = SOFTWARE / "aliascnt"
        directory.mkdir(exist_ok=True)
        path = directory / source["name"]
        if not path.exists():
            with urllib.request.urlopen(source["url"], timeout=45) as response:
                path.write_bytes(response.read())
        data = path.read_bytes()
        assert len(data) == source["size"]
        git_object = f"blob {len(data)}\0".encode() + data
        assert hashlib.sha1(git_object).hexdigest() == source["git_blob_sha1"]
        assert hashlib.sha256(data).hexdigest() == source["sha256"]
        print("verified-source", source["name"], source["version"], "SHA-256", hashlib.sha256(data).hexdigest(), flush=True)
        extracted = subprocess.run(["pdflatex", "-no-shell-escape", "-interaction=nonstopmode", "-halt-on-error", r"\let\install=y\input{aliascnt.dtx}"], cwd=directory, env=ENV, capture_output=True, text=True)
        write(ROOT / "code/S6_SERIES_PUBLISH_c9_current_tex_aliascnt_extract.out", extracted.stdout)
        write(ROOT / "code/S6_SERIES_PUBLISH_c9_current_tex_aliascnt_extract.err", extracted.stderr)
        assert extracted.returncode == 0, extracted.stdout[-4000:]
        target = LOCAL / "tex/latex/aliascnt/aliascnt.sty"
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(directory / "aliascnt.sty", target)
        assert source["version"] in target.read_text()
        print("installed", source["name"], source["version"], flush=True)

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
\makeatletter
\typeout{S6-FORMAT-VERSION: \fmtversion}
\IfFormatAtLeastTF{2025-11-01}{}{\errmessage{LaTeX kernel is too old}}
\makeatother
\begin{document}
\section{Package and font sample}\label{sec:sample}
Latin Modern: B\'ezout; \textbf{bold}; \textit{italic};
\texttt{plain/path.py}; \textbf{\texttt{bold mono}};
\textit{\texttt{italic mono}}. See \cref{sec:sample}.
\begin{equation}\label{eq:sample}
\mathbb Z\quad\mathscr F\quad\mathcal O\quad\sum_{j=1}^{n}x_j
\end{equation}
See equation~\eqref{eq:sample}.
\[
\begin{tikzcd}A\arrow[r,"f"]\arrow[d,"g"']&B\arrow[d,"h"]\\
C\arrow[r,"k"']&D\end{tikzcd}
\]
\begin{tabular}{ll}\toprule Font&Sample\\\midrule Roman&ABC xyz\\
Monospace&\texttt{ABC xyz}\\\bottomrule\end{tabular}
\end{document}
"""
    tex = WORK / "S6_SERIES_PUBLISH_c9_current_tex_smoke.tex"
    write(tex, sample)
    for n in (1, 2):
        run(f"smoke_pass{n}", ["pdflatex", "-no-shell-escape", "-interaction=nonstopmode", "-halt-on-error", tex.name])
    run("pdffonts", ["pdffonts", "S6_SERIES_PUBLISH_c9_current_tex_smoke.pdf"])
    run("pdfinfo", ["pdfinfo", "S6_SERIES_PUBLISH_c9_current_tex_smoke.pdf"])
    log = (WORK / "S6_SERIES_PUBLISH_c9_current_tex_smoke.log").read_text()
    assert "S6-FORMAT-VERSION: 2026-11-01" in log
    issues = re.findall(r"^.*(?:Overfull|Missing character|undefined|LaTeX Font Warning|^!).*$", log, re.M)
    assert not issues, issues
    print("SMOKE_FORMAT 2026-11-01", flush=True)
    print("SMOKE_LOG_ISSUES", json.dumps(issues), flush=True)

    wrapper = '''#!/usr/bin/env python3
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
'''
    write(ROOT / "code/S6_SERIES_PUBLISH_c9_current_pdflatex.py", wrapper)
    print("READY_WRAPPER", ROOT / "code/S6_SERIES_PUBLISH_c9_current_pdflatex.py", flush=True)


if __name__ == "__main__":
    main()
