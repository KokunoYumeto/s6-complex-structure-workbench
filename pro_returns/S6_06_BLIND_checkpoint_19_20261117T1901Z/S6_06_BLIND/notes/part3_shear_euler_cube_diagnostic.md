# Retained Euler-cube calculation after K63

Working diagnostic, not a promoted integer-index theorem. The actual
K63 quotient/line/p1 proof is complete. The following calculation
records a possible further integer refinement while retaining its
remaining map obligation.

Orient the boundary coframe as
`(d alpha_q, du, dv, d gamma_B, d theta)`. For the selected source
loop, the source coframe is `omega_a=du+(alpha_q-6 theta)dv` after
the actual periodic unit logarithms have been separated. In the
piece coordinates the exterior connection pulls back with curvature

\[
 F_{\mathrm{ext},n}=d\alpha_q\wedge d\gamma_B
                         +n\,d\alpha_q\wedge dv.
\]

The piece has curvature difference `6n dtheta wedge dv`, and its
boundary connection difference is

\[
 \beta_n=-n\{du+(\alpha_q-6\theta)dv\},\qquad
 d\beta_n=-n\,d\alpha_q\wedge dv+6n\,d\theta\wedge dv.
\]

Consequently

\[
 F_{\mathrm{ext},n}+d\beta_n
     =d\alpha_q\wedge d\gamma_B+6n\,d\theta\wedge dv,
 \qquad F_{\mathrm{ext},n}^{,2}=(d\beta_n)^2=0,
\]
\[
 3\int_0^1\beta_n\wedge(F_{\mathrm{ext},n}+t\,d\beta_n)^2dt
   =18n^2\,d\alpha_q\wedge du\wedge dv
                         \wedge d\gamma_B\wedge d\theta.
\]

For a fixed-source scalar loop of winding J the corresponding exact
integral boundary data are

\[
 A_0=dd+(\alpha_q+J\theta)d\gamma_B,
\]
\[
 A_n=dd_n+(\alpha_q+J\theta)d\gamma_{B,n}
                       +nJ\theta\,dv,
\qquad \beta_n=-n(du+\alpha_qdv).
\]

The analogous fifth form has coefficient `3J n^2` in the same
ordered coframe. These are executed exterior-algebra identities,
not a value assigned to a closed manifold without its gluing sign.

The remaining integer-index step is to carry all zero-winding unit
cochains and the actual piece/cap line maps to a single affine family
of curvature representatives, including the global Mayer--Vietoris
class of the boundary gauge. The bulk line change is a multiple of
`theta*b` and its square is zero, so its cube contribution in such
representatives is linear. The actual initial/reflected characteristic
pair is known in K42/K46 (and K62 for the stated scalar scope), but
it has not been used here to choose an unproved global polynomial.
No integer lift of the K56 residue is entered by this diagnostic.

The code is `code/part3/shear_euler_cube_diagnostic.py` with its
saved exact output. This note is independent of the frozen K63 export.
