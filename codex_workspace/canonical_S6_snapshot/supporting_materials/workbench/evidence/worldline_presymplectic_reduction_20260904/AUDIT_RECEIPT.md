# Audit receipt: exact worldline presymplectic reduction

Generated: 2026-09-04T02:10:36+02:00 (Europe/Berlin)

## Scope and immutability

This directory is a standalone, non-canonical proof packet.  No canonical
source was edited.  The primary source audited for the original bridge was:

- `output/s6_consolidated_canonical_2026-08-26/supporting_materials/workbench/research/higher_rung_lorentz_observation_bridge.tex`
- physical line count: 927
- byte count: 31,339
- SHA-256: `68BDB0825113D61836CB8DAB494B25BE5159B35094D3FAC2522D24508F7B287C`
- requested source window: lines 748--927

The bounded comparison appendix audited the later packet:

- `agent_work/exact_lorentz_packet_intake_20260904/extracted/lorentz_observation_bridge/exact_lorentz_observation_bridge.tex`
- physical line count: 1,704
- byte count: 53,061
- SHA-256: `2BE16E1DC71B2E5DC04238F0FBE440138258D0825A4841AB2F29662587681599`
- requested source window: lines 875--1654

## Theorem-level result

The exact calculation, with the original constants and signs retained, gives:

1. For `m_0>0`, the colour quotient is the future fixed-mass shell, the
   characteristic quotient is canonically symplectomorphic to its cotangent
   bundle, and the action is exactly the usual future-directed spinless
   relativistic particle.  The covector identification is
   `xi(A)=-<x,A>_L`; this sign is forced by `Omega=-d<p,dx>_L`.
2. For `m_0=0` and nonzero rank-one `Z`, the intrinsic colour and
   characteristic quotient is exactly `T^* N_+^times`.  The displayed
   composite multiplier action is nevertheless not the standard massless
   variational system: `d(det p_alpha)_Z=0`, so its equations give
   `dot x=lambda p` without the equation `lambda=e`.  Four real rank-opening
   directions are first-order null but are not colour gauge directions.
3. At `Z=0`, `p=Dp=0`, the pulled-back two-form vanishes on the stratum, and
   arbitrary `x(tau)` is stationary.  This is an additional irregular branch
   absent from the standard massless particle.
4. For the later hard-constraint packet with `omega_0 != 0`, the constrained
   carrier stays rank two.  Its momentum map has rank four for `w!=0` and rank
   three at `w=0`.  Consequently its own first-order action forces
   `dot x=0` strictly above the threshold and yields the ordinary
   `dot x in R p` characteristic only at the threshold.  The threshold
   inequality and multiplication-operator spectrum are valid in their stated
   algebraic/free scope, but they do not constitute a dynamically generated
   interacting mass gap.

The standalone TeX contains the complete maps, stabilizers, kernel ranks,
properness proof for the characteristic action, reduced forms, equations,
singular counterexamples, and the line-specific extended-packet ledger.

## Reproducibility results

- Deterministic exact-arithmetic companion: **39/39 PASS**.
- Arithmetic mode: exact SymPy expressions; no floating-point comparisons.
- TeX build: two consecutive `pdflatex -interaction=nonstopmode
  -halt-on-error` passes succeeded.
- PDF: 14 pages, US letter, 374,672 bytes.
- Log scan: no LaTeX/package warnings, undefined references, undefined control
  sequences, overfull boxes, underfull boxes, or TeX errors.
- Visual QA: all fourteen pages were rendered at 120 dpi and inspected in a
  contact sheet; the dense claim ledger (page 12) and concluding proof pages
  (pages 13--14) were also inspected at individual-page resolution.  No
  clipping, collision, or unreadable table was found.

## Independent falsification passes

Three independent exact audits were applied to the proof before this receipt:

- a massless-stratum audit checked `d(det p_alpha)=0`, intrinsic versus ambient
  kernels, the four rank-opening directions, and the `Z=0` counterexample;
- a quotient/sign audit checked stabilizers, dimensions, the nonprojectivized
  null quotient, and the sign of the cotangent symplectomorphism;
- a whole-module adversarial audit checked every theorem plus the later-packet
  comparison.  It first identified two proof-completion needs (free/proper
  characteristic action and an explicit rank-one smooth section), which were
  repaired.  Its final verdict at the released TeX hash below was **PASS**, and
  it found no remaining line-specific correction.

## Released file identities

- `worldline_presymplectic_reduction.tex`
  - physical line count: 987
  - byte count: 35,157
  - SHA-256: `9098F5DC68362E7D03AD8EA892C994C5AB0B7A10F75DE82833F106AD1E268CB7`
- `worldline_presymplectic_reduction.pdf`
  - page count: 14
  - byte count: 374,672
  - SHA-256: `1B034519105647AD9F1F8F02ED1421669DEE4A8E3B9B0DA89E58891203244A81`
- `verify_worldline_reduction.py`
  - byte count: 11,266
  - SHA-256: `28CBBB5D31DBAD5775CA64E20E3CF12FD589C0893309B94A29CA4E64F299E83C`
- `worldline_reduction_checks.json`
  - byte count: 4,706
  - SHA-256: `0AF53F8004287CD5E8A9AFC11ACABD40ADB2CB3630AADA12C5B0691E93F5F5EC`
- `worldline_reduction_checks.log`
  - byte count: 1,875
  - SHA-256: `1C979FDDC94D315D931571268C60CF6E3F2CCB1A1DD460B34A084B72FBF66C92`
- `worldline_presymplectic_reduction_source_numbered.txt`
  - byte count: 42,066
  - SHA-256: `F227FAA45096AAF8887F096B0DD98A794D2D3E8FD60E134E37AAC77B57F454EB`
- `README.md`
  - byte count: 2,422
  - SHA-256: `92D358A6F0C59342FDF1D181C6CEAF2D95634D3780AE6636236F61A322C9C9AC`
- `WORKLOG.md`
  - byte count: 2,740
  - SHA-256: `9FD59E7217B7384ABE1AF670CC09619209C3471B15EF19D9CC3522BE4DC9C473`

## Reproduction commands

Run from this directory:

```powershell
python .\verify_worldline_reduction.py
pdflatex -interaction=nonstopmode -halt-on-error .\worldline_presymplectic_reduction.tex
pdflatex -interaction=nonstopmode -halt-on-error .\worldline_presymplectic_reduction.tex
```

The check program also regenerates the structured JSON, human-readable log,
and stable source-line index.
