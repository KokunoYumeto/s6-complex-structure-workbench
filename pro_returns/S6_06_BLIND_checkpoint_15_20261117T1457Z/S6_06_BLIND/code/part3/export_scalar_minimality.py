#!/usr/bin/env python3
from pathlib import Path
import datetime,json,re,subprocess

root=Path(__file__).resolve().parents[2]
source=root/'notes/part3_scalar_minimality_working.md'
s=source.read_text()
s=s.replace('Status: complete proof and exact certificate, submitted for independent\naudit. No automorphism mapping class is inferred here.',
            'Status: Proved after complete root and independent fourfold audits.\nNo automorphism mapping class is inferred here.')
source.write_text(s)
statement=s.split('## 1. Statement and the actual parameter being tested\n',1)[1].split('## 2.',1)[0]
body='## 2.'+s.split('## 2.',1)[1]
proof_body, certificate_body = body.split('## 7. Executed certificate and complete branch coverage',1)
certificate_body='## 7. Executed certificate and complete branch coverage'+certificate_body

def convert(t):
    t=re.sub(r'`([^`]+)`',lambda z:r'\path{'+z.group(1)+'}' if '/' in z.group(1)
             else r'\texttt{'+z.group(1).replace('_',r'\_')+'}',t)
    t=re.sub(r'(?m)^## (.+)$',lambda z:r'\par\medskip\noindent\textbf{'+z.group(1)+r'}\par\nobreak',t)
    return subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex',
                            '-t','latex','--wrap=preserve'],input=t,text=True,
                           capture_output=True,check=True).stdout

out=(r'\subsection{Intrinsic minimal scalar winding}'+'\n'
     +r'\begin{statement}{P3K.38}{Proved}'+'\n'+convert(statement)
     +r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+convert(proof_body)
     +r'\end{proof}'+'\n'+convert(certificate_body))
(root/'notes/part3_scalar_minimality.tex').write_text(out)
preamble=(root/'code/part3/k34_standalone.tex').read_text().split(r'\begin{document}')[0]
(root/'code/part3/k38_standalone.tex').write_text(preamble+'\n'+r'\begin{document}'+'\n'
    +r'\input{notes/part3_scalar_minimality.tex}'+'\n'+r'\end{document}'+'\n')
certificate=json.loads((root/'code/part3/scalar_cap_minimality.json').read_text())
mapping={'statement':'P3K.38','status':'Proved','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
         'proof':'notes/part3_scalar_minimality.tex','audit':'Full root and independent fourfold PASS',
         'whole_fibre_catalogue':{'branches':30,'least_positive_scalar_winding':'M/b',
             'actual_closed_parameter':'lambda=w^(M/b)','arbitrary_biholomorphic_endpoint_scope':True,
             'retained_data':['aG central Picard point','all n_i','all finite line characters','all fixed order-one clutches','every allowed fan'],
             'branch_values':[{'id':b['id'],'minimum':b['minimum_scalar_winding']}
                              for b in certificate['branches']]},
         'component_supported_OS49':{'m':'3k','norms':'n=+/-1','least_positive_scalar_winding':'k',
              'actual_closed_parameter':'lambda=w^k','actual_Picard_point':'G_0 of order3'},
         'automorphism_mapping_classes_inferred':False,
         'certificate':'code/part3/scalar_cap_minimality.py'}
(root/'code/part3/scalar_cap_minimality_results_mapping.json').write_text(json.dumps(mapping,indent=2)+'\n')
print('Exported full P3K.38, exact mapping, and standalone wrapper; master untouched.')
