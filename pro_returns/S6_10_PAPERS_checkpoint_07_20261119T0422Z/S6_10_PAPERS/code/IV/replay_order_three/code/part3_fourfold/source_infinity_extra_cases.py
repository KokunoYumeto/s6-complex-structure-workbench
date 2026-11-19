#!/usr/bin/env python3
"""Independent extra scalar orders for the local relative collision quantity."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import json,gc
from source_infinity_regular_fan import PeriodicFan
from source_infinity_fixed_charts import do_case as fixed
from source_infinity_interior_residues import do_case as interior
from source_infinity_h_residues import do_case as hdata
from source_infinity_e_cycles import one as ecycles
root=Path(__file__).resolve().parents[2]
folder=root/"code/part3_fourfold"
rows=[]
for a,b,N in ((1,2,4),(2,1,3),(1,2,12),(2,1,9)):
    fan=PeriodicFan(a,b,N);fan.initial();fan.resolve(progress=500)
    data=fan.export()
    path=folder/f"source_infinity_regular_fan_{a}_{b}_{N}.json"
    path.write_text(json.dumps(data,separators=(",",":"))+"\n")
    fchecks=data["checks"]
    del data,fan
    gc.collect()
    fixed(a,b,N);interior(a,b,N);hdata(a,b,N);ecycles(a,b,N)
    ii=json.loads((folder/f"source_infinity_interior_residues_{a}_{b}_{N}_summary.json").read_text())
    hh=json.loads((folder/f"source_infinity_h_residues_{a}_{b}_{N}_summary.json").read_text())
    rr=Fraction(ii["total_normal_link_residue"]["rational"])+Fraction(hh["H_normal_link_residue"]["rational"])
    predicted=Fraction(N*a*a,4)-Fraction(a*(a*a-1),6)
    assert rr==predicted,(a,b,N,rr,predicted)
    relative=rr-Fraction(N*a*a,4)
    rows.append({"a":a,"b":b,"N":N,"fan_checks":fchecks,
                 "interior_plus_H":str(rr),"reference_E_difference":str(-Fraction(N*a*a,4)),
                 "local_relative_sum":str(relative)})
    print("EXTRA_CASE_PASS",rows[-1],flush=True)
(folder/"source_infinity_extra_cases.json").write_text(json.dumps(
 {"utc":datetime.now(timezone.utc).isoformat(),"status":"PASS","rows":rows,
  "scope":"Four further exact fan calculations. A general-order or global-return theorem is not inferred from finite agreement."},indent=2)+"\n")
