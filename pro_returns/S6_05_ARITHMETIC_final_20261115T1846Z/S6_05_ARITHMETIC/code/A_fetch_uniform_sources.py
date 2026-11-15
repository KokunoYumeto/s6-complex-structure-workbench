"""Preserve primary PDFs already opened during the A.5 uniformity audit."""
from concurrent.futures import ThreadPoolExecutor
from hashlib import sha256
from pathlib import Path
from urllib.request import Request, urlopen
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    "A_Michel2003_Fields": "https://www.epfl.ch/labs/tan/wp-content/uploads/2018/10/Fields2003.pdf",
    "A_Nelson2022_Quadratic": "https://arxiv.org/pdf/2001.08704v3",
    "A_Merikoski2025_Primes": "https://arxiv.org/pdf/2503.05396v1",
    "A_Xu2025_Uniform": "https://arxiv.org/pdf/2509.05968v1",
}

def fetch(item):
    stem, url = item
    path = ROOT / "records" / (stem + ".pdf")
    try:
        data = urlopen(Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=40).read()
        if not data.startswith(b"%PDF-"):
            raise ValueError("response is not a PDF")
        path.write_bytes(data)
        subprocess.run(["pdftotext", "-layout", str(path), str(path.with_suffix(".txt"))],
                       check=True, capture_output=True)
        return f"{stem}: bytes={len(data)} sha256={sha256(data).hexdigest()} url={url}"
    except Exception as exc:
        return f"{stem}: FAILED {type(exc).__name__}: {exc}; url={url}"

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=4) as executor:
        for result in executor.map(fetch, SOURCES.items()):
            print(result)
