from pathlib import Path
import csv, datetime as dt, difflib, hashlib, io, json, re

R=Path(__file__).resolve().parents[1]
def sha(b): return hashlib.sha256(b).hexdigest()
p=R/'S6_SERIES_PUBLISH_II.tex'; before=p.read_bytes(); s=before.decode()
assert sha(before)=='dc94611a3ead46219230da3e4d41f6b0486b9bd1e409b851128c22d6d8fa7405'
old=r'''This corrects the sufficiency step
on p.~692 of \cite{CDP2020} and replaces
\cite[Theorem~2.2]{CDP2020}; the torsion-free conclusion of its
Proposition~7.3 is recovered in \ref{cdp:st:A.4.9}.
The final two calculations correct \cite[Lemma~1.5 and
Proposition~1.1]{CDP98} in the printed scopes stated in
\ref{cdp:st:E12} and \ref{cdp:st:E17}.'''
new=r'''The normal-crossing torsion obstruction and its application to
the standard family are \cite[Lemma~10.3, Theorem~10.5 and
\S10.4, pp.~87--90]{AC2026}. The normalization-Picard criterion
extends that obstruction through the stated normalization and
full-fibre maps and replaces \cite[Theorem~2.2, p.~680]{CDP2020}.
The torsion-free conclusion of \cite[Proposition~7.3, pp.~693--695]{CDP2020}
is proved in \ref{cdp:st:A.4.9}. The final two calculations correct
\cite[Lemma~1.5, pp.~79--80, and Proposition~1.1, p.~78]{CDP98}
in the scopes of \ref{cdp:st:E12} and \ref{cdp:st:E17}.'''
assert s.count(old)==2
s=s.replace(old,new,1)
old_table='A & '+old+r'\\'
new_table=r'''A & Extends the obstruction of \cite[Lemma~10.3 and Theorem~10.5]{AC2026}
to the normalization-Picard criterion; corrects
\cite[Theorem~2.2, p.~680]{CDP2020} and
\cite[Proposition~1.1 and Lemma~1.5, pp.~78--80]{CDP98}.\\'''
assert s.count(old_table)==1
s=s.replace(old_table,new_table,1)
after=s.encode()
env=r'\\begin\{(proof|theorem|proposition|lemma|corollary|definition|remark|maintheorem|citedresult)\}[\s\S]*?\\end\{\1\}'
assert [m.group() for m in re.finditer(env,before.decode())]==[m.group() for m in re.finditer(env,s)]
for pattern in [r'\\label\{[^}]+\}',r'\\hypertarget\{tag-[^}]+\}\{\}']:
    assert re.findall(pattern,before.decode())==re.findall(pattern,s)
now=dt.datetime.now(dt.timezone.utc).isoformat()
out=R/'records/S6_SERIES_PUBLISH_II_frontmatter_credit_01'; assert not out.exists(); out.mkdir()
diff=''.join(difflib.unified_diff(before.decode().splitlines(True),s.splitlines(True),fromfile='II before primary-credit revision',tofile='II after primary-credit revision'))
(out/'source.diff').write_text(diff)
dp=R/'S6_SERIES_PUBLISH_defects_II.tsv'; dbefore=dp.read_bytes()
reader=csv.DictReader(io.StringIO(dbefore.decode(),newline=''),delimiter='\t'); fields=reader.fieldnames; rows=list(reader)
added=[]
for number,kind,location,a,b,reason in [
    (1,'D18','series:II:A literature-status paragraph',old,new,'Credit the exact prior normal-crossing obstruction and its standard-family application, actually read in AC26 pp.87-90; specify the source pages for each correction. No theorem or proof text changes.'),
    (2,'D12','section 1.4, row A',old_table,new_table,'Replace the duplicated literature paragraph by a compact source relationship, including the primary credit verified by the reading. The complete scope remains in Theorem A and its status paragraph.')
]:
    added.append(dict(change_id='II-C2-FM01-'+str(number).zfill(3),type=kind,statement_id='series:II:A',old_location=location,old_page='pending baseline mapping',new_location=location,new_page='pending integrated PDF',old_text=a,new_text=b,reason=reason,review_status='Primary pages and receiving statement/proofs actually read; wording compared; final page review pending'))
buf=io.StringIO(newline=''); writer=csv.DictWriter(buf,fieldnames=fields,delimiter='\t',lineterminator='\n'); writer.writeheader(); writer.writerows(rows+added)
dafter=buf.getvalue().encode(); p.write_bytes(after); dp.write_bytes(dafter)
evidence=R/'records/S6_SERIES_PUBLISH_II_provenance_primary_reading_02.json'
manifest=dict(created_utc=now,source_before_sha256=sha(before),source_after_sha256=sha(after),defects_before_sha256=sha(dbefore),defects_after_sha256=sha(dafter),defect_rows_added=added,source_diff_sha256=sha(diff.encode()),primary_evidence=dict(path=str(evidence.relative_to(R)),sha256=sha(evidence.read_bytes())),statement_and_proof_environments_identical=True,labels_and_tags_identical=True,check_events_added=0,required_checks_closed=0,provenance_claims_closed=0,final_page_reading_credit=0)
(out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
note='\n\n### Paper II primary credit, '+now+'\n\nThe complete AC26 normal-crossing obstruction (Lemma 10.3), its standard-family nonvanishing (Theorem 10.5), and the precise CDP reduction comparison (section 10.4, pp.87-90) were read and compared with the receiving filtration and normalization maps. The opening status now credits those results explicitly; the duplicate A-row paragraph in section 1.4 is reduced to its source relationship. Both changes are logged, with an exact diff and hashes in `records/S6_SERIES_PUBLISH_II_frontmatter_credit_01/manifest.json`. Every statement and proof environment, label and tag is unchanged. This editorial credit revision closes no required proof check, global defect class, final provenance claim or final-PDF page.\n'
for name in ['S6_SERIES_PUBLISH_report.md','PROGRESS_LEDGER.md']:
    q=R/name; q.write_bytes(q.read_bytes()+note.encode())
print(json.dumps({k:v for k,v in manifest.items() if k in ['created_utc','source_before_sha256','source_after_sha256','defects_after_sha256','statement_and_proof_environments_identical','check_events_added']},indent=2))
