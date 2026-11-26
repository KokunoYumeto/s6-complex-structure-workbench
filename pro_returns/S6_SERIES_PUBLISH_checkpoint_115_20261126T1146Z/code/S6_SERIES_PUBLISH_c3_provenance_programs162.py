#!/usr/bin/env python3
"""Prepare exact section-ten program paths; do not edit or execute shared material."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation3_provenance'
data = json.loads((ROOT.parents[1] / 'tmp/c3_programs/programs162_metadata.json').read_text())
source = (ROOT / 'S6_SERIES_PUBLISH_II.tex').read_text()
table = source[source.index(r'\section*{Programs}'):source.index(r'\begin{thebibliography}')]
inventory = set((ROOT.parent / 'REPOSITORY_PROGRAM_PATHS.txt').read_text().splitlines())
for row in data:
    assert row['printed_path'] == row['repository_path']
    assert row['repository_path'] in inventory
    assert Path(row['repository_path']).name not in table
    content = Path(row['local_path']).read_bytes()
    assert len(content) == row['bytes']
    assert hashlib.sha256(content).hexdigest() == row['sha256']
    for path in OUT.glob('*records*II*.tsv'):
        if path.name == 'S6_SERIES_PUBLISH_records_II_additions162.tsv':
            continue
        with path.open(newline='') as f:
            for existing in csv.DictReader(f, delimiter='\t'):
                assert existing.get('sha256') != row['sha256'], (path, existing)

scopes = [
    r'Mixed-cycle edge frames, primitive normal periods and the horizontal translation (\cref{ex:II:three-hopf-cycle,cdp:st:C.2.UN.57})',
    r'Rooted restriction matrices, the integral Chern extension and analytic torsor periods (\cref{cdp:st:C.2.UN.61})',
    r'Primitive core periods and nested insertion orders (\cref{cdp:st:C.2.UN.61})',
    r'The real-linear period map, its inverse, determinant and frame at infinity (\cref{lem:II:logarithmic-period-family})',
    r'Weighted periods, finite actions and conjugate frames (\cref{cdp:st:C.2.UN.59})',
    r'Hopf-cycle matrices, affine translations and finite-secondary period divisors (\cref{ex:II:three-hopf-cycle,cdp:st:C.2.UN.48})',
    r'Inverse root charts, canonical orders and the quasi-bundle example (\cref{cdp:st:C.2.UN.62})',
    r'Root multiplicities, inertia groups, resolution charts and finite quotient actions (\cref{cdp:st:C.2.UN.52})',
    r'Weighted restriction matrices and their dual residue vectors (\cref{cdp:st:C.2.UN.54})',
    r'Canonical heights, root congruences, finite-orbit gauges and collar maps (\cref{cdp:st:C.2.UN.58})',
    r'Primitive fibre bases, two-mark Picard lattices and recursive insertion identities (\cref{cdp:st:C.2.UN.60})',
    r'Period determinants, conjugate Hopf frames and finite angular characters (\cref{lem:II:logarithmic-period-family,cdp:st:C.2.UN.57})',
    r'Hopf-star degree equations, weighted maps, canonical forms and core periods (\cref{cdp:st:C.2.UN.53})',
]
details = [
    'Full 91-line source. Builds the cyclic list of a copies of (1,0), then b copies of (0,-1), for 1<=a,b<=13; computes the two Hopf and a+b-2 ruled frames and edge maps, primitive divisor gcd(a,b), symbolic real determinant ell*(b*A+a*B), and a positive numerical instance. Also checks preservation of the horizontal translation under all-ruled normal changes. Conductor moves this explicit family into P332 and retains the general cycle owner UN57 with UN51 as an alias.',
    'Full 92-line source. Tests rooted chains, stars and binary-shaped trees with at most ten nonroot vertices and selected integer restriction coefficients; computes restriction/ordinary-incidence ranks and weighted height identities. Symbolically checks the full integral Chern-extension group law and its commutator, the analytic torsor determinant Im(tau)*Im(omega), and the specified equal/unequal leaf-height examples.',
    'Full 39-line source. Symbolically computes the determinant for the primitive elliptic core and its nonzero coefficient. Checks weighted insertion substitutions for m=1,...,15 and displacement orders m,...,24, including the ordinary cap order drop. Global pruning and reinsertion remain in the receiving proof.',
    'Full 77-line source. Symbolically retains both real line characters and arbitrary horizontal translation in the period determinant and inverse formula; checks the O(1)^2 frame at infinity, rank-one unipotent monodromy and its inverse. The displayed positivity is the algebraic determinant expression with the stated logarithmic substitution. P331 is the receiving owner of these formulas.',
    'Full 100-line source. Checks the unitary finite-action equivariance of the period map, the exact rational normal correction in affine overlaps, infinity linear/translation frames, the symbolic real determinant, explicit cyclic elliptic actions of orders2,3,4,6, and transport exponent arithmetic through N=120. The general weighted filling is owned by UN59.',
    'Full 121-line source. Computes the two-component product, the explicit three-component matrices/contraction logarithms and affine correction, and the common normal sum/primitive divisor. Uses Hermite bases to compare finite-secondary lattices through order24 and repetitions1,...,6, plus the specified free three-component quotients. P332 owns these concrete examples; UN48 owns the realization.',
    'Full 55-line source. Checks signed inverse-root divisor frames through m=60, canonical pole bounds through m=80,k=120, the specified two-core/four-leaf incidence matrix and residue vector, and the four-triple-fibre plurigenus arithmetic. It does not replace the general quasi-bundle construction.',
    'Full 98-line source. Computes Bezout root/inertia data for a,b=1,...,24 and root multipliers1,...,6, bounded invariant monomials, resolution chart transitions through h=24, finite angular lattices through order60, and the exact quadratic action on the three neck maps. General statements remain in UN52.',
    'Full 83-line source. Computes one branched unicycle with nonconstant restriction coefficients and its dual residue vector, the changed-holonomy rank, the symbolic two-component determinant, and cycle lengths2,...,8 with tails0,...,4. The cohomological construction is in UN54.',
    'Full 79-line source. Solves the specified nine-vertex canonical-height system and a mismatched leaf example, root congruences through m=40, symbolic finite-orbit gauge sums for m=2,...,20, and collar substitutions through m=20. The source expressly treats these as equation checks; no occurrence inference is assigned to it.',
    'Full 76-line source. Computes primitive fibre-basis changes for coordinates -5,...,5, two-mark Picard Smith forms for orders1,...,20, recursive weighted maps for coprime orders1,...,8 and five displacement orders each, and one full nested record including the product cap. The general pruning/reinsertion maps remain in UN60.',
    'Full 79-line source. Computes the symbolic period determinant with full horizontal translation, arbitrary complex Hopf frames and contraction-log conjugacy, free finite angular pairs through order24, and the infinity logarithmic coefficient. Its subsequent historical CSV-writing code was read and was not executed. P331 and UN57 own the mathematical inputs/applications.',
    'Full 96-line source. Enumerates bounded degree equations for p,q<=50 and m<=10, computes the line-swap logarithmic character, and checks weighted maps, invariant canonical forms, exact core translations/periods and central contraction types for r<=8 and five displacement orders, including free finite-secondary cases through order12. Its subsequent historical CSV-writing code was read and was not executed.',
]
new = ''.join(scope + r' & \nolinkurl{' + row['repository_path'] + r'} \\[3pt]' + '\n'
              for scope, row in zip(scopes, data))
(OUT / 'S6_SERIES_PUBLISH_c3_provenance_program_rows162.tex').write_text(new, newline='\n')
anchor = '\\end{longtable}}\n\n\\begin{thebibliography}'
assert source.count(anchor) == 1

def write(name, rows):
    with (OUT / name).open('w', newline='') as f:
        w = csv.DictWriter(f, list(rows[0]), delimiter='\t', lineterminator='\n')
        w.writeheader()
        w.writerows(rows)

write('S6_SERIES_PUBLISH_c3_provenance_program_edits162.tsv', [dict(
    change_id='II-C3-PROV-162', type='D09',
    statement_id='cdp:st:C.2.UN.48;cdp:st:C.2.UN.52;cdp:st:C.2.UN.53;cdp:st:C.2.UN.54;cdp:st:C.2.UN.57;cdp:st:C.2.UN.58;cdp:st:C.2.UN.59;cdp:st:C.2.UN.60;cdp:st:C.2.UN.61;cdp:st:C.2.UN.62;lem:II:logarithmic-period-family;ex:II:three-hopf-cycle',
    old_location='Programs: end of table', old_page='source guard; final concordance pending',
    new_location='Programs: marked cycles, roots and trees', new_page='integrated build pending',
    old_text=anchor, new_text=new + anchor,
    reason='All thirteen complete pinned program sources were opened, read and matched to exact attached-inventory paths. None appears under its basename or mapped source hash in the current appendix. The receiving owner maps were coordinated with the conductor agent, including P331/P332 and UN51\'s receiving alias at UN57. The table names their actual finite or symbolic computations; complete global proofs remain in their receiving owners. Body filename removal belongs to conductor\'s units and is not performed here.',
    review_status='All thirteen sources read in full, including output/CSV code; path, byte, SHA256 and duplicate checks passed. No program execution or full consumer-proof reading by this agent is claimed. P331/P332 must be admitted with or before these rows.')])
write('S6_SERIES_PUBLISH_records_II_additions162.tsv', [
    {key: row[key] for key in ['printed_path', 'repository_path', 'sha256']} for row in data])
write('S6_SERIES_PUBLISH_c3_provenance_program_checks162.tsv', [dict(
    printed_path=row['printed_path'], repository_path=row['repository_path'],
    sha256=row['sha256'], bytes=row['bytes'], checked_at=row['url'],
    mathematical_scope=scope, exact_extent=detail,
    date_utc=datetime.now(timezone.utc).isoformat(),
    outcome='Exact attached-inventory path and prescribed pinned bytes verified; complete source read; no appendix or mapped-hash duplicate; no execution.')
    for scope, detail, row in zip(scopes, details, data)])
print('Prepared addition162: thirteen exact rows; shared source unchanged; no cited program executed.')
