import csv, re, sys, json
csv.field_size_limit(10**9)
R = r"C:\Users\user\Documents\s6_pro_prompts_20261112_work\returns\S6_09_PAPERS_final_20261117T0601Z_unzipped"
OUT = r"C:\Users\user\Documents\s6_pro_prompts_20261112_work\reviews\S6_09_INTAKE_20261117\out"
inv = list(csv.DictReader(open(R + r"\S6_09_PAPERS_inventory.csv", encoding="utf-8", newline="")))
aux = json.load(open(OUT + r"\aux_labels.json", encoding="utf-8"))
runs = sys.argv[1].split(",")
pref = sys.argv[2] if len(sys.argv) > 2 else ""
for r in inv:
    if r["source_run"] in runs and r["source_id"].startswith(pref):
        s = re.sub(r"\s+", " ", r["statement_as_printed"])
        m = re.match(r".begin.[a-z]+.(\[(.*?)\])?", s)
        t = m.group(2) if m and m.group(2) else re.sub(r".label.[^}]*.", "", s[len(m.group(0)) if m else 0:])[:110]
        a = aux[r["paper"]].get(r["printed_label"], {})
        print("%s | %s %s %s p.%s | %s | %s" % (r["source_id"], r["paper"], a.get("anchor", "?").split(".")[0][:4], a.get("num", "?"), a.get("page", "?"), r["kind"][:14], t[:120]))
