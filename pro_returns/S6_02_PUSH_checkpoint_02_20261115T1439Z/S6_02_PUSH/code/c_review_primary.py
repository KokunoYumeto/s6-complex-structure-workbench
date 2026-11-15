#!/usr/bin/env python3
"""Inspect retrieved primary papers; retain metadata, not copyrighted page text."""
from pathlib import Path
import fitz
root=Path(__file__).resolve().parents[2]
spec={"Cerf1970.pdf":list(range(0,12)),
"KervaireMilnor1963.pdf":list(range(0,5))+list(range(26,35)),
"EellsKuiper1962.pdf":list(range(0,10)),
"DuranRigas2008.pdf":list(range(0,6))}
for fn, pages in spec.items():
    p=root/"external_sources"/fn
    print("\nSOURCE",fn)
    d=fitz.open(p)
    print("PAGES",len(d))
    for i in pages:
        if i>=len(d): continue
        s=d[i].get_text()
        print("\nPDF PAGE",i+1,"TEXT CHARACTERS",len(s))
        print("Contains theorem marker:", any(w in s.lower() for w in ("theorem","théorème")))
        print("Contains corollary marker:", any(w in s.lower() for w in ("corollary","corollaire")))

