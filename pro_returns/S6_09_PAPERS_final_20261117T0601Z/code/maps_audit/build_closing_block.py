"""Transfer full PUSH C.3.5 to Paper I, keeping mathematical/provenance scope."""
from pathlib import Path
import re,json,hashlib
R=Path('/workspace/scratch/037cd144174c');O=R/'deliverables/work/maps_audit'
p=R/'sources/returns/S6_02_PUSH/sections/C_closing_cocycle.tex';s=p.read_text();original=s
s=s.replace(r'\begin{proposition}[C.3.5 (Known formula, with proved comparison): the closing translation]',
            r'\begin{proposition}[The coherent closing translation]\label{push:src:C.3.5}')
s=s.replace('Fix the standard twists and all root and cusp markings of R2.',
            r'Fix the standard twists and the root and cusp markings of Proposition~\ref{fam:src:A.3.1}.')
s=s.replace('with the orientation convention of C.1.1.',
            r'with $w=e^{-\pi i c}$ and positive loops in the $w$-plane.')
s=s.replace('Any difference from the fixed R2 choice is a scalar automorphism,',
            r'Any difference from the fixed even-shift choice of Proposition~\ref{fam:src:A.3.1} is a scalar automorphism,')
s=s.replace(r'which lies in its connected \(\mathbb C^*\).',
            r'which lies in its connected $\mathbb C^*$ by Proposition~\ref{fam:src:B.4.1}.')
s=s.replace('This patching has not been established. The',
            'The separate scalings do not supply a patched isotopy. The')
s=s.replace(r'\path{code/d_push_monodromy.py} and',
            r'\path{code/maps_audit/PUSH/code/d_push_monodromy.py} and')
s=s.replace(r'\path{code/d_push_closing.py}; these are symbolic checks of the',
            r'\path{code/maps_audit/PUSH/code/d_push_closing.py}, run with \texttt{python3} followed by the indicated path; these are symbolic checks of the')
local=re.findall(r'\\label\{([^}]+)\}',original)
for lab in local:
 s=s.replace('{'+lab+'}','{mapsI:closing:'+lab+'}')
out=O/'paperI_closing_cocycle.tex';out.write_text(s)
meta={'source_run':'S6_02_PUSH','source_id':'C.3.5','source_file':str(p.relative_to(R)),
 'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'paper':'I',
 'output_file':str(out.relative_to(R)),'output_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
 'printed_label':'push:src:C.3.5','kind':'Known formula; full rederivation and actual chart comparison',
 'wording_vs_source':'Full statement and proof preserved. R2 and C.1.1 pointers replaced by internal family labels and explicit loop convention. Historical lack-of-patching sentence restricted to the unsuccessful separate-logarithm construction; no claim that the later smooth monodromy question remains open.',
 'recorded_checks':'Prior final intake did not claim to read this full proof. Expert cusp-origin concern and its later resolution remain separately recorded in check_events.json.',
 'your_check':{'reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date':'2026-11-17',
 'scope':'Full proof read, exact finite and ordinary affine defects rederived, cusp unit versus scalar representative and gamma deck sign checked, coherence correction verified. Both exact SymPy programs reread and rerun successfully. Actual cusp origin reconstructed from FAMILY periods; independent parent rederivation also recorded.',
 'evidence':['deliverables/code/maps_audit/PUSH/code/d_push_closing.audit_rerun.txt','deliverables/code/maps_audit/PUSH/code/d_push_monodromy.audit_rerun.txt','deliverables/work/maps_audit/closing_origin_check.tex']},
 'credit':{'source':'DGKX version 1', 'locators':['p2:prop:global-even-shift; source lines 10364–10746','p2:prop:raw-shift-defect, p2:eq:quadratic-strictification and p2:prop:strict-even-shift-action; source lines 11863–11955'],
 'status':'Original attached source opened; formula and coherent correction found, with complete chart agreement. Credited as known, not new.'},
 'remaining_dependencies':['The fixed FAMILY period and finite/cusp constructions','Connected scalar automorphism group, Proposition fam:src:B.4.1'],
 'route_reason':'Holomorphic gluing and coherent family translations are prerequisites for PUSH B.4.18 and B.4.24 in Paper I. Paper III cites this theorem for its downstream smooth monodromy arguments.'}
(O/'paperI_closing_cocycle_manifest.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
print('Saved full C.3.5:',len(s),'characters; label',meta['printed_label'])
