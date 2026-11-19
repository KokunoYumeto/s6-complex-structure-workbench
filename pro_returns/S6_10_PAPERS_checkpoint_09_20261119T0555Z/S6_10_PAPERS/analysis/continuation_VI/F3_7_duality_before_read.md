# F3.7: fresh dual, conjugate and cusp-marking derivation

Checker: GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation, 19 November 2026.

Only `analysis/continuation_V/F3_7_duality_statement_input_packet.md` has been read. The target proof and earlier producing calculation remain unopened. The following supplies the actual maps between the given cohomology construction and the specified homology, affine-root and cusp conventions.

## Evaluation and the global conjugation map

For the column-vector cohomology lattice V and its dual lattice Lambda, evaluation is lambda^t f. Thus cohomology transport A sends the dual vector to A^{-t}lambda: (A^{-t}lambda)^t(Af)=lambda^t f. The original evaluation tori therefore have homology transports M1^{-1},M2^{-1}, with Mi=Ai^t, exactly in the dual integral basis.

Let kappa be base conjugation, and form the family E'_lambda=conjugate(E_{conjugate(lambda)}). Equivalently its plane is F'_lambda=conjugate(F_{conjugate(lambda)}) in the conjugate pullback flat bundle. If phi is a functional on F_{conjugate(lambda)}, the map to the new fibre is the functional phi' defined by phi'(conjugate(v))=conjugate(phi(v)). It carries the evaluation of every real integral lambda to the evaluation of the same lambda. The quotient map is therefore defined on the actual tori, not just on their tangent spaces. Conjugation of base and fibre makes this a holomorphic family over the ordinary new complex base; in local holomorphic coefficients it is the map g(lambda) to conjugate(g(conjugate(lambda))).

For the specified real paths, kappa sends each finite peripheral generator gi to gi^{-1}. The new homology matrices are consequently Mi. For g0=(g1g2)^{-1}, the exact group identity is

kappa(g0)=g2g1=g1^{-1}g0^{-1}g1.

Write Mo=M2 M1 for the original dual cusp monodromy and M0=(M1 M2)^{-1} for the target cusp monodromy. The corresponding matrix identity is M0=M1 Mo^{-1} M1^{-1}. This records the based-path conjugation at the cusp; it is not suppressed by saying that all meridians invert.

## The finite affine quotients and their gluing maps

The given numerators satisfy Mi vi=vi. On the original dual root family choose the deck generator

d_old(t,x)=(zeta_m t, Mi^{-1}x-vi/m).

Under base and fibre conjugation it becomes a deck transformation with root rotation zeta_m^{-1}. Its inverse, the positive generator in the new root coordinate tau=conjugate(t), has the exact formula

d_new(tau,x)=(zeta_m tau, Mi x+vi/m).

Indeed inversion sends the old translation -vi/m to Mi vi/m=vi/m. These are precisely the prescribed target affine quotients, so their stipulated free-action property applies without changing any affine numerator. The m-th deck power differs by the integral vector vi, as required for the torus quotient.

The gluing to the punctured linear evaluation family is also explicit. On a root annulus put b_old(t)=-(log t/(2pi i))vi, evaluated as a section of the original torus. A change of logarithm adds an integral lattice vector, so the section is well defined. Since vi is fixed, b_old(zeta_m t)-Mi^{-1}b_old(t)=-vi/m. Thus x to x-b_old(t) identifies the affine root action with its linear action on that annulus. Under conjugation, log(conjugate(tau))/(2pi i)=-conjugate(log(tau)/(2pi i)) on the real-normalized branches. The section becomes b_new(tau)=(log(tau)/(2pi i))vi. Its corresponding identity is b_new(zeta_m tau)-Mi b_new(tau)=vi/m. The two gluing maps are therefore carried to each other exactly, with no added constant translation. Integer changes of branch are already lattice vectors. This supplies the zero-clutch comparison.

## The exact supplied cusp marking

Let Tplus denote the block matrix [[I3,I3],[0,I3]], and let J=diag(I3,-I3). Direct multiplication of the supplied matrices gives S^{-1}M0 S=Tplus. Define the original dual cusp marking

So=M1^{-1} S J.

It is integral and unimodular and satisfies So^{-1}Mo So=Tplus. Its explicit columns are the matrix with rows

(0,0,0,-1,0,0),
(1,0,0,-1,0,-1),
(1,-1,-1,-1,2,2),
(-1,0,0,1,0,0),
(0,1,0,0,-1,0),
(0,0,1,0,0,-1).

This marking is compatible with the supplied F3.6 logarithmic form. To see that the unspecified initial positive logarithmic marking can be replaced by So, compare two integral markings putting Mo into Tplus. Their change G commutes with Tplus. Writing G in 3-by-3 blocks and multiplying shows that G=[[P,Q],[0,P]], where P is unimodular integral and Q integral. The actual period matrix transforms as

(I,Z)G=(P,Q+ZP),

and normalization by P^{-1} on its left gives (I,sI+P^{-1}Q+P^{-1}C(q)P). The new bounded holomorphic remainder is explicit. Thus F3.6's positive logarithmic form holds in the specified So marking as well. This is a change of coordinates in the punctured family before choosing its filling.

The based-path map above carries the original So marking to M1 So. In that marking, fibre conjugation gives periods (I,-sI+C^kappa(q)), where C^kappa(q)=conjugate(C(conjugate(q))) is bounded holomorphic and s=log q/(2pi i). The sign follows from q_old=conjugate(q) in the supplied real-normalized coordinate lambda/a-1. Changing the period-cycle half by J gives the marking M1 So J=S and periods

(I,sI-C^kappa(q)).

Thus the target remainder is C_new=-C^kappa and the logarithmic coefficient in the exact supplied target marking is +I3.

## The period action and every Kuhn chart

In the original additive fibre coordinates, conjugation sends z_old to z_new=conjugate(z_old). In the multiplicative coordinates this is x_new=1/conjugate(x_old), while q_new=conjugate(q_old). Apply this map to the original period multiplier exp(2pi i C_old(q_old)nu_old)q_old^{nu_old}. It becomes exp(2pi i C^kappa(q)nu_old)q^{-nu_old}. With the actual J-induced index nu_new=-nu_old, it is exactly exp(2pi i C_new(q)nu_new)q^{nu_new}. Hence the deck actions are conjugate by the displayed map on the punctured charts.

On the cocharacter lattice this map is Phi=diag(-I3,1), together with conjugation of coefficients. It preserves the specified Kuhn fan. In detail, the simplex at v with order (sigma1,sigma2,sigma3) is carried to the simplex at -v-(1,1,1) with reversed order (sigma3,sigma2,sigma1); its four vertices occur in reverse order. This identity holds for every integral v. If N_old has the four height-one generators as columns and R reverses their order, then N_new=Phi N_old R. Therefore N_new^{-1}Phi=R N_old^{-1}. The exact character-coordinate map on these full affine charts is z_new,j=conjugate(z_old,3-j). It is holomorphic from the conjugate chart, preserves q as the product of the four coordinates, and agrees on every monomial overlap by the same character identity. The already verified period-action equality makes it descend to the actual quotient by the period lattice.

This proves the cusp comparison on the fixed fan, including its height coordinate, integral marking, deck index and bounded holomorphic remainder. The fan is chosen in the So marking before conjugation, and its image is exactly the prescribed fan in S. No refinement or replacement of the target fan is required.

## Scope

The maps above prove the requested passage from the supplied period family to the target homology matrices, affine numerators, zero clutch and the index-one Kuhn cusp. The separate existence of the F3.6 period plane and the general properness of the Kuhn filling are cited inputs. The new arithmetic and fan certificate will check all supplied matrices and the universal symbolic simplex identity before the target proof is read.
