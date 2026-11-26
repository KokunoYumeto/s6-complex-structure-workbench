#!/usr/bin/env python3
"""Complete order-three proof: scoped notation and exact reverse comparison."""
from S6_SERIES_PUBLISH_c9_backend_notation import Packet

p = Packet("02LF", "maps:src:D.2.39", "79695bb4b6ede15a0b81b8e47aaec6c6e8cf5d19222236fa66465d928f2a9374", "474–483",
           "Read the complete integral graph, original/finite/rank-one/cusp cap maps, affine conjugacies, period charts, doubled line, Borel character comparison, coefficient-one operation, C9 localization and surgery recognition. Traced both finite sweeps into the later cohomology comparison and each nodal pairing entry through its support and character uses.")

sweep_reason = ("D_delta=D=t(delta) and L_ell=L=t(ell) are the same fixed boundary sweeps. Identity on the ordered exterior coordinates (s,D_delta,L_ell) preserves all three Thom columns, every Bezout substitution and the quotient equations D_delta=-be s and L_ell=0. The later Borel comparison uses those same equations. The graph differential D and long period basis L retain their original names and maps.")
p.scope("finite-boundary-sweeps", r"Writing $D=t(\delta)$", "The two zero-dimensional toric strata",
        p.symbols([("D", r"D_\delta"), ("L", r"L_\ell")]), sweep_reason)
p.exact("borel-sweep-import",
        r"$H_2(X;\mathbb F_3)$: for a finite cap $L=0$ and $D=-be\,s=0$,",
        r"$H_2(X;\mathbb F_3)$: for a finite cap $L_\ell=0$ and $D_\delta=-be\,s=0$,",
        sweep_reason)
p.exact("free-abelian-chern-group",
        r"in the free group $H^2(F;\mathbb Z)$, so this class is zero.",
        r"in the free abelian group $H^2(F;\mathbb Z)$, so this class is zero.",
        "The preceding integral H_1(F), H_2(F) and universal coefficient description gives the displayed additive integral cohomology group. Its given commuting addition and basis are unchanged by the identity map. Adding abelian states that structure and retains the torsion-Chern-class argument.")

pairing_reason = ("n_per=N=a nu/d_0² and r_per=R=-b d_0²/nu are the same two diagonal entries of the exact pairing K_N=(SC_S)^t omega(LC_L). Identity on these integers and on every basis column preserves K_N, the support, base-return exponent, specialized I_3 values and line character. K_N and G_N keep their nodal names; the physical holomorphic factor R, later coefficient ring and tubular neighborhood are named separately.")
p.exact("nodal-pairing-entries",
        r""" K_N=(SC_S)^t\omega(LC_L)=\begin{pmatrix}N&0\\M&R\end{pmatrix},
 \quad N=a\nu/d_0^2,\quad R=-bd_0^2/\nu,\quad""",
        r""" K_N=(SC_S)^t\omega(LC_L)=\begin{pmatrix}n_{\rm per}&0\\M&r_{\rm per}\end{pmatrix},
 \quad n_{\rm per}=a\nu/d_0^2,\quad r_{\rm per}=-bd_0^2/\nu,\quad""", pairing_reason)
p.exact("i3-pairing-specialization",
        r"site, where $d_0=1$, $n_0=3$, $N=3a$, and $R=-b/3$.",
        r"site, where $d_0=1$, $n_0=3$, $n_{\rm per}=3a$, and $r_{\rm per}=-b/3$.", pairing_reason)
p.exact("nodal-support",
        r"The integral support $Nj^2$ has difference $2Nhj+Nh^2$, giving",
        r"The integral support $n_{\rm per}j^2$ has difference $2n_{\rm per}hj+n_{\rm per}h^2$, giving", pairing_reason)
p.exact("nodal-base-exponent",
        r"both add $NW_1^2$ to the exponent",
        r"both add $n_{\rm per}W_1^2$ to the exponent", pairing_reason)
p.exact("physical-support-pairing",
        r"          =-Nj^2+N\alpha_0j.",
        r"          =-n_{\rm per}j^2+n_{\rm per}\alpha_0j.", pairing_reason)
p.exact("i3-line-character",
        r"The local character is $-\sigma N(2j+1)$, divisible by three.",
        r"The local character is $-\sigma n_{\rm per}(2j+1)$, divisible by three.", pairing_reason)

p.scope("real-short-coordinate", "For the holomorphic comparison put", r"\item \emph{The global Borel class",
        p.literals([("U", r"u_{\rm per}", 8)]),
        "u_per=U is the same real short-coordinate column in R². The identity (U,W)↦(u_per,W), with inverse identity, preserves Z, the physical/nodal/cusp Gaussian exponents and the two base-return substitutions. Every complete period matrix and reciprocal inverse gauge remains unchanged. The later U in H²_{S¹}(X;F_3) remains the Borel class throughout its restrictions and coefficient-one detector.")

p.scope("localization-ring-and-tubes", r"Let $U_9$ be the restriction", "The normal roots on $C_0$",
        p.symbols([("R", r"R_9"), ("N", r"N_{\rm tub}")]),
        "R_9=R=Z/9 is the identical coefficient ring via [j]↦[j], preserving sums, products, every cohomology coefficient and the localized Thom inverse. N_tub=N is the same union of the two chosen invariant tubular discs, with the same inclusion into X and boundary inclusion. Identity on those spaces preserves the relative/excision maps and every induced action. The earlier physical contraction R, pairing entries and site count keep their stated domains.")

p.finish()
