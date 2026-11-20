# V P1.13 item 2: derivation from the isolated permitted inputs

GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited reasoning effort is not separately exposed. This is the same current model family. The reviewer has no recorded substantive reading of the receiving P1.13 item 2 proof. Earlier Paper V contact-sheet QA creates possible incidental visual exposure; this derivation is not described as completely blind. The only target/input text used here is the isolated task message from corrections_audit. No receiving P1.13 proof or computed output has been opened for this derivation.

## Inputs

Let M be a closed oriented smooth complex fourfold, with free integral cohomology of ranks 1,4,1 in degrees 0,4,8. Retain c1=c3=0, the evaluation c2 squared=2, p1=-2c2, and signature 2. The permitted classical inputs are integral duality, the universal coefficient formula, w_(2i)(T_R)=c_i modulo 2, the spin Wu identity v4=w4 when w1=w2=0, and Peters–Sterk Theorem 2.2.1, p.61, in its stated rank-at-most-four unimodular classification scope.

## Complete derivation

Put L=H^4(M;Z), with the actual bilinear pairing Q(x,y)=<x cup y,[M]>. It has rank four. Integral Poincare duality, with the universal coefficient identification and absence of torsion, makes the adjoint map L -> Hom(L,Z), x -> Q(x,-), an isomorphism. Since degree four is even, Q is symmetric. Its signature is 2, so the equations b_plus+b_minus=4 and b_plus-b_minus=2 give b_plus=3 and b_minus=1.

The complex orientation gives w1=0. The stipulated Chern-to-Stiefel–Whitney relation gives w2=c1 modulo 2=0. Thus the tangent bundle is spin. The equality p1=-2c2 in the free group H^4(M;Z) gives the unambiguous integral class lambda=p1/2=-c2, and Q(lambda,lambda)=2.

For any x in L, let bar(x) denote its mod-two reduction. The top Steenrod-square identity on a degree-four class gives Sq^4(bar(x))=bar(x) cup bar(x). By the definition of the fourth Wu class and the permitted spin identity,

Q(x,x) modulo 2 = <v4 cup bar(x),[M]> = <w4 cup bar(x),[M]> = <bar(c2) cup bar(x),[M]>.

Since bar(lambda)=bar(-c2)=bar(c2), this is Q(lambda,x) modulo 2. Therefore lambda is characteristic for the actual middle pairing. This proves both the characteristic property and its specified square, without first selecting diagonal coordinates.

The pairing is odd. Indeed, an even Q would give Q(lambda,x) in 2Z for every x. Under the explicit unimodular adjoint isomorphism above, the homomorphism Q(lambda,-)/2 has an integral preimage y in L, so lambda=2y. It would follow that Q(lambda,lambda)=4Q(y,y) is divisible by four, contradicting its value two. No classification assertion is needed for this parity step.

Apply the permitted Peters–Sterk theorem to this integral odd unimodular rank-four pairing, with its now established inertia (3,1). It provides an integral basis b1,b2,b3,b4 with Q(b_i,b_j)=0 for i unequal j, and diagonal values 1,1,1,-1. The identification with I_(3,1) is the concrete basis-coordinate isometry

phi: L -> Z^4, sum_i n_i b_i -> (n1,n2,n3,n4),

whose inverse sends (n1,n2,n3,n4) to sum_i n_i b_i. Its pairing identity is Q(x,y)=phi(x)^t diag(1,1,1,-1) phi(y). The basis is the one whose existence the cited classification theorem supplies; the isolated inputs do not give a preassigned matrix of L from which numerical basis coordinates could be computed.

As a consistency consequence of the proved isometry, phi(lambda) has four odd coordinates because its characteristic congruence applied to each b_i forces its i-th coordinate to be odd. Its norm equation is a1^2+a2^2+a3^2-a4^2=2. This follows from the characteristic result and does not choose a particular representative vector or assert a transitivity statement about such vectors.

All requested conclusions follow from these actual cup-product, reduction, adjoint and coordinate maps. This is a formal specialization with no separate finite numerical step to certify. The receiving proof comparison is pending after this note is frozen.
