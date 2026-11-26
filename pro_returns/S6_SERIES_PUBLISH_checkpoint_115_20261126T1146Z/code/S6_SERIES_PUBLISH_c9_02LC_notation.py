#!/usr/bin/env python3
"""Scoped source disposition of the complete order-five/seven proof."""
from S6_SERIES_PUBLISH_c9_backend_notation import Packet

p = Packet("02LC", "maps:src:D.2.36", "e5ba652d2f2414ed1f7979585f48e5068d29e1dd027185afd7c00410b5cb9a6c", "445–457",
           "Read the complete statement, all 36 input rows and every cap, period, equivariant-line, Borel, localization, marking and classification argument. Traced the affine action and swept boundary class through their later uses, and the valuation columns through both rank-one and cusp supports. Retained explicitly bound nodal pairing and bordism variables.")

affine_reason = ("R_aff=R is the identical affine torus map x↦T_i x+t_0, with inverse x↦T_i^{-1}(x-t_0); its iterates, norm equation N_m t_0=v and fixed-point equation are unchanged. The physical holomorphic contraction factor R retains its original name throughout the line return F, nodal/cusp units and Tate valuation.")
p.exact("affine-lift-definition",
        r"An affine lift $R(x)=T_i x+t_0$ has",
        r"An affine lift $R_{\rm aff}(x)=T_i x+t_0$ has", affine_reason)
p.exact("affine-lift-fixed-point",
        r"putative fixed point satisfies $x+\delta/p=R^j x$ modulo the",
        r"putative fixed point satisfies $x+\delta/p=R_{\rm aff}^{\,j}x$ modulo the", affine_reason)

p.scope("finite-boundary-sweep", r"$D=t(\delta)$, with relations", "Without a finite site the relation",
        p.symbols([("D", r"D_\delta")]),
        "D_delta=D=t(delta) is the same swept boundary two-cycle. The identity on s and this sweep preserves both displayed relation columns. The elimination map sends D_delta to -be s and retains s; its stated inverse inclusion is unchanged. The later D=diag(a,-b) continues to denote the polarization matrix.")

valuation_reason = ("H_val=H and F_val=F are the same two integral valuation columns in the displayed ordered two-dimensional coordinates. Identity in each coordinate, with the inverse identity, preserves alpha_0 u, beta_0 u, their elliptic combination, and the physical translation differences of the support. The actual line return F(z,v,zeta) and its complete multiplier/inverse keep their existing name.")
p.scope("nodal-valuation-columns", "The physical support can also be retained explicitly.", "At the fixed $I_p$",
        p.symbols([("H", r"H_{\rm val}"), ("F", r"F_{\rm val}")]), valuation_reason)
p.exact("cusp-valuation-columns",
        r"Its physical differences under $H=(\nu,ar)$ and $F=(-br,\rho)$",
        r"Its physical differences under $H_{\rm val}=(\nu,ar)$ and $F_{\rm val}=(-br,\rho)$", valuation_reason)

p.finish()
