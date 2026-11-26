#!/usr/bin/env python3
"""Final bounded LE notation repairs and explicit rank-one parity sentence."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
P = ROOT / "agents/continuation7_iii_mixed_torsion/S6_SERIES_PUBLISH_III_02LE_fresh_derivation.md"
old = P.read_text()
text = old
print("Final text repair UTC", datetime.now(timezone.utc).isoformat())
print("Input SHA256", sha256(old.encode()).hexdigest())
changes = [
    ("the value (1) exists", "the value $1$ exists"),
    ("Modulo either (2) or $p$", "Modulo either $2$ or $p$"),
    (r"$D=-be,s$", r"$D=-be\,s$"),
    (r"(b/q)(n-me)s=\pm2p,s=0.", r"(b/q)(n-me)s=\pm2p\,s=0."),
    (r"$be,s=\pm2p,s=0$", r"$be\,s=\pm2p\,s=0$"),
    (r"$2[S^2]\$", r"$2[S^2]$"),
    ("precisely $Phi$", r"precisely $\Phi$"),
    ("the full $mu$", r"the full $\mu$"),
    ("divisibility. Its physical support is $-kj(j-\\alpha_0)/2$.\n",
     "divisibility. Its physical support is $-kj(j-\\alpha_0)/2$.\n"
     "In these rows the physical first-period content is $\\alpha_0=d_0$,\n"
     "equal to one or three. It is odd, so $j(j-\\alpha_0)$ is even for\n"
     "every integer vertex $j$; this proves the asserted integrality of\n"
     "the physical support, including the nonprimitive column.\n"),
]
for before, after in changes:
    assert text.count(before) == 1, repr(before)
    text = text.replace(before, after)
    print("CHANGE", repr(before), "->", repr(after))
addition = """

The executed v001 table writer used CRLF. A separate retained conversion
program changed only the current TSV line endings to LF, verifying both
field equality and exact recovery of the original bytes. Its stdout
retains those original bytes in reversible base64 form and both hashes.
The corrected v002 catalogue writer has explicit LF and is saved but was
not run; the v001 source and both original streams remain unchanged.
The retained presentation-repair history includes the exact failed
code-mode invocation and its parser error, followed by the successful
repair sources and separate streams. The companion execution note gives
the exact paths and limits. These conversions add no numerical or
independent mathematical check.
"""
text += addition
assert text.count(r"\[") == text.count(r"\]")
assert text.count("$") % 2 == 0
assert not any(ord(c) < 32 and c != "\n" for c in text)
P.write_text(text)
print("Output SHA256", sha256(P.read_bytes()).hexdigest())
print("PASS: bounded notation repairs and rank-one parity explanation; no catalogue recomputation")
