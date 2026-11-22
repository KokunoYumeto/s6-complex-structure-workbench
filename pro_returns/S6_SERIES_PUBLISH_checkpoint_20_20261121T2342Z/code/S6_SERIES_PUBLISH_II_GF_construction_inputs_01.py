"""Expose exact construction/formula inputs D.22–D.30, with target proof excluded."""
from pathlib import Path
import datetime,hashlib,json
R=Path(__file__).resolve().parents[1];P=R/'S6_SERIES_PUBLISH_II.tex';s=P.read_text()
start=s.index(r'\label{cdp:st:D.2.7}')
end=s.index(r'\tag{D.31}',start)
scope=s[start:end];parts=[];spans=[]
def take(a,b,description):
 i=scope.index(a);j=scope.index(b,i)
 part=scope[i:j]
 parts.append('% '+description+'\n'+part)
 spans.append(dict(description=description,start_offset=start+i,end_offset=start+j,start_line=s[:start+i].count('\n')+1,end_line=s[:start+j].count('\n')+1,sha256=hashlib.sha256(part.encode()).hexdigest()))
take('Put $q=e^{-2\\pi}$.', '\\item Let $C$ and $B$', 'Exponential coordinate, period and oriented generators: D.22.')
take('\\item Let $C$ and $B$', '\\item The canonical section', 'Blowup, line bundle, scalar quotient and local elliptic-bundle definition: D.23.')
take('\\item The canonical section', 'Its canonical\nbundle is trivial', 'Canonical punctured product marking and central components; defining quotient of the first component: D.24.')
take('The inverse image of $R$ is', 'Since $p$ is a submersion', 'Defining quotient of the second component and their common elliptic curve.')
take('Let $\\Lambda=H_1(A;\\Z)$', 'To verify them,', 'Boundary input: the stated nearby-fibre quotient maps D.25; their proof is omitted.')
take('\\item Let $\\mu$ be the positive base meridian', 'For a cycle in $C$', 'Boundary input: the stated meridian and mixed-cycle maps D.26; bounding-chain proof omitted.')
take('\\item We now specify the three local fillings.', '\\item For the initial smooth $A$-bundle', 'Ordered lattice, three elliptic embeddings and exact complementary markings: D.27.')
take('\\item For the initial smooth $A$-bundle', 'The\nresulting $f:Y', 'Clutching translation and definition of the three replacements: D.28; global conclusions omitted.')
take('Let $M$ be the part above the sphere', 'This sign follows directly', 'Exterior boundary identification and the three clutching vectors: D.29.')
take('On mixed\ntwo-cycles the same map is', 'This formula can also be obtained', 'The induced mixed-cycle map D.30; later Mayer–Vietoris argument omitted.')
out=R/'agents/ii_infra/recovery_20261121/S6_SERIES_PUBLISH_II_01GF_construction_inputs.tex'
assert not out.exists()
body='% Exact cited construction and labelled formula inputs for 01GF.\n% Source '+hashlib.sha256(P.read_bytes()).hexdigest()+'\n% No target D.2.8 proof, D.36 calculation, or D.31–D.32 global argument is included.\n\n'+'\n\n'.join(parts)
for n in range(31,37):assert '\\tag{D.'+str(n)+'}' not in body
assert r'\label{cdp:st:D.2.8}' not in body
out.write_text(body)
record=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),source_path=str(P.relative_to(R)),source_sha256=hashlib.sha256(P.read_bytes()).hexdigest(),output_path=str(out.relative_to(R)),output_sha256=hashlib.sha256(out.read_bytes()).hexdigest(),spans=spans,scope='Exact construction and stated labelled input maps only. No target GF proof or D.31/D.32 global homology proof. The D.25/D.26 input formulas are stated without their derivations.',check_events_added=0)
out.with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(dict(path=record['output_path'],sha256=record['output_sha256'],parts=len(parts)),indent=2))
