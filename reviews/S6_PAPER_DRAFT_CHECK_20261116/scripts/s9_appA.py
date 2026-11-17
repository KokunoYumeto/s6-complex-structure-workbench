import re, json, difflib
HERE = r"C:\Users\user\Documents\s6_pro_prompts_20261112_work\reviews\S6_PAPER_DRAFT_CHECK_20261116"
src = open(HERE + r"\scripts\s3_diff.py", encoding="utf-8").read().split("results = []")[0]
ns = {}; exec(src, ns)
tex, norm_tokens, EXTRA = ns["tex"], ns["norm_tokens"], ns["EXTRA"]
lines = tex.split("\n")
app = "\n".join(lines[6229:6823])
wb = open(EXTRA["workbench/period_shift_classification.tex"], encoding="utf-8").read()
i = wb.find("\begin{document}")
wb = wb[i:] if i >= 0 else wb
a, b = norm_tokens(wb), norm_tokens(app)
sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
ops = [(tag, " ".join(a[i1:i2]), " ".join(b[j1:j2])) for tag, i1, i2, j1, j2 in sm.get_opcodes() if tag != "equal"]
print("workbench tokens", len(a), "appendix tokens", len(b), "ratio %.3f" % sm.ratio(), "ops", len(ops))
import collections
c = collections.Counter((x, y) for t, x, y in ops)
print("repeated pairs:", [(k, n) for k, n in c.most_common(14)])
big = [(t, x[:160], y[:260]) for t, x, y in ops if len(x.split()) + len(y.split()) >= 8]
print("long ops:", len(big))
for o in big[:14]:
    print("  ", json.dumps(o, ensure_ascii=False))
