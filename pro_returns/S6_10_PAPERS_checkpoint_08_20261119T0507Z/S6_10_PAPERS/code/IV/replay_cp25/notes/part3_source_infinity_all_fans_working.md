# The marked infinity family: full fan and endpoint comparison

Working scope, 2026-11-17 after checkpoint19 recovery. This note retains
actual maps while the extension of the K58 groupoid to every periodic
fan is checked. It assigns no new return class yet.

## IA.1. The global-to-infinity source and line map

Put epsilon=1/rho and v=epsilon^(-2)-1. The actual coordinate map is
X=epsilon^(-2)x, Y=epsilon^(-3)y, T=epsilon^(-4)t. It gives

    y^2=x^3+(-2+3epsilon^2)x^2+t*x+epsilon^2(1-epsilon^2)^2,
    G=(0,epsilon(1-epsilon^2)),
    t_*=(1-epsilon^2)(1-3epsilon^2).

The selected height obeys q_old=epsilon^(-4)q_*. With
s_new=epsilon*s_old the marked source coordinate is exactly

    Z_old=(s_old-rho)/(s_old+rho)=(s_new-1)/(s_new+1)=Z_new.

This is RG.13. It keeps the same selected fan in these two marked
atlases. The separate half-turn map is
I_epsilon(Z,V)=(1/Z,P^a V). Since the target P is P^(-1), the literal
source period h_target gives
h_target I_epsilon=(Q/Z,V)=R_rho. That equality compares the two
half-turn descriptions; it does not insert J into RG.13.

The primitive line lift scales by epsilon^(2a). In the full suspension
2(-1)^(b+1)lambda*q*U_a^b the power epsilon^(2ab-4) is one because
ab=2. Thus the scalar is unchanged. The Hom-section check is literal:
F_ab,old=epsilon^(-1)F_ab,new, v=epsilon^(-3)g and
q_old/(v F_ab,old)=q_*/(g F_ab,new). The degree-two Cartier r map is
retained on both source and target.

## IA.2. The actual finite-cap endpoint

On the parameter logarithm cover the root map is
z_old=epsilon^(4/m)z_new. Its positive endpoint is D_new^(-4), with
the reduced source-coordinate factors zeta_m^(-2), zeta_m^(-3).
The actual normalized line lift is A0=L D with [D,L]=1, so
A0^4 D^(-4)=L^4. The central scalar of L^4 is retained before taking
its small extending logarithm. In the reduced branch the annular
lattice cochain still contains 4 log R-log(4R)=2(1+i), including its
signed source and Cartier factors. The full reference overlap is
transported at a fixed nonzero epsilon_* and completed by the exact
relative Cech maps of RG.6/K49; the doubled period is not removed.

For a coupled global scalar r=v^k r0, the actual infinity path is
r=epsilon^(-2k)(1-epsilon^2)^k r0. The positive ordinary closing
ratio is epsilon^(8nk). Its compensating cochain is
exp(-2pi*i*4nk*t_epsilon*(t_epsilon-1)); the ratio at t+1 is
exactly epsilon^(-8nk). The full cap square and the logarithm of
(1-epsilon^2)^k remain in the same family map. For fixed scalar k=0
these two extra scalar factors are identically one.

## IA.3. Cone-by-cone extension and the marking to audit

For a cone sigma and a character (u,v,h), the half-turn pulls
Z^u V^v q^h back to Q^u Z^(-u) V^v q^h. Writing Q=kappa*q keeps
both the integral height shift h->h+u and the full invertible factor
kappa^u. This is the dual semigroup map for
(x,y,h)->(-x+h,y,h); its inverse is obtained by the same displayed
source/period arrow. All integer powers of the full nonzero unit
extend on the actual cone chart. Integral scalar q^e arrows are
height translations, with their bounded torus remainder retained.
The finite-cap charts lie outside the selected cusp replacement,
and the same ordinary/root maps and full F0 remain on their overlap.

The restored RG.1--6 family uses these actual charts over the compact
marked rho surface. Its source-zero punctures are related by R_rho,
whereas RG.13 transports infinity with the same fan. Therefore the
labelled relation to establish for arbitrary fan T is

    Z_T + Z_(J T) + C_T + I_T^epsilon = 0.

Here C_T is the actual selected-cusp return of that fan. The older
K58 theorem only states its initial/reflected scope; the complete
compact chart and endpoint extension for arbitrary T must be
written before using this relation as an all-fan theorem.

For vertical labels P_j=[[1,0],[j,1]], the exact identical-fan
basis map is P_(1-j)=J P_j S with S=[[-1,0],[1,1]]. The polynomial
identity P_b(j)+P_b(1-j)=3j(j-1)+a and the already proved selected
value C_j=-1-3j(j-1) give the arithmetic cancellation 1-a. This
identity is recorded as the calculation to apply after the full
marked groupoid extension; it is not a new index-pair calculation.

## Attempt history: the additional J at infinity

The pre-recovery candidate relation was
Z_T+Z_(J T)+C_T+I_(J T)^epsilon=0. It used the half-turn identity
h_target I_epsilon=R_rho as though it were the global-to-infinity
rescaling. The fresh full RG.6 read locates the exact distinction:
RG.13 has Z_old=Z_new, while RG.22 explicitly calls I_epsilon the
half-turn. The prior candidate is preserved here and not promoted.
The remaining all-cone/root-cap comparison will retain the local
normalization coordinate at both ends before any all-fan value is
assigned. The vertical cancellation alone does not replace that
completed comparison.
