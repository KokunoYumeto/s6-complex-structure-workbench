"""Additional primary-source access audit for the A.5 conjecture search.

The downloads are research inputs; this program records access and extracts
the statements to local text.  No theorem is accepted from a title or abstract.
"""
from pathlib import Path
import subprocess
import sys
import urllib.request

ROOT = Path(__file__).resolve().parents[2]
DEST = ROOT / "research_downloads"
DEST.mkdir(exist_ok=True)
SOURCES = [
    ("Chan2018", "https://arxiv.org/pdf/1801.01605"),
    ("Baier2026v4", "https://arxiv.org/pdf/2609.21195v4"),
    ("LekkasPetridis2026published", "https://www.degruyterbrill.com/document/doi/10.1515/forum-2026-0040/pdf"),
    ("OSullivanTaylor2017", "https://fsw01.bcc.cuny.edu/cormac.osullivan/Research/HyperbolicPoincare-final-version-arxiv.pdf"),
    ("FriedlanderIwaniec1987", "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/263E90590AE38FB006C54AA6C71DD919/S0008414X00005083a.pdf/on_the_distribution_of_the_sequence_n2_mod_1.pdf"),
    ("GoldfeldHinkleHoffstein2026v4", "https://arxiv.org/pdf/2311.06587v4"),
    ("BrowningKumaraswamySteiner2017v2", "https://arxiv.org/pdf/1609.06097v2"),
    ("HuangTernaryI2024", "https://arxiv.org/pdf/2412.03350v1"),
    ("HeathBrown1996author", "https://ora.ox.ac.uk/objects/uuid%3Abbd3c62f-f010-44b5-8be5-87e903fb0084/files/m7ec02df6e1b8303a66e7a6015ecb6044"),
    ("ElAbdalaouiShparlinskiSteiner2022", "https://arxiv.org/pdf/2211.00379"),
    ("Creech2025", "https://arxiv.org/pdf/2508.18666"),
    ("Bykovskii2017", "https://www.mathnet.ru/php/getFT.phtml?jrnid=dvmg&option_lang=eng&paperid=348&what=fullt"),
]
for name, url in SOURCES:
    if len(sys.argv) > 1 and name not in sys.argv[1:]:
        continue
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(request, timeout=30) as response:
            data = response.read()
        if not data.startswith(b"%PDF-"):
            print(name, "NOT_PDF", len(data), url, flush=True)
            continue
        pdf = DEST / (name + ".pdf")
        pdf.write_bytes(data)
        out = DEST / (name + ".txt")
        subprocess.run(["pdftotext", "-layout", str(pdf), str(out)], check=True)
        print(name, "OPENED_PDF", len(data), "bytes; text", out, url, flush=True)
    except Exception as exc:
        print(name, "ACCESS_FAILED", type(exc).__name__, str(exc), url, flush=True)
