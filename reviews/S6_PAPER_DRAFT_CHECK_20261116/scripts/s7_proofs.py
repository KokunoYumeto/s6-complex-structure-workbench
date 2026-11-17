# Every proof environment of the paper against the proof that follows the source statement.
# For each paper proof: the labelled statement that precedes it, the source proof located after the source statement,
# token ratio and the residual differences after the notation pairs. Output: out/proofs.txt (compact) and out/proofs.json.
import csv, json, os, re, sys, collections, difflib
HERE = r"C:\Users\user\Documents\s6_pro_prompts_20261112_work\reviews\S6_PAPER_DRAFT_CHECK_20261116"
src = open(HERE + r"\scripts\s3_diff.py", encoding="utf-8").read().split("results = []")[0]
ns = {}
exec(src, ns)
tex, rows, resolve, norm_tokens, ENVS = ns["tex"], ns["rows"], ns["resolve"], ns["norm_tokens"], ns["ENVS"]
rowby = {r["paper_label"]: r for r in rows}
SUBS = set("div ell cot rad tau Lambda B circ BC D KS cusp square det mu tan wp t c KS lin vir root mod".split())


def strip_subs(toks):
    out, i = [], 0
    while i < len(toks):
        if toks[i] in ("_", "^") and i + 1 < len(toks) and toks[i + 1] in SUBS:
            i += 2
            continue
        out.append(toks[i])
        i += 1
    return out


def clean_proof(s):
    s = re.sub(r"\\par\\(smallskip|medskip)?\\?noindent\\text(bf|it)\{Step \d+\.\}\\?\s?", " ", s)
    s = re.sub(r"\\par\\smallskip\\noindent\\textbf\{Step \d+\.\}", " ", s)
    s = re.sub(r"\\textbf\{Step~?\s?\d+\.\}|\\textit\{Step~?\s?\d+\.\}|\\emph\{Step~?\s?\d+\.\}", " ", s)
    s = re.sub(r"\b(FAM|PUSH|ARI|INV|MAPS|CDP)\b~?\s?", " ", s)
    s = re.sub(r"\b(fam|push|ari|inv|maps|cdp):", " ", s)
    return s


def source_proof(text, sid):
    for s in [x.strip() for x in re.split(r"[;,]", sid) if x.strip()]:
        s0 = s.split(" (")[0].strip()
        pat = re.escape(s0)
        m = re.search(r"\\begin\{(\w+)\}\s*(?:\[|\{)\s*" + pat + r"(?![\w.]*\d)[^\n]*", text)
        if m:
            e = text.find("\\end{%s}" % m.group(1), m.end())
            nxt = re.search(r"\\begin\{(theorem|proposition|lemma|corollary|statement|claim|remark|problem)\}", text[e:])
            lim = e + nxt.start() if nxt else len(text)
            p = re.search(r"\\begin\{proof\}(\[[^\]]*\])?", text[e:lim])
            if p:
                pe = text.find("\\end{proof}", e + p.end())
                return text[e + p.end():pe]
            return None
        m = re.search(r"\\paragraph\{[^\n]*?\b" + pat + r"(?![\w.]*\d)[^\n]*", text)
        if m:
            rest = text[m.end():]
            p = re.search(r"\\emph\{Proof[^}]*\}|\\textit\{Proof[^}]*\}|\\textbf\{Proof[^}]*\}|\n\s*Proof\.", rest)
            nx = re.search(r"\\paragraph\{", rest)
            if p and (not nx or p.start() < nx.start()):
                return rest[p.end():nx.start() if nx else len(rest)]
    return None


out, recs = [], []
proofs = [(m.start(), m.end()) for m in re.finditer(r"\\begin\{proof\}(\[[^\]]*\])?", tex)]
labels = [(m.start(), m.group(1)) for m in re.finditer(r"\\label\{([^}]+)\}", tex)]
pairfreq = collections.Counter()
tmp = []
for ps, pe0 in proofs:
    pe = tex.find("\\end{proof}", pe0)
    prev = [l for l in labels if l[0] < ps and l[1] in rowby]
    lab = prev[-1][1] if prev else None
    line = tex.count("\n", 0, ps) + 1
    body = tex[pe0:pe]
    rec = {"line": line, "label": lab, "chars": len(body)}
    r = rowby.get(lab)
    sp = None
    if r:
        for sf in r["source_file"].split(";"):
            p = resolve(sf)
            if p:
                st = open(p, encoding="utf-8").read()
                sp = source_proof(st, r["source_id"])
                if sp is None and "workbench" in sf:
                    j = st.find("\\label{%s}" % lab)
                    if j >= 0:
                        q = re.search(r"\\begin\{proof\}(\[[^\]]*\])?", st[j:])
                        if q:
                            sp = st[j + q.end():st.find("\\end{proof}", j + q.end())]
                if sp:
                    break
    if sp:
        a = strip_subs(norm_tokens(clean_proof(sp)))
        b = strip_subs(norm_tokens(clean_proof(body)))
        sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
        oo = [(" ".join(a[i1:i2]), " ".join(b[j1:j2])) for tag, i1, i2, j1, j2 in sm.get_opcodes() if tag != "equal"]
        rec.update(ratio=round(sm.ratio(), 4), ns=len(a), np=len(b), ops=oo)
        for o in oo:
            pairfreq[o] += 1
    recs.append(rec)
common = {p for p, n in pairfreq.items() if n >= 3}
for rec in recs:
    if "ops" in rec:
        resid = [o for o in rec["ops"] if o not in common and not re.fullmatch(r"(REF|CITE|[A-Z] ?\d+( \d+)*|Step|\d|Statement|Proposition|Theorem|Lemma|Section|Part [A-Z]|\[.*\]| )*", (o[0] + " " + o[1]).strip())]
        rec["resid"] = resid
        ins = sum(len(o[1].split()) for o in resid)
        dele = sum(len(o[0].split()) for o in resid)
        rec["ins"], rec["del"] = ins, dele
        out.append("l.%d | %s | src %d print %d tok | ratio %.3f | residual ops %d (print-only tokens %d, source-only %d) | %s" % (
            rec["line"], rec["label"], rec["ns"], rec["np"], rec["ratio"], len(resid), ins, dele,
            json.dumps([(x[:int(sys.argv[1]) if len(sys.argv) > 1 else 60], y[:int(sys.argv[1]) if len(sys.argv) > 1 else 60]) for x, y in sorted(resid, key=lambda o: -len(o[1]))[:3]], ensure_ascii=False)))
    else:
        out.append("l.%d | %s | %d chars | SOURCE PROOF NOT LOCATED" % (rec["line"], rec["label"], rec["chars"]))
json.dump(recs, open(HERE + r"\out\proofs.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
open(HERE + r"\out\proofs.txt", "w", encoding="utf-8").write("\n".join(out) + "\n")
loc = [r for r in recs if "ops" in r]
print("proofs", len(recs), "located", len(loc), "ratio>=0.98:", sum(1 for r in loc if r["ratio"] >= 0.98), "0.9-0.98:", sum(1 for r in loc if 0.9 <= r["ratio"] < 0.98), "<0.9:", sum(1 for r in loc if r["ratio"] < 0.9))
print("no residual:", sum(1 for r in loc if not r["resid"]), "; print-only tokens total:", sum(r["ins"] for r in loc), "; source-only:", sum(r["del"] for r in loc))
