# Prerelease derivation: 01GO / cdp:st:E17

Checker: `i_provenance_recovery`. I read the exact safe statement,
the E2 statement supplement, and the four exact graph/ambient excerpts
in `S6_SERIES_PUBLISH_II_E17_graph_ambient_inputs.tex` (SHA256
`dc7ce9c0413642b6ec48e9293d60728224a648277e1d541720dd0c03cbf7f624`).
No E17 target proof, other checker reconstruction, or E_checks.py has
been opened. Related Paper I divisor arguments are prior exposure.
The published CDP98 Proposition 1.1 and its complete proof, p.78,
were read in the journal PDF SHA256
`7e97396a1bea596bd086f6f1fb948ac418a2455a4562b24ad37e38227f512b7e`.
Its stated hypotheses explicitly allow nonreduced compact spaces and
only require the Cartier divisor to meet each positive-dimensional
irreducible component. They do not exclude embedded associated points.

Let I=O_Z(−D)⊂O_Z be the invertible ideal of the effective Cartier
divisor. The canonical inclusions I^(k+1)V⊂I^kV⊂V give a descending
sequence of finite-dimensional subspaces W_k of H0(Z,V). Compactness
and coherence make H0(Z,V) finite dimensional, so W_k is a single
fixed subspace W for every k beyond some integer K.

For s∈W and x∈|D|, its germ lies in I_x^k V_x for every k. A local
generator f of I belongs to the maximal ideal of the Noetherian local
analytic ring O_(Z,x). Krull intersection for the finite module V_x
gives intersection_k f^k V_x=0. Hence s_x=0. A section with zero germ
vanishes in an open neighborhood, so supp(s) is disjoint from |D|.

Conversely, a section whose support misses |D| vanishes on a
neighborhood of every point of |D|. There it has the zero preimage
under I^kV→V. Away from D this map is an isomorphism, with inverse
given by division by the local generator f^k. The preimages glue
because I^kV→V is injective. Thus the section belongs to every W_k.
This proves the exact stabilized subspace asserted in the statement.

Suppose now that Z has no embedded associated components. For a
nonzero section, the coherent image M of O_Z→V is a nonzero
submodule of the locally free V. Its associated primes lie among
those of O_Z. With no embedded primes, some irreducible component
of supp(M) is an entire irreducible component of Z; equivalently,
the section is nonzero at its generic point and its closed support
contains that component. Every such component meets D. Thus a
section with support disjoint from D must be zero, proving eventual
vanishing under exactly the stated associated-component hypothesis.

Here is a counterexample to the printed Proposition 1.1. On P1 choose
distinct points p and q and form the coherent O_(P1)-algebra

    B=O_(P1) ⊕ C_p ε,        ε²=0.

The multiplication is (a,u)(b,v)=(ab,a(p)v+b(p)u). This finite
analytic algebra defines a compact connected complex space Z with
underlying space P1. Its local ring at p is
C{z,ε}/(zε,ε²); away from p it is the reduced smooth curve. The
sole irreducible component has dimension one. Put D=q, with its
usual simple Cartier structure. Its local equation is a regular
parameter near q and a unit near p, so it is a nonzerodivisor
everywhere and meets the irreducible component. The actual tensor
decomposition is

    O_Z(−kD)=O_(P1)(−kq) ⊕ C_p ε.

For k>0 its global sections are exactly C ε. This is a nonzero
section supported at the embedded associated point p, disjoint
from D, for every k. The annihilator of ε at p is (z,ε), proving
the precise embedded-prime mechanism. No change of the meaning of
Cartier divisor or of irreducible component is used.

For the application to the supplied E2 construction, the ambient Y
is smooth: this is stated in the supplied exact E2 excerpt and in
the primary LRS2019 Theorem 3.1 manifold hypothesis. The graph Z in
Y×P1 has local equation av−bu=0, with a,b having no common prime
factor. At c=[u_c:v_c], the map

    Y_c={a v_c−b u_c=0} → Z_c,   y ↦ (y,c)

is an isomorphism of analytic spaces, including nilpotents and
multiplicities. Its inverse is the restriction of the projection
π. This follows directly by imposing u=u_c, v=v_c in the local
graph equation, giving the identical quotient of O_Y. The local
function a v_c−b u_c is nonzero because the meromorphic map is
nonconstant, and hence is a nonzerodivisor in the regular local
ring of Y. This quotient is Cohen–Macaulay and Gorenstein and has
no embedded associated components. The proved eventual-vanishing
criterion applies to these full Cartier fibres whenever the
twisting divisor meets each component, as in the cited use.
This argument uses the exact fibre isomorphism; it does not assume
the graph Z is smooth.

The current-series reference interface to E2 needs a citation repair:
root reports that no current II owning E2 body exists. That editorial
issue is separate from the explicit graph/fibre calculation above.
The whole target proof remains unopened until this derivation freezes.
