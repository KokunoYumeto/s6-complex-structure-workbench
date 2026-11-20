# Paper V statement-first derivations, checkpoint 06

Actor: GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited from root (not separately exposed).

Exposure: all 27 extracted target statements and the six main theorem outline maps were read. Earlier in this run the literature comparisons for P1.18, P1A.1--6, F4.1 and E.1/E.2 and the cited-specialization proofs P1.9/F1.1 were read. During setup extraction in this phase, source V lines 5190--5310, 5328--5375, 5470--5608, 6955--7048 and 8220--8264 were exposed: these include parts of F3.1/F3.2/F2.4/F2.5, the end of P1.19, the full first two P1.4 proof steps, and the end of F4.1. They are not blind receiving reads. No P1.15, P1B.1 or P1B.2 proof has been opened at this commit.

## P1B.1: integral maximal square-zero normal form

Let I=im(N). Since N^2=0, I lies in K=ker(N), and both have rank three. K is primitive as the kernel of a map to a torsion-free group. Primitivity of I in Z^6 means Z^6/I is torsion-free; K/I, a finite group of equal-rank sublattices, is then zero. Hence I=K. The map N:Z^6/K -> K is surjective and injective. Choose a basis e_1,e_2,e_3 of K and lifts f_i with N f_i=e_i. These six vectors form a basis because their quotient images are a basis of Z^6/K. In the order (e,f), N has upper-right identity and other blocks zero. For R=(A B; C D), RN=NR gives C=0 and D=A. Determinant R=det(A)^2, so integral invertibility is precisely A in GL_3(Z); B arbitrary integral. This proves the whole stated theorem before its receiving proof.

## P1B.2: finite spectral enumeration

A finite affine lift with linear part M lacking eigenvalue one has a fixed point: choose a real lift of its translation v and solve (I-M)x=v, then reduce mod Z^6. Thus Phi_1 must occur. The degree-six cyclotomic product is a multiset of phi(n) with sum6; only n with phi(n)<=6 are needed. A commuting J gives even real dimensions of the +1 and -1 eigenspaces. Conversely on those even spaces choose paired standard complex structures, and on every nonreal eigenpair use its rotation plane; this commutes with M. The upcoming independent enumeration records both filters exactly; the statement only claims a preliminary spectral list, not affine or global existence for each entry.

## P1.1: exact route before its receiving proof

Use the displayed A,B from F2.5, M_i=transpose, M0=(M1 M2)^-1. Orders, characteristic polynomials, rank/N^2 and Smith factors are direct exact matrix calculations. Coinvariants are coker of the horizontal concatenation (M1-I,M2-I), invariants kernel of the vertical concatenation; dual assertions use A,B. The invariant homology covector is first-coordinate projection because the first row of each M_i is e0^t. Its application to the jth affine power adds j*ell(v_i)/m_i, respectively j/5 and -j/4; for 0<j<m_i that is nonintegral and proves freeness. This proves all affine powers without a floating-point search.

## P1.15: independent algebraic connection route before receiving proof

For f=x^5+lambda^3*x+lambda^4 and omega_k=x^k dx/y, reduce
- x^k f_lambda/2 = f sum_{j=0}^3 c_j x^j + f R' - f'R/2,
where deg R<=4. This polynomial identity gives the Gauss--Manin derivative modulo the explicit exact form d(R/y). Form the exterior-square connection on ordered pairs (01,02,03,12,13,23); project by 12=-3*03 onto (01,02,03,13,23). Exact rational comparison with the printed Gamma_W closes the geometric lower-rank connection gate. It does not by itself identify the upper row b with the supplied nonsplit rank-six integral extension, prove a common normalized monodromy intertwiner exists, or determine the alpha scalar. Those exact extension/normalization gates are left for the full proof comparison; residual intervals containing zero cannot close them.
