#!/usr/bin/env python3
"""Bounded outline/reader-route corrections and records; never edits shared source."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import csv,re
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation4_horizontal'
s=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
STAMP=datetime.now(timezone.utc).isoformat(timespec='seconds')
WHO='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited reasoning effort not separately exposed; fourth continuation, complete-outline/reader-route review'
guards=[]
def add(ident,old,new,owner,reason):
 assert s.count(old)==1,(ident,s.count(old))
 guards.append(dict(change_id=ident,old_text=old,new_text=new,owner=owner,reason=reason))
add('II-C4-OUTLINE-B2',r'''\item\hypertarget{step-II-B-2}{} Fibre adjunction and divisor
Riemann--Roch give the displayed Chern and coherent-Euler
identities. Surface classification supplies the finite necessary
list (\cref{cdp:st:C.3.1}).''',r'''\item\hypertarget{step-II-B-2}{} Fibre adjunction and the tangent
sequence give the displayed Chern identities; Noether's formula
gives the coherent Euler number. Surface classification supplies
the finite necessary list (\cref{cdp:st:C.3.1}).''','series:II:B','C.3.1 uses the normal tangent exact sequence and Noether formula on the same smooth fibre. The outline now identifies these exact operations, preserving all Chern and coherent-Euler conclusions.')
add('II-C4-OUTLINE-B3',r'''\item\hypertarget{step-II-B-3}{} The explicit surface-group and
monodromy comparisons exclude the bielliptic, Kodaira and Inoue
entries; relative algebraic reduction forces the Hopf
fibre to have algebraic dimension zero
(\cref{cdp:st:C.3.7},
\cref{cdp:st:C.3.8},
\cref{cdp:st:C.3.9},
\cref{cdp:st:C.3.10},
\cref{cdp:st:C.3.12}).''',r'''\item\hypertarget{step-II-B-3}{} Relative Albanese maps and the
ambient second-cohomology vanishing exclude bielliptic fibres.
Picard quotients and period comparisons exclude the Kodaira
cases. For Inoue fibres, the form $d\log\operatorname{Im}w$
has zero meridian periods and gives a nonzero class in $H^1(Y,\R)$.
Anticanonical relative linear systems make a very general Hopf
fibre have algebraic dimension zero
(\cref{cdp:st:C.3.7},
\cref{cdp:st:C.3.8},
\cref{cdp:st:C.3.9},
\cref{cdp:st:C.3.10},
\cref{cdp:st:C.3.12}).''','series:II:B','Complete readings show distinct explicit arguments: C.3.7 relative Albanese/Kahler area; C.3.9/.10 Picard quotients, canonical covers and periods; C.3.12 the real-affine closed form and meridian descent; C.3.8 anticanonical systems. The old group/monodromy wording did not describe all five supplied proofs.')
add('II-C4-B-MECHANISM',r'''\textit{Mechanism.} The exact homology sequence of the complement
identifies the monodromy coinvariants, and the resulting integral
restrictions and surface-group comparisons determine the fibre types.''',r'''\textit{Mechanism.} The exact homology sequence of the complement
identifies the monodromy coinvariants. Relative Albanese and Picard
comparisons, surface classification and period calculations then
determine the possible general fibres.''','series:II:B','Match the reader route to the actual five surface-exclusion proofs and the separate component-count argument; all theorem hypotheses and conclusions stay byte-identical.')
add('II-C4-OUTLINE-E4',r'''\item\hypertarget{step-II-E-4}{} Properness of the direct-image
support makes the regular resonance set finite. The cusp adds
one reduced degree-two skyscraper and its nonzero map to the
normalization target. Leray gives $(0,J_z,1+J_z,0)$
(\cref{cdp:st:C5c}).''',r'''\item\hypertarget{step-II-E-4}{} The countable isolated resonance
loci and the Fourier contractions give a regular point with zero
fibre cohomology. The coherent direct-image support is therefore
a proper analytic subset of the compact base curve, hence finite.
The cusp adds one reduced degree-two skyscraper and its nonzero
map to the normalization target. Leray gives $(0,J_z,1+J_z,0)$
(\cref{cdp:st:C5c}).''','series:II:E','C5c proves proper analytic support using countable isolated resonance loci plus an acyclic point and semicontinuity. The outline now includes that premise; properness/compactness by itself does not supply zero-dimensionality.')
add('II-C4-OUTLINE-G4',r'''\item\hypertarget{step-II-G-4}{} The source-line lift of the
marked translation has square $tB_0$. Its two-turn endpoint map
extends through the good-root cap and every cusp chart. On the
$B_u$-quotient its square equals the prescribed four-turn closing map,
including the cusp multiplier. The free involution on the family closed after four
turns has quotient parameter $w=r^2$ and $u=w^2$
(\cref{ii:LR:covering}).''',r'''\item\hypertarget{step-II-G-4}{} The source-line lift $C$ satisfies
$C^2=tB_0$. Put $U=C^{-1}$ and $u=r^4$. The two-turn map
$\widetilde D_r=-r^{-2}U$ has cap expression
$-r^{-2}\zeta^2U$ and extends through every cusp chart.
Its exact norm is
$\widetilde D_{-r}\widetilde D_r=t^{-1}B_u^{-1}$.
On the $B_u$-quotient this gives the four-turn closing multiplier
$t^{-1}$, with cap multiplier $\theta/t$ for $\theta=\zeta^4$
and the same cusp period relabelling. The resulting free involution
on the family closed after four turns has quotient parameter
$w=r^2$ and $u=w^2$ (\cref{ii:LR:covering}).''','series:II:G','The complete owner distinguishes the lift C from its inverse U by an explicit inverse map. The endpoint is -r^-2 U, with exact norm t^-1 B_u^-1, cap multiplier theta/t and cusp period relabelling. Writing these maps prevents the C-square from being read as the endpoint norm; the complete cap/fan closing is preserved.')
a=s.index('\\subsection{How the paper is organized}')
b=s.index('\\begin{figure}',a)
old=s[a:b]
new=r'''\subsection{How the paper is organized}
\Cref{part:II:cotangent-fibre-geometry} develops the index,
Picard and direct-image calculations, the smooth-fibre classification,
and the cotangent and conductor arguments. It ends with the full
normalization criterion of Theorem~A in
\cref{sec:II:global-normalization-criterion}.
\Cref{part:II:irreducible-euler} treats irreducible supports:
normalization topology, canonical boundaries, local transverse
singularities and the equality cases for their Euler numbers.
It includes the compact construction with three doubled nodal
supports in \cref{ii:three-doubled-nodal-fibres}.

\Cref{part:II:periods-tangent-deformations} computes period ranks,
Picard resonance, tangent cohomology and deformation spaces for the
marked families. It contains the conductor nonvanishing arguments,
the open twelve-tooth splitting calculation in \cref{inv:E2.5},
and the Liu--Rollenske parameter covering.
\Cref{part:II:component-geometry} studies component covers,
meromorphic fields, integral component lattices and horizontal
conductors. Its elliptic-interface arguments give the reducible-fibre
Euler equality criterion in \cref{cdp:st:C.2.INT.3}.
\Cref{part:II:compact-occurrence} constructs compact torus fibrations
with the stated component types and classifies marked Hopf, ruled
and elliptic supports with their full multiplicities.

\Cref{part:II:canonical-reduction} develops the component contractions,
canonical-order reduction and finite rooted generation, ending with
the Euler sign and equality criterion for arbitrary torus fibres in
\cref{sec:II:all:12}.
\Cref{part:II:remaining-splitting} states the remaining comb bundle
splitting problem in \cref{inv:E2.3}. Its degree bounds, cup-duality
reduction and twelve-tooth case are proved in
\cref{prop:II:comb-kernel-bounds,prop:II:comb-cup-duality,inv:E2.5}
of \cref{part:II:periods-tangent-deformations}.
The figure identifies five premise uses in the proof of Theorem~A.

'''
add('II-C4-READER-ROUTES',old,new,'sec:results','Checked every final seven-part title and owner location. Route P205 to Part II; the open twelve-tooth calculation to Part III; the newly admitted INT3 to Part IV; and the established degree/duality proofs to Part III while the remaining problem is stated in Part VII. Preserve all seven existing part anchors and the premise figure.')
def write(path,data,fields):
 with path.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(data)
write(OUT/'S6_SERIES_PUBLISH_outline_guards.tsv',[{k:r[k] for k in ['change_id','old_text','new_text']} for r in guards],['change_id','old_text','new_text'])
defects=[]
for n,r in enumerate(guards,1):
 defects.append(dict(change_id=f'II-C4-OUTLINE-D24-{n:02d}',type='D24',statement_id=r['owner'],old_location=r['owner'],old_page='current post-horizontal/Stage20/21 source; integrated pages pending',new_location=r['owner'],new_page='receiving source; integrated PDF pending',old_text=r['old_text'],new_text=r['new_text'],reason=r['reason'],review_status='complete outline/reader-route comparison; guarded correction ready for central review; global rows remain open'))
write(OUT/'S6_SERIES_PUBLISH_outline_defects.tsv',defects,['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status'])
r=s
for g in guards:r=r.replace(g['old_text'],g['new_text'],1)
for pat in [r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}']:
 assert Counter(re.findall(pat,s))==Counter(re.findall(pat,r)),pat
print(len(guards),'unique guards;',len(defects),'bounded D24 rows; labels and targets unchanged.')

# These outcomes describe complete exposed proof readings made in this phase.
# They are not independent re-derivations or mathematical program executions.
readings=[
('cdp:st:A.1.1',
 'Read the complete statement and proof. The generic-point injection makes the reduced-hypersurface conormal map injective; the inverse image of torsion gives the two exact sequences. Their cohomology with the same locally free coefficient identifies ambient sections with the connecting-map kernel under exactly the two endpoint vanishings. Compared every clause with outline A.1.'),
('cdp:st:B1',
 'Read the complete nodal-family statement and proof, including its radius and properness checks. The normalization u maps to (u^2-1,u(u^2-1)), with inverse u=y/x and node preimages +/-1. The differential 1-lambda, inverse-image torsion line, product maps, explicit extending gluing line and lambda=1/3 computation give the printed dimensions in the stated local noncompact setting. Compared every clause with outline A.2 and the local-family abstract clause.'),
('cdp:st:A.4.7',
 'Read the complete proof through resolution, Stokes, local primitives and finite fibre-product descent. The constructed local-system class is the image of the same unitary twisted torsion-free differential, and the unitary maximum principle kills its kernel on the connected compact support. Verified the singular and reducible domains and the exact injection used in outline A.3.'),
('cdp:st:A.4.9',
 'Read the complete integral-CDP proof. Checked each smooth-surface group calculation, finite-cover transfer, Kodaira central-extension Koszul complex and Inoue mapping-torus eigenvalue argument. The marked diffeomorphism transports the identical integral character; punctured-neighbourhood comparison and proper semicontinuity give the stated support vanishings. Compared outline A.3 and both premise-figure applications, keeping the integral hypotheses.'),
('cdp:st:C4f',
 'Read the complete normalization-criterion proof. The full Cartier filtration, persistent full-fibre normalization pullback, final layer with its -mS factor and exact normalization submodule prove both directions. The separate torus and Hopf direct-image arguments give the generic equivalence and all-twist degree-two obstruction. Compared outline A.4, the abstract and all receiving premise arrows with these exact maps.'),
('cdp:st:E12',
 'Read the complete proof. The elliptic Poincare family is represented by the moving evaluation map O(-0) to O with simple zero, giving the reduced degree-one skyscraper; tensoring with the P1 O(-2) cohomology gives the length-one degree-two direct image. Compared the stated support, length and degree with outline A.5.'),
('cdp:st:E17',
 'Read the complete divisor-twisting proof. Finite-dimensional stabilization and local Krull intersection identify the stable section space with sections on associated components disjoint from the divisor. The no-embedded-components condition and the graph-fibre local ring and inverse projection give exactly the eventual vanishing assertion used by A.5.'),
('cdp:st:D.1.2',
 'Read the complete component-count proof. The nonempty puncture set makes the base group free; its lifted generators give the split abelianization and coinvariant quotient. Rational b2=0 gives the numerical formula. The separate integral H1/H2 assumptions, compact-support sequence and duality prove the free integral quotient and rational base. Compared all B.1 claims without strengthening the rational occurrence domain.'),
('cdp:st:C.3.1',
 'Read the complete smooth-fibre necessity proof. The tangent sequence and trivial normal line give the canonical and second-Chern restrictions; torsion-freeness in top integral cohomology gives c2=0. Noether formula gives chi(O)=0. Relative pluricanonical images and classification give the necessary very-general list. Corrected B.2 to name these exact operations.'),
('cdp:st:C.3.6',
 'Read the complete Hopf occurrence proof. Checked the C-action, unique S3 times S3 cross-section, explicit irrational diagonal contraction and eigenmonomial meromorphic-function calculation. The free finite quotient produces the secondary examples, retaining integral H2=Z/m and rational b1=b2=0; local charts give the proper bundles. Compared B.4 with its actual occurrence domain.'),
('cdp:st:C.3.7',
 'Read the complete bielliptic exclusion proof. The normalized base graph, relative Albanese compact surface and vertical resolution maps retain the same smooth fibres. Pulling back a Kahler area class gives the contradiction between the ambient rational degree-two vanishing and its positive fibre integral. Replaced the B.3 summary by this exact Albanese argument.'),
('cdp:st:C.3.8',
 'Read the complete Hopf algebraic-dimension proof. Effective anticanonical elliptic fibres, the finite-cover orbit invariants and the relative anticanonical linear system yield a second algebraically independent meromorphic parameter for the excluded case. Verified the very-general algebraic-dimension-zero conclusion and described this argument exactly in B.3.'),
('cdp:st:C.3.9',
 'Read the complete secondary-Kodaira exclusion proof. The finite etale canonical primary cover, oriented Picard quotient, bounded period parameter, nonzero transgression isogeny and norm comparison give an ambient line with the required multiple sections. Its relative linear system contradicts algebraic dimension one. Compared B.3 and its mechanism paragraph with these maps.'),
('cdp:st:C.3.10',
 'Read the complete primary-Kodaira exclusion proof. Checked both transgression cases, fixed primitive Albanese periods and isotriviality, explicit nilmanifold automorphism on H2, logarithmic coefficient projection and the nonzero wedge functional. The resulting ambient relative linear system supplies the contradiction. Compared the exact Picard and period argument with B.3.'),
('cdp:st:C.3.12',
 'Read the complete Inoue exclusion proof. Real-affine first-coordinate transitions glue d log Im(w); Schwarz-Pick makes every meridian period zero. The descended real degree-one class is nonzero, and the diffeomorphism-type argument treats the entire smooth locus. Recorded this explicit class and meridian argument in B.3.'),
('cdp:st:C.2.UN.1',
 'Read the complete local-parity proof. The tube-support equivalence and Poincare-Lefschetz sequence give the boundary Betti congruence, with even rank of the skew middle form. Wang reduces the parity to the Lambda2 monodromy kernel. Reciprocal eigenvalues and the symmetric wedge-form Cayley transform prove that kernel dimension even. Compared both D.1 and D.2, retaining arbitrary singularities and multiplicities.'),
('cdp:st:C.2.UN.4',
 'Read the complete vertical-refinement proof. Exact blowdown and exceptional-bundle maps give +2 for a point and -4 for the following genus-three quartic. The displayed full-fibre equations and blowup charts retain strict multiplicities. Iteration proves every even target, cofinal zero-Euler domination and the component-adding refinement. Compared every D.3 assertion.'),
('cdp:st:C.2.UN.14',
 'Read the complete normalization-type preservation proof. Strict-transform maps give bimeromorphisms of normalization resolutions and preserve the base-function valuations. New exceptional surfaces have the stated projective-bundle projections; subsequent transforms preserve their classes. The punctured marking is transported by composition with blowdown, including simultaneous compact refinements. Compared both directions of D.4.'),
('cdp:st:C.2.UN.2',
 'Read the complete projective-occurrence proof. The genus-two Abel embedding, successive marked section centres, split normal sequences and disjoint point centres give the exact reduced normal-crossing fibre charts. Curve and point blowups give 2(m-k), and the displayed compact projective constructions realize each even value. Compared D.5.'),
('cdp:st:C5b',
 'Read the complete integral twist and normalization-rank proof. Checked root degrees and invariant frames with inverse division, both direct-image differentials, the three line summands and the finite length-two term. Coarse line cohomology, root torsion and the semigroup generated by 3 and 4 give every dimension and rank. Kept the one-dimensional source and zero normalization map at n=-1. Compared E.1 and E.2.'),
('cdp:st:C5c',
 'Read the complete nonintegral resonance proof, including the full extension complex. Fourier contractions, invertible frames and exact invariant complexes give the regular modules and cubic coefficient, O/(s^2) plus O/(s^3) modules and finite-root lengths. The cusp chain inclusion, projection and homotopy give the acyclic logarithmic complex and reduced degree-two quotient. Countably many isolated resonances and an acyclic regular point give proper coherent analytic support, hence finiteness. Compared E.3/E.4 and added the missing finiteness premise to E.4.'),
('cdp:st:E8',
 'Read the complete period-rank proof. The identity-induced index-six isogeny gives the symmetric periods and exact tensor comparison. Theta heat and eta derivative identities retain the square and Weierstrass terms. The original zero-branch equation gives -g2^2/(36 pi^2 g3), with the stated cubic order, quartic rank and nonzero logarithmic cusp determinant. Compared E.5.'),
('cdp:st:E18',
 'Read the complete half-period comparison proof. The exact physical-line quotient and degree-six isogeny retain the same period tensors. Theta products give positive wp(1/2;i), so the determinant is nonzero where its square term vanishes; the proper direct-image calculation gives ranks 2,3,1. Compared the separate comparison used by E.5 without transferring its locus to the original zero branch.'),
('cdp:st:E5',
 'Read the complete infinitesimal stability proof. Cup product in the fixed cohomology basis is (b u1-a u2) tensor eta1 wedge eta2; rank two gives injectivity. Leray and local freeness locate the global tangent image in the pulled-back base H1, zero on P1. Checked the critical-point image ideals and every F.1 assertion.'),
('cdp:st:E6',
 'Read the complete all-order stability proof. For every small Artin extension, torus unobstructedness and the embedding H1 surjection lift the fibre. The lifted Cartier equation kills the restriction of the map-obstruction cocycle; Leray kills it globally. The absolute Douady graph construction, unit direct image and graph isomorphism locus include nilpotents. Formal smoothness gives the analytic section, connected torus fibres and the algebraic-dimension assertion under its additional b2=0 premise. Compared F.2.'),
('cdp:st:E13',
 'Read the complete nodal two-parameter Kuranishi proof. Checked multiplicative connection residues, root-curve tangent bundles and the two distinct-node residue determinant. The independent cross-ratio and elliptic-modulus directions give the tangent isomorphism; the inverse-function ideal argument proves the full smooth reduced two-dimensional germ and tuple. Compared the corresponding F.3 clause.'),
('cdp:st:E14',
 'Read the complete cuspidal two-parameter Kuranishi proof. Explicit Weierstrass source and physical-line maps preserve scale and the smoothing parameter; the root-line comparison extends in two parameters. The critical ring C[x]/(x^2), row (1,-i+i x), determinant i and the nonconstant smoothing image give two independent tangent directions. The inverse-function ideal argument proves the stated full Kuranishi germ. Compared the corresponding F.3 clause.'),
('cdp:st:E15',
 'Read the complete positive-comb Kuranishi proof. Verified the three root-character bundle comparisons, tangent dimensions, cusp cup injection, root graph constraints and H1 vanishing. The bounded cusp construction retains the fixed affine classes and realizes every period direction. Three marked critical values kill the base vector field; the tangent isomorphism makes the full Kuranishi ideal zero. Compared F.4 with the same constructed positive-comb range.'),
('push:src:E.2.23',
 'Read the complete connected-base separation proof. Local miniversality gives openness. The explicit finite local projection, curve through an open point and a closure point, normalization and disc propagation prove closedness. Passing to the reduction retains fibre classes; finite chains preserve the same coprime ordered pair, and the connected period family supplies the converse. Compared F.5.'),
('push:src:E.2.24',
 'Read the complete smooth-topology separation proof. The Cinfinity Kuranishi retraction uses an isotopic diffeomorphism, and the connected reduced Kuranishi family carries the exact E2.23 alternative. Saturation under both stated diffeomorphism groups and the quotient topology give the open-and-closed separation. Compared every F.6 clause.'),
('inv:E2.2',
 'Read the complete comb Hodge/cup-kernel proof. The root-invariant E/G extensions, exact normal quotient and displayed wedge maps give the tangent cup kernel; the residue length and free higher direct image give the Hodge formulas with the same K_m. Compared F.7 and its twelve-tooth substitution.'),
('inv:E2.5',
 'Read the entire twelve-tooth flat-kernel proof. Checked the seed maps, free node kernel with image ideal (x,y), sufficient mixed-jet condition, conic frame maps and inverse, and explicit diagonal-frame Jacobian. The twelve quotient witness meets the conic smoothability open set. Exact collapse and vanishing of higher pushforward transport the two cohomology vanishings; degree -26 and the section/quotient argument give O(-8) plus O(-9)^2. Compared F.7 and the abstract, preserving the nonempty open fixed-marking scope.'),
('ii:LR:covering',
 'Read the entire source, lattice, Albanese, topology, cap and cusp-fan proof. Checked the one-turn lattice shift and half-period nonisomorphism, physical-line coordinate maps and intrinsic fibration. The source lift satisfies C^2=tB0; its explicit inverse U gives the endpoint -r^-2 U, cap expression -r^-2 zeta^2 U and norm t^-1 B_u^-1. The cap multiplier theta/t and every fixed cusp period relabelling agree with four-turn closing. The free residual involution gives w=r^2 and u=w^2. Compared all four G steps and made the exact inverse/norm explicit in G.4.'),
('cdp:st:C.3.11',
 'Read the complete classification-synthesis and full-fibre cohomology proof. The preceding exclusions and occurrence constructions give the very-general list. Smooth-locus continuation and full-fibre base change retain the torus and Hopf alternatives; in the Hopf branch the Euler-length argument gives R1 O=O and R2 O=0. Compared both outgoing premise-figure arrows and the B synthesis with these exact domains.'),
('lem:II:persistent-normalization-pullback',
 'Read the complete persistent-pullback proof through every Cartier layer and ruled conductor case. The finite-kernel norm, exact reduced/double horizontal conductor and blowdown maps, Gauduchon degree and elliptic-Jacobian bounds produce the inverse-Jacobian section. The rank-two direct image leaves finitely many Picard kernel points; the connected ambient image is trivial, and line/inverse descent uses pi_*O. Compared all three incident premise-figure arrows and the full-fibre C4f application.'),
('ii:three-doubled-nodal-fibres',
 'Read the entire three-doubled-support construction and proof, including every lattice, filling and integral restriction computation. The marked period/lattice maps, equivariant source-line smoothing, full-chain charts and free order-four quotient give 2S with elliptic ruled normalization. Three annular gluings, the common character and exact half-integral transgression give integral H1=H2=0, e=0 and b3=2. Compared the exact abstract clause and located the proof in the irreducible-support part. Printed program calculations were read; no program was executed.'),
('prop:II:comb-kernel-bounds',
 'Read the complete degree/section bound proof. Exact root-to-coarse Hom entries and invariant-generator division give source degree -2 and target degree 2m. The actual cokernel length gives deg K=-2m-2+e and the section/Hodge bounds. The two explicit comparison matrices have their stated kernels; no assertion of their occurrence in the comb family is introduced. Located the full proof in the period/deformation part for the final reader route.'),
('prop:II:comb-cup-duality',
 'Read the complete cup-duality proof. The wedge map J and its explicit inverse, with dual transition -beta transpose, identify the precise tangent cup cokernel dual twisted by det G with the kernel. Finite averaging and pushforward preserve the identity, including the actual cokernel torsion. Located the proof in the period/deformation part and compared the exact remaining-problem route.'),
]
assert len(readings)==38
comparisons=[
('series:II:A','exposed complete outline comparison',
 'Compared all five A outline steps with their complete owners A1.1, B1, A4.7/A4.9, C4f, E12/E17 and the full P263 support. Retained the local nodal-family domain, integral-CDP twists, all full Cartier layers, exact connecting maps and both normalization-criterion directions. No A outline correction is needed. This is an exposed outline comparison, with no independent, literature-search or program-execution credit.'),
('series:II:B','exposed complete outline comparison',
 'Compared all four B steps with D1.2, C3.1, all five complete surface-exclusion proofs and C3.6; reused the full D2.7 reading recorded at publish:c4:global-C:013. Compared C3.11 synthesis as well. Three guards correct B2, B3 and the mechanism paragraph to the exact tangent/Noether, Albanese, Picard, period and meridian arguments. Main B and the rational versus integral domains are unchanged.'),
('series:II:D','exposed complete outline comparison',
 'Compared all five D steps with complete UN1, UN4, UN14 and UN2. The tube/Wang parity, skew and symmetric pairings, exact point/quartic blowup maps, cofinality, normalization multiset and projective 2(m-k) construction all match. Every full-fibre multiplicity and punctured marking is retained; no D outline change is needed.'),
('series:II:E','exposed complete outline comparison',
 'Compared all five E steps with complete C5b/C5c/E8/E18. Checked integral root degrees and rank loci, all regular and root resonance modules, cusp maps, finiteness and the exact original-branch determinant comparison. E4 now supplies the proved acyclic point and proper analytic support before finiteness. Every displayed formula and scope is unchanged.'),
('series:II:F','exposed complete outline comparison',
 'Compared all seven F steps with complete E5/E6/E13/E14/E15, E2.23/E2.24 and comb E2.2/E2.5. Checked all Artin orders and nilpotent graph loci, full Kuranishi ideals, fixed affine attachments, connected-base and Cinfinity separation, exact collapse and twelve-tooth open-family scope. No F outline change is needed.'),
('series:II:G','exposed complete outline comparison',
 'Compared all four G steps with the entire LR covering proof. Exact marked lattices, Albanese inverse maps, intrinsic fibration and unique multiple fibre prove the one-turn obstruction. The G4 guard writes C, its inverse U, the endpoint composition, cap multiplier and cusp relabelling before the free degree-two quotient. All constant-root-character and fixed-cusp data remain those of the theorem.'),
('series:II:outline','exposed complete premise-figure comparison',
 'Read the entire five-arrow figure and its premise table against complete C3.11, A4.9, P263 and C4f. Verified each exact supplying/receiving application, including the full-fibre filtration, persistent inverse-Jacobian section and the Hopf torsion direct-image/all-twist branch. No arrow or caption correction is needed. Reread all A-G receiving outlines, including the already admitted C repairs, after applying the six guards in memory.'),
('sec:results','exposed abstract and seven-part reader-route comparison',
 'Read the entire abstract, common series table and organization paragraphs. Compared all abstract claims with the complete owners, including P205 and the open twelve-tooth proof; no abstract correction is needed. Checked all seven final part titles, each named section and actual owner location. The route guard locates P205 in Part II, P320/P321/E2.5 in Part III, INT3 in Part IV and G1 in Part VI, while the remaining problem is stated in Part VII. Reread the complete receiving route and B mechanism; all main A-G statement environments are byte-identical and all replacement references exist. Global rows stay open.'),
]
event_fields=['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where']
events=[]
for owner,phase,outcome in [(a,'complete exposed supporting proof reading for outlines and routes',b) for a,b in readings]+comparisons:
 ident=f'publish:c4:outline:{len(events)+1:03d}'
 marker='\\label{'+owner+'}'
 assert s.count(marker)==1,(owner,s.count(marker))
 events.append(dict(statement_id=owner,date=STAMP[:10],who=WHO,type='used and rechecked in this run',outcome=outcome,event_id=ident,phase=phase,source_file='S6_SERIES_PUBLISH_II.tex',source_row=str(s.count('\n',0,s.index(marker))+1),source_event_type='used and rechecked in this run',evidence_group=ident,publish_input_file='',publish_input_row='',date_utc=STAMP,where='agents/continuation4_horizontal/S6_SERIES_PUBLISH_outline_comparison.md; complete current proof/outline and receiving six-guard comparison'))
assert len(events)==46 and len({e['event_id'] for e in events})==46
write(OUT/'S6_SERIES_PUBLISH_outline_CHECK_EVENTS.tsv',events,event_fields)

units=list(csv.DictReader((ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv').open(),delimiter='\t'))
proposals=[]
for unit,detail in [
('series:II:main-theorems','The B mechanism now names its complete owner arguments; the A-G main statement environments are byte-identical. The root main-statement comparisons and admitted separate C comparison remain the supporting records. Keep this row open pending central admission and the parent whole-unit global gate.'),
('series:II:outline','Every A/B/D/E/F/G step has a complete clause-to-owner comparison; the admitted C comparison covers all six C steps. The six-guard receiving first part was read completely. Keep this row open pending central admission and the parent whole-unit global gate.'),
('how-the-paper-is-organized','The complete abstract, five-arrow premise figure, seven final part titles and exact reader-route owner locations were read. The guarded route locates each established proof and the remaining problem precisely. Keep this row open pending central admission and the parent whole-unit global gate.'),
]:
 matches=[x for x in units if x['paper']=='II' and x['unit_id']==unit and x['row_kind']=='defect' and x['defect_type']=='D24']
 assert len(matches)==1,(unit,len(matches))
 u=matches[0]
 proposals.append(dict(paper='II',unit_id=unit,unit_title=u['unit_title'],row_kind='defect',defect_type='D24',prior_status=u['status'],proposed_status='open',date_utc=STAMP,evidence='agents/continuation4_horizontal/S6_SERIES_PUBLISH_outline_comparison.md; S6_SERIES_PUBLISH_outline_guards.tsv; CHECK_EVENTS.tsv publish:c4:outline:001-046',detail=detail))
write(OUT/'S6_SERIES_PUBLISH_outline_unit_proposals.tsv',proposals,['paper','unit_id','unit_title','row_kind','defect_type','prior_status','proposed_status','date_utc','evidence','detail'])
print(len(events),'honest exposed reading/comparison events;',len(proposals),'existing D24 rows retained open.')
