#!/usr/bin/env python3
"""Open the prescribed III records page; print bounded access evidence only."""

import datetime
import hashlib
import html
import json
import re
import urllib.error
import urllib.request


URL = (
    "https://github.com/KokunoYumeto/"
    "s6-complex-structure-workbench/blob/main/RECORDS.md#paper-iii"
)


def find_raw_lines(value):
    if isinstance(value, dict):
        lines = value.get("rawLines")
        if isinstance(lines, list) and all(isinstance(x, str) for x in lines):
            yield lines
        for child in value.values():
            yield from find_raw_lines(child)
    elif isinstance(value, list):
        for child in value:
            yield from find_raw_lines(child)


def main():
    print("UTC", datetime.datetime.now(datetime.timezone.utc).isoformat())
    print("REQUEST", URL)
    request = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            data = response.read()
            print("HTTP", response.status)
            print("FINAL_URL", response.geturl())
    except (urllib.error.URLError, TimeoutError) as exc:
        print("ACCESS_FAILURE", type(exc).__name__, str(exc))
        return
    print("BYTES", len(data))
    print("SHA256", hashlib.sha256(data).hexdigest())
    page = data.decode("utf-8")
    anchor = re.search(r'id="(?:user-content-)?paper-iii"', page)
    print("EXACT_HTML_ANCHOR", bool(anchor))
    found = False
    for block in re.findall(r'<script[^>]*type="application/json"[^>]*>(.*?)</script>', page, re.S):
        try:
            payload = json.loads(html.unescape(block))
        except json.JSONDecodeError:
            continue
        for lines in find_raw_lines(payload):
            try:
                start = lines.index("## Paper III")
            except ValueError:
                continue
            end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
            print("EXACT_MARKDOWN_SECTION_BEGIN")
            print("\n".join(lines[start:end]).strip())
            print("EXACT_MARKDOWN_SECTION_END")
            found = True
            break
        if found:
            break
    if not found and anchor:
        nearby = page[anchor.start():]
        section_end = re.search(r'<h2\b', nearby[1:])
        if section_end:
            nearby = nearby[:section_end.start() + 1]
        text = html.unescape(re.sub(r'<[^>]+>', ' ', nearby))
        print("EXACT_HTML_SECTION_TEXT", " ".join(text.split()))
        found = True
    print("SECTION_LOCATED", found)


if __name__ == "__main__":
    main()
