# Print printed statements (from the inventory) with number and page (from the aux), for a list "RUN:ID,RUN:ID,..."
import csv, sys, json, re
csv.field_size_limit(10**9)
R = r"C:\Users\user\Documents\s6_pro_prompts_20261112_work\returns\S6_09_PAPERS_final_20261117T0601Z_unzipped"
OUT = r"C:\Users\user\Documents\s6_pro_prompts_20261112_work\reviews\S6_09_INTAKE_20261117\out"
inv = list(csv.DictReader(open(R + r"\S6_09_PAPERS_inventory.csv", encoding="utf-8", newline="")))
aux = json.load(open(OUT + r"\aux_labels.json", encoding="utf-8"))
short = {"FAM": "S6_02_FAMILY", "PUSH": "S6_02_PUSH", "INV": "S6_01_INVARIANTS", "CDP": "S6_03_CDP", "MAPS": "S6_04_MAPS_MANIFOLDS", "ARI": "S6_05_ARITHMETIC"}
lim = int(sys.argv[2]) if len(sys.argv) > 2 else 1600
extra = sys.argv[3].split(",") if len(sys.argv) > 3 else []
for item in sys.argv[1].split(","):
    run, sid = item.split(":", 1)
    run = short.get(run, run)
    hit = [r for r in inv if r["source_run"] == run and r["source_id"] == sid]
    if not hit:
        print("#### NOT FOUND", item)
        continue
    for r in hit:
        a = aux[r["paper"]].get(r["printed_label"], {})
        s = re.sub(r"\s+", " ", r["statement_as_printed"])
        print("#### %s %s | Paper %s %s %s p.%s | %s | kind: %s" % (run, sid, r["paper"], a.get("anchor", "?").split(".")[0], a.get("num", "?"), a.get("page", "?"), r["printed_label"], r["kind"]))
        print(s[:lim])
        for c in extra:
            print("   [%s] %s" % (c, re.sub(r"\s+", " ", r[c])[:900]))
        print()
