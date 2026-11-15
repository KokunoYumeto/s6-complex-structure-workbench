#!/usr/bin/env python3
"""Assemble the source bibliography and exact numbered-statement registry."""
from pathlib import Path
import csv,re,json
root=Path(__file__).resolve().parents[1]
base=root/"sections"/"core_references.bib"
if not base.exists():
    base.write_text((root/"S6_02_PUSH_references.bib").read_text())
sources=[base]+sorted(p for p in (root/"sections").glob("*_references.bib") if p!=base)
entries={}
aliases={"Grauert1960D":"Grauert60push","Grauert1963ErratumD":"Grauert63push"}
for source in sources:
    chunks=re.split(r"(?=@\w+\s*\{)",source.read_text())
    for chunk in chunks:
        match=re.match(r"@\w+\s*\{\s*([^,\s]+)",chunk)
        if match and match.group(1) not in entries and match.group(1) not in aliases:
            entries[match.group(1)]=chunk.strip()
bib="\n\n".join(entries.values())+"\n"
keys=re.findall(r"@\w+\s*\{\s*([^,\s]+)",bib)
assert len(keys)==len(set(keys)), "Duplicate bibliography keys"
(root/"S6_02_PUSH_references.bib").write_text(bib)
headers=["id","statement","status","where_proved","depends_on","item_of_the_prompt","R_items_and_Leads_used","notes"]
rows=[]
for p in sorted((root/"sections").glob("*_results.csv")):
    with p.open(newline="") as f:
        reader=csv.DictReader(f)
        assert reader.fieldnames==headers, (p,reader.fieldnames)
        rows.extend(reader)
ids=[r["id"] for r in rows]
assert len(ids)==len(set(ids)), "Duplicate statement IDs"
def sortid(r):
    return tuple(int(x) if x.isdigit() else x for x in r["id"].split("."))
rows.sort(key=sortid)
with (root/"S6_02_PUSH_results.csv").open("w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=headers)
    w.writeheader();w.writerows(rows)
tex="\n".join(p.read_text() for p in (root/"sections").glob("*.tex"))
cited=set()
for s in re.findall(r"\\cite\w*(?:\[[^]]*\])*\{([^}]+)\}",tex):
    cited.update(s.split(","))
missing=sorted(cited-set(keys))
record={"bibliography_entries":len(keys),"statements":len(rows),"missing_citation_keys":missing,"deduplicated_aliases":aliases,"source_files":[p.name for p in sources]}
(root/"code"/"assembly_summary.json").write_text(json.dumps(record,indent=2))
print(json.dumps(record,indent=2))
