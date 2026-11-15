#!/usr/bin/env python3
"""Fetch primary material outside the distributable package and record provenance."""
from pathlib import Path
import hashlib
import json
import urllib.request

root = Path(__file__).resolve().parents[1]
external = root.parent / "external_sources" / "C_independent_primary"
external.mkdir(parents=True, exist_ok=True)
sources = [
    {
        "key": "Jiang2014E",
        "url": "https://archive.ymsc.tsinghua.edu.cn/pacm_download/613/12072-v4Regular_circle_actions_on_2-connected_7-manifolds.pdf",
        "filename": "Jiang2014_regular_circle_actions_author.pdf",
        "publication": "Yi Jiang (2014), Regular circle actions on 2-connected 7-manifolds, Journal of the London Mathematical Society 90(2), 373-387; DOI 10.1112/jlms/jdu028.",
        "version": "Author-hosted manuscript dated 19 April 2014, 19 pages; distinct from arXiv v3 dated 18 September 2013.",
        "verified": "Opened and visually read Lemma 3.5 Case 2, manuscript pp.13-15, and Lemma 3.6 on p.12. Publisher metadata independently opened. The Hopf four-handle, CP2 product normal, k=0 characteristic calculation and index coefficient are explicit.",
        "publisher_metadata": "https://academic.oup.com/jlms/article-abstract/90/2/373/2939198"
    },
    {
        "key": "MontgomeryYang1968E",
        "url": "https://page-one.springer.com/pdf/preview/10.1007/978-3-642-46141-5_4",
        "filename": "MontgomeryYang1968_II_primary_preview.pdf",
        "publication": "Deane Montgomery and C. T. Yang (1968), Differentiable actions on homotopy seven spheres, II, in P. S. Mostert (Ed.), Proceedings of the Conference on Transformation Groups, pp.125-134; DOI 10.1007/978-3-642-46141-5_4.",
        "version": "Publisher-authorized two-page preview of original pp.125-126; full chapter not opened.",
        "verified": "Opened primary first two pages: classical semifree action/knot correspondence and Pontryagin offset divisible by24. Page126 corrects the earlier claim that every homotopy7sphere supports free circle actions. The semifree and free assertions are kept distinct.",
        "publisher_metadata": "https://link.springer.com/chapter/10.1007/978-3-642-46141-5_4"
    }
]
for source in sources:
    target = external / source["filename"]
    try:
        request = urllib.request.Request(source["url"], headers={"User-Agent":"Mozilla/5.0"})
        with urllib.request.urlopen(request, timeout=45) as response:
            data = response.read()
        if not data.startswith(b"%PDF"):
            raise ValueError("Response is not a PDF")
        target.write_bytes(data)
        source["local_path"] = str(target)
        source["bytes"] = len(data)
        source["sha256"] = hashlib.sha256(data).hexdigest()
        source["download_status"] = "saved outside deliverable"
    except Exception as error:
        source["download_status"] = f"download unavailable: {error}"
record = {"scope":"Metadata and original reading record only; full articles are outside the deliverable.","sources":sources}
out = json.dumps(record, indent=2)+"\n"
(root/"evidence"/"E_C_index_sources.json").write_text(out)
Path(__file__).with_suffix(".out").write_text(out)
print(out)
