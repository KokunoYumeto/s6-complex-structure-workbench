from pathlib import Path
import subprocess,concurrent.futures,datetime
root=Path('/workspace/scratch/e7a4d66da343/S6_06_BLIND')
pdf=root/'records/primary_sources/OS91.pdf'
out=root/'records/primary_sources/os91_images'
subprocess.run(['pdftoppm','-r','150','-png',str(pdf),str(out/'os')],check=True)
def ocr(p):
 q=p.with_suffix('')
 subprocess.run(['tesseract',str(p),str(q),'--psm','3'],check=True,capture_output=True)
 return p.name
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 for name in ex.map(ocr,sorted(out.glob('*.png'))): print(name,flush=True)
text='\n\n'.join('PAGE '+p.stem+'\n'+p.read_text() for p in sorted(out.glob('*.txt')))
(root/'records/primary_sources/OS91_ocr.txt').write_text(text)
with (root/'records/literature_control.md').open('a') as f:
 f.write(f'{datetime.datetime.now(datetime.timezone.utc).isoformat()} — OS91 original scanned primary PDF, 17 pages, OCR generated for table discovery and page images kept for direct checking.\n')
