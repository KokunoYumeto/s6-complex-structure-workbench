"""One-time catalogue/report update after the A.4.8 independent referee."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
report = root/'sections'/'AB_push_report.md'
text = report.read_text()
changes = {
'Euler number, fundamental group, H1 and nearby Euler function are proved for every toroidal output, including nonreduced centres. Complete integral homology is proved for Q, the two minimal models and the infinite maximal-cone star subclass; higher integral homology for every arbitrary fan remains open. Classical Kähler Clemens–Schmid hypotheses fail. | A.4.1–A.4.7':
'Euler number, fundamental group, every integral homology group and nearby Euler function are proved for every toroidal output, including nonreduced centres; all homology is free. The formula uses integral reference maps and toroidal weak factorization. A second direct normalization-stratification chain computation for every arbitrary fan remains a verification task. Classical Kähler Clemens–Schmid hypotheses fail. | A.4.1–A.4.8',
'All outputs have pi1=Z, central Euler11k+t4 and nearby Euler2. Uniform blow-up normalizations and higher integral homology of every further model remain open. | B.2.1–B.2.3; A.2.4; A.4.7':
'All outputs have pi1=Z, central Euler11k+t4, explicit torsion-free integral homology and nearby Euler2. Uniform blow-up normalizations and a second direct integral chain computation remain to be supplied. | B.2.1–B.2.3; A.2.4; A.4.7–A.4.8',
'The unresolved part is a uniform blow-up presentation and complete integral topology for every such output, not existence of those toroidal families. A.4.6 supplies those geometric and topological answers for the infinite family of disjoint maximal-cone star subdivisions.':
'A.4.8 determines all integral homology groups: writing k for pure-top ray orbits, m for mixed ray orbits and t4 for maximal-cone orbits, the free Betti tuple is (1,1,8+k+m,7,9k+t4−2m−1,0,k+m). A uniform blow-up presentation and a second direct integral incidence computation for every arbitrary output remain to be supplied.',
'and the new unrestricted fan/gluing construction in A.2.4. The E agent':
'and the new unrestricted fan/gluing construction in A.2.4. D also opened the original AKMW and Matsuki factorization theorems and passed the full A.4.8 proof, including finite analytic scope, every centre type, hidden-stabilizer exclusion, noncompact blow-up splitting and the reference normalization maps. The E agent',
'| `ab_push_catalogue.py` | Statement ledger with the required eight columns. | `.out` |':
'| `ab_push_all_fan_homology.py` | Exact full reference normalization matrices and Smith forms for n=1,2,3,4,6,12; thirteen blow-up centre checks and all33 certified fan examples. | `.out`, `.json` |\n| `ab_push_update_homology_ledger.py` | One-time report and catalogue update after A.4.8. | `.out` |\n| `ab_push_catalogue.py` | Statement ledger with the required eight columns. | `.out` |',
'Three text patches failed validation before modifying files (a missing patch-line prefix; duplicate operations on a report filename; an outdated B.2.2 context); each was reapplied in valid smaller pieces.':
'Five text patches failed validation before modifying files (a missing patch-line prefix; duplicate operations on a report filename; an outdated B.2.2 context; two partial-line contexts during the A.4.8 ledger update); each was reapplied in valid smaller pieces or by an exact asserted text-update script.',
'The higher integral homology for arbitrary outputs remains open. The separate B.3.8':
'A.4.8 now determines the full free integral homology of every output by reference normalization maps and toroidal weak factorization. Its proof explicitly permits temporary pure-q blow-ups and uses only the finite cone-complex theorem, realized by analytic monomial ideals; it does not assume an unstated general relative analytic factorization theorem. The direct normalization/stratification incidence matrices of every arbitrary fan remain a second-computation task. The separate B.3.8'
}
for old,new in changes.items():
    assert text.count(old)==1,old[:100]
    text=text.replace(old,new)
report.write_text(text)

catalogue = root/'code'/'ab_push_catalogue.py'
text = catalogue.read_text()
changes = {
'the uniform normalization blow-up description and full integral topology remain open.':
'the uniform normalization blow-up description remains open; A.4.8 determines every integral homology group.',
'Compute the integral central topology for every unrestricted invariant smooth refinement parametrized in A.2.4.':
'Give a second direct integral normalization-stratification incidence computation for every unrestricted fan; all group values are determined by A.4.8.',
'Normalization and stratum charts are explicit; complete integral topology is proved for Q, the two minimal models and the infinite maximal-cone star subclass, but not every arbitrary output.':
'A.4.8 proves all group values using reference normalization maps and toroidal weak factorization; A.4.7 gives an independent stratum Euler count. The prompt also requests an independent full integral incidence calculation for every arbitrary output.',
'Give the uniform normalization blow-up description and integral topology for every further invariant smooth cusp subdivision.':
'Give the uniform normalization blow-up description and a second direct integral incidence calculation for every further invariant smooth cusp subdivision.',
'the remaining scope matches A.2.3 and A.4.5.':
'A.4.8 now determines all homology groups; the remaining description and independent-computation scope matches A.2.3 and A.4.5.'
}
for old,new in changes.items():
    assert text.count(old)==1,old[:100]
    text=text.replace(old,new)
catalogue.write_text(text)
print('Updated report and catalogue after the independently reviewed A.4.8 theorem.')
