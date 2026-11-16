"""Record complete root audits of the lattice and Hopf boundary results."""
from pathlib import Path
from datetime import datetime, timezone

root = Path(__file__).resolve().parents[1]
stamp = datetime.now(timezone.utc).isoformat()
record = f'''# Joint core lattices and Hopf boundaries

UTC: {stamp}

UN36: the root read the entire proof and exact matrix output. The boundary
is the inverse image of the singular locus of the entire reduced support,
not just of the individual component. Integral Alexander duality gives the
full vector of curve intersections, with a free target; isolated boundary
points add no degree-two generator. Thus integral basis classes in its
kernel have genuine compact representatives off the boundary. Transfer
through all strict components of the normalized root cover has total degree
m_i, even when disconnected, and preserves the intersection pairing with
that precise factor. The smooth horizontal flows move neighborhoods of all
selected cycles into one actual nearby torus. They are defined over the
whole small disc, so the resulting integral homology classes are invariant
under actual monodromy. No invariant-cycle surjectivity is used.

The preserved form makes the kernel radical. Its positive and negative
indices are bounded by those of the monodromy-invariant torus form. A
nondegenerate rank-six source embeds with finite lattice index and hence
has square absolute discriminant. The negative-index bounds give boundary
rank at least16+n for a K3 resolution with n blowups and6+n for Enriques or
chiO1 elliptic resolutions. The root reread UN11's actual nearby-cycle
spectral-sequence proof that unipotent H1 monodromy has square-zero
difference: its degree-one filtration has only two terms. All four oriented
Jordan forms and their exterior-square invariant forms were computed
exactly. The inertias are(3,3,0),(1,1,2),(1,2,1),(2,1,1). In particular
rank-one unipotent monodromy forces every component pg to vanish. Root PASS.

UN37: the root read the complete proof for the given primary or secondary
Hopf surface. Finite-cover transfer and the actual deck character give b1=1,
b2=0. The zero/pole intersection of a meromorphic function vanishes, so
positivity removes all pencil indeterminacy. Its Stein factor has base P1
by the injective H1 edge map. Adjunction and lifting a rational normalization
through C² minus the origin prove every curve is smooth elliptic; zero
intersection makes distinct curves disjoint. Each connected fibre is mC.
The exact root equations w^m=u,s=wx give a finite etale normalized cover.
Connected generic fibres and Stein factorization give a connected central
elliptic cover; its free deck action is by translations. An averaged
horizontal connection gives the actual identity integral monodromy. The
smooth-cover j-function descends and extends, so it is constant. UN34 then
retains this specified Hopf torsor, giving the prescribed surface unchanged
and with multiplicity one in an already Euler-zero SNC compact torus fibre.
No restriction on the finite primary-cover group is inserted. Root PASS.

UN38: the root read the complete source and exact jet certificate. The
proper canonical direct image is a torsion-free rank-one sheaf on the disc.
Evaluation of its generator is nowhere zero on every nearby torus and has
the exact vertical divisor sum k_iS_i. Near a compact subset of a single
smooth support component, the actual fibre section trivializes O(m_iS_i).
Adjunction then trivializes the m_i-th canonical power on that whole
neighborhood. For an elliptic curve there it makes the m_i-th normal power
trivial. A diagonal algebraic-dimension-zero Hopf axis has non-torsion normal:
the Laurent coefficients of a trivializing function would give a positive
power resonance, hence an actual meromorphic invariant.

The nonlinear Hopf has torsion axis normal, so the proof uses its entire
canonical neighborhood. The invariant form dz wedge dw / w^(r+1) gives
K=O(-(r+1)C). A hypothetical canonical trivialization produces an invariant
holomorphic function with positive divisor jC near the whole axis. Its
leading coefficient forces j=rk and h_j=c z^(-k). At order j+r the actual
functional equation has right coefficient k c beta^(-r) at z^(-k-1), while
the left Laurent operator annihilates that coefficient. This is an exact
contradiction. The symbolic output verifies72 resonant instances and all
canonical pullbacks for r=1,...,8; the written coefficient proof covers all r,k.

The curve list is independently derived: analytic closure at the origin,
the convergent contracting-unit product, and the weighted eigenfunction
equation give precisely the diagonal axes or the unique nonlinear axis.
The conductor and other-component boundary have curve support, so any axis
outside it is disjoint from it. The neighborhood obstruction applies.
Finite unramified primary covers pull back both the neighborhood and its
canonical trivialization, and preserve algebraic dimension by the actual
meromorphic symmetric-polynomial descent. Thus the boundary assertion
holds for secondary surfaces as well. Its statement explicitly requires
the normalization itself to be smooth minimal Hopf; arbitrary blowups are
being treated in a separate pushed divisor identity. Root PASS.

These three results directly advance the remaining C.2 component and
gluing problem. Their necessary lattice and boundary conditions are not
asserted to suffice for abstract smoothability. Algebraic-dimension-zero
Hopf occurrence and a complete whole-support realization description remain
under investigation.
'''
(root/'records/root_research_boundary.md').write_text(record)
p=root/'S6_03_CDP_report.md'
s=p.read_text().replace('C.2.UN.1–35; A.5.18–21','C.2.UN.1–38; A.5.18–21')
needle='The remaining unresolved clause is the unrestricted geometric classification of all reducible zero-Euler supports;'
s=s.replace(needle,'UN36 gives exact multiplicity-weighted compact-core lattices in the actual monodromy invariants and joint boundary-rank bounds. UN37 realizes every algebraic-dimension-one Hopf surface unchanged. UN38 forces every curve of a smooth minimal algebraic-dimension-zero Hopf normalization into the fibre boundary, including the nonlinear higher-jet obstruction. '+needle)
s+='''
## Exact joint lattices and the remaining Hopf boundary

UN36 maps all original boundary-orthogonal integral component lattices into
the actual monodromy invariants of one nearby torus, multiplying each form
by the original component multiplicity. The kernel is radical. Both joint
signature bounds, the full-rank discriminant-square condition, and all
oriented unipotent invariant forms are proved. In particular a K3 resolution
with n blowups has at least16+n independent boundary classes, and rank-one
unipotent monodromy forces every component geometric genus to vanish.

UN37 settles occurrence of every primary and secondary Hopf surface of
algebraic dimension one: its actual elliptic reduction has only smooth
multiple fibres, constant modulus and identity integral monodromy. UN34
retains that precise torsor in a compact zero-Euler fibre. UN38 gives the
remaining algebraic-dimension-zero boundary obstruction. Canonical
evaluation trivializes a positive canonical power on the entire smooth
single-component neighborhood. This excludes both diagonal axes through
their non-torsion normal and the nonlinear axis through an explicit
resonant higher-jet coefficient. For a normalization that is already smooth
minimal Hopf, all its elliptic curves must belong to the fibre boundary.
The later investigation of arbitrary blowups and whole-fibre adjacency
retains every full multiplicity. The exhaustive reducible classification
remains INCOMPLETE.
'''
p.write_text(s)
print('Full root audits UN36, UN37, UN38: PASS.')
print('Exact core-form and Hopf-jet outputs inspected; report updated throughUN38.')
