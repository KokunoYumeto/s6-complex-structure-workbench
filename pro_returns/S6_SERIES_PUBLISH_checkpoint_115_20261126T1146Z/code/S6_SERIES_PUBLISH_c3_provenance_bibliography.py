#!/usr/bin/env python3
"""Prepare version-specific bibliography edits140–141 without admission."""
from pathlib import Path
import csv
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "agents/continuation3_provenance"
source = (ROOT / "S6_SERIES_PUBLISH_II.tex").read_text()
items = [
    ("Reid1997Chapters", "140", "https://arxiv.org/pdf/alg-geom/9602006v1",
     "/tmp/S6_SERIES_PUBLISH_c3_conductor_primary/Reid1997Chapters_arxiv_v1.pdf",
     "92d96864143d3e3701712b1efe6e8e8b2a9802eb8f2c776356fb47c578f40e6e",
     r"\newblock URL \url{https://mreid.warwick.ac.uk/surf/Reid_Park_City_chapters.pdf}.",
     r"""\newblock Cited preprint edition: arXiv:alg-geom/9602006v1,
6 February 1996.
\newblock Page locators refer to this edition.
\newblock URL \url{https://arxiv.org/pdf/alg-geom/9602006v1}.""",
     "Proposition4.14(ii) pp91–92; §4.17 lemma pp94–95; Theorem4.20 p99",
     "Read the opened PDF title page and its arXiv v1 margin, then compared the complete existing bibliography entry. Conductor opened and read the cited statements/proofs and supplied the exact locus/hash. Preserve the publisher, book pagination and DOI while identifying the arXiv layout used by the proof citations."),
    ("Teleman2006", "141", "https://arxiv.org/pdf/0704.2948v3",
     "/tmp/S6_SERIES_PUBLISH_c3_conductor_primary/Teleman2006.pdf",
     "6fc69a26134b64b610ebc7281f4e82706d11be4fb5f522441a758fd5b884aca0",
     r"\newblock URL \url{https://arxiv.org/pdf/0704.2948}.",
     r"""\newblock Cited preprint edition: arXiv:0704.2948v3,
30 June 2007.
\newblock Page locators refer to this edition.
\newblock URL \url{https://arxiv.org/pdf/0704.2948v3}.""",
     "Lemma2.3(1)–(2), pp5–6",
     "Read the opened PDF title page, whose arXiv margin identifies v3 on30June2007 and whose internal typesetting date is14November2018. The citation identifies the arXiv version, preserving the journal2006 metadata and DOI. Conductor opened and read the complete lemma/proof and supplied the exact locus/hash.")
]
rows = []
evidence = []
for key, number, url, path, expected, old_url, replacement, locus, note in items:
    data = Path(path).read_bytes()
    actual = hashlib.sha256(data).hexdigest()
    assert actual == expected
    match = re.search(r"\\bibitem\[[^\n]*\]\{" + re.escape(key) + r"\}.*?(?=\n\\bibitem|\n\\end\{thebibliography\})", source, re.S)
    assert match, key
    old = match.group().rstrip()
    assert old.count(old_url) == 1
    new = old.replace(old_url, replacement)
    rows.append(dict(change_id="II-C3-PROV-"+number, type="D18",
        statement_id="bibliography:"+key, old_location="Paper II bibliography: "+key,
        old_page="cp35; final PDF concordance pending",
        new_location="Paper II bibliography: "+key, new_page="integrated build pending",
        old_text=old, new_text=new, reason=note,
        review_status="Exact old/new bibliography comparison and title-page version reading complete; no shared-source write."))
    evidence.append(dict(bibkey=key, url=url, version=re.search(r"arXiv:([^,\n]+)", replacement).group(1),
        sha256=actual, bytes=len(data), locus=locus,
        outcome=note, primary_source_bytes="Outside checkpoint; not copied into the deliverable."))
for name, data in [("S6_SERIES_PUBLISH_c3_provenance_bibliography_edits.tsv", rows),
                   ("S6_SERIES_PUBLISH_c3_provenance_bibliography_sources.tsv", evidence)]:
    with (OUT/name).open("w", newline="") as f:
        writer=csv.DictWriter(f, list(data[0]), delimiter="\t")
        writer.writeheader()
        writer.writerows(data)
print("Prepared II-C3-PROV-140 and141; source files unchanged.")
