"""One-time guarded integration of the received weighted OS45 proof."""
from pathlib import Path
import copy,datetime,hashlib,json
R=Path(__file__).resolve().parents[1]
P=R/'audit_corrections/III_equivariant_09'
out=R/'analysis/III_refined_class_integration_09.json'
assert not out.exists()
sha=lambda b:hashlib.sha256(b).hexdigest()
expected={
 'D253_refined_class_addition.tex':'2fb3c5c9532bd78281d07ebb16e38d62e10e9711aaff6d2253e2e376bcf0a13b',
 'D253_guarded_replacements.json':'754a52fc3003a935a58c50fc8fbbf7906c4a46b310e5efa02b7cb2e3ba4d8ef0',
 'D253_frontmatter_map_proposal.json':'02270dd2aa5f9317f1a187bba8608ea17363c2318ad072aaeaad3c0f1dfb82cd',
 'D253_source_metadata_proposal.json':'c36af9f3bff47f1ff499a199b01f04db2169045f1331beb7e70cfc7c8797110e'}
for name,h in expected.items():assert sha((P/name).read_bytes())==h,name
assert sha((P/'independent_full_derivation.md').read_bytes())=='2f0e2955c56447e6e5f9d81184ab0ce02bae85cc75be00c50d32776154faf47c'
assert sha((R/'audit_sign/III_equivariant_09/statement_first_derivation.md').read_bytes())=='b8ebe13a13fd8caea0fc942167a7c277becf7eb4486ddfa2b966bd1217b69724'
assert sha((R/'audit_sign/III_equivariant_09/MV_oddness_addendum.md').read_bytes())=='30b517ad21b96c89a258bb2d47025c38d98337625904b7a244811201ec732c2c'
patch=json.loads((P/'D253_guarded_replacements.json').read_text())
original={};pending={};changes=[]
def get(name):
 if name not in pending:
  original[name]=(R/name).read_text();pending[name]=original[name]
 return pending[name]
for q in patch['patches']:
 name=q['file'];t=get(name)
 assert t.count(q['old_text'])==q['expected_count'],(name,q['reason'])
 pending[name]=t.replace(q['old_text'],q['new_text'])
 changes.append(q)
# This is a publication wording correction, with identical marked section.
name='parts/III.body.linked.tex';old='The origin\nis the received section $O$';new='The origin\nis the marked section $O$'
assert pending[name].count(old)==1
pending[name]=pending[name].replace(old,new)
changes.append(dict(file=name,old_text=old,new_text=new,reason='Use the geometric marking in publication prose.'))
fm=json.loads((P/'D253_frontmatter_map_proposal.json').read_text())
name=fm['file'];data=json.loads(get(name));match=[v for v in data['main_theorems'] if v['letter']==fm['letter']]
assert len(match)==1 and match[0]==fm['old_entry']
data['main_theorems']=[fm['new_entry'] if v['letter']==fm['letter'] else v for v in data['main_theorems']]
pending[name]=json.dumps(data,indent=2)+'\n'
metadata=json.loads((P/'D253_source_metadata_proposal.json').read_text())
name=metadata['target'];data=json.loads(get(name))
for e in metadata['entries']:
 assert data.get(e['key'])==e['old_value'],e['key']
 data[e['key']]=e['new_value']
pending[name]=json.dumps(data,indent=2,ensure_ascii=False)+'\n'
name='analysis/additional_references.bib';t=get(name)
assert 'Redden2011StringStructures' not in t
bib=(R/'audit_sign/III_equivariant_09/Redden_bibliography_proposal.bib').read_text().rstrip()
assert bib.endswith('}')
bib=bib[:-1].rstrip()+',\n  verification = {verified at listed scope},\n  source_note = {arXiv version2, Definition2.15, Proposition2.16 and Remark2.17 pp11--12, Section6.1 pp24--25 freshly opened by the sign reviewer; root also read Section6.1. Exact quaternionic unit and adjoint index-two maps, with source-opening receipts retained.}\n}\n'
pending[name]=t+'\n'+bib
name='code/assemble_series.py';t=get(name)
old='profiles, including the extra torsion of free OS49 caps. Finally, an\nexplicit conifold transition'
new='profiles, including the extra torsion of free OS49 caps. For the specified\nweighted OS45 member, an embedded odd Hopf sphere and its explicit Borel\npair determine the refined characteristic class to be zero. Finally, an\nexplicit conifold transition'
assert t.count(old)==1
pending[name]=t.replace(old,new)
changes.append(dict(file=name,old_text=old,new_text=new,reason='State the exact new invariant in the abstract.'))
name='audit_root/row_assessments.json';data=json.loads(get(name));before=copy.deepcopy(data['maps:src:D.2.53'])
v=data['maps:src:D.2.53']
v['confidence_state']='Complete current weighted OS45 invariant proof; refined class zero at the fixed marked scope'
v['confidence_line']+=' The new complete actual source-line/collar/sphere proof and integral Borel framing computation now determine P_ref=0. Independently frozen Borel derivations, full receiving review, the exact mod-two Wang/MV repair, 47 root frame checks, 34 collar checks and 4 explicit integral splitting checks agree. The full seven-step proof is integrated with exact primary source loci.'
v['independent_routes']+=['Two independent Borel/relative framing derivations frozen before exchange; actual collar receiving comparison after their freezes.','Explicit integral Wang splitting and mod-two coefficient detector repair the odd-generator inference without changing frozen bytes.']
v['remaining_risk']='No refined0/4 mathematical gate remains for the exact weighted OS45/default P=2G,Q=8G member with weights(2,0,0,0,0), prescribed triangular Mumford caps and ordinary clutch1. Broader D2.4 families remain open. Whole-row before-reading/prerequisite eligibility retains its original exposure scopes; current source/layout verification follows integration.'
v['format_check']='Complete seven-step new proof, exact main-F scope and seven-step outline, abstract and final-part disposition are integrated by guarded changes. Current build and actual image checks pending.'
v['layout_check']='Pending the rebuild of the new refined-class proof and changed abstract/main/final passages; earlier receipts retain their exact PDF hashes.'
data['maps:src:D.2.4']={
 'confidence_state':'Open general classification with the exact weighted OS45 refined subproblem completed',
 'confidence_line':'D2.53 now proves P_ref=0 for its fixed marked weighted member by the full embedded odd sphere, actual unit/collar and integral Borel/reference maps. This is a strict reduction of the broader final-part gate.',
 'remaining_risk':'Other prescribed star-log families and h>1 original-additive-cap torsion markings remain. The exact weighted OS45/default member of D2.53 has its full refined invariant computed; whole-row classification is not closed.',
 'completion_state':'pending; broader marked classification and remaining original-cap columns open'}
pending[name]=json.dumps(data,indent=2)+'\n'
for name,t in pending.items():(R/name).write_text(t)
receipt={
 'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'decision':'Accepted and integrated at exact weighted OS45 scope; no whole-row completion or broad D2.4 closure awarded.',
 'inputs':expected,'changes':changes,'main_map':fm,'source_metadata':metadata,
 'D253_assessment_before':before,'D253_assessment_after':data['maps:src:D.2.53'],
 'files':{name:{'before_sha256':sha(original[name].encode()),'after_sha256':sha(t.encode())} for name,t in pending.items()},
 'root_reading':'Full corrections freeze, sign freeze, receiving report, exact MV addendum and all code certificates read. Complete publication proof read, then changed Wang/punctured-frame paragraphs read. Independent primary openings retain their named scopes.',
 'pending':'Rebuild, references, and actual current page QA.'}
out.write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'integrated_files':len(pending),'source_guards':len(patch['patches']),'receipt':str(out.relative_to(R))}))
