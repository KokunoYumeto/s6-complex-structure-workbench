# Theorem18.5: component-resolution repair

Canonical identity `night:P2.6`, tag02RG. Input source SHA256 `7479a42f0c18cb2853e483ba3b0b222087e800a6a720ca5f2a21313ff6706cc6`.

Complete original and current 18.3/18.5 statements/proofs actually read; replacement compared in full with all four steps. Exposed repair, not derivation-before-proof and not a new independent computation.

## Exact gap and origin

The original/current Step3 asserts D is smooth. The cited total-space/graph resolution establishes smoothness of the ambient filling, not of each central component. The replacement uses nu:Dtilde->D, Stein curve C, finite removed base values, the proper analytic exceptional/intersection subset A, and explicit U->V->Cprime->Bprime->Bcircle maps. Normal circles are taken in the original filling after nu identifies U with an open subset of D_reg.

The same sentence occurs in the attached original; this is a scoped proof dependency correction, not a refutation of the theorem.

## Exact maps and open sets

The proper resolution nu is an isomorphism over D_reg. The Stein factorization of f_D nu is p:Dtilde->C followed by finite h:C->B. The finite set Sigma contains0,1,infinity, branch values of h, and h-images of critical values of p. On Bprime=B minus Sigma, Cprime=h^-1(Bprime), and V=p^-1(Cprime), the first map is a proper submersion with connected fibres and the second is a finite unramified cover.

Remove A=V intersect nu^-1(D_sing union all D-intersections with other central components), and put U=V minus A. General position gives pi1(U)->pi1(V) onto. The image in pi1(Bprime) has index deg(h); the further surjection pi1(Bprime)->pi1(Bcircle) makes the final index at most deg(h). The open isomorphism nu|U sends these paths to D_reg in the original filling. Positive normal circles there keep the complex orientation, lambda and e=ord_D(R).

No ambient or base modification is used in this repair, and no SNC or smooth-component hypothesis is added. The theorem statement and Steps1,2,4 remain unchanged.

## Credit

The complete original/current proof and dependency were read before this repair. This is exposed used-and-rechecked work; no targeted-before-proof, independent or computational credit is claimed.
