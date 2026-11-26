#!/usr/bin/env python3
"""Nine exact layout proposals from the actual III pass03 warnings.

Read-only command: validate the exact old guards in canonical and owned fragments.
The root editor may import REPAIRS and apply_to_text after reading the proposals.
This program never writes manuscript, ledger, event, inventory, or progress files.
It makes no claim that a proposed layout has already passed the TeX engine.
"""
from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
UNITS = ROOT / "agents/continuation8_iii_integration/units"

REPAIRS = [
    dict(
        name="finite_reduction_definitions",
        pass03_line="23814", width_pt="21.04941",
        owner="maps:src:D.2.26", fragment="later/elliptic_sphere_outputs.tex",
        reason="Split the seven definitions over two aligned rows; retain their order and every parameter.",
        old=r"""\[
F=\prod_{\mathrm{finite}}m_i,\quad Q=\prod q_i,\quad
P=F/Q,\quad c=b/Q,\quad p_i=m_i/q_i,\quad
\alpha_i=bn_i/q_i,\quad N_f=\sum(F/m_i)n_i.
\]""",
        new=r"""\[
\begin{aligned}
F&=\prod_{\mathrm{finite}}m_i,\quad Q=\prod q_i,\quad
P=F/Q,\quad c=b/Q,\\
p_i&=m_i/q_i,\quad
\alpha_i=bn_i/q_i,\quad N_f=\sum(F/m_i)n_i.
\end{aligned}
\]""",
    ),
    dict(
        name="nonzero_chern_gysin_groups",
        pass03_line="27314", width_pt="8.26257",
        owner="maps:src:D.2.32", fragment="foundations/original_cap_homology.tex",
        reason="Put the four Gysin groups on two rows; retain the integral kernel and all exponents.",
        old=r"""\[
 H_1(E(M))=0,\qquad
 H_2(E(M))=\ker(c:\mathbb Z^{s_i}\to\mathbb Z),\qquad
 H_3(E(M))=\mathbb Z^{s_i},\qquad H_4(E(M))=0,
\]""",
        new=r"""\[
\begin{aligned}
 H_1(E(M))&=0,\qquad
 H_2(E(M))=\ker(c:\mathbb Z^{s_i}\to\mathbb Z),\\
 H_3(E(M))&=\mathbb Z^{s_i},\qquad H_4(E(M))=0,
\end{aligned}
\]""",
    ),
    dict(
        name="finite_odd_weight_list",
        pass03_line="32689--32699", width_pt="117.49649",
        owner="mapsIII:rem:odd-weighted-calculations", fragment="foundations/weighted_odd_cap_kernels.tex",
        reason="Permit line breaks at the commas of the existing inline list; retain all fourteen values and the whole paragraph.",
        old=r"""The finite calculations use the permitted odd-common-factor
weights among $1,2,3,5,7,9,15,21,25,35,45,105,315,1001$.""",
        new=r"""The finite calculations use the permitted odd-common-factor
weights among $1,\allowbreak 2,\allowbreak 3,\allowbreak 5,\allowbreak
7,\allowbreak 9,\allowbreak 15,\allowbreak 21,\allowbreak 25,\allowbreak
35,\allowbreak 45,\allowbreak 105,\allowbreak 315,\allowbreak 1001$.""",
    ),
    dict(
        name="mixed_primary_homology_and_type",
        pass03_line="39266", width_pt="17.42854",
        owner="maps:src:D.2.38", fragment="weighted/minimal_primary_types.tex",
        reason="Give the homology row and orientation-preserving smooth type separate aligned rows under the same numbered equation and target.",
        old=r"""\begin{equation}
 H_2(X)=\mathbb Z/(2p)\langle s\rangle,\quad H_3(X)=\mathbb Z/(2p),\quad b_3(X)=0,
 \qquad
 X\cong M_t\# Z_{p,\epsilon}
 \quad\hbox{orientation-preservingly}.
 \hypertarget{tag-0209}{}\label{maps:eq:D.MP1}
\end{equation}""",
        new=r"""\begin{equation}
\begin{aligned}
 H_2(X)&=\mathbb Z/(2p)\langle s\rangle,\quad H_3(X)=\mathbb Z/(2p),\quad b_3(X)=0,\\
 X&\cong M_t\# Z_{p,\epsilon}
 \quad\hbox{orientation-preservingly}.
\end{aligned}
 \hypertarget{tag-0209}{}\label{maps:eq:D.MP1}
\end{equation}""",
    ),
    dict(
        name="mixed_primary_coefficient_congruences",
        pass03_line="39272", width_pt="2.45212",
        owner="maps:src:D.2.38", fragment="weighted/minimal_primary_types.tex",
        reason="Separate the two primary coefficient definitions from the two CRT congruences without altering any coefficient or modulus.",
        old=r"""\[
 t=1+\kappa\pmod2,\qquad P_p=\frac{b/p-a\nu}{2}\pmod p,\qquad
 P_{2p}\equiv t\pmod2,\quad P_{2p}\equiv P_p\pmod p.
\]""",
        new=r"""\[
\begin{aligned}
 t&=1+\kappa\pmod2,\qquad P_p=\frac{b/p-a\nu}{2}\pmod p,\\
 P_{2p}&\equiv t\pmod2,\quad P_{2p}\equiv P_p\pmod p.
\end{aligned}
\]""",
    ),
    dict(
        name="mixed_primary_nonsymmetric_pairing",
        pass03_line="39967", width_pt="40.60501",
        owner="maps:src:D.2.38", fragment="weighted/minimal_primary_types.tex",
        reason="Split the full nonsymmetric pairing and inverse-coordinate identity over two rows, preserving Omega, every entry, and the single equation identity.",
        old=r"""\begin{equation}
 K_N=S_N^t\Omega L_N,\quad
 (K_N)_{11}=a n/d_0^2=:N_0,\quad (K_N)_{12}=0,
 \quad (K_N)_{22}=-b d_0^2/n,
 \quad C_S^{-1}\delta=(-\sigma,n_0)^t.               \hypertarget{tag-Q21E}{}\label{maps:eq:MP_local_47}
\end{equation}""",
        new=r"""\begin{equation}
\begin{aligned}
 K_N&=S_N^t\Omega L_N,\quad
 (K_N)_{11}=a n/d_0^2=:N_0,\quad (K_N)_{12}=0,\\
 (K_N)_{22}&=-b d_0^2/n,
 \quad C_S^{-1}\delta=(-\sigma,n_0)^t.
\end{aligned}
\hypertarget{tag-Q21E}{}\label{maps:eq:MP_local_47}
\end{equation}""",
    ),
    dict(
        name="mixed_primary_crt_divided_power_maps",
        pass03_line="40334", width_pt="24.85184",
        owner="maps:src:D.2.38", fragment="weighted/minimal_primary_types.tex",
        reason="Place the primary inclusions and each divided-power image on separate rows; retain both cubic and reduced coefficients and the single equation target.",
        old=r"""\begin{equation}
 e_2\mapsto p s,\qquad e_p\mapsto(1-p)s,\quad
 \gamma_3(e_2)\mapsto p^3\gamma_3(s)=p\gamma_3(s),
 \quad\gamma_3(e_p)\mapsto(1-p)^3\gamma_3(s)
                               =(1-p)\gamma_3(s).   \hypertarget{tag-Q21R}{}\label{maps:eq:MP_local_61}
\end{equation}""",
        new=r"""\begin{equation}
\begin{aligned}
 e_2&\mapsto p s,\qquad e_p\mapsto(1-p)s,\\
 \gamma_3(e_2)&\mapsto p^3\gamma_3(s)=p\gamma_3(s),\\
 \gamma_3(e_p)&\mapsto(1-p)^3\gamma_3(s)
                               =(1-p)\gamma_3(s).
\end{aligned}
\hypertarget{tag-Q21R}{}\label{maps:eq:MP_local_61}
\end{equation}""",
    ),
    dict(
        name="mixed_primary_marking_and_inverse",
        pass03_line="40490", width_pt="33.54132",
        owner="maps:src:D.2.38", fragment="weighted/minimal_primary_types.tex",
        reason="Put the CRT coefficient, forward marking, and exact inverse on three rows; retain all moduli and inverse coefficients under their existing identity.",
        old=r"""\begin{equation}
 k=P_{2p}-tp\pmod{2p},\quad
 \Phi(e_2)=p s,\quad\Phi(e_p)=k s,
 \quad\Phi^{-1}(n s)=(n\bmod2)e_2+
                       (P_p^{-1}n\bmod p)e_p.        \hypertarget{tag-Q221}{}\label{maps:eq:MP_local_71}
\end{equation}""",
        new=r"""\begin{equation}
\begin{aligned}
 k&=P_{2p}-tp\pmod{2p},\\
 \Phi(e_2)&=p s,\quad\Phi(e_p)=k s,\\
 \Phi^{-1}(n s)&=(n\bmod2)e_2+
                       (P_p^{-1}n\bmod p)e_p.
\end{aligned}
\hypertarget{tag-Q221}{}\label{maps:eq:MP_local_71}
\end{equation}""",
    ),
    dict(
        name="mixed_three_primary_homology",
        pass03_line="41449", width_pt="2.53989",
        owner="maps:src:D.2.42", fragment="weighted/three_primary_types.tex",
        reason="Split the full homology list over two rows while preserving the shared H2/H3 value, all zero groups, both Z groups, b3, and its equation identity.",
        old=r"""\begin{equation}
 H_2(X)=H_3(X)=\mathbb Z/c,\quad
 H_1(X)=H_4(X)=H_5(X)=0,\quad
 H_0(X)=H_6(X)=\mathbb Z,\quad b_3(X)=0.
\hypertarget{tag-Q22A}{}\label{maps:eq:MT_local_1}
\end{equation}""",
        new=r"""\begin{equation}
\begin{aligned}
 H_2(X)=H_3(X)&=\mathbb Z/c,\quad
 H_1(X)=H_4(X)=H_5(X)=0,\\
 H_0(X)=H_6(X)&=\mathbb Z,\quad b_3(X)=0.
\end{aligned}
\hypertarget{tag-Q22A}{}\label{maps:eq:MT_local_1}
\end{equation}""",
    ),
]


def identities(text: str) -> Counter:
    return Counter(re.findall(r"\\(?:label|hypertarget)\{[^{}]*\}", text))


def nonlayout_tokens(text: str) -> str:
    """Remove only the exact presentation tokens changed by these proposals."""
    text = re.sub(r"\\(?:begin|end)\{aligned\}", "", text)
    text = re.sub(r"\\(?:qquad|quad|allowbreak)\b", "", text)
    text = text.replace(r"\\", "").replace("&", "")
    return re.sub(r"\s+", "", text)


def verify_repair(repair: dict) -> None:
    old, new = repair["old"], repair["new"]
    if identities(old) != identities(new):
        raise ValueError(f"Identity mismatch: {repair['name']}")
    if nonlayout_tokens(old) != nonlayout_tokens(new):
        raise ValueError(f"Non-layout token change: {repair['name']}")
    for outer in (r"\begin{equation}", r"\end{equation}", r"\[", r"\]"):
        if old.count(outer) != new.count(outer):
            raise ValueError(f"Changed outer numbering construct: {repair['name']}")


def apply_to_text(text: str) -> str:
    """Return the guarded candidate in memory; perform no filesystem mutation."""
    original_identities = identities(text)
    for repair in REPAIRS:
        verify_repair(repair)
        count = text.count(repair["old"])
        if count != 1:
            raise ValueError(f"Expected one exact old guard for {repair['name']}; found {count}")
        text = text.replace(repair["old"], repair["new"], 1)
    if identities(text) != original_identities:
        raise ValueError("Candidate changed a literal label or hypertarget multiplicity")
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--show", action="store_true", help="print every exact old/new fragment")
    args = parser.parse_args()
    canonical = (ROOT / "S6_SERIES_PUBLISH_III.tex").read_text()
    apply_to_text(canonical)
    for repair in REPAIRS:
        fragment = (UNITS / repair["fragment"]).read_text()
        count = fragment.count(repair["old"])
        if count != 1:
            raise ValueError(f"Fragment guard {repair['name']}: found {count}")
        line = canonical.count("\n", 0, canonical.index(repair["old"])) + 1
        print(f"{repair['name']}: canonical guard starts {line}; fragment guard once; "
              f"owner {repair['owner']}; pass03 {repair['width_pt']}pt at {repair['pass03_line']}")
        print("  " + repair["reason"])
        if args.show:
            print("EXACT OLD\n" + repair["old"] + "\nEXACT NEW\n" + repair["new"])
    print("Nine guarded in-memory proposals validated; no source written and no TeX run.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
