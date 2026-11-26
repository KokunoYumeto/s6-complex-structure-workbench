#!/usr/bin/env python3
"""Render the single converged Paper III PDF for actual page-image reading."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import hashlib
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "agents/continuation8_tex_runtime/III_final/S6_SERIES_PUBLISH_III.pdf"
IMAGES = PDF.parent / "pages"
BATCHES = ((1, 94), (95, 294), (295, 494), (495, 680), (681, 694))


def render(first, last):
    command = ["pdftoppm", "-r", "150", "-png", "-f", str(first), "-l", str(last),
               str(PDF), str(IMAGES / "page")]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return first, last, result


def main():
    if not shutil.which("pdftoppm"):
        raise RuntimeError("pdftoppm is unavailable")
    IMAGES.mkdir(exist_ok=True)
    if any(IMAGES.glob("page-*.png")):
        raise RuntimeError("Page images already exist; no silent replacement")
    before = PDF.stat()
    identity = hashlib.sha256(PDF.read_bytes()).hexdigest()
    print("UTC start:", datetime.now(timezone.utc).isoformat(), flush=True)
    print("Single source PDF:", PDF, flush=True)
    print("PDF SHA256:", identity, flush=True)
    print("Image directory:", IMAGES, flush=True)
    print("Image names: page-001.png through page-694.png; 150 dpi", flush=True)
    failures = []
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = [pool.submit(render, first, last) for first, last in BATCHES]
        for future in as_completed(futures):
            first, last, result = future.result()
            print(f"Rendered requested pages {first}-{last}; exit {result.returncode}", flush=True)
            if result.stdout:
                sys.stdout.buffer.write(result.stdout)
            if result.stderr:
                sys.stderr.buffer.write(result.stderr)
            if result.returncode:
                failures.append((first, last, result.returncode))
    after = PDF.stat()
    if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
        raise RuntimeError("PDF changed during rendering; images require root review")
    missing = [page for page in range(1, 695) if not (IMAGES / f"page-{page:03d}.png").exists()]
    print("UTC complete:", datetime.now(timezone.utc).isoformat(), flush=True)
    print("Missing requested page images:", missing, flush=True)
    print("No visual-reading claim is assigned by rendering.", flush=True)
    return 1 if failures or missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
