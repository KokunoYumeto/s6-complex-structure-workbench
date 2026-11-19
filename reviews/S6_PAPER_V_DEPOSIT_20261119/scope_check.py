"""Do the printed class-0 statements carry the reference-fan scope (sweep 1, correction 2)?
For each label: the paper, whether the statement text (after its record, up to the end of its environment) names the
reference fan, and its first characters."""
import re, pathlib, sys
BS = chr(92)
CP = pathlib.Path("<local>/Documents/s6_pro_prompts_20261112_work/returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z_unzipped/S6_10_PAPERS")
LABELS = sys.argv[1:] or ["push:src:C.3.24", "push:src:C.3.27", "push:src:C.4.1", "push:src:E.1.3", "maps:src:B.6.2", "maps:src:B.6.21",
                          "maps:src:B.6.24", "maps:src:B.6.25", "night:P3F.17", "night:P3K.7", "night:P3K.8"]
SCOPE = re.compile(r"(?i)(reference (cusp )?fan|cusp fan of|reference-fan|for the reference|on the reference|reference cusp)")

def skip_args(t, i, n):
    for _ in range(n):
        while t[i] != "{":
            i += 1
        depth = 0
        while True:
            c = t[i]
            if c == BS:
                i += 2; continue
            if c == "{": depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    i += 1; break
            i += 1
    return i

for p in ["I", "II", "III", "IV", "V", "VI"]:
    t = (CP / f"S6_10_PAPERS_{p}.tex").read_text(encoding="utf-8")
    for lab in LABELS:
        i = t.find(BS + "StatementRecord{" + lab + "}")
        if i < 0:
            continue
        j = skip_args(t, i + len(BS + "StatementRecord"), 4)
        k = t.find(BS + "end{", j)
        stmt = re.sub(r"\s+", " ", t[j:k]).strip()
        print(f"{p} {lab}: reference fan named: {bool(SCOPE.search(stmt))} | {stmt[:1500]}")
