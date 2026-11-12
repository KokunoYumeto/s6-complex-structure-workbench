# Exact relation of the radial carrier representation to polymer kinematics

8 September 2026. This is a representation-theoretic identification of
the already constructed global radial limit. It is not a claim that
Yang--Mills has become quantum gravity, nor a replacement of the
finite-regulator construction by a chosen representation.

## 1. Source and conventions

Ashtekar, Fairhurst and Willis construct a nonregular Weyl representation
with an orthonormal basis indexed by the real numbers in Section III.B
of *Quantum gravity, shadow states, and quantum mechanics*,
Classical and Quantum Gravity 20 (2003), 1031--1062
([arXiv:gr-qc/0207106v3](https://arxiv.org/abs/gr-qc/0207106v3)).
Their equations labelled innerprod, uvops and xop give a Hilbert space
with basis \(|x\rangle\), \(x\in\mathbb R\), and actions
\[
 \widehat U(\ell)|x\rangle=e^{i\ell x}|x\rangle,\qquad
 \widehat V(\mu)|x\rangle=|x-\mu\rangle,\qquad
 \widehat x|x\rangle=x|x\rangle.
 \tag{1}
\]
In particular the sign of the shift in their convention is negative.
The label, its physical interpretation, and the Hamiltonian must not
be inferred from equality of these kinematic formulas alone.

## 2. The unitary map with all labels and signs retained

The full radial window space proved in the amplitude note is
\[
 \mathcal H_{\rm win}
 =\bigoplus_{b\in\mathbb R}L^2((0,\infty),\rho),\qquad
 d\rho(q)=\frac{q^{1/2}e^{-q}}{\Gamma(3/2)}dq .
 \tag{2}
\]
Let \(\mathcal H_{\rm pol}\) be the Hilbert space of (1).
For finite-support families \(f=(f_b)\), define
\[
 \mathcal I f=\sum_b |b\rangle\otimes f_b
       \quad\hbox{in }\mathcal H_{\rm pol}\otimes L^2(\rho).
 \tag{3}
\]
The original raw norm is preserved exactly:
\(\|\mathcal I f\|^2=\sum_b\|f_b\|^2\).
Finite-support families are dense in the direct sum, and simple tensors
with finite basis support are dense in the tensor product. Thus (3)
extends to a unitary onto the whole tensor product. Its inverse sends
\(|b\rangle\otimes f\) to \(f\) in fibre \(b\), zero elsewhere.
No measure or amplitude has been rescaled.

Write \(P f_b=b f_b\) on the maximal label-moment domain, and
\(Qf_b(q)=qf_b(q)\) on its maximal moment domain. Let
\[
 (U(a)f)_b=f_{b-a},\qquad
 (Z(\ell)f)_b=e^{i\ell b}f_b,\qquad
 (W(\alpha)f)_b(q)=e^{i\alpha q}f_b(q).
\]
Testing these formulas on the dense finite-support space gives
\[
 \begin{split}
 \mathcal I U(a)\mathcal I^{-1}
   &=\widehat V(-a)\otimes I,\\
 \mathcal I Z(\ell)\mathcal I^{-1}
   &=\widehat U(\ell)\otimes I,\\
 \mathcal I W(\alpha)\mathcal I^{-1}
   &=I\otimes e^{i\alpha Q},\\
 \mathcal I P\mathcal I^{-1}
   &=\widehat x\otimes I .
 \end{split}
 \tag{4}
\]
The first three identities extend by boundedness. The last extends
by the equality of the maximal squared label moments. The exact Weyl
phase is
\[
 Z(\ell)U(a)=e^{i\ell a}U(a)Z(\ell),
 \tag{5}
\]
as follows by evaluating both sides in fibre \(b\). The central
modulation \(W\) commutes with both. The group \(Z\) is strongly
continuous by dominated convergence in the sum of squared fibre norms;
\(U\) is not, since a nonzero shift sends a single-fibre vector to an
orthogonal fibre. These properties are preserved by (3).

## 3. Dynamics and what the comparison does not identify

The actual radial limit has physical Hamiltonian
\[
 Hf_b(q)=c\,b^2q f_b(q),\qquad c=100\sqrt2\pi,
\]
on
\[
 \operatorname{Dom}H=
 \left\{f:\sum_b c^2b^4\int q^2|f_b(q)|^2d\rho(q)<\infty\right\}.
 \tag{6}
\]
Equations (3)--(4) therefore identify it with the maximal joint
multiplication operator \(c\,\widehat x^2\otimes Q\).
This notation means the maximal joint operator in (6), not an
unclosed product with an artificially smaller domain. Its nonreal
resolvents are fibrewise multiplication by \((cb^2q-z)^{-1}\);
their norm is at most \(1/|\operatorname{Im}z|\).

The source's label \(x\) thus corresponds exactly to our global
carrier label \(b\), not automatically to a physical spatial
coordinate of the original gauge field. The additional Gamma
variable \(q\), its measure, and the coefficient \(c\) arise from
the specific radial state and physical lattice scaling. They are
not parameters supplied by the kinematic identification (1).
The source paper's particle Hamiltonian is not asserted equal to (6).

In particular the representation is not novel merely because its
carrier basis is uncountable or its shifts are nonregular. The
specific results established here are the map from the actual
nonlinear regulators to that representation, the retained Gamma
factor and Hamiltonian, and the explicit relation of its amplitudes
and local-cylinder observables. The remaining physical question is
which spatially local gauge observables, with all their scale
factors retained, survive on it. Neither the unitary map (3) nor
the established polymer terminology answers that question.
