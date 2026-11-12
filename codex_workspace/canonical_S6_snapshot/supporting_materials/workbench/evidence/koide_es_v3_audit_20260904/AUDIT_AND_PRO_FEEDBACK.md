# Koide–Erdős–Straus v3: independent audit and next exact map

4 September 2026. This feedback is for the **Erdős–Straus/Koide Pro session**,
not the Yang–Mills session. The supplied packet is preserved unchanged in
`source/`. Its archive is 998,504 bytes, SHA-256
`ab5c21cf00268f9019c95ee24b565d05c4d9337c51e4a576ded9e3cc3f0f235e`.

## Results retained

The complete ordered-channel map and inverse are correct with
`delta = n^2/gcd(R*y-n*a,n^2)`. I checked its proof and independently
enumerated reciprocal solutions by the smaller denominator bound
`N/R < y <= 2N/R`, then `z=N*y/(R*y-N)`. This reproduces all 1,430 ordered
states in 665 shells through n=161, without importing the packet's channel
enumerator. The exact terminal determinant is `-delta`, its Smith form is
`diag(1,delta)`, and the residue condition is `ell_1 == -delta (mod 3)`.

The divisor character formula, primitive-ray incidence, retained Lorentz
scale n² and determinant n³, CRT prime saturation, and diagonal multiplicity
proofs are coherent. The independent check reproduces 819 diagonal
certificates for 329 primes below 5000. The supplied verifier also replays
successfully; its 57 character comparisons are floating-point evaluations,
not exact symbolic character-sum computations. The finite-character theorem
itself has an exact orthogonality proof.

The density-one argument is correct. Its finite-set density is exactly
`1 - product((q-2)/(q-1))` for q ≡ 3 mod 4, q not dividing M; divergence of
the reciprocal-prime sum forces lower density one. No universal-prime claim
follows. For example p=73 misses this diagonal ray, but
`4/73 = 1/20 + 1/220 + 1/4015`, from R=7 and primitive ray [1:4].

This analytic mechanism must be situated in existing literature. I obtained
the primary LaTeX of Elsholtz–Tao, *Counting the number of solutions to the
Erdős–Straus equation on unit fractions*, arXiv:1107.1010v6,
https://arxiv.org/abs/1107.1010v6. Appendix A, Lemma A.3 records a stronger
shifted-prime additive-function theorem, attributed to Barban via Elliott.
The packet's exact marked-ray presentation is useful; neither almost-all
solvability nor the underlying prime-factor abundance should be presented
as a new analytic discovery.

## Corrections and exact scope

1. The TeX defines openings for all real delta>0, then asserts
   `A11 >= (delta-1/4)*r^2 > 0`. The last inequality is false at that
   generality. With (r,t,delta)=(2,1,1/8), every Bézout companion has odd x,
   so `A11 = 1/2-x^2 <= -1/2`. All positive **integer channel orders** are
   safe. For a fixed companion the exact positivity condition is
   `delta > (x/r)^2`.
2. If 3 divides delta, the source's gluing admissibility fails. The terminal
   matrix and cokernel are still correct. The paper's qualified remark is
   safer than the pasted turn's unconditional homology statement: do not
   infer a realized global threefold for nonadmissible triples.
3. The full-rank period matrix is an actual complex two-torus in the ambient
   coefficient domain. Membership in the particular global equivariant
   period curve has not been shown. Its exact determinant is retained as
   `-delta`; no coordinate factors have been dropped.
4. The original orthogonal/homothetic map really has no rational image point.
   This is a statement about that map, not about all rational correspondences
   between the two surfaces.
5. The repacked validation instructions refer to paths not present under
   those names. From `source/`, the executable is `verify_extension_v3.py`
   and the paper is `koide_es_extension_v3.tex`. Replay the script from a
   separate copy because it writes `verification_results.json` beside itself.

## New exact continuation: a rational bridge without changing the old map

Keep `A=[[a,b],[b,c]]`, `ac-b²=-delta`, delta>0 rational, and keep
`Delta(q)=4(q1*q2+q1*q3+q2*q3)-q1²-q2²-q3²`.
Define

    D = -1-a²-b²+4a+4b+4ab
    K = 1-2a-2b
    B_delta(A) = (1+2K/D, 2Ka/D, 2Kb/D).

On `a*D*K != 0`, this maps to `Delta=-1` and has inverse

    a = q2/(q1-1)
    b = q3/(q1-1)
    c = (b²-delta)/a.

The precise target open set is `q1 != 1`, `q2 != 0`, and
`D(q2/(q1-1),q3/(q1-1)) != 0`. All maps are regular on these opens.
Indeed, intersect the line `(1,0,0)+lambda*(1,a,b)` with `Delta=-1`:

    Delta = -1 - 2*K*lambda + D*lambda².

The second point is lambda=2K/D. This is a standard rational-point projection,
spelled out here in the packet's exact coordinates, not a novelty claim for
rational parametrization of quadrics.

For integral a,b, K is odd and D cannot vanish: `Delta=0` is anisotropic over
Q, as follows by infinite descent modulo 3 in
`2*Delta = 2*S²-3*U²-V²`, with S=q1+q2+q3, U=q1-q3,
V=q1+q3-2q2. Thus all integral openings with a>0 lie in the source open set.
Their image's exact common denominator is

    abs(D) / gcd(abs(D), abs(2*K)).

For the packet's `A*=[[1,1],[1,0]]`, this gives `(1/3,-2/3,-2/3)`.
Its Delta is -1, it is rational but not integral, and the inverse recovers A*.
The original orthogonal image remains irrational; no contradiction occurs.
The proof and 820 exact denominator cases are recorded alongside this note.

## A bounded, demanding next calculation for Pro

Retain a=delta*r²-x², b=delta*r*t-x*y, ry-tx=1, r,t positive and coprime,
and delta a positive divisor-channel order. Determine exactly when

    D(a,b) divides 2*K(a,b).

Do not replace the Bézout family by all symmetric matrices. Preserve its
companion parameter, the fixed channel state, and the period inequality a>0.
Classify the resulting integral images, test whether the packet's integral
Vieta action pulls back to rational maps preserving this marked opening
family, and compute the exact loss of divisor support or positivity where it
does not. Give proof-bearing forward and inverse formulas, or an exact
counterexample to the claimed invariance. A census may guide that proof but
must not substitute for it. This task does not assert any particle or global
complex-sphere interpretation.

## Reproducibility boundaries

`verify_independent.py` and `independent_results.json` cover this audit's own
checks. `replay/` contains a separate replay of the supplied program. Original
source hashes are verified against `source/SHA256SUMS.txt`; copied controlling
source extracts are compared to the current canonical files in the intake
receipt. A first independent-test draft had an incorrect hand-entered example
at p=73; its exact fraction assertion failed, and it was replaced with the
directly reconstructed (20,220,4015) example before this note was issued.
