# Derivation before target proof: 01AT

Owner `cdp:st:A.4.4`; checker `i_provenance`. Exact statement and supplied
statement inputs read. No target proof or earlier check has been read.
Related Paper I relative canonical and cohomology arguments are disclosed.

Take a sufficiently small disc Delta around c with no other critical values.
Write V=g^-1(Delta). Since g maps a smooth space to a nonsingular curve and
no component is contained in a fibre, the base parameter is a nonzerodivisor;
g is flat. The relative dualizing line is omega_(V/Delta)=K_V tensor g^*K_Delta^-1.
The coherent g_*omega_(V/Delta) is torsion-free on the disc: a section killed
by a nonzero holomorphic base function is zero on a dense open set and thus
zero. Its generic rank is one because the smooth fibre is a two-torus.
It is therefore a line bundle on Delta. Choose a local generator and apply
the evaluation map g^*g_*omega_(V/Delta)->omega_(V/Delta). This gives a
nonzero holomorphic section sigma of the relative canonical line.

On every smooth torus fibre sigma is a nonzero constant multiple of a
translation-invariant volume form and has no zeros. Its effective zero
divisor is supported on S. Since S is irreducible and reduced, that divisor
equals aS for an integer a>=0. Its local equation is t^a times a unit, where
t is the pulled-back disc coordinate. Dividing sigma by t^a gives a
holomorphic nowhere-zero relative volume form on a neighbourhood of S.
There is no residual zero set of codimension two: the zero set of a nonzero
section of a line on a smooth space is the effective Cartier divisor just
computed. Adjunction for the Cartier fibre identifies the restriction of
omega_(V/Delta) with omega_S, so the divided form trivializes omega_S.

Under H2(Y,Q)=0, the first Chern class of O_Y(S) vanishes rationally.
Hirzebruch-Riemann-Roch gives chi(Y,O_Y(-S))=chi(Y,O_Y), since their rational
Chern characters coincide. The exact ideal sequence gives chi(S,O_S)=0.
The reduced irreducible compact S has H0(O_S)=C. It is Gorenstein as a
Cartier divisor in a smooth threefold, so Serre duality and omega_S=O_S give
h2(O_S)=1. Therefore h1(O_S)=2. This proves the stated triple (1,2,1).

The canonical evaluation, division by the actual local equation, adjunction,
and ideal-sequence Euler equality are the exact maps used. The extra supplied
A.5.2 classification statement is not needed by this derivation.
