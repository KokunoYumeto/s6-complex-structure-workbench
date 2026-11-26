from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
# Published source pages stay outside the publication checkpoint.
OUT = ROOT.parent / 'S6_PUBLISH_c3_foundations_sources'
OUT.mkdir(exist_ok=True)


def fetch(page):
    sequence = page + 6
    url = ('https://images.p.sub.uni-goettingen.de/iiif/image/'
           f'gdz:PPN356556735_0031:{sequence:08}/full/1600,/0/default.jpg')
    with urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=35) as response:
        assert response.headers.get('Content-Type', '').startswith('image/')
        content = response.read()
    path = OUT / f'S6_SERIES_PUBLISH_Steenbrink1976_p{page}.jpg'
    path.write_bytes(content)
    return page, hashlib.sha256(content).hexdigest(), str(path), url


with ThreadPoolExecutor(max_workers=6) as pool:
    for page, sha, path, url in pool.map(fetch, (231, 233, 234, 237, 238, 239)):
        print(f'{page}\t{sha}\t{path}\t{url}')
