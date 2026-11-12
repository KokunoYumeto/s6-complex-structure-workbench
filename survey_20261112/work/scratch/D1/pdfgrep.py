import sys, re, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
import pypdf
r = pypdf.PdfReader(sys.argv[1])
n = len(r.pages)
cnt = 0
for i in range(0, n):
    try:
        t = r.pages[i].extract_text() or ""
    except Exception:
        continue
    if "4.2.10" in t and ("Coxeter" in t or "racines" in t) and i > 60:
        k = t.find("4.2.10")
        print("=== page", i + 1); print(t[max(0, k - 1800): k + 2600]); cnt += 1
        if cnt >= 2: break
