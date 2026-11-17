"""Replace repeated statement environments; retain complete proof bodies verbatim.

The root-owned shared statements must receive the labels/additions supplied in
shared_statement_additions.tex.  This script never modifies root-owned files.
"""
from pathlib import Path
import hashlib, json, re, csv

ROOT = Path(__file__).resolve().parents[3]
D = ROOT / 'deliverables/work/invariants_arithmetic'
S = D / 'sections'
specs = [
 ('ari_analytic.tex', 'ari:C.8.5', 'fam:st:C.2.3',
  r'\begin{proof}[Division-ladder proof of Theorem~\ref{fam:st:C.2.3} (source ARI C.8.5)]'),
 ('inv_part_D.tex', 'inv:D1.3', 'fam:st:A.5.2',
  r'\begin{proof}[Koszul and direct-image proof of Theorem~\ref{fam:st:A.5.2} (source INV D1.3)]'),
 ('inv_part_D.tex', 'inv:D2.1', 'fam:st:A.5.2',
  r'\begin{proof}[Actual-gluing Kodaira--Spencer calculation for Theorem~\ref{fam:st:A.5.2} (source INV D2.1)]'),
 ('inv_part_D.tex', 'inv:D3.1', 'fam:st:A.5.2',
  r'\begin{proof}[Kuranishi ideal calculation for Theorem~\ref{fam:st:A.5.2} (source INV D3.1)]'),
]
records=[]
for file,alias,target,heading in specs:
 p=S/file; text=p.read_text()
 pat=r'\\begin\{proposition\}\[[^\n]*\]\\label\{'+re.escape(alias)+r'\}\n([\s\S]*?)\\end\{proposition\}\n\\begin\{proof\}([\s\S]*?)\\end\{proof\}'
 m=re.search(pat,text)
 if not m:
  if heading in text: continue
  raise RuntimeError('Cannot find '+alias)
 statement=m[1]; proof=m[2]
 replacement=heading+proof+r'\end{proof}'
 text=text[:m.start()]+replacement+text[m.end():]
 p.write_text(text)
 records.append({'source_label':alias,'shared_printed_label':target,
  'candidate_file':str(p.relative_to(ROOT/'deliverables')),
  'removed_duplicate_statement':statement,
  'complete_original_proof_body_sha256':hashlib.sha256(proof.encode()).hexdigest(),
  'proof_body_retained_verbatim':True,
  'alias_placement':'inside root-owned shared theorem, after its main label',
  'date':'2026-11-17'})
if records:
 (D/'statement_aliases.json').write_text(json.dumps(records,indent=2)+'\n')

# The extra direct-image and generator conclusions are part of the shared
# statement, rather than silently lost when the repeated environments go away.
(D/'shared_statement_additions.tex').write_text(r'''% Root integration patch.  Do not input this file as an independent section.
% Add immediately after \label{fam:st:C.2.3} inside the shared maximum theorem:
\label{ari:C.8.5}
% Add immediately after \label{fam:st:A.5.2} inside the shared tangent theorem:
\label{inv:D1.3}\label{inv:D2.1}\label{inv:D3.1}
% Append the following paragraph INSIDE that tangent theorem, before its end:
More precisely, for the intrinsic fibration $f:X_c\to\mathbb P^1$,
\[
 f_*T_{X_c}=\mathcal O\oplus\mathcal O(-1),\qquad
 R^1f_*T_{X_c}=\mathcal O\oplus\mathcal O(-1)^2,\qquad
 R^2f_*T_{X_c}=\mathcal O.\tag{D.4}
\]
The Leray class $\xi\otimes[\gamma]$ generates $H^1(X_c,T_{X_c})$.
The primary Kuranishi bracket is zero; the one-dimensional obstruction
space $H^2(X_c,T_{X_c})$ therefore does not imply a nonzero obstruction
map.
''')

audit=json.loads((D/'result_audit.json').read_text())
aliases={a:b for _,a,b,_ in specs}
for row in audit:
 old=row['printed_label']
 if old in aliases:
  row['source_label_alias']=old
  row['printed_label']=aliases[old]
  row['taken_over_by']=aliases[old]
  row['change_notes'].append('Duplicate statement merged; complete proof body retained verbatim. Alias and shared-statement additions in statement_aliases.json/shared_statement_additions.tex.')
 if row['candidate_file'].startswith('work/invariants_arithmetic/sections/'):
  row['own_check']['candidate_sha256']=hashlib.sha256((ROOT/'deliverables'/row['candidate_file']).read_bytes()).hexdigest()
(D/'result_audit.json').write_text(json.dumps(audit,indent=2)+'\n')
fields=list(dict.fromkeys(k for r in audit for k in r))
with (D/'result_audit.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
 for row in audit:w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in row.items()})
print('Merged',len(records),'duplicate environments; all proof bodies preserved.')
