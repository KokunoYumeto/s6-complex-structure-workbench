#!/usr/bin/env python3
"""Retained receiver-only reference and primary-locator correction."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import re
W=Path(__file__).resolve().parents[1]
path=W/"agents/continuation7_iii_mixed_three_receiving/S6_SERIES_PUBLISH_III_02LJ_receiving.tex"
old=path.read_bytes(); text=old.decode()
print("START",datetime.now(timezone.utc).isoformat())
print("OLD_SHA256",sha256(old).hexdigest())
for number,marker in [
    (4,r" Y_{30,t}=M_t\#M_{3,0}\#Z_{5,0}."),
    (1,r" H_0(X)=H_6(X)=\mathbb Z,\quad b_3(X)=0."),
    (2,r" P_p=\frac{b/p-a\nu}{2}\pmod p\quad(p=3,5;\ p\mid c)."),
    (3,r"30&15t\,s&45t\,\gamma_3(s)\pmod{90}.")]:
    assert text.count(marker)==1
    text=text.replace(marker,marker+r"\qquad\textnormal{("+str(number)+")}")
    print("STATEMENT_DISPLAY_REFERENCE",number)
bad=re.findall(r"\bthe theorem([0-9])\b",text)
text=re.sub(r"\bthe theorem([0-9])\b",r"Section 1\1",text)
print("RESTORED_SECTION_REFERENCES",bad)
phrase="primary sources disclosed in the LF and bounded Cartan/Thomas notes."
replacement=(r"primary sources \cite[Expos\'e~11, Theorems~1 and~4]{manCartan1955EML}, "
             r"\cite[(3.3)--(3.6), p.~268]{ffThomas56}, and "
             r"\cite[Theorem~I(ii), pp.~897--898; \S5, pp.~904--905]{ffThomas1959Suspension}.")
assert text.count(phrase)==1
text=text.replace(phrase,replacement)
print("INSERTED_EXACT_PRIMARY_LOCATORS")
path.write_text(text)
print("NEW_SHA256",sha256(path.read_bytes()).hexdigest())
print("COMPLETE",datetime.now(timezone.utc).isoformat())
