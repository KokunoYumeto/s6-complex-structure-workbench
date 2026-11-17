# Mechanical diff of every row of the source table: printed statement (taken from the paper's TeX by label) against the
# source statement (taken from the source file by id). Output: out/diff_rows.json and out/diff_summary.txt.
import csv, json, os, re, sys, collections, difflib, hashlib

W = r"C:\Users\user\Documents\s6_pro_prompts_20261112_work"
R = W + r"\returns\S6_07_PAPER_final_20261116T1537Z_unzipped"
HERE = W + r"\reviews\S6_PAPER_DRAFT_CHECK_20261116"
os.makedirs(HERE + r"\out", exist_ok=True)
RUNDIR = {
    "returns/S6_02_FAMILY/": W + r"\returns\S6_02_FAMILY_unzipped\S6_02_FAMILY",
    "returns/S6_02_PUSH/": W + r"\returns\S6_02_PUSH_final_20261115T2217Z_unzipped\S6_02_PUSH",
    "returns/S6_01_INVARIANTS/": W + r"\returns\S6_01_INVARIANTS_unzipped\S6_01_INVARIANTS",
    "returns/S6_05_ARITHMETIC/": W + r"\returns\S6_05_ARITHMETIC_final_20261115T1846Z_unzipped\S6_05_ARITHMETIC",
    "returns/S6_04_MAPS_MANIFOLDS/": W + r"\returns\S6_04_MAPS_MANIFOLDS_checkpoint_12_20261116T0243Z_unzipped\S6_04_MAPS_MANIFOLDS",
    "returns/S6_03_CDP/": W + r"\returns\S6_03_CDP_checkpoint_13_20261116T0136Z_unzipped\S6_03_CDP",
}
EXTRA = {
    "papers/arXiv_2610.00250v1_Du_Guo_Kusakabe_Xie.tex": W + r"\literature\arXiv_2610.00250v1\v5oka_maps_modifications_deformations.tex",
    "workbench/period_shift_classification.tex": W + r"\staging\S6_3_FAMILY\workbench\period_shift_classification.tex",
    "status/REVIEW_S6_02_FAMILY.md": W + r"\reviews\S6_02_REVIEW_FABLE\REVIEW.md",
}
tex = open(R + r"\S6_07_PAPER_paper.tex", encoding="utf-8").read()
rows = list(csv.DictReader(open(R + r"\S6_07_PAPER_source_table.csv", encoding="utf-8")))
ENVS = "theorem|proposition|lemma|corollary|cited|announcement|computed|refuted|definition|remark|example|openq"


def resolve(sf):
    sf = sf.strip()
    if sf in EXTRA:
        return EXTRA[sf] if os.path.exists(EXTRA[sf]) else None
    for pre, d in RUNDIR.items():
        if sf.startswith(pre):
            p = os.path.join(d, sf[len(pre):].replace("/", "\\"))
            return p if os.path.exists(p) else None
    return None


def paper_env(label):
    i = tex.find("\\label{%s}" % label)
    if i < 0:
        return None, None, None
    begins = [m for m in re.finditer(r"\\begin\{(%s)\}" % ENVS, tex[:i])]
    if not begins:
        return None, None, None
    b = begins[-1]
    env = b.group(1)
    e = tex.find("\\end{%s}" % env, i)
    if e < 0 or tex.find("\\end{%s}" % env, b.end(), i) >= 0:
        return None, None, None  # label not inside an environment
    line = tex.count("\n", 0, b.start()) + 1
    body = tex[b.end():e]
    body = re.sub(r"^\s*\[[^\]]*\]", "", body, count=1)  # the optional argument (run label; status; title)
    return env, body, line


def source_stmt(text, sid):
    ids = [s.strip() for s in re.split(r"[;,]", sid) if s.strip()]
    for s in ids:
        s0 = s.split(" (")[0].strip()
        if not re.match(r"^[A-Za-z]{0,4}\.?\d[\w.]*$|^[A-Z]\d+[a-z]?$|^[A-Z]\d\.\d+$", s0):
            continue
        pat = re.escape(s0)
        m = re.search(r"\\begin\{(\w+)\}\s*(?:\[|\{)\s*" + pat + r"(?![\w.]*\d)[^\n]*", text)
        if m:
            env = m.group(1)
            e = text.find("\\end{%s}" % env, m.end())
            return s0, m.group(0), text[m.end():e]
        m = re.search(r"\\paragraph\{[^\n]*?\b" + pat + r"(?![\w.]*\d)[^\n]*", text)
        if m:
            rest = text[m.end():]
            e = re.search(r"\\paragraph\{|\\begin\{proof\}|\\emph\{Proof|\\textit\{Proof|\\textbf\{Proof|\n\s*Proof\.|\\subsection|\\section", rest)
            return s0, m.group(0), rest[:e.start()] if e else rest[:6000]
    return None, None, None


DROP_CMD = set("mathbb mathcal mathrm mathbf mathfrak mathsf operatorname text textbf textit emph rm bf it left right bigl bigr Bigl Bigr big Big bigg Bigg quad qquad displaystyle textstyle scriptstyle limits nolimits noindent par smallskip medskip bigskip label tag nonumber allowbreak hfill break mbox hbox ensuremath boldsymbol".split())
ALIAS = {"tfrac": "frac", "dfrac": "frac", "widehat": "hat", "widetilde": "tilde", "le": "leq", "ge": "geq", "ne": "neq", "to": "rightarrow", "longrightarrow": "rightarrow", "colon": ":", "dots": "ldots", "cdots": "ldots", "dotsc": "ldots", "varepsilon": "epsilon", "vartheta": "theta", "varphi": "phi", "Pp": "P", "PP": "P", "OO": "O", "ZZ": "Z", "CC": "C", "QQ": "Q", "RR": "R", "cO": "O", "bZ": "Z", "bC": "C", "bQ": "Q", "bR": "R", "bP": "P", "Im": "Im", "Re": "Re", "im": "Im", "re": "Re"}


def norm_tokens(s):
    s = re.sub(r"(?<!\\)%[^\n]*", "", s)
    s = re.sub(r"\\(label|uses|tag)\{[^{}]*\}", " ", s)
    s = re.sub(r"\\(c|C|eq|auto)?ref\{[^{}]*\}", " REF ", s)
    s = re.sub(r"\\cite(\[[^\]]*\])?\{[^{}]*\}", lambda m: " CITE " + (m.group(1) or ""), s)
    s = re.sub(r"\\(begin|end)\{(equation|align|aligned|gather|gathered|split|multline|displaymath)\*?\}", " ", s)
    s = s.replace("\\[", " ").replace("\\]", " ").replace("\\(", " ").replace("\\)", " ").replace("$", " ")
    s = re.sub(r"\\[,;!: ]", " ", s).replace("~", " ").replace("\\\\", " ").replace("&", " ")
    toks = []
    for m in re.finditer(r"\\([A-Za-z]+)|([A-Za-z]+)|(\d+)|([^\sA-Za-z\d{}\\])", s):
        if m.group(1):
            c = m.group(1)
            if c in DROP_CMD:
                continue
            toks.append(ALIAS.get(c, c))
        elif m.group(2):
            toks.append(ALIAS.get(m.group(2), m.group(2)))
        elif m.group(3):
            toks.append(m.group(3))
        else:
            ch = m.group(4)
            if ch in ".,;:":  # punctuation changes are not content
                continue
            toks.append(ch)
    return toks


def ops(a, b):
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    out = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag != "equal":
            out.append((" ".join(a[i1:i2]), " ".join(b[j1:j2])))
    return sm.ratio(), out


results = []
pair_freq = collections.Counter()
for r in rows:
    lab = r["paper_label"]
    env, body, line = paper_env(lab)
    res = {"label": lab, "status": r["status"], "run": r["source_run"], "sid": r["source_id"], "line": line, "env": env}
    # CSV text against the TeX body
    if body is not None:
        tb, tc = norm_tokens(body), norm_tokens(r["statement_as_printed"])
        rr, oo = ops(tc, tb)
        res["csv_vs_tex_ratio"] = round(rr, 4)
        res["csv_vs_tex_ops"] = len(oo)
    else:
        res["problem"] = "label not found as an environment in the paper"
    srcs = [resolve(x) for x in r["source_file"].split(";")]
    res["src_resolved"] = [bool(x) for x in srcs]
    found = None
    for sp in srcs:
        if not sp:
            continue
        st = open(sp, encoding="utf-8").read()
        sid, head, sbody = source_stmt(st, r["source_id"])
        if sbody is not None:
            found = (sid, head, sbody, sp)
            break
    if found and body is not None:
        sid, head, sbody, sp = found
        res["src_head"] = head[:140]
        a, b = norm_tokens(sbody), norm_tokens(body)
        ratio, oo = ops(a, b)
        res["ratio"] = round(ratio, 4)
        res["n_src_tokens"], res["n_print_tokens"] = len(a), len(b)
        res["ops"] = oo
        for o in oo:
            pair_freq[o] += 1
    elif body is not None:
        res["problem"] = res.get("problem", "") + " source statement not located by id"
    results.append(res)

common = {p for p, n in pair_freq.items() if n >= 3}
lines = []
lines.append("rows %d" % len(results))
lines.append("frequent replacement pairs (>=3 rows), treated as notation: " + json.dumps(sorted(((a, b, pair_freq[(a, b)]) for a, b in common), key=lambda x: -x[2])[:70], ensure_ascii=False))
nident = 0
for res in results:
    if "ops" in res:
        resid = [o for o in res["ops"] if o not in common]
        res["residual"] = resid
        if not resid:
            nident += 1
lines.append("located and compared: %d; identical after notation pairs: %d; not located: %d; label missing: %d" % (
    sum(1 for x in results if "ops" in x), nident, sum(1 for x in results if "ops" not in x and x.get("env")), sum(1 for x in results if not x.get("env"))))
lines.append("csv_vs_tex mismatches: " + json.dumps([(x["label"], x["csv_vs_tex_ratio"], x["csv_vs_tex_ops"]) for x in results if x.get("csv_vs_tex_ops")], ensure_ascii=False))
lines.append("env vs status: " + json.dumps(collections.Counter((x["status"], x["env"]) for x in results).most_common(), ensure_ascii=False))
for res in results:
    if "ops" in res and res["residual"]:
        short = [(a[:70], b[:70]) for a, b in res["residual"][:int(sys.argv[1]) if len(sys.argv) > 1 else 8]]
        lines.append("%s | %s | l.%s | ratio %.3f | src %d print %d tok | residual %d | head: %s | %s" % (
            res["label"], res["status"], res["line"], res["ratio"], res["n_src_tokens"], res["n_print_tokens"], len(res["residual"]),
            res["src_head"][:80], json.dumps(short, ensure_ascii=False)))
    elif "ops" not in res:
        lines.append("%s | %s | l.%s | NOT COMPARED: %s | sid: %s | resolved %s" % (res["label"], res["status"], res["line"], res.get("problem"), res["sid"][:60], res["src_resolved"]))
json.dump(results, open(HERE + r"\out\diff_rows.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
open(HERE + r"\out\diff_summary.txt", "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("\n".join(l[:900] for l in lines[:5]))
print("flag lines:", len(lines) - 5)
