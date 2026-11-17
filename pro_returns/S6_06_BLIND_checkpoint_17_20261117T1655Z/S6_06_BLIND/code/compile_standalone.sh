#!/bin/bash
set -eu
standalone_root="$(cd "$(dirname "$0")/.." && pwd)"
standalone_runtime="$(dirname "$standalone_root")/tex_runtime"
export TEXMF='{/usr/share/texlive/texmf-dist,/usr/share/texmf}'
export TEXFORMATS="$standalone_runtime"
export TEXINPUTS="$standalone_runtime/packages//:"
export LUAINPUTS="$standalone_runtime/packages//:"
cd "$standalone_root"
lualatex -interaction=nonstopmode -halt-on-error -output-directory="$2" "$1"
