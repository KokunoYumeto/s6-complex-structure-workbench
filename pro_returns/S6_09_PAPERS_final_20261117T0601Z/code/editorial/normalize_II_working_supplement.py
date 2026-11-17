"""Apply scoped citation normalization and a full elementary exponential-sequence step."""
from pathlib import Path
import hashlib,json
D=Path(__file__).resolve().parents[2];p=D/'editorial/II_working_supplement.tex';s=p.read_text();before=hashlib.sha256(s.encode()).hexdigest()
archive=D/'editorial/history/II_working_supplement_before_root_citations.tex';archive.parent.mkdir(exist_ok=True)
if not archive.exists():archive.write_text(s)
old=r'''This neighbourhood is Stein and retracts onto \(S^1\), so its second
integral cohomology vanishes.  Cartan's theorem~B and the exponential
sequence therefore give trivial Picard group
\cite[\S2, fundamental theorem, p.~81]{Cartan1957}%
\cite[Proposition~6.28 and equations~(6.35)--(6.36),
pp.~180--182]{Lee2024}.  Pull \(L|_{N_0}\) back to'''
new=r'''Write \(U=A_u\times D_{x_1}\times D_{x_2}\) for this neighbourhood.
It is Stein and retracts onto \(S^1\), so \(H^2(U,\mathbb Z)=0\).
For completeness, the exponential sequence is
\[
0\longrightarrow\mathbb Z\longrightarrow\mathcal O_U
 \xrightarrow{\,h\mapsto e^{2\pi i h}\,}\mathcal O_U^*
 \longrightarrow1.
\]
Its exactness follows from the existence of a holomorphic logarithm locally
for every nonvanishing holomorphic function, and from the integral kernel
of the exponential. Cartan's theorem~B gives
\(H^1(U,\mathcal O_U)=H^2(U,\mathcal O_U)=0\)
\cite[\S2, fundamental theorem~B, p.~80]{Cartan1957}.
The long cohomology sequence therefore identifies
\(\operatorname{Pic}(U)=H^1(U,\mathcal O_U^*)\) with
\(H^2(U,\mathbb Z)=0\). Pull \(L|_{N_0}\) back to'''
if old in s:s=s.replace(old,new)
elif new not in s:raise ValueError('Expected full exponential-sequence source interval absent')
s=s.replace(r'\cite[\S3.3, pp.~60--63; \S3.4, pp.~63--72]{Fulton1993}%'+'\n','')
s=s.replace(r'\cite[\S2.1, pp.~28--29]{Fulton1993} and'+'\n','')
s=s.replace('p.~179 and~4.2.12, p.~182','p.~181 and~4.2.12, p.~184')
s=s.replace('compare\n'+r'\cite[Example~1.2.21', 'compare the author preprint\n'+r'\cite[Example~1.2.21')
p.write_text(s)
record={'before_sha256':before,'after_sha256':hashlib.sha256(s.encode()).hexdigest(),'retained_before':str(archive.relative_to(D)),'changes':['Explicit complete exponential-sequence argument replaces unopened Lee2024 citation; opened Cartan1957 fundamental theorem locator corrected to p80.','Redundant unopened Fulton1993 Ch2/3 references replaced by actually opened Cox–Little–Schenck author-preprint statements; exact support-function convention preserved.','CLS Theorems4.2.8/4.2.12 pages181/184 refer to opened2010preprint; original draft179/182 preserved in history.']}
(D/'records/II_working_supplement_root_changes.json').write_text(json.dumps(record,indent=2)+'\n')
refs=D/'work/root/references_verified.json';d=json.loads(refs.read_text())
for r in d:
 if r.get('keys')==['Bingener1980']:
  r['locator']='Introduction p318; Satz6.2 p337; setup pp336–337'
  r['verification']+=' The original introduction p318 was additionally opened: topological local triviality plus degree-one cohomological flatness permits the exponential quotient; in general the quotient method encounters difficulties. This precisely matches the limited historical discussion. Web ref turn259view0.'
refs.write_text(json.dumps(d,indent=2)+'\n')
mapping=json.loads((D/'work/cdp_audit/working_supplement_mapping.json').read_text())
aliases={}
for r in mapping['rows']:
 if r['printed_paper']=='II':
  aliases[r['source_id']]=r['printed_label'];aliases['wb:'+r['source_id']]=r['printed_label'];aliases[r.get('alias_label') or 'wbII:'+r['source_id']]=r['printed_label']
(D/'work/cdp_audit/paperII_statement_aliases.json').write_text(json.dumps(aliases,indent=2)+'\n')
p=D/'code/editorial/assemble_paper_ii.py';s=p.read_text()
s=s.replace("joined=replace_external_I('\\n'.join(body))", "joined=replace_external_I('\\n'.join(body))\n# Canonical statement aliases identify the shared statement, not a repeated proof.\nif (W/'working_supplement_mapping.json').exists():\n    mapping=json.loads((W/'working_supplement_mapping.json').read_text())\n    for item in mapping['canonical_alias_insertions']:\n        target=r'\\label{'+item['insert_at']+'}'\n        alias=r'\\label{'+item['alias']+'}'\n        assert target in joined, item\n        if alias not in joined:joined=joined.replace(target,target+alias,1)")
p.write_text(s)
print('Normalized full supplement; preserved before version; aliases',len(aliases))
