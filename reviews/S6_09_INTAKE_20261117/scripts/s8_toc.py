# Sections (and, with argument "sub", subsections) of each paper with page numbers, from the TeX and aux labels.
import re, sys
R = r"C:\Users\user\Documents\s6_pro_prompts_20261112_work\returns\S6_09_PAPERS_final_20261117T0601Z_unzipped"
BS = chr(92)
want = sys.argv[1].split(",")
sub = len(sys.argv) > 2
for p in want:
    tex = open(R + r"\S6_09_PAPERS_%s.tex" % p, encoding="utf-8").read().split("\n")
    print("=====", p)
    sec = 0
    app = False
    for n, l in enumerate(tex, 1):
        if l.startswith(BS + "appendix") or (BS + "appendix") in l[:30]:
            app = True
            print("%6d  --- appendix ---" % n)
        m = re.match(re.escape(BS) + r"(part|section|subsection)(\*?)\{(.*)", l)
        if m and (m.group(1) != "subsection" or sub):
            print("%6d  %s%s %s" % (n, "   " if m.group(1) == "subsection" else "", m.group(1) + m.group(2), m.group(3)[:130]))
