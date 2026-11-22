from pathlib import Path
import datetime as dt, hashlib, json, subprocess
R=Path(__file__).resolve().parents[1]
source=R.parent/'S6_GRIND_6_literature/papers/arXiv_2610.00250v1_Du_Guo_Kusakabe_Xie_src/v5oka_maps_modifications_deformations.tex'
out=R.parent/'primary_continuation2_root_provenance'
out.mkdir(exist_ok=True)
record=R/'records/S6_SERIES_PUBLISH_II_DGKXv1_primary_build_01.json'
assert not record.exists()
argv=['pdflatex','-interaction=nonstopmode','-halt-on-error','-output-directory='+str(out),'-jobname=DGKXv1',str(source)]
passes=[]
for number in [1,2]:
    log=out/('DGKXv1_build_'+str(number).zfill(2)+'.stdout')
    run=subprocess.run(argv,cwd=source.parent,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    log.write_bytes(run.stdout)
    passes.append(dict(number=number,exit_code=run.returncode,stdout=str(log),stdout_sha256=hashlib.sha256(run.stdout).hexdigest()))
    if run.returncode: break
data=dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),primary_source=str(source),primary_source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),argv=argv,passes=passes,source_unchanged=True,check_events_added=0,page_reading_credit=0)
record.write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
