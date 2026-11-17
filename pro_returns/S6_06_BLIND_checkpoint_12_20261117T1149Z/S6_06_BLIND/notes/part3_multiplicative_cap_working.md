# Multiplicative-cap derivation: completed one-site proof

The completed and independently audited derivation is P3F.40 in
`notes/part3_multiplicative_cap.tex`. Its complete boundary certificate is
`code/part3_root/multiplicative_cap_boundary.py`, with JSON and recorded output.

The exact one-site degree-two cokernel is (Z/m)^2. The actual sphere
sector is m=1,n=+/-1. This does not assert the classification of
simultaneous multiplicative-site replacements or their parameter returns.

The first draft left an exterior coefficient e and two cap coefficients
s,t arbitrary. The executable isotropy check showed the additional
self-pairing condition: e=0 and m*t=A*s. Transitivity gives gcd(m,A)=1,
so s=m*k,t=A*k; the exact integral target basis change retains k and
reduces the full degree-two quotient to diag(m,m). The signed full
four-by-four determinant is -m^2 and the reduced determinant is m^2.

The earlier draft and failed script are preserved under
`code/part3_root/attempts/multiplicative_cap_before_isotropy.md` and
`code/part3_root/attempts/multiplicative_cap_boundary_before_isotropy.py`.
They were never promoted. The final orientation uses c=-c_G because
physical outward gamma covers +G; its affine-root displacement is -A.

The relative Chern-frame argument was independently checked by the checks
agent: the translated Tate-unit boundary frame has no elliptic winding;
dividing the actual Hom section by its sole base zero adds exactly one
signed alpha winding. Its Poincare--Lefschetz dual is +/-F with no rim term.
