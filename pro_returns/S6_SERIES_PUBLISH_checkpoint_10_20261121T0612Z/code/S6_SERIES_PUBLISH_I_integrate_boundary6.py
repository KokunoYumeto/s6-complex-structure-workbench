from pathlib import Path
import json,datetime,hashlib
from S6_SERIES_PUBLISH_editing import Editor
r=Path(__file__).resolve().parents[1];ed=Editor('I')
p=r/'agents/i_topology/editorial/S6_SERIES_PUBLISH_I_boundary_batch6_guarded.json';d=json.loads(p.read_text())
for x in d['patches']:ed.replace(x['old'],x['new'],x.get('type','D12'),x['reason'],x['id'],count=x.get('expected_count',1))
ed.replace(r'The additive translation construction of Proposition~\ref{fam:src:A.5.1} has finite-chart connector',
 r'The finite-chart comparison of \cref{fam:src:A.3.1} uses the connector',
 'D04','Point to the actual construction and connector proof, with its current theorem type supplied by cleveref.','I:finite-connector-two-logarithms')
ed.replace(r'\subsection{The actual global family with one base point removed}',r'\subsection{The global family with one base point removed}',
 'D08','Remove the process modifier from the mathematical subsection title.','push:src:B.4.19')
ed.save()
(r/'records/S6_SERIES_PUBLISH_I_boundary6_integration.json').write_text(json.dumps({'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'guard_path':str(p.relative_to(r)),'guard_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'scope':'Root read every proposed passage and the full scoped comparison. Agent complete old/new comparisons remain the evidence; no additional independent event. Exact known-source openings for inherited Oda/Fujimoto/Nishiguchi/SS roles remain tracked separately.','root_variations':['Point the finite connector to its actual A3.1 proof using cleveref.','Remove actual from a subsection title.'],'source_sha256':hashlib.sha256(ed.text.encode()).hexdigest()},indent=2)+'\n')
