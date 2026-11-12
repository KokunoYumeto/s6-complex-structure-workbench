# Koide exact checkpoint — 4 September 2026

This directory is the project-relative reproducibility checkpoint for the exact
Koide arithmetic material integrated into the canonical workbench.  It contains
the final height-`100000000` census evidence, the quaternion arithmetic replay,
and the independent parametrization verifier.  The source artifacts were copied
without modification; their original absolute paths embedded in JSON receipts
and logs are intentionally retained as provenance.

## Canonical references

The reference chain is:

1. `koide_arithmetic_preprint.tex` inputs
   `supporting_materials/workbench/research/koide_counting_repair.tex`.
2. That module inputs `koide_exact_parametrization.tex`,
   `koide_exact_census.tex`, and `koide_quaternion_bridge.tex`.
3. `koide_exact_census.tex` records the same SHA-256 values found here for
   `koide_fast_enum.py`, the `100000000` result JSON, the compressed coordinate
   dataset, and the coordinate-audit receipt.
4. `koide_quaternion_bridge.tex` identifies `verify_quaternion_bridge.py` as
   its exact arithmetic replay and points to its accompanying manifest.

## Exact provenance and inventory

- `census/` is copied from
  `agent_work/koide_discrepancy_computation_20260904/`.  It contains the four
  final-checkpoint scripts, the method/results record, both top-level receipts,
  and `final_100000000/` with the result, full six-coordinate dataset, audit
  receipt, fine-candidate analysis, and selected witnesses.
- `quaternion/` is copied from
  `agent_work/koide_quaternion_bridge_20260904/` and contains exactly the
  requested verifier, recorded verification log, and original manifest.  That
  source manifest also records the hash of the source `REPORT.md`; the report
  is not duplicated here because its mathematics is integrated in the
  canonical `koide_quaternion_bridge.tex` module.
- `parametrization/verify_parametrization.py` is copied from
  `agent_work/koide_discrepancy_parametrization_20260904/`.
- `SHA256SUMS` covers every file in this checkpoint except itself.  Every
  source-derived entry has the same digest as its source artifact.

Pilot outputs, Python caches, literature downloads, standalone manuscript build
products, and PDFs are deliberately excluded.  This is finite evidence through
height `100000000`, where the recorded count is `3536002`; it is not a proof of
the open square-root discrepancy estimate.

## Hash verification

From this directory in PowerShell:

```powershell
Get-Content .\SHA256SUMS | ForEach-Object {
    $expected, $path = $_ -split '  ', 2
    $actual = (Get-FileHash -Algorithm SHA256 -LiteralPath $path).Hash.ToLowerInvariant()
    if ($actual -ne $expected) { throw "SHA-256 mismatch: $path" }
}
```

## Replays

The two bounded exact-integer verifiers are read-only:

```powershell
python -B .\parametrization\verify_parametrization.py
python -B .\quaternion\verify_quaternion_bridge.py
```

For census validation, write regenerated receipts to a fresh directory so that
the preserved checkpoint remains byte-for-byte unchanged:

```powershell
$replay = New-Item -ItemType Directory -Path (Join-Path $env:TEMP ("koide-replay-" + [guid]::NewGuid()))
python -B .\census\validate_fast_enum.py --receipt (Join-Path $replay.FullName 'validation_receipt.json')
python -B .\census\audit_coordinate_file.py .\census\final_100000000\koide_roots_through_100000000.csv.gz .\census\final_100000000\koide_discrepancy_100000000.json (Join-Path $replay.FullName 'coordinate_audit_receipt.json')
python -B .\census\supplemental_candidate_analysis.py .\census\final_100000000\koide_roots_through_100000000.csv.gz .\census\final_100000000\koide_discrepancy_100000000.json (Join-Path $replay.FullName 'fine_candidate_analysis.json')
```

To regenerate the complete final census rather than audit the preserved data:

```powershell
python -B .\census\koide_fast_enum.py --max-height 100000000 --output-directory $replay.FullName
```

The expected final count is `3536002`.  Regenerated JSON files contain the new
output paths and runtime timings, so verify mathematical fields and dataset
hashes rather than expecting every regenerated JSON byte to equal the archived
receipt.
