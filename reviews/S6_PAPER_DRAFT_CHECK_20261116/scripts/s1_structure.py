# Structure of the paper and statistics of the source table (no content dumped).
import csv, re, sys, collections
R = r"C:\Users\user\Documents\s6_pro_prompts_20261112_work\returns\S6_07_PAPER_final_20261116T1537Z_unzipped"
tex = open(R + r"\S6_07_PAPER_paper.tex", encoding="utf-8").read()
lines = tex.split("\n")
print("lines", len(lines), "chars", len(tex))
for i, l in enumerate(lines, 1):
    m = re.match(r"\\(part|section|subsection|appendix)\*?\s*(\{.*)?$", l)
    if m and (l.startswith("\\section") or l.startswith("\\appendix") or l.startswith("\\part") or (len(sys.argv) > 1 and l.startswith("\\subsection"))):
        print(i, l[:120])
envs = collections.Counter(re.findall(r"\\begin\{([a-zA-Z*]+)\}", tex))
print({k: v for k, v in envs.items() if k not in ("equation", "aligned", "align", "pmatrix", "cases", "array", "gathered", "smallmatrix", "split", "itemize", "enumerate", "tabular", "center")})
print("newtheorem:", re.findall(r"\\newtheorem\*?\{(\w+)\}(?:\[\w+\])?\{([^}]*)\}", tex))
rows = list(csv.DictReader(open(R + r"\S6_07_PAPER_source_table.csv", encoding="utf-8")))
print("rows", len(rows), list(rows[0].keys()))
for col in ("status", "source_run", "wording_vs_source", "found_in_AC26", "found_in_E26", "found_in_DGKX_v1", "credited_to"):
    c = collections.Counter((r[col] or "")[:70] for r in rows)
    print(col, len(c), c.most_common(12))
print("source_file:", collections.Counter(r["source_file"] for r in rows).most_common(40))
print("label sample:", [r["paper_label"] for r in rows[:12]])
print("source_id sample:", [r["source_id"] for r in rows[:12]])
print("checks sample:", rows[0]["checks"][:300])
