#!/usr/bin/env python3
"""Retain v002 and add the exact angular section for the LM exterior."""
from pathlib import Path

root = Path(__file__).resolve().parent
source = root/'S6_SERIES_PUBLISH_c7_lm_fresh_geometry_v002.py'
target = root/'S6_SERIES_PUBLISH_c7_lm_fresh_geometry_v003.py'
text = source.read_text()
changes = [
    ('local,returns,crit,original_extra = [],[],[],S.zeros(6,1)',
     'local,returns,crit,original_extra = [],[],[],S.zeros(6,1)\n        angular = []'),
    ('                crit.append(v)\n                local.append(',
     '                angular.append(H[:,0])\n'
     '                if i == zero:\n'
     '                    angular.append(H[:,2])\n'
     '                crit.append(v)\n                local.append('),
    ('        product = S.eye(4)',
     '        angular_matrix = S.Matrix.hstack(*angular)\n'
     '        assert angular_matrix[3,:] == S.zeros(1,angular_matrix.cols)\n'
     '        angular_section,angular_U,angular_V = relation_section(angular_matrix[:3,:])\n'
     '        assert angular_matrix*angular_section == E[:,:3]\n'
     '        product = S.eye(4)'),
    ('                      fibre_basis=integers(F),fibre_inverse=integers(F.inv()),',
     '                      angular_matrix=integers(angular_matrix),\n'
     '                      angular_section=integers(angular_section),\n'
     '                      angular_euclid_left=integers(angular_U),\n'
     '                      angular_euclid_right=integers(angular_V),\n'
     '                      fibre_basis=integers(F),fibre_inverse=integers(F.inv()),'),
    ("        print('  PASS all period inverses; integral Cartier gradients; full Euclid relation section; actual critical chains')",
     "        print('  ANGULAR_MATRIX',integers(angular_matrix))\n"
     "        print('  ANGULAR_RIGHT_INVERSE',integers(angular_section))\n"
     "        print('  PASS all period inverses; angular and exterior Euclid sections; integral Cartier gradients; actual critical chains')"),
    ('S6_SERIES_PUBLISH_III_02LM_fresh_geometry_v002.json',
     'S6_SERIES_PUBLISH_III_02LM_fresh_geometry_v003.json'),
]
for old,new in changes:
    assert text.count(old) == 1, old
    text = text.replace(old,new,1)
with target.open('x') as stream:
    stream.write(text)
assert b'\r' not in target.read_bytes()
print('CREATED',target.name,'LINES',len(text.splitlines()))
print('ADDED full angular relation section and its unimodular inverse coordinates')
