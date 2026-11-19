"""Retain the proved regularization and the remaining marked cap square."""
from pathlib import Path
import ast

root=Path(__file__).resolve().parents[1]
p=root/'code/update_report.py'
s=p.read_text()
old='Equivariant regular subdivision and the oriented fixed-stratum boundary computation remain active; neither the lattice index 2N nor a local CP3 value is used as a global link count.'
new=(
    'The relative barycentric orbit separator and exact integral star-subdivision algorithm now prove an equivariant regular subdivision preserving the actual I,W,E boundaries. '
    'The finite cone-orbit export and oriented fixed-stratum boundary computation remain active. '
    'The old source-coordinate loop also requires its exact finite-cap endpoint comparison: v=u^3, T=u^4*t and z_old^m=u^4*z_new^m retain a threefold source covering and a root rotation. '
    'The generic suspension scalar cancellation does not replace that character square. '
    'Neither the lattice index 2N nor a local CP3 value is used as a global link count.'
)
assert s.count(old)==2
s=s.replace(old,new)
ast.parse(s)
p.write_text(s)
print('Recorded the proved regularization and exact outstanding original-source cap square.')
