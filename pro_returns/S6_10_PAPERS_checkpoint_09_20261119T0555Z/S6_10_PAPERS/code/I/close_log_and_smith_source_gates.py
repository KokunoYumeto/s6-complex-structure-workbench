"""Close named citation gates without manufacturing another proof re-derivation."""
from pathlib import Path
import csv
P=Path(__file__).resolve().parents[2]
f=P/'records/root_events.tsv'
rows=list(csv.DictReader(f.open(),delimiter='\t'))
entries={
 'push:src:B.4.30':'Opened IKN Proposition6.1 and complete Theorems6.2–6.3 proofs, pp30–34, the adjacent remarks and the entire mathematical erratum pp113–115. Rechecked the receiving proper separated log-smooth fs setup, torsion-free characteristic cokernels and unipotent-coefficient application. Also read the exact strict-analytic toroidal Lemma2.14 and full proof, and Parusinski Corollary1.2 with complete proof pp3–6. This closes these named source gates; it adds no second whole-proof credit.',
 'push:src:B.4.32':'Matched the exact IKN Theorem6.3 and full proof p34, with the hypotheses carried by B.4.30 and the separately read erratum. This closes the named logarithmic comparison citation gate; the already recorded receiving proof re-derivation retains its own scope.',
 'push:src:B.4.33':'Read and matched IKN Theorems6.2–6.3 and the full mathematical erratum at the exact scope recorded in current_source_matches.json. This supplements the existing complete receiving-proof review and closes the named IKN source gate only.',
 'mapsI:src:A.3.1':'Opened Illman Theorem3.1 printedp48 visually and read the following proof opening; read Knudson Theorem4.1 and full proof p10 and Theorem4.2 and full proof p11. The actual smooth compact finite-involution manifold has finite-dimensional equivariant cells and mod2 coefficients required by Smith. These named external gates close; no entire Illman proof review is claimed.'
}
for label,outcome in entries.items():
 row={'statement_id':label,'date':'2026-11-18','who':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS','type':'exact primary-source check','outcome':outcome}
 if row not in rows:rows.append(row)
with f.open('w',newline='') as o:
 w=csv.DictWriter(o,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(rows)
print('Recorded four scoped source-closure events; total events',len(rows))
