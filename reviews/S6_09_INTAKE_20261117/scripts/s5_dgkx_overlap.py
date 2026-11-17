# Text of arXiv:2610.00250 v1 reproduced in the papers? 8-word shingles (letters only, lowercased) of the DGKX v1 TeX
# searched in each paper; report line clusters with many hits.
import re, sys, collections
W = r"C:\Users\user\Documents\s6_pro_prompts_20261112_work"
R = W + r"\returns\S6_09_PAPERS_final_20261117T0601Z_unzipped"
def words(s):
    s = re.sub(r"%.*", "", s)
    return re.findall(r"[A-Za-z]{2,}", s.lower())
K = 8
for srcname, src in (("DGKXv1", W + r"\literature\arXiv_2610.00250v1\v5oka_maps_modifications_deformations.tex"),
                     ("DGKXv2", W + r"\literature\arXiv_2610.00250v2\submited-tams.tex")):
    sw = words(open(src, encoding="utf-8", errors="replace").read())
    sh = set(tuple(sw[i:i+K]) for i in range(len(sw)-K+1))
    for p in ("I", "II", "III"):
        lines = open(R + r"\S6_09_PAPERS_%s.tex" % p, encoding="utf-8").read().split("\n")
        # word list with line numbers
        wl = []
        for n, l in enumerate(lines, 1):
            for w in words(l):
                wl.append((w, n))
        hits = collections.Counter()
        tot = 0
        for i in range(len(wl)-K+1):
            if tuple(w for w, _ in wl[i:i+K]) in sh:
                hits[wl[i][1] // 20] += 1
                tot += 1
        print(srcname, "in Paper", p, ": shingle hits", tot, "of", len(wl))
        for b, n in sorted(hits.items()):
            if n >= 12:
                print("     lines %d-%d: %d hits | %s" % (b*20, b*20+19, n, lines[b*20][:110]))
