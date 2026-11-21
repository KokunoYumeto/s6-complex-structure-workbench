# Partial filling and virtual Euler comparisons

The two preread derivations are saved separately; both target proofs were first opened only afterwards. Source SHA d2e6c3bec1500144bfc0ef85e636ded534f2abc998cf58fdaf521b1e8a183169.

## night:P2.3 (02RD)

All four printed steps were read and compared.

1. The period characters, flat elliptic line bundle and twelve-shift chain coincide with the preread construction. The source supplies exact coordinates X_i=W/r^i,Y_i=r^(i+1)/W and overlap X_(i+1)=Y_i^-1,Y_(i+1)=rY_i. Direct substitution gives X_iY_i=r and the same identity after transition. The unit acts by inverse factors and is compatible with the elliptic line-bundle transition, so it introduces no missing singularity.
2. The source's compact fundamental cover uses uniformly bounded elliptic parallelograms and bounds on finitely many units. Together with the finite twelve-index range and closed overlap graphs, this gives both Hausdorffness and properness on each smaller base chart. This fills in the compactness detail of the preread argument. The local total space xy=r is smooth, and r=0 is reduced NC.
3. The actual gamma coefficient l_j/m_j and character W=exp(-2pi i eta2) give the positive component shift12l_j/m_j. Fresh enumeration of all48 admissible residue pairs modulo12 verifies freeness of each nonidentity finite power, and the monodromy product and connectedness of the Kummer cover. The printed infinity rotation p mod12 equals -b mod12 since p=12l0-b. This checks the exact morphism of cyclic label systems, including sign.
4. The printed overlap is specifically the translation sigma-o of P2.2. This is the actual original punctured family, so gluing over the indicated open cover of the target preserves the base-local proper/Hausdorff properties. The equation xy=r also verifies the extra proof conclusion of parameter-flatness. No extension to the removed corner is claimed. No source fault found.

## night:P2.11 (02RB)

All four printed steps were read and compared. Engel's actual primary p22 was viewed before the derivation; it specifies precisely the normalization and section identification used here.

1. The source identifies the lci pinching, double locus S and smoothing line L=M tensor h*M^-1=O(F_infinity). These are the exact fam:E.1.1 inputs used in the preread derivation.
2. The saved derivation uses the supported K-class on the normalization and the projective-bundle tangent sequence. The printed proof instead expands one local hypersurface Chern fraction, then symmetrizes the two branch corrections. A fresh symbolic graded calculation verifies the single correction -c2(S)+c1(S)b-ab-b², and its sum -2c2(S)+c1(S)(a+b)-(a+b)². With a+b=c1(L)=F and c1(S)=F,F²=0, it gives24-24=0. The independently derived pullback Chern polynomial gives F²(D0+Dinfinity), also zero. The two calculations use the same actual normalization/gluing map and agree in the stated geometry.
3. Flatness makes reduction of the embedding ideal exact at the parameter; lifting its regular sequence and applying Nakayama gives a relative lci presentation. The perfect relative cotangent complex restricts to the intrinsic central complex. For invariance of the compact virtual Chern pairing the preread argument used the earlier analytic specialization lemma push:A.3.1. The printed argument repeats its oriented regular-sequence specialization mechanism. This comparison verifies its application and local algebra; it does not claim another independently established general analytic specialization theorem.
4. The printed Euler stratification has zero contributions from the finite-base scaling-circle strata and from positive-dimensional cusp tori, with two zero-dimensional cusp strata. Its value2 agrees with our independent alternating sum from the established untwisted integral Betti table and with26-2*12 from the semistable normalization. Thus the exact prescribed Q is excluded. The proper modified filling of P2.10 remains within the statement's scope. No source fault found.

## Safe consolidation

P2.11 and push:A.3.2 concern the same Q and same untwisted X(u); fam:E.1.1 provides the identical normalization map. Retain one theorem with both statement labels/tags and one full proof consisting of the explicit Chern calculation above plus invocation of push:A.3.1 and the established Euler2 calculation. The repeated local lci specialization proof can be removed from P2.11 once A.3.1 precedes the combined statement. Keep the independent normalization K-class computation in this check file. Do not merge the nearby nodal or small-resolution models into Q: their actual maps and changed central normalizations must remain explicit.
