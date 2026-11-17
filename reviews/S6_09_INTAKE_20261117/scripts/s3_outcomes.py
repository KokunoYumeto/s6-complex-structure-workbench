import csv, collections, re
csv.field_size_limit(10**9)
R = r"C:\Users\user\Documents\s6_pro_prompts_20261112_work\returns\S6_09_PAPERS_final_20261117T0601Z_unzipped"
inv = list(csv.DictReader(open(R + r"\S6_09_PAPERS_inventory.csv", encoding="utf-8", newline="")))
c = collections.Counter(r["check_outcome"] for r in inv)
print("distinct outcomes", len(c), "empty", sum(1 for r in inv if not r["check_outcome"].strip()))
for k, n in c.most_common():
    print("%5d | %s" % (n, k.replace("\n", " ")[:330]))
print()
print("=== kinds that are not plain proved")
for r in inv:
    k = r["kind"]
    if re.search(r"open|question|conditional|gap|diagnostic|verification|correction|counterexample", k, re.I) and not k.startswith("Counterexample") :
        print("--", r["paper"], r["source_run"], r["source_id"], "|", r["printed_label"], "|", k, "|", r["check_outcome"][:200].replace("\n"," "))
