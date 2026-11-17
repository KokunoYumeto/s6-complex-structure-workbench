import csv, sys, collections, re, glob, os
csv.field_size_limit(10**9)
W = r"C:\Users\user\Documents\s6_pro_prompts_20261112_work\returns"
R = W + r"\S6_09_PAPERS_final_20261117T0601Z_unzipped"
inv = list(csv.DictReader(open(R + r"\S6_09_PAPERS_inventory.csv", encoding="utf-8", newline="")))
src = {
 "S6_01_INVARIANTS": W + r"\S6_01_INVARIANTS_unzipped\S6_01_INVARIANTS\S6_01_INVARIANTS_results.csv",
 "S6_02_FAMILY": W + r"\S6_02_FAMILY_unzipped\S6_02_FAMILY\S6_02_FAMILY_results.csv",
 "S6_02_PUSH": W + r"\S6_02_PUSH_final_20261115T2217Z_unzipped\S6_02_PUSH\S6_02_PUSH_results.csv",
 "S6_03_CDP": W + r"\S6_03_CDP_checkpoint_13_20261116T0136Z_unzipped\S6_03_CDP\S6_03_CDP_results.csv",
 "S6_04_MAPS_MANIFOLDS": W + r"\S6_04_MAPS_MANIFOLDS_checkpoint_12_20261116T0243Z_unzipped\S6_04_MAPS_MANIFOLDS\S6_04_MAPS_MANIFOLDS_results.csv",
 "S6_05_ARITHMETIC": W + r"\S6_05_ARITHMETIC_final_20261115T1846Z_unzipped\S6_05_ARITHMETIC\S6_05_ARITHMETIC_results.csv",
}
tot = 0
for run, path in src.items():
    rows = list(csv.DictReader(open(path, encoding="utf-8-sig", newline="")))
    idcol = [c for c in rows[0].keys() if c.strip().lower() in ("id", "statement_id", "label", "number")]
    idcol = idcol[0] if idcol else list(rows[0].keys())[0]
    ids = [r[idcol].strip() for r in rows]
    if run == "S6_05_ARITHMETIC":
        idsC = [i for i in ids if i.startswith("C")]
        print(run, "all rows", len(ids), "Part C rows", len(idsC), "other prefixes", collections.Counter(i[:1] for i in ids))
        ids = idsC
    invids = [r["source_id"].strip() for r in inv if r["source_run"] == run]
    tot += len(invids)
    missing = [i for i in ids if i not in invids]
    extra = [i for i in invids if i not in ids]
    dup = [i for i, n in collections.Counter(invids).items() if n > 1]
    print(run, "| source rows", len(ids), "| inventory rows", len(invids), "| missing from inventory", missing[:30], "| extra in inventory", extra[:30], "| dup", dup[:10])
    # status of source vs kind in inventory
    stcol = [c for c in rows[0].keys() if c.strip().lower() == "status"]
    if stcol:
        st = {r[idcol].strip(): r[stcol[0]].strip() for r in rows}
        print("    source statuses:", collections.Counter(st[i] for i in ids if i in st))
print("total inventory run rows", tot)
print()
print("paper x source_run:")
c = collections.Counter((r["paper"], r["source_run"]) for r in inv)
for k in sorted(c): print("  ", k, c[k])
