"""Export exact ambient and graph definitions without exposing the E17 proof."""
from pathlib import Path
import datetime, hashlib, json
R=Path(__file__).resolve().parents[1]
base=R.parent/'S6_SERIES_PUBLISH_work'
p=base/'S6_GRIND_4_s6_09_compendium/S6_09_PAPERS_II.tex';s=p.read_text()
l=base/'S6_GRIND_6_literature/papers/arXiv_1912.09719_Lehn_Rollenske_Schinko_src/main.tex';t=l.read_text()
parts=[];bindings=[]
def take(text,path,start,end):
    a=text.index(start);b=text.index(end,a)+len(end)
    parts.append(text[a:b])
    bindings.append(dict(source=str(path),source_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),character_span=[a,b],excerpt_sha256=hashlib.sha256(text[a:b].encode()).hexdigest()))
take(t,l,r'\begin{theorem}\label{theorem main2 new}',r'\end{theorem}')
take(s,p,r'Let $Z\subset Y\times\mathbb P^1$ be the closure of its graph',r'hypersurface is integral.')
take(s,p,r'A fibre $Z_c$ is identified',r'It is therefore Cohen--Macaulay and Gorenstein.')
take(s,p,r'Let $D_i$ be the sum, with coefficient',r'Cartier divisor since $Y$ is smooth.')
out=R/'agents/ii_checks_provenance/recovery_20261121T2000Z/S6_SERIES_PUBLISH_II_E17_graph_ambient_inputs.tex'
assert not out.exists()
out.write_text('% Exact primary statement and cited-input definitions only. No E17 target proof.\n\n'+'\n\n'.join(parts)+'\n')
d=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),target='01GO/cdp:st:E17',path=str(out.relative_to(R)),sha256=hashlib.sha256(out.read_bytes()).hexdigest(),excerpts=bindings,
       scope='LRS Theorem3.1 explicitly assumes a compact complex manifold. The attached compendium E2 proof explicitly says Y is smooth and identifies its full graph fibres with Cartier divisors of Y. The graph itself is given as an integral hypersurface; no smoothness of that graph is asserted. This export includes only the ambient/graph/fibre definitions and the primary theorem statement, no E17 proof. Current series II has no E2 owning body; that reference remains to be repaired after mathematical comparison.',
       target_proof_included=False,events_added=0)
out.with_suffix('.json').write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps(dict(path=d['path'],sha256=d['sha256'],excerpts=len(bindings)),indent=2))
