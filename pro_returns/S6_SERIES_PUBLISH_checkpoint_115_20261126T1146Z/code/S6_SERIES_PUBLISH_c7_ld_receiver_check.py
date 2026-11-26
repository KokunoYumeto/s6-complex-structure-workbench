#!/usr/bin/env python3
"""Read the complete LD receiver and owned post-exposure mathematical packets."""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import ast
import csv
import json
import re
import subprocess

ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/"agents/continuation7_iii_weighted_catalogue"
BASE="S6_SERIES_PUBLISH_III_02LD_"
source=(LANE/(BASE+"receiving.tex")).read_text()
raw=source.encode()
assert raw.endswith(b"\n")
assert all(x>=32 or x in (9,10) for x in raw)
assert "\\tightlist" not in source and "\\textquotesingle" not in source
assert not re.search(r"\\emph\{,\s*(?:IV|I[13])",source)
assert not re.search(r"maps:(?:src|eq):d\.",source)
assert "original proof item" not in source
for l,r in ((r"\(",r"\)"),(r"\[",r"\]")):
    assert source.count(l)==source.count(r),(l,r)

statement,proof=source.split(r"\begin{proof}",1)
proof=r"\begin{proof}"+proof
patterns=(r"\\label\{([^}]+)\}",r"\\hypertarget\{([^}]+)\}",r"\\tag\{([^}]+)\}")
for kind,new in (("statement",statement),("proof",proof)):
    old="\n".join((LANE/(BASE+"released_"+kind+".tex")).read_text().splitlines()[5:])
    for pattern in patterns:
        assert sorted(re.findall(pattern,old))==sorted(re.findall(pattern,new)),(kind,pattern)
print("PASS all 13 permanent labels/targets and 12 equation tags, separately in theorem and proof.")

known=set()
with (ROOT/"S6_SERIES_PUBLISH_tags.tsv").open() as f:
    for row in csv.DictReader(f,delimiter="\t"):
        known.add(row["label"])
references=re.findall(r"\\(?:eq)?ref\{([^}]+)\}",source)
assert all(label in known for label in references),sorted(set(references)-known)
print("PASS every receiver reference resolves to an existing permanent identity.")

displays=re.findall(r"\\\[(.*?)\\\]",source,re.S)
inlines=re.findall(r"\\\((.*?)\\\)",source,re.S)
dollars=re.findall(r"(?<!\\)\$([^$]+)(?<!\\)\$",source,re.S)
fragments=displays+inlines+dollars
clean=[]
for f in fragments:
    f=re.sub(r"\\hypertarget\{[^}]+\}\{\}","",f)
    f=re.sub(r"\\(?:tag|label)\{[^}]+\}","",f).strip()
    clean.append(f)
p=subprocess.run(["pandoc","--from=markdown+tex_math_dollars","--to=html","--mathml"],
                 input="\n\n".join("$$\n"+f+"\n$$" for f in clean),
                 text=True,capture_output=True,check=False)
assert p.returncode==0,p.stderr
assert not p.stderr.strip(),p.stderr
assert len(re.findall(r"<math(?:\s|>)",p.stdout))==len(fragments)
print("PASS receiver LF/control bytes, delimiters and all",len(fragments),"mathematical fragments.")

post=(LANE/(BASE+"post_exposure_derivation.md")).read_text()
assert "\r" not in post and all(ord(x)>=32 or x in "\n\t" for x in post)
postfrags=re.findall(r"\\\[(.*?)\\\]",post,re.S)+re.findall(r"\\\((.*?)\\\)",post,re.S)
p=subprocess.run(["pandoc","--from=markdown+tex_math_dollars","--to=html","--mathml"],
                 input="\n\n".join("$$\n"+f.strip()+"\n$$" for f in postfrags),
                 text=True,capture_output=True,check=False)
assert p.returncode==0 and not p.stderr.strip(),p.stderr
assert len(re.findall(r"<math(?:\s|>)",p.stdout))==len(postfrags)
print("PASS all",len(postfrags),"post-exposure mathematical fragments.")

patterns_data=json.loads((LANE/(BASE+"fresh_patterns.json")).read_text())
for row in patterns_data["profile_counts"]:
    values=[row["OS"],row["profile"],row["rows"],row["nonzero_multiplicative"],
            row["patterns"],row["all_star_original"],row["individual_choices"]]
    line=" & ".join(map(str,values))+r" \\"
    assert source.count(line)==1,line
extra=Counter((x["key"][0],x["key"][1]) for x in patterns_data["extra_finite_star_families"])
assert sum(extra.values())==36
for (os,profile),count in extra.items():
    assert f"{os} & {profile} & {count} "+r"\\" in source
assert len(patterns_data["patterns"])==495
assert sum(x["all_star_original"] for x in patterns_data["patterns"])==459
print("PASS all 21 count rows and the 36-pattern 495-to-459 retraction, with every profile total.")

postdata=json.loads((LANE/(BASE+"post_exposure_data.json")).read_text())
assert len(postdata["rankone"])==436 and len(postdata["zero_weight"])==172
assert sum(x["narrow"] for x in postdata["rankone"])==316
for x in postdata["zero_weight"]:
    a=x["row"][2]
    assert x["smith_one"]==[1,1,a] and x["smith_two"]==[1,1,1,1,a]
print("PASS complete new auxiliary data: 436 primitive factors and 172 exact zero-weight Smith pairs.")

for name in ("post_exposure","receiver"):
    stem=ROOT/"code"/("S6_SERIES_PUBLISH_c7_ld_"+name)
    ast.parse(stem.with_suffix(".py").read_text())
    assert stem.with_suffix(".err").read_bytes()==b""
    output=stem.with_suffix(".out").read_text()
    assert output.endswith("\n") and "PASS" in output
    print("PASS",name,"complete source/output readback;",len(output.splitlines()),"output lines; error empty.")
print("SCOPE syntax, permanent identities and saved integer-data readback; no TeX/PDF build or page credit.")
print("RECEIVER_SHA256",sha256(raw).hexdigest())

