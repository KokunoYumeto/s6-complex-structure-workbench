"""Repair the observed deferred list label without changing mathematical text."""
from pathlib import Path
import datetime, hashlib, json, re

R=Path(__file__).resolve().parents[1]
receipts=[]
for paper, expected in [('I',8),('III',4),('IV',5)]:
    p=R/f'parts/{paper}.body.linked.tex'
    before=p.read_text()
    hits=list(re.finditer(r'\\item\s+\\paragraph(?=\{)',before))
    assert len(hits)==expected,(paper,len(hits))
    after=re.sub(r'\\item\s+\\paragraph(?=\{)',lambda m:r'\item \textbf',before)
    if paper=='IV':
        assert after.count('proof 20 F.')==1
        after=after.replace('proof 20 F.','proof 20, substep 6.')
    assert re.findall(r'\\(?:tag|label)\{[^}]+\}',before)==re.findall(r'\\(?:tag|label)\{[^}]+\}',after)
    p.write_text(after)
    receipts.append({'paper':paper,'paragraph_markers_replaced':expected,
      'before_sha256':hashlib.sha256(before.encode()).hexdigest(),
      'after_sha256':hashlib.sha256(after.encode()).hexdigest(),
      'original_lines':[before.count('\n',0,m.start())+1 for m in hits]})

out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'observed_defect':'Build25 I page398 has both list labels 9 and 10 at y150.075: the paragraph heading immediately following item 9 defers that item label until item 10. Replace only the paragraph control word by bold text for every exact item/paragraph occurrence in the linked bodies.',
 'scope':'Seventeen identical TeX constructions repaired; the heading strings, mathematics, tags and labels are preserved. The remaining IV supporting-proof 20 F reference is transported to substep 6 using the recorded A-G to 1-7 bijection.',
 'receipts':receipts,'pending':'Rebuild and inspect the affected proof pages.'}
(R/'analysis/observed_step_label_repairs_07.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'repairs':17,'reference_repairs':1,'papers':[x['paper'] for x in receipts]}))
