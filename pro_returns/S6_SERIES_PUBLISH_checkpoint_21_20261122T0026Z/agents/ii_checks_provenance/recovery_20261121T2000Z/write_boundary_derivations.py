from pathlib import Path
import json,hashlib,datetime

ROOT=Path('/workspace/scratch/08a92fb2355d/S6_SERIES_PUBLISH')
D=ROOT/'agents/ii_checks_provenance/recovery_20261121T2000Z/clean_derivations'
R=D.parent
def bind(p): return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
common=r'''
## Scope, exposure and exact inputs

This is a fresh derivation from the exact named statement and its safe cited-input packet and supplement. The target's printed proof, its method outline and old owner-specific check records remain unopened. All eight boundary derivations are being written together before any of their proofs is released. Paper I was extensively read in the earlier publication work, and its established construction is an input here; no claim of discovery independent of Paper I is made. The claim sought is a new derivation of this Paper II target before reading that target's proof. A later complete comparison and source review remain required.

The exact construction packet is S6_SERIES_PUBLISH_II_boundary_construction_inputs.json, SHA c92879fad86dfe710f2771af118d359bdfc51603c2219826a4e80e0f8d4bf7f6. It supplies the integral marking (gammahat, uhat, what, deltahat), the period matrix, finite affine actions, logarithmic connectors, cusp coordinates, toric rays, and the complete pre-IN Phi/Psi definitions. Safe statements supply the invariant and coinvariant lattices and the integral local specialization map. The displayed symbols in this derivation denote those exact maps.

For a chosen based loop g, A_g means its actual homology parallel transport and T_g=(A_g^{-1})^t. Current Paper I labels its positive base meridians counterclockwise, whereas these targets choose clockwise boundary meridians. Reversing a local meridian inverts its transport. For a finite order m transport, sum_{k=0}^{m-1} T^k equals sum_{k=0}^{m-1} T^{-k}, so the norm and the common invariant/coinvariant modules used below have the explicit inverse-loop transport. No unexplained equality of the positive-meridian product with the clockwise based product is used. The based boundary relation itself is taken in the target's zero-section whiskers.

The fresh program S6_SERIES_PUBLISH_II_boundary_preproof_exact.py and its output were written, executed, and completely read before target proof release. It uses Fraction elimination and integer coefficient-basis interpolation, and checks the finite norms, contractions, quadratic shifts, divisor degrees, support-form recovery and Chern matrix. The written arguments prove the analytic and unrestricted assertions. No comparison with an unidentified inherited program is asserted. Timing and hashes are bound in the companion input receipt.
'''

deriv={}
deriv['03IC']=r'''# Prereading derivation: wbII:lem:picard-crossed-defect (03IC)

The flat torus bundle over the pants core P has its zero section. Its section lifts respect composition. With the stated whiskers the relation rho_1 rho_2 rho_0=1 therefore lifts to the stated relation with no vertical factor. The tautological cusp gluing has mu=0 and hence its image ell_0=gamma(mu)=0. Only this forward implication is needed; injectivity of an unspecified map gamma is not being assumed from the parenthetical word “equivalently.”

Let E be the restriction of c_1(L) to a marked fibre. Parallel transport of the restricted line bundle identifies its Chern class, proving A_g^*E=E. Consequently the constant vertical alternating two-form E in flat real coordinates descends to a globally defined closed form Omega_E. It has the same fibrewise cohomology class as c_1(L).

Retract P to its two-loop graph. The cellular filtration of the torus bundle over that graph gives in total degree two

    0 -> H^1(P,V_R) -> H^2(J_P,R) -> H^0(P,wedge^2 V_R) -> 0.

Here the left map is the base-first cup map. This exact sequence can be obtained directly by gluing the two cylinder bundles to one fibre: the only base cochain groups are C^0=V_R and C^1=V_R plus V_R, with differential a -> ((T_rho1-I)a,(T_rho2-I)a). There is no base cell in degree two or higher and hence no missing higher-base differential. The global vertical form proves surjectivity onto its invariant class as well. The difference kappa=c_1(L)-[Omega_E] restricts to zero and therefore has a unique class in H^1(P,V_R).

Choose its two values on free generators, and extend along words by z(gh)=z(g)+T_g z(h); the inverse rule z(g^{-1})=-T_g^{-1}z(g) makes cancellations exact. The cellular coboundary changes z(g) by (T_g-I)a. Applying z to rho_1 rho_2 rho_0=1 gives d_1+T_1d_2+T_1T_2d_0=0; applying V_R -> (V_G)_R gives the barred sum zero. A principal change dies in coinvariants. Since deltahat is fixed by A_0, <(T_0-I)a,deltahat>=<a,A_0^{-1}deltahat-deltahat>=0. This proves representative independence of the indicated number.

Finally restrict to the mapping torus of any rho and a fixed fibre cycle nu. A representative of the base-first edge class is dtheta wedge alpha in a cut cylinder; its integral on the product oriented as (nu,rho) is -alpha(nu). The endpoint correction in the cut cylinder is exactly the crossed-cocycle coboundary already described, so it vanishes on the fixed cycle. Thus <z(rho),nu>=-<kappa,a_*([S^1_nu] times [rhoutil])>. This proves the asserted sign and actual map, without identifying a fibre-first cup map with the base-first one.
'''

deriv['03IE']=r'''# Prereading derivation: wbII:lem:picard-finite-norm (03IE)

Fix one actual finite filling of order m, with invariant integral vector v. Pull back the clockwise meridian to its full root circle s(theta)=r exp(-2 pi i theta), 0<=theta<=1. Its linear monodromy is the identity, and the crossed-cocycle identity gives z(rho^m)=N_T d. The pullback of the line bundle extends over the smooth torus family over the root disc. Its real homology marking extends over that disc and its fibrewise Chern class is E.

The supplied logarithmic overlap map from cap coordinates to flat coordinates is

    zeta_flat = zeta_cap + (log s)/(2 pi i) Pi_s v.

This direction follows directly from equivariance: the clockwise deck generator changes log s/(2 pi i) by -1/m, cancelling the affine translation v/m in the cap action. It is not an arbitrary coordinate convention.

On the pulled-back flat zero section the cap coordinate is

    - (log s)/(2 pi i) Pi_s v
       = theta Pi_s v + i (log r)/(2 pi) Pi_s v.

The real period map Pi_{s,R}:Lambda_R -> C^2 is an isomorphism. In its real coordinates this path is theta v + k(theta), where

    k(theta)=Pi_{s,R}^{-1}( i (log r)/(2 pi) Pi_s v ).

The function k is periodic on the full root circle. In particular the imaginary constant multiplying Pi_s v has not been silently treated as a real multiple of v. The path has integral endpoint difference v. For every nu in Lambda its swept torus in the cap has representative u nu+theta v+k(theta). The explicit homotopy replacing k(theta) by k(0)+t(k(theta)-k(0)) preserves the periodic endpoints and proves its homology class is the product (nu,v). The cap-disc trivialization gives Chern pairing E(nu,v).

On the original flat sweep Omega_E has zero integral, because one tangent direction is horizontal and the other vertical. The base-first sign in the defect definition therefore gives

    <N_Td,nu> = -E(nu,v) = E(v,nu)

for every integral nu. Equality on the basis gives N_Td=i_v E as an equality in V_R. Projecting to coinvariants replaces each T^k d by d, giving m dbar=[i_vE]. The same norm is obtained from the positive-meridian matrix or its inverse by the finite reindexing k -> m-k, so this calculation respects the stated clockwise meridian.
'''

deriv['03ID']=r'''# Prereading derivation: wbII:lem:picard-cusp-defect (03ID)

Use the actual cusp toric chart t=z_0 z_1 z_2, x_1=z_1, x_2=z_2 supplied in the input. The holomorphic map in the second variable

    H:S^1 times Delta_r -> Y_epsilon,
    H(u,q)=(q exp(-2 pi i u),1,exp(2 pi i u))

is continuous on the whole solid torus, including q=0. Its base coordinate is t=q. On its boundary q=r exp(-2 pi i v), x_1=1 and x_2=exp(2 pi i u). These are exactly the flat zero-section lift of the clockwise cusp meridian swept by deltahat: the period column of deltahat is (0,1). Composing H with the actual cusp quotient map produces the required solid torus in N_0. Tautological cusp gluing has no additional vertical translation.

Every first Chern class pairs to zero on this boundary, because it extends over the solid torus. The constant vertical form has zero pairing on its flat boundary sweep, as one direction is horizontal. The base-first defect pairing therefore gives <d_0,deltahat>=0. The supplied integral computation identifies V_G with Z[delta], and evaluation on deltahat is the displayed coefficient map. Hence dbar_0=0.

For the second assertion use the actual inclusions i_W:W->N_0 and i_F:F->N_0. The proper local cusp tube comparison identifies the specialization map with restriction from the tube: sp^2 i_W^*=i_F^* on H^2(N_0,Z). This is also the natural map from the constant sheaf to nearby cycles; its equality on these maps follows from restricting the same cochain or line-bundle transition cocycle to the central and nearby fibres. The established Paper I cusp-tube retraction supplies an inverse to i_W^*, so this describes exactly the named specialization rather than a replacement isomorphism. Apply the equality to c_1(L). Naturality of the exponential-sequence connecting homomorphism gives i_W^*c_1(L)=c_1(L|W) and i_F^*c_1(L)=c_1(L|F), proving the formula. No global H^2(X) computation is involved.
'''

deriv['03IL']=r'''# Prereading derivation: wbII:prop:direct-boundary-picard (03IL)

The invariant-lattice input gives E=nq, n in Z, with exactly q=u wedge w+6 gamma wedge delta. There is no rescaling from q to 2q here. For v_1=(1,2,-4,0) and v_2=(-1,-3,3,0), direct contraction gives

    i_v1 q=4u+2w+6delta,
    i_v2 q=-3u-3w-6delta.

The supplied coinvariant map kills gamma,u,w and carries delta to its primitive generator. The actual finite norm identities with m_1=3 and m_2=4 consequently give

    dbar_1=2n[delta],    dbar_2=-(3n/2)[delta].

The cusp solid-torus calculation gives dbar_0=0. The based boundary relation gives their sum zero, hence (n/2)[delta]=0 in the real coinvariant line. Therefore n=0. This reasoning uses the actual finite covers and their logarithmic overlaps; it does not assume an unproved parity convention for an auxiliary finite-filling basis.

For the line bundle restricted to N_0, the local Chern compatibility gives sp^2(c_1(L|W))=c_1(L|F)=0. The supplied integral local specialization theorem is injective in degree two, so c_1(L|W)=0 integrally. Pull back along the exact normalization eta:dP6->W to obtain c_1(eta^*i^*L)=0. On dP6, H^1(O)=0 (the proved toric cohomology/GAGA input), and the exponential sequence makes Pic(dP6)->H^2(dP6,Z) injective. Thus eta^*i^*L is the trivial holomorphic line bundle. Both conclusions hold for the given arbitrary analytic L on X. Global Leray transgressions and the packaged H^2(X,Z)=0 statement were not used.
'''

deriv['03IN']=r'''# Prereading derivation: wbII:prop:local-cusp-picard-obstruction (03IN)

Set B=B_0, H=diag(1,-6), Q(v)=v^tHv. The toric fan is smooth with rays (v,1), v in Z^2. On each full cone the primitive ray generators form a Z-basis, so the three integer Q-values are the values of one integral character. This constructs the local Cartier equation for the prescribed divisor. The fan is locally finite, so each chart meets finitely many relevant divisors; the Cartier equations agree on overlaps up to a unit. This proves local finiteness and the Cartier assertion for D_Q.

The actual action Psi_lambda sends E_v to E_{v+B lambda}. Consequently

    Psi_lambda^*D_Q-D_Q=div(f_lambda),
    f_lambda=x^{2HB lambda} t^{Q(B lambda)}.

This is the exact character-divisor identity, because Q(v+B lambda)-Q(v)=2(HB lambda) dot v+Q(B lambda). Write

    C=[[6mu,h],[b-h,mu]],
    S=C^t HB=[[6(b-h),6mu],[6mu,h]].

The matrix S is symmetric. Define b_lambda=exp(2 pi i lambda^t S lambda), g_lambda=b_lambda f_lambda. Substituting the actual Psi action x -> exp(2 pi i C lambda)t^{B lambda}x gives

    f_lambda (f_mu o Psi_lambda)
       = f_{lambda+mu} exp(4 pi i lambda^t S mu).

Since b_{lambda+mu}/(b_lambda b_mu) is that same exponential, g_lambda(g_mu o Psi_lambda)=g_{lambda+mu}. Multiplication by g_lambda is the isomorphism Psi_lambda^*O(D_Q)->O(D_Q): its divisor is precisely the source divisor minus the target divisor. Thus the action on the actual bundle fibre from p to Psi_lambda(p) is multiplication by g_lambda(p)^{-1}. This inverse is necessary for the Chern-class sign. The equivariance cocycle and the given free properly discontinuous quotient descend the line bundle to N_0.

The coefficient of E_0 is Q(0)=0. Only the six adjacent E_ai meet E_0 as boundary curves. Restriction therefore gives O_E0(sum Q(ai) C_i). The values in the stated ray order are (1,-6,-5,1,-6,-5). The dP6 hexagon has C_i^2=-1 and C_i.C_{i+/-1}=1, all other distinct intersections zero. Its degrees are consequently (-12,2,0,-12,2,0), in particular nonzero.

On a nonzero fibre use additive coordinates x=exp(2 pi i zeta), t=exp(2 pi i s), and the ordered lattice [Z|I_2], Z=sB+C. The actual action factors are

    j_lambda(zeta)=exp[-2 pi i(2 zeta^t HB lambda+s Q(B lambda)+lambda^t S lambda)],
    j_m=1 for m in Z^2.

The logarithmic commutator for (lambda,m) is

    (log j_lambda(zeta+m)-log j_lambda(zeta))/(2 pi i)
       =-2 m^t HB lambda.

This is the first Chern alternating form obtained from the transition factors and the oriented fundamental square. The lambda-lambda part vanishes because Z^t HB=s B^t HB+S is symmetric; the m-m part is zero. In the basis (gammahat,uhat,what,deltahat), m^t HB lambda=lambda_2 m_1+6lambda_1 m_2=q(lambda,m). Thus the full alternating form is exactly -2q, with no unproved coordinate interchange or orientation replacement.
'''

deriv['03I6']=r'''# Prereading derivation: wbII:lem:analytic-support-specialization (03I6)

Let L=pi^*M. The following construction applies to an arbitrary analytic line bundle; it does not start by assuming L has a toric divisor or a torus action. Every full smooth-cone chart restricted to Y_epsilon is

    U_sigma={ (z_0,z_1,z_2) in C^3 : |z_0z_1z_2|<epsilon }.

It contracts by radial scaling. It is Stein directly from holomorphic convexity: for a compact K its O(U_sigma)-hull lies in the compact polynomial hull in C^3 and satisfies |z_0z_1z_2|<=max_K|z_0z_1z_2|<epsilon; hence it is compact inside U_sigma. Coordinates separate points and give local coordinates. Cartan Theorem B and the exponential sequence now give Pic(U_sigma)=0. The exact primary Theorem B statement is Cartan, Seminaire 1951-52, expose 18, printed p.18-7; its actual image confirms H^q=0 for q>=1.

Choose a holomorphic frame e_sigma on each such chart. All charts contain T=(C*)^2 times Delta*, so choose e_T as the restriction of one of these frames. Write e_T=f_sigma e_sigma on T. The three integral windings of f_sigma form n_sigma in M'=Z^3. Around a common divisor E_v, f_sigma/f_tau is the transition unit between two holomorphic nonvanishing frames and extends across that divisor. Its winding on the transverse meridian is zero. Hence

    phi(v)=<n_sigma,(v,1)>

is independent of the chart containing that ray. This is an actual integral support function derived from the analytic frames. Terms with zero winding have zero Chern class in the relevant exponential-sequence calculation; no global meromorphic representative of L has been assumed.

On E_v the same local frames and transverse meridians give the divisor-class coefficients phi(v+a_i)-phi(v) along its boundary hexagon. Its degree on the i-th curve is therefore

    d_i(v)=phi(v+a_{i-1})+phi(v+a_{i+1})-phi(v+a_i)-phi(v).

This follows by pairing with the hexagon intersection matrix, whose diagonal is -1 and adjacent entries are 1. Deck equivariance of the pullback L identifies E_v with E_{v+B_0 lambda}, preserving the labeled boundary directions. Since B_0 is unimodular, d_i(v) is constant in v. The common curve between adjacent components has the same line-bundle degree from either component, giving d_i=d_{i+3}. Denote the first three integers by d_1,d_2,d_3 and define

    Bform=[[d_2+d_3,d_3],[d_3,d_1+d_3]].

This is an integral symmetric form. The integer-valued polynomial

    Q_B(v)=B11*v1(v1-1)/2+B12*v1*v2+B22*v2(v2-1)/2

has exactly these six degrees. For psi=phi-Q_B all six degree equations vanish. The third gives Delta_1 Delta_2 psi=0; combining the second and first respectively with it gives Delta_1^2 psi=0 and Delta_2^2 psi=0. Applying these difference equations successively on the integral grid gives psi(v)=c+ell_1 v_1+ell_2 v_2 with integral constants. Thus phi(v+B_0 lambda)-phi(v) is affine in v with linear part Bform(B_0 lambda,v). The binomial polynomial treats odd diagonal coefficients integrally; no division by two of an arbitrary integer quadratic coefficient has been made.

It remains to identify the actual fibre Chern form. Write the deck action on e_T as e_T(p)->j_lambda(p)e_T(Psi_lambda p). If Psi_lambda maps U_sigma to U_tau, its action on the chosen local frames is a holomorphic unit b_{lambda,sigma} on the contractible chart. Its winding is zero. The exact frame equation gives

    j_lambda=b_{lambda,sigma} f_sigma/(f_tau o Psi_lambda).

Consequently the winding of j_lambda along a torus loop m is the negative linear part of the support-function difference, namely -Bform(B_0 lambda,m). Pulling e_T to the additive cover of F_t makes all integral m-translation factors equal to 1. The logarithmic commutator on the fundamental square for (lambda,m) is then exactly that winding. The exponential-sequence/argument-principle definition of c_1 therefore gives

    E_M((lambda,0),(0,m))=-Bform(B_0 lambda,m).

This proves the displayed map between the degree data and the actual Appell--Humbert form. For E_M=0, unimodularity of B_0 gives Bform=0, hence d_1=d_2=d_3=0. The toric boundary curves generate the curve lattice of E_0=dP6, and their intersection pairing detects every Chern class. Thus c_1(L|E_0)=0; H^1(E_0,O)=0 and the exponential sequence give L|E_0=O_E0. The identity L|E_0=nu^*(M|W) is restriction of the given maps. No integral nearby-cycle specialization is used.
'''

deriv['03IH']=r'''# Prereading derivation: wbII:prop:analytic-ah-boundary (03IH)

Take an open pants neighbourhood and its simply connected base cover U. In the period construction the additive fibre cover is U times C^2. It is Stein and contractible, so Cartan B and the exponential sequence trivialize the pullback of L holomorphically. The actual deck group is Lambda semidirect pi_1(P), with the zero-section splitting prescribed in the target. In a chosen frame let j_g be its nonvanishing holomorphic transition factors. Holomorphic logarithms exist on this simply connected additive cover.

The numbers

    c(g,h)=(log j_g(hx)+log j_h(x)-log j_{gh}(x))/(2 pi i)

are constant integers and satisfy the two-cocycle identity by associativity of the factors. On the lattice the alternating part is the fibre Chern form E, by the argument principle on a fundamental square. Transport of the restricted bundle proves invariance of E. The real two-cocycle

    c_E((lambda,g),(mu,h))=1/2 E(lambda,A_g mu)

is an explicit reference extension: invariance of E proves its cocycle identity, and its lattice alternating part is E. Integration of the constant vertical form over the affine triangle with sides lambda and A_g mu is exactly this half-E expression. Thus this reference records the flat vertical class, with zero mixed contribution in the zero-section marking.

Subtract c_E. The resulting real central extension restricts to an extension of Lambda with zero commutators. Choose lifts of its four basis vectors and define the lift of any lattice vector by their commuting integer powers; this is a splitting of that restricted extension. Choose lifts of the two free base generators and extend along reduced words; freeness gives a splitting over pi_1(P). In the resulting extension write

    ghat lambdahat ghat^{-1}=i(k_g(lambda)) (A_g lambda)hat.

The function k_g is additive. Conjugating twice gives k_{gh}(lambda)=k_h(lambda)+k_g(A_h lambda). Define d(g)(nu)=k_g(A_g^{-1}nu). It follows by substitution that d(gh)=d(g)+T_g d(h). Replacing the lattice splitting by its translate a(lambda) changes k_g(lambda) by a(lambda)-a(A_g lambda), hence d(g) by (T_g-I)a. Changes of frame or logarithms give an isomorphic central extension and the same class. This proves uniqueness of the class associated to this line bundle and this fixed flat reference; it does not claim that every arbitrary crossed homomorphism on the free group lies in one cohomology class.

The chosen base lifts multiply according to rho_1 rho_2 rho_0=1 without a vertical endpoint. Thus d_1+T_1d_2+T_1T_2d_0=0 and the barred sum is zero. The mixed commutator of the logarithmic factors on the rectangle formed by nu and the base loop is the first Chern integer on that rectangle after subtracting the reference vertical contribution. With the rectangle ordered (fibre,base), the base-first convention gives <d(rho),nu>=-<c_1(L)-[Omega_E],sweep(nu,rho)>. This sign follows directly by interchanging the two oriented edge parameters of the rectangle.

For a finite filling take the full clockwise root circle s=r exp(-2 pi i theta). The exact logarithmic overlap sends the flat zero section to cap real coordinates theta v+k(theta), with k(theta)=Pi_{s,R}^{-1}(i(log r)/(2 pi) Pi_s v) periodic. The homotopy k(theta)->k(0) proves that the swept cap torus has Chern pairing E(nu,v). The logarithmic commutator just computed is its negative, so <N_Td,nu>=E(v,nu) on every lattice vector, and N_Td=i_vE. Projection gives m dbar=[i_vE]. Inverse local loop conventions give the same finite norm by the explicit finite reindexing of its terms.

At the cusp the actual map (u,q)->(q exp(-2 pi i u),1,exp(2 pi i u)) in the chart t=z_0z_1z_2 is a solid torus whose boundary is exactly the deltahat sweep. The line bundle extends over that solid torus. Its exponential transition cocycle therefore has zero boundary Chern number, or equivalently its argument-principle commutator is zero. The flat vertical reference has zero boundary pairing. Hence <d_0,deltahat>=0; evaluation identifies the real coinvariant line with its delta coefficient, so dbar_0=0. All these identities have been obtained from holomorphic factors, their logarithmic cocycle, and actual filling maps. No global Leray transgression or local integral nearby-cycle theorem enters this derivation.
'''

deriv['03IW']=r'''# Prereading derivation: wbII:thm:analytic-all-picard (03IW)

Take an arbitrary holomorphic line bundle L on the given standard X. Its fibre Chern form E is invariant, so the exact integral invariant lattice gives E=nq with n in Z and q=u wedge w+6gamma wedge delta. The holomorphic-factor boundary construction gives a crossed class with barred boundary sum zero, finite norm identities, and zero cusp defect. Contracting with the actual v_1 and v_2 gives 6n[delta] and -6n[delta] in coinvariants. Division by the actual covering orders 3 and 4 yields dbar_1=2n[delta] and dbar_2=-(3n/2)[delta]. Therefore (n/2)[delta]=0 and n=0. This uses the explicit norm transports and does not replace q by a differently normalized generator.

Restrict the same L to the actual cusp neighbourhood N_0, obtaining M. The previous conclusion is E_M=0. The analytic support-function construction from holomorphic chart frames gives the integral symmetric form B with mixed pairing E_M((lambda,0),(0,m))=-B(B_0lambda,m). Since B_0 is unimodular this forces B=0, hence all three independent central degrees vanish. The boundary curves detect the integral first Chern class on dP6, and Pic^0(dP6)=0, so nu^*(M|W) is holomorphically trivial.

The map nu here is precisely the normalization eta followed by the inclusion of W in the cusp neighbourhood, while M is L restricted along the cusp-neighbourhood inclusion. Composition of these actual restriction maps is eta^*i^*. Thus r(L)=O_dP6 for every L, proving r is the zero homomorphism. The calculation uses only the holomorphic factors, finite logarithmic overlaps, explicit cusp solid torus, and analytic chart-frame support function. It does not use global integral Leray transgressions or local integral nearby-cycle specialization.
'''

now=datetime.datetime.now(datetime.timezone.utc).isoformat()
inputs=[R/'S6_SERIES_PUBLISH_II_boundary_construction_inputs.json',D/'S6_SERIES_PUBLISH_II_boundary_preproof_exact.py',D/'S6_SERIES_PUBLISH_II_boundary_preproof_exact.output.json',R/'primary_inputs/Cartan1952_exp18.pdf',R/'primary_inputs/Cartan1952_exp18_printed_7.png']
for tag,body in deriv.items():
 p=D/f'S6_SERIES_PUBLISH_II_{tag}_derivation.md'
 assert not p.exists(),p
 p.write_text(body+common+'\n## Bound inputs\n\n'+json.dumps([bind(q) for q in inputs],indent=2)+'\n')
receipt={'created_utc':now,'checker':'i_provenance_recovery','targets':list(deriv),
 'all_target_proofs_unopened_at_writing':True,'prior_Paper_I_exposure_disclosed':True,
 'actual_primary_view':{'url':'https://www.numdam.org/item/SHC_1951-1952__4__A18_0.pdf','printed_page':'18-7','pdf_page_1_based':8,'scope':'Complete page actually viewed; Theorem B has q>=1. This is a primary input reading, not a target-proof or manuscript-page reading.'},
 'inputs':[bind(q) for q in inputs],'derivations':[bind(D/f'S6_SERIES_PUBLISH_II_{t}_derivation.md') for t in deriv],
 'code_and_output_actually_read':True,'events_added':0,'canonical_mutations':0}
p=D/'S6_SERIES_PUBLISH_II_boundary_prereading_input_receipt.json';assert not p.exists();p.write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(bind(p)))
