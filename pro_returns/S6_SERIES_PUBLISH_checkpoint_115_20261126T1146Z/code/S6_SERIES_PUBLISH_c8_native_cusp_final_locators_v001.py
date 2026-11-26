"""Apply the two bounded final readback corrections, with exact local rows."""
import csv
import hashlib
from pathlib import Path
import S6_SERIES_PUBLISH_c8_integrate_units as units

root = Path(__file__).resolve().parent.parent
folder = root / 'agents/continuation8_iii_integration/units/root'
lane = root / 'agents/continuation8_iii_weighted_units'
changes = [
    ('cusp_nullbordism', '1924c72ac17006e008cfaac1fa7a416bbf956c9c466342e13de17a66fb1004c9',
     'CUSP_NULLBORDISM', 'CUSP', 23, 'wb:def:marked-cusp-nullbordism-data',
     r'\SeriesRef{mapsI:src:A.1.2}; its quotient projection is a local',
     r'\SeriesRef{fam:src:A.3.1}; its quotient projection is a local',
     ['D06', 'D18'],
     'Direct bounded Paper I reading showed mapsI:src:A.1.2 proves the toric chart and character limits. The exact full-period free properly discontinuous action on every toric stratum is proved in fam:src:A.3.1 proof item2 (current Paper I8386-8452). Replace only the locator; the actual action and quotient assertion are unchanged.'),
    ('full_sphere_nullity', '722fb631de909e575d2fdab4da37cfce2ee61442a7b17fec5778198d8bacfa30',
     'NATIVE_SPHERE', 'NATIVE-SPHERE', 31, 'wb:cusp-s12-one-copy-invariant',
     '$(r,c_1,c_2)$. That framed fibre represents $[g]$, and its sixfold\nframed product represents $E^6[g]$, so the framing determines the\ndisplayed coefficient.',
     '$(r,c_1,c_2)$. That framed fibre represents $[g]$. Its product\nwith an interior point of the ordered six-cell, with the six\ncoordinate normal vectors, represents $E^6[g]$. Thus the framing\ndetermines the displayed coefficient.',
     ['D20', 'D26'],
     'Name the actual product used in the full proof: N times one interior point of the six-cell, with its six ordered normal vectors. This precision preserves the exact suspension map and avoids an ambiguous shorthand for the displayed product.')
]
for name, sha, prefix, stem, number, owner, old, new, kinds, reason in changes:
    path = folder / (name + '.tex')
    before = path.read_text()
    assert hashlib.sha256(path.read_bytes()).hexdigest() == sha
    assert before.count(old) == 1
    line = before.count('\n', 0, before.index(old)) + 1
    after = before.replace(old, new, 1)
    units.check_permanent_identifiers(before, after)
    table = lane / ('S6_SERIES_PUBLISH_' + prefix + '_publication_defects.tsv')
    with table.open(newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        fields = reader.fieldnames
        rows = list(reader)
    for row in rows:
        if prefix == 'NATIVE_SPHERE':
            row['reason'] = row['reason'].replace('shared marked cusp data remain in Q257', 'shared marked cusp data remain in Q258')
        row['review_status'] = 'whole final source read, including all bounded follow-up changes; source-local complete; actual placement and global gates remain root'
    for kind in kinds:
        rows.append(dict(zip(fields, [
            f'III-C8-{stem}-PUB-{number:03}-{kind}', kind, owner,
            f'{name}.tex sequential line {line}', 'pending page concordance',
            'root/' + name + '.tex', 'pending final build', old, new, reason,
            'bounded final correction read with complete final source; source-local complete; actual placement/global gates remain root'
        ])))
    temporary = path.with_suffix('.tex.tmp')
    temporary.write_text(after, encoding='utf-8', newline='\n')
    temporary.replace(path)
    temporary = table.with_suffix('.tsv.tmp')
    with temporary.open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)
    temporary.replace(table)
    print('BOUNDED_CHANGE', name, number, ','.join(kinds))
    print('OLD', old)
    print('NEW', new)
    print('FINAL', len(after.splitlines()), hashlib.sha256(after.encode()).hexdigest(), 'DEFECT_ROWS', len(rows))
print('IDENTITIES_PRESERVED; CANONICAL_AND_SHARED_WRITES 0; INDEPENDENT_CHECK_CREDIT 0')
