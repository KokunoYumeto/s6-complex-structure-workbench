# Validation report

## Mathematical verifier

Command:

```text
python verification/verify_extension_v3.py
```

Runtime in the build environment: approximately 1.2 seconds.

Exact bounded checks include:

- 665 coprime odd fixed shells through `n <= 161`;
- 1,430 oriented divisor-channel states;
- 146 universal diagonal divisor-channel states;
- 512 explicit `GL_2(Z)` opening--terminal morphisms;
- 9,137 prime shells for primes below 1,000;
- 4,156 oriented prime-channel states;
- 57 exact character-count comparisons;
- 192 ray/progression constructions over four primitive rays and all 48 hard
  classes modulo 840;
- 48 explicit primes in those classes;
- 48 fixed `q=11` subprogressions;
- 30 Bezout-opening torsors with eleven consecutive companion shifts each;
- all 329 primes `p = 1 mod 4` below 5,000 for the exact diagonal-ray count;
- 819 diagonal-ray certificates in that range;
- maximum diagonal multiplicity 8 in that range;
- exact irrational square-class obstructions in the rational-nonintersection
  theorem.

The character checks use complex floating arithmetic only to replay finite
character sums; their maximum numerical residual was approximately
`9.18e-15`. All channel, determinant, inverse, unit-fraction, terminal, and
morphism checks use exact integer or symbolic arithmetic.

## PDF build

Source:

`Koide_ES_Extension_v3.tex`

Build command:

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error Koide_ES_Extension_v3.tex
```

Result:

- 21 pages;
- A4;
- unencrypted;
- text-extractable;
- no undefined references;
- no LaTeX warnings;
- no overfull or underfull box warnings;
- PDF preflight passed;
- all pages rendered at 170 dpi and visually inspected through a contact sheet;
- individual pages containing the density theorem, diagonal multiplicity
  theorem, and rational-nonintersection theorem were inspected separately.
