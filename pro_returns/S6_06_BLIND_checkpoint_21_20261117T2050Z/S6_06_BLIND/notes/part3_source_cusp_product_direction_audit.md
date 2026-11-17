# Actual-to-reference products and the boundary connecting sign

Independent audit of the literal OP.20 arrow in the working K48 proof.
The full transported unit maps remain those of OP.19 and K42; this
note records the product and connecting-map directions.

Write \(p_H(\theta)\) and \(p_O(\theta)\) for the Hopf and ordinary
products, both maps from the actual fibre to the reference fibre.
OP.20 has the actual coordinate arrow
\[
 \Gamma_\theta=p_O(\theta)p_H(\theta)^{-1},\qquad
 (h,q)\longmapsto(h,L(h,\theta)qR(h,\theta)).
\]
Its closed Spin(4) factor degrees on the outward h-sphere followed
by positive theta are \((-6,0)\). The forward transports are their
inverses, so the exact order is
\[
 p_O(\theta)^{-1}=p_H(\theta)^{-1}\Gamma_\theta^{-1}.
\]
Extend the boundary loop \(\Gamma^{-1}\) over the reference exterior
\(D^3_y\times S^3_q\), beginning at the identity, and call that
extension \(\psi_\theta\). The same actual endpoint closing is
used for the two products. Consequently
\[
                      \Phi_O=\Phi_H\circ\psi_1.
\]
This is right composition; inversion of the boundary gauge occurs
before taking the connecting endpoint.

The extension can be chosen in the actual fibrewise Spin(4) group.
Its two factors extend the based maps on
\((S^2\times I)\cup(D^3\times\{0\})\). This union is the boundary
of \(D^3\times I\) with the open top face removed, and the cylinder
retracts to it after a collar rounding. Pulling back the displayed
factors supplies an extension, which can be smoothed relative to
the prescribed collars. Thus
\[
 \psi_\theta(y,q)=(y,a_\theta(y)q\,b_\theta(y))
\]
with the specified boundary values. Its endpoint is fixed on a
boundary collar, because the boundary gauge is a closed based loop.

The degree sign follows from the actual product orientation. Orient
\(D^3\times I\) by \(\Omega_{D^3}\wedge d\theta\). The side has
orientation \(\Omega_{S^2}\wedge d\theta\), while the top has
orientation \(-\Omega_{D^3}\). For a normalized closed volume form
on \(S^3\), Stokes therefore gives
\[
             \deg(a_1)=\deg(a|_{S^2\times I})=6,\qquad
             \deg(b_1)=0.
\]
These are precisely the positive relative D3 degrees used by
K23's map \(\zeta:(D^3,S^2)\to(S^3,1)\). The endpoint is homotopic
through fibre rotations, relative to the boundary, to the pure
left sixth power in those conventions.

There is no central disc-supported class in this chosen extension:
the same formula
\((y,q)\mapsto(y,a_1(y)q\,b_1(y))\) extends literally over
\(D^3\times D^4\), preserving its boundary orientation. Different
extensions with the same boundary loop differ by a path of
boundary-fixed diffeomorphisms, so their endpoints have the same
relative class. This verifies the connecting arrow itself.
The complete application to a source-family relative return retains
the full K42-to-OP.20 unit identification and is owned by the
checks/root proof; no new all-fan return is assigned in this audit.
