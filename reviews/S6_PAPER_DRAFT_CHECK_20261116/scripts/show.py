# show.py LABEL [N] [before]: print N characters of the paper starting `before` characters before \label{LABEL};
# show.py @LINE1-LINE2 [N]: print lines LINE1..LINE2, at most N characters;
# show.py /REGEX/ [N] [before]: first match of the regex.
import re, sys
R = r"C:\Users\user\Documents\s6_pro_prompts_20261112_work\returns\S6_07_PAPER_final_20261116T1537Z_unzipped\S6_07_PAPER_paper.tex"
tex = open(R, encoding="utf-8").read()
arg = sys.argv[1]
N = int(sys.argv[2]) if len(sys.argv) > 2 else 1500
before = int(sys.argv[3]) if len(sys.argv) > 3 else 200
if arg.startswith("@"):
    a, b = arg[1:].split("-")
    lines = tex.split("\n")
    out = "\n".join(lines[int(a) - 1:int(b)])
    print(out[:N])
    if len(out) > N:
        print("... [%d more characters]" % (len(out) - N))
elif arg.startswith("/"):
    ms = list(re.finditer(arg.strip("/"), tex))
    print("matches:", len(ms), "at lines", [tex.count("\n", 0, m.start()) + 1 for m in ms[:12]])
    if ms:
        i = ms[0].start()
        print(tex[max(0, i - before):i - before + N])
else:
    i = tex.find("\\label{%s}" % arg)
    print("line", tex.count("\n", 0, i) + 1)
    print(tex[max(0, i - before):i - before + N])
