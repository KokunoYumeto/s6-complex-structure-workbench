"""Retrieve only the three individually authorized LS historical sources."""
from pathlib import Path
from urllib.request import Request, urlopen
from datetime import datetime, timezone
from hashlib import sha256

store = Path("/tmp/S6_SERIES_PUBLISH_c7_LS_historical")
store.mkdir(exist_ok=True)
base = ("https://raw.githubusercontent.com/KokunoYumeto/"
        "s6-complex-structure-workbench/a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7/"
        "pro_returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z/S6_10_PAPERS/")
paths = [
    "code/III/root_vertical_corrections.py",
    "code/III/fourfolds_corrected_Mumford_examples.py",
    "code/V/replay_chains/code/fourfolds_vertical_correction_audit.py",
]
print("START", datetime.now(timezone.utc).isoformat(), flush=True)
for relative in paths:
    url = base + relative
    try:
        with urlopen(Request(url, headers={"User-Agent":"S6-series-source-audit"}), timeout=25) as response:
            blob = response.read()
        blob.decode()
        path = store / ("S6_SERIES_PUBLISH_" + Path(relative).name)
        with path.open("xb") as handle:
            handle.write(blob)
        print("SUCCESS", url, "PATH", path, "SHA256", sha256(blob).hexdigest(),
              "BYTES", len(blob), "LINES", len(blob.splitlines()), flush=True)
    except Exception as error:
        print("FAILED", url, type(error).__name__, str(error), flush=True)
print("COMPLETE", datetime.now(timezone.utc).isoformat(), flush=True)
