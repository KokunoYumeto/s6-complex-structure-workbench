# Current Paper I exact calculations

Author: GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort; same model family.
These are new implementations written after the printed proofs were read. They do not import or replay the historical programs named in the received draft. The accompanying guarded publication patches replace those absent executable assertions and preserve the removed wording in their receipts.

## Programs and outputs

| Program | Method | Executed result |
|---|---|---|
| `priority_rows_exact.py` | SymPy rational functions and integer matrices; verified unimodular Smith transformations and primitive integral kernel bases | 79 checks pass; all major matrices and Smith data saved in `priority_rows_exact.output.json` |
| `main_D_double_complex.py` | Python `Fraction`; independent Gaussian elimination on kernels, images and induced maps, with separate corner counts | 54 checks pass for h=0,…,5; complete model matrices and tables saved in `main_D_double_complex.output.json` |
| `a2_scalar_arb.py` | Arb balls through python-flint, 120 decimal working precision, 100 q-series terms and proved infinite-tail bounds | 12 checks pass; strict scalar intervals and full balls saved in `a2_scalar_arb.output.json` |

Each program also has a saved `.stdout.txt`. Results are corroboration at the explicit scope in the mathematical proof. In particular, finitely many double-complex models do not replace the universal decomposition theorem, and numerical scalar bounds do not replace the geometric identification of the connecting map.

## Dependency recipe

The executed environment used Python 3.12.14, SymPy 1.14.0 and python-flint 0.9.0. The second program uses only the Python standard library. The first and third can be reproduced in an isolated local environment:

```sh
python3 -m venv paper_i_replay_env
paper_i_replay_env/bin/python -m pip install sympy==1.14.0 python-flint==0.9.0
paper_i_replay_env/bin/python priority_rows_exact.py
paper_i_replay_env/bin/python main_D_double_complex.py
paper_i_replay_env/bin/python a2_scalar_arb.py
```

The Arb program also accepts the path of an already installed local python-flint dependency through `PAPER_I_VENDOR`. The task's actual dependency installation was into `audit_paper_i/vendor`; no elevated installation is required. Paths are resolved relative to each program, so keep the corresponding output files beside the programs.

## Exact saved outcomes

The integral cone has cochain dimensions 14, 28, 20, 8. Both consecutive differential products vanish. Smith transformations and primitive kernel bases give H0=Z, H1=0 and H2=Z⊕Z/2. The actual obstruction class is detected nontrivially by the saved mod-two functional. The centralizer has rank-14 defining equations and basis I,E41.

The Arb program proves:

\[
0.2366093140807852<C_4<0.2366093140807853,
\]
\[
0.0801022110875382<\Re K_2<0.0801022110875383,
\qquad
0.1387410994022233<\Im K_2<0.1387410994022234.
\]

For N=100 the two q-series tails are bounded by
250(N+1)^4 500^{-N-1} and 1024(N+1)^6 200^{-N-1}.
The program verifies the q bounds and geometric-ratio estimates used in these bounds. An independent Arb gamma-function evaluation of C4 agrees with the modular evaluation.

The current output SHA256 values are recorded in `../priority_assessments_receipt.json`.

## Period-curve followup

`period_curve_exact.py` uses the same SymPy1.14.0 dependency. Its freshly executed18 checks give the complete stabilizer matrices, universal square-zero power law, original cubic discriminant/j identity and finite-root derivative ratios over Q[rho]/(rho²-rho+1). The output is `period_curve_exact.output.json`, SHA256 b0d5ce19c1b9cfacac29d201d5bf9e36db0f6793f2e07238ce7dc4e240d25f5d. This supplements the printed analytic quotient and extension proofs.
