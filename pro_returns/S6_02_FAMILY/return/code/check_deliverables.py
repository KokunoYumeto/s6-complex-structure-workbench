"""Final structural checks of sources, ledger, bibliography, and certificate."""
from pathlib import Path
import csv,json,re,sys
import sympy,mpmath

ROOT=Path(__file__).resolve().parents[1]
texfiles=list(ROOT.glob('*.tex'))+list((ROOT/'sections').glob('*.tex'))
for path in texfiles:
    text=path.read_text()
    bad=[ord(c) for c in text if ord(c)<32 and c not in '\n\r\t']
    assert not bad,(str(path),bad)
bib=(ROOT/'S6_02_FAMILY_references.bib').read_text()
entries=re.findall(r'@\w+\{([^,]+),',bib)
assert len(entries)==len(set(entries))
assert bib.count('note = {verified:')==len(entries)
citations=set()
for path in texfiles:
    for match in re.finditer(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}',path.read_text()):
        citations.update(match.group(1).split(','))
assert citations<=set(entries),citations-set(entries)
rows=list(csv.DictReader((ROOT/'S6_02_FAMILY_results.csv').open()))
assert len(rows)==55
assert {r['id'] for r in rows if r['status']=='Open'}=={'C.3.3','E.1.5','E.2.3'}
report=(ROOT/'S6_02_FAMILY_report.md').read_text()
assert report.startswith('| Item |')
assert len(re.findall(r'^\| [A-F]\.\d+ \|',report,flags=re.M))>=20
cert=json.loads((ROOT/'code/f_interval_parallel_certificate.json').read_text())
assert cert['summary']['result']=='PASS'
assert not cert['pending'] and not cert['summary']['undecided_boxes']
assert len(cert['certified'])==19701
log=(ROOT/'S6_02_FAMILY_paper.log').read_text(errors='replace')
for forbidden in ['Undefined control sequence','undefined references','Overfull','Missing character','Fatal error']:
    assert forbidden not in log,forbidden
assert (ROOT/'S6_02_FAMILY_paper.pdf').stat().st_size>100000
print('PASS: source controls, bibliography, citations, ledger, every prompt item, certificate, and final compiler log.')
print('STATEMENTS',len(rows))
print('VERIFIED_BIBLIOGRAPHY_ENTRIES',len(entries))
print('PYTHON',sys.version.replace('\n',' '))
print('SYMPY',sympy.__version__)
print('MPMATH',mpmath.__version__)
print('PDF_BYTES',(ROOT/'S6_02_FAMILY_paper.pdf').stat().st_size)

