#!/usr/bin/env python3
"""Recovered K86 export; no master input mutation."""
from pathlib import Path
import re,json,hashlib
BASE=Path(__file__).resolve().parents[2]
src=BASE/"notes/part3_source_zero_normal_clutch_working.md"
text=src.read_text()
(BASE/"notes/part3_source_zero_normal_clutch_complete.md").write_text(text)
text=text[text.index("## Statement"):]
blocks={}
def protect(m):
 key="PROTECTEDSPAN"+str(len(blocks))+"END";blocks[key]=m.group(0);return key
text=re.sub(r"\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)",protect,text)
text=re.sub(r"^## (.+)$",lambda m:r"\par\medskip\noindent\textbf{"+m.group(1)+r".}\par\nopagebreak[4]",text,flags=re.M)
text=re.sub(r"(?<!\\)_",r"\\_",text)
text=re.sub(r"(?<!\\)\^",r"\\textasciicircum{}",text)
for key,value in blocks.items():text=text.replace(key,value)
cut=text.index(r"\par\medskip\noindent\textbf{NC.1.")
inc=r"\subsection{The complete source-zero normal cap clutch}"+"\n"+r"\begin{statement}{P3K.86}{Proved}"+"\n"+text[:cut]+r"\end{statement}"+"\n"+r"\begin{proof}"+"\n"+text[cut:]+r"\end{proof}"+"\n"
out=BASE/"notes/part3_source_zero_normal_clutch.tex";out.write_text(inc)
template=(BASE/"code/part3_fourfold/k80_standalone.tex").read_text()
template=template.replace("part3_source_zero_reduced_attachment.tex","part3_source_zero_normal_clutch.tex")
(BASE/"code/part3_fourfold/k86_standalone.tex").write_text(template)
record={"id":"P3K.86","status":"Proved mathematical content; recovered transcription pending new standalone visual QA","reconstruction":True,"source_sha256":hashlib.sha256(src.read_bytes()).hexdigest(),"tex_sha256":hashlib.sha256(out.read_bytes()).hexdigest(),"original_qa":{"pages":9,"status":"PASS before outage","tex_sha256":"910f9f46cd8133cdab1ea1e89b71e603299bef7285a35cd6fac288b7655cae28","pdf_sha256":"48da617c553c4ea0707fa8665dde89e7a9fa949473852aacde9ab4cc99a570dd"},"new_qa":"pending","original_checkpoint19_overwrites":False}
(BASE/"records/k86_proof_assembly.json").write_text(json.dumps(record,indent=2)+"\n")
print(json.dumps(record,indent=2))

