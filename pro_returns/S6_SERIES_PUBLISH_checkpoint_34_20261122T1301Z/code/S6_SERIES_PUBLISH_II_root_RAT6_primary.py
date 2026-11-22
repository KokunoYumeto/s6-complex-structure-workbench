from pathlib import Path
import datetime as dt,hashlib,json,subprocess,urllib.request
R=Path(__file__).resolve().parents[1]
temp=R.parent/'S6_SERIES_PUBLISH_root_RAT6_primary_temp';temp.mkdir(exist_ok=True)
url='https://webhomes.maths.ed.ac.uk/~v1ranick/papers/arnold15.pdf'
with urllib.request.urlopen(url,timeout=45) as f:payload=f.read();resolved=f.url
assert payload.startswith(b'%PDF')
pdf=temp/'Arnold1976.pdf';pdf.write_bytes(payload)
for p in [6,9,14,15]:
 subprocess.run(['pdftotext','-f',str(p),'-l',str(p),'-layout',str(pdf),str(temp/f'Arnold-p{p}.txt')],check=True)
for p in [6,9,15]:
 subprocess.run(['pdftoppm','-f',str(p),'-l',str(p),'-scale-to','1700','-png','-singlefile',str(pdf),str(temp/f'Arnold-p{p}')],check=True)
out=R/'agents/continuation2_root/S6_SERIES_PUBLISH_II_root_RAT6_primary_retrieval.json'
assert not out.exists()
out.write_text(json.dumps(dict(retrieved_utc=dt.datetime.now(dt.timezone.utc).isoformat(),url=url,resolved_url=resolved,sha256=hashlib.sha256(payload).hexdigest(),bytes=len(payload),version='Published Inventiones Mathematicae35(1976),87-109, university-hosted scan',downloaded_source_outside_checkpoint=True,extracted_pdf_pages=[6,9,14,15],rendered_pdf_pages=[6,9,15],actual_reading='Pending; extraction/rendering alone gives no reading credit.'),indent=2)+'\n')
print(out.read_text())
