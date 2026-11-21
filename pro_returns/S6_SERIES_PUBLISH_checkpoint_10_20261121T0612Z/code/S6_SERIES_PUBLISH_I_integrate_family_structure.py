from pathlib import Path
import re,json,datetime,hashlib
from S6_SERIES_PUBLISH_editing import Editor
r=Path(__file__).resolve().parents[1];ed=Editor('I')
p=r/'agents/i_provenance/S6_SERIES_PUBLISH_I_family_structure_guards.json'
for x in json.loads(p.read_text())['changes']:
 ed.replace(x['old'],x['new'],'D15',x['reason'],x.get('statement_id','fam:src:A.3.1'))

# The normalization surface is P throughout these two local calculations;
# the same proof uses E for the rank-two vertical bundle.
starts=[r'Let $\nu:E\to W$ be the normalization, $E=\mathrm{dP}_6$',
 r'\item On the normalization $\nu:E=\mathrm{dP}_6\to W\subset X$,']
ends=[r'Thus the three dimensions are constant on every',
 r'\item The derivative $\partial_c\Pi=e\otimes\gamma$']
for a,b in zip(starts,ends):
 start=ed.text.index(a);end=ed.text.index(b,start);old=ed.text[start:end]
 new=re.sub(r'(?<![A-Za-z])E(?![A-Za-z0-9])','P',old)
 assert new!=old
 ed.replace(old,new,'D18','Use P for the normalization surface via the identical map nu:P=dP6→W; reserve E for the vertical rank-two bundle in the same argument. All sheaves, maps, pairings and dimensions are transported by this notation identity.','push:src:E.3.1' if a==starts[0] else 'push:src:E.2.1')
ed.save()
receipt={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'guard_file':str(p.relative_to(r)),'guard_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'source_sha256':hashlib.sha256(ed.text.encode()).hexdigest(),'scope':'Root read all moved proper-family proof passages, the full old/new split comparison and the coherent-descent text. Exact agent comparison retains the original coherent steps byte-for-byte; the connector equality is explicit. Root notation substitutions identify the same normalization morphism with the name P, without altering the objects or maps. No additional independent event.','labels_and_tags':'Every preexisting label and target retained exactly once; Editor invariant checks passed.'}
(r/'records/S6_SERIES_PUBLISH_I_family_structure_integration.json').write_text(json.dumps(receipt,indent=2)+'\n')
