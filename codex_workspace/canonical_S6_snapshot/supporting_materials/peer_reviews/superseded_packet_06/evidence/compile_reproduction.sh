#!/usr/bin/env bash
set -euo pipefail
# Run from a directory containing s6_canonical_modular_main_108_pages.tex.
pdflatex -interaction=nonstopmode -halt-on-error s6_canonical_modular_main_108_pages.tex
# Expected with the supplied tree: failure because parts/packet_01_body.tex is absent.
