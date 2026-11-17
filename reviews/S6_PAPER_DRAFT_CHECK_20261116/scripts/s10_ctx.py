import re, sys, difflib, csv
HERE = r"C:\Users\user\Documents\s6_pro_prompts_20261112_work\reviews\S6_PAPER_DRAFT_CHECK_20261116"
src = open(HERE + r"\scripts\s3_diff.py", encoding="utf-8").read().split("results = []")[0]
ns = {}; exec(src, ns)
rows, resolve, paper_env, source_stmt, norm_tokens = ns["rows"], ns["resolve"], ns["paper_env"], ns["source_stmt"], ns["norm_tokens"]
lab = sys.argv[1]; want = sys.argv[2:]
r = [x for x in rows if x["paper_label"] == lab][0]
env, body, line = paper_env(lab)
st = open(resolve(r["source_file"].split(";")[0]), encoding="utf-8").read()
sid, head, sbody = source_stmt(st, r["source_id"])
a, b = norm_tokens(sbody), norm_tokens(body)
sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag != "equal" and (not want or " ".join(a[i1:i2]) in want or any(w in " ".join(b[j1:j2]) for w in want)):
        print("SRC:", " ".join(a[max(0, i1 - 9):i2 + 9]), "\nPRT:", " ".join(b[max(0, j1 - 9):j2 + 9]), "\n")
