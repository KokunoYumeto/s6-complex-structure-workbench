"""Integrate proved fourth-hour advances without making a checkpoint."""
from pathlib import Path
import datetime
import json

root = Path(__file__).resolve().parents[1]
path = root / "S6_04_MAPS_MANIFOLDS_report.md"
report = path.read_text()
replacements = {
    "| B.6 | B.6.1–B.6.9 |": "| B.6 | B.6.1–B.6.14 |",
    "the conditional complex-filling formula is checked but numerical residues remain uncomputed |": "the conditional complex-filling formula is checked; scalar-cover, norm and torsor data are computed, but the direct one-component filling has the wrong boundary and numerical residues remain uncomputed |",
    "| D.2 | D.2.1–D.2.12 |": "| D.2 | D.2.1–D.2.15 |",
    "remaining choices and smooth classifications are not exhausted |": "four all-semistable families now have exact twisted-suspension smooth types, and the index-two cusp gives S2×S4 at every order6k; remaining choices and smooth classifications are not exhausted |",
    "| F.3 | F.3.1–F.3.7 | Undecided in universal scope: natural abelian-surface source excluded; the explicit nonselfdual tuple has a holomorphic period realization; other tuples remain unclassified |": "| F.3 | F.3.1–F.3.9 | Undecided only in compactification scope: explicit nonselfdual tuple compactified; an explicit LSAP/Oka-1 proof now realizes every oriented rank-six monodromy by nondegenerate holomorphic periods on the open base; finite-fibre extension and bounded cusp correction remain to be decided for all data |"
}
for old, new in replacements.items():
    if old not in report:
        raise RuntimeError("Expected report passage absent: " + old)
    report = report.replace(old, new)

report += """

## Fourth-hour advances on the open items

D.2.13 computes the four all-semistable configurations at unrestricted smooth-fibre logarithmic order m and every primitive twist (a,b,c,n). For n nonzero, put t=gcd(m,n,a,b)gcd(m,n,p,c); the factors are coprime. The exact middle torsion is Z/t⊕Z/m⊕Z/(m|n|/t), with π1=Z/|n|. The n=0 case is treated separately, including its free Mayer–Vietoris kernel. D.2.14 identifies every simply connected member as the explicitly framed twisted suspension of the unique simply connected spin five-manifold with H2=(Z/m)^2. This uses the full smooth classification after a fixed-curve equivariant surgery, including the two-primary invariants. D.2.15 retains the index-two cusp in OS56 II and its boundary Z/2; the local torsion maps isomorphically to the regular-family torsion. Its simply connected members are exactly S2×S4 for every logarithmic order6k. Root reran2924 full Smith forms for D.2.13 and630 for D.2.15, and checked the circle-action geometry and the published classification steps.

B.6.10 computes the actual scalar-return cover and its elliptic surface, including all deck eigenspaces and their signatures. B.6.11 computes signature+2 and c1²=0 for the untwisted K13 filling, whose boundary is nonspin and therefore cannot be the sphere mapping torus. B.6.12 proves the generic section-norm obstruction N(MW)=12ZP. B.6.13 overcomes that particular obstruction with a four-torsion elliptic torsor and the required conductor line. B.6.14 then proves that its direct one-component semistable plumbing still cannot be the desired filling: H² of its boundary is nonzero, and its new rank-one fibre has multiplicity12. These conclusions locate the failed boundary comparison; none is used as a numerical Eells–Kuiper computation. Extra vertical components or a different ramified model require a new comparison. A separate route now under examination uses equivariant surgery on the actual fixed sphere, followed by the disk bundle of a principal circle bundle; its shear and parametrized framing remain uncomputed.

F.3.8 gives nine explicit integer matrix directions spanning M3(C). The entire complex lines in these directions have a uniform least-singular-value bound, so their radius1/4 spanning tube lies in the unpolarized period domain. This proves LSAP and Oka-1 by Alarcón–Forstnerič, with an exact symbolic certificate rather than sampled positivity. F.3.9 applies their actual fibre-bundle section theorem to every oriented rank-six local system on an open Riemann surface. Thus holomorphic nondegenerate periods on the smooth locus are no longer an obstruction for any datum. The theorem controls finite jets at interior points; it does not automatically prescribe good reduction or a bounded logarithmic correction at omitted punctures. The latter remains the precise period problem.

The independent audits, exact reruns and primary theorem checks are recorded in records/root_audit_checkpoint04_progress.json and the corresponding root_*_audit.out files. The new period-domain argument and both section-theorem hypotheses have been independently checked by root. These are advances on the stated open items; no claim of completion or priority is made.
"""
path.write_text(report)

audit_path = root / "records/root_audit_checkpoint04_progress.json"
audit = json.loads(audit_path.read_text())
audit["reviewed_utc"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
audit["statements"]["F.3.8"] = "Passed: all nine real directions span over C; symbolic normal-matrix singular-value bound holds for every real parameter; Frobenius perturbation radius1/4 stays in det(ImZ)>0; this is a spanning tube under the exact primary Definition2.1. GL+(6,R) transport gives strong domination, LSAP and Oka-1. Root independently reran the exact determinant and identity certificate."
audit["statements"]["F.3.9"] = "Passed: primary Alarcon-Forstneric Proposition7.13(d) and Definition7.7 opened directly; continuous sections exist over a graph spine, so the actual section lifting property applies. The holomorphic quotient by a uniformly discrete full lattice gives a proper family. Missing-puncture conditions are expressly not inferred."
audit_path.write_text(json.dumps(audit, indent=2) + "\n")
print("Integrated B.6.10–14, D.2.13–15 and F.3.8–9; five item scopes remain open.")
