import csv, collections, re
csv.field_size_limit(10**9)
R = r"C:\Users\user\Documents\s6_pro_prompts_20261112_work\returns\S6_09_PAPERS_final_20261117T0601Z_unzipped"
inv = list(csv.DictReader(open(R + r"\S6_09_PAPERS_inventory.csv", encoding="utf-8", newline="")))
c = collections.Counter(r["recorded_checks"] for r in inv)
print("distinct recorded_checks", len(c))
for k, n in c.most_common(25):
    print("%5d | %s" % (n, k.replace("\n", " ")[:1500]))
    print()
print("=== rows with notable outcome words")
for r in inv:
    o = r["check_outcome"]
    if re.search(r"timed out|remains|unresolved|open|conditional|not asserted|refuted|false|corrected|error", o, re.I):
        print("--", r["paper"], r["source_run"], r["source_id"], "|", r["printed_label"], "|", r["kind"], "|", o[:500].replace("\n", " "))
print()
print("=== your_check top values")
c = collections.Counter(r["your_check"] for r in inv)
for k, n in c.most_common(8):
    print("%5d | %s" % (n, k.replace("\n", " ")[:1200]))
    print()
