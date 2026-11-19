"""Where do the superseded values (the polynomial KL(S-1)(S-3)/8, OS45 class 25, the meridian-one line) appear?
Per paper: the section of each occurrence and whether it sits in a statement printed as false or as a correction."""
import re, pathlib, collections
BS = chr(92)
CP = pathlib.Path("<local>/Documents/s6_pro_prompts_20261112_work/returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z_unzipped/S6_10_PAPERS")
PATS = {"poly": re.compile(r"\(S ?- ?1\)\s*\(S ?- ?3\)"), "OS45=25": re.compile(r"OS45[^.]{0,80}?\b25\b"),
        "meridian-one": re.compile(r"(?i)meridian-one")}
SEC = re.compile(re.escape(BS) + r"section\*?\{([^}]{0,70})")
REC = re.compile(re.escape(BS) + r"StatementRecord\{([^}]*)\}\{([^}]*)\}")
for p in ["I", "II", "III", "IV", "V", "VI"]:
    t = (CP / f"S6_10_PAPERS_{p}.tex").read_text(encoding="utf-8")
    secs = [(m.start(), m.group(1)) for m in SEC.finditer(t)]
    recs = [(m.start(), m.group(1), m.group(2)) for m in REC.finditer(t)]
    for name, rx in PATS.items():
        c = collections.Counter()
        for m in rx.finditer(t):
            s = [x[1] for x in secs if x[0] < m.start()]
            r = [x for x in recs if x[0] < m.start()]
            st = r[-1][2] if r else "-"
            c[((s[-1] if s else "front")[:48], st)] += 1
        if c:
            print(p, name, dict(c))
