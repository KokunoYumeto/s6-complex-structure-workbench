"""Read current exact source/PDF hashes and all six current typesetting logs."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,re,subprocess

P=Path(__file__).resolve().parents[2]
arg=argparse.ArgumentParser();arg.add_argument('checkpoint',type=int);ns=arg.parse_args()
previews={'I':'build/I_preview','II':'build/sign_II','III':'build/III_preview','IV':'analysis/IV/preview','V':'analysis/V/preview','VI':'build/sign_VI'}
papers={}
for paper,preview in previews.items():
    folder=P/'build/standalone'/paper
    record=json.loads((folder/'assembly_record.json').read_text())
    tex=P/f'S6_10_PAPERS_{paper}.tex';pdf=tex.with_suffix('.pdf')
    log=(folder/f'S6_10_PAPERS_{paper}.log').read_text(errors='replace')
    hashes={'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'tex_sha256':hashlib.sha256(tex.read_bytes()).hexdigest(),'source_sha256':hashlib.sha256((P/preview/'preview.tex').read_bytes()).hexdigest()}
    assert all(record[k]==v for k,v in hashes.items()),paper
    diagnostics={
        'missing_characters':len(re.findall('Missing character:',log)),
        'font_warnings':len(re.findall(r'(?:LaTeX Font Warning|fontspec Warning)',log)),
        'overfull_above2pt':[float(x) for x in re.findall(r'Overfull \\[hv]box \(([0-9.]+)pt',log) if float(x)>2],
        'undefined_reference_messages':len(re.findall(r'LaTeX Warning: Reference',log)),
        'undefined_citation_messages':len(re.findall(r'Package natbib Warning: Citation',log))}
    assert diagnostics=={k:record[k] for k in diagnostics},paper
    assert not any(diagnostics.values()),(paper,diagnostics)
    info=subprocess.check_output(['pdfinfo',str(pdf)],text=True)
    pages=int(re.search(r'^Pages:\s+(\d+)',info,re.M)[1])
    papers[paper]={'pages':pages,**hashes,'diagnostics':diagnostics,'current_log_read':True}
out={'timestamp_utc':datetime.now(timezone.utc).isoformat(),'papers':papers,'scope':'All six current canonical TeX/PDF and exact preview-source hashes match successful assembly records. All six current logs read; required diagnostics zero. Visual review is separately recorded and confers no mathematical proof credit.'}
dest=P/f'analysis/continuation_root/checkpoint{ns.checkpoint:02d}_build_snapshot.json'
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'snapshot':str(dest),'pages':{k:v['pages'] for k,v in papers.items()},'status':'PASS'}))
