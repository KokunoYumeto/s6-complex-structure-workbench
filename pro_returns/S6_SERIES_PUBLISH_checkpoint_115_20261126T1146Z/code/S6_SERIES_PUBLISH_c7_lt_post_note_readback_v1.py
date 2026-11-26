"""Retain the exact 468-line mathematical prefix and show the appended scope."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import difflib
ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT / "agents/continuation7_iii_invariant_chern_receiving"
P = "S6_SERIES_PUBLISH_III_02LT_"
path = LANE / (P + "post_exposure_derivation.md")
raw = path.read_bytes()
lines = raw.splitlines(keepends=True)
prefix = b"".join(lines[:468])
assert prefix.endswith(b"The frozen pre-exposure files remain unchanged.\n")
assert lines[469].startswith(b"## 7. Exact inverse reading")
old_path = LANE / (P + "post_exposure_derivation_v1.md")
assert not old_path.exists()
old_path.write_bytes(prefix)
print("START", datetime.now(timezone.utc).isoformat())
print("V1_EXACT_UNCHANGED_PREFIX", 468, len(prefix), sha256(prefix).hexdigest())
print("CURRENT", len(lines), len(raw), sha256(raw).hexdigest())
print("".join(difflib.unified_diff(prefix.decode().splitlines(True), raw.decode().splitlines(True),
                                fromfile="post_note_v1", tofile="post_note_with_section7")), end="")
print("SCOPE", "v1 is the exact unchanged prefix; section 7 was appended by the retained apply_patch tool call.")
print("END", datetime.now(timezone.utc).isoformat())
