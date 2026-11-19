#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime,timezone
root=Path(__file__).resolve().parents[2]
entry=('\n- '+datetime.now(timezone.utc).isoformat()+
 ' — Reopened the primary title page of Atiyah–Bott, '
 'The moment map and equivariant cohomology, Topology 23(1) (1984), 1–28. '
 'URL https://www.math.stonybrook.edu/~mmovshev/MAT570Spring2008/BOOKS/atiyahbott_moment.pdf ; '
 'tool ref turn360view0. Reason: verify bibliography metadata requested by root. '
 'Material: authors, exact title, journal, volume, issue, pages and year from '
 'the printed first page. No DOI inferred from the scan identifier. '
 'Entry saved in code/part3_fourfold/references_atiyah_bott.bib, key AtiyahBott1984.\n')
with (root/'records/literature_fourfold.md').open('a') as f:f.write(entry)
print(entry.strip())
