#!/usr/bin/env python3
from pathlib import Path
import datetime,json,re,subprocess

root=Path(__file__).resolve().parents[2]
s=(root/'notes/part3_source_cusp_link.md').read_text()
statement=s[s.index('Let\n'):s.index('## 1.')]
body=s[s.index('## 1.'):]
def convert(t):
    t=re.sub(r'(?m)^## (.+)$',lambda z:r'\par\medskip\noindent\textbf{'+z.group(1)+r'}\par\nobreak',t)
    t=re.sub(r'(?<![\w{/])(code/[A-Za-z0-9_./-]+)',lambda z:r'\path{'+z.group(1).rstrip('.')+'}'+('.' if z.group(1).endswith('.') else ''),t)
    return subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex',
        '-t','latex','--wrap=preserve'],input=t,text=True,capture_output=True,check=True).stdout
out=(r'\subsection{The exact lifted link of the selected-cusp normalization}'+'\n'
     +r'\begin{statement}{P3F.55}{Proved}'+'\n'+convert(statement)
     +'\n'+r'This statement computes the specified local lifted link. Its comparison with a completed source-parameter family requires the separate ambient and circle-line morphisms.'+'\n'
     +r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+convert(body)+r'\end{proof}'+'\n'
     +r'\par\medskip\noindent\textbf{Verified primary sources.} '
     +r'\href{https://doi.org/10.4171/CMH/363}{N\'emethi--Pint\'er (2015)}, '
     +r'\S2.4, Propositions 4.2.2--4.2.3 and 6.1.1, and Theorem 9.1.6; '
     +r'\href{https://doi.org/10.1017/S0013091526101485}{Gauniyal--Turchin (2026)}, '
     +r'\S1, \S2.1, equations (4.1)--(4.3), and Theorem 4.1 with its preceding spherical-knot qualification; '
     +r'\href{https://arxiv.org/abs/math/0506356}{Takase, correction preprint (2005)}, '
     +r'Corollary 2.6 and Remark 4.2; '
     +r'\href{https://www.maths.ed.ac.uk/~v1ranick/tda/haefliger.pdf}{Haefliger (1966)}, '
     +r'Theorem 5.17, printed p.421, and its preceding compression proof; '
     +r'\href{https://doi.org/10.4310/HHA.2015.v17.n2.a15}{Sakai (2015)}, Proposition 6.8.'+'\n')
(root/'notes/part3_source_cusp_link.tex').write_text(out)
preamble=(root/'code/part3/k34_standalone.tex').read_text().split(r'\begin{document}')[0]
(root/'code/part3/f55_standalone.tex').write_text(preamble+'\n'+r'\begin{document}'+'\n'
    +r'\input{notes/part3_source_cusp_link.tex}'+'\n'+r'\end{document}'+'\n')
record={'statement':'P3F.55','status':'Proved','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'audit':'Root substantive sign audit and complete checks independent audit PASS',
        'proof':'notes/part3_source_cusp_link.tex','own_values':{'complex_smale':2,'stable_smale_L':-2,
            'double_linking':1,'Ekholm_E':2,'Whitehead_square_to_L':-4,'Omega_S2':'1/2','Haefliger':1,
            'GT_equals_corrected_Takase':True,'nonzero_normalization_test':{'sigma':-16,'e':0,'Omega_a':-24,'Omega_S2':6,'GT':2,'Takase':2}},
        'scope':'Explicit local lifted-link embedding only; no completed-threefold return inferred.',
        'certificates':['code/part3_root/source_cusp_link.py','code/part3_root/haefliger_normalization_bridge.py']}
(root/'code/part3/source_cusp_link_results_mapping.json').write_text(json.dumps(record,indent=2)+'\n')
print('Exported full P3F.55, local-only mapping, and standalone wrapper; master untouched.')
