# (1) Proofs whose source proof was mislocated (the K-proofs moved to Appendix B): best match among all proofs of the
#     first run's AB.tex and of the workbench file.  (2) For every proof: the print-only runs of 12 tokens or more, and
#     whether that text occurs anywhere in the six returns (4-token shingle cover); runs with cover < 0.85 are new text.
import json, os, re, sys, difflib, glob
HERE = r"C:\Users\user\Documents\s6_pro_prompts_20261112_work\reviews\S6_PAPER_DRAFT_CHECK_20261116"
src = open(HERE + r"\scripts\s3_diff.py", encoding="utf-8").read().split("results = []")[0]
ns = {}
exec(src, ns)
tex, norm_tokens, RUNDIR, EXTRA = ns["tex"], ns["norm_tokens"], ns["RUNDIR"], ns["EXTRA"]
s7 = open(HERE + r"\scripts\s7_proofs.py", encoding="utf-8").read().split("out, recs = [], []")[0].split("def source_proof")[0]
exec(s7.split("rowby =")[1].split("\n", 1)[1], ns)  # strip_subs, clean_proof
strip_subs, clean_proof = ns["strip_subs"], ns["clean_proof"]
recs = json.load(open(HERE + r"\out\proofs.json", encoding="utf-8"))


def toks(s):
    return strip_subs(norm_tokens(clean_proof(s)))


# all source text, tokenised once
alltoks = []
files = []
for d in RUNDIR.values():
    for f in glob.glob(os.path.join(d, "sections", "*.tex")) + glob.glob(os.path.join(d, "fragments", "*.tex")):
        files.append(f)
files += [EXTRA["workbench/period_shift_classification.tex"]]
for f in files:
    alltoks += toks(open(f, encoding="utf-8").read()) + ["<<FILE>>"] * 5
S = set(tuple(alltoks[i:i + 4]) for i in range(len(alltoks) - 3))
print("source files", len(files), "tokens", len(alltoks))

# (1) candidate source proofs for the moved K-proofs
cands = []
for f in (os.path.join(RUNDIR["returns/S6_02_FAMILY/"], "sections", "AB.tex"), EXTRA["workbench/period_shift_classification.tex"]):
    st = open(f, encoding="utf-8").read()
    for m in re.finditer(r"\\begin\{proof\}(\[[^\]]*\])?", st):
        e = st.find("\\end{proof}", m.end())
        heads = re.findall(r"\\begin\{(?:theorem|proposition|lemma|corollary)\}(?:\[([^\]]*)\])?(?:\\label\{([^}]*)\})?", st[:m.start()])
        cands.append((os.path.basename(f), (heads[-1][0] or heads[-1][1])[:40] if heads else "?", toks(st[m.end():e])))
proofs = [(m.start(), m.end()) for m in re.finditer(r"\\begin\{proof\}(\[[^\]]*\])?", tex)]
for (ps, pe0), rec in zip(proofs, recs):
    body = tex[pe0:tex.find("\\end{proof}", pe0)]
    b = toks(body)
    note = ""
    if rec.get("ratio", 0) < 0.5:
        best = max(cands, key=lambda c: difflib.SequenceMatcher(None, c[2], b, autojunk=False).quick_ratio())
        sm = difflib.SequenceMatcher(None, best[2], b, autojunk=False)
        oo = [(" ".join(best[2][i1:i2]), " ".join(b[j1:j2])) for tag, i1, i2, j1, j2 in sm.get_opcodes() if tag != "equal"]
        rec["ops"] = oo
        note = "REMATCHED to %s %s: ratio %.3f, src %d print %d tok" % (best[0], best[1], sm.ratio(), len(best[2]), len(b))
    runs = [o[1].split() for o in rec.get("ops", []) if len(o[1].split()) >= 12]
    new = []
    for r in runs:
        sh = [tuple(r[i:i + 4]) for i in range(len(r) - 3)]
        cov = sum(1 for s in sh if s in S) / max(1, len(sh))
        if cov < 0.85:
            new.append((len(r), round(cov, 2), " ".join(r)[:int(sys.argv[1]) if len(sys.argv) > 1 else 170]))
    if note or new:
        print("l.%d | %s | %s | long print-only runs %d, of which not found in any source: %s" % (rec["line"], rec["label"], note, len(runs), json.dumps(new, ensure_ascii=False)))
