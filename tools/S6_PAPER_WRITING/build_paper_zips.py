# Builds the two attachment zips of the daytime writing prompt S6_07_PAPER (16 Nov 2026, Claude Fable 5.2 at effort max).
# Zip 1: the returns' relevant sections as LaTeX, with their results tables, reports and bibliographies.
# Zip 2: status and credit input (intakes, debate, review), the workbench's own 2Z proof, the AC26 transcription,
#        the literature for the credit check (LaTeX), and the Hexagon post format.
# Text members are copied with local path prefixes removed; originals are not touched.
import csv, io, os, re, zipfile

DOC = "C:/Users/user/Documents"
WORK = DOC + "/s6_pro_prompts_20261112_work"
RET = WORK + "/returns"
REV = WORK + "/reviews"
OUT = DOC + "/s6_pro_prompts_20261112/07_S6_PAPER_WRITING"
OLDZ = DOC + "/s6_pro_prompts_20261112/ALREADY_RAN"
TEXT_EXT = (".tex", ".md", ".csv", ".bib", ".txt", ".tsv", ".py", ".out", ".json")
NAME = "Flo" + "ris"

def clean(data, name, counts):
    if not name.lower().endswith(TEXT_EXT):
        return data
    t = data.decode("utf-8", "replace")
    n0 = t.count(NAME)
    t = t.replace("C:\\Users\\" + NAME + "\\Documents\\", "").replace("C:/Users/" + NAME + "/Documents/", "")
    t = t.replace("C:\\Users\\" + NAME + "\\", "").replace("C:/Users/" + NAME + "/", "")
    t = t.replace(NAME, "user")
    if n0:
        counts[name] = n0
    return t.encode("utf-8")

def add_file(z, src, arc, why, origin, manifest, counts):
    with open(src, "rb") as f:
        data = f.read()
    z.writestr(arc, clean(data, arc, counts))
    manifest.append((arc, origin, why))

def add_dir(z, folder, arcprefix, why, origin, manifest, counts, keep=lambda n: True):
    n = 0
    for name in sorted(os.listdir(folder)):
        p = folder + "/" + name
        if os.path.isfile(p) and keep(name):
            add_file(z, p, arcprefix + name, why, origin, manifest, counts)
            n += 1
    return n

def close(z, manifest):
    buf = io.StringIO()
    csv.writer(buf, delimiter="\t", lineterminator="\n").writerows(
        [("path_in_zip", "origin", "why_attached")] + manifest + [("MANIFEST.tsv", "this file", "list of contents")])
    z.writestr("MANIFEST.tsv", buf.getvalue())

def first(folder, suffix):
    c = sorted([n for n in os.listdir(folder) if n.endswith(suffix)], key=len)
    return folder + "/" + c[0], c[0]

def main():
    os.makedirs(OUT, exist_ok=True)
    counts = {}
    # ---------------- zip 1: sources ----------------
    m = []
    z1p = OUT + "/S6_07_PAPER_sources.zip"
    with zipfile.ZipFile(z1p, "w", zipfile.ZIP_DEFLATED) as z:
        runs = [
            ("S6_02_FAMILY", RET + "/S6_02_FAMILY_unzipped/S6_02_FAMILY", "sections",
             lambda n: n.endswith(".tex"), "the first run, 12 Nov 2026: family, classification, periods, fibres, monodromy"),
            ("S6_02_PUSH", RET + "/S6_02_PUSH_final_20261115T2217Z_unzipped/S6_02_PUSH", "sections",
             lambda n: n.endswith(".tex") or n.endswith(".bib"), "the push run, final of 15 Nov 2026: the two ends, Theta_7, components"),
            ("S6_05_ARITHMETIC", RET + "/S6_05_ARITHMETIC_final_20261115T1846Z_unzipped/S6_05_ARITHMETIC", "sections",
             lambda n: n.startswith("C_") and n.endswith(".tex"), "Part C of the arithmetic run, final of 15 Nov 2026: the periods and N"),
            ("S6_01_INVARIANTS", RET + "/S6_01_INVARIANTS_unzipped/S6_01_INVARIANTS", "fragments",
             lambda n: n.endswith(".tex"), "the invariants run, 12 Nov 2026: Hodge table, Frolicher, Bott-Chern"),
            ("S6_03_CDP", RET + "/S6_03_CDP_checkpoint_13_20261116T0136Z_unzipped/S6_03_CDP", "sections",
             lambda n: n in ("conventions.tex", "part_C5.tex", "part_E.tex", "part_E_rank.tex"),
             "from the CDP run, checkpoint 13: the twists C5b and the tangent cohomology of the (3k,4l) members only"),
            ("S6_04_MAPS_MANIFOLDS", RET + "/S6_04_MAPS_MANIFOLDS_checkpoint_12_20261116T0243Z_unzipped/S6_04_MAPS_MANIFOLDS", "sections",
             lambda n: n in ("conventions.tex", "real_forms.tex", "maps.tex", "maps_B.tex"),
             "from the maps run, checkpoint 12: real forms (A.3) and the Theta_7 statements (B.6) only"),
        ]
        for run, base, sub, keep, why in runs:
            origin = "return of " + run + " (GPT-6 Astra, ChatGPT Pro mode)"
            n = add_dir(z, base + "/" + sub, "returns/" + run + "/" + sub + "/", why, origin, m, counts, keep)
            extra = 0
            for name in sorted(os.listdir(base)):
                if name.endswith("_results.csv") or name.endswith("_report.md") or name.endswith("_references.bib") \
                        or (run == "S6_05_ARITHMETIC" and (name.startswith("results_C") or name.startswith("references_C"))):
                    add_file(z, base + "/" + name, "returns/" + run + "/" + name, "results table, report or bibliography of the run", origin, m, counts)
                    extra += 1
            print(run, "section files:", n, "top-level files:", extra)
        close(z, m)
    # ---------------- zip 2: status, credit, format ----------------
    m = []
    z2p = OUT + "/S6_07_PAPER_status_credit_format.zip"
    with zipfile.ZipFile(z2p, "w", zipfile.ZIP_DEFLATED) as z:
        fin = REV + "/S6_FINAL_INTAKE_20261116"
        for name, why in [("INTAKE_FINAL.md", "who read what in the four finals; the cross-run findings; corrections"),
                          ("INTAKE_S6_01.md", "the intake of the invariants run; the proposal for section 5"),
                          ("RESPONSE_INTAKE.md", "the section-by-section status table (binding with the prompt's table)"),
                          ("RESPONSE_EXPERT.md", "the credit table against arXiv:2610.00250, [AC26], [E26]")]:
            add_file(z, fin + "/" + name, "status/" + name, why, "Claude Fable 5.2 (effort high: intake; effort max: expert), 16 Nov 2026", m, counts)
        add_file(z, REV + "/S6_02_REVIEW_FABLE/REVIEW.md", "status/REVIEW_S6_02_FAMILY.md",
                 "the review of the first run: verdict per statement, label corrections (section 5), credits (section 6)",
                 "Claude Fable 5.2 at effort high, 12 Nov 2026", m, counts)
        p5 = REV + "/S6_INTAKE_CHECKPOINTS_20261115/INTAKE_S6_05_FINAL.md"
        if os.path.exists(p5):
            add_file(z, p5, "status/INTAKE_S6_05_FINAL.md", "the intake of the arithmetic run's final", "Claude Fable 5.2 at effort high, 15 Nov 2026", m, counts)
        add_file(z, DOC + "/math/research/s6_recent_results_main/canonical_S6_snapshot/supporting_materials/workbench/research/period_shift_classification.tex",
                 "workbench/period_shift_classification.tex", "the workbench's own proof of the 2Z classification, for Appendix A",
                 "the September 2026 workbench (GPT-5.6 Sol and GPT-6 Astra in Codex at reasoning effort ultra)", m, counts)
        add_file(z, DOC + "/math/research/s6_recent_results_main/canonical_S6_snapshot/original_clean_transcription.tex",
                 "original/AC26_transcription.tex", "[AC26] in an AI transcription: for the credit check only; the paper cites [AC26] and reproduces none of its text",
                 "AI transcription of https://alpo.ge/s6.pdf", m, counts)
        with zipfile.ZipFile(OLDZ + "/S6_03_CDP/S6_03_CDP_background.zip") as zin:
            for name in zin.namelist():
                if name.endswith("/"):
                    continue
                if name.startswith(("papers/arXiv_2609.38442_Engel_src/", "papers/arXiv_2610.00250v1", "papers/arXiv_2610.00250v2",
                                    "papers/arXiv_2610.39102_Viaclovsky", "papers/arXiv_2609.33785_Viaclovsky",
                                    "papers/arXiv_2610.10451_Viaclovsky", "papers/arXiv_2609.33826_Liu_Rollenske")):
                    z.writestr(name, clean(zin.read(name), name, counts))
                    m.append((name, "arXiv e-print (LaTeX source), as in the earlier S6 zips", "literature for the credit check and the citations"))
        with zipfile.ZipFile(OLDZ + "/S6_05_ARITHMETIC/S6_05_ARITHMETIC_background.zip") as zin:
            for name in zin.namelist():
                if "Duke_Imamoglu" in name:
                    z.writestr(name, zin.read(name))
                    m.append((name, "journal paper, PDF (no LaTeX source exists)", "states the Eichler-Zagier formula for the zero of the Weierstrass function"))
        hx = DOC + "/recent_results_20261114"
        for name, why in [("HEXAGON_POST_FORMAT_20261114.md", "the format the paper must follow (binding)"),
                          ("hexagon_post_template.tex", "the LaTeX template of the format"),
                          ("hexagon_post_example_Q03.tex", "a worked example of the format")]:
            add_file(z, hx + "/" + name, "format/" + name, why, "the project's post format, version 1, 14 Nov 2026", m, counts)
        close(z, m)
    for p in (z1p, z2p):
        with zipfile.ZipFile(p) as z:
            names = z.namelist()
            left = [n for n in names if n.lower().endswith(TEXT_EXT) and NAME in z.read(n).decode("utf-8", "replace")]
            pdfs = [n for n in names if n.lower().endswith(".pdf")]
            print(os.path.basename(p), len(names), "members,", os.path.getsize(p), "bytes; PDFs:", pdfs, "; name left in:", left)
    print("members in which the local name was replaced:", counts)

if __name__ == "__main__":
    main()
