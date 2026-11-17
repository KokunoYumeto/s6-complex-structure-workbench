# label -> (number, page, kind) from the .aux files; and reverse lookup of numbers quoted across papers.
import re, json, sys, collections
R = r"C:\Users\user\Documents\s6_pro_prompts_20261112_work\returns\S6_09_PAPERS_final_20261117T0601Z_unzipped"
OUT = r"C:\Users\user\Documents\s6_pro_prompts_20261112_work\reviews\S6_09_INTAKE_20261117\out"
BS = chr(92)
maps = {}
for p in ("I", "II", "III"):
    aux = open(R + r"\S6_09_PAPERS_%s.aux" % p, encoding="utf-8", errors="replace").read()
    d = {}
    # \newlabel{lab}{{num}{page}{title}{anchor}{}}
    for m in re.finditer(re.escape(BS + "newlabel{") + r"([^}]+)\}\{\{([^{}]*)\}\{([^{}]*)\}\{((?:[^{}]|\{[^{}]*\})*)\}\{([^{}]*)\}", aux):
        lab, num, page, title, anchor = m.groups()
        if lab.endswith("@cref"):
            continue
        d[lab] = {"num": num, "page": page, "anchor": anchor, "title": title[:120]}
    maps[p] = d
    print("paper", p, "labels", len(d))
json.dump(maps, open(OUT + r"\aux_labels.json", "w", encoding="utf-8"))
want = {"II": ["5.1", "13.2"], "III": ["2.4", "6.52", "7.32"], "I": []}
for p, nums in want.items():
    for n in nums:
        hits = [(lab, v["anchor"], v["page"]) for lab, v in maps[p].items() if v["num"] == n and not v["anchor"].startswith(("section", "subsection", "equation", "table", "figure", "appendix", "Item"))]
        print("Paper", p, "number", n, "->", hits[:8])
