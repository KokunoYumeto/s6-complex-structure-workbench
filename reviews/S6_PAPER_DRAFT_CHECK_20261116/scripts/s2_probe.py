# Probe: where the source files live locally, how statements are marked in each, and the shape of the writer's records.
import csv, json, os, re, collections
W = r"C:\Users\user\Documents\s6_pro_prompts_20261112_work"
R = W + r"\returns\S6_07_PAPER_final_20261116T1537Z_unzipped"
rows = list(csv.DictReader(open(R + r"\S6_07_PAPER_source_table.csv", encoding="utf-8")))
RUNDIR = {
    "returns/S6_02_FAMILY/": W + r"\returns\S6_02_FAMILY_unzipped",
    "returns/S6_02_PUSH/": W + r"\returns\S6_02_PUSH_final_20261115T2217Z_unzipped",
    "returns/S6_01_INVARIANTS/": W + r"\returns\S6_01_INVARIANTS_unzipped",
    "returns/S6_05_ARITHMETIC/": W + r"\returns\S6_05_ARITHMETIC_final_20261115T1846Z_unzipped",
    "returns/S6_04_MAPS_MANIFOLDS/": W + r"\returns\S6_04_MAPS_MANIFOLDS_checkpoint_12_20261116T0243Z_unzipped",
    "returns/S6_03_CDP/": W + r"\returns\S6_03_CDP_checkpoint_13_20261116T0136Z_unzipped",
}
index = {}
for pre, d in RUNDIR.items():
    for root, dirs, files in os.walk(d):
        for f in files:
            if f.endswith((".tex", ".md")):
                rel = os.path.relpath(os.path.join(root, f), d).replace("\\", "/")
                index.setdefault(pre, {}).setdefault(f, []).append(os.path.join(root, f))
files = collections.Counter()
for r in rows:
    for sf in r["source_file"].split(";"):
        files[sf.strip()] += 1
for sf, n in files.items():
    hit = None
    for pre in RUNDIR:
        if sf.startswith(pre):
            hit = index.get(pre, {}).get(os.path.basename(sf))
    print(n, sf, "->", [h[len(W):] for h in hit] if hit else "NOT RESOLVED")
# how statements are marked in each resolved file: sample of begin lines
seen = set()
for r in rows:
    sf = r["source_file"].split(";")[0].strip()
    if sf in seen:
        continue
    seen.add(sf)
    for pre in RUNDIR:
        if sf.startswith(pre):
            hit = index.get(pre, {}).get(os.path.basename(sf))
            if hit:
                t = open(hit[0], encoding="utf-8").read()
                b = re.findall(r"\\begin\{(?:theorem|proposition|lemma|corollary|definition|remark|problem|statement|claim)[^\n]{0,70}", t)
                print("   ", os.path.basename(sf), "| id:", r["source_id"][:40], "| label:", r["paper_label"], "| begins:", b[:2])
sc = json.load(open(R + r"\records\statement_comparisons.json", encoding="utf-8"))
print(type(sc).__name__, len(sc))
first = sc[0] if isinstance(sc, list) else sc[list(sc)[0]]
print("keys:", list(first.keys()) if isinstance(first, dict) else str(first)[:300])
if isinstance(first, dict):
    for k, v in first.items():
        print("  ", k, ":", str(v)[:160].replace("\n", " "))
