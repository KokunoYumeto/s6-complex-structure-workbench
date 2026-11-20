"""Apply eight reviewed exact primary-credit and marked-topology guards."""
from pathlib import Path
import datetime,hashlib,json,re
R=Path(__file__).resolve().parents[1]
sources=['audit_sign/UN36_primary_credit_guards_08.json',
         'audit_corrections/V_exact_source_locators_guard_08.json',
         'audit_p119_fresh/receiving_guards_08.json']
before={};after={};receipt=[]
for file in sources:
    packet=json.loads((R/file).read_text())
    guards=packet['guards'] if isinstance(packet,dict) else packet
    for g in guards:
        target=g.get('file') or packet.get('target',packet.get('path'))
        if target not in before:before[target]=(R/target).read_text();after[target]=before[target]
        old=g.get('old_text',g.get('old'));new=g.get('new_text',g.get('new'))
        assert after[target].count(old)==1,(file,g.get('label',g.get('id')))
        after[target]=after[target].replace(old,new,1)
    receipt.append({'source':file,'sha256':hashlib.sha256((R/file).read_bytes()).hexdigest(),'guards':guards})
for file,s in after.items():
    assert re.findall(r'\\(?:tag|label)\{[^}]+\}',before[file])==re.findall(r'\\(?:tag|label)\{[^}]+\}',s),file
    (R/file).write_text(s)
a={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'guards':8,'receipts':receipt,
   'hashes':{p:{'before':hashlib.sha256(before[p].encode()).hexdigest(),'after':hashlib.sha256(after[p].encode()).hexdigest()} for p in before},
   'mathematical_scope':'The P1.19 addition supplies the actual invariant five-subtori, inverse-word edge coordinates and integral fibre-summand comparison. Its S locator is corrected to P1.1. Six other guards supply opened primary locators and the exact Stein/coherent-sheaf application.',
   'pending':'Assembly, build29, log inspection, reference audit and changed-page actual visual review.'}
(R/'analysis/primary_and_P119_integration_08.json').write_text(json.dumps(a,indent=2)+'\n')
print(json.dumps({'guards':8,'files':list(after)}))
