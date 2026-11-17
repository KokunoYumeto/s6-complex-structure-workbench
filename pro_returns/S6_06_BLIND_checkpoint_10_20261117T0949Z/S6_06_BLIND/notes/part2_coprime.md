# Extension of the corner proof to every coprime (3k,4l)

We use the supplied Viaclovsky logarithmic-transformation construction, Section 2.2, with m1=3k,m2=4l and gcd(m1,m2)=1. In the AC marking the gamma coefficient of the integral invariant twist at the two finite points is l1,l2; admissibility means gcd(lj,mj)=1. An integral cusp collar l0 is retained. Put

    N=m1*m2=12kl,
    b=m2*l1+m1*l2,
    a=b-N*l0.

The parameter cover is w=r^(N/2), so c=-Nv. All local functions tau=s+h,mu,C are unchanged. The gamma period is now (6mu,C-s-Nv). Parameter descent is the delta translation

    H=-(m2*l1 log t+m1*l2 log(t-1))/(2pi i)=b s+U(q),
    U=-m1*l2 log(1-q)/(2pi i).

The finite cyclic actions are unchanged by c->c-N because N/mj is integral. The collar changes the coefficient of s delta to a. Adding a gamma rewrites it as (6a mu,U+a C-Na v), a holomorphic unit action on the cusp charts. The rank-one parameter degeneration has N components. Its finite rotations are m2*l1 and m1*l2, and its component cover is y^N=t^(m2*l1)(t-1)^(m1*l2). Every nonidentity power of either finite group moves that cycle by admissibility. Thus the same charts prove smoothness, properness and reduced NC central fibre away from the corner.

On q=Q^N the two origins are

    o=(-6b mu s/N, b s²/(2N)-b C s/N+l0 s/2+v(b s+U)),
    sigma=-l0 z_gamma+(6a mu v,vU+aCv-Na v²/2+Na v/2).

Their difference is a F_N, with

    F_N=(6mu(s+Nv)/N, C(s+Nv)/N-(s+Nv)²/(2N)+Nv/2).

The exact differences on q=Q^(Nm), r=R^n are

    Delta_Q(aF_N)=a m gamma-(N/2)a m² delta,
    Delta_R(aF_N)=a n gamma-(N/2)a n(n-1)delta.

N is divisible by twelve, so every displayed lattice coefficient is integral. The program code/part2_general.py verifies all identities as rational polynomial identities with symbolic N.

## The intrinsic base map

The vertical determinant bundle from the finite root characters is

    L=f*O(-1) tensor O(2k S1+l S2).

To see the exponents, pull the original order-three chart back by the k-th power: its frame vanishing order 2 becomes 2k. The order-four frame vanishing order 1 becomes l. These are actual pullbacks of the local tangent transition matrices. The image of df has determinant f*O(2) tensor O(-(3k-1)S1-(4l-1)S2); the cusp singular ideal is supported in codimension two and contributes no determinant divisor. Therefore

    K_X^(-1)=f*O(1) tensor O((1-k)S1+(1-3l)S2),
    K_X^(-N)=f*O(d),       d=4l+3k-kl.

d is nonzero. Indeed d=0 would imply k divides 4l. Coprimality gives gcd(k,4l)=1, so k=1, but then d=3l+3>0. Taking K^(-N) for d>0 and K^(N) for d<0 gives f*O(|d|).

For an arbitrary proper filling, resolve its reduced dominating component. The direct image of the indicated relative pluricanonical line bundle is coherent and torsion free of rank |d|+1 on the disc. Its evaluation gives a meromorphic map into P^|d|, restricting on every punctured fibre to the degree-|d| Veronese embedding of the base. Resolve the graph. The proper image is an analytic surface over the disc. Its generic fibre over the field K of meromorphic germs is a smooth rational normal curve: its homogeneous equations are the kernels of the multiplication maps of the coherent direct-image modules, tensored with K, and on the puncture these equations are exactly the Veronese equations. The three components of the critical-value image give three distinct K-rational points, labelled by multiplicities 3k,4l and the cusp. Distinctness follows from gcd(3k,4l)=1, which excludes equality of the two multiplicities.

There is a unique isomorphism of this curve over an algebraic closure of K with P1 taking those points to 0,1,infinity. Its uniqueness makes it invariant under every automorphism of the algebraic closure over K, so its rational functions have coefficients in K. In particular its coefficients are meromorphic germs, with finite-order poles. Composing the proper-image map with this rational parameter gives the required meromorphic marked map f on the total space. Resolving its graph gives a proper map to P1 times the parameter disc. This proves the precise extension needed by the corner argument even when d is negative or |d|>1; an arbitrary ratio of two pluricanonical sections would not have supplied the marked degree-one parameter.

## Divisor meridians and contradiction

Modulo delta, the global quotient fundamental group is again the product of the finite-base semidirect product with the parameter loop: all changes of branch of H and all finite-chart c-changes are integral delta translations, while the finite linear coordinate changes are parameter-independent and fix delta. Thus the finite-orbit lemma and the horizontal-central-meridian proof of P2.10-P2.11 apply literally.

At the corner, after q=Q^(Nm), r=R^n, the deck matrices and affine commutator are

    A_Q=I-Nm E32+Nm E41,
    A_R=I+Nn E41,
    [Q,R]=-Nmn b delta.

The commuting lifts Q_o=T_(-mb gamma)Q,R_o=R give the same equation

    (m alpha_i+n beta_i)kappa_j=(m alpha_j+n beta_j)kappa_i

for meridians of meeting axis divisors. The horizontal central ratio is zero; the strict cusp ratio is a. The same connected-fibre and finite-incidence-graph argument forces a=0. But modulo m1, a=m2*l1 is a unit, and modulo m2, a=m1*l2 is a unit. Hence gcd(a,N)=1 and a is nonzero. This is the contradiction for every admissible logarithmic datum of the coprime family, after every finite parameter cover.

The comparison from a hypothetical filling in its original parameter to this cover is finite base change followed by normalization of the dominating component and resolution. All maps are proper, and the open torus family is preserved. Thus nonexistence on this further cover implies nonexistence on the originally proposed cover.
