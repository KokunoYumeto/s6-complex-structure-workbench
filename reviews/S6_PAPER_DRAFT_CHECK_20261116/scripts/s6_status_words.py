# Status of every row against the environment that prints it; sizes of the parts to read; forbidden and sensitive words.
import json, re, collections
HERE = r"C:\Users\user\Documents\s6_pro_prompts_20261112_work\reviews\S6_PAPER_DRAFT_CHECK_20261116"
R = r"C:\Users\user\Documents\s6_pro_prompts_20261112_work\returns\S6_07_PAPER_final_20261116T1537Z_unzipped\S6_07_PAPER_paper.tex"
tex = open(R, encoding="utf-8").read()
lines = tex.split("\n")
res = json.load(open(HERE + r"\out\diff_rows.json", encoding="utf-8"))
by = collections.defaultdict(list)
for r in res:
    by[(r["run"], r["status"], r["env"])].append(r["label"].split(":", 1)[-1])
for k in sorted(by, key=str):
    print(k, " ".join(by[k]))
def size(a, b):
    return sum(len(l) + 1 for l in lines[a - 1:b])
for name, a, b in (("front matter 1-212", 1, 212), ("Result 213-264", 213, 264), ("2a 472-483", 472, 483), ("Open+Limits+record 6197-6229", 6197, 6229), ("App A 6230-6823", 6230, 6823), ("App B 6824-7407", 6824, 7407), ("App C 7408-end", 7408, len(lines))):
    print(name, size(a, b), "chars")
# words
low = tex
for pat in (r"\bfirst\b", r"\bpriority\b", r"\bbefore\b", r"\bearlier than\b", r"AI-assisted", r"independently", r"\bnovel\b", r"\bnew\b", r"Overleaf", r"Reddit", r"Zenodo", r"8 Sep|September 2026|23 Sep|23 Oct|October 2026|2026-\d\d-\d\d", r"version~?2|v2\b", r"CC0", r"no human", r"effort", r"Campana", r"Counterexample|counterexample", r"two runs", r"no second reader", r"unverified", r"Fable|Opus|Astra"):
    ms = [m for m in re.finditer(pat, low)]
    ls = sorted({tex.count("\n", 0, m.start()) + 1 for m in ms})
    print(pat, len(ms), "lines:", ls[:40])
