# Paper I: nine-target comparison and settled discrepancies

## Scope, chronology, and evidence

This record concerns ari:C.6.1, ari:C.6.2, ari:C.7.1,
ari:C.8.1, ari:C.8.2, ari:C.8.3, ari:C.8.4,
ari:C.8.11, and ari:C.8.12 in the attached original
source/S6_SERIES_GRIND_I.tex, SHA256
d2e6c3bec1500144bfc0ef85e636ded534f2abc998cf58fdaf521b1e8a183169.

The nine preread derivations were sealed at
2026-11-21T01:16:01.072050+00:00. The sealed Markdown has SHA256
24982458daf1814e677dcee90371a1ea6364e6969d6b6018f82009044ce16112.
The exact seal also binds the two new programs, their outputs, the extracted
statements, and the primary-source receipt. Only afterward were the printed
proofs extracted and read. Their full text and source spans are retained in
S6_SERIES_PUBLISH_I_nine_printed_proofs.json.

The original exposure note is preserved. The proof of dependency C.7.6 and
other adjacent dependency material had been exposed before this assignment;
none of these nine target proof bodies had been opened before the seal.
The broad earlier norm search displayed formulas at original source
lines 30930–31134. The nine target proof spans, recorded by extraction, are
28398–28432, 28450–28466, 34361–34419, 7846–7937, 7947–8112,
8124–8150, 8184–8215, 30289–30323, and 30380–30412, respectively.
Thus those earlier isolated formulas were outside these targets. The
cp-periods/ca-sup/ca-exp/ca-GHbounds/ca-derivatives/ca-H/ca-delta-h
anchors are internal target-proof anchors, not independent input statements.

The event type is a **targeted proof check** for the actual preread scopes
below. External literature, the previously checked C.4.1 normalization,
and the read C.3.1/C.3.2/fam:C.1.1 dependency statements remain inputs.
No whole-result independence from those inputs is claimed.

## Settled discrepancies

### A. A mistake in the checker’s sealed derivation

In the first sigma–theta display of the sealed C.7.1 derivation, the
denominator was incorrectly written as \(2\pi\eta(\tau)^2\).
The printed proof correctly has \(2\pi\eta(\tau)^3\).
The exact general-lattice formula is
\[
 \sigma(u)=\frac{\omega_1}{2\pi\eta(\tau)^3}
 e^{\eta_1u^2/(2\omega_1)}
 \vartheta_1(u/\omega_1,\tau).
\]
Indeed \(\sigma'(0)=1\), whereas the Jacobi product gives
\(\vartheta_1'(0,\tau)=2\pi\eta(\tau)^3\). With this prefactor and
\(\Delta=(2\pi)^{12}\omega_1^{-12}\eta^{24}\), the product
\(|\Delta|^{1/12}|\sigma(u)|\) contributes
\(|\vartheta_1/\eta|\), exactly as required. The Legendre correction gives
the Gaussian already derived.

The sealed file is not altered to conceal this error. This constant
calculation receives **comparison/recheck credit only**, not pristine
preread credit. C.6.1’s archimedean normalization uses the already checked
C.4.1 input; it does not rely on the erroneous line. The relative-period
calculation in the preread C.7.1 section does not use this prefactor.

### B. C.7.1: the literal all-logarithm clause is false

The printed statement says that “choices of logarithms” change its bracket
only by purely imaginary integral multiples of \(2\pi\). For a fixed
elliptic lift \(u\), changing the ordinary logarithm \(\log\sigma(u)\)
does indeed add \(4\pi i\mathbb Z\). A change of elliptic lift has the
different, exact transport already derived before opening the proof:
\[
 B(u+\omega)-B(u)\equiv
 u\eta(\omega)-\omega\eta(u)+2\log\chi(\omega)
 \pmod{4\pi i\mathbb Z},
 \quad B(u)=2\log\sigma(u)-u\eta(u).
\]
Here \(\sigma(u+\omega)=\chi(\omega)
e^{\eta(\omega)(u+\omega/2)}\sigma(u)\).
For \(u=a\omega_1+b\omega_2\) and
\(\omega=m\omega_1+n\omega_2\), Legendre gives
\[
 u\eta(\omega)-\omega\eta(u)=2\pi i(bm-an).
\]
This is purely imaginary, but need not be an integral multiple of \(2\pi i\).
For an algebraic elliptic curve, take the algebraic nonzero 3-torsion point
with \(u=\omega_2/3\), and change the lift by \(2\omega_1\). Its phase is
\(4\pi i/3\) modulo \(4\pi i\mathbb Z\), since
\(\chi(2\omega_1)=1\). The hypotheses \(P\ne O\) and \(2P\ne O\) hold.

The exact clause refinement has id ari:C.7.1:lift-transport, retaining
the original statement label and tag and adding tag IA01. The norm identity
and relative-period conclusions are unchanged. The correction is recorded
as a **refuted** event on the original clause with that refined id, as
requested by the parent. The guard includes the transport proof, not only
a weaker verbal invariance assertion.

### C. C.8.12: a missing factor in an intermediate proof equation

The printed intermediate equation
\[
 \frac{t-1}{t'_\tau}=-\frac{E_6}{2\pi iE_4}
\]
is false. From
\(t=E_4^3/(E_4^3-E_6^2)\) and
\(t'_\tau=-2\pi it E_6/E_4\), the exact result is
\[
 \frac{t-1}{t'_\tau}=-\frac{E_6}{2\pi iE_4^2}.
\]
The sealed preread had already obtained the equivalent correct expression
\(-3\pi i p^2/g_2^2\). The fresh symbolic comparison gives printed-minus-
correct equal to \(iE_6(E_4-1)/(2\pi E_4^2)\).
The theorem’s radial formula is correct after this one-factor repair.
This is a D25 correction to an intermediate assertion, **not a refutation
of the unchanged radial theorem**.

## Target-by-target comparison

| Target | Scope actually derived before reading | Comparison outcome |
|---|---|---|
| C.6.1 | Canonical division-function constant from the local pole; exact scaling law; global weighted decomposition and complex-embedding multiplicities; algebraicity of the finite product; rational family discriminant | Agrees. The printed proof alternatively obtains the global height by iterating duplication and the product formula; that particular iteration was read at comparison. The printed sigma identity has the same division sign. |
| C.6.2 | Solve the multiplication law on the identity component, with all valuation signs; general-model \(\psi_2=2y+a_1x+a_3\) transported by completion of the square | Agrees. The source’s nonsingular-reduction test includes residue characteristics 2 and 3. No later numerical height table is claimed checked merely from this formula. |
| C.7.1 | Logarithmic algebra after the norm formula, explicit Serre factor and differential, relative-period coordinate, exact elliptic-lift transport, and dual-polarization sign | Period calculation agrees. The sigma prefactor mistake in the preread is disclosed above and excluded from preread credit. The literal branch clause is refined by the exact transport. |
| C.8.1 | Whole-strip Gaussian/eta bound via convexity; separate cusp estimate using a directly bounded \(\wp\) Fourier remainder | All assertions agree. The independent upper bounds are 1.425900,1.694403,1.478416,1.419343 at the relevant endpoints and 1.062978 for the cusp. The different printed rational endpoint/cusp estimates were subsequently recomputed. |
| C.8.2 | Full polydisc Fourier majorants, ODE bootstrap at the square lattice, two-zero Rouché argument, \(|\delta|<20|h|^2\), and strict negative quadratic loss | Agrees by a different local estimate. The preread loss coefficient is below 0.810, leaving a positive margin above 0.760. The printed proof uses a larger polydisc and sharper \(|\delta|<7|h|^2\); all its constants were separately checked after reading. |
| C.8.3 | Explicit \(E_6\) boundary lower bound, nonvanishing \(\Delta_0\), and two applications of Rouché for actual coverage of the \(t\)-disc | Agrees. The preread boundary bound is above 0.0032087, exceeding 1/500. The printed weaker bound 121/43200 also passes. Homothety transports both zero sections and the norm exactly. |
| C.8.4 | Division functions reconstructed by rational tangent doubling, exact \(A_1,A_2,A_3\), one-disc triangle bound, and all-\(k\) limit from the root chart | Agrees. No attached division-polynomial code was imported. The printed coarse five-coefficient bound was separately recomputed and passes. |
| C.8.11 | Wirtinger derivative with the factor 1/2, period-matrix determinant, implicit \(\wp\) differentiation and the exact \(R\) formula | Agrees. The new symbolic differences are identically zero. The half-period case remains covered by the stated root-chart input, rather than division by \(p=0\). |
| C.8.12 | Modular/translation/sign transports, correct \(t\)-derivative substitution, radial formula, endpoint limits and strict negativity under the stated \(|F|<1\) hypothesis | Statement agrees; intermediate denominator repaired as above. No global \(|F|<1\) assertion is inferred from this proposition. The final endpoint computation \(F(0)=3/4\), \(X(0)=1/4\), \(X(1)=0\) uses the read C.3.2 expansion. |

## Computational coverage and method

1. S6_SERIES_PUBLISH_I_nine_analytic_bounds.py/.out/.json was written and
   run before target-proof access. It uses 75-digit outward interval
   arithmetic, finite positive Fourier sums, explicit geometric tails,
   an ODE bootstrap, and Rouché inequalities. It proves estimates on entire
   discs/strips; it does not infer a maximum from a grid.
2. S6_SERIES_PUBLISH_I_nine_symbolic.py/.out/.json was written and run
   before target-proof access. It constructs division functions from
   rational tangent/chord doubling, checks the exact polynomials and
   constant factors, solves the finite-height valuation identity, and
   verifies the Wirtinger/implicit/radial algebra symbolically.
3. S6_SERIES_PUBLISH_I_nine_printed_scalars.py/.out/.json was written
   after reading the printed proofs. It recomputes every displayed scalar
   estimate in C.8.1–4 using outward interval evaluation and explicit
   Gaussian tails instead of the printed 80-term exponential Taylor
   arithmetic. Exact rational arithmetic checks all Rouché, quartic,
   triangle and coefficient margins. The C.8.12 missing-factor discrepancy
   is explicitly evaluated symbolically.

All assertions pass. Representative original-proof margins are:
the cusp exclusion bound 0.315855 is below 1/3; the cusp norm 1.081373 is
below 541/500; the larger-polydisc \(|G|\) bound 27.383927 is below 30;
the \(|H|\) bound 0.644177 is below 2/3; the quartic constant is exactly
318748/2205, below 150. These rounded numbers summarize the outward
enclosures retained in the JSON; they do not replace those enclosures.

The elementary Taylor remainder in the printed proof follows directly
because consecutive terms after \(x^{81}/81!\) have ratios at most
\(x/82<1\) on \(0\le x\le20\). The rational polynomial and differential
identities are checked exactly. No unexplained numerical certificate
is required for these nine results.

## Primary literature actually inspected

- DeMarco–Mavraki, arXiv:1701.07947v2, §2.1, pp.5–6: canonical height,
  product-formula weights, local decomposition and duplication convention.
- Bertolin–Philippon–Saha–Saha, arXiv:2010.15170v2, §2.3,
  equations (2.10)–(2.13), pp.7–8; Definitions 2.3–2.4 p.8; Table 1 p.24;
  §6.1 pp.26–27: the extension factor, exponential, relative logarithm,
  and one-motive. The elliptic factor has divisor \((-P)-(O)\);
  the exact identification with the class \(P\) is
  \(P\mapsto t_P^*\mathcal O_E(O)\otimes\mathcal O_E(O)^{-1}\).

The PDF/image hashes and scope are in
literature/S6_SERIES_PUBLISH_I_nine_primary_scope_receipt.json.
These are locator-scoped reads, not claims to have checked either whole
paper. The operative relative-period section is §2.3; an earlier
provisional pointer to §2.2 is explicitly corrected.

## Guarded corrections and remaining work

S6_SERIES_PUBLISH_I_nine_correction_guards.json contains five guarded
old/new edits against the current work source. Each old snippet occurred
exactly once. The parent reports that all five are now integrated. No root
TeX was edited by this agent.

The nine assigned checks are complete with the above exact scopes and
settled discrepancies. Publication editing of the assigned analytic and
arithmetic sections is a separate next task. Each rewritten proof will be
compared against its old proof and receive scoped reread events. A final
main-theorem comparison remains to be done after those edits are integrated;
this record does not pre-credit that future comparison.
