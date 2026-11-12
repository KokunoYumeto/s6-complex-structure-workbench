# Report build

Primary source: `full_mathematical_peer_review.md`.

Build command:

```bash
pandoc full_mathematical_peer_review.md \
  --standalone \
  --from markdown+raw_tex+tex_math_dollars \
  --pdf-engine=xelatex \
  --output full_mathematical_peer_review.pdf
```

The generated `full_mathematical_peer_review.tex` is included. The final PDF has 17 letter-size pages. It was rendered at 200 dpi and inspected as individual pages and a contact sheet. `pdf_preflight.py` reports that it is openable, unencrypted, text-based, and non-XFA.
