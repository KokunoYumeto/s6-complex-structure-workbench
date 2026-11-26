#!/usr/bin/env python3
"""Complete free-cap homology proof: exact root, class and transfer names."""
from S6_SERIES_PUBLISH_c9_backend_notation import Packet

p = Packet("02SB", "night:P3F.34", "78b45526624ef533141dcc387cd4bb6a8e593dda76b5cf5a8b27cf62f2196c17", "584–587",
           "This agent read all 298 source lines; root read the actual page images. Traced the gcd and affine root generator through quotient/power relations, the boundary cohomology basis through exterior restriction and transfer, both Smith arguments and all homology groups. Prepared reversible names and explicit math-mode references without changing the clockwise Thom signs or any map.",
           image_reader="root (this agent's contribution is the full source-context review)")

root_reason = ("g_root=g is the same affine root map (z,s)↦(Az+ell/m,exp(-2pi i/m)s), with inverse (z',s')↦(A^{-1}(z'-ell/m),exp(2pi i/m)s'). Its restriction to the central torus, quotient action, m-th-power relation and positive/clockwise meridian images are unchanged. The integer g=gcd(m,n,3d), its divisibility, Smith entries and homology groups retain their original name.")
p.exact("root-generator-definition",
        r" g(z,s)=(Az+\ell/m,e^{-2\pi i/m}s),\qquad",
        r" g_{\rm root}(z,s)=(Az+\ell/m,e^{-2\pi i/m}s),\qquad", root_reason)
p.exact("root-meridian-images",
        r"""The positive exterior meridian maps to \(g^{-1}\), and
\(\alpha\) maps to g.""",
        r"""The positive exterior meridian maps to \(g_{\rm root}^{-1}\), and
\(\alpha\) maps to \(g_{\rm root}\).""", root_reason)
p.exact("central-root-quotient",
        r"\(B=B_{m,n,d}=T^4/\langle g\rangle\).",
        r"\(B=B_{m,n,d}=T^4/\langle g_{\rm root}\rangle\).", root_reason)
p.exact("root-power-relation",
        r"Abelianizing \(g^m=\ell\) and the conjugation relations gives",
        r"Abelianizing \(g_{\rm root}^{\,m}=\ell\) and the conjugation relations gives", root_reason)

p.scope("dual-transfer-columns", "In this explicit exterior basis", "The primitive normal",
        p.literals([("v_1", r"v_1^{\rm tr}", 2), ("v_2", r"v_2^{\rm tr}", 2)]),
        "v_1^tr=v_1=(3d,-n,0) and v_2^tr=v_2=(m,0,n) are the same two transfer columns in the primitive lattice L_{m,n,d}. The identity on Z³ and its restricted inverse fix every entry, the cross product n(-n,-3d,m), primitive normal, index and both Smith factors. The boundary cohomology class v_2=(psi+u)w retains its existing name and zero-transfer identity.")

class_reason = ("The words u2 and v2 refer to the already defined boundary classes u_2=psi h and v_2=(psi+u)w in H²(E). The identity on that integral basis preserves the projection modulo v_2, exterior basis change M^{-1}, unit (u_2,p) minor and zero transfer of v_2. Explicit math-mode subscripts carry the same class names into each prose use; no formula, coefficient or basis changes.")
p.exact("boundary-class-modulus",
        "Project two exterior restriction basis vectors modulo v2 to",
        r"Project two exterior restriction basis vectors modulo \(v_2\) to", class_reason)
p.exact("unit-minor-class-names",
        "cross product vanish and their u2,p minor is the unit epsilon.",
        r"cross product vanish and their \((u_2,p)\) minor is the unit \(\varepsilon\).", class_reason)
p.exact("exterior-restriction-class-names",
        "inverse multiplies by M. Their restrictions are u2,p modulo\nmultiples of v2, whose transfer is zero.",
        r"""inverse multiplies by M. Their restrictions are \(u_2,p\) modulo
multiples of \(v_2\), whose transfer is zero.""", class_reason)
p.exact("final-homology-group-name",
        "integral duality identifies its torsion with that of H2.",
        r"integral duality identifies its torsion with that of \(H_2(X)\).",
        "The immediately preceding paragraph computes H_2(X)=Z²⊕Z/3 and then H_3(X); the final plain H2 refers to that same stated homology group. Printing H_2(X) in math mode retains the exact integral-duality assertion and its torsion group.")

p.finish()
