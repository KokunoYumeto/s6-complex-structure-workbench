#!/usr/bin/env python3
"""P3K.93 full proof export; leaves the master and result mapping untouched."""
from pathlib import Path
import re,json,hashlib,datetime
BASE=Path(__file__).resolve().parents[2]
src=BASE/'notes/part3_source_infinity_closed_formula_working.md'
text=src.read_text();text=text[text.index('## Statement'):]
protected={}
def hold(m):
 key='PROTECTEDSPAN'+str(len(protected))+'END';protected[key]=m.group(0);return key
text=re.sub(r'\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)',hold,text)
text=re.sub(r'^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'.}\par\nopagebreak[4]',text,flags=re.M)
text=re.sub(r'\*([^*\n]+)\*',lambda m:r'\emph{'+m.group(1)+'}',text)
text=re.sub(r'`([^`\n]+)`',lambda m:r'\texttt{'+m.group(1)+'}',text)
text=re.sub(r'(?<!\\)_',r'\\_',text)
text=re.sub(r'(?<!\\)\^',r'\\textasciicircum{}',text)
text=re.sub(r'(?<!\\)%',r'\\%',text)
for k,v in protected.items():text=text.replace(k,v)
cut=text.index(r'\par\medskip\noindent\textbf{IC.1.')
inc=(r'\subsection{The closed infinity formula and its complete image}'+'\n'+r'\begin{statement}{P3K.93}{Proved}'+'\n'+text[:cut]+r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+text[cut:]+r'\end{proof}'+'\n')
out=BASE/'notes/part3_source_infinity_closed_formula.tex';out.write_text(inc)
template=(BASE/'code/part3_fourfold/k86_standalone.tex').read_text().replace('part3_source_zero_normal_clutch.tex','part3_source_infinity_closed_formula.tex')
(BASE/'code/part3_fourfold/k93_standalone.tex').write_text(template)
rec={'id':'P3K.93','status':'Proved; full standalone visual QA pending','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'tex_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'root_and_peer_audit':'Full root and independent symbolic audits passed the complete paired-algorithm seed/reset proof and all exact image witnesses.','qa':'pending','master_modified':False}
(BASE/'records/k93_proof_assembly.json').write_text(json.dumps(rec,indent=2)+'\n')
print(json.dumps(rec,indent=2))
