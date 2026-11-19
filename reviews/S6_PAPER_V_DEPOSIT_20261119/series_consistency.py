"""Series consistency of S6_10_PAPERS at checkpoint 15: which statements each paper takes from the others, whether the
source paper still states them (label, number, status), and whether a later result changes them.
Claude Opus 5.5 at effort max, 19 Nov 2026. usage: python -B series_consistency.py > series_consistency.out"""
import csv, json, pathlib, re, collections
import fitz

csv.field_size_limit(10**9)
BS = chr(92)
CP = pathlib.Path("<local>/Documents/s6_pro_prompts_20261112_work/returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z_unzipped/S6_10_PAPERS")
PAPERS = ["I", "II", "III", "IV", "V", "VI"]
tex = {p: (CP / f"S6_10_PAPERS_{p}.tex").read_text(encoding="utf-8") for p in PAPERS}
defined = {p: set(re.findall(re.escape(BS) + r"label\{([^}]*)\}", tex[p])) for p in PAPERS}
status = {}
for p in PAPERS:
    for m in re.finditer(re.escape(BS) + r"StatementRecord\{([^}]*)\}\{([^}]*)\}", tex[p]):
        status[(p, m.group(1))] = m.group(2)
inv = list(csv.DictReader(open(CP / "S6_10_PAPERS_inventory.csv", encoding="utf-8")))
invrow = {(r["paper"], r["label"]): r for r in inv}

# number -> label in each paper's current PDF ("Theorem 6.2 (title). Label: maps:src:E.1.2.")
KINDS = r"(Theorem|Proposition|Lemma|Corollary|Definition|Remark|Correction|Computation|Open question|Cited result|Statement|Claim|Example|Construction|Conjecture|Counterexample)"
num2lab, lab2num = {}, {}
for p in PAPERS:
    d = fitz.open(CP / f"S6_10_PAPERS_{p}.pdf")
    for i in range(len(d)):
        t = re.sub(r"\s+", " ", d[i].get_text())
        for m in re.finditer(KINDS + r" ([A-Z]?\d*(?:\.\d+)+)(?![0-9])(.{0,400}?)Label: ?(.{1,90}?)\. ?Status:", t):
            lab = m.group(4).replace(" ", "")
            key = (p, m.group(1).lower(), m.group(2))
            num2lab.setdefault(key, (lab, i + 1))
            lab2num.setdefault((p, lab), (m.group(1).lower(), m.group(2), i + 1))

# citations as printed: \ExternalPaperRef{kind~}{num}{Q}
cites = collections.defaultdict(list)
for p in PAPERS:
    for m in re.finditer(re.escape(BS) + r"ExternalPaperRef\{([^}]*)\}\{([^}]*)\}\{([IVX]+)\}", tex[p]):
        kind = m.group(1).replace("~", "").strip().lower()
        kind = {"cited": "cited result", "refuted": "correction"}.get(kind, kind)
        cites[(p, m.group(3))].append((kind, m.group(2)))

# intended labels: references in each paper's own source files to labels defined only in another paper
src_refs = collections.defaultdict(set)
for p in PAPERS:
    for f in (CP / "papers" / p).glob("*.tex"):
        if f.name.endswith(".source.tex"):
            continue
        for m in re.finditer(re.escape(BS) + r"(?:c|C)?ref\{([^}]*)\}", f.read_text(encoding="utf-8", errors="replace")):
            for lab in m.group(1).split(","):
                lab = lab.strip()
                if lab and lab not in defined[p]:
                    owners = [q for q in PAPERS if q != p and lab in defined[q]]
                    if len(owners) == 1:
                        src_refs[(p, owners[0])].add(lab)

out = {"pairs": []}
for p in PAPERS:
    for q in PAPERS:
        if p == q or not (cites.get((p, q)) or src_refs.get((p, q))):
            continue
        printed = cites.get((p, q), [])
        resolved, unresolved = collections.Counter(), []
        for kind, num in printed:
            hit = None
            for k in ([kind] if kind else ["theorem", "proposition", "lemma", "corollary", "definition", "remark", "correction", "computation", "cited result", "open question"]):
                hit = hit or num2lab.get((q, k, num))
            if hit:
                resolved[hit[0]] += 1
            else:
                unresolved.append(f"{kind} {num}".strip())
        intended = sorted(src_refs.get((p, q), set()))
        # labels whose current number is not among the printed numbers (possible drift or untransported reference)
        printed_nums = {num for _, num in printed}
        missing = [lab for lab in intended if lab2num.get((q, lab)) and lab2num[(q, lab)][1] not in printed_nums]
        extra = [lab for lab in resolved if lab not in intended] if intended else []
        stats = collections.Counter(status.get((q, lab), "no record") for lab in set(resolved) | set(intended))
        bad = sorted({lab for lab in set(resolved) | set(intended) if status.get((q, lab), "") not in ("proved", "")})
        out["pairs"].append({"from": p, "to": q, "printed_citations": len(printed), "distinct_resolved_labels": len(resolved),
                             "unresolved_numbers": sorted(set(unresolved)), "source_intended_labels": len(intended),
                             "intended_label_number_not_printed": missing[:20], "resolved_not_in_sources": extra[:20],
                             "status_counts": dict(stats), "non_proved_statements_used": [(lab, status.get((q, lab))) for lab in bad],
                             "labels": sorted(set(resolved) | set(intended))})
for r in out["pairs"]:
    print(f"{r['from']} -> {r['to']}: printed {r['printed_citations']}, resolved labels {r['distinct_resolved_labels']}, "
          f"unresolved {r['unresolved_numbers'][:8]}, source labels {r['source_intended_labels']}, "
          f"source label numbers not printed {r['intended_label_number_not_printed'][:6]}, resolved-not-in-sources {r['resolved_not_in_sources'][:6]}, "
          f"status {r['status_counts']}, non-proved used {r['non_proved_statements_used'][:8]}")
json.dump(out, open(pathlib.Path(__file__).with_suffix(".json"), "w", encoding="utf-8"), indent=1)
print("PDF statement map sizes:", {p: sum(1 for k in num2lab if k[0] == p) for p in PAPERS})
