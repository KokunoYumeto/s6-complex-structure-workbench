#!/usr/bin/env python3
"""Record the bounded selector and input-identity clarification; no calculation rerun."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import difflib

ROOT = Path(__file__).resolve().parents[1]
path = ROOT/'agents/continuation7_iii_corrected_initial_receiving/S6_SERIES_PUBLISH_III_02LU_post_exposure_derivation.md'
before = path.read_text()
assert sha256(path.read_bytes()).hexdigest() == '6923c85e7b38d91afa535ea7f53825094a5c8bf916c11d2de662b62da6b40a70'
anchor = 'For the 16 OS45 inputs the historical audit checks the displayed group\n'
addition = '''The literal default divisor at these 42 inputs is also zero. This is
an attributed bounded source check from the authorized LS checker, not a
new exposure of the LS historical program in this lane. At p=0 its
solve_local has c=e_(labels[p])-e_(labels[0])=0, hence rhs=0. The already
authorized LN integer_solution initializes every Smith solution coordinate
to zero and returns V times that vector. Its selector therefore adds no
kernel term. The LS source SHA256 supplied by that checker is
db309494e50559a43d52fec581c425c8c237a46702b3b5d81c642d199cd645c2;
the named LN helper source SHA256 is
f581acf2eaef5e40001ad8b27d6f93be7b213e9b42831853213e6dc227c5d669.

The finite affine input rule agrees literally as well. The authorized
old rankone_families decomp and the frozen fresh LN smith both evaluate

    smith_normal_decomp(DomainMatrix.from_Matrix(A-I).convert_to(ZZ))

on the same integer matrix, and both return the ordered kernel columns
F=V[:,rank:] without a subsequent basis operation. The fresh integer()
only checks integrality and copies the matrix. Thus their ordered F,
not merely its integer span, is identical. The fresh reader is the
corresponding row block of V^(-1); the old reader is a second Smith
left inverse of F. Both compose with F to the identity. Every norm
column and each candidate v lies in im(F), so the two readers give
exactly the same integer coordinates there. Their Hermite matrix H
and vector order*H^(-1)*coordinates(v) consequently agree. The remaining
primitive and divisibility tests are the same displayed gcd tests.
The supplied local order equals the minimal finite order of A in both
functions. Finally both enumerate product(range(-3,4),repeat=2) in the
same order and use m=order. The first accepted v is therefore the same
literal marked vector; it is printed in every new OLD_OVERLAP record.

This is a source-level identity of the two deterministic selectors,
with the same Smith routine, rather than an inference from equal groups.
The old audit JSON has no retained affine-vector fields for the 42
overlaps and no old runtime-version or stdout record was recovered;
no separate recovery of such absent execution metadata is claimed.
The already authorized old helper hashes are
c61db918ba5e4552a9f81c7a4c14e980e5decc317f77496fbc17b214a77d781a
(weighted_profiles, bounded lines 1--79) and
f2c80dfca5aac28e17f090e9873bb9b1da52583584a086882a775081bd4458d0
(rankone_families, bounded lines 1--100). The fresh LN source hash is
9639dd5997dd9868224ca1ac308d286642f008f975fc6911af7fd52583413f26.
No historical helper was imported or rerun for this comparison.

'''
assert before.count(anchor) == 1
after = before.replace(anchor, addition+anchor)
old = '''Its section inserts a zero final coordinate. The error in the other
composite is minus tau_(N-1) times the sum relation. The integer column
'''
new = '''Its section S inserts a zero final coordinate. Precisely,
S P-id=-tau_(N-1) times the peripheral-sum vector, while P S=id.
The integer column
'''
assert after.count(old) == 1
after = after.replace(old, new)
print('START', datetime.now(timezone.utc).isoformat())
print(''.join(difflib.unified_diff(before.splitlines(True), after.splitlines(True),
                                   fromfile='postnote-before', tofile='postnote-after')), end='')
path.write_text(after)
print('LINES', len(after.splitlines()))
print('SHA256', sha256(path.read_bytes()).hexdigest())
print('END', datetime.now(timezone.utc).isoformat())
