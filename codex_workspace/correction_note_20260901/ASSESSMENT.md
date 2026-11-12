# Non-duplication assessment

## Result of the comparison

Levent Alpöge's source manuscript is not missing the qualitative conductor idea. Its
Section 10 already gives the normalization--conductor sequence, constructs a
conductor-supported ambient differential for the proposed fibre, and records
the split-extension coinvariant calculation. Those are source results and are
credited rather than claimed as Codex discoveries.

The strongest material that remains worth saying independently is the
following.

1. **Exact obstruction.** Filtering the conormal sequence by the torsion
   subsheaf gives a canonical connecting map
   \(\delta_A:H^0(\mathscr T_S\otimes A)\to
   H^1(N^*_{S/X}\otimes A)\). After the two endpoint vanishings, the ambient
   twisted cotangent space is \(\ker\delta_A\). This identifies the precise
   missing datum in the printed “immediate” reduction.

2. **Proper test.** The proper morphism over a disc defined by
   \(y^2z=x^2(x+z)+tz^3\) crossed with \(\mathbb P^1\) has smooth total
   space and a nodal-cubic central fibre. A non-torsion gluing bundle has
   \(H^0(\widetilde\Omega^1_S\otimes A)=0\) and
   \(H^0(N^*_{S/\mathcal X}\otimes A)=0\), but
   \(H^0(\Omega^1_{\mathcal X}|_S\otimes A)\ne0\). The bundle can be chosen
   explicitly as \(\mathcal O(P-O)\), so it extends over this displayed total
   space; the gluing multiplier is \(1/3\) (up to inversion).

3. **Local bookkeeping correction.** For ordinary relative one-forms on the
   smooth total-space charts, \(\Omega^1_{R/\mathbb C\{t\}}\) is torsion-free
   but non-locally-free in the bare \(t=xy\) and \(t=xyz\) crossing charts,
   while in a smooth cyclic chart \(t=s^m\) its total-space torsion is
   exactly \(R/(s^{m-1})\,ds\). Restriction to the singular fibre can acquire
   conductor torsion, and a quotient chart needs a separate invariant-module
   calculation. This does **not** make a claim about the exterior powers,
   whose torsion is a separate calculation.

4. **Safe global reformulation.** A single verified twist with
   \(H^2(X,T_X\otimes L_0)=0\), together with the stated compact global
   hypotheses, suffices for the generic vanishing and \(c_3\le0\) conclusion.
   This is a transparent derivation of an intact sufficient criterion, not a
   priority claim.

## What is not yet a standalone result

The reconstructed candidate values \(h^{1,2}=1\), the full Hodge/Frölicher and
Bott--Chern tables, and the global direct-image splittings are interesting
candidate-specific calculations not present in the source, but their current
workbench proofs still depend on unstated global frame, saturation,
base-change, or cup-map bridges. They remain marked for specialist
replication and are not used as headline theorems in `main.tex`.

The note therefore does not claim a complex structure on \(S^6\), does not
claim to disprove CDP20 Theorem 2.2, and does not present the source's
conductor mechanism or coinvariant lemma as new.

## Publication judgment

The proper test family is the only component that plausibly carries enough
independent mathematical content to anchor a short correction note. The
connecting-map formula is the exact conceptual statement that makes that
example useful, but it is elementary; the local module calculation is a
precise correction; and the global criterion is a clean sufficient condition,
not a priority claim. This is worth circulating for expert review, but it is
not represented here as a new proof of the candidate construction or as an
already established arXiv-level novelty claim.
