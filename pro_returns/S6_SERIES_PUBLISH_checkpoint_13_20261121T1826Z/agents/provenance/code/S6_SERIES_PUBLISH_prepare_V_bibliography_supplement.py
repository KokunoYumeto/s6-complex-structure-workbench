#!/usr/bin/env python3
"""Add the two newly reopened analytic locators after the main bibliography patch."""
from pathlib import Path
import importlib.util
import json
import re

ROOT = Path(__file__).resolve().parents[1]
module_path = ROOT / "code/S6_SERIES_PUBLISH_prepare_V_bibliography.py"
spec = importlib.util.spec_from_file_location("bib_patch", module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
text = (ROOT / "S6_SERIES_PUBLISH_references_V_proposed.bib").read_text()
matches = list(re.finditer(r"^@[A-Za-z]+\{([^,]+),", text, re.M))
updates = {
    "TeschlODE2012": (
        "20 November 2026. Primary author PDF: Lemma 2.7 and equation (2.36), printed pp.42--43/PDF pp.53--54. The Gronwall estimate supports the interval ODE majorant.",
        "agents/v_analytic/literature/S6_SERIES_PUBLISH_V_Teschl_locator_receipt.json"),
    "DLMFCauchy2026": (
        "20 November 2026. NIST Digital Library of Mathematical Functions, section 1.9(iii), equations 1.9.30--1.9.31. The exact Cauchy coefficient formulas were opened for the analytic continuation tail bound.",
        "agents/v_analytic/literature/S6_SERIES_PUBLISH_V_DLMF_locator_receipt.json"),
}
patches = []
for i, match in enumerate(matches):
    key = match.group(1)
    if key not in updates:
        continue
    entry = text[match.start():matches[i+1].start() if i+1<len(matches) else len(text)]
    scope, receipt = updates[key]
    new = module.setfield(entry, "verification", "verified at the listed primary-source scope")
    new = module.setfield(new, "publication_verification", scope)
    new = module.setfield(new, "publication_verification_record", receipt.replace("_", r"\_"))
    fields = module.fields(new)
    if "note" in fields:
        _, _, a, b = fields["note"]
        value = new[a:b]
        if "verified" in value.lower() or "opened" in value.lower():
            new = module.delfield(new, "note")
            new = module.setfield(new, "verification_history", value)
    patches.append({"key":key,"old_text":entry,"new_text":new,
                    "reason":"Record the newly opened exact analytic locator; apply after the 40-entry bibliography patch."})
assert len(patches) == 2
(ROOT / "S6_SERIES_PUBLISH_V_bibliography_supplement.json").write_text(json.dumps(patches,indent=2)+"\n")
print("Two guarded current-primary-scope additions; no mathematical events added.")
