from pathlib import Path
import json,hashlib,datetime
from S6_SERIES_PUBLISH_editing import Editor

r=Path(__file__).resolve().parents[1]
ed=Editor('I'); sources=[]
ed.replace('\\part{Results not yet established}\n\\section{Arithmetic periods and compact subgroups}',
 '\\section{Arithmetic periods and compact subgroups}','D23',
 'Remove the obsolete open-part divider before proved arithmetic material; the final open part remains after all proved sections.',
 'I:open-part-order')
paths=[
 r/'agents/i_provenance/S6_SERIES_PUBLISH_I_editorial_mapsI_guards.json',
 r/'agents/i_provenance/S6_SERIES_PUBLISH_I_primary_citation_guards_03.json',
 r/'agents/i_analytic/S6_SERIES_PUBLISH_I_editorial_batch_h_guards.json',
 r/'agents/i_topology/editorial/S6_SERIES_PUBLISH_I_boundary_batch2_guarded.json']
for p in paths:
 d=json.loads(p.read_text()); changes=d.get('changes',d.get('guards',d.get('patches')))
 for x in changes:
  ed.replace(x['old'],x['new'],x.get('type','D12'),x['reason'],x['id'],count=x.get('expected_count',1))
 sources.append({'path':str(p.relative_to(r)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'guards':len(changes)})
start=ed.text.rfind('\\section{',0,ed.text.index('\\label{mapsI:circle-quotient}'))
end=ed.text.index('\\subsection{The Albanese coordinates and real structures}',ed.text.index('\\label{mapsI:circle-quotient}'))
circle=ed.text[start:end]
assert 'mapsI:src:A.2.1' in circle and 'ari:C.2.1' not in circle
ed.replace(circle,'','D23','Move the complete corrected circle-quotient construction immediately before the real structures which use its cusp replacement.','mapsI:circle-quotient')
anchor='\\section{Real structures and their fixed three-spheres}'
ed.replace(anchor,circle+anchor,'D23','Place the already constructed circle quotient before its real-form restrictions.','mapsI:real-forms')
ed.save()

p=r/'agents/i_provenance/S6_SERIES_PUBLISH_I_shared_bib_guards_03.json'
d=json.loads(p.read_text()); bib=r/'S6_SERIES_PUBLISH_references.bib'; old=bib.read_text(); new=old
for x in d['changes']:
 assert new.count(x['old'])==x.get('expected_count',1),x['id']
 new=new.replace(x['old'],x['new'])
bib.write_text(new)
(r/'records/S6_SERIES_PUBLISH_I_real_boundary2_H_integration.json').write_text(json.dumps({
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sources':sources,
 'root_review':'Read the full real/circle comparison report, every changed new real/circle passage including the full moved B4.2 proof, all H replacements, all primary03 replacements, the full boundary2 comparison report and every boundary2 new passage. Agents recorded their complete affected old/new proof comparisons. This integration does not claim a second full reread of all removed old proofs by root.',
 'scope':'Applied-source guard verification and mathematical editorial comparison; no new independent mathematical event is created by integration or movement.',
 'bibliography_guard':str(p.relative_to(r)),
 'structure':['Remove obsolete earlier open-part divider.','Move full corrected circle section before real forms, after family topology.','Move full conjugation classification before real-form representatives.'],
 'remaining':'Final rendered-page reading, publication-level scope wording and program end-table remain open.'
},indent=2)+'\n')
