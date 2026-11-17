#!/usr/bin/env python3
from pathlib import Path
import subprocess,re,json,datetime
root=Path(__file__).resolve().parents[2]
p=root/'notes/part3_liu_rollenske_parameter.md'
s=p.read_text().replace('Status: complete proof, submitted for independent audit.','Status: Proved after the root’s complete four-section independent audit.')
s=s.replace('advertised punctured \\(u\\)-disc','punctured \\(u\\)-disc with these fixed data')
p.write_text(s)
statement=s[s.index('## Statement')+len('## Statement'):s.index('## 1.')]
body=s[s.index('## 1.'):]
def convert(t):
 t=re.sub(r'`([^`]+)`',lambda m:r'\path{'+m.group(1)+'}' if '/' in m.group(1) else r'\texttt{'+m.group(1).replace('_',r'\_')+'}',t)
 t=re.sub(r'(?m)^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',t)
 return subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex','-t','latex','--wrap=preserve'],input=t,text=True,capture_output=True,check=True).stdout
out=r'\subsection{The literal Liu--Rollenske scalar and its double cover}'+'\n'+r'\begin{statement}{P3K.36}{Proved}'+'\n'+convert(statement)+'\n'+r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+convert(body)+'\n'+r'\end{proof}'+'\n'
(root/'notes/part3_liu_rollenske_parameter.tex').write_text(out)
preamble=(root/'code/part3/k34_standalone.tex').read_text().split(r'\begin{document}')[0]
(root/'code/part3/k36_standalone.tex').write_text(preamble+'\n'+r'\begin{document}'+'\n'+r'\input{notes/part3_liu_rollenske_parameter.tex}'+'\n'+r'\end{document}'+'\n')
mapping={'statement':'P3K.36','status':'Proved','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'proof':'notes/part3_liu_rollenske_parameter.tex','audit':'Root complete four-section audit PASS','own_value':{'literal_scalar':'u in B_u=u B_0','one_positive_u_turn':'No holomorphic endpoint: reduced multiple-fibre Albanese Q changes to -Q and j changes.','corrected_parameter':'u=w^2, minimal degree2','corrected_pair':[-3,-12],'relative_pair':[3,0],'vertical_fan_class':0,'all_fan_class':'3*(S-1)*(S-3)/8 mod28'},'certificate':'code/part3/liu_rollenske_parameter.py','primary_safe_locator':'Supplied Liu–Rollenske S6_arxiv.tex lines85–88; central-torus Corollary and Definition def: choice of a; no commented material used.'}
(root/'code/part3/liu_rollenske_parameter_results_mapping.json').write_text(json.dumps(mapping,indent=2)+'\n')
print('Exported notes/part3_liu_rollenske_parameter.tex and standalone; master untouched.')


# BEGIN POST-CHECKPOINT15 SCALAR-SCOPE RESTORATION
import importlib.util as _scalar_scope_importlib
from pathlib import Path as _ScalarScopePath
_scalar_scope_root = _ScalarScopePath(__file__).resolve().parents[2]
_scalar_scope_spec = _scalar_scope_importlib.spec_from_file_location(
    "_scalar_dependency_scope",
    _scalar_scope_root / "code/part3/scalar_dependency_scope.py")
_scalar_scope_module = _scalar_scope_importlib.module_from_spec(_scalar_scope_spec)
_scalar_scope_spec.loader.exec_module(_scalar_scope_module)
_scalar_scope_module.postprocess_generated(
    ['code/part3/liu_rollenske_parameter_results_mapping.json'], ['notes/part3_liu_rollenske_parameter.tex'], origin='code/part3/export_liu_rollenske_parameter.py')
# END POST-CHECKPOINT15 SCALAR-SCOPE RESTORATION
