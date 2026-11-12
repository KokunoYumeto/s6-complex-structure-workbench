# Exact Lorentz observation bridge audit evidence

This directory promotes the completed read-only audit from `agent_work/lorentz_bridge_intake_20260904` into the canonical project's evidence tree. It does not alter any mathematical TeX or canonical ledger.

The packet TeX was not re-imported. The packet file and the existing canonical evidence file `../worldline_presymplectic_reduction_20260904/exact_lorentz_observation_bridge.tex` are byte-identical: each is 53,061 bytes with SHA-256 `2be16e1dc71b2e5dc04238f0fbe440138258d0825a4841ab2f29662587681599`. Consequently, the audited packet contributes no genuinely new mathematical result relative to the canonical tree.

## Exact verdict

- **PROVED:** C01--C22, C24--C26, C31, and the all-spin occurrence statement in C30, each in the exact scope stated in `CLAIM_LEDGER.md`. This includes the finite-dimensional algebra, orbit and compactification results, the filling square, and the separately defined multiplication/Fock spectra. The packet replay passes 33/33 checks and the independent checker passes 30/30 checks.
- **REFUTED:** C23 under its natural dynamical interpretation and C32 under its global-completion interpretation. The displayed first-order action forces `dot x = 0` in the strict interior and does not make the multiplication operator `H_n` its evolution Hamiltonian; the full toroidal, elliptic, spin-selection, and interacting bridge is therefore not complete.
- **OPEN:** C27 (a pointwise toroidal-total-space map to the phase-retaining carrier), C28 (the global analytic elliptic overlap cocycle through the finite fillings), C29 (an interacting Yang--Mills transfer and energy-form intertwiner), and the unique-spin selection part of C30. The canonical-quantization link from the action to the C24 Hilbert space and multiplication operator is also open.

## Preserved evidence

`AUDIT_SHA256SUMS.txt` authenticates the nine original top-level audit records. The `packet_checker` subdirectory preserves the publisher's exact checker source and its two exact archived outputs; `packet_verifier_replay.json` and `independent_verification.json` preserve the audit replay and independent run. `CANONICAL_READONLY_RECEIPT.md` records the canonical comparison snapshots.
