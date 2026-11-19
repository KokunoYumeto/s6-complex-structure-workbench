"""Append exact source-use checks, preserving every earlier event and its scope."""
from pathlib import Path
import csv,json
P=Path(__file__).resolve().parents[2]
f=P/'records/root_events.tsv';rows=list(csv.DictReader(f.open(),delimiter='\t'))
entries={
'fam:src:A.5.1':'Opened DGKXv1 Theorem1.4 p3 and the pair/bare equivalence proof passages pp92,95 in the original107-page PDF, matching the exact supplied-source labels. The receiving complete proof and its8September2026 working-edition record remain separately credited. This closes the named statement/page-source gate only.',
'fam:src:A.5.2':'Opened DGKXv1 Lemma6.11 and full proof p81, Theorem6.12 and full proof pp81–82, and Proposition6.16 and full proof p85; matched branch-normal adjunction, cohomology and the actual injective local-ring substitution. The current receiving rederivation and renewed cusp module check are retained as separate events. Exact co-located alias labels share this same source reading, without additional independent credit.',
'fam:src:B.4.1':'Opened DGKXv1 Theorem7.14 and complete proof p95, including its exact intrinsic-fibration and vertical-translation inputs. The current source locator is corrected to that theorem and stable label; no whole-proof check of all source dependencies is inferred from this bounded reading.',
'push:src:C.3.5':'Read DGKXv1 Proposition7.8 and full proof pp91–92 and PropositionsC.1–C.2 with complete proofs p102. Rechecked the displayed defect -kl/12 and quadratic correction -k^2/24 and matched the fixed roots and analytic markings. This closes the exact source-locator gate for the credited short application.',
'push:src:B.4.3':'Opened Nishiguchi MPI/88-48 Theorem1.4 printedp7 and Example2.1 printedp13, with their exact K3 and Hopf-component scope. The receiving citations now use these precise loci. Istrati source checks remain separately recorded; no new broad degeneration theorem is inferred.',
'push:src:B.4.6':'Opened Schroeer–Siebert Definition2.1 p4 and the Section3 conductor/normal-line propositions pp6–10, together with the previously read Kamenova and KKN hypotheses. Rechecked the receiving explicit cohomology comparison: these source models are not asserted to identify an arbitrary cap. The only supported comparisons are the displayed actual maps and the specific hypotheses stated there.',
'push:src:B.4.7':'Read Doi Section5.3 through Theorem5.5 pp881–883 and Example5.3 pp880–881; read Nishiguchi Theorem1.4 and Example2.1 and Schroeer–Siebert Section3. Matched smooth-map versus requested holomorphic-map data explicitly and retained the receiving complete proper product-cap construction. The SS Theorem4.4 quotient-generator exponent issue is recorded in the report and is unused by this receiving proof.',
'push:src:B.4.10':'Opened Teleman Introduction pp1750–1751, including the exact modification and spherical-shell gluing description. This closes the named background source gate; the moving Kato embedding, uniform collar containment and exceptional correction are checked by the previously recorded receiving proof.',
'ari:C.6.4':'Opened Silverman author slides21–22 (PDF26–27), matching the uniform height bound and specialization limit with their hypotheses. The exact DeMarco–Mavraki application and its bounded local remainder remain the operative proof. The original1983Silverman and Tate articles remain explicitly unverified background records.',
'push:src:E.4.1':'Read Johansson2016 Section2 pp2–4 and complete Section3 pp4–6, and official python-flint0.9.0 constructor/lower/upper/man_exp/str semantics. Matched rational/binary input enclosures and outward endpoint comparisons to the already replayed19701 norm-box and19911-leaf certificate. This closes the software-semantics citation gate; no additional execution or implementation-wide audit is claimed.',
'inv:D1.2':'Matched the previously successful unchanged d_exact.py and d_koszul.py replays to this full tangent/Koszul proof:481 weighted cohomology counts, root-character invariants, polynomial module relations and the joint coefficient123i/(64pi). The earlier event saying replay pending is superseded at exactly this finite-algebra scope; its complete analytic comparison review remains separate.'
}
for label,outcome in entries.items():
 r={'statement_id':label,'date':'2026-11-18','who':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS','type':'used and rechecked in this run','outcome':outcome}
 if r not in rows:rows.append(r)
with f.open('w',newline='') as o:
 w=csv.DictWriter(o,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(rows)
(P/'analysis/I_final_cited_scope_closures.json').write_text(json.dumps(entries,indent=2))
print('Added',len(entries),'bounded source-use checks; total root events',len(rows))
