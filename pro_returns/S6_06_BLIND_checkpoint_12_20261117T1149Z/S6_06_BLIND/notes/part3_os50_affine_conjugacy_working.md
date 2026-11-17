# Actual local affine-norm conjugacy for the OS50 caps

This is a new complete local derivation for audit. It concerns extending affine source maps with the prescribed canonical root deck D and the already permitted central component action. It does not move an order-one annular clutch between distinct source sites.

Let A0=t_R0 D be the constructed canonical source norm solution and A=t_R D another extending solution, with A^m=A0^m=t_(−nQ). Their translation difference S=R−R0 is a holomorphic section of the root Neron smooth group and satisfies Norm_D S=0. Conjugation by the actual translation t_T changes R0 to R0+(1−D)T. We construct T with(1−D)T=S.

## Central value and its exact solution

For the good-IV root, the central group is the elliptic curve E0 and D has order3. The actual isogeny1−D:E0→E0 is surjective of degree3. Thus choose T0 with(1−D)T0=S0 and extend it to a holomorphic local section of the smooth root family. Such an extension follows from the local submersion coordinate at T0.

For the reduced-IV root, D fixes the component group Z/3 and m≡1 mod3. The central component of Norm S is m times that of S, so S0 lies in the additive identity component. Write the derivative of D there as lambda. If lambda≠1, take T0=S0/(1−lambda). If lambda=1, Norm S0=mS0=0 forces S0=0, and take T0=0. Extend T0 through the smooth Neron group by its submersion coordinate.

For the starred root, m=2 and both source solutions act transitively on I2, so both translation components are odd. Their difference S0 lies in the multiplicative identity component C*. There D acts by inversion. The actual map1−D on C* is squaring, so choose T0 with T0²=S0. Extend it as a section of the identity component. This uses equality of the permitted component actions; no assertion is made about the nontransitive component class.

After this first translation, the remaining norm-zero section has central value zero. Shrink the root disc so it lies in the formal-group neighbourhood of the identity. The fibrewise analytic logarithm identifies that neighbourhood with the Lie line, and D acts linearly on it over its finite base rotation. Let s be the logarithm. Then Norm_D s=0, since its sum is an analytic lattice-valued function and vanishes at the central point. The explicit finite sum

    t=−(1/m) sum_(j=0)^(m−1) j D^j s

satisfies(1−D)t=s: multiplying the sum by1−D gives Norm s−m s. Exponentiating t gives the required residual section. Combining the two actual translations produces

    t_T A0 t_T^−1=A,   t_T t_(−Q)=t_(−Q) t_T.

These maps extend on the minimal root surface because the translating section lies in its Neron smooth group; in the good case this is the smooth elliptic group action, in the Tate case it is multiplication by its unit point, and in the reduced-IV charts it is the extending section translation already used in the actual construction.

## Lifting the conjugacy and retaining the remaining phase

The root line N has multidegree zero. Translation by T preserves its generic Picard point. The proper-direct-image/vertical-degree argument of P3K.15 gives an actual invertible line lift L_T after removing an integral whole-fibre factor by its base equation. Such degree-zero translation lifts commute fibrewise: on a vector cover the line is(C×C*)/Lambda with constant multiplicative period characters, and two translation lifts act by constant translations in C and constant scalars in C*, hence commute. Every other lift differs by a base scalar. This proves[L_T,B]=1 on the smooth generic fibres, and extension proves it on the root neighbourhood.

The conjugated canonical line map L_T A0 L_T^−1 and the given A cover the same actual source map. Their ratio is therefore a holomorphic base unit f(z). Both have mth power B^n, so

    product_(j=0)^(m−1) f(zeta_m^j z)=1.

Its central value chi=f(0) satisfies chi^m=1. Write f=chi exp(g), with g(0)=0. The same finite averaging sum solves the norm-zero logarithm g as a scalar coboundary. Conjugating by the resulting nowhere-zero base unit removes exp(g), leaving precisely the constant character chi. This character is retained as the integral delta phase of the cap; it is not declared zero.

Thus every extending source norm solution in these permitted OS50 component classes is actually conjugate to the constructed one, and every line lift differs after that conjugacy only by the retained finite delta character and the specified outer collar. The one- and two-cap homology matrices already retain the actual collar coefficients c,kappa, so their topology conclusions do not require a numerical choice for this conjugacy's outer marking. The result is local and does not settle the integral effect of transferring order-one clutches between distinct sites.

## Exact quadratic Tate formula and scalar arrow

With the prescribed marking, A(Z,z)=(R(z)/Z,-z), R=z w, and A0 has R0=z w0. Equality of norms makes S=w/w0 an even unit. Its even analytic square root U gives C_U(Z,z)=(U(z)Z,z) and C_U A0 C_U^-1=A, because U(z)U(-z)R0(z)=R(z). The map need not fix the canonical inversion centres. Transport the full divisor diagram by the actual isomorphism Bl_(Z0)S'→Bl_(C_U Z0)S' induced by C_U, and define the new quotient map as the old quotient composed with the inverse lift. This transports E0+E1 instead of asserting invariance of its original centres.

In the line comparison set C=L_T A0 L_T^-1 and define the ratio by A=m_f C, so f is a **target** scalar. Scalar conjugation has target ratio b(z)/b(zeta_m^-1 z). Formula (F49.2) gives A=chi m_b C m_b^-1. In the quadratic case g is odd and b=exp(g/2), so b(z)/b(-z)=exp(g). The finite chi is retained.
