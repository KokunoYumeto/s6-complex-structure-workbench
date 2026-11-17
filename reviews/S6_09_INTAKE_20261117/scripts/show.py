import csv, sys
csv.field_size_limit(10**9)
R = r"C:\Users\user\Documents\s6_pro_prompts_20261112_work\returns\S6_09_PAPERS_final_20261117T0601Z_unzipped"
inv = list(csv.DictReader(open(R + r"\S6_09_PAPERS_inventory.csv", encoding="utf-8", newline="")))
run, ids = sys.argv[1], sys.argv[2].split(",")
cols = sys.argv[3].split(",") if len(sys.argv) > 3 else ["paper","printed_label","kind","statement_as_printed","recorded_checks","your_check","check_outcome","credited_to","notes"]
lim = int(sys.argv[4]) if len(sys.argv) > 4 else 1500
for r in inv:
    if (run == "*" or r["source_run"] == run) and (r["source_id"] in ids or r["printed_label"] in ids):
        print("#####", r["source_run"], r["source_id"], r["source_file"])
        for c in cols:
            print("  [%s] %s" % (c, r[c][:lim].replace("\n", " ")))
