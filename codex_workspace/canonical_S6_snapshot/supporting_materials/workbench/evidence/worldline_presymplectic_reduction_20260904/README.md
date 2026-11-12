# Exact worldline presymplectic reduction packet

This packet audits the first-order action

\[
S[x,Z,e]=\int_I\left(
\langle\alpha Z^*Z,\dot x\rangle_L
-\frac e2\bigl(\det(\alpha Z^*Z)-m_0^2c^2\bigr)
\right)\,d\tau
\]

under arbitrary time-dependent left \(SU(3)\) transformations of
\(Z\in\operatorname{Mat}_{3\times2}(\mathbb C)\).

## Main files

- *worldline_presymplectic_reduction.tex*: standalone, line-numbered proof.
- *worldline_presymplectic_reduction.pdf*: compiled fourteen-page proof.
- *worldline_presymplectic_reduction_source_numbered.txt*: stable source-line
  index generated from the TeX file.
- *verify_worldline_reduction.py*: deterministic exact-arithmetic checks.
- *worldline_reduction_checks.json*: structured check results.
- *worldline_reduction_checks.log*: human-readable check log.
- *AUDIT_RECEIPT.md*: scope, build, visual-QA, and hash receipt.
- *WORKLOG.md*: durable task scope, decisions, and completion record.

The proof also contains a line-specific appendix for source lines
875--1654 of *exact_lorentz_observation_bridge.tex*.  It verifies the
algebraic constrained threshold and multiplication spectra, separates
that externally constraint-selected/free-Fock gap from a dynamically
generated interacting gap, and derives the full classical equations
omitted from the packet's displayed constrained action.

## Exact result

For \(m_0>0\), the rank-two \(SU(3)\) quotient is exactly the standard
future-timelike spinless relativistic particle, and its physical phase
space is \(T^*\mathcal H^+_{m_0,c}\).

For \(m_0=0\), the punctured rank-one characteristic quotient is exactly
\(T^*\mathcal N_+^\times\), but the written multiplier action is not the
standard massless variational system.  The composite constraint is a sum
of squared minors and has zero differential on the entire massless locus.
The rank-one equation is therefore \(\dot x=\lambda p\), with no equation
\(\lambda=e\); four real rank-opening directions are first-order null but
not colour gauge; and the \(Z=0\) branch admits arbitrary \(x(\tau)\).

## Reproduction

From this directory:

    python .\verify_worldline_reduction.py
    pdflatex -interaction=nonstopmode -halt-on-error worldline_presymplectic_reduction.tex
    pdflatex -interaction=nonstopmode -halt-on-error worldline_presymplectic_reduction.tex

The verification program uses SymPy exact arithmetic and contains no
floating-point comparison.
