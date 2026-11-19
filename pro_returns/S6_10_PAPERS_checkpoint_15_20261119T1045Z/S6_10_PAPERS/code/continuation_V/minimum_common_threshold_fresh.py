"""New exact common-threshold verification of the already fresh interval leaves."""
from pathlib import Path
import sys,json,hashlib
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'build/continuation_numeric/python'))
from flint import arb,ctx
ctx.dps=150
base=Path(__file__).parent
threshold='-1.0945402503114027801162682630549457037'
bound=arb(threshold)
inputs={name:json.loads((base/name).read_text()) for name in ['minimum_root_regions.json','minimum_cusp_regions.json','minimum_collar.json','infinity_and_splitting.json']}
root=inputs['minimum_root_regions.json'];cusp=inputs['minimum_cusp_regions.json'];collar=inputs['minimum_collar.json'];inf=inputs['infinity_and_splitting.json']
sets={name:d['accepted'] for name,d in root['root_regions'].items()}
sets['cusp_annulus']=cusp['annulus']['accepted'];sets['collar']=collar['accepted']
out={'threshold_exact_decimal':threshold,'h_infinity_strictly_below_threshold':bool(arb(inf['h_b_infinity'])<bound),'regions':{},'inputs':{}}
assert out['h_infinity_strictly_below_threshold']
for name,leaves in sets.items():
    tests=[bool(arb(leaf['h'])>bound) for leaf in leaves]
    assert all(tests),(name,[i for i,v in enumerate(tests) if not v][:5])
    out['regions'][name]={'leaves':len(tests),'all_strictly_above_exact_threshold':all(tests)}
out['inner_cusp_sample_strictly_above_threshold']=bool(arb(cusp['inner_height'])>bound)
assert out['inner_cusp_sample_strictly_above_threshold']
for name in inputs:
    p=base/name;out['inputs'][name]={'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
out['scope']='Fresh postprocessing of every already independently computed interval leaf. This supplies one common exact rational threshold; it is not a substitute for the analytic domain/height argument.'
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='inputs'},indent=2))
