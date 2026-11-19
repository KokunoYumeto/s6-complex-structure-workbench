"""Update the live report with the seven completely audited proofs."""
from datetime import datetime, timezone
from pathlib import Path
import ast
import hashlib
import json
import shutil

root = Path(__file__).resolve().parents[1]
path = root / 'code/update_report.py'
old = path.read_text()
start = 'The subsequent ordinary-product working proof fixes the connecting sign'
end = 'no uncomputed loop is assigned a class.'
replacement = (
    'P3K.50 proves the actual ordinary-product fixed-C0 coordinates(6,-6,1), variation0 and ambient derivative-12 by the explicit D3-cylinder extension with its boundary orientation. '
    'P3K.51 computes the complete ordinary-product variation V=[[0,6,-6],[6,0,0],[-6,0,0]] from the actual circle traces, their vertex caps and the signed chain-prism identity. '
    'P3K.52 computes the full stable derivative delta=(-12,-12,0), using the universal covering group of GL+ and its normalized third form; its actual native nonfixed triples are(0,-6,1) and(-6,0,1). '
    'P3K.53 constructs a proper smooth disc extension through the unselected source collision v=1/8, retaining the translation flow, Hom divisor, complete root characters and full cap overlap; its positive return is zero in the specified one-cap whole-zero family. '
    'P3K.54 computes the three actual first periodic flops as classes(23,23,1), with the native Cox maps, complex-normal reset and inverse comparisons. '
    'P3K.55 constructs the ordinary product on every integral lattice-basis fan by the literal source/line characters and period changes, retaining every unit. Its local orbit degrees and full stable-derivative traces give exact integral relations for the actual variation and derivative; the remaining transverse entries and central return are not inferred. '
    'P3K.56 proves the selected-cusp positive return s(n)=1-3n(n-1) modulo28 on every fan containing the physical vertical edge. Its actual adjacent flop maps give the formula for every signed integer n, its exact period28 and its range{1,7,9,11,15,21,23,25}. '
    'The source-infinity working construction now supplies an actual partial filling away from the selected cusp, with the changed-origin parameter deck, both collision chains and the full finite-cap attachment. Its relative circle-quotient excision comparison and fixed-surface determinant pairing are undergoing complete-map audit; no infinity value from that draft is included among the proved results. '
    'The global rho-family working relation retains both source-zero fan objects, every scalar closing arrow, the half-source period/reflection map and the full infinity source/Cartier/root dictionary. Individual source-zero returns, the general source-loop fan formula beyond the proved vertical-edge sector, remaining source-moduli loops, added ordinary OS49 clutch sectors and additional unmarked endpoint symmetries remain under proof; no uncomputed loop is assigned a class.'
)
assert "'" not in replacement
assert old.count(start) == 2
new = old
for _ in range(2):
    a = new.index(start)
    b = new.index(end, a) + len(end)
    new = new[:a] + replacement + new[b:]
new = new.replace('P3K.40–P3K.49', 'P3K.40–P3K.56')
ast.parse(new)
dest = root / 'records/checkpoint14_prior_report'
dest.mkdir(exist_ok=True)
for name in ['code/update_report.py', 'S6_06_BLIND_report.md', 'S6_06_BLIND_results.csv']:
    target = dest / Path(name).name
    assert not target.exists(), target
    shutil.copy2(root / name, target)
path.write_text(new)
record = {'utc': datetime.now(timezone.utc).isoformat(),
          'new_proved_statements': [f'P3K.{i}' for i in range(50,57)],
          'report_generator_before_sha256': hashlib.sha256(old.encode()).hexdigest(),
          'report_generator_after_sha256': hashlib.sha256(new.encode()).hexdigest(),
          'scope': 'Both source-zero global attachment and infinity excision remain explicitly unpromoted in this checkpoint report.'}
(root / 'records/checkpoint14_report_update.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
