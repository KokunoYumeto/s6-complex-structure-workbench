#!/usr/bin/env python3
"""Save separate exact infinity fixed-chart/residue programs."""
from pathlib import Path
from datetime import datetime,timezone
import json
root=Path(__file__).resolve().parents[2]
folder=root/"code/part3_fourfold"
records=[]
for part in ("fixed_charts","interior_residues","h_residues"):
    src=folder/f"source_zero_{part}.py"
    dst=folder/f"source_infinity_{part}.py"
    text=src.read_text()
    changes=[]
    def replace(old,new,count=None):
        global text
        got=text.count(old)
        if count is not None: assert got==count,(part,old,got,count)
        assert got
        text=text.replace(old,new)
        changes.append({"old":old,"new":new,"count":got})
    replace("source_zero_","source_infinity_")
    if part in ("fixed_charts","h_residues"):
        replace("ROOT/'code/part3'/f'source_infinity_regular_fan_",
                "ROOT/'code/part3_fourfold'/f'source_infinity_regular_fan_",1)
    if part=="interior_residues":
        replace("H=((2,b),(-a,N-1))","H=((2,b),(-a,N-2))",1)
        replace("'I':((1,0),(0,1))","'I':((1,0),(0,0))",1)
    if part=="h_residues":
        replace("hn=[2*n1+b*n2,-a*n1+(N-1)*n2]",
                "hn=[2*n1+b*n2,-a*n1+(N-2)*n2]",1)
    dst.write_text(text)
    records.append({"source":str(src),"destination":str(dst),"changes":changes})
(folder/"source_infinity_residue_derivation.json").write_text(
    json.dumps({"utc":datetime.now(timezone.utc).isoformat(),"programs":records},indent=2)+"\n")
print("Saved three independent infinity chart/residue programs.")
