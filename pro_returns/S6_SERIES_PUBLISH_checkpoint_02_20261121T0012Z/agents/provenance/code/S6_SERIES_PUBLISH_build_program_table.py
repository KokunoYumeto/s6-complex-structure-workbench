#!/usr/bin/env python3
"""Propose Paper V's program table and guarded citation-only edits.

The cited files are historical, verified public programs.  This script neither
publishes current work at the old commit nor awards mathematical check events.
"""
from pathlib import Path
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT.parents[2]
COMMIT = "83d76022bcd442278b760db9ff438afceed6c6ea"
CP10 = "pro_returns/S6_SERIES_GRIND_checkpoint_10_20261120T0211Z"

# Every filename appears once.  A row groups related implementations; its
# statement references identify the exact mathematical scope in the paper.
GROUPS = [
    ("height", "Endpoint and global height enclosures", ["night:P1.18"],
     ["fresh_frobenius.py", "fresh_local_domains.py", "fresh_global_cover.py", "verify_saved_certificate.py"]),
    ("resolved", "Cohomology of the resolved fourfold", ["maps:src:E.1.4", "maps:src:E.1.5"],
     ["fourfolds_checks.py", "fourfolds_integral_audit.py"]),
    ("second-pair", "Integral calculation for the second rational pair", ["maps:src:F.2.18"],
     ["fourfolds_v1_homology.py"]),
    ("normal-forms", "Relative rational normal forms", ["maps:src:F.2.20", "maps:src:F.2.26"],
     ["fourfolds_relative_normalform.py", "fourfolds_relative_six_probe.py"]),
    ("lattices", "Stable lattices and primitive extensions", ["maps:src:F.2.22", "maps:src:F.2.23"],
     ["fourfolds_lattice_algorithm.py", "fourfolds_two_classes_lattices.py"]),
    ("twists", "Affine twists of the two rational classes", ["maps:src:F.2.24"],
     ["fourfolds_family_twists.py"]),
    ("suspension", "Finite spectral suspension calculation", ["maps:src:F.2.25"],
     ["fourfolds_suspension_filter.py"]),
    ("middle-pairing", "Order-six middle-pairing obstruction", ["maps:src:F.2.27"],
     ["fourfolds_universal_56_obstruction.py"]),
    ("cap-tests", "Finite-cap and cusp tests for third and fifth cohomology", ["maps:src:F.2.29"],
     ["fourfolds_local_caps.py", "fourfolds_cusp_boundary.py", "fourfolds_survivor_test.py"]),
    ("fundamental-group", "Marked fundamental-group presentation", ["maps:src:F.2.31"],
     ["fourfolds_vankampen.py"]),
    ("three-points", "Three-finite-point family examples", ["maps:src:F.2.32"],
     ["fourfolds_three_point_family.py"]),
    ("chains", "Finite cap, complement and gluing chains", ["maps:src:F.2.33", "maps:src:F.2.34", "maps:src:F.2.35"],
     ["fourfolds_bar_koszul.py", "fourfolds_affine_cap_chains.py", "fourfolds_kuhn_cap_chains.py",
      "fourfolds_global_chains.py", "fourfolds_total_homology.py", "fourfolds_marked_gluing.py"]),
    ("periods", "Algebra of the period construction", ["maps:src:F.3.5"],
     ["fourfolds_periods.py"]),
    ("tubes", "Spanning tube directions", ["maps:src:F.3.8"],
     ["fourfolds_oka_tubes.py"]),
    ("shifted-homology", "Integral homology of shifted products", ["maps:src:E.2.5", "maps:src:E.2.6"],
     ["fourfolds_shifted_integral.py", "manifolds_shifted_mv.py"]),
    ("equivariant", "Bordism and low-degree boundary calculations", ["maps:src:E.2.9", "maps:src:E.2.11", "maps:src:E.2.12"],
     ["shifted_group_bordism.py", "maps_shifted_pi2.py", "manifolds_cusp_alexander.py"]),
    ("cyclic-cover", "Circle fibration, cyclic cover and integral fibre", ["maps:src:E.2.13", "maps:src:E.2.14", "maps:src:E.2.15"],
     ["maps_shifted_circle.py", "maps_shifted_return.py", "maps_shifted_cover.py",
      "maps_shifted_cover_integral.py", "maps_shifted_fibre_integral.py"]),
    ("quadratic", "Complement and splice modules and their quadratic maps", ["maps:src:E.2.16", "maps:src:E.2.17", "maps:src:E.2.18"],
     ["maps_complement_module.py", "maps_splice_module.py", "maps_cusp_quadratic.py", "maps_splice_quadratic.py"]),
    ("framings", "Plumbing, finite-cap framings and handle inventory", ["maps:src:E.2.19", "maps:src:E.2.20", "maps:src:E.2.21"],
     ["maps_cusp_smooth_plumbing.py", "maps_finite_cap_framings.py", "maps_ordinary_handles.py"]),
]


def main():
    current = BASE / "work/S6_SERIES_PUBLISH_V.tex"
    text = current.read_text()
    rows = json.loads((ROOT / "S6_SERIES_PUBLISH_V_program_path_receipt.json").read_text())
    paths = {row["filename"]: row for row in rows}
    analytic = json.loads((BASE / "work/agents/v_analytic/S6_SERIES_PUBLISH_V_pinned_program_receipt.json").read_text())
    for row in analytic:
        name = row["path"].split("/")[-1]
        if name.startswith("fresh_") or name == "verify_saved_certificate.py":
            assert row["remote_matches_attached"] and row["manifest_matches_attached"]
            assert row["commit"] == COMMIT and row["http_status"] == 200
            paths[name] = {"filename": name, "statement_ids": row["statement_ids"].split(", "),
                           "commit": COMMIT, "path": f"{CP10}/{row['path']}",
                           "bytes": row["remote_bytes"], "sha256": row["remote_sha256"],
                           "verification_basis": "attached cp10 manifest and analytic agent primary raw-source receipt",
                           "url": row["url"], "source_receipt": str((BASE / "work/agents/v_analytic/S6_SERIES_PUBLISH_V_pinned_program_receipt.json").relative_to(BASE))}
    listed = [name for _, _, _, names in GROUPS for name in names]
    assert len(listed) == len(set(listed)) == 44
    assert len(paths) == 53
    labels = set(re.findall(r"\\label\{([^}]+)\}", text))
    for _, _, targets, _ in GROUPS:
        assert set(targets) <= labels, set(targets) - labels

    table = [r"\section*{Programs}", r"\addcontentsline{toc}{section}{Programs}",
             "The programs below are available in the "
             r"\href{https://github.com/KokunoYumeto/s6-complex-structure-workbench/tree/\SsixRepositoryCommit}{repository}",
             r"at commit \texttt{\SsixRepositoryCommit}. Each filename links to its immutable source.",
             r"\begingroup\small", r"\setlength{\tabcolsep}{4pt}",
             r"\begin{longtable}{@{}p{.39\textwidth}p{.57\textwidth}@{}}",
             r"\caption{Programs for the exact computations and interval enclosures.}\label{tab:V:programs}\\",
             r"\toprule Computation and statements & Programs \\\midrule", r"\endfirsthead",
             r"\toprule Computation and statements & Programs \\\midrule", r"\endhead",
             r"\bottomrule\endfoot"]
    mapping = []
    replacements = []
    for key, title, targets, names in GROUPS:
        refs = r"\cref{" + ",".join(targets) + "}"
        left = r"\hypertarget{prog:V:" + key + "}{}" + title + r"\par " + refs
        links = []
        for filename in names:
            row = paths[filename]
            url = row["url"].replace(COMMIT, r"\SsixRepositoryCommit")
            links.append(r"\href{" + url + r"}{\nolinkurl{" + filename + "}}")
        table.append(left + " &\n" + r"\par ".join(links) + r" \\[3pt]")
        for target in targets:
            mapping.append({"statement_id": target, "table_target": "prog:V:" + key,
                            "task": title, "programs": "; ".join(names)})

        # Existing proof scopes are left unchanged. These proposed inserts are
        # citations only; root will integrate them before the final PDF reading.
        for target in targets:
            if target in {"night:P1.18", "maps:src:E.1.4", "maps:src:E.1.5"}:
                continue
            anchor = r"\label{" + target + "}"
            at = text.index(anchor, text.index(r"\begin{document}"))
            begin = text.index(r"\begin{proof}", at)
            end = text.index(r"\end{proof}", begin)
            before = text[max(begin, end - 210):end]
            # Extend to the start of its first source line for a readable guard.
            first = text.rfind("\n", begin, max(begin, end - 210))
            if first >= begin:
                before = text[first + 1:end]
            old = before + r"\end{proof}"
            assert text.count(old) == 1, target
            if target == "maps:src:F.2.32":
                sentence = "Exact calculations for the displayed finite examples appear in "
            elif target == "maps:src:F.3.5":
                sentence = "The algebraic calculations are implemented in "
            elif target in {"maps:src:E.2.9", "maps:src:E.2.11", "maps:src:E.2.19", "maps:src:E.2.20", "maps:src:E.2.21"}:
                sentence = "The finite algebra and combinatorial data are implemented in "
            else:
                sentence = "The corresponding exact calculations are implemented in "
            sentence += r"\hyperlink{prog:V:" + key + r"}{the programs in Table~\ref*{tab:V:programs}}."
            new = before + sentence + "\n" + r"\end{proof}"
            replacements.append({"type": "D09", "location": target,
                                 "old_text": old, "new_text": new,
                                 "reason": "Cite the verified program once through the program table; no mathematical statement or proof step changes.",
                                 "review_status": "citation insertion proposed; final integrated proof reading remains with root"})

    special = [
        ("maps:src:E.1.4", "$(A_j\\oplus C_j-I)\\Lambda$ and $m_ja-(v_j,0)$.  The complete relation matrix is computed by the program \\texttt{fourfolds\\_checks.py}.",
         "$(A_j\\oplus C_j-I)\\Lambda$ and $m_ja-(v_j,0)$. The complete relation matrix is obtained by stacking these integral relations; see \\hyperlink{prog:V:resolved}{Table~\\ref*{tab:V:programs}}."),
        ("maps:src:E.1.5", "The matrices and the restriction\norders are computed exactly in\n\\texttt{fourfolds\\_integral\\_audit.py}.",
         "The matrices and restriction orders are obtained by integer kernels and Smith reduction; see \\hyperlink{prog:V:resolved}{Table~\\ref*{tab:V:programs}}."),
        ("night:P1.18", "All inputs to these enclosures are the displayed rational connection, its gauges,\nthe integral monodromies and the specified normalization.",
         "All inputs to these enclosures are the displayed rational connection, its gauges,\nthe integral monodromies and the specified normalization.\nThe endpoint, Hessian, cusp and outer-cover enclosures are given by the\n\\hyperlink{prog:V:height}{executable certificate in Table~\\ref*{tab:V:programs}}."),
    ]
    for target, old, new in special:
        count = text.count(old)
        if count != 1:
            # Only whitespace variation is permitted for this known sentence.
            pat = r"\s+".join(re.escape(x) for x in old.split())
            found = list(re.finditer(pat, text))
            assert len(found) == 1, (target, count, len(found))
            old = found[0].group()
        replacements.append({"type": "D09", "location": target, "old_text": old, "new_text": new,
                             "reason": "Move the filename to one verified program-table citation, preserving mathematical inputs, method and output.",
                             "review_status": "citation insertion proposed; final integrated proof reading remains with root"})
    table.extend([r"\end{longtable}", r"\endgroup", ""])
    (ROOT / "S6_SERIES_PUBLISH_V_program_table.tex").write_text("\n".join(table))
    (ROOT / "S6_SERIES_PUBLISH_V_program_citation_replacements.json").write_text(json.dumps(replacements, indent=2) + "\n")
    with (ROOT / "S6_SERIES_PUBLISH_V_program_citation_map.tsv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(mapping[0]), delimiter="\t")
        writer.writeheader(); writer.writerows(mapping)
    fields = ("filename", "statement_ids", "disposition", "commit", "path", "bytes", "sha256", "verification_basis", "url")
    with (ROOT / "S6_SERIES_PUBLISH_V_programs_all.tsv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        for filename, row in sorted(paths.items()):
            output = {field: row.get(field, "") for field in fields}
            output["statement_ids"] = "; ".join(row["statement_ids"])
            output["disposition"] = "program table" if filename in listed else "independent check records"
            writer.writerow(output)
    receipt = {"source": str(current.relative_to(BASE)), "source_sha256": hashlib.sha256(current.read_bytes()).hexdigest(),
               "verified_historical_files": 53, "historical_mentions_preserved": 49,
               "additional_interval_modules": 4, "table_groups": len(GROUPS), "table_files": len(listed),
               "diagnostic_record_files": sorted(set(paths) - set(listed)),
               "guarded_citation_edits": len(replacements),
               "new_publication_programs_claimed_at_old_commit": 0,
               "mathematical_check_events_added": 0}
    (ROOT / "S6_SERIES_PUBLISH_V_program_table_receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
