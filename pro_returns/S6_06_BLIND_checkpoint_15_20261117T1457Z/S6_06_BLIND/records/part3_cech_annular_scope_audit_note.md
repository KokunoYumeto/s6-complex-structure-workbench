# Pre-checkpoint scope note for the working Cech derivation

The checks agent identified this wording restriction before checkpoint08:
the displayed Pi(q)*lambda*log(q)/(2pi i) formula in
notes/part3_order_one_cech_working.md applies on a smooth-site disc
with a single-valued period frame. At a singular source site the proof
uses the actual given annular translation section; the global gluing,
canonical-line, rationality and section argument does not use that formula.
This source cochain note has not been promoted to a numbered theorem.

The exact Tate replacement supplied during the freeze is as follows.
Write s=log(q)/(2pi i), tau=Ns+tau0(q), with tau0 single-valued.
For elliptic winding periods (c,j),

    u(s)=(j*N/2)*s*(s-1)+j*tau0(q)*s+c*s

has u(s+1)-u(s)=j*tau(q)+c. If the actual line tau-period
character is P(q), the scalar exp(j*log(P(q))*s) supplies its
compensating line lift. The graph period j and delta phase remain
retained and gamma is unchanged. The agent will incorporate the exact
formula in the working note after the checkpoint release.
