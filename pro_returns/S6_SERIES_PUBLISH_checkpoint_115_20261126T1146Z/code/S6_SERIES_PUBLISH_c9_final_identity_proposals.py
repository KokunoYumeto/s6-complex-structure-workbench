#!/usr/bin/env python3
"""Last context-read P11 relabelling passages; writes only agent proposals."""
import csv
from datetime import datetime, timezone
import json
from pathlib import Path
from zipfile import ZipFile
from S6_SERIES_PUBLISH_c8_III_check_counts import parse_statements

ROOT = Path(__file__).resolve().parents[1]
OWN = ROOT / "agents/continuation9_global_sweep"
s = (ROOT / "S6_SERIES_PUBLISH_III.tex").read_text(encoding="utf-8")
owners, _, _ = parse_statements(s)
with ZipFile(ROOT.parents[1] / "upload/S6_SERIES_PUBLISH_continue_cp100.zip") as z:
    original = z.read("S6_SERIES_PUBLISH_checkpoint_100/S6_SERIES_PUBLISH_III.tex").decode("utf-8")
rows = [
    ("maps:def:semistable-residual-data", "zero-based-position",
     "The selected position is $i_0=i-1$\nin the input definition's peripheral order; the inverse is $i=i_0+1$.",
     "The selected position is $i_0=i-1$\nin the input definition's peripheral order.",
     "The retained preceding equation i_0=i-1 fixes the same selected position in zero-based indexing; addition of one recovers i. Only the redundant reverse renaming is removed. The allowed positions, profile, coefficients, Mumford cap and ordinary clutch are unchanged."),
    ("maps:def:additive-residual-data", "additive-position-index",
     "Selected positions are $i-1$ in Definition~\\ref{mapsIII:def:elliptic-marked-data},\nwith inverse $i=i_0+1$ for a selected index $i_0$. In an original-only pattern the ordinary",
     "Selected positions are $i_0=i-1$ in\nDefinition~\\ref{mapsIII:def:elliptic-marked-data}. In an original-only pattern the ordinary",
     "The map from the printed one-based selected index i to the defining zero-based index is explicitly retained as i_0=i-1. Its inverse is addition of one, and every site label, allowed filling and parameter is unchanged. The redundant inverse phrase is removed without changing the indexing map."),
    ("mapsIII:rem:original-additive-specializations", "untwisted-Engel-input-identity",
     "order-one site, gives the input map and its inverse. That theorem",
     "order-one site, gives the input identification. That theorem",
     "At the stated (m,v)=(1,0), the period lattice and every original cap are fixed and the extra order-one ordinary disc is the same marked disc. The input comparison is therefore the identity on these coordinates, and its square fixes every input. The identification, Betti list, cap data and cited theorem remain; only the redundant inverse narration is removed.")
]
now = datetime.now(timezone.utc).isoformat()
df = next(csv.reader((ROOT / "S6_SERIES_PUBLISH_defects_III.tsv").open(), delimiter="\t"))
ef = next(csv.reader((ROOT / "CHECK_EVENTS.tsv").open(), delimiter="\t"))
proposals, defects, events = [], [], []
candidate = s
for i, (sid, name, old, new, reason) in enumerate(rows, 1):
    assert s.count(old) == original.count(old) == 1, name
    pos = s.index(old)
    owner = next(o for o in owners if o.start <= pos < o.stop)
    assert owner.statement_id == sid
    cid = f"CLAUDE-III-P11-FINAL-{i:03d}"
    proposals.append(dict(change_id=cid, name=name, finding="P11", statement_id=sid, tag=owner.tag,
        old=old, new=new, interpretation=reason, source_line=s.count("\n", 0, pos)+1))
    candidate = candidate.replace(old, new, 1)
    defects.append(dict(change_id=cid, type="D08", statement_id=sid,
        old_location=f"original cp100; tag {owner.tag}", old_page="current page concordance pending",
        new_location="same marked input definition/remark", new_page="pending rendered-PDF review",
        old_text=old, new_text=new, reason=reason,
        review_status="Original and current paragraph compared at "+now+"; proposed; no whole-proof or page-review credit."))
    e = {k: "" for k in ef}; eid = f"publish:c9:III:final-identity:{i:03d}"
    e.update(statement_id=sid, date=now[:10], who="GPT-6 Astra (OpenAI), ChatGPT Pro mode; continuation nine global wording reviewer",
        type="used and rechecked in this run", outcome="Read and compared the exact original/current/proposed input paragraph for "+name+". The forward index/identity map is retained and its inverse is derived in the defect reason. All sites, parameters and mathematical results are unchanged. Scoped wording comparison only; no independent-check or PDF-page credit.",
        event_id=eid, phase="continuation9 Paper III final identity wording", source_file="code/S6_SERIES_PUBLISH_c9_final_identity_proposals.py",
        source_event_type="used and rechecked in this run", evidence_group=eid, date_utc=now,
        where="agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_final_identity_proposals.json")
    events.append(e)
    print(cid, sid, name)
restored = candidate
for p in reversed(proposals):
    assert restored.count(p["new"]) == 1
    restored = restored.replace(p["new"], p["old"], 1)
assert restored == s
(OWN / "S6_SERIES_PUBLISH_c9_final_identity_proposals.json").write_text(json.dumps(proposals, ensure_ascii=False, indent=2)+"\n", encoding="utf-8", newline="\n")
for name, fields, data in [("S6_SERIES_PUBLISH_c9_final_identity_defects.tsv", df, defects), ("S6_SERIES_PUBLISH_c9_final_identity_events.tsv", ef, events)]:
    with (OWN / name).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(data)
print("Prepared three exact relabelling proposals and three scoped events; original/live guards and reverse comparison pass.")
