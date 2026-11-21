# Derivation before target proof: 01BN

Owner: `cdp:st:C.1.1`. Checker: `i_provenance`.
Source packet: `agents/ii_infra/statement_packets_v2/S6_SERIES_PUBLISH_II_01BN_statement_inputs.tex`.
The target printed proof and earlier check programs have not been read. Related
Paper I cohomological and topological arguments were read previously; this is a
new derivation for this target, without a claim that its background is unfamiliar.

Let c_i=c_i(T_Y), and l=c_1(L), with rational cohomology coefficients. Since
H^2(Y,Q)=0, c_1=l=0. Hirzebruch--Riemann--Roch for the holomorphic vector bundle
T_Y tensor L gives chi as the degree-six integral of ch(T_Y) exp(l) td(T_Y).
In complex-degree notation,

ch(T_Y)=3+c_1+(c_1^2-2c_2)/2+(c_1^3-3c_1c_2+3c_3)/6,
td(T_Y)=1+c_1/2+(c_1^2+c_2)/12+c_1c_2/24.

Multiplication gives degree three

c_1^3/2 -19c_1c_2/24+c_3/2
+l(5c_1^2/4-3c_2/4)+5c_1l^2/4+l^3/2.

Every term other than c_3/2 vanishes by c_1=l=0. Thus chi(T_Y tensor L)=integral
c_3/2. The complex orientation identifies the Euler class of the real tangent
bundle with c_3. Poincare duality on the underlying closed oriented six-manifold
gives b_6=b_0=1, b_5=b_1=0, b_4=b_2=0; its Euler characteristic is 2-b_3.
This proves both asserted numerical equalities with the stated orientation.
The fresh Fraction-based multiplication in the accompanying 01BN program
checks the polynomial coefficients independently of a previously saved program.

For the Picard claim, finite CW type makes H^2(Y,Z) finitely generated, and b_2=0
makes it finite. Also H^1(Y,Z)=Hom(H_1(Y,Z),Z)=0 because b_1=0. The exponential
sequence gives the exact segment

H^1(Y,Z) -> H^1(Y,O_Y) -> H^1(Y,O_Y^*) -> H^2(Y,Z) -> H^2(Y,O_Y).

The last arrow is zero: its source is finite and its target is a complex vector
space. The first group is zero. Therefore the first Chern map is surjective
with kernel exactly the injected complex vector group H^1(Y,O_Y). That kernel
is the identity component: it is connected, and the finite discrete Chern
classes are locally constant in holomorphic families. Each fibre of c_1 is a
torsor for the kernel, so the claimed component description and canonical
component-group identification follow.

Scope: full statement derived from HRR, the exponential sequence, finite CW
type, and oriented Poincare duality. No new geometric hypothesis is introduced.
No target-proof comparison or event eligibility is asserted yet.
