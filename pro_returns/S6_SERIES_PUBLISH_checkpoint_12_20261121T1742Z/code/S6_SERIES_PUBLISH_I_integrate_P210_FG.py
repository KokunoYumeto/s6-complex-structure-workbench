from pathlib import Path
import json,hashlib,datetime
from S6_SERIES_PUBLISH_editing import Editor
r=Path(__file__).resolve().parents[1];ed=Editor('I');files=[]
for name,kind in [('S6_SERIES_PUBLISH_I_P210_resolution_guarded.json','D25'),('S6_SERIES_PUBLISH_I_main_FG_guarded.json','D07')]:
 p=r/'agents/i_topology/editorial'/name
 for x in json.loads(p.read_text())['patches']:
  ed.replace(x['old'],x['new'],kind,x['reason'],x.get('statement_id',x['id']),x.get('expected_count',1))
 files.append({'path':str(p.relative_to(r)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
ed.save()
error=r/'agents/i_topology/S6_SERIES_PUBLISH_I_P210_resolution_ERROR_EVENT.json'
out={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':hashlib.sha256(ed.text.encode()).hexdigest(),'guards':files,'error_record':str(error.relative_to(r)),'error_record_sha256':hashlib.sha256(error.read_bytes()).hexdigest(),'scope':'Root read the full new P2.10 steps6–8, exact old/new comparison and proof-error record, and all three front guards. Agent exact computation and exposed reread keep their own scopes. The theorem statement and all labels/tags are unchanged; no new root independent-check event.'}
(r/'records/S6_SERIES_PUBLISH_I_P210_FG_integration.json').write_text(json.dumps(out,indent=2)+'\n')
report=r/'S6_SERIES_PUBLISH_report.md'
report.write_text(report.read_text()+r'''

## Paper I: propagation of the chosen small-resolution correction

The final F comparison found the same selected-diagonal mismatch in the
attached proof of `night:P2.10`, steps 6–8. Its resolution of `(b,x)`
was valid as a local small resolution, but the claim identifying it with
the marked A1.2 filling used the other ruling. The exact receiving map
is `(X,Y,Z,V,u)=(z,rw,x,y,r²)`. The required ideal is therefore
`(z,y)`, or `(b,y)` after `z=rb`. The corrected charts are
`b=yk, x=kw` and `y=bj, w=jx`; their overlap is
`j=1/k, (b,x)=k(y,w)`. Their parameters in the two A1.2 charts
are `(y,w/r,rk)` and `(rb,x,j/r)`. The printed involution lifts
preserve these charts and the common invariant coordinate `W=rw`.

Both old and new resolutions contract to the same node. The common
node blowup, with its exceptional Segre quadric and the two ruling
projections, gives their exact comparison morphisms. The theorem's
existence, properness and flatness statement is unchanged. This is a
proof-error correction, with no newly refuted theorem statement.
Engel Proposition 2.8, printed pp.6–7, supplies the general triangular
construction; the specified edge is fixed by the receiving marked map.
The fresh exact chart/transition/involution calculation and the exposed
proof comparison are recorded separately in the topology evidence.
The first five proof steps are retained unchanged.

The same final comparison makes the higher-cover exponents explicit in
main F, retains the sign-dependent canonical or anticanonical power in
its outline, and gives the actual `V_n=n v+v_0` realization in outline G.
These passages now name the exact maps and constructions of the body.
''')
