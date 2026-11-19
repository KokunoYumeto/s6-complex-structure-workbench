#!/usr/bin/env python3
from pathlib import Path
import json
from datetime import datetime,timezone
root=Path(__file__).resolve().parents[2]
src=root/"code/part3_fourfold/source_zero_e_cycles.py"
dst=root/"code/part3_fourfold/source_infinity_e_cycles.py"
s=src.read_text()
assert s.count("s*(-a*n1+(N-1)*n2)")==1
s=s.replace("source_zero_","source_infinity_")
s=s.replace("s*(-a*n1+(N-1)*n2)","s*(-a*n1+(N-2)*n2)")
dst.write_text(s)
(root/"code/part3_fourfold/source_infinity_e_derivation.json").write_text(json.dumps(
 {"utc":datetime.now(timezone.utc).isoformat(),"source":str(src),"destination":str(dst),
  "changes":["source_zero_ -> source_infinity_","actual H second coordinate N-1 -> N-2"],
  "scope":"E annular marking only; compact cap and selected real trace not assigned"},indent=2)+"\n")
print("Saved separate infinity E-cycle calculation.")
