#!/usr/bin/env python3
"""Bounded authorized LP auxiliary source retrieval; no historical execution."""
from pathlib import Path
from urllib.request import Request, urlopen
from hashlib import sha256
from datetime import datetime, timezone

DEST = Path("/tmp/S6_SERIES_PUBLISH_c7_LP_aux")
DEST.mkdir(exist_ok=True)
sources = [
 ("S6_SERIES_PUBLISH_Thomas1956.pdf",
  "https://webhomes.maths.ed.ac.uk/~v1ranick/papers/thomas.pdf"),
 ("S6_SERIES_PUBLISH_Kaplan1979.pdf",
  "https://scispace.com/pdf/constructing-framed-4-manifolds-with-given-almost-framed-1vq4kmmbg3.pdf"),
 ("S6_SERIES_PUBLISH_lp_historical_thomas.py",
  "https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7/pro_returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z/S6_10_PAPERS/code/III/fourfolds_D48_thomas.py"),
]
print("Retrieval UTC", datetime.now(timezone.utc).isoformat(), flush=True)
for name, url in sources:
    path = DEST / name
    assert not path.exists()
    try:
        with urlopen(Request(url, headers={"User-Agent":"S6-series-source-audit"}), timeout=25) as response:
            data = response.read()
        assert data, "Empty response"
        if name.endswith(".pdf"):
            assert data.startswith(b"%PDF"), "Response is not a PDF"
        path.write_bytes(data)
        print("SUCCESS", url, str(path), len(data), sha256(data).hexdigest(), flush=True)
    except Exception as error:
        print("FAILED", url, type(error).__name__, str(error), flush=True)
print("No historical source executed; downloaded publications remain outside W.", flush=True)
