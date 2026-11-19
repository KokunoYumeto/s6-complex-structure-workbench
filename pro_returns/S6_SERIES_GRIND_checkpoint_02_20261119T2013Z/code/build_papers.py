"""Build current papers and retain exact log diagnostics and label/page maps."""
from pathlib import Path
import argparse,concurrent.futures,json,os,re,subprocess,time,shutil
from tex_tools import aux_labels
ROOT=Path(__file__).resolve().parents[1]
PAPERS=['I','II','III','IV','V']

def diagnostics(log):
    over=[]
    for m in re.finditer(r'Overfull \\[hv]box \(([-\d.]+)pt too (?:wide|high)\)([^\n]*(?:\n[^\n]*)?)',log):
        val=float(m.group(1));loc=re.search(r'(?:at lines?|detected at line)\s+(\d+)(?:--(\d+))?',m.group(2))
        over.append({'points':val,'source_lines':[int(loc.group(1)),int(loc.group(2) or loc.group(1))] if loc else [],'message':m.group(0)})
    missing=[line for line in log.splitlines() if 'Missing character:' in line or 'not loadable' in line or 'Font shape' in line]
    undefined=[line for line in log.splitlines() if ('undefined' in line.lower() and ('Reference' in line or 'Citation' in line or 'LaTeX Warning' in line))]
    return {'overfull_boxes':over,'overfull_above_2pt':[r for r in over if r['points']>2.0],
            'missing_fonts_or_glyphs':missing,'undefined_warning_lines':undefined,
            'rerun_requested':'Rerun to get cross-references right' in log or 'Rerun to get /PageLabels entry' in log}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--papers',nargs='*',default=PAPERS);parser.add_argument('--cycle',default='01');parser.add_argument('--passes',type=int,default=1)
    args=parser.parse_args()
    env=os.environ.copy();env['TEXMFHOME']=str(ROOT/'build/texlive-luatex/usr/share/texlive/texmf-dist');env['TEXMFCACHE']='.'
    if not Path(env['TEXMFHOME']).exists():
        deb=next((ROOT/'code/dependencies').glob('texlive-luatex_*.deb'))
        subprocess.run(['dpkg-deb','-x',str(deb),str(ROOT/'build/texlive-luatex')],check=True)
    dest=ROOT/'code/outputs'/('build_'+args.cycle);dest.mkdir(parents=True,exist_ok=True)
    def build(paper):
        name='S6_SERIES_GRIND_'+paper;started=time.monotonic();ret=0
        for attempt in range(args.passes):
            with (dest/(name+f'_pass{attempt+1}.stdout')).open('w') as f:
                proc=subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error','-file-line-error',name+'.tex'],cwd=ROOT,env=env,stdout=f,stderr=subprocess.STDOUT)
            ret=proc.returncode
            if ret:break
        logfile=ROOT/(name+'.log');log=logfile.read_text(errors='replace') if logfile.exists() else ''
        if logfile.exists():shutil.copyfile(logfile,dest/logfile.name)
        labels=aux_labels((ROOT/(name+'.aux')).read_text(errors='replace')) if (ROOT/(name+'.aux')).exists() else {}
        (ROOT/f'analysis/current_labels_{paper}.json').write_text(json.dumps(labels,indent=2,ensure_ascii=False))
        result={'paper':paper,'returncode':ret,'seconds':round(time.monotonic()-started,2),'labels':len(labels),**diagnostics(log)}
        pdf=ROOT/(name+'.pdf')
        if pdf.exists():
            import fitz
            doc=fitz.open(pdf);result.update(pages=len(doc),bookmarks=len(doc.get_toc()))
        (dest/(name+'_diagnostics.json')).write_text(json.dumps(result,indent=2,ensure_ascii=False))
        print(json.dumps({k:result.get(k) for k in ['paper','returncode','seconds','pages','labels','bookmarks']}|{'overfull_above_2pt':len(result['overfull_above_2pt']),'missing_fonts_or_glyphs':len(result['missing_fonts_or_glyphs']),'undefined_warning_lines':len(result['undefined_warning_lines'])}),flush=True)
        return result
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:results=list(pool.map(build,args.papers))
    (dest/'summary.json').write_text(json.dumps(results,indent=2,ensure_ascii=False))

if __name__=='__main__':main()
