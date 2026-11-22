#!/usr/bin/env python3
"""Prepare guarded shared-bibliography corrections, leaving the main files untouched."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT.parents[2]


def fields(entry):
    at = entry.index(",") + 1
    result = {}
    while at < len(entry):
        match = re.search(r"([A-Za-z_][\w-]*)\s*=\s*\{", entry[at:])
        if not match:
            break
        start = at + match.start()
        opening = at + match.end() - 1
        depth, i = 1, opening + 1
        while depth:
            if entry[i] == "\\":
                i += 2
                continue
            if entry[i] == "{": depth += 1
            if entry[i] == "}": depth -= 1
            i += 1
        end = i + (i < len(entry) and entry[i] == ",")
        result[match.group(1).lower()] = (start, end, opening + 1, i - 1)
        at = end
    return result


def setfield(entry, key, value):
    fs = fields(entry)
    if key in fs:
        _, _, a, b = fs[key]
        return entry[:a] + value + entry[b:]
    at = entry.rfind("}")
    prefix = entry[:at].rstrip()
    if not prefix.endswith(","):
        prefix += ","
    return prefix + "\n  " + key + " = {" + value + "},\n" + entry[at:]


def delfield(entry, key):
    fs = fields(entry)
    if key in fs:
        a, b, _, _ = fs[key]
        return entry[:a] + entry[b:]
    return entry


SCOPES = {
    "AC26": ("Attached original PDF, Theorem 7.17 p.57, Theorem 7.22 p.60, and section 7.7 pp.60--63 (Lemma 7.25 and Proposition 7.26 p.61; Proposition 7.27 pp.62--63; Corollary 7.29 p.63). The original PDF controls these locators.",
             "agents/provenance/S6_SERIES_PUBLISH_AC26_section_7_7_receipt.json"),
    "E26": ("Official arXiv:2609.38442v1 PDF: section 2 p.3 gives the rational elliptic surface, its j-function and displayed Weierstrass equation; Lemma 7.6 p.21 gives the transgressions used in the resolved-product calculation.",
            "agents/provenance/literature/S6_SERIES_PUBLISH_Engel_DGKX_receipt.json"),
    "DGKX2026v1": ("Official arXiv:2610.00250v1 PDF: Lemma 6.1 p.74; Lemma 6.2 pp.74--75; Proposition 6.5 p.76; Proposition 6.6 p.77; Proposition 6.10 pp.79--80. The direct-image proposition concerns the two-dimensional torus family; Paper V applies the method after giving its three-dimensional torus calculation.",
                   "agents/provenance/literature/S6_SERIES_PUBLISH_Engel_DGKX_receipt.json"),
    "ffEsoleKang": ("Official arXiv:1807.08755v1 PDF: equation (1.2), printed p.3/PDF p.4; equations (1.3)--(1.4), printed p.4/PDF p.5. Only the universal characteristic-class polynomials are used.",
                    "agents/provenance/literature/S6_SERIES_PUBLISH_primary_pdf_receipts.json"),
    "ffJiaMeng": ("Official arXiv:2201.06748v1 PDF: Theorem 1.1 and Remark 1.2, printed/PDF p.2, give a Kaehler modification obtained by blowups in smooth centres.",
                  "agents/provenance/literature/S6_SERIES_PUBLISH_primary_pdf_receipts.json"),
    "ffMandal": ("Official arXiv:2609.27929v1 PDF: Corollary 1.4 p.4, Lemma 2.1 p.5, Theorem 2.4 p.7. The almost-complex existence criterion and both displayed Pontryagin formulas were read at these printed pages.",
                 "agents/provenance/literature/S6_SERIES_PUBLISH_primary_pdf_receipts.json"),
    "Yang2026": ("Official arXiv:2609.29666v1 source archive was opened and its TeX member matched the attached source byte for byte, SHA256 5061ce4e6cda8ed7ba3bb2a7a597d50e018bfd53fb9e49e7b38317f628c332a5. Theorem 8.7 pp.57--59 and Corollary 8.8 p.59 explicitly allow the nonsymmetric holomorphic correction and uniform properness used in dimension three. Source filenames containing REPAIRED are members of that official v1 archive.",
                 "agents/provenance/S6_SERIES_PUBLISH_Yang_version_receipt.json; agents/v_analytic/S6_SERIES_PUBLISH_V_analytic_check.md"),
    "IVVOkaOneV5": ("Official arXiv:2303.15855v5 PDF: Definition 7.11, Remark 7.12 and the observation preceding Proposition 7.13, p.23; Proposition 7.13(a,b) p.23 and (c,d) p.24. The LSAP-fibre bundle implication is part (d). Published metadata independently opened at Springer DOI 10.1007/s00209-025-03833-4; cited pages remain those of v5.",
                      "agents/v_analytic/S6_SERIES_PUBLISH_V_Oka_v5_locator_receipt.json"),
    "IVVWallForm": ("Authors' version v3: section 3.3 pp.11--12, Definition 3.6 p.12, Theorem 3.7(1) pp.13--14. The cited oriented almost-diffeomorphism classification uses the pairing and stable normal homomorphism. Published journal metadata independently opened at Cambridge DOI 10.1017/S1446788722000167; cited pages remain those of the authors' version.",
                     "agents/v_topology/S6_SERIES_PUBLISH_V_topology_checks.md"),
    "IVVKramerStolz": ("Published primary institutional PDF, Theorem A p.178. The paper's orientation argument is retained in Paper V's connected-sum application.",
                        "agents/v_topology/S6_SERIES_PUBLISH_V_topology_checks.md"),
    "ffPetersSterk": ("Authors' June 2024 PDF: Theorem 2.2.1 printed p.61/PDF p.68, Theorem 2.3.1 p.62 and Theorem 2.4.2 p.63. Applied to the rank-four odd unimodular form with signature two.",
                      "agents/v_topology/S6_SERIES_PUBLISH_V_topology_checks.md"),
    "rootBHJ22": ("Published primary PDF: hypothesis (H) p.2, Theorem 3.4 and proof p.6, Propositions 8.1--8.2 and Algorithm 8.3 with correctness proof p.21, Theorem 8.4 p.22. The cusp-centralizer quotient is shown to satisfy (H), and the opposite-algebra conversion supplies the right-module convention.",
                   "agents/v_topology/S6_SERIES_PUBLISH_V_involution_checks.md"),
    "ffDeligne": ("Primary Numdam PDF: Definition 4.2.4 and Proposition 4.2.5 printed p.44, Theorem 4.2.6 p.45. Applied to the polarized algebraic abelian-surface local system in the source obstruction.",
                   "agents/v_analytic/S6_SERIES_PUBLISH_V_analytic_check.md"),
    "ffForstnericPrezelj02": ("Primary arXiv:math/0101040v3 PDF: Theorem 1.2 is printed on p.3, not p.2. Its holomorphic-section conclusion is used for the frame bundle with the explicit spray (g,A) mapped to g exp(A).",
                              "agents/v_analytic/S6_SERIES_PUBLISH_V_analytic_check.md"),
    "Catanese2004": ("Author-hosted published PDF: Theorem 2.1 on printed p.264/PDF p.4 and the immediately preceding marked-torus parameter space. The theorem states that deformations of a complex torus remain complex tori.",
                      "agents/provenance/literature/S6_SERIES_PUBLISH_Catanese_receipt.json"),
    "HirzebruchTopologicalMethods": ("Official author-archive scan: printed pp.183--184/PDF pp.194--195, Theorem 24.5.3, Theorem 24.5.4 and its Todd-genus integrality corollary. Both pages were rendered and visually read; the almost-complex hypothesis is explicit. The exact scan URL and hash are retained in the source receipt.",
                                     "agents/v_topology/S6_SERIES_PUBLISH_V_Hirzebruch_source_check.json"),
    "pubLieGroups2016": ("Primary Berkeley lecture notes, version of 5 October 2016, section 7.3 p.129/PDF p.139. The primitive exterior-square double cover has kernel plus or minus the identity. The form-specific unipotent calculation remains in Paper V.",
                         "root source-opening record; agents/provenance/S6_SERIES_PUBLISH_provenance_checks_V.tsv"),
}


def main():
    path = BASE / "work/S6_SERIES_PUBLISH_references.bib"
    old = path.read_text()
    tex = (BASE / "work/S6_SERIES_PUBLISH_V.tex").read_text()
    keys = set(re.findall(r"^\\bibitem[^\n]*\{([^{}]+)\}\s*$", tex, re.M))
    matches = list(re.finditer(r"^@([A-Za-z]+)\{([^,]+),", old, re.M))
    patches, scope_rows = [], []
    result = old
    for index, match in enumerate(matches):
        key = match.group(2)
        if key not in keys and key not in {"Grauert1960D", "manYang26"}:
            continue
        end = matches[index + 1].start() if index + 1 < len(matches) else len(old)
        entry = old[match.start():end]
        revised = entry
        original_fields = fields(entry)
        # Verification history is kept exactly, in a nonprinting custom field.
        # This prevents production records becoming printed bibliography notes.
        if "note" in original_fields:
            _, _, a, b = original_fields["note"]
            note = entry[a:b]
            if "verified" in note.lower() or "opened" in note.lower() or "scope:" in note.lower():
                revised = delfield(revised, "note")
                revised = setfield(revised, "verification_history", note)
        if key in SCOPES:
            scope, receipt = SCOPES[key]
            revised = setfield(revised, "verification", "verified at the listed primary-source scope")
            revised = setfield(revised, "publication_verification", "20 November 2026. " + scope)
            revised = setfield(revised, "publication_verification_record", receipt.replace("_", r"\_"))
            scope_rows.append({"key": key, "status": "verified at listed current scope", "scope": scope, "receipt": receipt})
        if key == "IVVWallForm":
            revised = revised.replace("@misc{", "@article{", 1)
            revised = delfield(revised, "howpublished")
            for field, value in {"title":"Simply connected manifolds with large homotopy stable classes",
                                 "journal":"Journal of the Australian Mathematical Society", "volume":"115",
                                 "number":"2", "pages":"172--203", "year":"2023",
                                 "doi":"10.1017/S1446788722000167",
                                 "note":"Statement and page numbers cited refer to the authors' version v3 (2021)."}.items():
                revised = setfield(revised, field, value)
        if key == "IVVOkaOneV5":
            revised = revised.replace("@misc{", "@article{", 1)
            revised = delfield(revised, "howpublished")
            for field, value in {"journal":"Mathematische Zeitschrift", "volume":"311", "pages":"33",
                                 "eid":"33", "year":"2025", "doi":"10.1007/s00209-025-03833-4",
                                 "archivePrefix":"arXiv", "eprint":"2303.15855v5",
                                 "note":"Article 33. Statement and page numbers cited refer to arXiv:2303.15855v5 (10 April 2025)."}.items():
                revised = setfield(revised, field, value)
        if key == "AC26": revised = setfield(revised, "howpublished", "Manuscript, 108 pages")
        if key == "ffDeligne": revised = setfield(revised, "url", "https://www.numdam.org/article/PMIHES_1971__40__5_0.pdf")
        if key == "IVVKramerStolz": revised = setfield(revised, "url", "https://www.uni-muenster.de/AGKramer/linuspub/27.pdf")
        if key == "rootBHJ22": revised = setfield(revised, "url", "https://epub.ub.uni-muenchen.de/94856/1/computation-of-lattice-isomorphisms-and-the-integral-matrix-similarity-problem.pdf")
        if key == "ffForstnericPrezelj02":
            revised = setfield(revised, "source_note", SCOPES[key][0])
            revised = setfield(revised, "url", "https://arxiv.org/pdf/math/0101040v3")
            revised = setfield(revised, "note", "Statement and page numbers cited refer to arXiv:math/0101040v3.")
        if key in {"Yang2026", "E26", "ffEsoleKang", "ffJiaMeng", "ffMandal"}:
            identifiers = {"Yang2026":"2609.29666v1", "E26":"2609.38442v1", "ffEsoleKang":"1807.08755v1",
                           "ffJiaMeng":"2201.06748v1", "ffMandal":"2609.27929v1"}
            revised = setfield(revised, "eprint", identifiers[key])
            revised = setfield(revised, "url", "https://arxiv.org/pdf/" + identifiers[key])
        if key == "HirzebruchTopologicalMethods":
            revised = setfield(revised, "publication_source_url", "https://hirzebruch.mpim-bonn.mpg.de/id/eprint/114/1/M2_Topological%20methods.pdf")
        if key == "pubLieGroups2016": revised = setfield(revised, "note", "Version of 5 October 2016.")
        titles = {"Douady1974":r"Le probl\`eme des modules locaux pour les espaces $\mathbf{C}$-analytiques compacts",
                  "ffDeligne":r"Th{\'e}orie de {Hodge}, {II}",
                  "mapsDeligne1974HodgeIII":r"Théorie de {Hodge}, {III}",
                  "ffEsoleKang":"Characteristic numbers of crepant resolutions of {Weierstrass} models",
                  "ffJiaMeng":r"Equivariant {K{\"a}hler} model for {Fujiki}'s class",
                  "ffChen":"Limits of {Hodge} structures via holonomic {D}-modules",
                  "mapsVogel09":"Existence of {Engel} structures",
                  "StacksProject":"The {Stacks} Project"}
        if key in titles: revised = setfield(revised, "title", titles[key])
        if key in {"Grauert1960D", "manYang26"}:
            revised = setfield(revised, "canonical_key", {"Grauert1960D":"Grauert60", "manYang26":"Yang2026"}[key])
        if revised != entry:
            assert result.count(entry) == 1, key
            result = result.replace(entry, revised, 1)
            patches.append({"key":key, "old_text":entry, "new_text":revised,
                            "reason":"Retain verified citation corrections, exact source-version locators, and nonprinting verification history; no citation alias is deleted while another paper may still use it."})
    assert set(SCOPES) <= {row["key"] for row in scope_rows}
    (ROOT / "S6_SERIES_PUBLISH_V_bibliography_replacements.json").write_text(json.dumps(patches,indent=2)+"\n")
    (ROOT / "S6_SERIES_PUBLISH_references_V_proposed.bib").write_text(result)
    (ROOT / "S6_SERIES_PUBLISH_V_bibliography_verification.json").write_text(json.dumps(scope_rows,indent=2)+"\n")
    receipt = {"source":str(path.relative_to(BASE)),"source_sha256":hashlib.sha256(old.encode()).hexdigest(),
               "proposed_sha256":hashlib.sha256(result.encode()).hexdigest(),"guarded_entries":len(patches),
               "current_primary_scope_entries":len(scope_rows),
               "citation_aliases":{"Grauert1960D":"Grauert60","manYang26":"Yang2026"},
               "old_alias_occurrences_in_V":{key:len(re.findall(r"\\cite\w*(?:\[[^\]]*\])*\{[^}]*\b"+key+r"\b[^}]*\}",tex)) for key in ["Grauert1960D","manYang26"]},
               "published_metadata_sources":["https://www.cambridge.org/core/journals/journal-of-the-australian-mathematical-society/article/simply-connected-manifolds-with-large-homotopy-stable-classes/8C98BF4A49F0C1558FFB0EAC550E6A31", "https://link.springer.com/article/10.1007/s00209-025-03833-4"]}
    (ROOT / "S6_SERIES_PUBLISH_V_bibliography_receipt.json").write_text(json.dumps(receipt,indent=2)+"\n")
    print(json.dumps(receipt,indent=2))


if __name__ == "__main__": main()
