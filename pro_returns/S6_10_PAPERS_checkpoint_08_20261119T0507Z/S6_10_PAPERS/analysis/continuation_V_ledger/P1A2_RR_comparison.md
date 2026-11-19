# P1A.2 Step9 comparison

19 November 2026, GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro,
S6_10_PAPERS continuation, reviewer /root/ledger.

The entire RR Chern-root derivation and the independently designed fresh
program were saved at04:57:42 UTC, before the printed P1A.2 proof was read.
`P1A2_RR_before_read_receipt.json` retains the exact SHA-256 hashes and
the read-order declarations. The original preread note and program remain
unchanged. Root's Hodge proof and producing programs were not inputs.

The fresh program performs formal exponential-series division and multiplies
the four resulting root series at u,-u,v,-v. All11 exact checks pass.
The universal coefficients found by the written Newton-identity argument
and by this distinct program agree:

    coefficient of c2^2 = (1+y)^4/240,
    coefficient of c4 = (-1-124y+474y^2-124y^3-y^4)/720.

Only after saving and executing those files was the printed ninth item
of the P1A.2 proof in `papers/V/body.tex` opened. Its c4 coefficient is

    (-1+10y-y^2)^2/144 - (1+y)^4/120.

The exact comparison uses a common denominator720. Its numerator is

    5(1-20y+102y^2-20y^3+y^4)
       -6(1+4y+6y^2+4y^3+y^4)
    = -1-124y+474y^2-124y^3-y^4.

Thus the printed universal expression agrees term by term, including
the constant and fourth-degree coefficients. Substitution of the
supplied Chern numbers2 and6 gives exactly -y+4y^2-y^3. In particular
chi(Omega^2)=4. Combined with the separately established zero endpoint
Hodge entries and h^{2,1}=h^{2,3}=1, the alternating sum then gives
h^{2,2}=6; the proof of those other entries belongs to their recorded
reviewers and is not claimed by this receipt.

The owner supplied analytic Hirzebruch--Riemann--Roch as the named input,
with Hirzebruch Theorem25.3.1, Section25.4(a), pages188--190. This
receipt proves the full algebraic RR step from that precise input;
it does not claim a new proof of the analytic index theorem itself.
The source-opening receipt remains the owner's separately attributed
event unless and until a direct additional reading is recorded here.

Subsequent primary-source reading: the official MPIM scan was downloaded
and opened directly. Theorem25.3.1 is on printed page187; Section25.4(a)
is on pages188--190. The source identifies the analytic index of the
Dolbeault operator with chi(V,W), and its topological index with
integral ch(W) Todd(TV), then applies the result to W tensor exterior
powers of the cotangent. The original1978 title and printed pages189--190
were visually inspected. Exact edition, SHA-256, URL and PDF/printed-page
mapping are saved in `Hirzebruch_primary_source_receipt.json`. This
additional reading is separately attributed in the event ledger.

Disposition: targeted before-reading rederivation of the whole RR
calculation in printed Step9, plus a new independent exact computation.
No change to that printed expression is needed. The aggregate whole-row
gate is owned by root; this receipt supplies only its explicitly missing
RR step and does not independently close the other proof steps.
