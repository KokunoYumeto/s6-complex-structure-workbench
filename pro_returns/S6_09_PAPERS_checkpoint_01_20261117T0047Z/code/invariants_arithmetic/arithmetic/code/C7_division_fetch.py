"""Preserve primary sources for the division-hull / variable-degree test."""
from pathlib import Path
from urllib.request import urlopen
import hashlib
import subprocess

root=Path(__file__).resolve().parents[1]
archive=root.parent/'research_downloads/C7_division'
archive.mkdir(parents=True,exist_ok=True)
sources=[
 ('C_Herblot2012_meromorphic','https://webusers.imj-prg.fr/~mathilde.herblot/publi/SL.pdf'),
 ('C_Gasbarri2010_analytic','https://preprints.ihes.fr/storage/newscheiderlang.pdf'),
 ('C_RMS2020_division_method','https://pazuki.perso.math.cnrs.fr/index_fichiers/RMSLNS-Vol-26.pdf')]
for stem,url in sources:
    with urlopen(url,timeout=40) as response:
        data=response.read()
        print('URL:',response.url)
        print('Content-Type:',response.headers.get('Content-Type'))
    assert data.startswith(b'%PDF-')
    path=archive/(stem+'.pdf')
    path.write_bytes(data)
    print('Bytes:',len(data),'SHA256:',hashlib.sha256(data).hexdigest())
    conversion=subprocess.run(['pdftotext','-layout',str(path),str(path.with_suffix('.txt'))],
                              stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,check=True)
    if conversion.stderr:
        (archive/(stem+'_pdftotext_warnings.out')).write_text(conversion.stderr)
        print('pdftotext warnings preserved separately:',len(conversion.stderr),'characters')
print('All three primary PDFs fetched and text-extracted.')
