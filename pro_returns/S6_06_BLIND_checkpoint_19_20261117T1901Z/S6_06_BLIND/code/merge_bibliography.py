"""Merge verified source records without discarding the earlier root entries."""
from pathlib import Path
import re, json
ROOT=Path(__file__).resolve().parents[1]
target=ROOT/'S6_06_BLIND_references.bib'
sources=[target]+sorted(ROOT.glob('code/part*/references.bib'))
entries={}
provenance={}
for source in sources:
    text=source.read_text()
    starts=list(re.finditer(r'(?m)^@\w+\s*\{\s*([^,]+),',text))
    for i,m in enumerate(starts):
        key=m.group(1).strip()
        entry=text[m.start():starts[i+1].start() if i+1<len(starts) else len(text)].strip()
        if key in entries:continue
        if not re.search(r'\b(?:unverified|verified)\b',entry,re.I):
            entry=re.sub(r'(note\s*=\s*\{)',r'\1verified: ',entry,count=1,flags=re.I)
        entries[key]=entry
        provenance[key]=str(source.relative_to(ROOT))
extra=r'''
@article{Lojasiewicz1964,
 author={Lojasiewicz, Stanislaw}, title={Triangulation of semi-analytic sets},
 journal={Annali della Scuola Normale Superiore di Pisa}, series={3},
 volume={18}, number={4}, pages={449--474}, year={1964},
 url={https://www.numdam.org/item/ASNSP_1964_3_18_4_449_0.pdf},
 note={verified: primary original article opened; Theorems 1 and 2, pp463--464; used for the explicit neighbourhood retraction in P4R.1}
}
@article{BobadillaKollar2012,
 author={Fernandez de Bobadilla, Javier and Kollar, Janos},
 title={Homotopically trivial deformations}, journal={Journal of Singularities},
 volume={5}, pages={85--93}, year={2012}, doi={10.5427/jsing.2012.5f},
 url={https://www.journalofsing.org/volume5/bobadilla-kollar.pdf},
 note={verified: primary PDF opened in the web tool; Definition 1 and the following neighbourhood-retraction statement p85. Direct archive request returned HTTP406.}
}
'''
starts=list(re.finditer(r'(?m)^@\w+\s*\{\s*([^,]+),',extra))
for i,m in enumerate(starts):
    key=m.group(1).strip()
    if key not in entries:
        entries[key]=extra[m.start():starts[i+1].start() if i+1<len(starts) else len(extra)].strip()
        provenance[key]='root primary-source checks'
target.write_text('\n\n'.join(entries.values())+'\n')
(ROOT/'records/bibliography_provenance.json').write_text(json.dumps(provenance,indent=2)+'\n')
print(json.dumps({'entries':len(entries),'sources':[str(s.relative_to(ROOT)) for s in sources]},indent=2))
