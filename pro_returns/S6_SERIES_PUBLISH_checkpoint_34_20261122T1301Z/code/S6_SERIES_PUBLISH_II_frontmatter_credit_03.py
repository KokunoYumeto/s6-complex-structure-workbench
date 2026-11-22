from pathlib import Path
import csv, datetime as dt, difflib, hashlib, io, json, re

R=Path(__file__).resolve().parents[1]
def sha(b):return hashlib.sha256(b).hexdigest()
def bind(p):
    b=(R/p).read_bytes()
    return dict(path=p,sha256=sha(b),bytes=len(b))

now=dt.datetime.now(dt.timezone.utc).isoformat()
addendum_path='records/S6_SERIES_PUBLISH_II_provenance_primary_reading_04_addendum.json'
assert not (R/addendum_path).exists()
addendum=dict(created_utc=now,extends=bind('records/S6_SERIES_PUBLISH_II_provenance_primary_reading_04.json'),source=bind('S6_SERIES_PUBLISH_II.tex'),primary=bind('../temporary_B_pdf/LiuRollenske2609_33826v2.pdf'),pages_actually_viewed=[4,5],images=[bind('../primary_continuation2_root_provenance/LR_v2-'+str(n).zfill(2)+'.png') for n in [4,5]],loci='Entire original version-two pages4-5 were actually displayed and read after primary-reading04 was written. Equation(2.3) and section2.B p4 give the exact source action. Complete Proposition2.4 and proof pp4-5 and Proposition2.5 and proof p5 were read. Page4 also contains the proof of Proposition2.1, but its full statement begins on the preceding page and no new complete-Proposition2.1 reading is claimed.',exact_map='The fixed morphism phi:t_(2P)^*M->M has divisor S_infinity and is an isomorphism over S^o. The action sends (s,m) to (t_(-2P)(s),u*phi(t_(2P)^*m)), where m is the same fibre element under the stated pullback identification. This is the exact B_u=u B_0 used in theorem G. The fixed-root central scalar is consequently alpha=c*u. The added first-page citation is equation(2.3),p4.',new_check_events=0,required_checks_closed=0,final_provenance_claims_closed=0,final_publication_page_reading_credit=0)
(R/addendum_path).write_text(json.dumps(addendum,indent=2)+'\n')
p=R/'S6_SERIES_PUBLISH_II.tex'
before=p.read_bytes()
assert sha(before)=='39421221ca61af1383f5ba22faf130c964e348d561c07f87ebf98fe374a4e2a4'
s=before.decode()
f_old=r'''The source families retain their
credit to \cite{Viaclovsky2026Two,LiuRollenske2026,Viaclovsky2026Combs}.
The comb vector-field value corrects the bound in
\cite[Corollary~1.3, p.~2]{HKP2000}, as explained in
\ref{inv:E2.4}.
The twelve-tooth calculation gives the stated open-family values
in the remaining-Hodge-number question of
\cite[Section~10(2)]{Viaclovsky2026Combs}; the general and
special-member splitting problem remains in \ref{inv:E2.3}.'''
f_new=r'''The source constructions are
\cite[Theorem~1.1, p.~2]{Viaclovsky2026Two},
\cite[Theorem~5.1, p.~21]{LiuRollenske2026}, and
\cite[Theorem~1.1, p.~2]{Viaclovsky2026Combs}.
The tangent and deformation formulas determine the full comb
Kuranishi germ asked for in
\cite[Section~10(1), p.~33]{Viaclovsky2026Combs}.
The ordered-multiplicity classification refines
\cite[Theorem~1.1, p.~1]{Viaclovsky2026Log} and answers its
deformation-class question in Section~1.1(1), p.~2.
The comb vector-field value corrects
\cite[Corollary~1.3, preprint p.~2]{HKP2000} through the explicit
meromorphic-function pullback in \ref{inv:E2.4}.
The twelve-tooth values answer the stated open-family case of
\cite[Section~10(2), p.~33]{Viaclovsky2026Combs}; the general
and special-member splitting problem remains in \ref{inv:E2.3}.'''
g_old=r'''The source action, good-root
lattice and logarithmic vector are
\cite[Lemma~2.7, Corollary~2.8, pp.~6--7; Proposition~3.6 and
Definition~3.7, pp.~9--10 of the attached-source edition]{LiuRollenske2026}.
The covering comparison is \ref{ii:LR:covering}. The former
fan-independent smooth-class clause is corrected separately by
\ref{night:P3K.36}, with the actual $T_2$ comparison yielding
$26\in\Z/28$.'''
g_new=r'''The exact scalar action is
\cite[equation~(2.3), p.~4]{LiuRollenske2026}; its good-root
lattice and logarithmic vector are
\cite[Lemma~2.7 and Corollary~2.8, pp.~6--7; Proposition~3.6 and
Definition~3.7, pp.~9--10]{LiuRollenske2026}, in arXiv version~2.
The covering comparison is \ref{ii:LR:covering}. The former
fan-independent smooth-class clause is corrected separately by
\ref{night:P3K.36}, with the actual $T_2$ comparison yielding
$26\in\Z/28$.'''
assert s.count(f_old)==2 and s.count(g_old)==2
changes=[
 ('D18','series:II:F','section1.2,Theorem F literature status',f_old,f_new,'Give exact construction and question locators for all four source families; identify the precise preprint edition of the corrected HKP corollary and its actual pullback map.'),
 ('D12','series:II:F','section1.4,row F','F & '+f_old+r'\\',r'''F & Tangent and full-deformation formulas for the cited constructions;
the comb germ and open twelve-tooth Hodge values address
\cite[Section~10(1)--(2), p.~33]{Viaclovsky2026Combs}.
The ordered-pair separation answers
\cite[Section~1.1(1), p.~2]{Viaclovsky2026Log}.
The vector-field correction is \ref{inv:E2.4}.\\''','Replace the duplicated paragraph by exact source relationships; full construction credits remain immediately after Theorem F.'),
 ('D18','series:II:G','section1.2,Theorem G literature status',g_old,g_new,'Identify the exact scalar action equation and the version-two page locators actually read; retain all covering and smooth-attachment assertions.'),
 ('D12','series:II:G','section1.4,row G','G & '+g_old+r'\\',r'''G & Minimal scalar covering degree for the action of
\cite[equation~(2.3), p.~4; Proposition~3.6 and Definition~3.7,
pp.~9--10]{LiuRollenske2026}. The retained $T_2$ smooth-class
comparison is \ref{night:P3K.36}, with value $26\in\Z/28$.\\''','Give the compact mathematical relationship and exact cited action. The T2 value and locator are preserved; the full history-bearing paragraph remains for its later exact-proof-bound editorial pass.')
]
applied=[]
for n,(kind,label,location,old,new,reason) in enumerate(changes,1):
    assert s.count(old)==(2 if n in [1,3] else 1),(n,s.count(old))
    s=s.replace(old,new,1)
    applied.append(dict(change_id='II-C2-FM03-'+str(n).zfill(3),type=kind,statement_id=label,old_location=location,old_page='pending baseline mapping',new_location=location,new_page='pending integrated PDF',old_text=old,new_text=new,reason=reason,review_status='Exact primary loci and receiving statements/outlines read; mathematical environments unchanged; final page review pending'))
env=r'\\begin\{(proof|theorem|proposition|lemma|corollary|definition|remark|maintheorem|citedresult)\}[\s\S]*?\\end\{\1\}'
assert [m.group() for m in re.finditer(env,before.decode())]==[m.group() for m in re.finditer(env,s)]
for pattern in [r'\\label\{[^}]+\}',r'\\hypertarget\{tag-[^}]+\}\{\}']:
    assert re.findall(pattern,before.decode())==re.findall(pattern,s)
after=s.encode()
dp=R/'S6_SERIES_PUBLISH_defects_II.tsv'
dbefore=dp.read_bytes()
reader=csv.DictReader(io.StringIO(dbefore.decode(),newline=''),delimiter='\t')
fields=reader.fieldnames
rows=list(reader)
buf=io.StringIO(newline='')
w=csv.DictWriter(buf,fieldnames=fields,delimiter='\t',lineterminator='\n')
w.writerows(applied)
assert dbefore.endswith(b'\n')
dafter=dbefore+buf.getvalue().encode()
out=R/'records/S6_SERIES_PUBLISH_II_frontmatter_credit_03'
assert not out.exists()
out.mkdir()
diff=''.join(difflib.unified_diff(before.decode().splitlines(True),s.splitlines(True),fromfile='II before F/G primary-credit revision',tofile='II after F/G primary-credit revision'))
(out/'source.diff').write_text(diff)
manifest=dict(created_utc=now,source_before_sha256=sha(before),source_after_sha256=sha(after),defects_before_sha256=sha(dbefore),defects_after_sha256=sha(dafter),defect_rows_added=applied,source_diff_sha256=sha(diff.encode()),primary_evidence=[bind('records/S6_SERIES_PUBLISH_II_provenance_primary_reading_04.json'),bind(addendum_path)],statement_and_proof_environments_identical=True,labels_and_tags_identical=True,check_events_added=0,required_checks_closed=0,provenance_claims_closed=0,final_page_reading_credit=0)
p.write_bytes(after)
dp.write_bytes(dafter)
(out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
note='\n\n### Paper II family, deformation and scalar-cover credits, '+now+'\n\nTheorem F now credits the exact Viaclovsky two-parameter and comb Theorem1.1 pages, Liu--Rollenske Theorem5.1, and the logarithmic-transformation Theorem1.1 and deformation-class question. The full original source statements were actually read; no rereading of their whole source proofs is claimed except the specifically recorded short LR statements. The HKP bound is located at preprint Corollary1.3,p2; its full proof and the receiving explicit meromorphic-function pullback were read. Theorem G now cites the exact scalar action(2.3),p4 and the good-root lattice/vector in the pinned LR version-two pages6-10. All source/receiving scopes and actual image readings are bound in primary-reading04 and its addendum. Four editorial changes preserve every statement/proof environment, label and tag. No required check, global defect class, final provenance gate or final-PDF page is closed by this revision.\n'
for name in ['S6_SERIES_PUBLISH_report.md','PROGRESS_LEDGER.md']:
    q=R/name
    q.write_bytes(q.read_bytes()+note.encode())
print(json.dumps(dict(created_utc=now,source_after_sha256=sha(after),defects_after_sha256=sha(dafter),defect_rows_added=len(applied),statement_and_proof_environments_identical=True,check_events_added=0),indent=2))
