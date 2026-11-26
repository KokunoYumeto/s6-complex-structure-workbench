#!/usr/bin/env python3
"""Map only the previously exposed source lines to existing statement metadata.
The canonical stream is inspected only for environment, label, StatementRecord,
and bibliography metadata. No argument text is emitted or copied.
"""
from pathlib import Path
import csv,re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"agents/continuation7_iii_weighted_cups/S6_SERIES_PUBLISH_III_02LP_exposed_line_metadata.tsv"
wanted={5601,7114,7677,7684,8227,12302,12968,15776,
16507,16578,16586,16673,16676,17351,17462,17463,17465,17472,
19359,19587,19918,19935,20002,20009,20012,20015,20126,20129,
22232,22234,23080,23264,23333,30190,30823,30824,30878}
with (ROOT/"S6_SERIES_PUBLISH_tags.tsv").open() as f:
    tags={r["label"]:r["tag"] for r in csv.DictReader(f,delimiter="\t") if r["paper"]=="III"}
statement_kinds={"theorem","proposition","lemma","corollary","definition","remark","claim"}
last={"label":"","tag":"","metadata_line":0}
stack=[];bibliography=False;bibkey=""
rows=[]
with (ROOT/"S6_SERIES_PUBLISH_III.tex").open() as f:
    for number,line in enumerate(f,1):
        # Only these structural tokens are retained; the original argument
        # line is neither displayed nor stored.
        for match in re.finditer(r"\\begin\{([^}]+)\}|\\end\{([^}]+)\}|\\StatementRecord\{([^}]+)\}\{[^}]*\}\{([^}]+)\}|\\label\{([^}]+)\}|\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}",line):
            begin,end,label_record,tag_record,label,bib=match.groups()
            if begin:
                if begin=="thebibliography":bibliography=True
                if begin in statement_kinds:
                    stack.append({"kind":begin,"owner":{"label":"","tag":"","metadata_line":number}})
                elif begin=="proof":
                    stack.append({"kind":"proof","owner":last.copy()})
            elif end:
                if end=="thebibliography":bibliography=False
                if stack and end==stack[-1]["kind"]:
                    done=stack.pop()
                    if done["kind"] in statement_kinds and done["owner"]["label"]:
                        last=done["owner"].copy()
            elif label_record:
                # This declares an existing statement identity. It is
                # used for an immediately following proof when no
                # theorem-environment label was carried.
                owner={"label":label_record,"tag":tag_record,"metadata_line":number}
                if not stack:last=owner
            elif label:
                if stack and stack[-1]["kind"] in statement_kinds and not stack[-1]["owner"]["label"]:
                    stack[-1]["owner"]={"label":label,"tag":tags.get(label,""),"metadata_line":number}
            elif bib:bibkey=bib
        if number in wanted:
            if bibliography:
                owner={"label":"bibliography:"+bibkey,"tag":"","metadata_line":number}
                locus="bibliography"
            else:
                owner=(stack[-1]["owner"] if stack else last)
                locus=stack[-1]["kind"] if stack else "metadata/prose"
            rows.append({"source_line":number,"statement_identity":owner["label"],
                         "existing_tag":owner["tag"],"locus":locus,
                         "owner_metadata_line":owner["metadata_line"]})
assert len(rows)==len(wanted)
with OUT.open("w", newline="\n") as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter="\t",lineterminator="\n")
    writer.writeheader();writer.writerows(rows)
for row in rows:
    print(row["source_line"],row["statement_identity"],row["existing_tag"],row["locus"],row["owner_metadata_line"])
print("SCOPE metadata only for the previously disclosed hit list; no argument text emitted.")
