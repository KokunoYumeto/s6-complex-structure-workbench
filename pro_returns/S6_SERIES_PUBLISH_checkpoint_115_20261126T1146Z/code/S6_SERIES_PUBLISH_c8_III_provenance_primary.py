#!/usr/bin/env python3
"""Read three prescribed primary URLs in memory; emit bounded access evidence."""

from concurrent.futures import ThreadPoolExecutor
import argparse
import datetime
import hashlib
import html
import json
import re
import urllib.request


SOURCES = (
    (
        "msc2020",
        "https://mathscinet.ams.org/mathscinet/msc/pdfs/classifications2020.pdf",
    ),
    ("arxiv_taxonomy", "https://arxiv.org/category_taxonomy"),
    ("cc0_deed", "https://creativecommons.org/publicdomain/zero/1.0/"),
)
MSC_ENTRIES = (
    ("32J17", 76, "Compact complex 3-folds"),
    ("32Q55", 78, "Topological aspects of complex manifolds"),
    ("55Q40", 147, "Homotopy groups of spheres"),
    ("57R55", 152, "Differentiable structures in differential topology"),
    ("14J27", 36, "Elliptic surfaces, elliptic or Calabi-Yau fibrations"),
)


def fetch(item):
    name, url = item
    rows = [
        ("SOURCE", name),
        ("UTC", datetime.datetime.now(datetime.timezone.utc).isoformat()),
        ("REQUEST", url),
    ]
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(request, timeout=40) as response:
            data = response.read()
            rows.extend((
                ("HTTP", response.status),
                ("FINAL_URL", response.geturl()),
                ("CONTENT_TYPE", response.headers.get("Content-Type")),
                ("LAST_MODIFIED", response.headers.get("Last-Modified")),
                ("ETAG", response.headers.get("ETag")),
            ))
        rows.extend((("BYTES", len(data)), ("SHA256", hashlib.sha256(data).hexdigest())))
        if name == "msc2020":
            import fitz

            with fitz.open(stream=data, filetype="pdf") as document:
                rows.append(("PDF_PAGES", len(document)))
                rows.append(("PDF_METADATA", document.metadata))
                first_page = " ".join(document[0].get_text().split())
                rows.append(("MSC2020_TITLE_PRESENT", "2020" in first_page))
                for code, index, phrase in MSC_ENTRIES:
                    page = " ".join(document[index].get_text().split())
                    exact = f"{code} {phrase}"
                    # Retain the exact character substitution used by this text check.
                    ligatures = {"ﬀ": "ff", "ﬁ": "fi", "ﬂ": "fl"}
                    extracted = page
                    for glyph, letters in ligatures.items():
                        extracted = extracted.replace(glyph, letters)
                    start = page.index(code) + len(code)
                    tail = page[start:].strip()
                    next_code = re.search(r"\s+\d{2}[A-Z]\d{2}\s", tail)
                    raw_label = tail[:next_code.start()] if next_code else tail
                    rows.append(("ENTRY", {
                        "code": code,
                        "PDF_page": index + 1,
                        "printed_page": index + 1,
                        "exact_label": phrase,
                        "exact_label_found": exact in extracted,
                        "ligature_substitutions_present": {
                            f"U+{ord(glyph):04X}": letters
                            for glyph, letters in ligatures.items() if glyph in raw_label
                        },
                    }))
        else:
            page = data.decode("utf-8")
            text = " ".join(html.unescape(re.sub(r"<[^>]+>", " ", page)).split())
            title = re.search(r"<title[^>]*>(.*?)</title>", page, re.S | re.I)
            rows.append(("TITLE", html.unescape(title.group(1)).strip() if title else None))
            if name == "arxiv_taxonomy":
                rows.append(("VERSION_SCOPE", "Current official taxonomy at this retrieval; no version number asserted."))
                for code in ("math.CV", "math.GT", "math.AT", "math.AG"):
                    match = re.search(re.escape(code) + r"\s*\(([^)]+)\)", text)
                    rows.append(("CATEGORY", {
                        "code": code,
                        "label": match.group(1) if match else None,
                        "exact_code_label_found": bool(match),
                    }))
            else:
                rows.append(("VERSION_SCOPE", "CC0 1.0 Universal"))
                rows.append(("CC0_1_0_UNIVERSAL_PRESENT", "CC0 1.0 Universal" in text))
    except Exception as exc:
        rows.append(("ACCESS_OR_ENTRY_FAILURE", f"{type(exc).__name__}: {exc}"))
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--msc-only", action="store_true")
    args = parser.parse_args()
    sources = SOURCES[:1] if args.msc_only else SOURCES
    with ThreadPoolExecutor(max_workers=3) as pool:
        for rows in pool.map(fetch, sources):
            for key, value in rows:
                print(key, json.dumps(value, ensure_ascii=False, sort_keys=True))
    print("SOURCE_COPY_SAVED false")


if __name__ == "__main__":
    main()
