# C.1: completed proof and audit record

Read the entire supplied `workbench/cusp_toric_cover_completion.tex`.
Checked the equivariance, the free module basis, the analytic invariant
ring, ramification orders, fibre lengths, and the regular-fibre lattice.
The proof can be shortened without weakening it: freeness and proper
discontinuity of the source lattice action follow from equivariance of the
finite toric power map and the corresponding target properties.

C.1.1 proves all the stated local cover properties. C.1.2 classifies smooth
finite covers of the entire periodic cusp fan. C.1.3 rules out every finite
holomorphic extension from a connected smooth compact source having the
prescribed local map as even one cusp component, for N>1. The identity
case N=1 extends. C.1.4 independently rules out a degree-N^3 extension
with a single preimage cusp, even for a normal singular source.

Exploratory approach: compute the orbit of the local sublattice under the
full monodromy. Exact Hermite-normal-form enumeration ran for N=2 through
8; code and output retained. The general lower bound N^2 follows by the
two explicit matrices D and M0. This resolves the one-cusp degree problem
but initially left the possibility of extra sheets. The adjacent-triangle
smoothness argument resolves that possibility for smooth sources.

Other approaches considered before the fan obstruction: cyclic roots of
O(W), finite affine quotients of the complement group, and subgroup
separability after reduction of the fibre lattice. None is used as a proof
of a smooth extension. A cyclic root gives a normal base change singular
along the double and triple strata; it does not produce the required
smooth local Kummer cover. The final proof does not depend on an
unconstructed finite quotient or a group-separability theorem.

Interpretation: 'branched cover of X' means a finite holomorphic map from
a smooth compact complex manifold. Arbitrary normal singular sources
with extra cusp sheets are not classified or excluded. This qualification
is explicit in the theorem, rather than silently identifying normality
with smoothness.

Further advance: C.1.5 constructs normal singular globalizations with additional cusp sheets, using the explicit finite quotient (Z/N)^4 semidirect G_N and subgroup spanned by g,u. Local normal toric completions give a finite flat map globally. The source is necessarily singular elsewhere for N>1. Exact G_N orders for N=2,3,4 are 48,216,3072. This supersedes the earlier sentence that arbitrary normal sources were not treated.
