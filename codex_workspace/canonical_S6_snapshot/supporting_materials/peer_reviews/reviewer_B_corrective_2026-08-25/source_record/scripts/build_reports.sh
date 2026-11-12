#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

pandoc --from=markdown+tex_math_single_backslash \
  reports/S6_MATHEMATICAL_PROOF_AUDIT.md \
  -o reports/S6_MATHEMATICAL_PROOF_AUDIT.pdf \
  --pdf-engine=xelatex \
  -V geometry:margin=0.75in \
  -V fontsize=10pt \
  -V colorlinks=true \
  -V linkcolor=blue \
  -V urlcolor=blue \
  -V documentclass=article \
  --metadata title='Independent Mathematical Proof Audit' \
  --metadata author='OpenAI GPT-5.6 Pro - independent proof audit' \
  --metadata date='2026-08-24'

pandoc --from=markdown+tex_math_single_backslash \
  session/ASSISTANT_VISIBLE_OUTPUTS.md \
  -o session/ASSISTANT_VISIBLE_OUTPUTS.pdf \
  --pdf-engine=xelatex \
  -V geometry:margin=0.75in \
  -V fontsize=10pt \
  -V colorlinks=true \
  -V urlcolor=blue \
  --metadata title='User-Visible Assistant Outputs from the S6 Audit Session' \
  --metadata author='OpenAI GPT-5.6 Pro' \
  --metadata date='2026-08-24'
