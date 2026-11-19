# P1.18 — actual right-ODE anchor and gauge maps, before target reading

Reviewer: GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation.

Only root's clean assertion is supplied here. The P1.18 anchor/connection opening and all producing code remain unopened. The earlier isolated polynomial-majorant excerpt did not contain these maps. Scope is exactly the right-ODE constant factor, its inverse/anchor enclosure, and the ordered coordinate/gauge connection formula.

## 1. Existence and invertibility with the given right convention

Use the given regular holomorphic right connection G on its actual parameter chart. On a disc containing the initial point 0, define U_0=I and recursively U_(n+1)(z)=integral_0^z U_n(w)G(w) dw, where U_n for n>=1 denotes the n-th Picard term. Along a straight segment, a bound ||G||<=M gives ||U_n(z)||<=(M|z|)^n/n!. Thus the sum U=I+sum_(n>=1)U_n converges normally, has U(0)=I, and termwise differentiation gives U'=U G with the prescribed right order. Uniqueness follows by the same integral iteration on the difference of two solutions. Continuation along the specified chart/transport path uses this uniqueness; no path independence beyond that specified domain or branch is assumed.

Construct V by the left equation V'=-G V, V(0)=I, with the corresponding convergent Picard series. Then

(UV)'=U G V-U G V=0,

so UV=I. These are square matrices, hence U is invertible and V=U^(-1). Differentiating UU^(-1)=I also gives the exact ordered identity

(U^(-1))'=-U^(-1)U'U^(-1)=-G U^(-1).

This establishes invertibility throughout the continued regular solution domain; it is not inferred from an approximate determinant.

## 2. The constant left factor and the actual anchor

The specified physical solution satisfies Y_root'=Y_root G on the same chart/branch. Therefore

(Y_root U^(-1))'
=Y_root G U^(-1)-Y_root G U^(-1)=0.

Each entry is a holomorphic function with zero derivative, hence constant on the connected overlap. Evaluating at the actual anchor z_c defines that constant as

H_c=Y_root(z_c) U(z_c)^(-1).

Multiplication on the right by U(z) gives the exact identification

Y_root(z)=H_c U(z).

The factor is on the left because both solutions satisfy the same right equation. The construction retains the physical anchor Y_root(z_c); replacing it by an unrecorded normalization would change H_c and is not used here.

## 3. Certified anchor inverse and its order

The algebraic identity above requires the actual inverse. Here is the precise enclosure mechanism for a certified anchor. Let C be a specified numerical matrix and let a rigorous interval/norm enclosure verify

E=I-C U(z_c),  ||E||<=rho<1

in the chosen submultiplicative norm. This is a certificate condition to be checked in the actual computation; no numerical success is claimed in this note. The convergent Neumann series gives

U(z_c)^(-1)=(I-E)^(-1) C=sum_(n>=0) E^n C.

Indeed multiplication on the right by U(z_c) gives (I-E)^(-1)(I-E)=I. The order cannot be reversed without a different residual. After truncating at N, the exact remaining norm is bounded by

rho^(N+1)/(1-rho) ||C||.

Rigorous interval evaluation of the finite sum, together with this norm tail, encloses the true inverse for every actual U(z_c) in the certified input box. Multiplying the certified Y_root(z_c) box on the left by this inverse enclosure encloses the exact H_c above. In the alternative residual convention E'=I-U(z_c)C, the corresponding formula is C(I-E')^(-1); the two residual conventions are not interchanged. This specifies precisely how an already verified anchor certificate enters the exact factorization.

## 4. Coordinate pullback and frame change

The given original frame obeys dE_original/dlambda=E_original Gamma(lambda), and the actual changed frame is

E_root(z)=E_original(lambda(z)) D(z).

Here D is the specified invertible change-of-frame matrix on the chart. Differentiate the actual product in its original order:

E_root'
=E_original(lambda(z)) lambda'(z) Gamma(lambda(z)) D(z)
 +E_original(lambda(z)) D'(z).

Substitute E_original(lambda(z))=E_root(z)D(z)^(-1) and factor only E_root on the left. The resulting right connection is exactly

G_root(z)=D^(-1) lambda' Gamma(lambda(z)) D + D^(-1)D'.

This proves the requested pullback/gauge formula without commuting any matrix factors. The scalar lambda' commutes with matrices, but the displayed order of D, Gamma and D' has been retained. No other collar, cusp, certificate-domain or whole-row scope is claimed.
