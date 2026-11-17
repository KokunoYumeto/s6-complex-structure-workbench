# P3F.28. Exact OS49 translation complexes and their vanishing indices

**Proved.** For the actual OS49 source and line of P3F.26, let
\(T:p\mapsto p+Q\). Its inverse is the suspended translation
\(-Q=-3G\). A lift covering that inverse is, at the target
point \(p\), precisely a map \(M_{p+Q}\to M_p\), so its
linearization is a morphism \(T^*M\to M\). Then
\[
 T^*M=M(-C_0),\qquad T^{2*}M=M(-F),
                                                        \tag{P3F.28.1}
\]
and the actual linearization gives the exact sequence
\[
 0\longrightarrow T^*M\xrightarrow{\phi}M
       \longrightarrow\mathcal O_{C_0}(-1)
       \longrightarrow0.                              \tag{P3F.28.2}
\]
The next translated sequence has quotient
\(\mathcal O_{C_1}(-1)\). Every further translated sequence
has the same form, alternating these two components. All of their
quotients have zero derived global sections. Moreover
\[
 R\pi_*M=0,
 \qquad R\pi_*(T^{j*}M)=0\quad(j\in\mathbb Z).          \tag{P3F.28.3}
\]
These are exact statements about the sheaf morphisms in the actual
construction. The direct spin-c symbol comparison pursued here remains an auxiliary route. P3F.31--32 give positive-fan index zero; P3K.65 gives the negative-fan class \(-3k\) for \(\lambda=r^{3k}\), retaining the actual closing and normal marking.

**Proof.** The divisor calculation in P3F.26 gives
\(\operatorname{Hom}(T^*M,M)=\mathcal O(C_0)\), and the
chosen linearization has its simple zero along \(C_0\).
Multiplication by that section is injective between line bundles
on the smooth source surface. Its cokernel is the restriction
\(M|_{C_0}\). Since \(G\) meets \(C_1\), while \(O\)
meets \(C_0\), this restriction has degree \(-1\) on
\(C_0\simeq\mathbb P^1\). This proves (P3F.28.2), including
the precise map and support of its cone. Translation exchanges
\(C_0,C_1\), and their sum is the full reduced \(I_2\) fibre.
Taking its second iterate gives (P3F.28.1). The next cokernel is
\(T^*M|_{C_1}\), whose degree is
\(M\cdot C_1-C_0\cdot C_1=1-2=-1\).
Full-fibre shifts do not change these restrictions. This proves
the assertion for every iterate, in both directions. The standard
two affine charts on \(\mathbb P^1\) compute
\(H^0(\mathcal O(-1))=H^1(\mathcal O(-1))=0\), so the
derived global sections of every displayed cone vanish.

There is also a direct global calculation of the source index.
The line \(M\) is nontrivial of degree zero on the generic
elliptic fibre. Thus it has no global section. The same argument
applies to \(K_S\otimes M^{-1}\), because \(K_S=-F\)
restricts trivially to that fibre. Serre duality gives
\(H^2(S,M)=0\). Since \(M^2=-2\) and \(M\cdot K_S=0\),
surface Riemann--Roch gives
\[
 \chi(S,M)=1+\frac{M\cdot(M-K_S)}2=0.
\]
It follows that \(H^1(S,M)=0\) as well. The sheaf
\(\pi_*M\) is torsion-free and is generically zero, hence is
zero. The coherent sheaf \(R^1\pi_*M\) is supported at finitely
many base points. Leray therefore identifies its space of global
sections with \(H^1(S,M)=0\). A nonzero coherent sheaf with
finite support has nonzero global sections, so it is zero.
There are no higher direct images because the fibres have
dimension one. Translation is an automorphism over the base,
which proves (P3F.28.3) for every iterate. In particular no
assumption about generic fibres alone is used to conclude
vanishing at the nonreduced \(IV^*\) fibre.

The same calculation applies to the precise degree-three compact
regular-binding pullback discussed in P3F.27. Its section line
has square \(-2\), is nontrivial on the generic fibre, and its
canonical class is a fibre class. Its three identity components
\(C_{0,i}\) satisfy
\[
 M\cdot C_{0,i}=-1,\qquad C_{0,i}^2=-2,
 \qquad C_{0,i}\cdot C_{0,j}=0\ (i\ne j).
\]
Consequently the explicitly defined sheet-translation line
\(M(-\sum_iC_{0,i})\) has exactly the same square as \(M\):
\[
 \left(M-\sum_iC_{0,i}\right)^2
 =-2-2(-3)-6=-2.
\]
Each elementary modification is the pullback of (P3F.28.2), with
its actual quotient \(\mathcal O_{C_{0,i}}(-1)\).
This proves equality of their Dolbeault indices by an explicit
exact sequence. Identifying this exact sequence with the direct
negative-fan graph-normal homotopy remains uncompleted in this
auxiliary approach. P3K.65 supplies the actual sphere-return comparison by the native Cox ruling map. It gives different fan classes and assigns no equality of the two integer indices. **End of proof.**
