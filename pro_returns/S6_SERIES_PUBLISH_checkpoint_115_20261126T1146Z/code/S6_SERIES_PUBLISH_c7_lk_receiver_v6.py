#!/usr/bin/env python3
"""Correct one capitalization in the reviewed LK receiver."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "agents/continuation7_iii_general_cusp_receiving/S6_SERIES_PUBLISH_III_02LK_receiving.tex"
before = path.read_bytes()
assert sha256(before).hexdigest() == "d24493851215eab793b60e564bbc3ae6b5d6af62720a68f066122a3c2e2e5eed"
old = b"alternatively\nThe unit family transports"
new = b"alternatively\nthe unit family transports"
assert before.count(old) == 1
after = before.replace(old, new)
assert len(before) == len(after)
assert sum(a != b for a, b in zip(before, after)) == 1
assert b"\r" not in after
path.write_bytes(after)
print("PASS one capitalization change; all mathematical text and identities retained")
print("LINES", len(after.splitlines()))
print("SHA256", sha256(after).hexdigest())
print("COMPLETED_UTC", datetime.now(timezone.utc).isoformat())
