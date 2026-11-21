# Clean prerelease derivation: 01G9 / cdp:st:D.2.2

Checker: i_provenance_recovery.

The exact original target packet, its D.2.3/D.2.5/D.2.7 statement inputs,
and the exact C.2.G.1 supplement have been read. The target proof and former
checker records have not been opened. Earlier Paper I topology and Euler
arguments are disclosed background. This derivation uses the cited
statements as inputs and does not award new checks to their proofs.

Scope comparison before target release: the original D.2.2 packet omits an
explicit smoothness adjective. The exact current adjacent D.2.1 statement,
isolated by root with its own receipt, explicitly says "smooth compact
complex threefold"; that clarification was applied before checkpoint 14.
The original D.2.1 statement-only extraction has also been compared with
this current statement. The proof below derives D.2.2 for the smooth
connected class to which its cited C.2.G.1 theorem applies. Its proposed
opening will say "smooth compact connected complex threefolds" explicitly.
No singular-total-space reading is certified by this derivation. This
scope issue was identified before opening the target proof.

Let Y be a member of the stated class. The base is the smooth compact curve
of the fibration. The supplied C.2.G.1 theorem applies to the smooth compact
connected total space with b1=b2=0 and two-torus general fibre. Its base
identification sends that curve isomorphically to P1. Composing the given
map with this base isomorphism changes no fibre and conjugates the monodromy
representation by the induced fundamental-group isomorphism. Thus trivial
rational monodromy is preserved, and D.2.5 applies to this very map.

C.2.G.1 gives c3(Y)=e(Y) in {0,2}; D.2.5 gives c3(Y)<=0. Their common value
is therefore exactly zero. Poincare duality for the connected oriented real
six-manifold with b1=b2=0 gives e(Y)=2-b3(Y), hence b3(Y)=2.

For completeness the passage to the individual fibres can be made at the
actual fibration. Properness and generic smoothness give finitely many
critical values. Over their complement the map is a differentiable fibre
bundle with real four-torus fibre of Euler number zero. Additivity and
multiplicativity of Euler characteristic on this finite analytic
stratification therefore give

  e(Y)=sum over critical c of e((Y_c)_red).

C.2.G.1 says every summand is nonnegative. The sum is zero, so every critical
support has Euler number zero; the regular torus supports already do. The
same theorem's exact equality criterion then supplies, for the actual
normalization and resolution maps of these fibres, the three descriptions
listed there. Its hypotheses allow arbitrary singularities and arbitrary
positive component multiplicities, so this deduction has the same scope.
No reduction of the scheme-theoretic multiplicities is used to transport
line bundles or conductor data; reduction is used only for the underlying
topological Euler number as in the cited theorem.

Finally D.2.7 supplies a smooth compact connected example with integral
H1=H2=0, algebraic dimension one, connected fibres, and marked integral
monodromy equal to the identity on H1(A,Z). Tensoring that exact identity
with Q gives the required trivial rational monodromy. Integral homology
vanishing gives b1=b2=0. Compactness makes the holomorphic map proper.
Thus that same example belongs to the target class and proves nonemptiness,
including the stronger integral homology and algebraic-dimension assertions.

The D.2.3 logarithmic-period obstruction is compatible with these inputs
but is not needed for this deduction. No numerical program is needed for
the two elementary integer inequalities. Target-proof reading and its
complete comparison remain pending until this derivation is frozen.

Additional exact current-scope input: `agents/ii_checks_provenance/recovery_20261121T2000Z/S6_SERIES_PUBLISH_II_01G9_D21_current_scope.tex`, SHA-256 `0fe2e3d7ec4d301d730450a278bf38401dd5bc3f2c766e4a7c6ecc3d226f908e`; companion receipt SHA-256 `f8a11e2c75a14a656395db79e7c699e93f2968c41699569bf8ab9958dc172e40`. The target proof remains unopened.
