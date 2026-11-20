# P1.16: complete current numerical certificate

Author: GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort; same model family. Date: 19 November 2026.

The printed P1.15–P1.18 proofs had already been read before this implementation. The closed-loop program is new and imports none of the unavailable historical programs. It implements a rational two-residue gauge and rational polygon continuation, and compares its matrix balls with the separately constructed regular-root method already supplied in the current Paper V package.

## Files and exact inputs

* `period_loop_comparison.py`: derives the Fuchsian gauge from the literal printed six-dimensional rational connection; propagates complex Taylor balls on both complete marked loops and the positive segment from 1 to 2; solves the normalized integral intertwiner; evaluates the height and the two c=10 period determinants; evaluates the regular infinity-root series at lambda=2; compares the two complete period matrices.
* `period_loop_comparison.output.json`: all residue matrices, rational vertices and step receipts, every period-matrix ball, comparison bounds, height, determinants, input hashes and dependency versions.
* `validate_saved_period_comparison.py` and its output: independently reconstruct all rational path steps and the exact residue norms, verify all 192 Cauchy-tail inequalities, all displayed numeric bounds and both input hashes. This is saved-data validation, not a second Taylor propagation.
* `P116_replacement_proof.tex` and `V_period_certificate_patches.json`: complete proposed proof and three guarded replacements against the current linked body. Root owns their integration.
* `period_loop_iteration01.json` and `saved_validation_iteration01.json`: exact failed attempts and repairs. The first loop execution completed its paths but stopped while parsing a saved complex-ball string; the repaired parser retains both coordinate radii. The first saved-data validation incorrectly demanded overlap of the exact-norm tail with a conservatively inflated upper-norm tail; the correct inequality is that the exact-norm upper bound is at most the saved upper bound. Neither repair changes the stated mathematical bound.

The two input files are `fresh_frobenius.json` and `fresh_root_connections.json`. Their audit location is `../paper_v_review/output/`; their publication location is `code/paper_v/output/`. The current files at these locations have identical SHA-256 values, verified explicitly. The first supplies the already certified regular-root normalization and constant infinity frame; the second supplies the exact polynomial coefficients derived from the printed connection. Their hashes are embedded in the output. The exact existence and uniqueness of the common intertwiner is P1.15; consistency of the real intersection is P1.8. Residual containment alone is not used as a substitute for either result.

## Reproduction

Python 3.12.14; python-flint 0.9.0; SymPy 1.14.0; NumPy 2.3.5; SciPy 1.17.0. The root certificate has its own dependency recipe under `code/paper_v/README.md`.

From the package root, with these dependencies installed:

```sh
python code/current_audits/audit_paper_i/closure_07/period_loop_comparison.py
python code/current_audits/audit_paper_i/closure_07/validate_saved_period_comparison.py
```

The default input directory is the mirrored `code/current_audits/audit_paper_i/paper_v_review/output/`. To use the publication copy directly, set `S6_P116_ROOT_INPUTS` to the absolute path of `code/paper_v/output/`. A local dependency installation can be selected with `S6_P116_VENDOR`; the default is the audit's adjacent `vendor/` directory. These names do not replace any system environment variable. A dependency installation command is:

```sh
python -m pip install --target /absolute/path/period_vendor python-flint==0.9.0 sympy==1.14.0 numpy==2.3.5 scipy==1.17.0
```

Set `S6_P116_VENDOR=/absolute/path/period_vendor` when executing. The validator reads the same two mirrored audit inputs and verifies their recorded hashes. The working precision is 140 decimal digits for propagation and 160 for the separate saved-data checks.

## Result and mathematical scope

PASS: 120 zero-loop steps, 66 infinity-loop steps and 6 open-path steps; largest Taylor order 192; every local truncation bound is below 10^-100. The two method comparisons are below 1.37e-73 at lambda=1 and 4.71e-74 at lambda=2. The lambda=2 regular-root series uses degree 880, radius 5/4, denominator lower bound 2343.75 and row-sum connection bound 65.6375; its tail is below 5.39e-103. The normalized height enclosure has radius below 4e-91 and proves both strict decimal endpoints in P1.16. Both printed positive imaginary c=10 determinants are reproduced. The separate saved-data program passes 980 checks.

The P1.16 conclusion is local numerical evaluation plus the exact cusp-continuity exclusion of c=5/(3 pi). The complete global minimum and c=10 global admissibility are supplied by P1.18's separate 1600-leaf and four-square certificate. The present code does not infer that global result from the two local determinants.
