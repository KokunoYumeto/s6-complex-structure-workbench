#!/usr/bin/env python3
"""Close the three remaining prompt items after the fully reviewed B.4.33.

This is an editorial status update, not a machine proof. Earlier bytes are
preserved by retain_checkpoint_versions.py and the immutable checkpoints.
"""
from pathlib import Path
import csv, datetime, hashlib, json

root = Path(__file__).resolve().parents[1]
changes = []

def replace(path, before, after):
    file = root / path
    original = file.read_text()
    assert original.count(before) == 1, (path, before[:100], original.count(before))
    revised = original.replace(before, after, 1)
    file.write_text(revised)
    changes.append({"path": path, "before": before, "after": after,
                    "old_sha256": hashlib.sha256(original.encode()).hexdigest(),
                    "new_sha256": hashlib.sha256(revised.encode()).hexdigest()})

ab = "sections/AB_push.tex"
replace(ab, r"\subsection{B.4--B.5. The remaining filling problem}",
        r"\subsection{B.4--B.5. Nonexistence of a proper analytic filling}")
replace(ab, r"""\begin{problem}[B.4.1; Open]\label{push:B41}
Construct, or obstruct, a proper flat
holomorphic filling of the actual $S^6$
family after a finite base change which
repairs the cusp incompatibility of B.3.1.
If it exists, determine an equivariant
model for descent to $w$, its central
multiplicities and a resolution, and the
least semistable base-change exponent.
The local constructions in B.1 and B.2
do not settle this problem.
\end{problem}""", r"""\begin{corollary}[B.4.1; Refuted; the proposed global filling]\label{push:B41}
The actual punctured $S^6$ family has no proper
Hausdorff complex-analytic filling after any finite
cover of $w=0$. In particular, a proper flat filling
with smooth total space and reduced normal-crossings
centre does not exist. There is no positive least
semistable exponent, no equivariant analytic filling
to descend, and no central multiplicity data for
such a descent.
\end{corollary}
\begin{proof}
Theorem B.4.33 below proves the stronger assertion
allowing arbitrary singular central spaces and
multiplicities. A hypothetical filling after any
initial cover remains proper after a further cover;
the theorem excludes that further cover as well.
The local constructions in B.1 and B.2 and the
partial filling B.4.19 therefore cannot be completed
to the requested global object.
\end{proof}""")
replace(ab, """fail for the prescribed pieces. A
construction with a corrected cusp remains
necessary before descent or characteristic
numbers can be computed.""", """fail for the prescribed pieces. That local
failure alone would not rule out a different cap.
B.4.30--B.4.33 supply the additional global argument
which excludes every proper analytic filling of
the actual family, including such alternatives.""")
replace(ab, r"""\begin{problem}[B.5.1; Open]\label{push:B51}
For an actual corrected filling in B.4.1,
compute the integral topology of its
central fibre and of a descent resolution,
the nearby-cycle Euler count, and the
applicable monodromy or Hodge comparison.
These invariants are not assigned to the
incompatible assembly refuted in B.3.1.
\end{problem}""", r"""\begin{corollary}[B.5.1; Refuted; the premise of a global central fibre]\label{push:B51}
There is no central fibre or descent resolution
of the requested proper analytic filling of the
actual $S^6$ family. Its proposed integral homology,
fundamental group, central Euler number and
nearby-cycle comparison are therefore undefined.
\end{corollary}
\begin{proof}
Theorem B.4.33 excludes the underlying proper
analytic space after every finite parameter cover.
An invariant of that nonexistent central fibre
cannot be computed by assigning it the topology
of a local or auxiliary model. The local topologies
and necessary degeneration conditions proved above
retain exactly their stated hypotheses. The
punctured family's smooth monodromy is a different,
well-defined invariant and is computed in Part C.
\end{proof}""")

cfile = "sections/C_push.tex"
replace(cfile, r"""and identified below. The specific analytic filling of Part B and
its Chern data remain open in C.5.1. In this section $M_\Phi$ is a closed seven-manifold, whereas $W_8$ denotes a""",
        r"""and identified below. B.4.33 excludes the specific analytic
filling of Part B, so C.5.1 records that its requested Chern
data are undefined. In this section $M_\Phi$ is a closed seven-manifold,
whereas $W_8$ denotes a""")
start = r"\begin{problem}[C.5.1 (Open): the specified analytic eight-dimensional filling]"
file = root / cfile
original = file.read_text()
pos = original.index(start)
end = original.index(r"\end{problem}", pos) + len(r"\end{problem}")
replace(cfile, original[pos:end], r"""\begin{corollary}[C.5.1 (Refuted): the specified analytic filling premise]
The analytic descended filling and its resolution $W_8$
requested in Parts B.4 and C.2 do not exist. Consequently
there are no values of $c_1,c_2,p_1,p_1^2,p_1c_1^2,c_1^4$,
relative lifts, intersection form or signature for that
specified analytic object. The actual positive-loop
monodromy is nevertheless
\[
                    [\Phi]=0\in\Theta_7\simeq\Z/28.
\]
\end{corollary}
\begin{proof}
A descended analytic filling of the specified family
would be a proper analytic filling before any resolution,
and its finite pullback would remain proper. B.4.33
excludes both possibilities. Characteristic numbers of
an unrelated manifold cannot supply the requested values.

C.3.24 determines the actual monodromy by the equivariant
orbit-knot integer. C.3.25--C.3.27 construct an actual
smooth spin$^c$ coboundary of the clutching sphere and
mapping torus and give a second determination by the
index formula. Both use the verified actual pairings
$p_\psi=-24\epsilon_{\rm cap}$ and
$k_\psi=-6\epsilon_{\rm cap}$ and pass from six loops
to one in an integer group before reduction modulo $28$.
Their distinct boundary-invariant arguments and shared
geometric inputs are stated in C.3.27. C.4.1 gives the
same zero for all the compared sphere twist data, and
C.4.2 gives the antiholomorphic transformation law.

The smooth coboundary of C.3.25 is fully specified and
has the intersection and spin$^c$ characteristic data
computed there. No complex structure on it is asserted,
and its determinant class is not identified with the first
Chern class of an almost-complex tangent bundle. This
distinction is essential now that the prescribed analytic
construction has been refuted.
\end{proof}""")

replace("sections/conventions_push.tex", r"""This return is \textbf{INCOMPLETE}. Every assertion is restricted to its
stated hypotheses; an unresolved construction or invariant is not
assigned a value. The supplied AI-produced return and review are
source material requiring verification. We claim no priority.""",
        r"""All requested items are proved or refuted in their stated categories.
In particular, B.4.33 excludes a proper analytic filling of the
actual sphere family; invariants of that nonexistent object are
undefined. The supplied AI-produced return and review require
verification. No human verification or priority is claimed.""")
paper = root / "S6_02_PUSH_paper.tex"
original = paper.read_text()
assert original.count(r"15 November 2026\quad---\quad INCOMPLETE") == 2
paper.write_text(original.replace(r"15 November 2026\quad---\quad INCOMPLETE", "15 November 2026"))
changes.append({"path": paper.name, "change": "Removed the provisional INCOMPLETE date suffix after all numbered Open items were resolved."})

replace("sections/C_corrected_seifert_comparison.tex", """three-dimensional push-off datum only; the normal correction
of C.3.11 remains a separate unresolved comparison.""", """three-dimensional push-off datum only. The actual normal-line
comparison and its contribution are established separately in
C.3.20--C.3.22; they are not inferred from this linking number.""")

updates = {
 "B.4.1": {
  "statement": "The proposed proper analytic S6 filling after finite parameter cover does not exist; no least semistable exponent or equivariant analytic descent exists.",
  "status": "Refuted", "where_proved": "sections/AB_push.tex B.4.1; sections/B_global_noncompletion.tex B.4.33",
  "depends_on": "B.4.33", "notes": "The existence premise is refuted in the arbitrary proper Hausdorff complex-analytic category, including singular central spaces and multiplicities. All finite cover degrees are excluded."},
 "B.5.1": {
  "statement": "The requested global S6 central fibre and its descent resolution do not exist, so their topology and nearby-cycle invariants are undefined.",
  "status": "Refuted", "where_proved": "sections/AB_push.tex B.5.1; sections/B_global_noncompletion.tex B.4.33",
  "depends_on": "B.4.33", "notes": "Refutes the object premise; undefined invariants are not assigned zero. The separately constructed local and auxiliary models retain their computed topology."},
 "C.5.1": {
  "statement": "The specified analytic eight-dimensional descended filling and resolution do not exist; their almost-complex Chern and intersection data are undefined, while the actual smooth monodromy is zero.",
  "status": "Refuted", "where_proved": "sections/C_push.tex C.5.1; sections/B_global_noncompletion.tex B.4.33",
  "depends_on": "B.4.33;C.3.24;C.3.25-C.3.27",
  "notes": "The actual smooth spin-c coboundary in C.3.25 is a different constructed object, with its own computed data. No almost-complex Chern class is assigned to it without proof."}
}
for relative in ["sections/AB_push_results.csv", "sections/C_push_results.csv"]:
    path = root / relative
    with path.open(newline="") as stream:
        reader = csv.DictReader(stream)
        fields = reader.fieldnames
        rows = list(reader)
    for row in rows:
        if row["id"] in updates:
            before = dict(row)
            row.update(updates[row["id"]])
            changes.append({"path": relative, "id": row["id"], "before": before, "after": row})
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader(); writer.writerows(rows)

for relative in ["sections/C_monodromy_value_results.csv", "sections/C_independent_monodromy_value_results.csv"]:
    path = root / relative
    original = path.read_text()
    revised = original.replace("The specific analytic B.4 filling remains Open.",
                               "The specific analytic B.4 filling is excluded by B.4.33; its characteristic data are undefined.")
    revised = revised.replace("The specific analytic B.4 filling and its Chern data remain Open.",
                              "B.4.33 excludes the specified analytic filling; C.5.1 records its undefined Chern data.")
    assert revised != original, relative
    path.write_text(revised)
    changes.append({"path": relative, "change": "Replaced obsolete analytic-filling Open note with B.4.33/C.5.1 outcome."})

record = {"updated_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
          "basis": "Full written B.4.33 reviewed by root, boundary_d and limits_ab; classification_e authored and checked its uniform reduction. Untwisted-family stress test passed independently.",
          "changes": changes}
(root/"code"/"final_main_status_changes.json").write_text(json.dumps(record, indent=2)+"\n")
print(json.dumps({"updated_utc": record["updated_utc"], "changed_records": len(changes),
                  "resolved_ids": list(updates), "proof": "B.4.33"}, indent=2))
