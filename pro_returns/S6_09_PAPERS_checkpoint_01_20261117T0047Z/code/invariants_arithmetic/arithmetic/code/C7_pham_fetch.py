from urllib.request import urlopen
from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
u='https://www.cambridge.org/core/journals/glasgow-mathematical-journal/article/abs/semiabelian-varieties-and-transcendence-on-weierstrass-sigma-functions/D291E48168188D71FF20D939CAFDD651'
try:
 d=urlopen(u,timeout=30).read();(root/'records/C_Pham2025_metadata.html').write_bytes(d);ss=d.decode('utf-8','replace');print('HTML bytes',len(d));print('Published PDF links:',re.findall(r'<meta[^>]*name="citation_pdf_url"[^>]*>',ss))
except Exception as e:print(type(e).__name__,e)
