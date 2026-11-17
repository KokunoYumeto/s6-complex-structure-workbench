#!/bin/bash
set -eu
root_dir="$(cd "$(dirname "$0")/.." && pwd)"
runtime_dir="$(dirname "$root_dir")/tex_runtime"
export TEXMF='{/usr/share/texlive/texmf-dist,/usr/share/texmf}'
export TEXFORMATS="$runtime_dir"
export TEXINPUTS="$runtime_dir/packages//:"
export LUAINPUTS="$runtime_dir/packages//:"
cd "$root_dir"
lualatex -interaction=nonstopmode -halt-on-error S6_06_BLIND_paper.tex
bibtex S6_06_BLIND_paper
lualatex -interaction=nonstopmode -halt-on-error S6_06_BLIND_paper.tex
lualatex -interaction=nonstopmode -halt-on-error S6_06_BLIND_paper.tex
