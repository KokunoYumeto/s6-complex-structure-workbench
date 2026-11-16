"""Record the exact essential-component comparison and its independent audit."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json

root = Path(__file__).resolve().parents[1]
p = root / 'records/root_results.csv'
with p.open(newline='') as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    rows = list(reader)
row = {
    'id': 'C.2.UN.14',
    'statement': 'For each fixed marked punctured torus family, the multisets of non-uniruled normalization classes occurring in smooth fillings are identical for every prescribed even fibre Euler number',
    'status': 'Proved',
    'where_proved': 'sections/part_C2_zero_essential.tex',
    'depends_on': 'C.2.UN.1; C.2.UN.4; actual strict-transform and exceptional-projective-bundle maps',
    'item_of_the_prompt': 'C.2',
    'findings_of_the_survey_settled (F-numbers)': 'F16',
    'notes': 'Exact multiset equality, with a bijection and the old full-fibre multiplicities preserved by explicit vertical blowups. Compact simultaneous version included. Does not assume a comparison between unrelated fillings. Independent A audit accepted.'
}
rows = [r for r in rows if r['id'] != row['id']] + [row]
with p.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

record = root / 'records/root_research_essential_components.md'
record.write_text('''# Essential components and the unrestricted zero-Euler problem

UN14 proves equality of the finite multisets of bimeromorphism classes of non-uniruled normalization resolutions occurring in fillings of one fixed marked punctured torus family, for every prescribed even Euler value. Its actual comparison is the finite sequence of smooth vertical blowups from UN4. Strict transforms are bimeromorphic through their graph resolutions, their generic multiplicities are retained, and every newly introduced component is a projective plane or a projective line bundle over a smooth curve. Such components remain uniruled after subsequent blowups. The same exact operation works simultaneously over the finitely many critical values of a compact base. A independently audited and accepted the complete proof, including the Hartogs pluricanonical argument that places general-type classes among the non-uniruled classes.

The root independently opened Kollár, Moishezon morphisms, arXiv2102.02614v1, Conjecture4 and Comments4.1. It also opened Chen–Rao–Tsai arXiv2506.12670v2, dated23April2026. The latter's specialization theorems assume locally Moishezon families; its general analytic fibrewise assertions start with an actual bimeromorphic map. Neither assertion was silently extended to an arbitrary torus filling. A records the exact theorem numbers in A_reducible_literature.md.

The root additionally opened Kajiwara–Kato–Nakayama, Logarithmic Abelian Varieties, PartI, J.Math.Sci.Univ.Tokyo15(2008),69–193, Theorem0.1 and the proper-model discussion in Section1.1. The equivalence there is between log complex tori and log Hodge structures. Applying it to a given analytic filling would still require construction of its comparison morphism to the specified log object. No such comparison has been assumed. The primary URL is https://www.ms.u-tokyo.ac.jp/journal/pdf/jms150104.pdf .

Searches run for this stage: “degenerations complex tori general type”; “degenerations of complex tori components classification”; “degeneration complex torus surfaces Hopf Kodaira Fujimoto central component”; “degeneration torus general type component analytic”; “degeneration complex tori non-Kähler”. Search results were used as leads; theorem claims were checked in primary papers. No priority claim is made.

The new semicomplete-vector-field attack is being proved separately by D as UN15. The root opened Guillot2019, arXiv1603.02288v2, MainTheorem and Definition5, and Guillot2024, On the singularities of complete holomorphic vector fields in dimension two, including the closed-locus section. A independently checked the targeted cyclic-cover and order-cancellation maps. E is auditing the complete reduction. At this record's creation that theorem is under proof audit, not yet counted as settled here.
''')
p = root / 'S6_03_CDP_report.md'
s = p.read_text().replace('C.2.UN.1–13; A.5.18–21', 'C.2.UN.1–14; A.5.18–21')
marker = '## Exact essential-component comparison'
if marker not in s:
    s += '''
## Exact essential-component comparison

C.2.UN.14 proves that fixing an even Euler number imposes no additional restriction on the multiset of non-uniruled normalization classes occurring in a fixed marked punctured torus family: its sets of possible multisets are exactly equal for every even Euler value. The proof uses the actual UN4 blowdowns and preserves the old generic multiplicities; new components are uniruled. The compact simultaneous version makes every fibre zero-Euler while preserving all these classes. A independently audited this statement. It reduces the occurrence of a specified general-type normalization in the zero-Euler classification to its occurrence in any filling, with the required comparison maps.
'''
p.write_text(s)
print(json.dumps({'utc': datetime.now(timezone.utc).isoformat(),
                  'statement': row['id'], 'audit': 'accepted',
                  'remaining': 'unrestricted reducible zero-Euler geometric classification'}, indent=2))
