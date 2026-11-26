#!/usr/bin/env python3
"""Compile temporary before/proposed sources and verify every equation label."""
from pathlib import Path
from datetime import datetime,timezone
import csv
import hashlib
import importlib.util
import json
import re
import shutil
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
BDIR=ROOT/"agents/continuation2_B/D19"
OLDPRE="S6_SERIES_PUBLISH_II_B2_D19_"
OUT=ROOT/"records/S6_SERIES_PUBLISH_II_D19_rebase_02"
TMP=ROOT.parent/"temporary_root_D19_rebase_02"
PRE="S6_SERIES_PUBLISH_II_D19_rebase_02_"
def rec(p):
    b=p.read_bytes()
    return dict(path=str(p),sha256=hashlib.sha256(b).hexdigest(),bytes=len(b))
def save(name,d):
    (OUT/(PRE+name+".json")).write_text(json.dumps(d,indent=2,ensure_ascii=False)+"\n")
start=datetime.now(timezone.utc).isoformat()
previous=OUT/(PRE+"v1_tex_runs.json")
failure=OUT/(PRE+"v1_tex_format_failure.json")
if previous.exists() and not failure.exists():
    prior=json.loads(previous.read_text())
    if any(r["returncode"] for r in prior["runs"]):
        for r in prior["runs"]:
            old=Path(r["stdout"]["path"])
            copied=TMP/(old.stem+"_format_missing.stdout")
            shutil.copyfile(old,copied)
            r["stdout"]=rec(copied)
        prior["correction"]="Use the existing standalone build environment with its ROOT redirected to the temporary directory; canonical TeX runtime and source remain untouched."
        failure.write_text(json.dumps(prior,indent=2,ensure_ascii=False)+"\n")
# Read the established runtime helper, but direct every generated runtime file to TMP.
runtime_helper=ROOT/"code/S6_SERIES_PUBLISH_build.py"
spec=importlib.util.spec_from_file_location("d19_build_runtime",runtime_helper)
runtime=importlib.util.module_from_spec(spec);spec.loader.exec_module(runtime)
runtime.ROOT=TMP
existing_format=ROOT/"tex-runtime/web2c/pdflatex.fmt"
if existing_format.exists():
    (TMP/"tex-runtime/web2c").mkdir(parents=True,exist_ok=True)
    shutil.copyfile(existing_format,TMP/"tex-runtime/web2c/pdflatex.fmt")
tex_env=runtime.environment("pdflatex")
meta=json.loads((OUT/(PRE+"v1_source_and_verification.json")).read_text())
before=TMP/"S6_SERIES_PUBLISH_II_D19_before.tex"
after=TMP/"S6_SERIES_PUBLISH_II_D19_proposed.tex"
assert rec(before)["sha256"]==meta["source_sha256"]
assert rec(after)["sha256"]==meta["proposed_source_sha256"]
version=subprocess.run(["pdflatex","--version"],capture_output=True,text=True,check=True).stdout.splitlines()[0]
runs=(json.loads((OUT/(PRE+"v1_tex_runs.json")).read_text())["runs"]
      if "--reuse-existing-builds" in sys.argv else [])
if runs:
    assert len(runs)==4 and all(r["returncode"]==0 for r in runs)
    for r in runs:
        assert rec(Path(r["source"]["path"]))==r["source"]
for name,count in ([] if runs else [("before",1),("proposed",3)]):
    source=before if name=="before" else after
    for n in range(1,count+1):
        cmd=["pdflatex","-interaction=nonstopmode","-halt-on-error","-file-line-error",
             "-no-shell-escape","-output-directory",str(TMP),str(source)]
        a=datetime.now(timezone.utc).isoformat()
        run=subprocess.run(cmd,cwd=TMP,env=tex_env,capture_output=True,text=True)
        stdout=TMP/(source.stem+f"_pass{n}.stdout")
        stdout.write_text(run.stdout+"\n"+run.stderr)
        item=dict(source=rec(source),pass_number=n,start_utc=a,
                  end_utc=datetime.now(timezone.utc).isoformat(),
                  command=cmd,returncode=run.returncode,stdout=rec(stdout))
        runs.append(item)
        save("v1_tex_runs",dict(start_utc=start,engine=version,runs=runs,canonical_mutations=0))
        print(json.dumps(dict(name=name,pass_number=n,returncode=run.returncode)),flush=True)
        if run.returncode:
            print(run.stdout[-5000:],flush=True)
            raise SystemExit(run.returncode)
def labels(p):
    result={}
    spec=importlib.util.spec_from_file_location("d19_aux_groups",BDIR/(OLDPRE+"scan.py"))
    auxparser=importlib.util.module_from_spec(spec);spec.loader.exec_module(auxparser)
    for line in p.read_text().splitlines():
        if line.startswith(r"\newlabel{"):
            key,end,_=auxparser.group(line,len(r"\newlabel"))
            body,_,_=auxparser.group(line,end)
            number,end,_=auxparser.group(body,0)
            page,_,_=auxparser.group(body,end)
            raw=number
            while number.startswith("{"):
                value,end,_=auxparser.group(number,0)
                if end!=len(number):break
                number=value
            assert key not in result,key
            result[key]=dict(number=number,page=page,raw_number_tex=raw)
    return result
oldaux=before.with_suffix(".aux");newaux=after.with_suffix(".aux")
oldlabels=labels(oldaux);newlabels=labels(newaux)
with (OUT/(PRE+"v1_equation_map.tsv")).open() as f:
    rows=list(csv.DictReader(f,delimiter="\t"))
checks=[]
for row in rows:
    label=row["target_label"];actual=newlabels[label]
    assert actual["number"]==row["new_number"],(label,actual,row)
    for alias in filter(None,row["labels"].split(";")):
        assert newlabels[alias]["number"]==row["new_number"],alias
    old=oldlabels.get(label)
    if row["old_tag"]:
        for alias in filter(None,row["labels"].split(";")):
            assert oldlabels[alias]["number"]==row["old_tag"],(alias,oldlabels[alias],row["old_tag"])
    checks.append(dict(label=label,old_tag=row["old_tag"],
                      actual_old_number=old["number"] if old else row["old_tag"],
                      actual_new_number=actual["number"],new_page=actual["page"],
                      old_labels=row["labels"].split(";") if row["labels"] else [],
                      passed=True))
log=after.with_suffix(".log").read_text(errors="replace")
counts={
    "undefined_reference_warnings":len(re.findall(r"LaTeX Warning: Reference .*undefined",log)),
    "undefined_citation_warnings":len(re.findall(r"LaTeX Warning: Citation .*undefined",log)),
    "multiply_defined_label_warnings":len(re.findall(r"multiply defined",log)),
    "duplicate_destination_warnings":len(re.findall(r"destination with the same identifier",log)),
    "overfull_boxes":len(re.findall(r"Overfull \\[hv]box",log)),
    "missing_characters":len(re.findall(r"Missing character:",log)),
    "rerun_reference_warning":len(re.findall(r"Label\(s\) may have changed",log)),
}
for key in ["undefined_reference_warnings","undefined_citation_warnings",
            "multiply_defined_label_warnings","duplicate_destination_warnings",
            "missing_characters","rerun_reference_warning"]:
    assert counts[key]==0,(key,counts[key])
save("v1_tex_label_checks",checks)
result=dict(start_utc=start,end_utc=datetime.now(timezone.utc).isoformat(),engine=version,
    runtime_helper=rec(runtime_helper),
    runtime_format=rec(TMP/"tex-runtime/web2c/pdflatex.fmt"),
    before=rec(before),proposed=rec(after),runs=runs,
    before_aux=rec(oldaux),proposed_aux=rec(newaux),
    proposed_pdf=rec(after.with_suffix(".pdf")),proposed_log=rec(after.with_suffix(".log")),
    equation_labels_verified=len(checks),all_expected_equation_numbers_match=True,
    warning_counts=counts,final_publication_page_reading_credit=0,check_events_added=0,
    canonical_mutations=0,
    temporary_artifacts_policy="Full working source, build log, aux and PDF are outside current and are not checkpoint deliverables.")
save("v1_tex_verification",result)
print(json.dumps(dict(equation_labels_verified=len(checks),all_expected_equation_numbers_match=True,
                     warning_counts=counts,pdf=rec(after.with_suffix(".pdf"))),indent=2),flush=True)
