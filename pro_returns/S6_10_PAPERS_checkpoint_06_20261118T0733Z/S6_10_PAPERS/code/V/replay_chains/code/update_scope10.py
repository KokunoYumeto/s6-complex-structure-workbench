"""Record the audited post09 scope without replacing historical records."""
from pathlib import Path
import csv, json, re, datetime

root = Path(__file__).resolve().parents[1]
now = datetime.datetime.now(datetime.timezone.utc).isoformat()

p = root/'sections/manifolds.tex'
s = p.read_text()
start = s.index(r'\paragraph{Remaining task D.2.4')
end = s.index(r'\paragraph{Theorem D.2.5', start)
old = root/'records/D2_4_superseded_at10.tex'
if not old.exists(): old.write_text(s[start:end])
replacement = r'''\paragraph{Remaining task D.2.4 (Open: the full filling and smooth classification).}
The natural section-line sphere question is complete on all $21$
profiles, with $59$ marked sphere patterns on $50$ initial rows
(D.2.24--28). D.2.29--33 compute every allowed finite affine
logarithm and every original/log additive and original/Mumford
multiplicative choice on the natural initial catalogue. There are
$495$ distinct integral homology presentations on $172$ rows.
D.2.37, D.2.40 and D.2.41 now compute every positive translation
iterate of every such row, including shared even factors, arbitrary
free finite and regular logarithms, and the ordinary clutch.
The exact bar-chain correction in D.2.41 retains the full
two-primary fibre coinvariant. Star caps in that theorem remain
original. D.2.43 additionally computes a general same-fan cusp's
actual torsion and its nonsaturated marked boundary kernel.

The simply connected minimal smooth sector is classified in
D.2.25--26 and D.2.35--39, D.2.42 for residual orders
$1,2,3,5,6,7,10,14,15,30$. This accounts for $144$ of its $162$
potentially simply connected patterns. All allowed finite orders,
affine twists and ordinary clutches are included within each
theorem's specified primitive-Mumford scope, without extra regular
logarithms. The $18$ remaining minimal patterns have residual
orders $4$ (five patterns), $8$ (eight), and $20$ (five).

'''+(root/'records/fourfolds_D2_remaining_paragraph.tex').read_text()+r'''

The complete D.2 request also includes logarithmic Mumford star
caps beyond the proved sphere obstruction, initial linearizations
and vertical corrections beyond the translation iterates, and
the full smooth invariants of the remaining weighted and
additional-regular-log sectors. Known integral presentations do
not determine those smooth types. The general cusp calculation
does not by itself complete their global attachment. The failed
ordinary-characteristic-class and half-weight shortcuts, their
exact certificates, and the next frame-parity and marked-cap
computations remain in the dated research records. Earlier
wordings of this remaining task are preserved separately.

'''
p.write_text(s[:start]+replacement+s[end:])

p = root/'sections/fourfolds.tex'
s = p.read_text()
start = s.index(r'\paragraph{Problem E.2.4')
end = s.index(r'\input{sections/shifted_integral}', start)
old = root/'records/E2_4_superseded_at10.tex'
if not old.exists(): old.write_text(s[start:end])
replacement = r'''\paragraph{Conclusion E.2.4 (Proved: the shifted product's smooth type).}
The shifted product in (E.16) is the closed oriented ten-manifold
$\mathcal H_{10}$ specified by the $2432$ ordinary framed handles
of E.2.21. Its regular-fibre complement is, relative to its entire
marked boundary, the $76$-handle six-manifold $\mathcal H_6$ of
that theorem. The full attaching embeddings, their ordered normal
coordinates, and every dual belt embedding are prescribed by
finite coordinate formulas. The identification follows by an
actual relative diffeomorphism of the cusp, core and finite caps,
and then by the handle-by-handle comparison of E.2.21 using
Milnor's Theorems~1.4, 3.13 and~5.8. Top attaching maps are
retained, so there is no uncomputed sphere-capping ambiguity.

Together with E.2.1--3, E.2.5--20, this supplies the complex
invariants, the general smooth compact pullback construction,
the product case $S^6\times N$, and the shifted product's
fundamental group and full integral homology. The smooth type
is given by the explicit framed-handle presentation, not by an
inference from its homology or by an asserted connected-sum
normal form. E.2.18's actual quadratic obstruction is consistent
with this presentation. The former open paragraph is retained
in the research records.

'''
p.write_text(s[:start]+replacement+s[end:])

changes = {
 'manifolds_results.csv': ('D.2.4', {
   'statement':'The full D2 classification remains open beyond the completed natural sphere sector, all-positive-weight natural homology, and144 minimal-pattern smooth identifications.',
   'status':'Open',
   'depends_on':'D.2.24–43',
   'notes':'INCOMPLETE: remaining minimal patterns are5 c4,8 c8,5 c20; the exact missing invariant is the relative3-frame parity. General star logarithms, broader initial corrections and weighted/additional-log smooth classifications also remain. OS55 a5 b4 zero I1 position2, e1 is an explicit undecided Z4 instance.'}),
 'fourfolds_results.csv': ('E.2.4', {
   'statement':'The shifted product is identified up to oriented diffeomorphism with the complete2432 ordinary framed-handle presentation of E.2.21; its regular-fibre complement has the specified76-handle relative presentation.',
   'status':'Proved',
   'depends_on':'E.2.1–3; E.2.5–21; Milnor Theorems1.4,3.13,5.8',
   'notes':'Resolved by full coordinate attaching embeddings and their normal framings, actual relative comparison, and all dual belt/top attachments. Complete integral homology and group were previously computed. The historical open paragraph is preserved in records/E2_4_superseded_at10.tex.'})}
old_rows = []
for name,(ident,values) in changes.items():
 p=root/'records'/name
 with p.open(newline='') as f:
  reader=csv.DictReader(f);fields=reader.fieldnames;rows=list(reader)
 found=[r for r in rows if r['id']==ident];assert len(found)==1
 old_rows.append(dict(source=name,row=dict(found[0])))
 found[0].update(values)
 with p.open('w',newline='') as f:
  writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader();writer.writerows(rows)
old=root/'records/scope_rows_superseded_at10.json'
if not old.exists():old.write_text(json.dumps(old_rows,indent=2)+'\n')

p=root/'S6_04_MAPS_MANIFOLDS_report.md';s=p.read_text()
s=s.replace('Current state, 15 November 2026','Current state, 16 November 2026')
table={
 'D.2':'| D.2 | D.2.1–D.2.43 | Undecided in the full classification. All21 natural sphere profiles,495 original/log/Mumford presentations on172 rows, and every positive translation weight now have exact integral algorithms. Complete simply connected smooth types cover144 of162 minimal patterns. The18 remaining minimal patterns have residual orders4,8,20; their refined two-primary frame parity is unresolved. Broader star/corrected and weighted/additional-log smooth sectors remain open |',
 'E.2':'| E.2 | E.2.1–E.2.21 | (a): complex invariants and general pullback construction proved; product case identified; shifted product has its full group, integral homology and a complete2432 ordinary framed-handle smooth identification. The76-handle complement is compared relative to its full marked boundary. Every normal framing and top attaching map is retained |'}
for item,line in table.items():s=re.sub(r'^\| '+re.escape(item)+r' \|.*$',lambda _:line,s,flags=re.M)
s=s.replace('F.2 closed after the eighth source freeze; D.2 and E.2 remain open.',
 'F.2 closed after the eighth source freeze and E.2 closed during the tenth hour; D.2 remains open.')
s=s.replace('The requested classified smooth type remains separate from these homological invariants.',
 'E.2.19–21 now give the requested smooth identification by a complete ordinary framed-handle presentation and an actual relative diffeomorphism; this conclusion uses the full attaching maps, not these homological invariants alone.')
p.write_text(s)

audits={
 'D.2.41':{'decision':'PASS','proof':'code/manifolds_all_weighted_profiles_proof.tex',
   'checks':'6606 exact quadratic identities,1548 literal last-word identities,1953 full presentations,426 shared-even cases,1527 odd-overlap comparisons; root independent24 even-factor comparisons under changed bar-coordinate order.',
   'root_output':'records/root_all_weighted_coordinate_audit.out'},
 'D.2.43':{'decision':'PASS','proof':'code/manifolds_general_cusp_proof.tex',
   'checks':'Full Laurent-unimodular reduction and Tor/Koszul proof,75 exact HNF cases including8 noncyclic cases; actual bounding normal sweeps and PL torsion argument independently checked by root and fourfolds.',
   'root_output':'records/root_general_cusp_audit.out'},
 'E.2.21':{'decision':'PASS','proof':'code/maps_ordinary_handles_proof.tex',
   'checks':'Full coordinate-block/collar/framing proof, exact76/2432 expanded handles, root executable replay, independent fourfolds geometric/scope audit; root read primary Milnor Theorems1.4 printed25,3.13 printed31,5.8 printed63–64 and Vogel equation16 printed103.',
   'root_output':'records/root_ordinary_handles_audit.out'}}
(root/'records/root_completion_audit10.json').write_text(json.dumps({'updated_utc':now,'audits':audits},indent=2)+'\n')
print(json.dumps({'updated_utc':now,'remaining_prompt_items':['D.2'],'audits':audits},indent=2))
