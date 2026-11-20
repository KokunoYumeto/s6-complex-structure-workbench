"""Print the actual UN13 certificate and exact relation of the comb cup maps."""
from pathlib import Path
import datetime, hashlib, json, re

R=Path(__file__).resolve().parents[1]
path=R/'parts/II.body.linked.tex'; before=path.read_text(); after=before
packets=['audit_sign/UN13_current_certificate_guard_08.json','audit_root/II_comb_dual_cup_map_guard_08.json']
receipts=[]
for packet_path in packets:
    p=R/packet_path; data=json.loads(p.read_text())
    guards=data.get('guards',[data])
    for g in guards:
        old=g.get('old_text',g.get('old')); new=g.get('new_text',g.get('new'))
        assert after.count(old)==1,(packet_path,g.get('label'))
        after=after.replace(old,new,1)
    receipts.append({'path':packet_path,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'guards':guards})
assert re.findall(r'\\(?:tag|label)\{[^}]+\}',before)==re.findall(r'\\(?:tag|label)\{[^}]+\}',after)
path.write_text(after)
record={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'before_sha256':hashlib.sha256(before.encode()).hexdigest(),'after_sha256':hashlib.sha256(after.encode()).hexdigest(),
 'guards':receipts,
 'second_reading':'audit_sign/II_comb_dual_cup_receiving_check_08.md',
 'scope':'UN13 retains its complete thirteen-step mathematical proof and uses the executed321-check current certificate. The actual comb maps are related by the explicit wedge/dual-extension morphism, including its sign and exact invariant pushforward. No period section or bundle splitting has been supplied; inv:E2.3 remains open and this reformulation supplies no strict main-gate movement.',
 'pending':'Assembly, clean build31, exact current-reference audit, and actual changed-page views.'}
(R/'analysis/UN13_and_comb_map_integration_08.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'guards':2,'file':'parts/II.body.linked.tex'}))
