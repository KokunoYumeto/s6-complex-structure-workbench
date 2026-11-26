"""Expose exact named helper definitions needed for LS relation transport."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import ast

lane=Path('agents/continuation7_iii_vertical_correction_receiving')
scopes={
 'manifolds_general_initial.py':{'graph_data','satimage','rational_solution'},
 'manifolds_rankone_families.py':{'decomp','ikernel','wedge','biv','bezout'},
 'manifolds_all_weighted_profiles.py':{'QuadraticCorrection'},
}
pieces=[]
print('START',datetime.now(timezone.utc).isoformat())
for name,selected in scopes.items():
    path=lane/('S6_SERIES_PUBLISH_'+name)
    source=path.read_text();lines=source.splitlines()
    print('SOURCE',path,'SHA256',sha256(path.read_bytes()).hexdigest())
    for node in ast.parse(source).body:
        if isinstance(node,(ast.FunctionDef,ast.ClassDef)) and node.name in selected:
            head=f'{name}:{node.lineno}-{node.end_lineno} {node.name}'
            body='\n'.join(lines[node.lineno-1:node.end_lineno])
            print('DEFINITION',head)
            print(body)
            pieces.append('# '+head+'\n'+body)
out=lane/'S6_SERIES_PUBLISH_III_02LS_historical_helper_bounded_v002.py'
out.write_text('\n\n'.join(pieces)+'\n')
print('EXTRACT',out,'SHA256',sha256(out.read_bytes()).hexdigest())
print('COMPLETE',datetime.now(timezone.utc).isoformat())
