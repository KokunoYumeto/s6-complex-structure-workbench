# SX, 033C and 033O: complete comparisons

Completed 2026-11-21T21:12:58.792290+00:00. All three derivations were frozen at 21:03:30 UTC before the target arguments were opened. The locator-only 033O exposure is explicitly archived.

Final guard file: `a52c8aadf120198414bededb44f66bd874786c0a9cb1bbd40936124e9135d23d`; five complete guards containing sixteen literal edits. No canonical mutation or event append has occurred.

## 01SX — inv:E2.4

The prerelease derivation uses the explicitly permitted E15 tangent-cohomology statement, the primary comb diffeomorphism Phi_m, and the AC main theorem item (4). The composition transports the complex structure to S6; the actual permitted member m=12 has h0(T)=25. This verifies the target counterexample without claiming a fresh independent derivation of the deeper E15 input.

After release I read the complete HKP v1 Corollary 1.3 proof, first in the attached source and then in the downloaded primary PDF, actual printed page 2. It expresses a third field using meromorphic coefficients and invokes the CDP assertion that these functions are constant. The exact source diagnosis in the target is therefore correct.

The injective pullback f_m^*:C(t)->M(X_m) follows from surjectivity of the algebraic reduction in the cited primary comb statement: a rational function with zero pullback vanishes at every base point where defined, so is zero. Hence the pullback of the coordinate t is nonconstant. The numeric counterexample, the historical error diagnosis, and the assertion h0(T_X0)=1 for the original member have distinct explicit scopes.

The proposed proof retains the numeric counterexample and the source diagnosis, gives the exact function-field map, and deletes only the redundant closing assertion and neighbouring algebraic-dimension-zero disclaimer. The HKP bibliography retains its journal/DOI and pins v1, 13 December 1998; all cited preprint page locators refer to that actual edition.

Freeze SHA: `665d9031655b6810ae2624631f3cd5b62241d3a9e9189b9f075b73fce30b793b`. Original block SHA: `212e76e5b8fa84d4e1f3dac5995f1b6318d7df095fef1d4cc52051dc03457293`. Final proposed block SHA: `e86ca445104d994aa4c5511d01405a24b232cac7430d4a3ff1d9db79f932401a`.

## 033C — push:src:E.2.4

The prerelease derivation obtains the precise corollary from permitted statements E.2.23 and E.2.24. Reduction of the analytic base has the same points and point fibres, and preserves properness/smoothness by base change. This explicitly accounts for the target allowing nonreduced bases while E.2.23 names reduced ones.

The finite-chain conclusion follows by induction at each common joining member; the converse for equal pairs is an explicit input conclusion of E.2.23. For a continuous family, the inverse image of the fixed-pair clopen locus from E.2.24 is a nonempty clopen subset of the connected parameter space, hence the entire parameter space.

The original proof gives a roadmap of the deeper closure, cusp and propagation arguments and then warns that local miniversality alone gives only openness. The new complete proof cites the two actual operating theorems and gives the short deduction. Deleted upstream references map to their role as proof ingredients of E.2.23/E.2.24, whose mathematical conclusions remain explicitly cited.

Structural review is pending: the body corollary combines conclusions already separately stated in E.2.23/E.2.24. Root has been asked to decide its D12/anchor/owner treatment. No count credit for those other owners is proposed. Reading the released old roadmap exposed the finite-projection/curve-normalization outline of still-unfrozen 0339; that cross-target exposure is recorded and no clean independent 0339 credit will be claimed by this checker.

Freeze SHA: `5c9b8a56298948835ea727a96f92d38aa5fab5473a3c6364ec4b9d290b2d5323`. Original block SHA: `41ab3cdf2e728c025af925b6d8777c2fd5ea8592c88f0e58bac2d6ee300b1bb6`. Final proposed block SHA: `2bcc9e06c2a66b993848400fdfe44817083efa5fa6fcc9c8cb059000cab4bd04`.

## 033O — push:src:E.5.2

Input matrices were supplied in the closed statement. The only prefreeze target snippet was a source-locator sentence identifying primary Proposition 4.2, explicitly approved by root and hash-disclosed. The primary statements mat and mum were read before freeze; no target arithmetic was read until after freeze.

The prerelease Fraction program computes the exact pairing transport H=T^{-t}, all four matrices, ordered monodromy product, order four, both simultaneous centralizers, integral fixed equations and the norm. The manual coordinate parameterizations give the entire integral kernels, not only a rational basis.

The norm columns are exactly 4 ell,2 delta,-2 delta,4 delta. The quotient map [a ell+d delta]->(a mod4,d mod2) has exactly that norm image as kernel and the evident basis-vector inverse. The three vanishing images are primitive by explicit integer generators. The primary specialization morphism and UCT identify those images with the geometric specialization kernels by the exact dual-annihilator argument in the frozen derivation.

After release the complete primary Proposition mat proof was read. The postrelease fresh polynomial check verifies the winding calculation over Z[d,c], the fourth-power entry 4(c+d^2), the rank-one minor 2d^2-c, and the four-matrix product. The sign change of the marking is explicitly D=diag(-1,1,1,-1), conjugating every T_i(d) to T_i(-d).

The pinned old e_push_two_parameter.py source was fetched from the known commit and matched its positive Git blob entry. Only exact lines 1–43 were read and run. Its SymPy matrix inversion/nullspace, HNF and SNF results match the fresh rational and explicit integral calculations. The norm Smith ordering is Z/2 plus Z/4; the explicit isomorphism to the printed Z/4 plus Z/2 swaps the coordinates. Later program scope was excluded.

D25: the original words inverse transpose cannot define a map on the entire centralizer algebra because E41 is singular. The proposed proof gives the linear bijection C->C^t, with inverse itself, using CH_i=H_iC iff C^tT_i=T_iC^t. It sends I,E41 to I,E14. All statement matrices, fixed/norm/vanishing lattices and all displayed mathematical formulas remain unchanged.

The proposed publication proof retains the rational elimination and integral Smith claims, removes file/program narration and defensive contrast, and places the one pinned program link in the end table. The complete original and final proposed statement/proof have both been read line by line.

Freeze SHA: `10685922ae261930d509da8a6f2ccfcbbfd2bdae8b6362a4ade61e81a072801a`. Original block SHA: `02ef624c7f85d85cca2b1b5904010f0b9843091b5f729ac4956bf756e9c5b5b4`. Final proposed block SHA: `68077dac4532c89a34eb43572c67bccf31b1faeee38d3b9d0ab9eba52910b795`.

## Method comparison for the lattice computation

The old isolated routine uses SymPy inversion, symbolic nullspace, Hermite and Smith forms. The prerelease program uses standard-library Fraction elimination and explicit primitive integer parametrizations. The postrelease supplement uses sparse integer polynomials and gives the exact marking conjugation. The norm-quotient ordering is related by an explicit coordinate swap. The current D25 repair concerns only the proof map between matrix-algebra centralizers; every displayed theorem formula is retained.

GW, 033P and 0339 are disclosed as exposed and reserved from any new clean-check claim by this checker. The 033C owner/D12 disposition belongs to root. Final event proposals remain subject to root approval and exact applied-block binding.

## Final v3 exact base-change map

Final v3 reread: i:B_red→B and the fibre product X×_B B_red are explicitly named. The second projection to X is the nilpotent closed immersion obtained by pulling back i, hence has identical underlying topological spaces. At every complex point its fibre is exactly the original fibre product with Spec(C). Properness and smoothness of the first projection to B_red follow from base change. The complete original and complete revised proposed statement/proof were actually reread after this refinement.

Guard SHA: `c6f82bfe5e1e121a8e8334ab4110e49ca41e9a85bf2606fa114d083de5239dcc`; comparison SHA: `4cc502ce1369ab66281c0b5ca6cec0fc3e0e5c9af783d95fefcafaf7352c1f6c`. All previous versions remain immutable.
