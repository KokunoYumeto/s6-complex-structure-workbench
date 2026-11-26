#!/usr/bin/env python3
"""Exact imported normal-bundle name in the full finite-cap return proof."""
from S6_SERIES_PUBLISH_c9_backend_notation import Packet

p = Packet("02S9", "night:P3F.32", "2781d4e9236c4b058929abd3520f157bd50dbf4cf43f12d02c079b7e740008ed", "578–583",
           "This agent read all 430 source lines and the imported 02S8 sphere-bundle definition, tangent identity and meridian-index formula. Root read the actual page images. Coordinated the same B_nu=S(bar nu) name with the 02S8 reader; preserved the explicitly bound cap-angular coordinate B and its full root/deck inverse.",
           image_reader="root (this agent's contribution is the full source-context review)")

p.exact("imported-capped-normal-bundle",
        r"""reverses the normal-sphere-bundle fundamental class.
Both signs reverse in the integral of
\(4x^3-p_1(TB)x\), so its return index is preserved.""",
        r"""reverses the fundamental class of the capped normal sphere
bundle \(B_\nu=S(\bar\nu)\).
Both signs reverse in the integral of
\(4x^3-p_1(TB_\nu)x\), so its return index is preserved.""",
        "B_nu=B=S(bar nu) is exactly the capped oriented normal sphere bundle imported from 02S8, with projection pi to bar X_m, meridian-one class x and e_v=2x-pi*b. The identity of its total space and base, with inverse identity, preserves the tangent identity p1(TB_nu)=pi*(p1(Tbar X_m)+p1(bar nu)), all orientations, the sign reversal of its fundamental class and the displayed meridian integral. The earlier cap coordinate B=exp(2pi i m a) keeps its explicit solid-torus map and its root/deck inverse. The same B_nu name is proposed in the complete 02S8 proof.")

p.finish()
