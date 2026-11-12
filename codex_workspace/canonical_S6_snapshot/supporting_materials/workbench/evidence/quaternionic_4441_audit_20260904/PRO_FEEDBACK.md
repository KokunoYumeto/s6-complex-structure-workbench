# Feedback for the 4+4+4+1 / Yang–Mills Pro sessions

4 September 2026. This feedback concerns the two quaternionic/triality
packets, not the separate Erdős–Straus/Koide v3 packet. It reports a bounded
audit, not a certification of every theorem in either packet.

The complete proof supplement is `s6_quaternionic_4441_reconciliation.tex`
in the [canonical Overleaf](https://www.overleaf.com/read/rtmyqxyrzprn#fa24eb).
Its proof module is
`supporting_materials/workbench/research/quaternionic_4441_reconciliation.tex`.
The evidence directory contains unchanged supplied source files, their
hashes, and `verify_exact.py` with 26 passing exact checks.

## 1. The two Lorentz constructions agree as embedded spaces

Keep exactly

P = [[1,−1,0],[0,1,−1]], u = (1,1,1)ᵀ,
R = P*(PP*)⁻¹, X = (R,u), det X = 1.

For Θ(A,b) = A+B(b)j, with B(b)ᵢⱼ = εᵢⱼₖ b̄ₖ, direct multiplication gives

P B(b) Pᵀ = overline(u* b) [[0,1],[−1,0]],
X⁻¹ B(b) X⁻ᵀ = B(X* b).

Consequently {H: PHP* ∈ Herm₂(ℂ)} is exactly {Θ(A,b): u* b = 0}.
In X* b = (χ,ρ), ρ = u* b, and the two spinor conventions satisfy

w = −ε χ̄, χ = ε w̄, ε = [[0,1],[−1,0]].

Thus χ = −ψ_R in the quaternionic packet's w = ε overline(ψ_R) convention.
This is the identity of the ambient quaternionic matrix, so positivity,
the cubic and the embedded old complex space all agree. The proof includes
every positive fibre and the standard pair (S¹²,S⁸), with complement
S³ × ℝ⁹. The equal-diagonal triality slice remains a different slice.

## 2. Retain the nonunitary marking in the Jordan product

X*X = D = diag((PP*)⁻¹,3), not I.
The ordinary ambient Jordan product pulls back to

M ∘_D N = (MDN + NDM)/2.

For ψ=(1,0), φ=(0,j), the original embedded product's upper-left block is
(3/2)[[0,−j],[j,0]], not (1/2)[[0,−j],[j,0]].
The latter is the ordinary block-frame product. The closure conclusion
survives: the j and k witnesses supply both missing directions and generate
all Herm₃(ℍ). The proof now gives the coefficient for the actual marking.

## 3. Exact force in the omitted coordinate

Your full cubic is confirmed:

N₁₅ = λ det G − z*adj(G)z − χ*Gχ − 2 Re(ρ χ*z) − λ|ρ|².

At ρ=0 its normal covector is −2 Re(δρ χ*z). The positive-definite witness
G=I₂, z=χ=(1,0), λ=3, ρ=t gives N₁₅(t)=1−2t−3t².

More concretely, retain your actual scalar kinetic terms and potential:

L = tr(Φ̇²)/2 + ḃ*ḃ − V,
s = tr Φ² + 2b*b,
V = m²s/2 + Γs²/4 − κ(det Φ − b*Φb), tr Φ=0.

Then

b̈ = −[(m²+Γs)I₃ + κΦ]b,
ρ̈ = −(m²+Γs)ρ − κu*Φb.

With Φ=diag(1,−1,0), b=(1,−1,0), and both velocities zero,
ρ=ρ̇=0 but ρ̈=−2κ. This is spatially constant scalar mechanics with gauge
fields omitted, not a claim about every gauge-field configuration.

Your remark already distinguishes the symmetry reduction from full
dynamical closure. The calculation above makes that distinction exact;
“consistent symmetry reduction” must not be read as an automatically
consistent unconstrained dynamical truncation.

There is also a precise alternative. Restrict the variational problem to
b∈u⊥ and let Π_u=uu*/3, Q_u=I−Π_u. It gives

b̈ = −(m²+Γs)b − κQ_u Φb,
Φ̈ = −(m²+Γs)Φ + κ(adj Φ − bb*)₀,

where T₀=T−tr(T)I/3. Relative to the full model, the reaction force is
κΠ_u Φb. It vanishes exactly when the constrained solution is also a full
solution. This preserves a rigorous constrained model while keeping its
difference from the unrestricted model explicit.

## 4. Two action-convention repairs

- For the usual direct-product **left** action use (g,k): Z ↦ gZk⁻¹.
  The printed gZk is a commuting left/right action, or a left action of
  SL₂(ℂ) × SU(2)ᵒᵖ. The orbit set and central kernel {±(I,I)} are unchanged.
- With A_μ∈su(3) anti-Hermitian, D=∂+A, and signature (+−−−), the
  positive gauge density is +tr(F_μν F^μν)/(2g_c²). The printed minus sign
  gives negative electric kinetic energy with those conventions.
  F₀₁=diag(i,−i,0) gives tr(F_μν F^μν)=4, so the sign is directly testable.
  The scalar potential and its force calculation are unchanged.

## 5. Exact continuation already completed: invariant motions

Keep the full equations above, with a=m²+Γs. For every fixed complex
W⊂u⊥ of dimension r=1 or 2, the space

    T_W = {(Phi,b): Phi=Phi*, tr(Phi)=0, Phi W⊂W, b∈W}

with tangent velocities is globally invariant. Its configuration dimension
is r²+(3−r)²−1+2r, namely 6 or 8. Hermiticity makes Phi block diagonal
on W⊕W⊥. The adjugate is Phi²−tr(Phi²)I/2, and bb* preserves both
blocks, so the full acceleration is tangent. Uniqueness proves invariance;
the conserved energy and quartic coercivity prove global existence.
The reaction κ(uu*/3)Phi b vanishes identically. These are interacting
solutions of the original system, not solutions of a replacement model.

The line case need not set the marked cross-coordinate z to zero. Retain
v=(1,−1,0), w₀=(1,1,−2), E=vv*/2, F=w₀w₀*/6 and take

    Phi₀=E−F+w₀u*+uw₀*, b₀=v, both velocities zero.

Then Phi₀v=v, s₀=42, b₀*Phi₀b₀=2, chi₀=(1,0), z₀=(0,3), lambda₀=0.
The exact initial acceleration is −(m²+42Γ+κ)v. The original nonunitary
marking and the factors 2, 3 and 6 are unchanged.

For c=u*Phi b and h=u*dot(Phi)dot(b), the next tangency identity is

    c'' = −2a c − (κs/3)rho + 2h.

In particular, rho=rho'=c=c'=0 gives rho''''=−2κh, not automatic zero.
With Phi₀=0, b₀=v, dot(b)₀=w₀, dot(Phi)₀=(uw₀*+w₀u*)/3,
all rho derivatives through order three vanish but rho''''(0)=−12κ.
The solution leaves as rho(t)=−(κ/2)t⁴+o(t⁴).
The added proof and 20 exact checks are in the same canonical supplement.

## 6. The fixed-W classification is false: exact periodic continuation

For m²=Γ=1 and κ=6, take

    b₀=(1,−1,0)/4,
    Phi₀=[[1,1,1],[1,1,1],[1,1,−2]]/4,
    J₀=[[0,−1,1],[1,0,−1],[−1,1,0]],
    Π=uu*/3, Q=I−Π,
    Ω=√(2/3) J₀,
    O(t)=Π+cos(√2 t)Q+sin(√2 t)J₀/√3.

Then b(t)=O(t)b₀ and Phi(t)=O(t)Phi₀O(t)* solve both FULL scalar
equations for every real t. They have s=1, Phi b=0, and rho=0.
At times 0 and π/(2√2), b spans u-perp; nevertheless Phi₀ does not
preserve u-perp. Hence no fixed W works. The instantaneous kernel line
moves, although span{b(t),dot(b)(t)} is the fixed plane u-perp.
This corrects the overly specific moving-plane suggestion in the preceding
handoff: a moving kernel already refutes the proposed fixed-W classification.

This is a family, not an isolated numerical orbit. For Gamma>0, kappa≠0,
choose 0<x/kappa≤1/(6Gamma), a>kappa*x/3, and B,d>0 with
B²+d²=3ax/kappa−x². Set m²=a(1−6Gamma*x/kappa). In the exact frame
K=(v/√2,w₀/√6,u/√3), where v=(1,−1,0), w₀=(1,1,−2), retain

    K*Phi₀K = [[0,0,0],[0,−x,d],[0,d,x]], K*b₀=B e₁.

Rotation about u with frequency √a gives a solution with s=6ax/kappa.
The full original-coordinate formulas and inverse frame are in the draft.

The conserved anti-Hermitian moment is

    J=[Phi,dot(Phi)]+b dot(b)*−dot(b)b* = −(s/2)Ω.

For the concrete orbit it is −Ω/2≠0; kinetic energy is 1, potential 3/4,
total energy 7/4. Thus setting every gauge connection to zero does not
give a source-free gauge solution: variation of A₀ requires the trace-free
part of J to vanish. Gauge transformation U=O* makes the scalar coordinates
static but produces A₀'=Ω and retains the nonzero charge. This is an exact
comparison with the gauged equations, not a claim of no possible gauge lift.

## 7. Scalar vacuum and full Hessian independently verified

For Q=Theta(Phi,b), retain g(Y,Y)=tr(Y²), s=tr(Q²) and n=MooreDet(Q).
The exact discriminant identity is

    s³−54n²=2(λ₁−λ₂)²(λ₁−λ₃)²(λ₂−λ₃)².

Equality away from zero is Q=x(3P−I), P a quaternionic rank-one projector.
All stated global minima are correct, including coexistence at
m²=κ²/(27Γ), and the broken-phase x formula. The full Hessian—not only
its radial restriction—has eigenvalues x(12Γx−κ), 0, 3κx with
multiplicities 1,8,5. Its zero block is precisely tangent to HP².
At the origin the fourteen metric eigenvalues are m². The audit includes
the full cubic expansion in all fourteen variation coordinates and the
kinetic weights 6,2,...,2. This confirms your scalar theorem; it does not
yet certify the gauge-orbit classification or the finite-lattice theorem.

## 8. One bounded next calculation in the genuinely complex gauge class

The complete field equations are already derived. Temporal gauge, zero
spatial connection, all real-skew connections with arbitrary time dependence,
and constant complex spatial connections in the constant-matter frame are
settled negatively; their specified matter-stabilizer gauge saturations are
also excluded. Do not repeat those cases as the next result.

For the same literal orbit at `(m²,Gamma,kappa)=(1,1,6)`, retain
`H=[[0,0,0],[0,-1/2,1/(2sqrt(2))],[0,1/(2sqrt(2)),1/2]]`,
`q=e1/(2sqrt(2))`, `A=sqrt(2)[[0,-1,0],[1,0,0],[0,0,0]]`,
and the unchanged original `K,O,Omega`. Keep `g²>0` symbolic.
Solve the following finite, genuinely complex spatial-rotation class:
constant `C,Z1,Z2` in the full `su(3)`, real `omega!=0`,

    Y1(t)=cos(omega t)Z1−sin(omega t)Z2,
    Y2(t)=sin(omega t)Z1+cos(omega t)Z2, Y3=0.

With `I Z=([H,[H,Z]]+qq*Z+Zqq*)_tf`,
`K_Z Z=−[Z1,[Z1,Z]]−[Z2,[Z2,Z]]`, and `F_H=[A,[A,H]]`,
the exact finite system to solve is

    [C,[C,H]]−[Z1,[Z1,H]]−[Z2,[Z2,H]]=F_H,
    (C²−Z1²−Z2²)q=−2q,
    (I+2K_Z/g²)C=(4omega/g²)[Z1,Z2],
    −omega²Z1−2omega[C,Z2]+[C,[C,Z1]]+K_Z Z1+(g²/2)I Z1=0,
    −omega²Z2+2omega[C,Z1]+[C,[C,Z2]]+K_Z Z2+(g²/2)I Z2=0.

These equations include Gauss with its nonzero electric contribution and
both nontrivial spatial equations; the third spatial equation is identically
zero for this ansatz. Obtain one exact solution with its allowed coupling
and frequency relation, or prove exclusion of this entire finite class.
Verify any solution in every original field equation after the exact inverse
map `A0=OKCK*O*−Omega`, `Ai=OKYiK*O*`. Do not reset the scalar time
scale or replace the force by a constraint. Use bounded exact small-matrix
calculation; an unresolved remainder must be reported as unresolved, not as
a general no-lift theorem. The problem outside this class remains distinct.

## 9. What the dimension experiments now suggest

The 9=4+4+1 complex carrier and 13=4+4+4+1 common slice are embedded
in the full 15=6+4+4+1 quaternionic carrier. The 13-slice generates the
full 15-dimensional Jordan algebra with the original marking retained.
Keep that full carrier and use an observation instead of assuming a
smaller slice is dynamically invariant. The following map is proved:

    O(H)=pi_C(P H P*), pi_C(A)=(A−i A i)/2,
    P=[[1,−1,0],[0,1,−1]], C=P P*=[[2,−1],[−1,2]], R=P* C^-1.

This map is positive, onto Herm2(C), has positive section G→R G R*,
and has real kernel dimension 11. Write H=Theta(A,b) and rho=u*b.
The full compressed quaternionic block is G+bar(rho)epsilon*j and its
Moore determinant is det(G)−|rho|². The complete permitted-pair image is

    G>=0, |rho|²<=det(G).

Every such pair lifts: A=R G R*+lambda u u*, b=(rho/3)u, lambda>=0.
Thus a null Lorentz block forces rho=0; a timelike block admits exactly
the disk |rho|<=sqrt(det G). In coordinates

    G=[[p0+p3,p1−i p2],[p1+i p2,p0−p3]],
    det(G)=p0²−p1²−p2²−p3².

There is no uniform positive threshold in this positive cone: G=e I2,
rho=e/2, lambda=e gives positive definite lifts for every e>0 and
det(G)=e²→0. This is not a quantum Hamiltonian spectral statement.

Important exact domain correction: a tracefree positive Hermitian matrix
is zero. The scalar Q=Theta(Phi,b) therefore cannot itself be a nonzero
positive configuration. Its positive-boundary representative is instead

    F(Q)=Q−lambda_min(Q)I3,
    Ghat(Q)=P Phi P*−lambda_min(Q) C.

F has exact inverse H→H−tr(H)I3/3 on the positive singular boundary,
leaves rho unchanged, and yields det(Ghat)>=|rho|². It retains C, not I2.
This map is continuous but need not be differentiable at repeated least
eigenvalues. It is not an assumed kinetic/Hamiltonian intertwiner.

The completed local geometric bridge retains the rank-six integral toroidal
period data, rather than identifying a Gram-cone boundary with the completed
Fable threefold by sphere dimension. Its exact Hermitian metric and spectral
content is recorded in Section 16 below. Global transition and dynamical
selection questions remain outside that local theorem.

There is now an explicit metric-dependent period-to-Gram bridge. Retain
Z3=s I3+C3(t), Z2=s B0+C2(t), P Z3=Z2 Q_latt and Phi=P⊕Q_latt.
With Omega3=(I3,Z3), Omega2=(I2,Z2), every positive real W3 gives

    P(Omega3 W3 Omega3*)P*=Omega2(Phi W3 Phi^T)Omega2*.

A constant positive W3 cannot descend through the cusp's unipotent
monodromy. For M(x)=[[I3,xI3],[0,I3]], x=Re(s), every fixed W_*>0
gives an explicit equivariant W3(s)=M(−x)W_*M(−x)^T. The descended
Gram matrix is (I3,iyI3+C3)W_*(I3,iyI3+C3)*, y=Im(s).
Its observed determinant has leading coefficient det(P K P*)>0 times
y^4, where K is W_*'s lower3×3 principal block. With the explicit choice
W_*=I6 it is 3y^4+O(y^3), retaining the exact lower terms in the proof.
Thus this family has full-rank timelike cusp growth, not rank loss.
This gives an actual bridge and a precise result for it, not a geometric
identification of the Gram boundary with the original global threefold.

## 10. Completed gauge continuation: use these equations, not only a constraint

Retain anti-Hermitian A_mu, signature (+---), the corrected positive
electric kinetic sign, and g²>0. Put
E_i=dot(A_i)+[A_0,A_i], X=dot(Phi)+[A_0,Phi],
v=dot(b)+A_0 b, a=m²+Gamma s. The complete homogeneous equations are

    D_0 X − Σ_i[A_i,[A_i,Phi]] + a Phi − kappa(adj Phi−bb*)_tf = 0,
    D_0 v − Σ_i A_i² b + (a I+kappa Phi)b = 0,
    (2/g²)Σ_i[A_i,E_i] − (J_0)_tf = 0,
    D_0 E_i − Σ_j[A_j,[A_j,A_i]] − (g²/2)(J_i)_tf = 0,

    J_0=[Phi,X]+b v*−v b*,
    J_i=[Phi,[A_i,Phi]]−bb*A_i−A_i bb*.

For the exact rotating orbit with r²=x²+d², temporal-gauge scalar
compatibility forces each A_i=i c_i(t) Phi. This is its full Lie
stabilizer: Phi has simple eigenvalues 0,+r,−r and b spans its kernel.
Gauss' residual is exactly

    [(2r²/g²)Σ_i c_i²+r²+B²] Ω ≠ 0.

Thus NO homogeneous temporal-gauge lift retains this literal scalar orbit.
There is also no lift with all spatial A_i=0 and arbitrary A_0:
Gauss forces D_0 Phi=D_0 b=0, contradicting a b≠0.

Do not extend that stabilizer deduction to arbitrary A_0. For
alpha²−Σ_i beta_i²=1, the exact flat connection

    A_0=(alpha−1)Ω, A_i=beta_i Ω

preserves BOTH original scalar equations while its spatial fields need
not stabilize the scalars. It still fails Gauss: J_0=alpha J_scalar≠0.
For general positions and velocities Gauss has the exact inertia form

    (I_m + 2K_A/g²) A_0 = (J_scalar)_tf − (2/g²)Σ_i[A_i,dot(A_i)],
    I_m Z=([Phi,[Phi,Z]]+{bb*,Z})_tf,
    K_A Z=−Σ_i[A_i,[A_i,Z]].

The operator is positive semidefinite for −tr(ZW). Its quadratic form is

    tr[Z,Phi]²+2||Zb||²+(2/g²)Σ_i||[A_i,Z]||².

Its kernel is the common stabilizer; the right side annihilates that
kernel. This proves pointwise A_0 solvability, not a smooth selection
through rank changes and not the other equations. Section 13 records the
additional all-time and complex static-frame exclusions; the single bounded
remaining calculation in Section 8 enforces all full equations.

There is also a constructive interacting full-gauge sector, distinct
from that rotating orbit:

    Phi=x(t)diag(−2,1,1), b=beta(t)e_1, A_mu=0,
    x''=−a x−kappa x²+kappa beta²/3,
    beta''=−(a−2kappa x)beta,
    a=m²+Gamma(6x²+2beta²).

All currents vanish identically, so these are complete gauge solutions.
The exact conserved density is 3x'²+beta'²+V, and quartic coercivity
proves global existence for every real initial datum. They have finite
total energy on any specified finite-volume flat T³, not on all of R³
when the constant density is nonzero.

## 11. An invariant observation, and what the vacuum calculation confirms

At (m²,Gamma,kappa)=(1,1,6), x₀=(3+sqrt(3))/12, beta=3x₀ is a global
scalar minimum and full-gauge equilibrium. Q=Theta(Phi,b) has eigenvalues
(4x₀,−2x₀,−2x₀). The positive spectral-floor H=Q+2x₀I has rank one,

    G=3x₀[[1,−1],[−1,2]], rho=3x₀, det G=9x₀².

On the SAME SU(3) orbit, write e=g e_1:

    Phi=x₀(I−3ee*), b=3x₀e,
    G=3x₀P(I−ee*)P*, det G=9x₀²|u*e|²=|rho|².

This ranges from timelike to null. Fixed-P det G is not a gauge-invariant
mass. The exact covariance is (H,P)→(gHg*,Pg*), which keeps PHP* unchanged.

A nontrivial invariant bridge is nevertheless explicit. For every
Hermitian complex A and Haar measure with total mass V_mu retained,

    det(PAP*)=u*adj(A)u,
    ∫_SU(3) det(PgAg*P*) dmu = V_mu tr adj(A).

For positive quaternionic rank-one H=Theta(A,b), adj A=bb* exactly.
Thus the averaged Lorentz determinant is V_mu||b||². This is the
bridge to the invariant in your vacuum calculation, not a dismissal
of the marked observation.

Keep chi=2x₀ and v_theta=(cos theta,sin theta*j,0), 0≤theta≤pi/4.
The minima Q_theta=chi(3v_theta v_theta*−I) have

    b_theta=(0,0,−3chi cos theta sin theta),
    ||b_theta||²=(9chi²/4)sin²(2theta).

They are gauge inequivalent for distinct theta and have identical
potential energy. The coefficient validates your existing invariant
formula; the classical HP²/SU(3) orbit geometry is not new (Gambioli,
arXiv:math/0611796). The new comparison is its exact relation to the
Lorentz observation. Do not infer a quantum spectral gap or its absence
solely from this classical minimum family.

## 12. Complete period cometric fibres; rank loss constructed

The unchanged cusp periods are Z3=sI+C3(t), s=x+iy, t=exp(2pi i s).
Retain C3=S C2 Q_latt. Let

    N=[[I,xI+Re C3],[0,yI+Im C3]], Omega3=(I,iI)N.

On y>||C3||_bound this has the exact block inverse in the draft.
For H=E+iF>0 all real positive lattice cometrics/weights W with Omega3 W Omega3*=H are

    W=N^-1 { 1/2[[E,−F],[F,E]] + [[U,V],[V,−U]] } N^-T,

where U,V are real symmetric and the bracket is positive. This is the
full 12-dimensional positive fibre. For fixed G=P H P*>0 all H are

    H=X[[G,z],[z*,z*G^-1 z+tau]]X*, z∈C², tau>0,

so the observed positive W fibre is 17-dimensional. Periodic choices
give the exact inverse-congruence cometric monodromy. The covariant lattice
metric is W^-1, not W. No period correction
has been removed; C2=P C3 S B0 recovers it.

In particular every smooth positive G(t) has a lift. Keep arbitrary
alpha_obs,beta_obs,lambda,p>0 and choose

    G=diag(alpha_obs,beta_obs y^-p), H=R G R*+lambda uu*,

then choose U=V=0 above. The observation approaches a nonzero null block.
For W_*=M(x)W M(x)^T, its exact determinant is

    det W_* = alpha_obs² lambda² beta_obs² y^(-2p) /
              [64 det(yI+Im C3)²],
    det(yI+Im C3)
       = y[y²+y tr(Im(C2) B0^-1)+det Im(C2)].

Its condition number has the explicit asymptotic

    kappa(W_*) ~ 2 max(2alpha_obs/3,3lambda) y^(p+2) / beta_obs.

Conversely, with ||C3||≤K, bounded relative condition number cannot
produce projective rank loss, meaning a vanishing observed eigenvalue ratio:

    lambda_min(G)/lambda_max(G)
      ≥ [1+(y−K)²] / {3 kappa(W_*) [1+(y+K)²]}.

The same periods also allow W_*=I, with det G=3y⁴+O(y³).
Do distinguish collapse of the entire matrix to zero: W_*=y^(-3)I
has condition number one and G=y^(-1)C+O(y^(-2))→0, but its eigenvalue
ratio tends to 1/3, so it does not contradict the projective statement.
Thus the periods and positivity support both behaviours but select neither.
The Hermitian interpretation and native metric are now determined exactly
in Section 16. A global metric-selection or dynamics law compatible with
the actual transitions remains open; an arbitrarily chosen rank-losing
cometric is not thereby a derived physical vacuum or interacting spectrum.

## 13. New complete exclusions for the literal moving-kernel orbit

The canonical `q444:static-lift-system` gives the invertible maps

    C=K*O*A0OK+A, Yi=K*O*AiOK,
    A0=OKCK*O*−Omega, Ai=OKYiK*O*.

Matter is exactly the fixed pair `(H,q)`. Both scalar equations, Gauss,
and all three spatial equations are proved equivalent, with the original
couplings and time scale retained.

For arbitrary real-skew fields write `C=L(c)`, `Yi=L(yi)` with
`L(c)z=c cross z`. Both scalar equations force `dot(c)=0` and

    Q=cc^T−Σ_i yi yi^T=[[0,0,0],[0,d tau/x,tau],[0,tau,a−d tau/x]].

Thus `Qe1=0`, `tr Q=a>0`. Positivity of `Σ yi yi^T` forces `c1=0`:
if `c1!=0`, its Schur complement is minus the lower block of `Q`,
which would make that block negative semidefinite despite its positive
trace. Then `Q11=−Σ yi1²=0` gives every `yi1=0`. Consequently
`Σ yi cross dot(yi)` is perpendicular to `c`, while the exact Gauss
pairing, using `−tr(L(c)L(c))=2|c|²`, is

    2(r²+B²)|c|²+(4/g²)Σ_i|yi cross c|²=0.

It forces `c=0`, contradicting `tr Q=a>0`. This is an all-time
obstruction for arbitrary real spatial functions, including multifrequency
functions, not merely a stationary or temporal-gauge ansatz
(`q444:real-no-lift`).

For constant `Yi` with arbitrary complex `C(t)`, Gauss positivity instead
forces `Cq=0`, `[C,H]=[C,Yi]=0`. The vector equation then gives
`Σ_i||Yi q||²+aB²=0`, impossible (`q444:static-complex-no-lift`).
The exact transformations `S=exp(i theta H)` retain `H,q` and exclude
the gauge saturations of both classes (`q444:real-stabilizer-no-lift`).
These theorems do not exclude every genuinely complex time-dependent lift.

## 14. Full current-free periodic motion and exact null waves

The minimum section has tangent squared norm `18chi²`, kinetic density
`9chi² dot(theta)²`, and acceleration squared norm `72chi²` normal to
the entire minimum manifold. A homogeneous unconstrained solution confined
to that curve is constant; even varying only its common amplitude does not
supply the missing normal motion (`q444:vk-horizontal`, `q444:vk-polar`).

The new independent full-field sector is

    Phi=diag(h+k,h−k,−2h), b=beta e3, A_mu=0,
    Box h=−a h−kappa h²+(kappa/3)(k²+beta²),
    Box k=−(a−2kappa h)k, Box beta=−(a−2kappa h)beta,
    a=m²+Gamma(6h²+2k²+2beta²).

Every current vanishes for every spacetime derivative, so these equations
solve the complete gauge model, not only a scalar truncation. All homogeneous
initial conditions extend globally (`q444:vk-sector`). For
`0<m²<kappa²/(27Gamma)` and positive `kappa,Gamma`, define

    h0=(kappa+sqrt(kappa²−24Gamma m²))/(24Gamma),
    h0<h<kappa/(6Gamma), Delta=1−6Gamma h/kappa,
    a=(m²+12Gamma h²)/Delta,
    R²=3ah/kappa+3h², omega²=a−2kappa h.

Then constant `h`, `k=R cos(omega t)`, `beta=R sin(omega t)` are exact
nonconstant full-gauge solutions. The invariant `||b||²=R²sin²(omega t)`
is nonconstant. As `h` decreases to `h0`, `R` tends to `3h0`, `omega`
tends to zero, and the conserved density satisfies
`E−V0=9h0²omega²+O(omega⁴)`. The total excess on retained volume `V3`
is `V3(E−V0)` (`q444:vk-periodic`, `q444:vk-excess`). These finite-amplitude
motions approach a manifold of minima, not one small harmonic oscillation.

There are also exact nonlinear waves on that minimum section:
`theta=f(t−x1)`, `(Phi,b)=q_theta`, `A_mu=0`, for every smooth real `f`.
The chain rule gives `Box q_theta=T Box theta+N(partial theta)²=0`
and all currents vanish. On a rectangular torus choose `f` to be
`L1`-periodic; the exact excess is
`18chi² L2 L3 integral_0^L1(f')² du` (`q444:vk-wave`). The horizontal
linearized tangent obeys `Box eta=0` with its original kinetic coefficient.
No claim of a quantum gap or its absence follows from these classical solutions.

## 15. A conserved invariant current detects a proved classical mass branch

For `q=cos(2theta)`, the full gauge-inertia eigenvalues at the retained
nonzero minimum are

    0 (once), 3chi²(1−q²) (once), 9chi²q² (twice),
    (9/2)chi²(1+q) (twice), (9/2)chi²(1−q) (twice).

The generator kinetic Gram weights remain `2,2,2,2,2,2,2,6`.
Actual transverse solutions of all linearized equations, including Gauss,
have squared masses `g²/2` times these eigenvalues (`q444:gauge-spectrum`).

The exact full nonlinear current

    j_nu=−i(b*D_nu b−(D_nu b)*b), div j=0

is real and gauge invariant. On the transverse
`i diag(1,1,−2)` branch its linear coefficient is `−4||b||²`, and

    mu_d²=(2g²/3)||b||²
          =(2g²/(3V_mu)) integral_SU3 det(PgA_theta g*P*) dmu.

All marking and Haar-volume factors are retained (`q444:current-mass`).
This supplies a precise invariant observable-to-mass relation in this
specified adjoint-plus-fundamental model. At `b=0` the current's linear
coefficient vanishes. A zero transverse branch exists throughout; the
strictly positive branches alone have no positive lower bound uniform over
the minimum family (`q444:massive-branch-bound`). These are classical
linearized statements, not a pure interacting quantum Yang–Mills spectrum.

## 16. The exact Hermitian metric and original-lattice spectrum

For the unchanged period matrix `Omega3=(I,iI)N`, write the physical
cometric as `T`. Then

    W=N^-1 T N^-T=(g_latt)^-1,
    H=(I,iI)T(I,iI)*.

The full fibre in Section 12 is Hermitian-compatible exactly when `U=V=0`.
With the convention `g_phys(v,w)=Re(v*h3 w)`, this gives

    h3=2H^-1, T=realification(H)/2,
    g_latt=2N^T realification(H^-1)N.

Thus `W` is a lattice cometric/weight, not a covariant metric
(`q444:hermitian-cometric`). The complete marked eigenbasis is
`exp(2pi i k^T xi)`, `k in Z6`, with
`lambda_k=4pi² k^T W k`. Polarization of these eigenvalues recovers every
entry of `W` (`q444:torus-laplace`). No lattice is replaced.

The original torus homomorphism `[z]->[Pz]` has connected kernel
`C u/(Z u+s Z u)`. It is a Riemannian submersion for
`h2=2(PHP*)^-1`, with horizontal lift `H P*(PHP*)^-1`.
Target characters pull back by `L^T`, preserving their eigenvalues;
they are exactly source characters constant on the kernel, not all source
modes (`q444:metric-submersion`).

In particular native Euclidean `h3=I` gives `H=2I`, `G=2PP*`,
`h2=(PP*)^-1`. With `A=xI+Re C3`, `Y=yI+Im C3`, the exact source
eigenvalues are

    lambda_(m,n)=4pi²(|m|²+|Y^-T(n−A^T m)|²), m,n in Z3.

For `y>K+1`, the source first positive gap lies between
`4pi²/(y+K)²` and `4pi²/(y−K)²`. The quotient gap has the same bounds
with `8pi²`, because its nonzero integer indices have zero coordinate sum
and smallest squared length two. Thus the two gaps are asymptotic to
`4pi²/y²` and `8pi²/y²`, or `16pi⁴/(log|t|)²` and
`32pi⁴/(log|t|)²`, with every correction and original scale retained
(`q444:native-period-spectrum`). Constant observed `H` therefore coexists
with an expanding original lattice and shrinking dual spectral gap. These
are exact geometric spectra, not a chosen global dynamical metric or a
field-theoretic mass.

## 17. Full homogeneous quantization: a positive finite-model gap

Use the new standalone draft s6_homogeneous_quantum_confinement.tex in
the same canonical Overleaf, or its complete TeX in the current AI bundle.
The full proof module is
supporting_materials/workbench/research/homogeneous_quantum_confinement.tex.

Keep all 38 real coordinates, not just the vacuum curve:
A_i in su(3), Phi in Herm3(C)_0, b in C3.
The retained scalar metric is tr(dPhi^2)+2 db*db and gauge metric is -tr.
For positive hbar, g^2, V3, Gamma, with m^2>=0 and real kappa,

H = (hbar^2 g^2/(4 V3)) T_A + (hbar^2/(2 V3)) T_E + V3 U,

U = g^-2 sum_(i<j)||[A_i,A_j]||^2
  + (1/2) sum_i tr[A_i,Phi]^2 + sum_i ||A_i b||^2
  + m^2 s/2 + Gamma s^2/4 - kappa(det Phi-b*Phi b),

s = tr Phi^2 + 2b*b.

The exact root trace is
tr_su3 sqrt(-ad_X^2)=4(lambda_max(-iX)-lambda_min(-iX))
>=2 sqrt(6)||X||, including repeated eigenvalues.
Six directed oscillator slices, retaining a fraction eta of gauge
kinetic energy, give for every 0<eta<1

H >= eta hbar^2 g^2 T_A/(4V3) + hbar^2 T_E/(2V3)
   + hbar sqrt(6(1-eta)) sum_i||A_i||
   + V3 Gamma s^2/8 - V3 kappa^4/(54 Gamma^3).

This is a form inequality, not a substituted classical potential.
A direct finite-cell plus tail estimate proves compact resolvent
on all 38 coordinates. We derive all Gauss generators and their domains;
constant-SU3 averaging gives the exact physical subspace. The
strictly positive Brownian-bridge kernel proves a unique invariant
ground state. Thus E1_phys-E0>0 for this finite homogeneous mechanics.
No numerical value or uniform volume limit is proved. The bosonic
commutator-matrix discreteness mechanism is classical (Simon 1983),
not a new claim about pure Yang-Mills.

The classical homogeneous embedding into torus fields is exact,
but not an automatic invariant quantum subsector. For the retained
Fourier pair Phi=(q+y cos(2pi x1/L1))diag(1,-1,0)/sqrt2, the quartic
potential is Gamma V3(q^4+3q^2 y^2+3y^4/8)/4. The nonzero mixed
coefficient makes an all-q-wavefunctions tensor fixed-Omega(y)
subspace non-reducing: it would force y^2 Omega=lambda Omega,
impossible for nonzero L2 Omega. The complete operator-domain
argument is included. This obstruction is specific to that map;
it is not a statement that no quantum correspondence can exist.

### Bounded next task for the Yang-Mills / quaternionic session

Take that exact two-coordinate Fourier model, with kinetic masses
V3 and V3/2, and retain its mass, gradient, and quartic terms.
Derive the q-dependent lowest y-state and its induced Berry/Born-Huang
terms with a rigorous controlled error estimate for an explicitly
specified parameter regime. Do not tensor with a fixed y-vacuum,
discard q^2 y^2, set a coupling or volume to one, or identify the
result with a continuum gap. The target is an actual map and
error-controlled Hamiltonian comparison beyond the product obstruction.
Keep the earlier genuinely complex rotating-gauge question separate.

## 18. Exact complex rotating-pair continuation

The full proofs are now in the existing quaternionic draft, labels
q444:cx:thm:block, q444:complex-exact-zero-set,
q444:complex-full-scalar-equivalence,
q444:complex-stabilizer-spacelike and q444:complex-stress-obstruction.
This updates Section 8; that unrestricted question remains OPEN.

Keep the original matrices
H=[[0,0,0],[0,-1/2,1/(2sqrt2)],[0,1/(2sqrt2),1/2]],
q=(1,0,0)^T/(2sqrt2),
A=sqrt2[[0,-1,0],[1,0,0],[0,0,0]],
F=[A,[A,H]], g²>0, and omega !=0. Set

I(X)=([H,[H,X]]+q q* X+X q q*)tf,
K(X)=-sum_j[Zj,[Zj,X]],
L=g² I+2K, B=[Z1,Z2].

A genuinely complex class C,Z1 in the cross block of the fixed q-line
and Z2 preserving that line has been excluded, including its constant
SO2 spatial saturation. Neither an arbitrary C nor an arbitrary pair
is assumed to admit that block description.

For unrestricted Z1,Z2 in su(3), B!=0 implies L positive definite.
Every possible solution has B!=0 and Tq!=0, where

T=4 L^-1 B,
tau=(1/4+||Z1 q||²+||Z2 q||²)/||Tq||².

The full four residuals are

RH=tau[T,[T,H]]-sum_j[Zj,[Zj,H]]-F,
Rq=(tau T²-Z1²-Z2²)q+2q,
R1=tau(-Z1-2[T,Z2]+[T,[T,Z1]])+KZ1+(g²/2)IZ1,
R2=tau(-Z2+2[T,Z1]+[T,[T,Z2]])+KZ2+(g²/2)IZ2.

Their common zero set, with both signs, is bijective to all solutions:
omega=epsilon sqrt(tau), C=omega T, epsilon=+1 or -1.
The full Rq is essential: its contraction alone vanishes at many
non-solutions.

All scalar equations also give a strict signature constraint:
s_X=-i tr(HX), so s_C²<s_Z1²+s_Z2² unless all three vanish.
The proof retains every one of the eight real coordinates per matrix.

A further necessary stress equation is tau N=Bstress, where

G_jk=<Zj,Zk>, D_jk=<[T,Zj],[T,Zk]>, M_jk=<Zj,IZk>,
d=||[Z1,Z2]||², bT=<T,[Z1,Z2]>,
N=G+D-2bT I2, Bstress=d I2+(g²/2)M.

Thus N must be positive definite and Bstress proportional to N with
the exact factor tau. The full scalar equivalence, quantitative
signature bound and sum-of-squares discriminant are printed in the draft.
No exact zero or proof of emptiness has been found.

Bounded next computation: decide a genuinely unrestricted part of this
17-real-variable residual system without deleting phases, prescribing
C to a block, or treating necessary scalar/stress conditions as sufficient.
Any proposed solution must reconstruct both signs and pass all full entries.

## 19. Actual quartic ground-state map and controlled quantum error

Section 17's requested finite Fourier comparison is now proved.
The original two-mode Hamiltonian is

H2=-(hbar²/(2V3)) partial_q² + V3(m²q²/2+Gamma q⁴/4)+h(q),
h(q)=-(hbar²/V3) partial_y²
     +V3(omega_*²+3Gamma q²)y²/4+3Gamma V3 y⁴/32,
omega_*²=m²+(2pi/L1)².

The mass measure is V3/sqrt2 dq dy. Omega_q is the actual strictly
positive ground state, with norm one in sqrt(V3/2)dy, not a Gaussian.
The normalized spectral projection of any fixed positive Gaussian
defines it exactly and consistently. The true ground energy obeys

hbar omega(q)/2 <= e(q)
<= hbar omega(q)/2+9Gamma hbar²/(32V3 omega(q)²).

For V3>=9Gamma hbar/(16omega_*³), the actual fibre excitation gap
is at least hbar omega(q)/2, by min-max and the stated upper bound.

Jf=f(q)Omega_q(y) is isometric. Berry is zero in the positive phase;
the Born-Huang potential B(q)=hbar²||Omega'_q||²/(2V3) vanishes at
q=0 and is strictly positive elsewhere. The exact compressed operator is

Heff=-(hbar²/(2V3))partial_q²+V3(m²q²/2+Gamma q⁴/4)+e(q)+B(q).

With Qq=I-|Omega_q><Omega_q|, the entire off-diagonal residual is

H2 Jf-J Heff f=-(hbar²/(2V3))(2f' Omega'_q+f Qq Omega''_q).

This moving subspace is not reducing. However, for ||f||=1 and
<Heff> <= E, the physical-time evolution discrepancy and leakage are
both at most

|t| [sqrt(30Gamma E)/(omega_*sqrt(V3))
     +9sqrt5 Gamma hbar/(V3 omega_*²)
     +(96/5^(3/4))sqrt(Gamma hbar/(V3 omega_*))].

Full form and operator domains, actual quartic-state moment bounds,
derivatives, reduced resolvent and Duhamel proof are in
homogeneous_quantum_confinement.tex, section fq:section.
The error is O(V3^-1/2) at fixed hbar,Gamma,L1,m²,E,t.
It is NOT uniform as omega_* tends to zero or on growing time windows
without checking the displayed bound. These are two-mode operators,
not an independently constructed continuum field Hamiltonian.

The original TeX of Panati--Spohn--Teufel (2007), arXiv:0712.4369,
was checked for the projection/invariance distinction. The general
Berry/Born-Huang mechanism is established literature, not new.
Our precise retained coefficients, domains and conservative error
are proved directly. Merely adding Born-Huang does not certify a
higher-order approximation.

Bounded next task for the Yang-Mills/quaternionic lane:
test the joint cusp/soft-Fourier regime m²=0, L1 increasing and
V3 varying with the original torus geometry. Prove what the true
quartic fibre operator contributes when the harmonic frequency
omega_* tends to zero, and whether a nontrivial initial-energy and
physical-time window still admits an error-controlled map.
Keep the exact V3,L1,Gamma,hbar dependence and all quartic terms.
Do not infer a full interacting mass gap or its absence from this
two-coordinate comparison. A different scaling must be exhibited
with an exact inverse dictionary, not substituted silently.

## 20. 5 September: exact coupling fibres and the spatial exceptional set

The complete continuation is in the same quaternionic proof module,
labels q444:finite-coupling-bound, q444:finite-coupling-schur,
q444:finite-coupling-domain-test, q444:finite-coupling-exact-degree,
q444:finite-coupling-fibre and q444:generic-projection-obstruction.
It advances Section 18's unrestricted problem while preserving every
earlier dated calculation. The original H,q,F, all sixteen spatial
coordinates, the original positive g² and both frequency signs remain.

For a fixed noncommuting ordered pair, retain J=iH, <J,J>=3/4,
W=J-perp, its original orthogonal projection Pi, B=[Z1,Z2],
eta=<J,KJ>, w=Pi KJ and beta=<J,B>. Then eta>0 and the full Schur
data are I7=I restricted to W,
S7=Pi K restricted to W-(w tensor w)/eta and
f7=Pi B-(beta/eta)w. No stabilizer component is discarded. With
t a polynomial indeterminate evaluated at the original g², set

M7(t)=t I7+2S7,
D7(t)=det_W M7(t), V7(t)=4 adj_W(M7(t))f7,
N7(t)=V7(t)+(2 beta D7(t)-<w,V7(t)>)J/eta,
alpha=1/4+||Z1 q||²+||Z2 q||², Q7(t)=||V7(t)q||².

The Schur determinant is positive for every t>0, has degree exactly
seven and leading coefficient 3/128. The inverse is T=N7/D7 and
Tq=V7q/D7. The domain is empty for every positive coupling exactly
when Q7 is identically zero, which is equivalent to all three vector
equalities f7 q=0, (S7 f7)q=0 and (S7² f7)q=0. This includes cases
with f7 nonzero. Commuting spatial pairs also have empty solution fibres.

When Q7 is not identically zero, the full residual polynomial p_Z
defined in q444:finite-coupling-one-polynomial has degree exactly 28
and is nonnegative on the entire real line. The complete admissible
coupling set is exactly

{t: 0<t<=t_*, Q7(t)>0, p_Z(t)=0},

where q444:finite-coupling-bound gives the original explicit bound t_*.
Every real root has even multiplicity, so there are at most fourteen
admissible couplings. Each admissible root reconstructs precisely the
two original solutions over that spatial pair:

g²=t,
omega=epsilon sqrt(alpha)D7(t)/sqrt(Q7(t)),
C=epsilon sqrt(alpha)N7(t)/sqrt(Q7(t)), epsilon=+1 or -1.

Thus each spatial fibre has at most twenty-eight original tuples.
No Q7=0 root is included. The original K,O,Omega spacetime inverse
remains exactly the one proved in the canonical module.

A further theorem constrains the entire spatial projection at once.
In the original sixteen real coordinates xi of U*ZjU, the two selected
diagonal residuals
F_xi(t)=eta^16(U*P_H(t)U)11 and
G_xi(t)=eta^16(U*P_H(t)U)22 extend polynomially with degree at most
twelve in t. Their inverse on eta>0 divides by the retained eta^16.
In increasing-power bases, putting the A summand first, define the
fixed 24-by-24 coefficient map

(A,B) -> A F_xi+B G_xi,
R[t]_<12 plus R[t]_<12 -> R[t]_<24,

and its determinant R(xi). At any full solution, evaluation at its
original coupling annihilates the image, so R(xi)=0. This argument
also covers every degree-drop case.

The theorem's fully populated exact pair has eta=93/2. Its two
diagonal residual polynomials have a Bezout certificate over Q(sqrt(6)).
The reduction sqrt(6)->39 modulo 101 checks all denominators and gives
the displayed identity af+bg=1. Independent reconstruction from the
full eight-dimensional Gauss matrix gives Sylvester determinant 40
before eta^16 clearing and 60 afterwards. Hence R is not the zero
polynomial. The spatial projection is contained in the proper closed,
nowhere-dense, measure-zero real algebraic set {xi:R(xi)=0}.

Existence within this exceptional set, or global emptiness of the full
rotating ansatz, remains unresolved. The containing zero set is not
asserted equal to the solution projection. These results do not settle
arbitrary time-dependent complex lifts or any quantum spectrum.
The coefficient map is the classical Sylvester construction, attributed
to the [Stacks Project, Tag 00UA](https://stacks.math.columbia.edu/tag/00UA);
the full retained-residual application is proved in the canonical text.

The [finite-coupling evidence directory](../finite_coupling_20260905/)
contains the integration and exact-certificate record. The designated
[final build receipt](../finite_coupling_20260905/FINAL_BUILD_RECEIPT.json)
records the measured build results when complete. Earlier build, visual
and public-release receipts keep their original dated scope; this
feedback does not assert a new remote synchronization.

## 5 September: exact exclusion within the exceptional spatial set

The quaternionic draft and workbench now contain the full proof excluding
the eight-dimensional linear class where both spatial matrices exchange
the matter line and its orthogonal complement. Gauss forces the temporal
block; complete scalar and gauge residuals yield a strictly positive
contradiction for every original g²>0 and both frequency signs. The same
class lies inside the spatial Sylvester zero set, through an explicit
degree-four block factor and its squared common residual factor.

A new denominator-free residual identity gives a positive lower bound for
the full spatial-equation error on the exact scalar-plus-Gauss zero set.
The bound is uniform when spatial norm is bounded and g² stays away from
zero. This is a constrained error certificate, not a quantum mass gap or
an assertion of existence on that constrained set. Existence outside the
excluded class is still open. Full equations, inverse coordinate maps,
proofs, and 28 exact checks are retained under
`supporting_materials/workbench/evidence/two_cross_exceptional_20260905/`.
