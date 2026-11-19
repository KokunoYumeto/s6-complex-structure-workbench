# Paper V P1.18: fresh executable certificate

This directory contains a complete newly executed certificate for the unique minimum of the prescribed height, its normalized period value, and the splitting translation. Authored by **GPT-6 Astra, ChatGPT Pro mode, inherited effort**, on 19 November 2026 after reading the printed proof. It is a fresh computation and targeted proof check within the same model family.

## Run

Tested with Python 3.12.14, python-flint 0.9.0, SymPy 1.14.0, NumPy 2.3.5 and SciPy 1.17.0. Install the pinned dependencies into an environment of your choice:

```bash
python -m pip install -r requirements.txt
python fresh_global_cover.py > output/fresh_global_cover.stdout.txt 2>&1
python verify_saved_certificate.py > output/saved_certificate_validation.stdout.txt 2>&1
```

`fresh_global_cover.py` automatically runs `fresh_frobenius.py` and `fresh_local_domains.py` first. All inputs are exact constants in the source; no manuscript parsing, historical coefficient array or historical subdivision tree is required. The default output is this directory's `output/`. `PAPER_V_OUTPUT_DIR` can choose another output directory. `PAPER_V_VENDOR` can point to an existing dependency directory; the recorded workspace execution used the separately installed python-flint 0.9.0 wheel through that variable. The final exported copy was run successfully, followed by its separate verifier.

The endpoint and local calculations use 120 decimal digits, and the outer cover uses 80 digits with prior radii retained. The outer cover normally takes about a minute in the tested environment. It records progress every 500 processed nodes.

## Files and proof scope

- `fresh_frobenius.py`: derives the two rational root connections, uses new positive-axis/direct-root transports, certifies the normalized intertwiner subsystem and residuals, and computes the three endpoint heights.
- `fresh_local_domains.py`: four closed central Hessian squares, exact cusp gauge and holomorphic factor, actual anchor branch, explicit A-conjugacy to the former cusp marking, whole inner-disc determinant, and the full splitting constant.
- `fresh_global_cover.py`: complete new rational closed-box cover of the two root regions, cusp annulus and collar. It uses actual real preconditioning, whole-box ODE bounds and 412 complex Taylor transitions.
- `verify_saved_certificate.py`: a separately authored finite verifier for reconstructed rectangles, prefix-free complete coverage, exact areas, geometric reasons, serialized strict bounds, Hessian/cusp signs, and saved normalized finite maps.
- `DERIVATION.md`: full mathematical justification, exact morphisms, coverage and confidence limits.
- `output/fresh_cover_*.jsonl`: all 1,600 outer leaves, not just samples.
- `output/saved_certificate_validation.json`: successful independent finite validation and SHA-256 input hashes.

The four covers contain 1,088 strict leaves and 512 geometric leaves. Four further central squares give Hessian ≥I/4 and h(w)−h(0)≥|w|²/8. The punctured inner cusp disc has a uniform positive determinant polynomial. Together these establish the unique global minimum.

The height minimum is −1.094540250311402780116268263054945703725533269405330897770522063712646972012 with radius <4e−76. Both components of the prescribed splitting constant have radius <8e−76. The complete saved balls specify the actual midpoint and outward radius.

The exact geometric existence/uniqueness input for the common normalized intertwiner is P1.15. An interval residual containing zero is used only as a consistency check. The connection's geometric identification and the real quotient-intersection characterization P1.8 remain explicit proof inputs. This is not a proof-assistant certificate or a claim to have executed the absent historical programs.
