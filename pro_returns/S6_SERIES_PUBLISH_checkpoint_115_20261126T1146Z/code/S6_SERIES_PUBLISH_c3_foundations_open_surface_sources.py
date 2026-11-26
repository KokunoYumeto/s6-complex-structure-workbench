from pathlib import Path
import concurrent.futures
import hashlib
import urllib.request

OUT = Path('/workspace/scratch/9fcd229a9ed4/base/S6_PUBLISH_c3_foundations_sources')
OUT.mkdir(exist_ok=True)
URLS = {
    'S6_SERIES_PUBLISH_Inoue1974_volume.pdf': 'https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0024/PPN356556735_0024.pdf',
    'S6_SERIES_PUBLISH_Beauville1978.pdf': 'https://numdam.org/item/AST_1978__54__R1_0.pdf',
    'S6_SERIES_PUBLISH_Kodaira1954_reprint.pdf': 'https://api.pageplace.de/preview/DT0400.9781400869862_A26058233/preview-9781400869862_A26058233.pdf',
    'S6_SERIES_PUBLISH_OVV2020_v3.pdf': 'https://arxiv.org/pdf/1810.05768v3',
}

def get(item):
    name, url = item
    path = OUT / name
    if not path.exists():
        request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(request, timeout=45) as response:
            path.write_bytes(response.read())
    data = path.read_bytes()
    return name, len(data), hashlib.sha256(data).hexdigest()

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    results = [executor.submit(get, item) for item in URLS.items()]
    for future in results:
        try:
            print(*future.result())
        except Exception as error:
            print(type(error).__name__, str(error))
