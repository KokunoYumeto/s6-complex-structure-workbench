# Superseded catalogue norm-set wording and correction

Status: historical correction record; the current `canonical_scalar_catalogue.py`, `.json` and `.out` are authoritative.

The first catalogue draft put a witness with zero regular dummy-cap norm into the `all_norm_solutions` field. In the one-additive-cap case it forced `n_0=0`; the zero-additive-cap case likewise did not retain both actual regular order-one norms as free variables. Those prescriptions were witnesses, not the complete norm set. No morphism that eliminates an arbitrary regular norm was proved or used in the corrected result.

The exact review message identifying the error was:

> One concrete correction before final audit: row['all_norm_solutions'] for one-cap currently forces n0=0, but SC1 retains the actual regular order-one dummy-cap norm. State the literal full set n_infty=epsilon-m_infty*(n_0+N), with arbitrary n_0,N; zero-additive m∞=m0=1 has arbitrary n∞,n0,N with n∞+n0+N=epsilon (or solve n∞=epsilon-n0-N). The witness n0=0 stays fine. Please update general equations/tests so no unproved gauge normalization sits in the all-solutions field, rerun then continue source transport.

This record preserves the superseded mathematical restriction and its review, rather than reconstructing an unavailable byte-for-byte earlier Python file.

## Exact corrected equations

Throughout, retain the actual regular order-one norms and

`N=sum_j n_j-b_0`,

`D=m_0*n_infty+m_infty*n_0+m_infty*m_0*N=epsilon`, with `epsilon=+1` or `-1`.

For one additive cap, `m_0=1`, all solutions are

`n_infty=epsilon-m_infty*(n_0+N)`, with arbitrary integers `n_0,N`.

For no additive caps, `m_infty=m_0=1`, all solutions are

`n_infty=epsilon-n_0-N`, with arbitrary integers `n_0,N`.

The choice `n_0=0` is retained only as a primitive witness. The two-additive-cap Bezout parameterization already retained all norms and was not changed.

The corrected catalogue was rerun and passed all 437 exact checks. Its branch arithmetic, positive and negative witnesses, source/root Euler data, and canonical/all-fan return formulas remain those of the final certificate. The correction changes the completeness description of the norm set; it does not change the exhibited witness or its return.

Recorded UTC: 2026-11-17T09:42:00.737868+00:00

Authoritative files at this correction record:

- `code/part3/canonical_scalar_catalogue.py`: SHA-256 `6a1173a3002c826f26b7399751bd38a02f8c7718eefe96715df04b22e2786b13`.
- `code/part3/canonical_scalar_catalogue.json`: SHA-256 `0a1fa2b0fd97f4c66e1a3bdd20bb0d63bb51aa58213777ee3bf6b7a150948985`.
- `code/part3/canonical_scalar_catalogue.out`: SHA-256 `c72f7028d81cb8ab189d1080d4cecb950875a44a950a37fca68714d3529fd94a`.
