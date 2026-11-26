"""Resolve notation and model-transport contexts found in full final readback."""
from S6_SERIES_PUBLISH_c8_foundations_editing import Editor

e = Editor("cyclic_invariants", "c8-III-foundations-cyclic-models-followup-", group="root")
e.replace(r""" \mathcal I_d=(A_d,\ b_3=0,\ p=0,\ \mu_d),
\]
where $p$ is the refined Pontryagin class and the group-valued
invariants are expressed by a marking $H_2\to A_d$.""", r""" \mathcal I_d=(A_d,0,0,\mu_d).
\]
Its entries give second homology, the third Betti number, the
refined Pontryagin class $p(N)$ and the fundamental-class invariant,
respectively. The group-valued invariants are expressed by a
marking $H_2(N)\to A_d$.""", "D20", "mapsIII:def:cyclic-classifying-data",
          "Name the refined class with its manifold argument p(N), preserving the identical four-entry datum while avoiding a bare p=0 beside the nonzero integer p defining the cyclic cover.")
e.replace(r"""By \cref{maps:src:D.1.11}, $Z_d$ is an oriented representative of
$M_d$. On this representative set $\sigma_d=D_\gamma$; on any other
representative transfer it by an oriented diffeomorphism
$\iota_d:Z_d\to M_d$, as
$\sigma_d=\iota_dD_\gamma\iota_d^{-1}$.""", r"""Use the identity from $Z_d$ to its underlying oriented manifold
$M_d$ in Definition~\ref{mapsIII:def:canonical-cyclic-model} to
set $\sigma_d=D_\gamma$. For any other oriented representative
$N_d$ of this type, Theorem~\ref{maps:src:D.1.11} gives an oriented
diffeomorphism $\iota_d:M_d\to N_d$. The transported action is
$\iota_d\sigma_d\iota_d^{-1}$, with inverse conjugacy
$\iota_d^{-1}$.""", "D20", "maps:src:D.1.12",
          "Keep the chosen canonical model Md fixed by its new actual-cover definition. State separately the same action on another representative Nd through the exact oriented conjugacy and inverse; no action or quotient scope changes.")
e.replace(r"\cite[Theorem~2.2, p.~38; Lemma~2.14, pp.~52--53]{TeschlODE2012}",
          r"\cite[author's preliminary version, Theorem~2.2, p.~38; Lemma~2.14, pp.~52--53]{TeschlODE2012}",
          "D18", "maps:src:D.1.7", "Name the precise already admitted preliminary version whose printed pages are used, matching the bounded source record and existing Teschl bibliography entry.")
e.finish()
