"""Integrate the completely audited full OS49 holomorphic endpoint theorem."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil
root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
m=json.loads((root/'records/k79_export_manifest.json').read_text())
q=json.loads((root/'records/k79_standalone_visual_qa.json').read_text())
r=json.loads((root/'records/root_audit_os49_full_automorphisms_working.json').read_text())
s=root/'notes/part3_os49_full_automorphisms.tex'
sha=hashlib.sha256(s.read_bytes()).hexdigest()
assert sha==m['include_sha256']==q['tex_sha256']
assert m['source_sha256']==r['source_sha256']
assert q['status']=='PASS'
archive=root/'records/checkpoint19_prior_master62';archive.mkdir(exist_ok=False)
for name in ('S6_06_BLIND_paper.pdf','S6_06_BLIND_paper.log',
             'notes/part3.tex','notes/part3_remaining_return_obligations.tex',
             'code/update_report.py','code/part3/results_mapping.json'):
    dest=archive/name;dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(root/name,dest)
p=root/'notes/part3.tex';text=p.read_text()
assert '\\input{notes/part3_os49_full_automorphisms.tex}' not in text
p.write_text(text+'\n\\input{notes/part3_os49_full_automorphisms.tex}\n')
p=root/'notes/part3_remaining_return_obligations.tex';text=p.read_text()
old='''Remaining parts of item 3.4 include the further ordinary and
singular-site sectors beyond that scope, the remaining marked
source-moduli loops, and unmarked endpoint sectors. No value is
assigned here to those sectors.'''
new=r'''K79 proves that the full holomorphic automorphism group of every
fixed OS49 sphere datum in this scope is the physical
\(\mathbb C^*\), with its actual isotopy. For a prescribed scalar
path and a holomorphic endpoint, its full root and affine squares
give \(L=Nk\), and its return is \(N S_k(P)\). Thus this entire
fixed-source holomorphic endpoint scope is completed.
Remaining parts of item 3.4 include the further ordinary and
singular-site sectors beyond that scope, the remaining marked
source-moduli loops, and endpoint sectors outside this completed
fixed-source OS49 calculation. No value is assigned here to those
remaining sectors.'''
assert old in text;text=text.replace(old,new)
old='''For arbitrary unmarked endpoints the endpoint automorphism
must be carried through the lattice, physical circle and
finite-cap data before its return can be combined with
these values. The corresponding sectors have not been
assigned a value by changing the marking silently.'''
new=r'''K79 now carries every holomorphic endpoint of the stated fixed
OS49 sphere data through its full lattice, local inverse, physical
circle and finite-cap groupoid. It gives the same return for all
specified endpoints at each allowed scalar winding. For the other
remaining source data, those endpoint maps still require their
own such comparison; no value is assigned by changing a marking.'''
assert old in text;text=text.replace(old,new)
p.write_text(text)
p=root/'code/update_report.py';text=p.read_text()
text=text.replace('P3K.5–P3K.78; exact corrected scopes below',
                  'P3K.5–P3K.79; exact corrected scopes below')
old='K75 retains the source-zero global attachment, further ordinary/singular-site scopes, marked source-moduli loops and unmarked endpoints.'
new='K79 proves the full holomorphic automorphism group C* for all these fixed OS49 sphere data, using actual base recovery, the integral centralizer, local inversions and the full affine torsor obstruction. Every specified holomorphic scalar endpoint has winding L=Nk and return N S_k(P). K75 retains the source-zero global attachment, further ordinary/singular-site scopes, marked source-moduli loops and endpoint sectors outside this completed fixed-source OS49 scope.'
assert old in text;text=text.replace(old,new)
p.write_text(text)
p=root/'code/part3/results_mapping.json';mapping=json.loads(p.read_text())
if not any(x.get('id')=='P3K.79' for x in mapping.get('additional_source_loop_results',[])):
    mapping.setdefault('additional_source_loop_results',[]).append({
      'id':'P3K.79','status':'Proved',
      'statement':'Full physical C* automorphism group and all holomorphic scalar endpoints of the fixed OS49 sphere data; L=Nk and return N S_k(P).',
      'proof':'notes/part3_os49_full_automorphisms.tex',
      'certificate':'code/part3/os49_full_automorphisms.json',
      'audit':'records/root_audit_os49_full_automorphisms_working.json',
      'independent_audit':'records/checks_audit_os49_full_automorphisms.json'})
p.write_text(json.dumps(mapping,indent=2)+'\n')
(root/'records/k79_promotion.json').write_text(json.dumps({
 'utc':now,'status':'PROMOTED_AFTER_TWO_PROOF_AUDITS_AND_FULL_STANDALONE_QA',
 'statement':'P3K.79','tex_sha256':sha,'working_source_sha256':r['source_sha256'],
 'archive':str(archive.relative_to(root)),'master_to_build':63,
 'pdf_qa':'records/k79_standalone_visual_qa.json'
},indent=2)+'\n')
print('K79 integrated; prior master62 and current-scope sources preserved.')

