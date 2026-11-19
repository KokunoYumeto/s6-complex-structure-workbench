"""Rebuild source statement numbering without changing mathematical text.

The check-record argument is hidden to reduce build cost; original numbering
is unchanged. Baseline pagination is not asserted to equal the supplied run.
"""
from pathlib import Path
import concurrent.futures, json, re, subprocess, time, os
from tex_tools import PAPERS, remove_check_text, aux_labels
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT.parent/'S6_SERIES_GRIND_source/S6_GRIND_1_papers_cp15'
OUT=ROOT/'build/baseline'
OUT.mkdir(parents=True,exist_ok=True)
ENV=os.environ.copy()
ENV['TEXMFHOME']=str(ROOT/'build/texlive-luatex/usr/share/texlive/texmf-dist')
ENV['TEXMFCACHE']='.'

def build(p):
    name=f'S6_10_PAPERS_{p}'
    text=(SOURCE/(name+'.tex')).read_text()
    text=remove_check_text(text)
    (OUT/(name+'.tex')).write_text(text)
    started=time.monotonic()
    with (OUT/(name+'.stdout')).open('w') as log:
        proc=subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error','-file-line-error',name+'.tex'],cwd=OUT,stdout=log,stderr=subprocess.STDOUT,env=ENV)
    aux=OUT/(name+'.aux')
    labels=aux_labels(aux.read_text(errors='replace')) if aux.exists() else {}
    result={'paper':p,'returncode':proc.returncode,'seconds':round(time.monotonic()-started,2),'labels':len(labels)}
    (ROOT/f'analysis/baseline_labels_{p}.json').write_text(json.dumps(labels,indent=2,ensure_ascii=False))
    (ROOT/f'code/outputs/baseline_{p}.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result),flush=True)
    return result

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    results=list(pool.map(build,PAPERS))
(ROOT/'code/outputs/baseline_build.json').write_text(json.dumps(results,indent=2))
