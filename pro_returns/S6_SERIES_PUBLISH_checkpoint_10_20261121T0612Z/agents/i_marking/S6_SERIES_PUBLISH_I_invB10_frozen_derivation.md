# Paper I inv:B1.0 — frozen statement-directed derivation

Checker: `/root/i_marking_fresh`.

## Exposure and scope

Before this derivation was frozen I read the target statement intake, the authenticated primary-matrix intake, three verbatim prerequisite definitions supplied separately by the root, and the literal affine-convention input from the root and provenance agent. I did not open the inv:B1.0 proof, any old/current target comparison, or any legacy verification script. The task brief disclosed that other agents had previously seen an equivalent marking computation and suggested a simultaneous-nullspace method in place of their reported direct multiplication. I have not treated the intake author's prior exposure as my own exposure, nor treated that author's provenance authentication as a primary-page view by me.

This check concerns the exact integral marking, the two finite intertwiners, the distinguished circle, the affine signs and denominators, and reversed finite meridians. It does not establish literature novelty, identity of an entire family, or check credit for any overlapping label. The statement retains its common integral basis, index labels, constants 3 and 4, circle, columns, and meridian conventions.

## 1. Exact input objects

The marked lattice is Z^4 with ordered columns (hatgamma, hatu, hatw, hatdelta). The distinguished vector d=hatdelta is (0,0,0,1), and gamma is the row (1,0,0,0). The base labels are p1=0, p2=1, p0=infinity. Thus the index relabelling is the explicit map 0 -> 1, 1 -> 2, infinity -> 0; it changes only the displayed labels of these three points.

The primary common-basis monodromies are

T0 = [[0,-1,-1,0],[1,-1,0,0],[0,0,1,0],[0,0,0,1]],
T1 = [[-1,1,-1,2],[-1,0,-1,1],[1,1,2,-1],[0,0,0,1]],

delta_E=(-2,-1,3,0).

The receiving monodromies are

A1 = [[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]],
A2 = [[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]].

The finite translations are v1=(1,2,-4,0), v2=(-1,-3,3,0), with (m1,m2)=(3,4). Matrices act on columns. The exact source/input hashes and supplied primary locators are in the intake files and freeze manifest.

## 2. Integral coordinate morphism of the named marking

Write the statement's P as

P = [[0,-2,-1,-2],[2,-1,0,-1],[0,2,1,3],[-1,0,0,0]].

Solving x=P y by elementary elimination gives successively

y1=-x4,
y4=x1+x3,
y2=-x1-x2-x3-2*x4,
y3=-x1+2*x2+4*x4.

Thus the exact inverse coordinate map is

P^(-1) x=(-x4,-x1-x2-x3-2*x4,-x1+2*x2+4*x4,x1+x3).

Both maps have integer coefficients, so this is an integral lattice isomorphism. Expansion along the fourth row gives

det(P)=det([[-2,-1,-2],[-1,0,-1],[2,1,3]])=-2-1+2=-1.

The new exact program separately recovers the inverse by four coordinate solves and the determinant by fraction-free Bareiss elimination. It does not evaluate the two target products T_i P and P A_i.

## 3. Reconstruct every simultaneous intertwiner

For an unknown 4-by-4 matrix X=(x_ij), form the 32 scalar linear equations T0 X=X A1 and T1 X=X A2. Their coefficients are formed before a candidate X is inserted. Flatten X by rows in the order x11,x12,...,x44. Exact rational elementary row reduction has rank 14 and free coordinates x31 and x41. Its complete reduced equations are

x11=-(2/3)*x31,
x12=2*x41, x13=x41, x14=2*x41,
x21=-(1/3)*x31-2*x41,
x22=x41, x23=0, x24=x41,
x32=-2*x41, x33=-x41, x34=-3*x41,
x42=x43=x44=0.

Every row operation and its nonzero scaling coefficient are recorded in the exact output; replay reproduces the RREF. Swaps invert by the same swap, a scaling by a nonzero rational inverts by its reciprocal, and row addition inverts by the negative multiplier. Therefore the original and displayed solution spaces agree by explicit invertible operations.

Set x31=3r and x41=k. For integer matrices, k is integral from x41, and r is integral from x21=-r-2k. Conversely every integral r,k gives an integral solution. The entire integral solution lattice is

X(r,k) = [[-2r,2k,k,2k],[-r-2k,k,0,k],[3r,-2k,-k,-3k],[k,0,0,0]]
       = -k*P+r*delta_E*gamma.

The statement's P is reconstructed from the free coordinates (x31,x41)=(0,-1), equivalently (r,k)=(0,-1). This proves both positive-base intertwining identities for the displayed P without inferring a marking from a guessed product equality.

The circle constraint alone does not determine P: X(r,k)d=-k*delta_E, so this constraint fixes k=-1 and leaves r arbitrary. The explicit map P+r*delta_E*gamma equals P*(I+r*d*gamma). Since gamma(d)=0, its inverse shear is I-r*d*gamma. Hence these remaining choices are related by a specified integral shear. No uniqueness claim is made. The proposition states the chosen columns P, which select r=0.

## 4. Distinguished circle

Solving P d=delta_E with the inverse from step 2 gives d=(0,0,0,1). This proves delta_E=P hatdelta. It also follows from the displayed fourth column; the new program verifies it by solving the coordinate equations.

## 5. Fixed translations and the actual affine sign

The fixed-coordinate equations for A1 are y2=2*y1, y3=-4*y1, with y4 free. Thus v1 is fixed by A1. For A2 they are y2=3*y1, y3=-3*y1, with y4 free. Thus v2 is fixed by A2. The program reconstructs these vectors from the two exact kernels ker(A_j-I).

The receiving finite action, supplied as input chart data in display (PD7), has real marking form

G_j(z,c,u)=(g_j z,c,A_j u+v_j/m_j).

The negative-root convention is s_j(g_j z)=exp(-2*pi*i/m_j)*s_j(z). Therefore G_j^(-1) covers the positive-root multiplication exp(2*pi*i/m_j). Using the proved invariance A_j v_j=v_j, the inverse affine map is exactly

G_j^(-1)(z,c,u)=(g_j^(-1) z,c,A_j^(-1) u-v_j/m_j).

Both compositions with G_j equal the identity: the translation term is respectively -A_j*v_j/m_j+v_j/m_j=0 and A_j^(-1)*v_j/m_j-v_j/m_j=0.

The explicit coordinate morphism Phi_P(z,c,u)=(z,c,P u) conjugates this inverse affine map to

(z,c,x) -> (g_j^(-1) z,c,T_(j-1)^(-1) x-P*v_j/m_j),

where j=1 corresponds to Engel index 0 and j=2 to Engel index 1. The linear term follows by multiplying the already proved relation T_(j-1)P=P A_j by the two inverses. Engel's supplied positive-root input uses T_(j-1)^(-1) and adds a_(j-1). Thus the transported affine vectors, with the exact coordinate map and sign specified, are

a0=-P*v1/3,
a1=-P*v2/4.

Solving P w=-3*a0 and P w=-4*a1 yields respectively v1 and v2 for the explicit values

a0=(0,0,0,1/3),
a1=(-3/4,-1/4,3/4,-1/4).

Equivalently P*v1=(0,0,0,-1) and P*v2=(3,1,-3,1). The new program checks these by coordinate solving rather than multiplying P by each v. All denominators and signs in the target statement are retained.

## 6. Reversed finite meridians

The statement gives

Q=[[2,-1,0,-2],[2,-1,0,-1],[0,2,1,3],[1,0,0,0]],
S=[[-1,0,0,0],[-6,0,-1,0],[6,-1,0,0],[2,1,1,1]].

Solving each column equation P*s_j=q_j gives exactly the displayed S, so Q=P S. The inverse coordinate equations for S are

y1=-z1,
y2=-6*z1-z3,
y3=6*z1-z2,
y4=2*z1+z2+z3+z4.

These are the same coefficient matrix S, proving S^(-1)=S. Its determinant is 1 and Q has determinant -1, independently recovered by the new exact program. Thus the reversed basis is again integral, with explicit morphism u -> S u -> P S u=Q u.

For the reversed intertwiner, form the 32 scalar equations T0 Y A1=Y and T1 Y A2=Y. They have rank 14 and free coordinates y31,y41. Exact row reduction gives, with y31=3r,y41=k,

Y(r,k)=[[-2r+2k,-k,0,-2k],[-r+2k,-k,0,-k],[3r,2k,k,3k],[k,0,0,0]]
      = k*Q+r*delta_E*gamma.

The integral-parameter argument is the same explicit coordinate calculation y21=-r+2k. The displayed Q is reconstructed at (r,k)=(0,1). The program proves A1 and A2 have integral inverses and determinant 1. Right multiplication of the two established equations by those inverses therefore gives precisely

T0 Q=Q A1^(-1),
T1 Q=Q A2^(-1).

This checks the two finite-meridian assertions stated in the proposition. No additional cusp-meridian identification or order reversal is asserted.

## 7. Computation record and limitations before proof comparison

All computational steps used newly written standard-library exact rational elimination, explicit kernel reconstruction, and fraction-free determinant elimination. The executable is `S6_SERIES_PUBLISH_I_invB10_exact_reconstruction.py`; its complete row-operation certificates and outputs are in `S6_SERIES_PUBLISH_I_invB10_exact_reconstruction_output.json`. A smaller new probe produced the same two rank-14 kernel parametrizations before the full certificate program was written. Both were written and run before target-proof exposure. No legacy script was executed or imported.

The numerical results establish the displayed integral maps and equations. The geometric affine convention enters through the separately supplied literal (PD7) chart action and Engel's authenticated Construction 3.5/Lemma 3.6 transcription. I have not personally opened those primary page images in this pre-proof phase. I do not claim these linear data uniquely determine the named marking, a family, or literature novelty. The explicit shear family above records the exact ambiguity left by monodromy and circle normalization.

This derivation is to be frozen by content hash and UTC time before the complete target proof is opened. Any later comparison or correction belongs in a separate record and will not alter this frozen file.
