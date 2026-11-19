"""Independent cellular accounting for the explicit blow-up disc bundle.

No earlier blow-up or topology verifier is imported. Actual beta maps and
Mayer--Vietoris identifications are in the frozen written proof.
"""
from pathlib import Path
import hashlib
import json

# CP3 has one cell in each even dimension through six; every cellular
# differential is zero because neighboring odd cell groups vanish.
projective_cells=[1 if k in [0,2,4,6] else 0 for k in range(9)]
ball_homology=[1]+[0]*8
sphere_homology=[1]+[0]*6+[1,0]
assert sum((-1)**k*n for k,n in enumerate(projective_cells))==4
assert sum((-1)**k*n for k,n in enumerate(ball_homology))==1
assert sum((-1)**k*n for k,n in enumerate(sphere_homology))==0
extra=[projective_cells[k]-ball_homology[k] for k in range(9)]
assert [k for k,n in enumerate(extra) if n]==[2,4,6]
assert all(extra[k]==1 for k in [2,4,6])
assert sum((-1)**k*n for k,n in enumerate(extra))==3
out={'status':'all exact cellular assertions passed',
     'disc_bundle_retraction_cell_ranks':projective_cells,
     'sphere_boundary_homology_ranks':sphere_homology,
     'beta_kernel_free_ranks':extra,'Euler_change':3,
     'scope':'Projective-cell and Euler counts only; beta splitting including torsion is proved through the actual pair and Mayer--Vietoris maps.',
     'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
