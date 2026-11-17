#!/usr/bin/env python3
"""Retain search/source metadata without redistributing retrieved article bodies."""
from pathlib import Path
import re,json
root=Path(__file__).resolve().parents[1]
private=root.parent/"external_sources"/"private_web_logs"
private.mkdir(parents=True,exist_ok=True)
for p in (root/"evidence").glob("*.json"):
    data=json.loads(p.read_text())
    if isinstance(data, list):
        assert all(isinstance(row, dict) and 'content' not in row for row in data), p
        continue  # Lists of original source metadata contain no retrieved body.
    if data.get("metadata_only"): continue
    text="\n".join(c.get("text","") for c in data.get("content",[]) if c.get("type")=="text")
    if not text: continue
    (private/p.name).write_text(p.read_text())
    urls=sorted(set(re.findall(r"https?://[^\s)<>\"】]+",text)))
    refs=sorted(set(re.findall(r"【(turn[^\s】]+)】",text)))
    headings=[]
    for block in text.split("--------------------------------------------------------------------------------"):
        lines=block.strip().splitlines()
        if lines: headings.append(lines[0][:600])
    p.write_text(json.dumps({"metadata_only":True,"source_titles":headings,"urls":urls,"source_refs":refs,"note":"Full retrieved bodies omitted; exact theorem locations and use are in the paper and reports."},indent=2,ensure_ascii=False))
    print(p.name,len(urls),"URLs",len(refs),"references")
