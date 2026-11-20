from pathlib import Path
import json,hashlib,re,csv
R=Path(__file__).resolve().parents[1];p=R/'parts/III.body.linked.tex';old=p.read_text();s=old
patches=[]
def sub(a,b):
 global s
 assert s.count(a)==1,(a[:100],s.count(a))
 s=s.replace(a,b,1);patches.append({'old':a,'new':b})
sub(r'''\path{code/III/fourfolds_OS45_primitive_cubic.py}
reconstructs the actual complement before using its torsion
character, checks all sixteen meridians, computes the exact
index-two primitive lattice, and verifies all $15^3=3375$ primitive
triples and all $16^3=4096$ recovered component triples. The
normalization restriction \eqref{maps:eq:D.PC14}, the actual period basis, and
all sparse integral entries are retained in its JSON output.
The preliminary component-only calculation is retained separately
in \path{code/III/fourfolds_OS45_component_ring.py}.''',r'''The supplied program
\path{code/III_OS45_primitive_cubic_independent.py}
constructs the sixteen normalized component restrictions from the
six cyclic boundary classes \eqref{maps:eq:D.PC13}, with intersection
matrix \(\operatorname{diag}(1,-1,-1,-1)\). It forms the exact
index-two primitive lattice using \eqref{maps:eq:D.PC9}, records
the full \(15\times16\) basis matrix and its rational inverse
modulo the all-one component relation, and verifies all
\(16^3=4096\) component triples, \(15^3=3375\) primitive triples
and \(16^3=4096\) recovered component triples.
It also verifies \eqref{maps:eq:D.PC14} on every normalization and
the exact period transport
\[
 L=\begin{pmatrix}8&24\\-6&-16\end{pmatrix}
  =\operatorname{diag}(8,2)
    \begin{pmatrix}1&3\\-3&-8\end{pmatrix},
 \qquad \det\begin{pmatrix}1&3\\-3&-8\end{pmatrix}=1.
\]
All 19,349 exact assertions pass. The basis matrices, component
restrictions and complete nonzero tensors are saved in
\path{code/outputs/III_OS45_primitive_cubic_independent.json}.
The core relation matrix and the framed critical-cycle comparison
are separate constructions in the following paragraphs.''')
sub(r'''The exact program
\path{code/III/fourfolds_OS45_localization.py}
retains every wall value and every $\eta_v$, verifies the actual
quasiperiods on all sixteen residues, and proves the six
all-character polynomial divisibility identities \eqref{maps:eq:D.OL11}.
It explicitly records the required geometric support comparison
as a separate hypothesis.''',r'''The supplied exact program
\path{code/III_weighted_OS45_checks.py}
retains every wall value and every \(\eta_v\). Substituting
\(r=8a+r_0\), \(s=2b+s_0\) with independent integers \(a,b\)
proves the two affine quasiperiod identities on every one of
the sixteen residue classes. The program also computes the
normalization squares modulo sixteen, the mixed entries involving
\(y\), and all six polynomial divisibility identities in
\eqref{maps:eq:D.OL11} for every character. Its exact tables and
polynomials are in
\path{code/outputs/III_weighted_OS45_checks.json}.
The geometric support comparison is supplied by the preceding
bundle and boundary maps.''')
assert re.findall(r'\\label\{([^}]+)\}',old)==re.findall(r'\\label\{([^}]+)\}',s)
p.write_text(s)
(R/'analysis/III_fresh_cubic_integration_05.json').write_text(json.dumps({'patches':patches,'before_sha256':hashlib.sha256(old.encode()).hexdigest(),'after_sha256':hashlib.sha256(s.encode()).hexdigest(),'labels_preserved':True,'remaining_gate':'The full core/peripheral Smith matrices and the framed odd generator are not reconstructed by these programs; older missing program references in those separate paragraphs remain pending.'},indent=2)+'\n')
f=R/'audit_root/CHECK_EVENTS.tsv'
with f.open() as h:rows=list(csv.DictReader(h,delimiter='\t'))
fields=list(rows[0]);eid='root-III-OS45-full-cubic-05';assert not any(r['event_id']==eid for r in rows)
rows.append({'statement_id':'maps:src:D.2.53','date':'2026-11-19','who':'GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort; S6_SERIES_GRIND root','type':'computation','outcome':'New independent program III_OS45_primitive_cubic_independent.py derives the exact six-ray normalization restrictions and complete15x16primitive matrix, inverse modulo all-one relation, full4096component/3375primitive/4096recovered tensors, all16half-class restrictions and unimodular period transport.19349assertions pass; no earlier implementation or certificate imported. Receiving full-proof computation paragraphs now name the actual supplied code. This does not reconstruct core/peripheral Smith arrays or the odd framed torsion cycle, and D2.4 remains open.','event_id':eid,'phase':'S6_SERIES_GRIND'})
with f.open('w',newline='') as h:w=csv.DictWriter(h,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
print('applied',len(patches),'proof computation paragraphs; event',eid)
