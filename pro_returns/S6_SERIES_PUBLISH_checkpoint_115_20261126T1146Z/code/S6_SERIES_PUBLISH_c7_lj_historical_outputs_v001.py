#!/usr/bin/env python3
"""Retrieve only the released LJ output names; record every exact attempt."""
from pathlib import Path
from urllib.request import Request,urlopen
from datetime import datetime,timezone
from hashlib import sha256
import json
STORE=Path("/tmp/S6_SERIES_PUBLISH_c7_LJ_historical")
BASE=("https://raw.githubusercontent.com/KokunoYumeto/"
      "s6-complex-structure-workbench/a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7/"
      "pro_returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z/S6_10_PAPERS/")
print("START",datetime.now(timezone.utc).isoformat(),flush=True)
for name,dirs in [
    ("manifolds_three_mixed_AH.json",["code/III/","code/","records/"]),
    ("manifolds_three_mixed_AH.out",["code/","outputs/III/"])]:
    for folder in dirs:
        url=BASE+folder+name
        try:
            with urlopen(Request(url,headers={"User-Agent":"S6-series-source-audit"}),timeout=25) as r:
                blob=r.read()
            blob.decode()
            if name.endswith(".json"):json.loads(blob)
            target=STORE/("S6_SERIES_PUBLISH_"+name)
            with target.open("xb") as f:f.write(blob)
            print("SUCCESS",url,"PATH",target,"SHA256",sha256(blob).hexdigest(),
                  "BYTES",len(blob),"LINES",len(blob.splitlines()),flush=True)
            break
        except Exception as exc:
            print("FAILED",url,type(exc).__name__,str(exc),flush=True)
print("COMPLETE",datetime.now(timezone.utc).isoformat(),flush=True)
