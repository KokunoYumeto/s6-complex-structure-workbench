"""Bind the completed, exposed D/E global comparison to unchanged final blocks."""
import datetime,hashlib,json,re
from pathlib import Path
from S6_SERIES_PUBLISH_editing import block
root=Path(__file__).resolve().parents[1]
sha=lambda b:hashlib.sha256(b).hexdigest()
source=root/'S6_SERIES_PUBLISH_I.tex';s=source.read_text()
old=(root/'agents/i_provenance/S6_SERIES_PUBLISH_I_provenance_source_7479a42f0c18.tex').read_text()
a=s.index(r'\hypertarget{outline-I-D}{}');b=s.index(r'\hypertarget{outline-I-F}{}',a)
outlines=s[a:b]
refs=list(dict.fromkeys(re.findall(r'\\hyperref\[([^]]+)\]',outlines)))
prior=json.loads((root/'records/S6_SERIES_PUBLISH_I_global_DE_candidate12_blocks.json').read_text())
expected={r['label']:r['current_sha256'] for r in prior['references']}
rows=[]
for label in refs:
    body=block(s,label)
    assert sha(body.encode())==expected[label], label
    rows.append({'label':label,'sha256':sha(body.encode()),'unchanged_since_full_comparison':True,
                 'immediate_proof_in_block':body.endswith(r'\end{proof}')})
# The cited Hodge proof follows a credited attribution paragraph, so bind it explicitly.
label='inv:A3.1';st=block(s,label);start=s.index(st);end=s.index(r'\end{proof}',start)+len(r'\end{proof}')
hodge=s[start:end];st0=block(old,label);start0=old.index(st0);end0=old.index(r'\end{proof}',start0)+len(r'\end{proof}')
hodge_old=old[start0:end0]
hodge_wording_old=('gives columns $p=1,2$ directly.  Statement \\ref{inv:A1.0} gives column zero,\n'
 'and Serre duality gives column three.  Thus the numbers are outputs\n'
 'of the sheaf computation.  Replacing $\\beta$ by $\\beta+c$ leaves')
hodge_wording_new=('gives columns $p=1,2$ directly.  \\Cref{inv:A1.0} gives column zero,\n'
 'and Serre duality gives column three. Replacing $\\beta$ by $\\beta+c$ leaves')
assert hodge_old.count(hodge_wording_old)==1
assert hodge==hodge_old.replace(hodge_wording_old,hodge_wording_new)
r={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
   'source_sha256':sha(source.read_bytes()),'main_statement_hashes':{label:sha(block(s,label,False).encode()) for label in ['series:I:D','series:I:E']},
   'complete_outlines_sha256':sha(outlines.encode()),'direct_receiving_blocks':rows,
   'credited_hodge_full_proof_sha256':sha(hodge.encode()),
   'credited_hodge_exact_wording_map':{'old':hodge_wording_old,'new':hodge_wording_new,'all_other_bytes_equal':True},
   'original_global_comparison':'records/S6_SERIES_PUBLISH_I_global_DE_comparison.json',
   'original_frozen_derivation':'records/S6_SERIES_PUBLISH_I_global_DE_freeze.json',
   'root_actual_review':'Complete current D/E headlines and all11 outline items read. All four changed direct-input diffs from candidate11 read in full. The full old/new Aut proof and the new residue/kernel lemma plus full scalar proof were read in their integration records. The credited Hodge proof was reopened in full; structure-sheaf inputs are the cited numbered setup with the explicitly supplied root-to-coarse maps.',
   'exact_changed_dependencies':[
       'D step1 now obtains sheaf surjectivity and the Hodge-number formulas from the preceding PI00 residue/kernel lemma. The same invariant generators and cup-product row give the unit argument; the evaluated scalar remains -i*C4/4. No rank or table entry changes.',
       'D coefficient atlas changes only two prose expressions. Its overlap morphisms, recursive coefficients and factor12 remain byte-identical.',
       'E higher-root proof replaces a negative clause by the positive assertion that the chosen generator is preserved; all root maps and norms remain.',
       'E automorphism proof sets c-prime=c and n=0 in the earlier period and finite-norm equations; gamma(N1*ell)=3gamma(ell)=-2l1 excludes a=-1. All sheaf extension, integral H1 and exponential-map steps remain in the full proof.',
       'The coherent-family and classification proofs were moved earlier. Their complete comparisons preserve the maps needed for local finiteness and miniversality.'
   ],
   'new_events':0,'scope':'Exposed final-form global consistency binding. Prior evidence groups and the existing computation scopes are reused. No additional independent, targeted or computation credit.'}
(root/'records/S6_SERIES_PUBLISH_I_global_DE_final_binding.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'source_sha256':r['source_sha256'],'outline_items':len(re.findall(r'\\item',outlines)),'receiving_blocks':len(rows),'new_events':0}))
