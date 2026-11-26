#!/usr/bin/env python3
"""Apply only the two final LJ prose corrections; no mathematical rerun."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib

W = Path(__file__).resolve().parents[1]
path = W / "agents/continuation7_iii_mixed_three/S6_SERIES_PUBLISH_III_02LJ_fresh_derivation.md"
before = path.read_bytes()
text = before.decode()
old_header = """remain closed. The admitted inputs and the separately completed LF input
are disclosed in the input note. This file is under final reading and is
not yet frozen for original release."""
new_header = """remain closed. The admitted inputs, including the final admitted LF
receiver, are disclosed in the input note. The complete derivation and both
new mathematical programs and outputs have been read. The final completion
time and hashes are reported to root after the note reread."""
old_telescope = r"I-(T_1\cdots T_N)^{-1}=0"
new_telescope = r"I-T_1\cdots T_N=0"
assert text.count(old_header) == 1
assert text.count(old_telescope) == 1
print("START", datetime.now(timezone.utc).isoformat())
print("PROOF_BEFORE_SHA256", hashlib.sha256(before).hexdigest())
text = text.replace(old_header, new_header).replace(old_telescope, new_telescope)
path.write_text(text)
print("EDIT_HEADER", repr(old_header), "->", repr(new_header))
print("EDIT_TELESCOPE", old_telescope, "->", new_telescope)
print("PROOF_AFTER_SHA256", hashlib.sha256(path.read_bytes()).hexdigest())
print("COMPLETE", datetime.now(timezone.utc).isoformat())
