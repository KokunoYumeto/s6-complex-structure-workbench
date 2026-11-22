from pathlib import Path
import json, hashlib, datetime
from S6_SERIES_PUBLISH_editing import Editor

r=Path(__file__).resolve().parents[1]
p=r/'agents/i_analytic/S6_SERIES_PUBLISH_I_editorial_batch_a_guards.json'
d=json.loads(p.read_text())
ed=Editor('I')
rows=[]
for x in d['guards']:
    new=x['new']
    if x['id']=='IA-A-13':
        new=new.replace('That proof and\nits separate local argument are retained in the verification records.',
            'The verification records linked in Section~1.5 give this proof\nand its separate local argument.')
    ed.replace(x['old'],new,'D12',x['reason'],x['id'],count=x.get('expected_count',1))
    rows.append({'id':x['id'],'old_sha256':hashlib.sha256(x['old'].encode()).hexdigest(),
                 'new_sha256':hashlib.sha256(new.encode()).hexdigest(),
                 'root_comparison':'Read complete old/new guard text, including every mathematical estimate; read entire retained division-ladder proof before integration.'})
ed.replace(r'\newcommand{\Uses}[1]{\par\smallskip\noindent\textit{Uses:} #1.\par\smallskip}',
           r'\newcommand{\Uses}[1]{}','D10',
           'Suppress the remaining printed dependency header; dependency data is preserved in the check files and source.',
           'preamble:Uses')
ed.save()
(r/'records/S6_SERIES_PUBLISH_I_editorial_a_integration.json').write_text(json.dumps({
    'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'source_guards':str(p.relative_to(r)),
    'comparison':rows,
    'mathematical_dispositions':[
        'The finite-period difference is exactly -1-(3i/(2pi))log(4/3); its strict bounds follow from integrating 1/(1+x) and 3<pi<15/4.',
        'Coarse upper bounds are subsumed by the exact maximum. Original proof bodies and numerical corroborations remain in the removed-record artifact.',
        'The norm identity explicitly identifies N and mathcal N through the identical theta quotient and Gaussian; the modular lattice isomorphism is printed.',
        'The canonical maximum proof is the existing division-ladder proof. Its unique determinant/path/cusp and radius steps are incorporated.',
        'The interval and smaller-disc proofs are preserved outside the paper with all their original labels and tags pointing to the numbered verification remark.'
    ]},indent=2)+'\n')
