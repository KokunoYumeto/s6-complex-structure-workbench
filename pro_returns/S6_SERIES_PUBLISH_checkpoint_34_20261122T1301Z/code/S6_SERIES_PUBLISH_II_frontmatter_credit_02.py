from pathlib import Path
import csv, datetime as dt, difflib, hashlib, io, json, re
R=Path(__file__).resolve().parents[1]
def sha(b): return hashlib.sha256(b).hexdigest()
p=R/'S6_SERIES_PUBLISH_II.tex'; before=p.read_bytes(); s=before.decode()
assert sha(before)=='2981a1387eae34af5e26847262bc5e1449d8a3638a6b928ebae57215f193a7da'
c_old=r'''The value two for the supplied
sphere family is credited to \cite[Theorem~7.22, p.~60]{AC26}
and \cite[Proposition~7.1]{Engel2026}. The unrestricted sign and
equality statement is proved through the actual fibre comparisons
in \ref{cdp:st:C.2.G.1}; the analytic period input is
\cite[\S2, pp.~234--239]{Steenbrink1976} in its stated scope.'''
c_new=r'''The Euler number two for the standard sphere family is
\cite[Theorem~7.22, p.~60]{AC2026} and
\cite[Proposition~7.1, p.~17]{Engel2026}. The sign and equality
criteria for all the stated degenerations are proved in
\ref{cdp:st:C.2.G.1}. The analytic period input is
\cite[\S2, pp.~234--239]{Steenbrink1976}.'''
e_old=r'''The untwisted tangent tuple is
among the credited DGKX version-one results discussed in Paper~I;
the full twist and map formulas here give the explicit correction
to the generic vanishing invoked in \cite[Theorem~2.2]{CDP2020}.'''
e_new=r'''The untwisted tuple is
\cite[Theorem~6.12, pp.~81--82]{DGKXv1}. The twist formulas and
normalization-map ranks refine the degree-two obstruction of
\cite[Theorem~10.5 and Corollary~10.6, pp.~88--89]{AC2026},
which corrects \cite[Theorem~2.2, p.~680]{CDP2020}.'''
assert s.count(c_old)==2 and s.count(e_old)==2
changes=[
    ('D18','series:II:C','section 1.2, Theorem C literature status',c_old,c_new,'Give the exact original-family Euler loci actually read, and describe the receiving sign/equality scope in mathematical terms.'),
    ('D12','series:II:C','section 1.4, row C','C & '+c_old+r'\\',r'''C & All-degeneration sign and equality criteria; the standard-family value
is \cite[Theorem~7.22, p.~60]{AC2026} and
\cite[Proposition~7.1, p.~17]{Engel2026}.\\''','Replace a duplicated paragraph by its compact source relationship, with the independently opened Euler loci.'),
    ('D18','series:II:E','section 1.2, Theorem E literature status',e_old,e_new,'Name the precise version-one untwisted theorem and prior degree-two obstruction. The explicit normalization-map comparison and n=0 specialization are recorded in primary reading03.'),
    ('D12','series:II:E','section 1.4, row E','E & '+e_old+r'\\',r'''E & Twist and normalization-map formulas refining
\cite[Theorem~10.5]{AC2026}; the untwisted tuple is
\cite[Theorem~6.12, pp.~81--82]{DGKXv1}.\\''','Replace the duplicated E paragraph by a compact relationship that preserves the primary credit.')
]
applied=[]
for n,(kind,label,location,old,new,reason) in enumerate(changes,1):
    count=s.count(old)
    assert count==(2 if n in [1,3] else 1),(n,count)
    s=s.replace(old,new,1)
    applied.append(dict(change_id='II-C2-FM02-'+str(n).zfill(3),type=kind,statement_id=label,old_location=location,old_page='pending baseline mapping',new_location=location,new_page='pending integrated PDF',old_text=old,new_text=new,reason=reason,review_status='Exact primary loci and receiving statements read; statement/proof environments unchanged; final page review pending'))
env=r'\\begin\{(proof|theorem|proposition|lemma|corollary|definition|remark|maintheorem|citedresult)\}[\s\S]*?\\end\{\1\}'
assert [m.group() for m in re.finditer(env,before.decode())]==[m.group() for m in re.finditer(env,s)]
for pattern in [r'\\label\{[^}]+\}',r'\\hypertarget\{tag-[^}]+\}\{\}']:
    assert re.findall(pattern,before.decode())==re.findall(pattern,s)
after=s.encode(); dp=R/'S6_SERIES_PUBLISH_defects_II.tsv'; dbefore=dp.read_bytes()
reader=csv.DictReader(io.StringIO(dbefore.decode(),newline=''),delimiter='\t');fields=reader.fieldnames;rows=list(reader)
buf=io.StringIO(newline='');w=csv.DictWriter(buf,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows+applied);dafter=buf.getvalue().encode()
out=R/'records/S6_SERIES_PUBLISH_II_frontmatter_credit_02';assert not out.exists();out.mkdir()
diff=''.join(difflib.unified_diff(before.decode().splitlines(True),s.splitlines(True),fromfile='II before C/E primary-credit revision',tofile='II after C/E primary-credit revision'))
(out/'source.diff').write_text(diff)
now=dt.datetime.now(dt.timezone.utc).isoformat();evidence=R/'records/S6_SERIES_PUBLISH_II_provenance_primary_reading_03.json'
manifest=dict(created_utc=now,source_before_sha256=sha(before),source_after_sha256=sha(after),defects_before_sha256=sha(dbefore),defects_after_sha256=sha(dafter),defect_rows_added=applied,source_diff_sha256=sha(diff.encode()),primary_evidence=dict(path=str(evidence.relative_to(R)),sha256=sha(evidence.read_bytes())),statement_and_proof_environments_identical=True,labels_and_tags_identical=True,check_events_added=0,required_checks_closed=0,provenance_claims_closed=0,final_page_reading_credit=0)
p.write_bytes(after);dp.write_bytes(dafter);(out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
note='\n\n### Paper II Euler and tangent-cohomology credits, '+now+'\n\nThe exact first-page credits now name Engel Proposition 7.1, p.17, DGKX version-one Theorem 6.12, pp.81-82, and the prior AC26 degree-two obstruction. The complete cited statements and proofs were read in their original PDFs. The receiving C5a-C5c statements and complete proofs were read; the trivial twist agrees with (1,1,1,0), and the exceptional n=-1 map has rank zero through its exact boundary sequence. A new weighted-monomial calculation compares 193 integral twists and proves the displayed Euler value through the twelve residue classes and its period identity. All statement/proof environments and labels/tags are unchanged by these four editorial credit/table changes. The exact diff and rows are in `records/S6_SERIES_PUBLISH_II_frontmatter_credit_02/manifest.json`; the primary and arithmetic scopes are in `records/S6_SERIES_PUBLISH_II_provenance_primary_reading_03.json`. No required proof row, global defect class, final provenance claim or final-PDF page is closed by this revision.\n'
for name in ['S6_SERIES_PUBLISH_report.md','PROGRESS_LEDGER.md']:
    q=R/name;q.write_bytes(q.read_bytes()+note.encode())
print(json.dumps(dict(created_utc=now,source_after_sha256=sha(after),defects_after_sha256=sha(dafter),defect_rows_added=len(applied),statement_and_proof_environments_identical=True,check_events_added=0),indent=2))
