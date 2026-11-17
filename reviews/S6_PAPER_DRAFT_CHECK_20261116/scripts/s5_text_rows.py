# Rows the id-based diff could not compare (text/definition rows, label-based K rows): containment of the printed
# block in the source file(s) by 4-token shingles, and a direct diff for sources addressed by a TeX label.
import csv, json, os, re, sys, importlib.util, difflib
HERE = r"C:\Users\user\Documents\s6_pro_prompts_20261112_work\reviews\S6_PAPER_DRAFT_CHECK_20261116"
spec = importlib.util.spec_from_file_location("s3", HERE + r"\scripts\s3_diff.py")
# reuse helpers without re-running the main loop: exec only the definitions
src = open(HERE + r"\scripts\s3_diff.py", encoding="utf-8").read().split("results = []")[0]
ns = {}
exec(src, ns)
tex, rows, resolve, paper_env, norm_tokens, ops = ns["tex"], ns["rows"], ns["resolve"], ns["paper_env"], ns["norm_tokens"], ns["ops"]
res = {r["label"]: r for r in json.load(open(HERE + r"\out\diff_rows.json", encoding="utf-8"))}
targets = [r for r in rows if "ops" not in res[r["paper_label"]] or res[r["paper_label"]]["ratio"] < 0.6]
SUBS = set("div ell cot rad tau Lambda B circ BC D KS cusp square det mu tan wp t c".split())


def printed_block(label):
    env, body, line = paper_env(label)
    if body is not None:
        return body, line, env
    i = tex.find("\\label{%s}" % label)
    if i < 0:
        return None, None, None
    a = tex.rfind("\n\n", 0, i)
    b = tex.find("\n\n", i)
    return tex[a:b], tex.count("\n", 0, i) + 1, "paragraph"


def strip_subs(toks):  # drop the disambiguating subscripts the paper adds (x _ ell -> x)
    out = []
    i = 0
    while i < len(toks):
        if toks[i] in ("_", "^") and i + 1 < len(toks) and toks[i + 1] in SUBS:
            i += 2
            continue
        out.append(toks[i])
        i += 1
    return out


for r in targets:
    lab = r["paper_label"]
    blk, line, env = printed_block(lab)
    if blk is None:
        print(lab, "| NO LABEL IN PAPER")
        continue
    p = strip_subs(norm_tokens(blk))
    srctoks = []
    for sf in r["source_file"].split(";"):
        sp = resolve(sf)
        if sp:
            srctoks += strip_subs(norm_tokens(open(sp, encoding="utf-8").read()))
    extra = ""
    # label-addressed sources
    for sf in r["source_file"].split(";"):
        sp = resolve(sf)
        if sp:
            st = open(sp, encoding="utf-8").read()
            for cand in re.findall(r"[\w:.\-]+", r["source_id"]):
                j = st.find("\\label{%s}" % cand)
                if j >= 0:
                    bs = [m for m in re.finditer(r"\\begin\{(\w+)\}", st[:j])]
                    if bs:
                        e = st.find("\\end{%s}" % bs[-1].group(1), j)
                        a = norm_tokens(re.sub(r"^\s*\[[^\]]*\]", "", st[bs[-1].end():e]))
                        ratio, oo = ops(strip_subs(a), p)
                        extra = " | BY LABEL %s: ratio %.3f ops %s" % (cand, ratio, json.dumps([(x[:60], y[:60]) for x, y in oo[:6]], ensure_ascii=False))
    if not srctoks:
        print("%s | %s | l.%s | %s | SOURCE NOT ON DISK (%s) | %d tokens" % (lab, r["status"], line, env, r["source_file"][:50], len(p)))
        continue
    S = set(tuple(srctoks[i:i + 4]) for i in range(len(srctoks) - 3))
    sh = [tuple(p[i:i + 4]) for i in range(len(p) - 3)]
    miss = [s for s in sh if s not in S]
    cov = 1 - len(miss) / max(1, len(sh))
    # numbers of the printed block that do not occur in the source at all
    nums = sorted({t for t in p if t.isdigit() and len(t) >= 2} - set(srctoks))
    # merge consecutive missing shingles into runs
    runs, cur, last = [], [], -9
    for i, s in enumerate(sh):
        if s not in S:
            if i == last + 1:
                cur.append(s[-1])
            else:
                if cur:
                    runs.append(" ".join(cur))
                cur = list(s)
            last = i
    if cur:
        runs.append(" ".join(cur))
    print("%s | %s | l.%s | %s | %d tok | shingle cover %.2f | numbers absent from source: %s%s | uncovered: %s" % (
        lab, r["status"], line, env, len(p), cov, nums, extra, json.dumps([x[:int(sys.argv[1]) if len(sys.argv) > 1 else 90] for x in runs[:5]], ensure_ascii=False)))
