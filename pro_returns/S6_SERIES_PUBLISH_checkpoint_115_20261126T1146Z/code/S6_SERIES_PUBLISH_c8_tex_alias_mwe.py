"""Bounded real-pdfLaTeX check of literal AMS display-label aliases.

Runs one requested pass, preserving that pass's actual stdout/stderr/log/aux.
No manuscript, shared record, or canonical preamble is written.
"""
import argparse
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "agents/continuation8_tex_runtime/aliases"
CODE = ROOT / "code"
WRAPPER = CODE / "S6_SERIES_PUBLISH_c8_tex_pdflatex.py"

PREAMBLE = r"""\documentclass[11pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage{amsmath,amssymb,amsthm,amscd,mathtools,mathrsfs}
\usepackage[unicode,colorlinks=true,linkcolor=blue]{hyperref}
\usepackage{aliascnt}
\usepackage[nameinlink,noabbrev]{cleveref}
\usepackage{etoolbox}
\numberwithin{equation}{section}
\listfiles
"""

BODY = r"""\begin{document}
\section{Display aliases}\label{sec:first}
\begin{equation}
  a=1\hypertarget{mwe-target-equation}{}
  \label{eq:one}\label{eq:one-alias}\label[equation]{eq:one-typed}
\end{equation}
\begin{align}
  b&=2\hypertarget{mwe-target-align-a}{}
      \label{eq:align-a}\label{eq:align-a-alias}\\
  c&=3\hypertarget{mwe-target-align-b}{}
      \label{eq:align-b}\label{eq:align-b-alias}\\
  d&=4\label{eq:align-single}
\end{align}
\begin{equation}e=5\label{eq:after-align}\end{equation}
\begin{gather}
  f=6\label{eq:gather-a}\label{eq:gather-a-alias}\\
  g=7\label{eq:gather-b}\label{eq:gather-b-alias}
\end{gather}
\begin{multline}
  h=8+0\label{eq:multline-a}\\
  +0\hypertarget{mwe-target-multline}{}\label{eq:multline-b}
\end{multline}
\begin{equation}
  \begin{split}
    j&=9\label{eq:split-a}\\
     &=9\hypertarget{mwe-target-split}{}\label{eq:split-b}
  \end{split}
\end{equation}
\noindent Equation: \ref{eq:one}, \ref{eq:one-alias}, \ref{eq:one-typed}.
\par Align rows: \ref{eq:align-a}, \ref{eq:align-a-alias};
\ref{eq:align-b}, \ref{eq:align-b-alias}; \ref{eq:align-single}.
\par Next equation: \ref{eq:after-align}.
\par Gather: \ref{eq:gather-a}, \ref{eq:gather-a-alias};
\ref{eq:gather-b}, \ref{eq:gather-b-alias}.
\par Multline: \ref{eq:multline-a}, \ref{eq:multline-b}.
\par Split: \ref{eq:split-a}, \ref{eq:split-b}.
\par Types: \cref{eq:one}, \cref{eq:one-alias}, \cref{eq:one-typed},
\cref{eq:align-a}, \cref{eq:multline-b}, \cref{eq:split-b}.
\par Explicit destinations:
\hyperlink{mwe-target-equation}{equation},
\hyperlink{mwe-target-align-a}{first align row},
\hyperlink{mwe-target-align-b}{second align row},
\hyperlink{mwe-target-multline}{multline},
\hyperlink{mwe-target-split}{split}.
\section{A later counter}\label{sec:second}
\begin{equation}
 k=10\label{eq:second}\label{eq:second-alias}
\end{equation}
\noindent Later equation: \ref{eq:second}, \ref{eq:second-alias}.
\par Sections: \ref{sec:first}, \ref{sec:second}.
\section{Current manuscript displays}
\begin{equation}
 w(a,b)=
 \bigl(\rho_0e^{i(\phi_0-a-b)},\rho_1e^{ia},\rho_2e^{ib}\bigr),
 \qquad
 \rho_0=r_0^{1/2},\quad \rho_1=\rho_2=r_0^{1/4},
 \quad (a,b)\in\bigl(\mathbb R/(2\pi\mathbb Z)\bigr)^2.
 \hypertarget{tag-03AP}{}\label{wb:h24:ret:eq:M}
 \hypertarget{tag-01V0}{}\label{maps:eq:B.3.2}
\end{equation}
\begin{align}
 N_\ell&=\tfrac12L_0+\tfrac14L_1+\tfrac14L_2,
       &N_\phi&=Q_0,\hypertarget{tag-03B2}{}\label{wb:h24:ret:eq:normal-first}\\
 N_i&=-\bigl((A_0)_{1i}+(A_0)_{2i}\bigr)L_0
           +(A_0)_{1i}L_1+(A_0)_{2i}L_2
       &&(i=1,2).\hypertarget{tag-03B3}{}\label{wb:h24:ret:eq:normal-u}
 \hypertarget{tag-01V2}{}\label{maps:eq:B.3.4}
\end{align}
\begin{equation}
 \Psi(r,s)=4\left\lfloor r/8\right\rfloor
       +3(r\bmod8)\left\lfloor s/2\right\rfloor
                                      \quad\hbox{in }k.       \hypertarget{tag-0217}{}\label{maps:eq:D.OF1}
\hypertarget{tag-021Q}{}\label{maps:eq:D.OL1}
\end{equation}
\noindent Retained equation: \ref{wb:h24:ret:eq:M}, \ref{maps:eq:B.3.2}.
\par Retained align: \ref{wb:h24:ret:eq:normal-first};
\ref{wb:h24:ret:eq:normal-u}, \ref{maps:eq:B.3.4}.
\par LV equation: \ref{maps:eq:D.OF1}, \ref{maps:eq:D.OL1}.
\par Types: \cref{wb:h24:ret:eq:M}, \cref{maps:eq:B.3.2},
\cref{wb:h24:ret:eq:normal-u}, \cref{maps:eq:B.3.4},
\cref{maps:eq:D.OF1}, \cref{maps:eq:D.OL1}.
\par Preserved explicit targets:
\hyperlink{tag-03AP}{03AP}, \hyperlink{tag-01V0}{01V0},
\hyperlink{tag-03B2}{03B2}, \hyperlink{tag-03B3}{03B3},
\hyperlink{tag-01V2}{01V2}, \hyperlink{tag-0217}{0217},
\hyperlink{tag-021Q}{021Q}.
\end{document}
"""

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("case", choices=("baseline", "patched"))
    parser.add_argument("pass_name")
    args = parser.parse_args()
    if not args.pass_name.replace("_", "").isalnum():
        raise ValueError("Use a plain alphanumeric pass name")
    WORK.mkdir(parents=True, exist_ok=True)
    patch = ""
    if args.case == "patched":
        patch = (CODE / "S6_SERIES_PUBLISH_c8_tex_alias_proposal.tex").read_text()
    source = WORK / ("S6_SERIES_PUBLISH_c8_tex_alias_" + args.case + ".tex")
    source.write_text(PREAMBLE + patch + BODY, encoding="utf-8", newline="\n")
    command = [sys.executable, str(WRAPPER), "-interaction=nonstopmode", "-file-line-error"]
    if args.case == "patched":
        command.append("-halt-on-error")
    command.append(source.name)
    result = subprocess.run(command, cwd=WORK, capture_output=True, text=True)
    prefix = CODE / ("S6_SERIES_PUBLISH_c8_tex_alias_" + args.pass_name)
    prefix.with_suffix(".out").write_text(result.stdout, encoding="utf-8", newline="\n")
    prefix.with_suffix(".err").write_text(result.stderr, encoding="utf-8", newline="\n")
    prefix.with_suffix(".tex").write_bytes(source.read_bytes())
    for suffix in (".log", ".aux"):
        generated = source.with_suffix(suffix)
        if generated.exists():
            prefix.with_suffix(suffix).write_bytes(generated.read_bytes())
    print("Requested case:", args.case)
    print("Command:", " ".join(command))
    print("pdfLaTeX/wrapper exit:", result.returncode)
    print("Actual streams and generated log/aux:", prefix.relative_to(ROOT))
    print("No canonical or shared file changed.")
    return result.returncode

if __name__ == "__main__":
    raise SystemExit(main())
