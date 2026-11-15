from pathlib import Path
from urllib.request import urlopen
root=Path(__file__).resolve().parents[1]
urls=[('C_Waldschmidt1979_original.pdf','https://mathreports.ca/download/1451/?tmstv=1788658231'),('C_Waldschmidt1979_translation.pdf','https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/GDL/SigmaNoteCanada1979-eng.pdf')]
for name,url in urls:
 try:
  d=urlopen(url,timeout=30).read();(root/'records'/name).write_bytes(d);print(name,len(d),d[:10],url)
 except Exception as e:print(name,type(e).__name__,str(e),url)
