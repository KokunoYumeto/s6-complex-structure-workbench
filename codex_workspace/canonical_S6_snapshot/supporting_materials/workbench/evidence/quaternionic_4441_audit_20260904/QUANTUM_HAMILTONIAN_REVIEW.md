# Homogeneous gauge-scalar quantization: completed independent proof

Completed 2026-09-04. All work is confined to this directory. No canonical
files, remote state, other tasks, or Lean sessions were changed.

The full insertion-ready proof is
[homogeneous_quantization_fragment.tex](C:/Users/user/Documents/math/agent_work/quaternionic_homogeneous_quantization_20260904/homogeneous_quantization_fragment.tex).
The portable checker is
[verify_homogeneous_quantization.py](C:/Users/user/Documents/math/agent_work/quaternionic_homogeneous_quantization_20260904/verify_homogeneous_quantization.py).

## Exact model and constants

The configuration space is
su(3)^3 direct-sum Herm_3(C)_0 direct-sum C^3, of real dimension 38:
24 gauge, 8 Hermitian scalar and 6 real triplet coordinates. A0 is a
multiplier, not another kinetic coordinate. Retained hypotheses:
V3>0, g²>0, hbar>0, m²>=0, Gamma>0, kappa real.

With an orthonormal basis for the original gauge metric -tr and the
corresponding orthonormal Hermitian basis, and b=x+iy without rescaling,
the exact canonical kinetic operator is
\[
T=-\frac{\hbar^2g^2}{4\mathcal V_3}\Delta_{24,A}
  -\frac{\hbar^2}{2\mathcal V_3}\Delta_{8,\Phi}
  -\frac{\hbar^2}{4\mathcal V_3}\Delta_{6,x,y}.
\]
The potential is W=V3 U, with
\[
U=\frac1{g^2}\sum_{i<j}\|[A_i,A_j]\|_{-\mathrm{tr}}^2
 +\frac12\sum_i\operatorname{tr}[A_i,\Phi]^2
 +\sum_i\|A_i b\|^2
 +\frac{m^2}{2}s+\frac{\Gamma}{4}s^2
 -\kappa(\det\Phi-b^*\Phi b),
\quad s=\operatorname{tr}\Phi^2+2b^*b.
\]
The mass-metric volume measure is retained as
\[
d\mu_M=\frac{2^{15}\mathcal V_3^{19}}{(g^2)^{12}}\,d^{38}q.
\]
Its constant factor appears explicitly in the heat kernel. The
semigroup parameter has inverse-energy units; physical Euclidean time
is hbar times that parameter. No hbar=1 convention is used.

## Gauss map, operator and invariant Hilbert space

The complex triplet duality is 2Re(pi_b* db). Therefore the momenta are
Pi_i=2V3 E_i/g², Pi_Phi=V3 X, and pi_b=V3 v. Their momentum map is
\[
\mathcal G=\sum_i[A_i,\Pi_i]-[\Phi,\Pi_\Phi]
 -(b\pi_b^*-\pi_b b^*)_{\rm tf}
 =\mathcal V_3\left(\frac2{g^2}\sum_i[A_i,E_i]
  -([\Phi,X]+bv^*-vb^*)_{\rm tf}\right).
\]
This is exactly the full retained Gauss equation, including sign and
volume. The canonical Hamiltonian with temporal multiplier is
H_A0=H0-M_A0, where M_xi pairs G with xi using -tr.

On L²(Q,dmu_M), the spatially constant group acts by pullback through
inverse SU(3) transformations. Its exact self-adjoint Gauss generators
are closures of -i hbar K_xi dot grad on compact smooth functions.
Their domains are the L² functions whose indicated distributional
derivative is in L². The proof establishes essential self-adjointness,
a compact-smooth graph core, the commutator signs, and the absence of a
divergence ordering term.

The constrained Hilbert space is precisely the simultaneous kernel of
the eight closed generators, equivalently the group-invariant subspace.
Its orthogonal projection is Haar averaging divided by the retained
positive Haar mass. Smooth compactly supported invariant functions are
dense; disjoint invariant radial annuli give an explicit infinite
orthogonal family. This construction does not insert a singular
orbit-space measure or an unproved gauge-fixing formula.

## Friedrichs domain, compactness and positivity

The scalar inequality is proved directly in complex Phi,b coordinates:
\[
|\det\Phi-b^*\Phi b|\leq s^{3/2}/(3\sqrt6),\qquad
V\geq \Gamma s^2/8-\kappa^4/(54\Gamma^3).
\]
The form domain is exactly
H¹(Q) intersect L²((W+C)dmu_M), where
C=V3 kappa^4/(54Gamma^3). Its compact-smooth core and closedness are
proved. A Riesz-resolvent construction supplies the self-adjoint
Friedrichs operator, whose domain is the form-domain elements for which
-div(D grad u)+Wu is in L² distributionally. No unjustified separate
condition Delta u,Wu in L² is substituted.

The fragment includes the independently agreeing moving-sector estimate
\[
a(-\Delta_A)+b\sum_{i<j}\|[A_i,A_j]\|^2
\geq\eta a(-\Delta_A)
 +\hbar\sqrt{6(1-\eta)}\sum_i\|A_i\|,\quad
a=\frac{\hbar^2g^2}{4V3},\quad b=\frac{V3}{g^2},\quad0<\eta<1.
\]
Its oscillator allocation and exact adjoint singular-value calculation
are proved without differentiating a parameter-dependent diagonalizing
frame. Together with the scalar bound this yields compact resolvent
for the full and invariant operators. Parent will replace this local
compactness section with its own complete independently proved version;
the marker COMPACTNESS_INSERTION_POINT identifies the location.

The heat-kernel proof is complete for the actual polynomial W:
bounded truncations, the convergent Duhamel series, increasing-form
resolvent convergence and continuous Brownian bridges give a strictly
positive kernel. The kernel is positivity improving on the full and
invariant Hilbert spaces. The general bounded-below bridge formula is
also checked against [Simon, Theorem 1.1](https://arxiv.org/pdf/math-ph/9907022);
the constants, domain and actual-potential arguments are derived in the
fragment.

A square-root average of the squared orbit amplitudes proves equality
of the full and invariant spectral infima without presupposing a ground
state. Strict positivity proves that the bottom spectral projection has
rank at most one. The actual compactness estimate supplies existence,
so the ground state is unique, strictly positive and SU(3)-invariant.
The physical spectrum is discrete with E0<E1_phys and tends to infinity.
The positive difference E1_phys-E0 is a gap of this finite homogeneous
quantum mechanics. No numerical value, parameter-uniform estimate,
continuum limit, or continuum quantum mass gap is claimed.

## Exact classical embedding and two limitations

Spatially constant configurations map into full smooth torus fields.
The action pulls back to V3 times the homogeneous density; all local
field residuals are constant, so homogeneous Euler-Lagrange and Gauss
solutions are genuine full classical solutions. Constant momentum
densities Pi/V3 pull the full canonical one-form back exactly to the
finite-dimensional one.

The constant-SU(3) quotient is not the full torus gauge quotient.
The explicit periodic transformation
diag(exp(2pi i x1/L1),exp(-2pi i x1/L1),1) maps zero connection and
zero scalars to a nonzero homogeneous flat connection not related by
constant conjugation. The same transformation sends a constant
off-diagonal Phi to a nonconstant Phi. More generally preservation of
all homogeneous triplets forces a spatial gauge function to be constant;
this includes the obstruction for genuinely large spatial transformations.
The periodic diagonal example is not incorrectly classified as a
nontrivial homotopy class in SU(3).

Nor is an automatic quantum-sector embedding claimed. For
Phi=(q+y cos(2pi x1/L1)) diag(1,-1,0)/sqrt2, the integrated quartic
potential is exactly
Gamma V3(q^4+3q²y²+3y^4/8)/4. The mixed term prevents a product sector
of all homogeneous wavefunctions times one fixed normalizable
discarded-mode wavefunction from being reducing. The proof includes
the domain argument for arbitrary initial L² discarded-mode
wavefunctions, and then uses that multiplication by y² has no
nonzero L² eigenvector. A delta function at y=0 is not an L² state.

## Primary provenance and checks

Read the canonical source
output/s6_consolidated_canonical_2026-08-26/supporting_materials/workbench/research/quaternionic_4441_reconciliation.tex
at the current full-density/Gauss section, lines 2347-2465 of the snapshot
read. Those source line numbers may change as parent integrates work.

Read the local primary Tong text
literature_primary/Tong_Gauge_Theory_20260904/gt.txt, lines 2085-2270:
Section 2.2.1 and the beginning of 2.2.2, especially equations
(2.27)-(2.31). Its source SHA256 is
e79e69d704ca4a3fd84f1bdf7ed9095c843506e8fbff7b567f261ad6050f65ba.
Official source:
[David Tong, Lectures on Gauge Theory](https://www.damtp.cam.ac.uk/user/tong/gaugetheory/gt.pdf).
The proof uses his Gauss-after-temporal-gauge principle, not his
different Hermitian-field coefficient normalization.

Executed:

    python agent_work/quaternionic_homogeneous_quantization_20260904/verify_homogeneous_quantization.py
    PASS: 124 exact checks.

The checker uses only SymPy, with no repository dependencies, file writes
or network calls. Its checks include both basis metrics, all 38 masses,
the retained volume factor, eight divergence/skew identities, all 64
Lie brackets, all eight Gauss pairings, the full field Gauss substitution,
the complex triplet momentum convention, the Legendre transform, sharp
scalar-bound constants, oscillator allocation and Fourier coupling.
One matrix identity counts once; every matrix entry is tested.
Analytic self-adjointness, compactness, positivity and spectral arguments
are proofs in the TeX, not claims that a symbolic checker proves analysis.

TeX environment nesting and all 14 unique labels pass structural checks.
The proof fragment's final SHA256 is
0efbf89c29b5ba3934b170210e1460df9d3a329c88d61915bfcadf7ea4cbe2d9.
No PDF build or visual inspection is claimed for this TeX fragment.

One post-snapshot improvement was explicitly sent to parent: the paragraph
beginning "Here invariance means a reducing quantum subspace" supplies the
domain justification in the final Fourier-product obstruction. The proof
fragment is otherwise frozen for integration.
