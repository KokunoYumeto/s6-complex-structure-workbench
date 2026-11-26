"""Exact semantic and notation contexts from the complete edited LD reading."""
from S6_SERIES_PUBLISH_c8_foundations_editing import Editor


def main():
    e = Editor("weighted_natural_profiles", "C8-FND-WEIGHTED-PROFILES-FOLLOW-")
    e.replace("Let $L$ count the nonzero-Chern originals. Define $\\beta$ by\n",
              "At a multiplicative site write its type as $I_{n_i}$.\nLet $L$ count the nonzero-Chern originals. Define $\\beta$ by\n",
              "D05", "mapsIII:def:weighted-natural-data",
              "Define the multiplicative component index n_i before its two uses in the relocated component-count definition; its original Kodaira meaning is unchanged.")
    e.replace("The defining component coordinate and the positive Tate indexing\nare related by the exact map\n",
              "Write $\\kappa_{\\mathrm c}$ for the defining component coordinate\nof $G$ at $I_\\nu$. This coordinate and the positive Tate indexing\nare related by the exact map\n",
              "D05", "maps:src:D.2.37",
              "Restore the local component-coordinate name after its duplicate natural-row enumeration was moved to KX; preserve the complete residue morphism and inverse.")
    e.replace("Theorem~\\ref{maps:src:D.2.32}--Theorem~\\ref{maps:src:D.2.33}.\n",
              "Theorems~\\ref{maps:src:D.2.32} and~\\ref{maps:src:D.2.33}.\n",
              "D04", "maps:src:D.2.37",
              "Print the two exact original-cap owners as a plural theorem reference rather than an awkward repeated-kind range.")
    e.replace(r" H_j(N_d;\mathbb Z)=" + "\n",
              r" H_*(N_d;\mathbb Z)=" + "\n",
              "D20", "maps:src:D.2.37",
              "Use the graded-group symbol for the displayed full seven-degree tuple; every group and its order are unchanged.")
    e.replace(r" P_dH_d=H_dP_1,\qquad P_d=N_h(A(d))/h ." + "\n",
              r" \Pi_dH_d=H_d\Pi_1,\qquad \Pi_d=N_h(A(d))/h ." + "\n",
              "D20", "maps:src:D.2.37",
              "Distinguish the four-dimensional finite fixed-plane projection Pi_d from the exterior graph projector P_d. Identity on each displayed projection matrix is the renaming map and inverse.")
    old = "This comparison extends on the good-reduction root\ndisc. Let R be the finite deck operator on holomorphic Lie\nsections, \\(R^m=I\\). After matching the same integral power,\nthe difference \\(b_0\\) of two affine lifts satisfies \\(Nb_0=0\\).\nSet\n\\[\n h_0=-\\frac1m\\sum_{j=0}^{m-1}jR^j b_0.\n\\]\nThe identity \\((I-R)\\sum jR^j=N-mI\\) gives\n\\((I-R)h_0=b_0\\). Translation by \\(h_0\\) and by -\\(h_0\\) are\ninverse holomorphic maps across the centre. A universal\nlift change by a period \\(\\lambda\\) changes the power by \\(N_m\\lambda\\). This is the exact norm convention used here.\n"
    new = r"""Use the finite-operator identity proved in
Theorem~\ref{maps:src:D.2.29} on the good-reduction root disc.
Here its operator is the finite deck operator $R$ on holomorphic
Lie sections, with $R^m=I$, and its zero-norm section is the
difference $b_0$ of two lifts with the same integral power.
Identity on $R,m,b_0$ and the root coordinate identifies the
equations and their inverse translation. Explicitly,
\[
 h_0=-\frac1m\sum_{j=0}^{m-1}jR^j b_0,\qquad
 (I-R)h_0=b_0.
\]
Translation by $h_0$, inverted by translation by $-h_0$,
extends across the centre. A period change $\lambda$ changes
the power by $N_m\lambda$, with inverse subtraction.
"""
    e.replace(old, new, "D12", "maps:src:D.2.37",
              "Use the earlier proof of the abstract finite-operator identity with the exact R,m,b0 hypotheses, preserving the complete holomorphic map, inverse and norm lift. This reuse makes no additional family identification.")
    e.replace("Let \\(\\mathcal P\\) use all five finite-good types II, III, IV,\n",
              "In $\\mathcal P$ of Definition~\\ref{mapsIII:def:weighted-natural-data},\nlabel all five finite-good types II, III, IV,\n",
              "D12", "maps:src:D.2.37",
              "Use the numbered cap-pattern definition when introducing its O/F/M labels for the exhaustive proof, retaining all site options.")
    e.replace("Let \\(\\mathcal P_{\\mathrm{all\\ star\\ O}}\\) be the subset with\nO at \\(\\mathrm{III}^*\\) and \\(\\mathrm{IV}^*\\) as well. Its inclusion j keeps every site\n",
              "For $\\mathcal P_{\\mathrm{all\\ star\\ O}}$ of that definition,\nthe inclusion $j$ keeps every site\n",
              "D12", "maps:src:D.2.37",
              "Use the single defined all-star-original subset and retain the exact inclusion, projection and composite identities in the proof.")

    # These are the actual prose contexts read in full above. No global
    # token substitution is used; every old string has a unique guard.
    typography = [
        ("In a line frame with multiplier u(x), its multiplier is the ordered\nproduct of u over the first d translates.", "In a line frame with multiplier $u(x)$, its multiplier is the ordered\nproduct of $u$ over the first $d$ translates."),
        ("The d disjoint local inverse branches are the lifts to the d chosen\n", "The $d$ disjoint local inverse branches are the lifts to the $d$ chosen\n"),
        ("A positively oriented weight-d suspension period is d old suspension\nperiods.", "A positive suspension period at weight $d$ consists of $d$ original\nsuspension periods."),
        ("(0,0,0,1), \\eqref{maps:eq:D.WP2} multiplies precisely", "$(0,0,0,1)$, \\eqref{maps:eq:D.WP2} multiplies precisely"),
        ("\\(\\gamma\\) column by d and leaves all other entries unchanged. It is\nintegral for every d.", "\\(\\gamma\\) column by $d$ and leaves all other entries unchanged. It is\nintegral for every $d$."),
        ("The forward arrow covers minus Q and has Tate valuation\nb \\(\\kappa\\); hence P has Tate component", "The forward arrow covers $-Q$ and has Tate valuation\n$b\\kappa$; hence $P$ has Tate component"),
        ("Let \\(L_d\\) multiply each nongamma domain column by d and leave each\n", "Let \\(L_d\\) multiply each nongamma domain column by $d$ and leave each\n"),
        ("This is an all-d integer right inverse.", "This is an integer right inverse for every permitted $d$."),
        ("The coefficients depend linearly on d.", "The coefficients depend linearly on $d$."),
        ("\\(n\\gamma+k\\delta\\); changing k by a changes this representative\n", "\\(n\\gamma+k\\delta\\); changing $k$ by $a$ changes this representative\n"),
        ("coordinates and the last coordinate divided by a on the image.", "coordinates and the last coordinate divided by $a$ on the image."),
        ("\\(\\delta\\)-\\(\\gamma\\) coordinate is divisible by a, so this is also the\n", "\\(\\delta\\)-\\(\\gamma\\) coordinate is divisible by $a$, so this is also the\n"),
        ("Retract the punctured base onto the ordered bouquet of N-1 loops.", "Retract the punctured base onto the ordered bouquet of $N-1$ loops."),
        ("has image K. A Hermite basis of that image gives an integral\nbasis of K.", "has image $K$. A Hermite basis of that image gives an integral\nbasis of $K$."),
        ("basis vector of K by the corresponding loop cylinders", "basis vector of $K$ by the corresponding loop cylinders"),
        ("The edge projection reads the K coordinate;", "The edge projection reads the $K$ coordinate;"),
        ("The d-period subgroup in this fan marking is generated\nby the first original period and d times the second. The\nnormalization of its cusp \\(N_d\\) therefore has d toric degree-six\n", "The period subgroup at weight $d$ in this fan marking is generated\nby the first original period and $d$ times the second. The\nnormalization of its cusp \\(N_d\\) therefore has $d$ toric degree-six\n"),
        ("is exactly \\(\\ker Q\\). Substitution verifies these polynomial identities for every d.", "is exactly \\(\\ker Q\\). Substitution verifies these polynomial identities for every $d$."),
        ("The d normal component discs all have boundary equal to the\n", "The $d$ normal component discs all have boundary equal to the\n"),
        ("is the sum of the d coordinates times that meridian.", "is the sum of the $d$ coordinates times that meridian."),
        ("cover: their fundamental loops lie in S and have \\(\\gamma\\) coordinate\nzero. Applying the integral inverse of C to the fan short\nthimbles gives the physical short directions u and \\(\\delta\\);\nthe inverse C transports the fan thimbles to both physical directions.", "cover: their fundamental loops lie in $S$ and have \\(\\gamma\\) coordinate\nzero. Applying $C^{-1}$ to the fan short thimbles gives the physical\nshort directions $u$ and \\(\\delta\\); multiplication by $C$ is the\ninverse coordinate map."),
        ("This is a primitive rank-two sublattice. The short lattice S is\n", "This is a primitive rank-two sublattice. The short lattice $S$ is\n"),
        ("and for a last site its final block is minus the identity on S.", "and for a last site its final block is minus the identity on $S$."),
        ("Let q be the order of G in the component group of a zero-Chern\noriginal additive site. P narrow says \\(q\\mid a\\). Since\n\\(\\gcd(a,b)=1\\), b is a unit modulo q; and", "Let $q$ be the order of $G$ in the component group of a zero-Chern\noriginal additive site. Narrow $P$ gives \\(q\\mid a\\). Since\n\\(\\gcd(a,b)=1\\), $b$ is a unit modulo $q$; and"),
        ("of the forward arrow \\(-Q\\). Its order is q, with each component\norbit length dividing q. Choose a positive E such that", "of the forward arrow \\(-Q\\). Its order is $q$, with each component\norbit length dividing $q$. Choose a positive $E$ such that"),
        ("Their index parametrizations are related by multiplication by d\nand the inverse multiplication by E modulo the orbit length.", "Their index parametrizations are related by multiplication by $d$\nand the inverse multiplication by $E$ modulo the orbit length."),
        ("\\(\\kappa_{\\mathrm{c}}\\) is a unit modulo \\(\\nu\\). P narrow gives", "\\(\\kappa_{\\mathrm{c}}\\) is a unit modulo \\(\\nu\\). Narrow $P$ gives"),
        ("unchanged line bundle is unchanged. Q was narrow, so dQ is narrow\n", "unchanged line bundle is unchanged. The section $Q$ is narrow, so $dQ$ is narrow\n"),
        ("Raising the component permutation to its dth power gives these\n", "Raising the component permutation to its $d$th power gives these\n"),
        ("\\(g_0\\) because d is coprime to \\(g_0\\).", "\\(g_0\\) because $d$ is coprime to \\(g_0\\)."),
        ("roofs on the d translates; the positive-roof map", "roofs on the $d$ translates; the positive-roof map"),
        ("as at weight one. The component-group order q divides a.\nThe orbit of the outer component met by O has q\n", "as at weight one. The component-group order $q$ divides $a$.\nThe orbit of the outer component met by $O$ has $q$\n"),
        ("The forward basis change replaces \\(U_1\\) by W. Its inverse", "The forward basis change replaces \\(U_1\\) by $W$. Its inverse"),
        ("An inverse section sends W to\n", "An inverse section sends $W$ to\n"),
        ("extending line-circle tube and the q-fold orbit tube closed", "extending line-circle tube and the $q$-fold orbit tube closed"),
        ("count is q, and its angular unit is the extending", "count is $q$, and its angular unit is the extending"),
        ("Raising these permutations to the dth power and using the inverse", "Raising these permutations to the $d$th power and using the inverse"),
        ("Now q divides b and \\(\\gcd(a,q)=1\\). The line Chern vector on\nthe Kodaira neighbourhood N is", "Now $q$ divides $b$ and \\(\\gcd(a,q)=1\\). The line Chern vector on\nthe Kodaira neighbourhood $N$ is"),
        ("components have multiplicity one. Since dQ is narrow,\nthe original logarithm of Q gives the logarithm\nd times that section.", "components have multiplicity one. Since $dQ$ is narrow,\nthe original logarithm of $Q$, multiplied by $d$, is a logarithm\nof that section."),
        ("gauge of Theorem~\\ref{maps:src:D.2.32}, and compose its endpoint isotopy\nd times.", "gauge of Theorem~\\ref{maps:src:D.2.32}, and compose its endpoint isotopy\n$d$ times."),
        ("The original cap sends \\(e_{12}\\) to F and \\(k_d\\) to zero.", "The original cap sends \\(e_{12}\\) to $F$ and \\(k_d\\) to zero."),
        ("local boundary images are primitive for every d.", "local boundary images are primitive for every $d$."),
        ("The Tate component of P is \\(-a\\kappa\\bmod\\nu\\),", "The Tate component of $P$ is \\(-a\\kappa\\bmod\\nu\\),"),
        ("The marked geometric normal torus of u can have a rim", "The marked geometric normal torus of $u$ can have a rim"),
        ("For P narrow, \\(\\nu\\mid a\\) and the physical short vector", "For narrow $P$, \\(\\nu\\mid a\\) and the physical short vector"),
        ("Choose integers x,y with \\(\\nu x+db\\kappa y=1\\).", "Choose integers $x,y$ with \\(\\nu x+db\\kappa y=1\\)."),
        ("For P non-narrow the primitive vector is instead", "For non-narrow $P$ the primitive vector is instead"),
        ("316 have narrow P and 120 have non-narrow P.", "316 have narrow $P$ and 120 have non-narrow $P$."),
        ("orders h are respectively 6,4,3,4,3.", "orders $h$ are respectively $6,4,3,4,3$."),
        ("Let \\(A=A_i(d)\\), let F be any primitive integral basis of", "Let \\(A=A_i(d)\\), let $F$ be any primitive integral basis of"),
        ("Its image lies in \\(\\Lambda^A\\). Let H be an integral basis", "Its image lies in \\(\\Lambda^A\\). Let $H$ be an integral basis"),
        ("The definition of H makes Q surjective.", "The definition of $H$ makes $Q$ surjective."),
        ("Thus the displayed projection, the Q coordinates, and", "Thus the displayed projection, the $Q$ coordinates, and"),
        ("difference of its translation and v/m lies in", "difference of its translation and $v/m$ lies in"),
        ("The moving plane of A has a primitive h-th root pair as", "The moving plane of $A$ has a primitive $h$th-root pair as"),
        ("\\(\\ker P\\) whenever h does not divide j.", "\\(\\ker P\\) whenever $h$ does not divide $j$."),
        ("For necessity apply P to the equation.", "For necessity apply $P$ to the equation."),
        ("of m/t.\n", "of $m/t$.\n"),
        ("For \\(u>1\\) the power m/u\n", "For \\(u>1\\) the power $m/u$\n"),
        ("by h has identity linear part and nonintegral translation.\nAll remaining obstruction indices are divisible by h\n", "by $h$ has identity linear part and nonintegral translation.\nAll remaining obstruction indices are divisible by $h$\n"),
        ("Here q is the component-group order.", "Here $q$ is the component-group order."),
        ("q & \\(g_0\\) & Positions", "$q$ & \\(g_0\\) & Positions"),
        ("unimodular matrix V, giving the coordinate maps", "unimodular matrix $V$, giving the coordinate maps"),
        ("\\(w_\\epsilon\\mapsto V^{-1}w_\\epsilon\\) and its inverse V.", "\\(w_\\epsilon\\mapsto V^{-1}w_\\epsilon\\) and its inverse $V$."),
        ("lattice for every permitted d.~Its", "lattice for every permitted $d$. Its"),
        ("The kernel of Q is the image of", "The kernel of $Q$ is the image of"),
        ("\\(\\Lambda\\) and c, relations", "\\(\\Lambda\\) and $c$, relations"),
        ("generator is this primitive vector modulo its t-fold\n", "generator is this primitive vector modulo its $t$-fold\n"),
        ("The root normal character is zero on \\(\\Lambda\\) and 1/m\non c.~Its value on that torsion generator is 1/t.", "The root normal character is zero on \\(\\Lambda\\) and $1/m$\non $c$. Its value on that torsion generator is $1/t$."),
        ("therefore that class has exact order t and no free", "therefore that class has exact order $t$ and no free"),
        ("The torsion identification sends a coordinate k to the", "The torsion identification sends a coordinate $k$ to the"),
        ("The normal disk bundle U retracts onto \\(F_0\\). Its boundary\nis identified with the mapping torus of A by", "The normal disk bundle $U$ retracts onto \\(F_0\\). Its boundary\nis identified with the mapping torus of $A$ by"),
        ("m root sectors. Its positive fixed sweep", "$m$ root sectors. Its positive fixed sweep"),
        ("the sectors along their marked A-edges is the inverse\nchain map. For the core loop c, use", "the sectors along their marked $A$-edges is the inverse\nchain map. For the core loop $c$, use"),
        ("Its fixed sweep is v and its vertical area is zero.", "Its fixed sweep is $v$ and its vertical area is zero."),
        ("invariance of \\(\\omega_d\\) with Av=v", "invariance of \\(\\omega_d\\) with $Av=v$"),
        ("generate that full integral relation lattice. The Q\n", "generate that full integral relation lattice. The $Q$\n"),
        ("by v/m, and its every-power freeness is exactly", "by $v/m$, and its every-power freeness is exactly"),
        ("This proves the clutch convention for every e,", "This proves the clutch convention for every $e$,"),
        ("\\(\\lambda\\) changes v to", "\\(\\lambda\\) changes $v$ to"),
        ("Form the graph kernel K in", "Form the graph kernel $K$ in"),
        ("the projector following it. Form B with", "the projector following it. Form $B$ with"),
        ("Attach the k finite or regular logarithmic caps to V and call the\nresult E.", "Attach the $k$ finite or regular logarithmic caps to $V$ and call the\nresult $E$."),
        ("namely Z. Write \\(x_i\\) for the positive base meridian at site i.", "namely $\\mathbb Z$. Write \\(x_i\\) for the positive base meridian at site $i$."),
        ("and this is free. The free ranks are d at the cusp,", "and this is free. The free ranks are $d$ at the cusp,"),
        ("images at site j generate exactly", "images at site $j$ generate exactly"),
        ("An explicit kernel algorithm retains \\(H_1(E)\\)'s torsion: if P is its\ninteger power-relation matrix in the omitted-edge coordinates and\nM the displayed component-disc\nboundary matrix, solve", "An explicit kernel algorithm retains \\(H_1(E)\\)'s torsion. Let $P$ be its\ninteger power-relation matrix in the omitted-edge coordinates and\n$M$ the displayed component-disc boundary matrix. Solve"),
        ("integer kernel of \\([M,-P]\\) to z. The columns of P are independent", "integer kernel of \\([M,-P]\\) to $z$. The columns of $P$ are independent"),
        ("z' and an integral chain in E. Gluing", "$z'$ and an integral chain in $E$. Gluing"),
        ("remaining exterior class modulo B.", "remaining exterior class modulo $B$."),
        ("conjugations is the same vertical subgroup for all d:", "conjugations is the same vertical subgroup for all $d$:"),
        ("On 170 rows those words give two elliptic vectors u,v", "On 170 rows those words give two elliptic vectors $u,v$"),
        ("Together with \\(\\delta\\) this kills ker \\(\\chi\\).", "Together with \\(\\delta\\) this kills $\\ker\\chi$."),
        ("the sphere met by P. The circle-bundle Hopf disc", "the sphere met by $P$. The circle-bundle Hopf disc"),
        ("line bundle for every permitted d; only the", "line bundle for every permitted $d$; only the"),
        ("then the remaining return exponent r,", "then the remaining return exponent $r$,"),
        ("construction realizes every integer e.", "construction realizes every integer $e$."),
        ("inverse coordinates. Over the rationals the first s\n", "inverse coordinates. Over the rationals the first $s$\n"),
        ("for every d.~Each added identity site", "for every $d$. Each added identity site"),
        ("At a logarithmic site the full norm is m times the\nfixed-plane projection. For a fixed u,", "At a logarithmic site the full norm is $m$ times the\nfixed-plane projection. For a fixed $u$,"),
        ("s over the rationals, and \\(\\operatorname{rank}C_d=0\\).", "$s$ over the rationals, and \\(\\operatorname{rank}C_d=0\\)."),
        ("of B already constructed.", "of $B$ already constructed."),
        ("and torsion in \\(H_3\\) equal to T. More explicitly, a Smith\ntorsion generator of order n determines", "and torsion in \\(H_3\\) equal to $T$. More explicitly, a Smith\ntorsion generator of order $n$ determines"),
        ("choices, where z\nis the number of those sites.", "choices, where $z$\nis the number of those sites."),
        ("affine power v cannot be zero.", "affine power $v$ cannot be zero."),
        ("Here R is the natural-row count, K the nonzero-Chern\nmultiplicative position count, P the broad pattern\ncount, S the all-star-original subset, and A the\n", "Here $R$ is the natural-row count, $K$ the nonzero-Chern\nmultiplicative position count, $P$ the broad pattern\ncount, $S$ the all-star-original subset, and $A$ the\n"),
    ]
    for old, new in typography:
        e.replace(old, new, "D23", "maps:src:D.2.37",
                  "Typeset the actual variables in this wholly read mathematical context and make the stated coordinate operation legible; all symbols, coefficients, domains and inverse maps retain their original meanings.")
    e.finish()


if __name__ == "__main__":
    main()
