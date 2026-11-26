"""Record the completed paper-local main-theorem scope comparisons."""
from S6_SERIES_PUBLISH_c3_edit import *
from S6_SERIES_PUBLISH_c3_main_scope_read import groups

outcomes={
 'A': 'Read the complete final main statement and all five outline steps against the full current statements A1.1, B1, A4.7, A4.9, C4f, E12 and E17, and the already recorded complete proof comparisons. '
      'The conormal defining map, inverse image of torsion and two connecting maps have the same domains. '
      'The nodal normalization u maps to (u^2-1,u(u^2-1)); lambda=1 and lambda!=1 give the stated endpoint and ambient dimensions. '
      'The same cubic has critical parameters 0 and -4/27, explaining the disc bound. '
      'The global part keeps the integral CDP hypotheses, the exact normalization Picard pullback on each irreducible nonnormal support, '
      'all full multiplicities and the zero-map H2 conclusion. The direct-image example uses the same normalized Poincare line and projection, '
      'and the divisor claim keeps the associated-component hypothesis. The two auxiliary corrections remain attached to their exact CDP98 loci.',
 'B': 'Read the complete main statement and all four outline steps against the full D1.2, C3.1, C3.11, C3.7--C3.10, C3.12, C3.6 and D2.7 statements, '
      'with the complete proof comparisons already recorded. The rational formula keeps b2=0 and the b1(Y) term; integral freeness has both integral vanishing hypotheses. '
      'The classification keeps algebraic reduction, a(Y)=1 and the very-general qualifier. The same exclusions and occurrence maps give precisely the stated three types. '
      'For the D2.7 example, the identity lattice monodromy has t-prime=4 and three removed values, giving six components, exactly its three two-component fibres. '
      'For a smooth Hopf bundle, t-prime=1 gives r=s for any nonempty finite set of removed values, exactly one component per fibre.',
 'D': 'Read the full main statement and five outline steps against the full UN1, UN4, UN14 and UN2 statements and the admitted complete proofs. '
      'The mapping-torus pairing is applied to the same proper tube and its boundary. The vertical morphism pi is an isomorphism off the chosen base value, '
      'preserves the valuations on strict transforms and induces exactly the asserted bimeromorphisms of normalization resolutions. '
      'A point blowup changes support Euler number by +2; the following genus-three quartic blowup changes it by -4, for net -2. '
      'Their cohomology changes (Delta b2,Delta b3,Delta b4)=(2,6,2) preserve the precise local scope. '
      'The projective UN2 examples (k,m)=(1,0),(1,1) give -2 and 0, and the construction with arbitrary k,m covers all even integers.',
 'E': 'Read the complete main statement and five outline steps against the full C5b, C5c, E8 and E18 statements, the marked conventions and the admitted proof comparisons. '
      'The root residues, coarse degrees and four direct-image summands agree term for term. Substitution n=0 gives (1,1,1,0), the opened DGKX untwisted special case; '
      'n=-1 gives (0,0,1,0) with zero normalization map, as required by C5b. The nonintegral formulas use the identical marked lattice generators, '
      'finite regular resonance set and local lengths. The determinant keeps its Weierstrass term before restricting to wp(mu)=0. '
      'The constant half-period mu=1/2 in E18 has vanishing square term and nonzero determinant, so it remains in the full theta identity domain. '
      'The original branch, root order-three determinant zero and cusp rank retain their stated coordinate conventions. Historical arithmetic evidence is reused; no fresh computation credit is claimed.',
 'F': 'Read the complete main statement and seven outline steps against the full E5, E6, E13--E15, E2.23, E2.24, inv:E2.5 and inv:E2.2 statements and their admitted proof comparisons. '
      'The rank-two cup map is on the same fibre and base P1; the analytic-germ extension includes nonreduced bases, while algebraic dimension one uses b2=0. '
      'The two surface Kuranishi germs keep their sufficiently-small nonzero scale domains. The positive-comb statement retains the constructed range and fixed affine attachments. '
      'The balanced kernel and Hodge values are asserted only on the proved nonempty open twelve-tooth family. Its rank-three degree -26 kernel has h0=0,h1=23, '
      'and the same Hodge formula gives 49 and 48. General comb splitting remains the final open problem. '
      'Deformation-chain propagation keeps the connected reduced analytic-base domain and the same ordered multiplicity pair; the topological quotients use the exact Kuranishi retraction. '
      'The refined 02Y6/02XE Paper II consumer comparison is already admitted; III/IV and cross-series reconciliation remain pending.',
 'G': 'Read the full main statement and four outline steps against the full ii:LR:covering statement and its admitted complete analytic proof comparison. '
      'The scalar, good fourth root, character, logarithmic vector and fixed cusp fan agree exactly. The inverse maps eta maps to 2eta and v maps to v/2 identify '
      'the Albanese period lattice with modulus omega=tau/2+2kappa. A scalar turn changes it by 1/2. '
      'For Im(omega)>1, modular equivalence would imply |C omega+D|=1 and hence C=0, leaving an integral translation, which cannot give that half shift. '
      'The unique multiplicity-four fibre and meromorphic-field pullback enforce this same comparison for an endpoint biholomorphism. '
      'The explicit source-line lift, cap maps and cusp multiplier give the two-turn closing quotient u=w^2 and its minimal degree, uniformly for the fixed allowed root-line characters.',
}
for letter,outcome in outcomes.items():
    add_event('series:II:'+letter,'II-C3-MAIN-'+letter+'-BODY-SCOPE',
        'used and rechecked in this run',
        outcome+' This is an exposed paper-local outline/body/special-case comparison, not a new independent derivation. '
        'The final C theorem comparison awaits atomic INT admission; final text, rendered first pages and cross-series review remain open. '
        'Papers I and V have not been reopened. No required-check or final-page credit.',
        'S6_SERIES_PUBLISH_II.tex: main theorem '+letter+', its full outline, and '+', '.join(groups[letter]),
        source='code/S6_SERIES_PUBLISH_c3_main_scope_record.py')
print('Six main-theorem scope comparisons recorded. Theorem C, final-page and cross-series gates remain open.')
