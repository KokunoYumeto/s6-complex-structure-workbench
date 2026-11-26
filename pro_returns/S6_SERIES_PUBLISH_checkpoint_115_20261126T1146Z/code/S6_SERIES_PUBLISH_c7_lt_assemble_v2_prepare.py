"""Retain failed v1 and form v2 by the complete two-edit source difference."""
from pathlib import Path
from hashlib import sha256
import difflib
ROOT = Path(__file__).resolve().parents[1]
old_path = ROOT / "code/S6_SERIES_PUBLISH_c7_lt_assemble_v1.py"
new_path = ROOT / "code/S6_SERIES_PUBLISH_c7_lt_assemble_v2.py"
old = old_path.read_text()
needle = '("The literal area", "The area"),\n'
assert old.count(needle) == 1
new = old.replace(needle, "")
needle = 'statement = statement.replace("there is no omitted finite normal index.", "")\n'
assert new.count(needle) == 1
new = new.replace(needle, needle + 'statement = statement.replace("in the Wang sequence;\\n", "in the Wang sequence.\\n")\n')
assert not new_path.exists()
new_path.write_text(new, encoding="utf-8", newline="\n")
print("V1_UNCHANGED", sha256(old_path.read_bytes()).hexdigest())
print("V2", len(new.splitlines()), sha256(new_path.read_bytes()).hexdigest())
print("".join(difflib.unified_diff(old.splitlines(True), new.splitlines(True),
                                fromfile=old_path.name, tofile=new_path.name)), end="")
