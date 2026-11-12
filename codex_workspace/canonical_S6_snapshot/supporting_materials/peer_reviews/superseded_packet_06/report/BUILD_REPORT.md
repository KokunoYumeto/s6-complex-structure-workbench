# Report build

The PDF was generated from `peer_review_report.md` with Pandoc and XeLaTeX:

```bash
pandoc peer_review_report.md \
  --standalone \
  --from=markdown+tex_math_dollars+tex_math_single_backslash+raw_tex+pipe_tables \
  --pdf-engine=xelatex \
  --toc --number-sections \
  -o peer_review_report.pdf
```

The PDF was then rendered at 160 dpi and visually inspected. `preflight.txt` records the structural preflight result.
