#!/usr/bin/env python3
"""Aggregate the new independent numerical certificates and exact comparisons."""
from pathlib import Path
import json,hashlib,sys
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'build/continuation_numeric/python'))
from flint import arb,ctx
ctx.dps=110
here=Path(__file__).parent
names=['minimum_root_regions','minimum_cusp_regions','minimum_collar','period_root_method','central_hessian_refined','extension_normalization']
d={n:json.loads((here/(n+'.json')).read_text()) for n in names};assert all(j['status']=='PASS' for j in d.values());numbers=json.loads((here/'infinity_and_splitting.json').read_text());h=arb(numbers['h_b_infinity']);h_original=arb(numbers['h_original_infinity']);prior=json.loads(Path('/workspace/scratch/ae06852560d6/materials/S6_10_PAPERS_2_night_run/night_run/code/part1/minimum_certificate_summary.json').read_text());assert h>arb(prior['h_min']['lower']) and h<arb(prior['h_min']['upper']);assert h_original>arb(prior['h_original_min']['lower']) and h_original<arb(prior['h_original_min']['upper']);cubic=[arb(x) for x in d['minimum_cusp_regions']['inner_cubic_lower_bounds']];assert all(x>0 for x in cubic)
files=['period_balls','infinity_and_splitting',*names];manifest={}
for stem in files:
 for suffix in ['.py','.json']:
  f=here/(stem+suffix);manifest[str(f.relative_to(ROOT))]={'size':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()}
out={'status':'PASS','date':'2026-11-19','scope':'All newly computed constants and global-minimum numerical regions; the logical use of the period model, height and symmetries is a separate proof review. No earlier producing program was imported. Earlier rectangle coordinates were reevaluated as finite witnesses.','h_b_infinity':str(h),'h_original_infinity':str(h_original),'within_both_printed_certified_intervals':True,'within_all_printed_hessian_intervals':d['central_hessian_refined']['within_all_printed_Hessian_bounds'],'positive_cusp_cubic_lower_bounds':[str(x.lower()) for x in cubic],'new_leaf_counts':{'infinity':d['minimum_root_regions']['root_regions']['infinity']['passed'],'zero':d['minimum_root_regions']['root_regions']['zero']['passed'],'cusp_annulus':d['minimum_cusp_regions']['annulus']['passed'],'collar':d['minimum_collar']['accepted_count']},'second_period_method':d['period_root_method']['comparisons'],'manifest':manifest}
(here/'minimum_certificate_renewal.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
