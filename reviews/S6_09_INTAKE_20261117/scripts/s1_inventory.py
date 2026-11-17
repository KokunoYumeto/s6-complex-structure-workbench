import csv, sys, collections
csv.field_size_limit(10**9)
R = r"C:\Users\user\Documents\s6_pro_prompts_20261112_work\returns\S6_09_PAPERS_final_20261117T0601Z_unzipped"
rows = list(csv.DictReader(open(R + r"\S6_09_PAPERS_inventory.csv", encoding="utf-8", newline="")))
cols = list(rows[0].keys())
print("rows", len(rows), "cols", len(cols))
for c in cols:
    vals = [r[c] for r in rows]
    lens = [len(v) for v in vals]
    distinct = collections.Counter(vals)
    print("==", c, "| empty:", sum(1 for v in vals if not v.strip()), "| distinct:", len(distinct), "| maxlen:", max(lens), "| avglen: %d" % (sum(lens) / len(lens)))
    if len(distinct) <= 40:
        for k, n in distinct.most_common():
            print("     %5d  %r" % (n, k[:150]))
    else:
        for k, n in distinct.most_common(6):
            print("     %5d  %r" % (n, k[:150]))
print()
for r in rows[:2]:
    for c in cols:
        print(c, "::", r[c][:600].replace("\n", " "))
    print("-----")
