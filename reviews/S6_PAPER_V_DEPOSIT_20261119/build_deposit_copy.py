"""Paper V deposit copy: rebuild every check record with its public record, link the cross-paper references.
Claude Opus 5.5 at effort max, 19 Nov 2026 (S6 Paper V deposit preparation). The mathematics is not touched: only the
third argument of each \\StatementRecord (the check record), the macros \\ExternalPaperRef and \\CompendiumRef, the
record macro's layout, and one provenance paragraph after the abstract change.
usage: python -B build_deposit_copy.py
Reads the S6_10_PAPERS checkpoint 15 return (local copy, identical to the public one) and the public clone of
s6-complex-structure-workbench; writes S6_10_PAPERS_V_deposit.tex, records.tsv and links.json beside this script."""
import csv, json, pathlib, re, sys
import fitz  # PyMuPDF

csv.field_size_limit(10**9)
BS = chr(92)
HERE = pathlib.Path(__file__).resolve().parent
DOC = pathlib.Path("<local>/Documents")
CP = DOC / "s6_pro_prompts_20261112_work/returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z_unzipped/S6_10_PAPERS"
PUB = DOC / "github_backup_20261113/s6-complex-structure-workbench"
SHA = "4e8b547874c2acff6b49713ca96f84b281ab5793"          # s6-complex-structure-workbench, pinned
ASHA = "96b2bcaec355870a8faa9457406673b7cd897654"         # grothendieck-montpellier-archive, pinned
G = f"https://github.com/KokunoYumeto/s6-complex-structure-workbench/blob/{SHA}/"
GRAW = f"https://github.com/KokunoYumeto/s6-complex-structure-workbench/raw/{SHA}/"
GA = f"https://github.com/KokunoYumeto/grothendieck-montpellier-archive/blob/{ASHA}/"
P15 = "pro_returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z/S6_10_PAPERS/"
P09 = "pro_returns/S6_09_PAPERS_final_20261117T0601Z/"
N35 = "pro_returns/S6_06_BLIND_checkpoint_35_20261118T1208Z/S6_06_BLIND/"

tex = (CP / "S6_10_PAPERS_V.tex").read_text(encoding="utf-8")
events = list(csv.DictReader(open(CP / "CHECK_EVENTS.tsv", encoding="utf-8"), delimiter="\t"))
inv = {r["label"]: r for r in csv.DictReader(open(CP / "S6_10_PAPERS_inventory.csv", encoding="utf-8")) if r["paper"] == "V"}
aux09 = (PUB / P09 / "S6_09_PAPERS_III.aux").read_text(encoding="utf-8", errors="replace")
intake06 = list(csv.DictReader(open(PUB / "raw/intake/S6_10_INTAKE_CHECK_EVENTS.tsv", encoding="utf-8"), delimiter="\t"))

# ---------- helpers
def tex_escape(s):
    s = s.replace("\\", "\u0000")
    for a, b in [("{", "\\{"), ("}", "\\}"), ("$", "\\$"), ("&", "\\&"), ("#", "\\#"), ("%", "\\%"), ("_", "\\_"),
                 ("^", "\\^{}"), ("~", "\\~{}"), ("<", "\\textless{}"), (">", "\\textgreater{}"), ("|", "\\textbar{}")]:
        s = s.replace(a, b)
    s = s.replace("\u0000", "\\textbackslash{}")
    for a, b in [("\u2212", "-"), ("\u00d7", "x"), ("\u2264", "<="), ("\u2265", ">="), ("\u2192", "->"), ("\u2013", "--"),
                 ("\u2014", "---"), ("\u2018", "`"), ("\u2019", "'"), ("\u201c", "``"), ("\u201d", "''"), ("\u2026", "...")]:
        s = s.replace(a, b)
    return "".join(ch if ord(ch) < 0x2000 else "?" for ch in s)

def first_sentences(s, limit=230):
    s = re.sub(r"\s+", " ", s).strip()
    if len(s) <= limit:
        return s
    cut = s[:limit]
    k = max(cut.rfind(". "), cut.rfind("; "))
    return (cut[:k + 1] if k > 80 else cut.rsplit(" ", 1)[0] + " ...").strip()

def link(url, text):
    return BS + "href{" + url.replace("%", BS + "%").replace("#", BS + "#") + "}{" + text + "}"

def args(t, i, n):
    """positions of n balanced-brace arguments starting at t[i] == '{'"""
    out = []
    for _ in range(n):
        assert t[i] == "{", t[i:i + 40]
        depth, j = 0, i
        while True:
            c = t[j]
            if c == BS:
                j += 2; continue
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        out.append((i + 1, j))
        i = j + 1
    return out, i

# ---------- public locators
aux = {}
for m in re.finditer(r"\\newlabel\{([^}]*)\}\{\{([^}]*)\}\{([^}]*)\}", aux09):
    aux.setdefault(m.group(1), (m.group(2), m.group(3)))
night_doc = fitz.open(PUB / N35 / "S6_06_BLIND_paper.pdf")
night_text = [night_doc[i].get_text() for i in range(len(night_doc))]
def night_page(sid):
    rx = re.compile(r"Statement\s+" + re.escape(sid) + r"\s+\(")
    for i, t in enumerate(night_text):
        if rx.search(t):
            return i + 1
    return None

def who_of(w):
    if "S6_10_PAPERS continuation" in w:
        return "GPT-6 Astra (ChatGPT Pro mode), run S6\\_10\\_PAPERS (continuation)", "S10"
    if "S6_10_PAPERS" in w:
        return "GPT-6 Astra (ChatGPT Pro mode), run S6\\_10\\_PAPERS", "S10"
    if "S6_09_PAPERS" in w:
        return "GPT-6 Astra (ChatGPT Pro mode), run S6\\_09\\_PAPERS", "S09"
    if "S6_06_BLIND" in w:
        return "GPT-6 Astra (ChatGPT Pro mode), run S6\\_06\\_BLIND (the producing run)", "NIGHT"
    m = re.search(r"Claude (Fable 5\.2|Opus 5\.5) \(Anthropic\),? effort (high|max)", w)
    if m:
        extra = " (sweep 1 of the S6 register)" if "sweep 1" in w else ""
        return f"Claude {m.group(1)} at effort {m.group(2)}{extra}", "CL"
    return tex_escape(w), "OTHER"

BOOK = re.compile(r"^(Administrative status reconciliation|Metadata-only|Full current proof/computation gate|Current full-row proof/computation gate|complete:)")
CREDIT = re.compile(r"^(Renewed bounded primary-source credit check|Supporting-row source/credit check)")
TYPES = {"targeted proof check": "Targeted proof check", "independent re-proof": "Independent re-proof",
         "computation or formal certificate": "Computation", "carried as background without fault found":
         "Carried as background, no fault found (not a proof check)", "used and rechecked in this run": "Used and rechecked"}

local_files = {p.relative_to(CP).as_posix() for p in CP.rglob("*") if p.is_file()}
public_large = (PUB / "pro_returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z/LARGE_FILES.md").read_text(encoding="utf-8")

def record_of(e, label):
    who, key = who_of(e["who"])
    typ = e["type"]
    out = e["outcome"]
    if typ == "used and rechecked in this run":
        if BOOK.search(out):
            return None
        kind = "Source and credit check" if CREDIT.search(out) else TYPES[typ]
    else:
        kind = TYPES.get(typ, tex_escape(typ))
    date = e["date"][:10]
    what, where = "", []
    if key == "S10":
        txt = re.sub(r"^(proved|pass|PASS)\s+", "", out)
        what = first_sentences(txt)
        where.append(link(G + P15 + "CHECK_EVENTS.tsv", "CHECK\\_EVENTS.tsv") + ", event " + tex_escape(e["event_id"]))
        for ev_path in dict.fromkeys(re.findall(r"\b((?:analysis|code|records)/[A-Za-z0-9_./-]+[A-Za-z0-9_])", out)):
            if ev_path in local_files and ev_path not in public_large:
                where.append(link(G + P15 + ev_path, tex_escape(ev_path.split("/")[-1])))
                break
    elif key == "S09":
        what = "complete proof read and re-derived in the writing run S6\\_09\\_PAPERS"
        lab09 = inv.get(label, {}).get("s6_09_label") or label
        loc = aux.get(lab09)
        w = link(G + P09 + "S6_09_PAPERS_inventory.csv", "S6\\_09 inventory") + ", row " + BS + "nolinkurl{" + lab09 + "}"
        if loc:
            w += "; the statement is " + link(GRAW + P09 + "S6_09_PAPERS_III.pdf#page=" + loc[1], f"S6\\_09 Paper III, {loc[0]}, p.~{loc[1]}")
        where.append(w)
        return kind, who, date, what, where, key
    elif key == "NIGHT":
        sid = inv.get(label, {}).get("source_id") or label.split(":")[-1]
        what = "re-derivation recorded by the producing run (register status: " + ("Proved" if "Proved" in out else "as in its register") + ")"
        pg = night_page(sid)
        w = link(G + N35 + "S6_06_BLIND_results.csv", "S6\\_06\\_BLIND register") + ", row " + tex_escape(sid)
        if pg:
            w += "; the statement is " + link(GRAW + N35 + "S6_06_BLIND_paper.pdf#page=" + str(pg), f"S6\\_06\\_BLIND paper (checkpoint 35), p.~{pg}")
        where.append(w)
        return kind, who, date, what, where, key
    elif key == "CL":
        txt = re.sub(r"^Received historical check:\s*", "", out)
        txt = re.sub(r"^Claude (Fable|Opus)[^:]*?\d{4}(-\d\d-\d\d)?[^:]*:\s*", "", txt)
        txt = re.sub(r"^Recorded result-register intake:\s*Claude[^;]*;\s*", "Register intake; ", txt)
        txt = re.sub(r"^Historical document record:\s*", "", txt)
        m = re.search(r"(?:sources/)?(reviews/[A-Za-z0-9_./-]+\.md)(?::\s*([^\]\n;.]{0,80}))?", out)
        what = first_sentences(re.sub(r"\[?(?:sources/)?reviews/[^\]]*\]?", "", txt))
        if m and (PUB / m.group(1)).exists():
            loc = (", " + tex_escape(m.group(2).strip())) if m.group(2) and m.group(2).strip() else ""
            where.append(link(G + m.group(1), tex_escape(m.group(1).split("/")[-1])) + loc)
        elif "sweep 1" in e["who"]:
            rs = re.search(r"Read scope:\s*([^.]{0,90})", out)
            where.append(link(GA + "raw/results_register/sweep1_s6/CHECK_EVENTS.tsv", "sweep 1 CHECK\\_EVENTS.tsv")
                         + (", " + tex_escape(rs.group(1).strip()) if rs else ""))
        else:
            where.append(link(G + P15 + "CHECK_EVENTS.tsv", "CHECK\\_EVENTS.tsv") + ", event " + tex_escape(e["event_id"]))
    else:
        what = first_sentences(out)
        where.append(link(G + P15 + "CHECK_EVENTS.tsv", "CHECK\\_EVENTS.tsv") + ", event " + tex_escape(e["event_id"]))
    return kind, who, date, tex_escape(what) if key != "S09" else what, where, key

ORDER = {"Targeted proof check": 0, "Independent re-proof": 1, "Computation": 2, "Source and credit check": 3,
         "Used and rechecked": 4, "Carried as background, no fault found (not a proof check)": 5}
by = {}
for e in events:
    by.setdefault(e["statement_id"], []).append(e)

EXTRA = {}
for e in intake06:
    sid = e["statement_id"]
    if sid in ("night:P1A.2", "night:P1A.3"):
        EXTRA.setdefault(sid, []).append(("Computation", "Claude Opus 5.5 at effort max (intake of S6\\_10\\_PAPERS checkpoint 06)",
            e["date"][:10], tex_escape(first_sentences(e["outcome"])),
            [link(G + "raw/intake/S6_10_INTAKE_20261118.md", "S6\\_10\\_INTAKE\\_20261118.md") + "; "
             + link(G + "raw/intake/S6_10_INTAKE_CHECK_EVENTS.tsv", "its CHECK\\_EVENTS.tsv") + ", row " + BS + "nolinkurl{" + sid + "}"], "CL"))
p16, p114 = night_page("P1.6"), night_page("P1.14")
EXTRA.setdefault("maps:src:F.4.1", []).append(("Independent re-proof", "GPT-6 Astra (ChatGPT Pro mode), run S6\\_06\\_BLIND", "2026-11-16 to 18",
    "another run derived the conclusion itself: statement P1.14 (the constructed fourfold is orientation-preservingly diffeomorphic to "
    "$3\\mathbb{HP}^2\\#(-\\mathbb{HP}^2)$, by Wall's extended-form classification) and statement P1.6 (connected sum with any homotopy "
    "eight-sphere is absorbed, by Kramer--Stolz, Theorem A); a re-proof of the conclusion, not a reading of the printed proof",
    [link(G + N35 + "S6_06_BLIND_results.csv", "S6\\_06\\_BLIND register") + ", rows P1.6 and P1.14; statements "
     + link(GRAW + N35 + f"S6_06_BLIND_paper.pdf#page={p16}", f"p.~{p16}") + " and "
     + link(GRAW + N35 + f"S6_06_BLIND_paper.pdf#page={p114}", f"p.~{p114}") + " of the S6\\_06\\_BLIND paper (checkpoint 35)"], "NIGHT"))

def build_record(label):
    rows = []
    for e in by.get(label, []):
        r = record_of(e, label)
        if r:
            rows.append(r)
    rows += EXTRA.get(label, [])
    groups = {}
    for kind, who, date, what, where, key in rows:
        k = (kind, who, date)
        g = groups.setdefault(k, {"what": what, "where": [], "n": 0})
        g["n"] += 1
        for w in where:
            if w not in g["where"]:
                g["where"].append(w)
    lines = []
    for (kind, who, date), g in sorted(groups.items(), key=lambda kv: (ORDER.get(kv[0][0], 9), kv[0][2], kv[0][1])):
        more = f" ({g['n']} recorded events)" if g["n"] > 1 else ""
        wh = g["where"][:3]
        if len(g["where"]) > 3:
            wh.append(f"and {len(g['where']) - 3} further events in the same file")
        lines.append(BS + "CheckLine{" + kind + "}{" + who + ", " + date + more + "}{" + g["what"].rstrip(".") + ".}{" + "; ".join(wh) + "}")
    return lines

# ---------- rewrite the records
out, i, stats = [], 0, []
SR = BS + "StatementRecord"
for m in re.finditer(re.escape(SR) + r"\{", tex):
    if m.start() < tex.find(BS + "begin{document}"):
        continue
    (a1, a2, a3, a4), end = args(tex, m.end() - 1, 4)
    label = tex[a1[0]:a1[1]]
    lines = build_record(label)
    out.append(tex[i:a3[0]])
    out.append("%\n" + "\n".join(lines) + "%\n")
    i = a3[1]
    kinds = sorted({re.match(r"\\CheckLine\{([^}]*)\}", l).group(1) for l in lines})
    stats.append((label, len(lines), "; ".join(kinds)))
out.append(tex[i:])
new = "".join(out)

# ---------- cross-paper references, pinned to the public PDFs of checkpoint 15
docs = {}
def page_of(paper, kind, num):
    if paper not in docs:
        d = fitz.open(CP / f"S6_10_PAPERS_{paper}.pdf")
        docs[paper] = [d[k].get_text() for k in range(len(d))]
    head = re.compile(r"(?m)^\s*" + re.escape(kind) + r"\s+" + re.escape(num) + r"(?![0-9])")
    for k, t in enumerate(docs[paper]):
        if head.search(t):
            return k + 1
    return None
links = {}
def ext_sub(m):
    a, b, c = m.group(1), m.group(2), m.group(3)
    kind = a.replace("~", "").strip().capitalize()
    kinds = [kind] if kind else ["Theorem", "Proposition", "Lemma", "Corollary"]
    pg = None
    for kd in kinds:
        pg = pg or page_of(c, kd, b)
    links[f"{a}{b} (Paper {c})"] = pg
    if pg is None:
        return m.group(0)
    return BS + "ExternalPaperRefAt{" + a + "}{" + b + "}{" + c + "}{" + str(pg) + "}"
new = re.sub(re.escape(BS) + r"ExternalPaperRef\{([^}]*)\}\{([^}]*)\}\{([IVX]+)\}", ext_sub, new)
def comp_sub(m):
    p, lab = m.group(1), m.group(2)
    loc = aux.get(lab) if p == "III" else None
    links[f"S6_09 Paper {p}, {lab}"] = loc
    if not loc:
        return m.group(0)
    return BS + "CompendiumRefAt{" + p + "}{" + lab + "}{" + loc[0] + "}{" + loc[1] + "}"
new = re.sub(re.escape(BS) + r"CompendiumRef\{([IVX]+)\}\{([^}]*)\}", comp_sub, new)

# ---------- macros and provenance
old_macro = new[new.find(BS + "newcommand{" + BS + "StatementRecord}"):]
old_macro = old_macro[:old_macro.find("\n")]
new_macro = (BS + "newcommand{" + BS + "StatementRecord}[4]{\\par\\smallskip\\begingroup\\upshape\\raggedright\\noindent\\textbf{Label:} "
             "\\nolinkurl{#1}.\\par\\noindent\\textbf{Status:} #2.\\par\\noindent\\textbf{Checks}, each with its public record:\\par"
             "{\\small #3}\\par\\noindent\\textbf{Uses:} #4.\\par\\endgroup\\smallskip}\n"
             "\\newcommand{\\CheckLine}[4]{\\par\\noindent\\hangindent=1.5em\\hangafter=1\\textbullet\\ \\emph{#1.} #2: #3 Record: #4.\\par}")
new = new.replace(old_macro, new_macro, 1)
P = GRAW + P15
ext_def = (BS + "newcommand{" + BS + "ExternalPaperRefAt}[4]{\\ifmmode\\text{\\upshape\\href{" + P.replace("%", "\\%")
           + "S6_10_PAPERS_#3.pdf\\##4}{#1#2 (Paper~#3, p.~#4)}}\\else\\href{" + P + "S6_10_PAPERS_#3.pdf\\##4}{#1#2 (Paper~#3, p.~#4)}\\fi}\n"
           + BS + "newcommand{" + BS + "CompendiumRefAt}[4]{\\ifmmode\\text{\\upshape\\href{" + GRAW + P09 + "S6_09_PAPERS_#1.pdf\\##4}{S6\\_09, Paper~#1, #3, p.~#4}}"
           "\\else\\href{" + GRAW + P09 + "S6_09_PAPERS_#1.pdf\\##4}{S6\\_09, Paper~#1, #3, p.~#4}\\fi}\n")
anchor = BS + "newcommand{" + BS + "ExternalPaperRef}"
assert anchor in new
new = new.replace(anchor, ext_def + anchor, 1)
prov = ("\n\\paragraph{This version.} Paper~V of the series S6\\_10\\_PAPERS as of its checkpoint~15 (19~November~2026, 10:45~UTC; "
        "GPT-6 Astra (ChatGPT Pro mode)), prepared for deposit by Claude Opus~5.5 at effort max on 19~November~2026. "
        "The mathematics is unchanged. Each statement's check record now names every recorded check (who, with model and effort; "
        "the date; what was done) with a link to its public record; bookkeeping entries of the writing run that are not checks "
        "are left out. References to Papers~I, III and~VI and to the S6\\_09 compendium link to the public PDFs at checkpoint~15, "
        "with the page. Links are pinned to commit \\texttt{" + SHA[:12] + "} of the repository \\texttt{s6-complex-structure-workbench}.\n")
k = new.find(BS + "end{abstract}")
assert k > 0
k = new.find("\n", k) + 1
new = new[:k] + prov + new[k:]
(HERE / "S6_10_PAPERS_V_deposit.tex").write_text(new, encoding="utf-8")
with open(HERE / "records.tsv", "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, delimiter="\t"); w.writerow(["label", "check_lines", "kinds"]); w.writerows(stats)
(HERE / "links.json").write_text(json.dumps(links, indent=1), encoding="utf-8")
print("records rebuilt:", len(stats), "| check lines:", sum(s[1] for s in stats), "| statements without a proof check:",
      [s[0] for s in stats if not re.search("Targeted proof check|Independent re-proof|Computation", s[2])])
print("cross-references:", links)
