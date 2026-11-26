#!/usr/bin/env python3
"""Retained named-object repairs in already-read LT/LV/SB complete proofs."""
from S6_SERIES_PUBLISH_c9_backend_notation import Packet
from S6_SERIES_PUBLISH_c9_notation_addendum_io import stage

packets = []
p = Packet('02LT', 'maps:src:D.2.51',
           '2ec11aa93748507f453312bfb868188e646726942c185659c963c5180e8f7c99',
           '417–428', 'Mapping-torus retraction, Euclidean matrix, monodromy covector and Dynkin rank.')
p.scope('mapping-torus-retraction', 'Let $X$ be the unit circle bundle over $N$',
        'It remains to determine the circle-bundle map over the wedge',
        p.literals([(r'$r:X\to E$', r'$r_{\rm ret}:X\to E$', 1),
                    (r'\simeq ir', r'\simeq i r_{\rm ret}', 1),
                    ('H_s=r', r'H_s=r_{\rm ret}', 1), ('H_0=r', r'H_0=r_{\rm ret}', 1),
                    (r'\phi_0r', r'\phi_0 r_{\rm ret}', 2),
                    ('[r(x)', r'[r_{\rm ret}(x)', 1),
                    (r'[r\phi(x)', r'[r_{\rm ret}\phi(x)', 1),
                    (r'\phi ir(x)', r'\phi i r_{\rm ret}(x)', 1)]),
        'r_ret is the same connection-lifted retraction from the unit circle bundle X to its restriction E over K. Identity on X and E preserves every point map, i r_ret and R_s. The map of mapping tori uses the identical path H_s=r_ret phi R_s and the identical two pieces; the midpoint and endpoint identities and both displayed inverse-composite homotopies are unchanged. The inverse here is at the stated homotopy scope, through inclusion, without asserting that the retraction is a bijection. The positive roof is already varrho(p), retained with its increasing inverse tau_p.')
p.exact('euclidean-basis-matrix',
        r''' E=\begin{pmatrix}s&-b/d\\t&a/d\end{pmatrix},\qquad
 E^{-1}=\begin{pmatrix}a/d&b/d\\-t&s\end{pmatrix}.''',
        r''' E_{\rm Bez}=\begin{pmatrix}s&-b/d\\t&a/d\end{pmatrix},\qquad
 E_{\rm Bez}^{-1}=\begin{pmatrix}a/d&b/d\\-t&s\end{pmatrix}.''',
        'E_Bez is exactly the displayed elementary automorphism of the same ordered Z^2 columns. Its entries are unchanged; multiplying the two displayed matrices gives diag((sa+tb)/d,(sa+tb)/d)=I since sa+tb=d. It therefore gives the same products V and V^(-1), row kernel basis and inverse coordinates. The earlier E remains the actual restricted unit circle bundle throughout its mapping-torus construction.')
p.scope('scalar-monodromy-row', 'This also determines the scalar entry of the full monodromy',
        'The equation $(B-I)z=q$ now shows directly',
        p.literals([('       r&1&', r'       r_{\rm mon}&1&', 1),
                    (r'\alpha-rz', r'\alpha-r_{\rm mon}z', 1),
                    (r'\alpha=rz', r'\alpha=r_{\rm mon}z', 1)]),
        'r_mon is the same integral covector obtained by including the ordered elliptic two-plane into the domain of A and then projecting A to the scalar delta coordinate. That coordinate definition is the displayed row of the unchanged block matrix. On the lifted vector (-q_0 z,0,q_0), its scalar displacement is still q_0(alpha-r_mon z)delta, the same winding/Chern pairing. Thus alpha=r_mon z is the identical conclusion and the following fixed-vector computation is unchanged. The generic row argument r of the Euclidean basis algorithm retains its formal input role.')
p.scope('dynkin-rank', 'Use the affine $D_r$ diagram with $r=n+4$',
        'For $n=1$ its tuple is',
        p.literals([('$D_r$', r'$D_{r_{\rm Dyn}}$', 1), ('$r=n+4$', r'$r_{\rm Dyn}=n+4$', 1),
                    ('$r-2$', r'$r_{\rm Dyn}-2$', 2), ('$r-1,r$', r'$r_{\rm Dyn}-1,r_{\rm Dyn}$', 1),
                    (r'$(0\,1)(r-1\,r)$', r'$(0\,1)(r_{\rm Dyn}-1\,r_{\rm Dyn})$', 1),
                    (r'p=(0,1,r-1,r,2,3,\ldots,r-2)', r'p=(0,1,r_{\rm Dyn}-1,r_{\rm Dyn},2,3,\ldots,r_{\rm Dyn}-2)', 1)]),
        'r_Dyn is the same integer n+4 for the two stated values n=1,3. Identity on each vertex label preserves the affine D diagram, all intersection entries, the return transposition and c=e_0+e_1-e_2. The outer-first-to-chain index tuple has precisely the same integers after substitution; both explicit inverse tuples and the basis-permutation matrix P remain unchanged. This rank has a persistent name distinct from the generic integer-row argument and actual retraction.')
packets.append(p)

p = Packet('02LV', 'maps:src:D.2.53',
           'bda4d153773bd96b19a02d9f6cbab808111279d4823442cf250da94607e5fcb0',
           '534–550', 'Transverse period, marked Laurent generators and fixed-curve generator.',
           image_reader='root')
p.scope('transverse-elliptic-period', 'For the second rank-one site take the transverse elliptic period',
        'Let $T_i(v)$ be the marked monodromy prism',
        p.literals([('$r=e_1$', r'$r_{\rm per}=e_1$', 1),
                    ('$r=e_2$', r"$r_{\rm per}'=e_2$", 1),
                    (r'\det(2e_1-e_2,r)', r'\det(2e_1-e_2,r_{\rm per})', 1)]),
        'r_per is exactly e_1 at the second rank-one site and r_per-prime exactly e_2 at the third. The identity of each elliptic lattice vector preserves det(2e_1-e_2,r_per)=1 and each oriented transverse torus. The fixed long period gamma-8e_1, nodal specialization and all four integral rows remain unchanged. The component label r in Z/8 and the integer support argument r retain their explicit quotient/remainder relationship; the two selected period vectors now also have distinct printed names.')
p.scope('annular-group-ring-generators', 'The short-long marking also follows from the annulus map',
        r'\medskip\noindent\emph{Extension through the other caps.}',
        p.literals([('S_x', r'S_{x_{\rm gr}}', 4), ('S_y', r'S_{y_{\rm gr}}', 4),
                    ('x^py^q', r'x_{\rm gr}^p y_{\rm gr}^q', 1),
                    ('(x-1)', r'(x_{\rm gr}-1)', 3), ('(y-1)', r'(y_{\rm gr}-1)', 3),
                    ('x^{-1}', r'x_{\rm gr}^{-1}', 3), ('x^{-2}', r'x_{\rm gr}^{-2}', 1),
                    ('y^{-1}', r'y_{\rm gr}^{-1}', 3), ('y^{-2}', r'y_{\rm gr}^{-2}', 1),
                    (r'\(x\)', r'\(x_{\rm gr}\)', 1), (r'\(y\)', r'\(y_{\rm gr}\)', 1)]),
        'The exact Laurent-ring isomorphism sends x to x_gr and y to y_gr, with inverse x_gr to x and y_gr to y, and fixes integers and the module basis E_1,E_2,E_3. It sends S_x,S_y to their renamed images and carries the augmentation-ideal-square basis, all three Picard columns and the Hilbert--Burch relation entry for entry. The action is still translation by (-1,0) for x_gr and (0,1) for y_gr on the positive component labels. Thus the actual marked annulus map, angular exponents, integer matrix (9,24;0,0) and path-independence argument are unchanged. The global cohomology class y and later fixed-curve generator have their own names.')
p.scope('fixed-curve-generator-binding', 'Since $X$ is simply connected, both $u$ and $y$ have circle-equivariant',
        'The ordinary degrees and fibre characters have the following formulas.',
        p.literals([('$x$', r'$x_C$', 2), ('d_{r,s}x+', 'd_{r,s}x_C+', 1)]),
        'x_C is the identical positive generator on each C_(r,s), characterized by integral evaluation one on its complex orientation. This characterization identifies H^2(C_(r,s);Z) with Z by evaluation; the inverse sends n to n x_C. The same class appears in the restriction d_(r,s)x_C+lambda_(r,s)t, while the global y still has zero ordinary curve restriction. The equivariant lifts and their character changes are preserved.')
p.scope('fixed-curve-localization-generator', r'Each restriction of $\widehat u$ in \eqref{maps:eq:D.OL4}',
        r'The representatives \eqref{maps:eq:D.OL6}',
        p.literals([('(d x+', '(d x_C+', 1), ('(-x+t)(-x-t)', '(-x_C+t)(-x_C-t)', 1),
                    ('coefficient of $x$', 'coefficient of $x_C$', 1)]),
        'This is the same positive curve generator x_C bound in the preceding restriction formula. Identity on integral cohomology and all its coefficient reductions preserves Thomas degree-four operation, both equivariant normal roots and the Euler class -t^2. Taking the coefficient of x_C is the original integral over the oriented curve. The actual localized inverse sum and all three finite-coefficient evaluations retain every value and modulus.')
p.exact('integral-fixed-curve-roots',
        r'''sixteen fixed curves let $x$ be its positive generator.  The tangent and normal data give roots
$2x,-x+t,-x-t$, with $x^2=0$.''',
        r'''sixteen fixed curves let $x_C$ be its positive generator.  The tangent and normal data give roots
$2x_C,-x_C+t,-x_C-t$, with $x_C^2=0$.''',
        'The same sixteen curves and their complex orientations again give x_C by evaluation one. Their tangent and normal roots are the same classes 2x_C,-x_C+t,-x_C-t, so the integral equivariant Chern and lambda classes are unchanged. The earlier adjoint-representation root x remains a formal splitting-principle argument; the actual analytic chart coordinates x,y,z likewise remain arguments of their explicit coordinate maps and inverses. No named cohomology class is rebound to those formal arguments.')
packets.append(p)

p = Packet('02SB', 'night:P3F.34',
           'b0e4049a0b64a3268ca2e10041eef0c2c5e2927ad5c7f649b699fb1d1b823e05',
           '584–587', 'Final Bezout coefficients and splitting projection versus opening affine vector and boundary class.',
           image_reader='root')
p.scope('zero-sector-bezout-coefficients', r'For \(n=0\), freeness gives',
        'The pair sequence gives',
        p.literals([('a,b with \\(ad+bk=1\\)', r'\(a_{\rm Bez},b_{\rm Bez}\) with \(a_{\rm Bez}d+b_{\rm Bez}k=1\)', 1),
                    (r'\(a(3d\psi)+b(3k\psi)=3\psi\)', r'\(a_{\rm Bez}(3d\psi)+b_{\rm Bez}(3k\psi)=3\psi\)', 1)]),
        'a_Bez,b_Bez are the identical two chosen integers satisfying a_Bez d+b_Bez k=1. The identity on this ordered integer pair preserves the combination of transfer columns yielding 3 psi, its image lattice and cokernel. The opening a remains the actual affine root-gluing vector throughout U,R and their full inverse formulas. The new integer names are explicitly mathematical names, including their prose introduction.')
p.scope('zero-sector-splitting-projection', 'The pair sequence gives',
        r'Thus \(H_2(X)=\mathbb Z^2\oplus\mathbb Z/3\).',
        p.literals([(r'\xrightarrow{p}', r'\xrightarrow{p_{\rm spl}}', 1),
                    ('p(z)', r'p_{\rm spl}(z)', 1), ('p(x)', r'p_{\rm spl}(x)', 2)]),
        'p_spl is the same surjection H_2(X) to Z in the displayed pair sequence, now distinct from the previously named boundary cohomology class p. The chosen z has the same value p_spl(z)=1. The maps (c,r) to i(c)+rz and x to (i^(-1)(x-p_spl(x)z),p_spl(x)) retain every point and still have both identity composites by exactness and this chosen value. The formal input variables c,r,x and injection i retain their original roles.')
packets.append(p)

stage(packets, 'S6_SERIES_PUBLISH_c9_geometric_role_addenda',
      'continuation9_geometric_role_addenda', 'retained-geometric-role-readback',
      'Each identity is stated at the actual lattice, bundle, ring, cohomology or mapping-torus domain; the existing forward and inverse constructions are unchanged.')
