"""Bind Paper I's current dependency graph to visible statements and proofs."""
from pathlib import Path
import json,datetime
from S6_SERIES_PUBLISH_editing import Editor
r=Path(__file__).resolve().parents[1]
ed=Editor('I')
ed.replace(r'\subsection{Known and new}',r'\subsection{Known and new}\label{pub:I:known-new}',
 'D06','Add the stable section anchor used by the publication graph parser. Current dependencies use visible statements, immediate proofs and their own outlines; hidden historical uses/used-by records are not mathematical premises.','pub:I:known-new')
ed.save()
p=r/'code/S6_SERIES_PUBLISH_current_metadata.py'
s=p.read_text();old='maintheorem|theorem|lemma|proposition|corollary|definition|remark'
assert s.count(old)==1
p.write_text(s.replace(old,old+'|cited'))
(r/'records/S6_SERIES_PUBLISH_I_precise_graph_marker.json').write_text(json.dumps({
 'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'change':'Activate the already implemented exact proof/outline ownership and hidden-metadata exclusion for I via its stable known-new section label. Include cited-result environments in final metadata inventory.',
 'finding':'The preceding I graph was still conservative because this source marker was absent. Boundary consolidation exposed twenty historical-header dependencies; they require visible-premise review rather than automatic extra mathematical checks.',
 'mathematical_events':0,'remaining':'Final first-part rewrite, actual premise review and global theorem/outline checks remain open.'
},indent=2)+'\n')
