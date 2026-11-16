from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[3]
D=ROOT/'deliverables'; R=D/'records'
def read(p):
    p=R/p
    return p.read_text() if p.exists() else ''
parts=[read('root/preamble.tex'),read('root/front.tex')]
for agent in ['root','periods','cohomology','geometry_ends']:
    parts.append('\n% ===== '+agent+' source-preserving fragment =====\n')
    parts.append(read(agent+'/sections.tex'))
parts.append(read('root/back.tex'))
parts.append('\n\\appendix\n\\section{The workbench period-shift proof}\\label{app:workbench}\n')
parts.append(read('root/appendix_a.tex'))
parts.append('\n\\section{Re-derivations of known results}\\label{app:known}\n')
for p in ['root/appendix_b_periods.tex','cohomology/appendix_b_tangent.tex','geometry_ends/appendix_b_aut.tex']:
    parts.append(read(p))
parts.append('\n\\section{Sources, status, credit and notation}\\label{app:audits}\n')
parts.append(read('root/appendix_c.tex'))
parts.append(read('root/bibliography.tex'))
parts.append('\n\\end{document}\n')
text='\n'.join(parts)
# Cross-run bibliography aliases are pure reference-key substitutions.
text=text.replace('{DGKX26v1}','{DGKXv1}').replace('{DGKX26v2}','{DGKXv2}').replace('{ViaclovskyLog26}','{VL26}')
text=re.sub(r'\\dh\b',r'\\dhat',text)
text=text.replace('–','--').replace('—','---').replace('’',"'").replace('‘','`').replace('“','``').replace('”',"''")
(D/'S6_07_PAPER_paper.tex').write_text(text)
print('Master characters',len(text),'lines',len(text.splitlines()))
