# For every inventory row: is its printed label a \label in its paper; does the printed statement text equal the TeX at
# the label; is there a proof (a \begin{proof} before the next statement environment, or a pointer to an appendix proof).
import csv, re, collections, json, bisect
csv.field_size_limit(10**9)
R = r"C:\Users\user\Documents\s6_pro_prompts_20261112_work\returns\S6_09_PAPERS_final_20261117T0601Z_unzipped"
OUT = r"C:\Users\user\Documents\s6_pro_prompts_20261112_work\reviews\S6_09_INTAKE_20261117\out"
inv = list(csv.DictReader(open(R + r"\S6_09_PAPERS_inventory.csv", encoding="utf-8", newline="")))
tex = {p: open(R + r"\S6_09_PAPERS_%s.tex" % p, encoding="utf-8").read() for p in ("I", "II", "III")}
BS = chr(92)
norm = lambda s: re.sub(r"\s+", " ", s).strip()
res = collections.Counter()
out = []
labpos = {p: {m.group(1): m.start() for m in re.finditer(re.escape(BS + "label{") + r"([^}]+)\}", tex[p])} for p in tex}
# environments: every \begin{X} whose X is declared by \newtheorem in the preamble
envnames = {}
for p in tex:
    names = set(re.findall(re.escape(BS + "newtheorem") + r"\*?\{([A-Za-z]+)\}", tex[p]))
    envnames[p] = names
    print("paper", p, "theorem-like environments:", sorted(names))
begins = {}
for p in tex:
    pat = re.escape(BS + "begin{") + "(?:" + "|".join(sorted(envnames[p])) + r")\*?\}"
    begins[p] = [m.start() for m in re.finditer(pat, tex[p])]
    print("paper", p, "statement environments:", len(begins[p]), " proofs:", tex[p].count(BS + "begin{proof}"))
for r in inv:
    p, lab = r["paper"], r["printed_label"]
    row = {"run": r["source_run"], "id": r["source_id"], "paper": p, "label": lab, "kind": r["kind"]}
    if lab not in labpos[p]:
        other = [q for q in tex if lab in labpos[q]]
        row["label_found"] = "NO" + (" (in paper %s)" % ",".join(other) if other else "")
        res["label missing in its paper"] += 1
        out.append(row)
        continue
    pos = labpos[p][lab]
    row["line"] = tex[p].count("\n", 0, pos) + 1
    st = norm(r["statement_as_printed"])
    window = norm(tex[p][max(0, pos - 4000): pos + len(r["statement_as_printed"]) + 8000])
    row["statement_in_tex"] = (st[:400] in window) if len(st) >= 40 else (st in window)
    res["statement text found at label" if row["statement_in_tex"] else "statement text NOT at label"] += 1
    endpat = re.escape(BS + "end{") + "(" + "|".join(sorted(envnames[p])) + r")\*?\}"
    m = re.search(endpat, tex[p][pos:pos + 60000])
    # is the label inside a statement environment? (last begin before pos is after last end before pos)
    i0 = bisect.bisect_right(begins[p], pos) - 1
    inside = False
    if i0 >= 0:
        seg0 = tex[p][begins[p][i0]:pos]
        inside = re.search(endpat, seg0) is None
    if m and inside:
        endpos = pos + m.end()
        i = bisect.bisect_right(begins[p], endpos)
        nxt = begins[p][i] if i < len(begins[p]) else len(tex[p])
        seg = tex[p][endpos:nxt]
        if BS + "begin{proof}" in seg:
            row["proof"] = "adjacent"
        elif re.search(r"re-deriv|rederiv|proof is given in|is proved in|Appendix~|app:", seg[:3000]):
            row["proof"] = "pointer to appendix/other label"
        else:
            row["proof"] = "none adjacent"
            row["after"] = norm(seg[:300])
    else:
        row["proof"] = "label not in a statement environment"
        row["context"] = norm(tex[p][pos - 200:pos + 200])
    res["proof: " + row["proof"]] += 1
    out.append(row)
for k, v in sorted(res.items()):
    print("%5d  %s" % (v, k))
json.dump(out, open(OUT + r"\s6_labels.json", "w", encoding="utf-8"), indent=0)
print()
for row in out:
    if row.get("label_found", "").startswith("NO"):
        print("MISSING LABEL", row)
print()
c = collections.Counter((row["paper"], row.get("proof")) for row in out)
for k in sorted(c, key=str):
    print(k, c[k])
print()
for row in out:
    if row.get("statement_in_tex") is False:
        print("STATEMENT MISMATCH", row["paper"], row["run"], row["id"], row["label"], row.get("line"))
print()
n = 0
for row in out:
    if row.get("proof") in ("none adjacent", "label not in a statement environment"):
        n += 1
        if n <= 400:
            print(row["paper"], row["run"], row["id"], "|", row["label"], "| line", row.get("line"), "|", row["kind"], "|", row["proof"], "|", (row.get("after") or row.get("context") or "")[:230])
