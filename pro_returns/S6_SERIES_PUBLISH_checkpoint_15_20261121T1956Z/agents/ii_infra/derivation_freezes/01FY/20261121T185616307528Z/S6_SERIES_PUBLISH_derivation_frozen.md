# Independent derivation: cdp:st:D.1.13 (tag 01FY)

The target proof remains unopened. Inputs read are the exact statement packet and supplement, the root-separated D.1.6 data packet, the already frozen/compared D.1.4, D.1.7–9 and D.1.12, and the stated E1 field theorem. I opened Wang's primary construction, source order_two_rational_homology_sphere_new.tex, lines150–292,297–425,493–676 and1440–1460, in addition to its main homology statement. I also opened Serre, Un théorème de dualité, Comment. Math. Helv.29 (1955), Theorem4 and its corollary, printed p22, and the preceding duality construction. The primary theorem applies to compact complex manifolds and every holomorphic vector bundle, with dualizing bundle K. This permits an independent absolute-duality route to R2, without needing a singular relative-duality theorem as an unverified input.

## 1. Canonical form on the original quotient

Wang starts from the rational elliptic surface S→P1 with singular fibres IV*, I2, I1, I1, and M=O_S(P−O). The primary source verifies K_S=π*O(-1). Over a base open set where a frame of O(-1) is fixed, let η be its image in K_S. On the complement M× of the zero section define the three-form η∧dv/v in a local line-bundle frame. Changing v to h(x,t)v changes dv/v by dh/h. Its wedge with the top two-form η on S is zero. Thus these local forms glue, with exactly the transition functions of π*O(-1). The lift F covers translation on the elliptic fibres. Locally η=dt∧α where α is the invariant elliptic one-form; the base-varying translation changes α only by a dt term and preserves dt∧α. The fibre multiplier in F adds another one-form pulled back from S to dv/v. Consequently F preserves the displayed three-form, which descends to the smooth torus quotient. This defines an isomorphism f*O(-1)→K_Y over the punctured base.

## 2. Extension through the three Mumford fillings

At the two rank-one points Wang's toric coordinates have a primitive exponent vector, either (2,1) or (1,0). The explicit monomial map (z,v)↦(x,y)=(v,v²/z) has determinant1 on character lattices. It therefore carries dlog z∧dlog v to dlog x∧dlog y. The rational elliptic canonical form at a multiplicative fibre is a unit times dq∧dlog z: its residue on the normalization is the invariant differential and has nonzero residue at the two branches. Hence the descended three-form is a unit times dq∧dlog x∧dlog y. In a regular rank-one chart with q=XY, it is, up to a fixed sign, dX∧dY∧dlog Z. This is a nowhere-zero holomorphic three-form because Z is a nonzero coordinate. At a rank-two chart q=X0 X1 X2, the corresponding form dq∧dlog X1∧dlog X2 equals dX0∧dX1∧dX2. The regular height-one fan charts differ by unimodular monomial maps, so these expressions are compatible and nonvanishing. Period translations preserve them and have no boundary stabilizers. Thus the same canonical-bundle isomorphism extends through all three fillings, with no added divisor there.

## 3. Extension through the multiplicity-three fibre

Use Wang's s=1/t, s=r³, X=s²x, Y=s³y, x'=r²x, y'=r³y. Thus X=r⁴x', Y=r⁶y'. A local generator of K_S is ds∧dX/Y. Its pullback is

3r²dr ∧ (r⁴ dx'+4r³x' dr)/(r⁶y') = 3 dr∧dx'/y'.

This is holomorphic and nowhere zero on the smooth good-reduction elliptic family. Wang's comparison of line-bundle frames is v'=r²v. Since dlog v=dlog v'−2dr/r, the extra term vanishes after wedging with dr. The three-form therefore pulls back to 3dr∧dx'/y'∧dlog v', a nowhere-zero form on the smooth torus family. The twisted gluing map is translation by σ(r)=(log r)/(2πi) ell. Such a base-dependent fibre translation preserves relative invariant forms modulo dr terms, so it preserves this total form. The deck map multiplies dr by ω^-1, the elliptic differential dx'/y' by ω, and the kernel differential by1 modulo the other two directions. Its determinant is1. The translation twist has determinant1 as well. Wang proves that this order-three action is free; hence the invariant nonzero form descends to a nonzero canonical form on the quotient. The canonical isomorphism across the puncture therefore has zero divisor on the multiplicity-three support too. We have proved K_Y≅f*O(-1) on the entire compact threefold by the explicit form map.

## 4. The top direct image by absolute Serre duality

D.1.12 applies because the primary homology gives b2=0 and general fibres are two-tori. It gives locally free E=R1 f_*O of rank2 and G=R2 f_*O of rank1, and det E≅G. Write G=O(b). Connected fibres and the normal base give f_*O=O. For every integer m, projection formula and coherent Leray over P1 yield

H3(Y,f*O(m))=H1(P1,G(m)).

Absolute Serre duality on the smooth compact threefold identifies its dual with

H0(Y,K_Y⊗f*O(-m))=H0(P1,O(-m-1)).

Thus h1(O(b+m))=h0(O(-m-1)) for every m. Choose m less than both -b-1 and -1. The two dimensions are -b-m-1 and -m. Equality gives b=-1. This proves G≅O(-1), and det E≅O(-1).

## 5. Degree-one splitting and all coherent dimensions

Split E=O(a)⊕O(-1-a), ordering a≥-1-a, so a≥0. The integral Leray construction of D.1.9 supplies beta whose restriction to each full fibre is a nonzero coefficient class. Its associated section of E is nowhere zero, since zero evaluation in E would map to zero fibre cohomology. For a>0, the second summand has negative degree and no global section; every section of E is a section of O(a) in the first summand and has a zero. This contradicts beta. Therefore a=0 and E=O⊕O(-1). Coherent Leray gives h0(Y,O)=1, h1=h0(E)=1, h2=h1(E)+h0(G)=0, h3=h1(G)=0. Degree-one base change at every fibre is provided by D.1.12. On a smooth torus, restriction is the edge map followed by evaluation and this base-change isomorphism. Evaluation of O contributes rank1 and O(-1) contributes rank0, so restriction has rank1 at every smooth fibre.

## 6. Integral hypotheses, field and published comparison

Wang's primary homology has H1=0, H2=Z/2 and H3=Z/2. The integral UCT gives H1(cohom)=Hom(H1,Z)=0 and H2(cohom)=Hom(H2,Z)⊕Ext(H1,Z)=0. The E1 input applies to b2=0 and the Kähler smooth tori, giving the exact field isomorphism f*:M(P1)→M(Y), hence a(Y)=1. CDP20 Corollary5.2 and Proposition5.5 were opened in the primary source: their surjectivity/nonnegative-degree claims contradict respectively the just-proved rank1 into a2-dimensional fibre cohomology and the summand O(-1). This is an explicit counterexample under their integral cohomology assumptions. An integral homology six-sphere has H2=0, whereas H2(Y)=Z/2. Any homeomorphism would induce an isomorphism on H2 by functoriality, impossible for those groups; this specifies the precise homological obstruction to such an identification. No stronger classification comparison is claimed.

The separate fresh program checks the local Jacobian/wedge factors and the elementary cohomology-dimension calculations, without reading or importing any previous program or target proof.
