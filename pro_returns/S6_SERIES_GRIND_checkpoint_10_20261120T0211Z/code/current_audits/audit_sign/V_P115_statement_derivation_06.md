# P1.15: derivation from the isolated target and supplied inputs

Date: 19 November 2026. Reviewer: GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited reasoning effort. Input: `audit_corrections/V_P115_isolated_statement_inputs_06.tex`, SHA256 `ace3b9abf8cd0e79f95eef8228dd08b917ec61338cdfe44d83034a8f09519165`.

## Exposure boundary, frozen before further proof access

I have not opened or read the full P1.15 proof as text. I previously inspected build12 Paper V contact sheets for layout, including pages109,118,122,124,125. The current P1.15 starts on page113, so parts of its proof may have been visible at that resolution. This is a fresh algebraic derivation from the isolated statement and listed inputs, with that prior visual exposure; it is not described as completely blind. No producing upper-extension computation, residue basis, numerical period result or receiving proof has been opened for this derivation.

## Holomorphic splitting and its complete freedom

The five summands of W* are L^j, j=-2,-1,0,1,2. The given Laurent descent yields coarse degrees -1,-1,0,-1,-1. The finite stabilizers are over C, so averaging makes invariant pushforward exact. Cohomology is therefore the corresponding cohomology on P1: H1(W*)=0 and H0(W*)=C in the j=0 summand. Thus every supplied holomorphic extension of W by Oe splits as a holomorphic bundle, and its entire splitting freedom is the one constant row tau=(0,0,c,0,0). This follows from the actual root frames, not an arbitrary meromorphic change of basis.

Write a general upper connection row as beta_j(lambda)d(lambda) in the given column order j=2,1,0,-1,-2. At zero, the actual regular frame is u^(3j)w_j and lambda=u^4, so its upper coefficient is 4u^(3+3j) beta_j(u^4) du. Regularity requires

    ord_0 beta_j >= ceil(-(3+3j)/4) = (-2,-1,0,0,1).

At infinity the frame is v^(-4j)w_j and lambda=v^-5; its upper coefficient is -5v^(-6-4j) beta_j(v^-5) dv. Thus

    ord_infinity beta_j >= ceil((6+4j)/5) = (3,2,2,1,0).

Only a simple pole at a=-256/3125 is allowed elsewhere. Consequently the complete space of global upper rows, before the nilpotent-residue condition, is

    beta = (A/[lambda^2(lambda-a)], B/[lambda(lambda-a)], 0,
            C/(lambda-a), D*lambda/(lambda-a)).

The middle component vanishes because a rational function with at most one simple finite pole cannot vanish to order two at infinity. Each of the other four components is forced to its displayed one-dimensional space by the same divisor count. These bounds also establish that there are no omitted polynomial or higher-pole rows.

## Residue constraint and exact quotient to compute

Let R=Res_a Gamma_W and r=(A/a^2,B/a,0,C,D*a). The full residue is N=[[0,r],[0,R]]. Its square is [[0,rR],[0,R^2]]. I will compute R^2 and the exact linear equations rR=0 directly from the displayed rational matrix, then quotient their solution space by the actual splitting change.

For F' = F[[1,tau],[0,I]], right-row differentiation gives

    Gamma' = C^-1 Gamma C + C^-1 dC,
    beta' = beta - tau Gamma_W + d tau.

Here tau is constant in the middle summand. The full gauge row is therefore the negative of the third row of Gamma_W; it has parameter vector proportional to (300,-375,-48,60), with common divisor3125. This is an actual connection isomorphism fixing e and the quotient, with inverse obtained by -tau. The quotient of residue-admissible rows by this one-dimensional image classifies exactly the supplied extensions at the fixed quotient identification.

The stated row b has (A,B,C,D)=(-25/6,-125/48,1,0). Its D=0 and C=1 imply it cannot be a nonzero multiple of the gauge row, whose D=60/3125. Once the residue equations are checked and their solution space is found to have dimension two, this proves that b represents a nonzero class in a one-dimensional extension space.

## The actual equivalence and common intertwiner

The given integral local system is nonsplit: a splitting off its invariant line supplies a nonzero common invariant covector taking value1 on e0, while the stated input (and the direct matrix check below) gives no common invariant covector. Its canonical root extension is holomorphic and has exactly the regularity/residue constraints used above, so it belongs to the same classified space.

Two nonzero classes in a one-dimensional vector space differ by multiplication by a unique nonzero scalar. Multiplying the quotient W by that scalar is a global horizontal automorphism, and adding the exact tau row gives the required upper-triangular bundle map. This map fixes e, has nonzero quotient scalar, and hence is invertible with the reciprocal scalar and the corresponding negative upper row. It intertwines the complete connections and therefore both fixed based monodromies simultaneously. Evaluation at lambda=1 in the identity-initial-value frame yields the required constant X with Xe0=e0. No interval residual or numerical period approximation is used in this existence argument.

The classification is for flat bundles on the stated punctured root curve. Every meromorphic connection on a complex curve is flat there. The full root-frame regularity and the explicit square-zero residue guarantee the stipulated extensions at the three distinguished points.

## Contraction and uniqueness to compute

Compute the one-dimensional kernel of R restricted to P=<w2,w1,w0>, and evaluate the actual residue row of b on that vector. Changing the holomorphic splitting adds -tau R, which vanishes on this kernel. Thus the restriction gives the splitting-independent map N_V(vtilde)=2pi*i*r(v)e. Dividing that coefficient by alpha_alg(v)=4v0/3 gives the exact claimed scalar; all factors are rational before multiplying by2pi*i.

Finally solve ZA=AZ and ZB=BZ as an exact homogeneous linear system in36 entries. The space of solutions supplies the full simultaneous centralizer. A scalar-only result makes the fixed-line normalization Xe0=e0 unique: the quotient of any two normalized intertwiners is a scalar centralizer element fixing e0, hence the identity.

This note is frozen before opening the receiving proof. The finite calculations just specified are to be saved separately, including their input matrices and complete exact nullspaces.
