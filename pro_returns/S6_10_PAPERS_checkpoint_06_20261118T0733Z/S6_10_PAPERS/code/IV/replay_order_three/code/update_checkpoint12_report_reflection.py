"""Register K45 and the audited source-zero construction progress."""
from pathlib import Path
from datetime import datetime, timezone
import ast
import json
import shutil

root=Path(__file__).resolve().parents[1]
p=root/'code/update_report.py'
s=p.read_text().replace('P3K.40–P3K.44','P3K.40–P3K.45')
old='The actual source-suspension transport across the v=0 component flop is still under proof. Its exact residual contraction prevents identifying omitted-origin labels with ordinary CP3 links without the full periodic quotient.'
new=(
    'The actual source-suspension return across v=0 is still under proof. '
    'Its working construction now has exact full-base Tate and Cartier units, a safe rescaling by a multiple of the full one-gamma exponent, explicit period-equivariant sector fans with independently checked common faces, and the actual default-fan and primitive scalar-chain boundaries. '
    'The two rank-one residual contractions and signed finite-cap chain maps, including both logarithmic deck squares, are retained in the normal analytic quotient construction. '
    'Equivariant regular subdivision and the oriented fixed-stratum boundary computation remain active; neither the lattice index 2N nor a local CP3 value is used as a global link count.'
)
assert s.count(old)==2
s=s.replace(old,new)
old='The later source-loop fan transports, remaining source-moduli loops, added ordinary OS49 clutch sectors and additional unmarked endpoint symmetries remain under their stated scope checks; no uncomputed loop is assigned a class.'
new=(
    'P3K.45 constructs the literal half-source reflection between the two fan families, including the theta line-factor cancellation and physical-height character map. '
    'The two-component source family gives conjugate positive double-loop returns, so the reflected nonfixed diagonal-flop fan has class1. '
    'This conclusion does not assign its separate characteristic pair or an integer derivative. '
    'The other source-loop fan transports, remaining source-moduli loops, added ordinary OS49 clutch sectors and additional unmarked endpoint symmetries remain under their stated scope checks; no uncomputed loop is assigned a class.'
)
assert s.count(old)==2
s=s.replace(old,new)
ast.parse(s)
p.write_text(s)
p=root/'records/progress_check_12_hours.json'
prior=root/'records/progress_check_12_hours_initial.json'
if not prior.exists():
    shutil.copy2(p,prior)
r=json.loads(p.read_text())
r['amended_utc']=datetime.now(timezone.utc).isoformat()
r['reason']=r['reason'].replace('Five newly audited proofs','Six newly audited proofs')
r['main_question_progress'][-1]=(
    'P3K.45 proves the actual half-source reflection conjugacy for the two fan families and computes class1 for the reflected nonfixed diagonal flop. The general simultaneous seam extension remains open; its marked-pole degrees(+3,-3) are retained.'
)
p.write_text(json.dumps(r,indent=2)+'\n')
print('Registered K45, the actual source-zero construction progress, and the amended twelfth-hour decision.')
