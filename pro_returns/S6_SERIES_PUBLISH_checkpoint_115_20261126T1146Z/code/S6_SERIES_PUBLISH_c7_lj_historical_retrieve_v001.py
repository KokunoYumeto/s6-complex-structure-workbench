#!/usr/bin/env python3
"""Read-only retrieval of the released LJ historical source and its output.

No historical program is executed. No broad helper body is opened.
"""
from pathlib import Path
from urllib.request import Request, urlopen
from datetime import datetime, timezone
from hashlib import sha256

STORE=Path("/tmp/S6_SERIES_PUBLISH_c7_LJ_historical")
STORE.mkdir(exist_ok=True)
BASE=("https://raw.githubusercontent.com/KokunoYumeto/"
      "s6-complex-structure-workbench/a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7/"
      "pro_returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z/S6_10_PAPERS/")
print("START",datetime.now(timezone.utc).isoformat(),flush=True)
for name in ("manifolds_three_mixed_AH.py","manifolds_three_mixed_AH.out"):
    url=BASE+"code/III/"+name
    try:
        with urlopen(Request(url,headers={"User-Agent":"S6-series-source-audit"}),timeout=25) as r:
            blob=r.read()
        blob.decode()
        out=STORE/("S6_SERIES_PUBLISH_"+name)
        with out.open("xb") as f:
            f.write(blob)
        print("SUCCESS",url,"PATH",out,"SHA256",sha256(blob).hexdigest(),
              "BYTES",len(blob),"LINES",len(blob.splitlines()),flush=True)
    except Exception as exc:
        print("FAILED",url,type(exc).__name__,str(exc),flush=True)
print("COMPLETE",datetime.now(timezone.utc).isoformat(),flush=True)
