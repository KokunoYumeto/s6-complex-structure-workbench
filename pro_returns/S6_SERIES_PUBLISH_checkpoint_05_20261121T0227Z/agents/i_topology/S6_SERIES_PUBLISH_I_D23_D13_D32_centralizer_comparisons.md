# Boundary and reused centralizer comparisons

Original source: source/S6_SERIES_GRIND_I.tex, SHA d2e6c3bec1500144bfc0ef85e636ded534f2abc998cf58fdaf521b1e8a183169. Comparison completed 2026-11-21. Each target proof was opened after the associated saved derivation; WB centralizer deliberately reuses the earlier E.1.2 exact centralizer evidence, with prior parallel proof exposure disclosed in the preread file.

## push:src:D.2.3 (032F)

The preread proof was derived directly from the four period columns, using an exact separating character and explicit approaching period vectors. It avoids the printed proof's generic-ray/duality route. The saved program independently inverts the actual real period matrix over rational test fields; all 64 exact cases agree with the printed dual formula and the direct character. The same output checks 12,175 reduced rational gcd cases for G_a=(1/lcm(2,n))Z. No retained program was executed.

Printed Step1: with r=d0,p=q=0, the exact inverse-transpose formula equals d0 times the preread character chi_h. The Taylor cancellation T Re B-6xy=O(|h|^4), while D=-3|h|^2+O(|h|^4), proves its continuity and all claimed coefficient orders. Its period values are integral. Thus it separates exactly the indicated distinct rational central classes.

Printed Step2: on a ray with p Re omega+q Im omega nonzero for every nonzero half-integral pair, the dual coefficient diverges for such pairs. A convergent sequence of dual vectors has bounded first and third entries, hence constant p and r after passage to a subsequence; its second entry then makes q bounded and likewise constant. The integer fourth label is bounded as well. Thus examination of fixed labels does exhaust bounded dual subsequences. If p=q=0, boundedness requires ar integral; the surviving lattice is Z d0 Re xi for rational a, and zero for irrational a. Cornulier's exact Theorem3.1 applies to the real vector space underlying C² and identifies annihilator limits. Its primary publisher PDF was actually viewed/read on PDF11–12, printed pp2017–2018: statement, linear-dual identification, and complete proof. This agrees with the preread explicit construction of every required limit period, including the quadratic-scale imaginary differences. No assertion of the full D.3.1 arbitrary-K realization is checked by this event.

Printed Step3: the base coordinate, local torus-bundle separating functions away from zero, and the exact central character distinguish the surviving classes. These functions descend through the proposed quotient; its universal property follows from the quotient topology and identification of every nonseparated pair. The central quotient topology is the usual circle topology in the rational case because the section r -> [(0,r)] gives the inverse to the character quotient. Irrational a collapses the central fibre to a point. All printed steps agree. No source correction is required.

## push:src:D.1.3 (032C)

Saved preread uses canonical uniqueness, finite étale torus/Kähler cover and the stated elliptic Albanese to verify D.1.2, then selects a good point on an uncountable boundary arc. Printed Step1 instead computes b1=2 directly from the rotation-invariant first cohomology of the product cover; both give the same value. Canonical h0=1 and intrinsic support are exact consequences of the cited floor formula. Printed Step2 is the same countability/holomorphic-continuation contradiction. No selection of the fibrewise isomorphisms is needed. This check uses D.1.2 and D.1.1 as stated proved inputs; it is not a new check of their proofs. Both printed steps agree.

## push:src:D.3.2 (032I)

Saved preread gives explicit sequences for both limits, rather than invoking the full converse realization in D.3.1. The path h=0,c=c*-i epsilon gives V=0, K=L_a, ell=0. The path h=epsilon(1+i sqrt2), c=c*+sqrt3 epsilon-i epsilon² has delta=10epsilon²+O(epsilon^4). Q-linear independence of 1,sqrt2,sqrt3 kills every nonzero rational/half-integral label, producing K=0. The marked quotient maps give dimensions three/two and zero respectively. Printed sole step agrees. Its additional remark about ordinary invertibility away from the order-four centre uses the established strict maximum theorem; the nonextension conclusion is already D.1.3. This event does not reprove the full D.3.1 realization theorem.

## wb:pshift:lem:centralizer (03CQ), association to existing E.1.2 evidence

Printed Steps1–2: fixed-vector and fixed-covector spans have dimension two individually and dimension one in the simultaneous intersection. A fresh small exact supplementary computation verifies the displayed spanning vectors, ranks, quotient matrices Q1,Q2, and their scalar common centralizer. The column equations imply u0=w0=0,d0=b,r=2(a-b),s=-4(a-b),r=-s, hence H=aI+kE. This is the same result as the already independently executed 32×16 rank14 nullspace calculation for E.1.2; the evidence group is deliberately unchanged.

Printed Step3: periodic derivative of a lifted torus map descends to the compact torus and is constant. Its integral lattice map is locally constant and commutes with both monodromies over the identity of the base. Integrality and det=a^4 force a=±1,b integral. Printed Step4: the third/fourth columns are the coordinate vectors, forcing L=aI2; the first column gives a(c'-c)+b=0. These are exactly the preread geometric deductions. All four steps agree. The event associates the reused calculation and the actual full proof comparison to this statement; it is not a new independent centralizer experiment.

## Citation repair to carry into editorial guards

Both D.2.3 and D.3.1 currently cite “Cornulier, Theorem 3.1” without a bibliographic item or page. Exact source: Yves Cornulier, *On the Chabauty space of locally compact abelian groups*, Algebraic & Geometric Topology 11 (2011), 2007–2035, Theorem3.1 p2017; complete proof p2018; DOI10.2140/agt.2011.11.2007. Publisher PDF https://msp.org/agt/2011/11-4/agt-v11-n4-p06-p.pdf, SHA ec403f23a20857eba3224c2a81ee8525596eacc903a43d76d597f336d16ab88b. The receipt records the two actually viewed page-image hashes.
