"""Record completed exposed readings for main E/G and two C dependencies."""
from S6_SERIES_PUBLISH_c4_edit import *

readings = [
('cdp:st:C5b', 'C5B', 'Read the complete root-curve calculation. The stated character representatives give the integer d(n); the explicit frame and coefficient maps give the two direct-image differentials and their cokernel O plus O(-1) plus O(2), with the length-two root term. Coarse polynomial cohomology, the epsilon torsion character and the normalization semigroup {0,3,4,6,7,...} give every displayed dimension. The rank-zero n=-1 source has dimension one exactly as stated.'),
('cdp:st:C5c', 'C5C', 'Read the complete nonintegral calculation. The lattice resonance equations identify the same Fourier-character complexes. The explicit frame operations give the regular modules C_s squared and O/(s squared), while the cubic computation keeps the nonzero cubic transverse coefficient and the O/(s squared) plus O/(s cubed) modules. Finite-root characters give both local lengths. The displayed cusp inclusion, projection and contracting homotopy prove acyclicity. Proper coherent analytic support combined with the countable resonance description makes the support finite, yielding the full tuple and normalization surjection.'),
('cdp:st:E8', 'E8', 'Read the complete period calculation. The explicit index-six identity-induced isogeny transports the raw lattice to the symmetric period matrix. Theta heat, eta and logarithmic derivative identities give the exact determinant with its square term. The original wp-zero branch yields the stated g2-squared/g3 expression; root parameters give the order-two zero, rank-one cubic point and rank-two quartic and cusp tensors.'),
('cdp:st:E18', 'E18', 'Read the complete half-period comparison. The elliptic-line quotient and degree-six isogeny retain the same period maps. The theta product signs prove wp(1/2;i)>0, so the determinant is nonzero at the displayed point where the square term vanishes. The proper direct-image calculation retains the ranks 2,3,1 and the full local maps.'),
('ii:LR:covering', 'LR-COVERING', 'Read the complete four-step source, lattice, cap and descent proof. Exact Weierstrass coordinate changes retain the physical line and cusp attachments. The marked lattice gives a one-turn shift a to a+delta/4. The reduced multiple-fibre Albanese modulus is tau/2+2kappa; the imaginary-part estimate and integer translations exclude the half-shift isomorphism, and the intrinsic meromorphic field identifies the unique multiple fibre. The cap root s^4=t, L=s^2U, L^2=B0 inverse and source involution give the two-turn lift. Its norm is t inverse times B_u inverse, transported through the cap and each fixed cusp cone. The four-turn family and free residual involution yield u=w^2; all fixed constant root characters retain the same minimal degree.'),
('cdp:st:D.1.9', 'D19', 'Read the complete transgression proof. Rational b1=b2=0 makes H1 integral zero and H2 integral finite. The nonzero integral transgression image dZ and the local meridian comparison give a nonzero fibre character at every support. An irrational exponential gives the required non-torsion line. Integral H2 zero is used only for the stronger primitive-image clause, so the rational-hypothesis application in main C retains the proved scope.'),
('cdp:st:C.2.G.1', 'G1', 'Read the complete current sign proof before its bounded main-C wording repair. The rational ambient hypotheses give the base and character input; smooth and nonnormal irreducible cases use their exact full-support comparisons. The minimal-Hopfs and irrational-ruled equality cases use P4.36/P4.37/P4.32. The admitted INT1-3 arguments supply the reducible Euler summands and exact equality maps. Global Euler additivity and the skew H3 pairing give the two ambient values. The separate final C comparison corrects the wording of the reduced normalization composite into the full fibre.'),
]
comparisons = [
('E', 'Every integer formula, character representative, rank locus and exceptional source dimension matches C5b under the same marked physical-line parameter. The nonintegral lattice equations, finite root lengths, finite resonance set, tuple and surjection match C5c. The period matrix and determinant, original-branch expression, root orders and cusp rank match E8; E18 separately supplies the exact comparison that the square term alone does not determine the determinant. The complete receiving proofs and main statement have been read.'),
('G', 'The main statement fixes exactly the scalar B_u=uB0, good fourth root, root-line character, logarithmic vector and periodic cusp fan used by ii:LR:covering. Its one-turn nonisomorphism follows through the explicit multiple-fibre Albanese and intrinsic meromorphic-field maps. Its degree-two descent uses the complete two-turn source-line norm on every cap and the residual quotient. The constant-root-character clause is retained by the same proof. The complete receiving proof and main statement have been read.'),
]
path = ROOT / 'S6_SERIES_PUBLISH_c4_global_comparison.md'
text = path.read_text().replace('Main C awaits the horizontal/interface admission; E and G remain to be compared in this continuation.', 'Main C has a separate final comparison in progress after horizontal/interface admission; A, B, D, E, F and G have complete root comparisons.')
for label, short, outcome in readings:
    add_event(label, 'II-C4-ROOT-READ-' + short, 'used and rechecked in this run', outcome,
              'Complete exposed current statement and proof in S6_SERIES_PUBLISH_II.tex',
              source='code/S6_SERIES_PUBLISH_c4_global_eg_readings.py')
    text += '\n## Complete receiving proof: ' + label + '\n\n' + outcome + '\n'
for letter, outcome in comparisons:
    add_event('series:II:' + letter, 'II-C4-GLOBAL-' + letter, 'used and rechecked in this run',
              outcome + ' No independent derivation, required-check completion, final page-reading credit or first-part closure is claimed.',
              'S6_SERIES_PUBLISH_II.tex; complete receiving proof comparisons',
              source='code/S6_SERIES_PUBLISH_c4_global_eg_readings.py')
    text += '\n## Main theorem ' + letter + '\n\n' + outcome + '\n'
path.write_text(text, newline='\n')
print('Complete exposed proof readings:', len(readings))
print('Bounded global comparisons: E, G')
print('No independent credit, derived refresh, unit closure or final PDF credit.')
