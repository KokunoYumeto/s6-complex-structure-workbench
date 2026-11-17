# For every run row: what fraction of the 6-token shingles of the printed statement occurs in the run's own TeX
# (all files under the run folder)? Labels, references and citations are removed on both sides. Low cover = wording
# changed against the source (to be read).
import csv, re, os, collections, json
csv.field_size_limit(10**9)
W = r"C:\Users\user\Documents\s6_pro_prompts_20261112_work\returns"
R = W + r"\S6_09_PAPERS_final_20261117T0601Z_unzipped"
OUT = r"C:\Users\user\Documents\s6_pro_prompts_20261112_work\reviews\S6_09_INTAKE_20261117\out"
BS = chr(92)
src = {
 "S6_01_INVARIANTS": W + r"\S6_01_INVARIANTS_unzipped\S6_01_INVARIANTS",
 "S6_02_FAMILY": W + r"\S6_02_FAMILY_unzipped\S6_02_FAMILY",
 "S6_02_PUSH": W + r"\S6_02_PUSH_final_20261115T2217Z_unzipped\S6_02_PUSH",
 "S6_03_CDP": W + r"\S6_03_CDP_checkpoint_13_20261116T0136Z_unzipped\S6_03_CDP",
 "S6_04_MAPS_MANIFOLDS": W + r"\S6_04_MAPS_MANIFOLDS_checkpoint_12_20261116T0243Z_unzipped\S6_04_MAPS_MANIFOLDS",
 "S6_05_ARITHMETIC": W + r"\S6_05_ARITHMETIC_final_20261115T1846Z_unzipped\S6_05_ARITHMETIC",
}
def toks(s):
    s = re.sub(re.escape(BS) + r"(label|ref|cref|Cref|eqref|cite|citet|citep|path|texttt)\*?(\[[^\]]*\])*\{[^}]*\}", " ", s)
    s = re.sub(re.escape(BS) + r"(begin|end)\{[a-zA-Z*]+\}(\[[^\]]*\])?", " ", s)
    s = re.sub(r"(Statement|Theorem|Proposition|Lemma|Corollary|Paper~?I+|Paper)\s*~?[A-Z]?[\d.]*", " ", s)
    return re.findall(r"[A-Za-z]+|\d+", s)
K = 6
inv = list(csv.DictReader(open(R + r"\S6_09_PAPERS_inventory.csv", encoding="utf-8", newline="")))
res = []
for run, d in src.items():
    sh = set()
    for root, dirs, files in os.walk(d):
        if any(x in root for x in ("records", "build", "evidence", "logs", "outputs")):
            continue
        for f in files:
            if f.endswith(".tex"):
                t = toks(open(os.path.join(root, f), encoding="utf-8", errors="replace").read())
                for i in range(len(t) - K + 1):
                    sh.add(tuple(t[i:i + K]))
    for r in inv:
        if r["source_run"] != run:
            continue
        t = toks(r["statement_as_printed"])
        n = max(1, len(t) - K + 1)
        hit = sum(1 for i in range(len(t) - K + 1) if tuple(t[i:i + K]) in sh)
        res.append((hit / n, run, r["source_id"], r["printed_label"], r["paper"], len(t)))
res.sort()
json.dump(res, open(OUT + r"\s9_source_cover.json", "w"))
b = collections.Counter()
for c, *_ in res:
    b["1.00" if c >= 0.999 else ">=0.95" if c >= 0.95 else ">=0.85" if c >= 0.85 else ">=0.60" if c >= 0.6 else "<0.60"] += 1
print("rows", len(res), dict(b))
for c, run, sid, lab, p, n in res[:45]:
    print("%.2f  %-22s %-10s %-28s paper %s  tokens %d" % (c, run, sid, lab, p, n))
