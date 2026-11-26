from pathlib import Path
import datetime, hashlib, json, shutil, subprocess
import S6_SERIES_PUBLISH_build as build_runtime
R=Path(__file__).resolve().parents[1]
src=R.parent/'S6_GRIND_6_literature/papers/arXiv_2610.10451_Viaclovsky_combs_src'
dest=R.parent/'temporary_root_SV_primary';dest.mkdir(exist_ok=True)
stem='Viaclovsky_Comb_S6_Draft_October_7_2026'
if (dest/'build_1.out').exists() and not (dest/'format_unavailable.out').exists():
    shutil.copyfile(dest/'build_1.out',dest/'format_unavailable.out')
build_runtime.ROOT=dest
env=build_runtime.environment('pdflatex')
for suffix in ['.tex','.bbl']:shutil.copyfile(src/(stem+suffix),dest/(stem+suffix))
runs=[]
for k in range(2):
    p=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','-no-shell-escape',stem+'.tex'],cwd=dest,env=env,capture_output=True,text=True)
    (dest/f'build_{k+1}.out').write_text(p.stdout+p.stderr)
    runs.append({'run':k+1,'exit':p.returncode})
    assert p.returncode==0,p.stdout[-3000:]
pdf=dest/(stem+'.pdf')
subprocess.run(['pdftotext','-layout',str(pdf),str(dest/'primary.txt')],check=True)
rec={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source':str(src/(stem+'.tex')),
 'source_sha256':hashlib.sha256((src/(stem+'.tex')).read_bytes()).hexdigest(),
 'edition':'supplied arXiv2610.10451v1 source, October7 2026; byte identity with official retrieved source is recorded in the inherited retrieval receipt',
 'pdf':str(pdf),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'build_runs':runs,
 'official_pdf_open_attempts':[{'url':'https://arxiv.org/pdf/2610.10451','web_ref':'turn384392134view0','result':'DisabledError'},{'url':'https://arxiv.org/pdf/2610.10451v1','web_ref':'turn410266146view0','result':'DisabledError'}],
 'initial_failure':'Default runtime lacked pdflatex.fmt. The existing standalone build environment() supplies generated format and font-map files in the temporary primary-build directory; source unchanged.',
 'publication_page_reading_credit':0,'primary_page_image_readings':[]}
out=R/'agents/continuation2_root/01SV/S6_SERIES_PUBLISH_II_root_01SV_primary_build.json'
assert not out.exists();out.write_text(json.dumps(rec,indent=2)+'\n')
print(json.dumps(rec,indent=2))
