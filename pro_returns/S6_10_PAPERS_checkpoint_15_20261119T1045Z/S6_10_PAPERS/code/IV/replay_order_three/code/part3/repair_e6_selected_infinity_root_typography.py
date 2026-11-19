"""Preserve the appended draft, then repair its literal inline TeX delimiters."""
from pathlib import Path
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parents[2]
p = ROOT / "notes/part3_e6_selected_infinity_root_working.md"
archive = ROOT / "records/attempts/e6_selected_infinity_root/before_inline_typography_repair"
archive.mkdir(parents=True, exist_ok=True)
before = p.read_bytes()
target = archive / p.name
if not target.exists():
    target.write_bytes(before)
s = before.decode()
changes = [
    ("The identities (m=3r_*-c) and (b_*=r_*+c)", r"The identities \(m=3r_*-c\) and \(b_*=r_*+c\)"),
    ("at (r=0,t=0).", r"at \(r=0,t=0\)."),
    ("It preserves (e,z,X,Y)", r"It preserves \((e,z,X,Y)\)"),
    ("The original (m)-root deck", r"The original \(m\)-root deck"),
    (r"It preserves (e), sends (z) to", r"It preserves \(e\), sends \(z\) to"),
    ("the native (X,Y)", r"the native \((X,Y)\)"),
    ("Its (m)-th power", r"Its \(m\)-th power"),
    (r"curve (y^2=x^3+a_2x^2+d x+\sigma^2)", r"curve \(y^2=x^3+a_2x^2+d x+\sigma^2\)"),
    (r"slope (d/(2\sigma))", r"slope \(d/(2\sigma)\)"),
    (r"(x=d^2/(4\sigma^2)-a_2)", r"\(x=d^2/(4\sigma^2)-a_2\)"),
    ("at (3G),", r"at \(3G\),"),
    (r"slope is (d/(6\sigma))", r"slope is \(d/(6\sigma)\)"),
    ("translation by (-G)", r"translation by \(-G\)"),
    (r"(d|_{\sigma=0}=1)", r"\(d|_{\sigma=0}=1\)"),
    ("exactly (O,T):", r"exactly \(O,T\):"),
    (r"point has (-\bar X=\bar X) and (-i\bar Y=\bar Y)", r"point has \(-\bar X=\bar X\) and \(-i\bar Y=\bar Y\)"),
    ("hence (\x08ar X=\x08ar Y=0). For even (m)", r"hence \(\bar X=\bar Y=0\). For even \(m\)"),
    ("point has (mR=bT=T), because (b=1)", r"point has \(mR=bT=T\), because \(b=1\)"),
    ("order (m=2), any central", r"order \(m=2\), any central"),
    ("half (R_0) of (T) satisfies", r"half \(R_0\) of \(T\) satisfies"),
    ("have (x=1,-1)", r"have \(x=1,-1\)"),
    (r"(y=\pm\sqrt2,\pm i\sqrt2)", r"\(y=\pm\sqrt2,\pm i\sqrt2\)"),
    (r"On a local (m=2) division chart, let (T(\xi,\sigma))", r"On a local \(m=2\) division chart, let \(T(\xi,\sigma)\)"),
    ("(T); it is the analytic cubic root near (x=0) with", r"\(T\); it is the analytic cubic root near \(x=0\) with"),
    ("(y=0). The curve", r"\(y=0\). The curve"),
    ("value (R_0) then", r"value \(R_0\) then"),
    (r"double (-G(\xi,\sigma)),", r"double \(-G(\xi,\sigma)\),"),
    ("of ([2]) proves", r"of \([2]\) proves"),
    ("agrees with (G)", r"agrees with \(G\)"),
    ("it by (G) off", r"it by \(G\) off"),
]
applied = []
for old, new in changes:
    count = s.count(old)
    if count:
        s = s.replace(old, new)
        applied.append({"old": old, "new": new, "count": count})
assert not any(ord(c) < 32 and c not in "\n\t\r" for c in s)
p.write_text(s)
(archive / "repair.json").write_text(json.dumps({
    "before_sha256": hashlib.sha256(before).hexdigest(),
    "after_sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
    "changes": applied,
    "scope": "Inline TeX delimiters and one accidental backspace escape; no mathematical formula changed."
}, indent=2) + "\n")
print(json.dumps({"changed_patterns": len(applied), "source_sha256": hashlib.sha256(p.read_bytes()).hexdigest()}))
