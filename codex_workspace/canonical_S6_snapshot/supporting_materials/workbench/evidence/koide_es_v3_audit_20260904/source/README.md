# Koide--Erdos--Straus full arithmetic extension

The main paper is:

`Koide_ES_Extension_v3.pdf`

The extension keeps the exact source selector, terminal matrix, Koide
coordinate maps, and canonical period discriminant. It adds complete composite
divisor channels, Fourier counts, Lorentz channel maps, prime saturation,
density one on the diagonal Koide ray, exact individual-prime multiplicity,
Bezout openings, and an exact rational-nonintersection theorem for the
orthogonal defect map.

## Build

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error Koide_ES_Extension_v3.tex
```

## Verify

```text
python verification/verify_extension_v3.py
```

The packages are intentionally separated into small archives:

- **core**: paper, LaTeX, summary, README;
- **verification**: checker, JSON receipt, validation report, checksums;
- **sources**: exact extracted controlling source files and provenance;
- **background**: the prior exact crosswalk paper and its checker;
- **complete**: all of the preceding, excluding page renderings and build
  intermediates.

Every archive is under 2 MB. No artifact approaches a 400 MB download limit.
