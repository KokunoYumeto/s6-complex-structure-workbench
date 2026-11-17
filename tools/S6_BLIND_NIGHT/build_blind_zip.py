# Builds the attachment zip of the blind night prompt S6_06_BLIND (16 Nov 2026, Claude Fable 5.2 at effort max).
# It carries data and statements only: the construction papers (LaTeX; the AC26 manuscript also as PDF, since it has
# no source), the matrices of the fourfold, and the earlier runs' stated values as CSV rows (id, statement, status).
# No proof text of the earlier runs, no review, no workbench, no arXiv:2610.00250 (Part 5 is a blind control).
import csv, io, os, sys, zipfile, hashlib

DOC = r"C:/Users/user/Documents"
WORK = DOC + "/s6_pro_prompts_20261112_work"
OUTDIR = DOC + "/s6_pro_prompts_20261112/06_S6_BLIND_NIGHT"
HERE = WORK + "/S6_BLIND_NIGHT"
SRCZIP = DOC + "/s6_pro_prompts_20261112/ALREADY_RAN/S6_04_MAPS_MANIFOLDS/S6_04_MAPS_MANIFOLDS_background.zip"
RET = WORK + "/returns"

KEEP_PREFIXES = [
    ("original/AC26_original_manuscript.pdf", "[AC26], the original manuscript (PDF; it has no LaTeX source): the authority"),
    ("original/AC26_transcription.tex", "[AC26], LaTeX transcription made by AI from the PDF"),
    ("papers/arXiv_2609.38442_Engel_src/", "[E26] Engel, Complex structures on S6, arXiv:2609.38442, LaTeX source"),
    ("papers/arXiv_2610.39102_Viaclovsky_log_transformations_src/", "Viaclovsky, arXiv:2610.39102 (orders 3k, 4l), LaTeX source"),
    ("papers/arXiv_2609.33785_Viaclovsky_two_parameter_src/", "Viaclovsky, arXiv:2609.33785 (two-parameter family), LaTeX source"),
    ("papers/arXiv_2610.10451_Viaclovsky_combs_src/", "Viaclovsky, arXiv:2610.10451 (combs), LaTeX source"),
    ("papers/arXiv_2609.33826_Liu_Rollenske_src/", "Liu and Rollenske, arXiv:2609.33826, LaTeX source"),
    ("papers/arXiv_2609.29666_Yang_src/", "Yang, arXiv:2609.29666, LaTeX source"),
    ("papers/arXiv_2609.11541_Wang_src/", "Wang, arXiv:2609.11541, LaTeX source"),
]

# rows of the earlier runs' results tables that are passed on as stated values (id, statement, status only)
STATED = [
    ("S6_04", RET + "/S6_04_MAPS_MANIFOLDS_checkpoint_12_20261116T0243Z_unzipped/S6_04_MAPS_MANIFOLDS/S6_04_MAPS_MANIFOLDS_results.csv",
     lambda i: i.startswith("D.2.") or i.startswith("B.6.") or i.startswith("F.1.") or i.startswith("F.2.")
               or i.startswith("F.3.") or i.startswith("F.4.") or i in ("E.1.3",)),
    ("S6_02_PUSH", None,
     lambda i: i in ("B.1.1", "B.1.2", "B.4.9", "B.4.18", "B.4.19", "B.4.24", "B.4.26", "B.4.27", "B.4.30", "B.4.31",
                     "B.4.32", "B.4.33", "A.3.1", "A.3.2") or i.startswith("C.3.") or i.startswith("C.4.")),
    ("S6_03", RET + "/S6_03_CDP_checkpoint_13_20261116T0136Z_unzipped/S6_03_CDP/S6_03_CDP_results.csv",
     lambda i: i in ("D.2.5", "D.2.7", "C.2.G.1") or i.startswith("C.2.NC")),
]

def find_csv(folder, suffix="_results.csv"):
    names = [n for n in os.listdir(folder) if n.endswith(suffix)]
    names.sort(key=len)
    return folder + "/" + names[0]

def main():
    os.makedirs(OUTDIR, exist_ok=True)
    os.makedirs(HERE + "/data", exist_ok=True)
    push_dir = RET + "/S6_02_PUSH_final_20261115T2217Z_unzipped/S6_02_PUSH"
    rows_out = [("run", "id", "statement", "status")]
    for run, path, pred in STATED:
        if path is None:
            path = find_csv(push_dir)
        with open(path, encoding="utf-8", errors="replace", newline="") as f:
            rd = list(csv.reader(f))
        n = 0
        for r in rd[1:]:
            text = (" ".join(r[:3])).lower()
            # Part 5 is a blind control: no row may state the tangent cohomology or the automorphism group
            if any(k in text for k in ("(1,1,1,0)", "aut(", "aut =", "automorphism", "tangent cohomology",
                                       "kuranishi", "00250", "h^q(t")):
                continue
            if r and pred(r[0].strip()):
                rows_out.append((run, r[0].strip(), r[1].strip() if len(r) > 1 else "", r[2].strip() if len(r) > 2 else ""))
                n += 1
        print(run, "rows passed on:", n, "from", os.path.basename(path))
    buf = io.StringIO()
    csv.writer(buf, lineterminator="\n").writerows(rows_out)
    with open(HERE + "/data/stated_values.csv", "w", encoding="utf-8", newline="") as f:
        f.write(buf.getvalue())

    manifest = [("path_in_zip", "origin", "why_attached")]
    zout_path = OUTDIR + "/S6_06_BLIND_background.zip"
    with zipfile.ZipFile(SRCZIP) as zin, zipfile.ZipFile(zout_path, "w", zipfile.ZIP_DEFLATED) as zout:
        for name in zin.namelist():
            if name.endswith("/"):
                continue
            for pre, why in KEEP_PREFIXES:
                if name == pre or (pre.endswith("/") and name.startswith(pre)):
                    zout.writestr(name, zin.read(name))
                    manifest.append((name, "S6_04_MAPS_MANIFOLDS_background.zip (same file)", why))
                    break
        for fn, why in [("fourfold_tuple.py", "Part 1: the matrices A, B, the twists and the companion matrices, as data"),
                        ("stated_values.csv", "the earlier runs' stated values: run, id, statement, status; no proofs")]:
            p = HERE + "/data/" + fn
            if os.path.exists(p):
                zout.write(p, "data/" + fn)
                manifest.append(("data/" + fn, "written for this prompt, 16 Nov 2026", why))
            else:
                print("MISSING data file:", fn)
        mbuf = io.StringIO()
        csv.writer(mbuf, delimiter="\t", lineterminator="\n").writerows(manifest + [("MANIFEST.tsv", "this file", "list of contents")])
        zout.writestr("MANIFEST.tsv", mbuf.getvalue())
    with zipfile.ZipFile(zout_path) as z:
        names = z.namelist()
        bad = [n for n in names if "00250" in n or "return" in n or "review" in n or "workbench" in n or n.lower().endswith(".pdf") and "AC26" not in n]
        print("zip:", zout_path, len(names), "members,", os.path.getsize(zout_path), "bytes; forbidden members:", bad)
        for n in names:
            print("   ", n, z.getinfo(n).file_size)

if __name__ == "__main__":
    main()
