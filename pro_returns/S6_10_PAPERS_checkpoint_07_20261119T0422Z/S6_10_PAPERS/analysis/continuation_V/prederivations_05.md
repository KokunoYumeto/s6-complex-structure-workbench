# Prereading derivations, batch 05 — connection and numerical gates

Written before opening printed proofs of night:P1.15, P1.16 or P1.18. The displayed connection and the normalized-intertwiner definition are statement data. No earlier numerical checking program has been inspected or imported.

## Exact model checks

The new polynomial de Rham reduction already gives all entries of Gamma_W. With the displayed extension row b, use D=diag(1,lambda^2,lambda,1,lambda^-1,lambda^-2). The row-frame rule (E D)'=(E D)(D^-1 Gamma D+D^-1 D') gives a Fuchsian matrix R0/lambda+Ra/(lambda-a), with a=-256/3125 and rational constant residues. This equality has now been checked symbolically entry by entry in fuchsian_model.py. At the cusp, the original residue squares to zero and has rank three. After lambda=t^4 and gauge diag(1,t^6,t^3,1,t^-3,t^-6), every connection entry is regular at zero. After lambda=u^-5 and gauge diag(1,u^-8,u^-4,1,u^4,u^8), every entry is regular at u=0. The corresponding deck characters are (1,-1,-i,1,i,-1) at zero and all fifth-root characters with the trivial one repeated at infinity. Thus the displayed local model has the finite spectral types, finite local reduction and maximal square-zero cusp that the statement requires. Identifying this complex extension with the integral representation still uses the exact uniqueness/monodromy result; the alpha normalization 625 pi i/128 needs an explicit invariant-line comparison. These have not been independently derived here and must not be claimed as completed whole-proof checks merely from local spectra.

## New continuation recurrence and its error estimate

For H'=H(R0/lambda+Ra/(lambda-a)), put Q1=R0+Ra. At a centre z, let p0=z(z-a), p1=2z-a, q0=zQ1-aR0. Writing H(z+t)=sum H_n t^n gives

(n+1)p0 H_(n+1) = H_n(q0-n p1 I)+H_(n-1)(Q1-(n-1)I),

with H_-1=0. This two-term matrix recurrence is derived by multiplying the ODE by lambda(lambda-a) and comparing coefficients. It avoids numerical differentiation and convolution.

Choose a complex disc of radius R below both |z| and |z-a|. A valid infinity-norm coefficient bound on it is K=||R0||/(|z|-R)+||Ra||/(|z-a|-R). Along a radius the ODE and the submultiplicative matrix norm give sup ||H|| <= ||H(z)|| exp(KR). The Cauchy estimate therefore bounds the truncation after degree n at |t|<R by ||H(z)|| exp(KR)(|t|/R)^(n+1)/(1-|t|/R). All arithmetic and this remainder can be enclosed by Arb complex balls. Rational polygon vertices and dyadic subdivision keep all step endpoints exact. This is a rigorous analytic tail bound; checking that a last coefficient happens to be small would not supply the required certificate.

## Recovering the marked real form

Continue H(1)=I around based loops for zero and infinity. The original frame has D(1)=I, so these are the original monodromy matrices. For the declared target integer matrices A,B, solve XL_infty=AX and XL_zero=BX, Xe0=e0. The solution has thirty remaining unknowns. Choose a nonsingular thirty-row minor by approximate pivoting and then solve that exact selected linear system in ball arithmetic. An invertible enclosed determinant proves uniqueness for those equations. Existence and compatibility with all the other equations must come from the independently checked global extension identification; numerical residual containment is a useful check but does not by itself prove existence for an overdetermined system.

At an ordinary lambda, recover Y=H D^-1 and multiply by X. The four real unknowns Re/Im(v2,v1) solve the five real lower-coordinate equations Im(Y_(lower,1)v2+Y_(lower,2)v1-iY_(lower,3))=0. The rank-four unique solvability comes from the intersection-line theorem. Select a nonsingular real minor, solve it with balls, and evaluate h_b by the stated top-coordinate formula. This supplies enclosures at lambda=1 and 2. A second independently formulated numerical continuation, if written, can compare precision but does not replace the first certificate.

## What remains for the global minimum

The root chart at infinity has an ordinary holomorphic connection in u=lambda^-1/5. It gives a convergent Taylor fundamental solution at u=0. Joining a small positive root point to lambda=1 fixes its normalization and computes XH_infinity. The displayed exact constant then has an Arb enclosure. To prove a global minimum, a separate argument must enclose all other base points and the Hessian/first nonzero root expansion near infinity, with finite covers of the remaining compact region and a cusp lower bound. Neither a sampled grid nor agreement of two point values proves the unique global minimum. I have not yet derived that global inequality and will not claim P1.18 proved merely from the infinity constant.
