"""Keep third-party primary papers outside the deliverable artifact tree."""
from pathlib import Path
import hashlib
import shutil

root=Path(__file__).resolve().parents[1]
dest=root.parent/'research_downloads/C7_division'
dest.mkdir(parents=True,exist_ok=True)
stems=['C_Herblot2012_meromorphic','C_Gasbarri2010_analytic',
       'C_RMS2020_division_method','C_GramainMignotteWaldschmidt1986']
for stem in stems:
    for suffix in ['.pdf','.txt','_pdftotext_warnings.out']:
        src=root/'records'/(stem+suffix)
        if src.exists():
            target=dest/src.name
            shutil.move(str(src),str(target))
            print(target,'bytes=',target.stat().st_size,
                  'sha256=',hashlib.sha256(target.read_bytes()).hexdigest())
src=root/'records/C_GMW1986_render'
if src.exists():
    shutil.move(str(src),str(dest/src.name))
    print('Moved source-page render directory:',dest/src.name)
print('Own access scripts and mathematical audit records remain in artifact tree.')
