from pathlib import Path
import hashlib,json,csv,datetime
R=Path(__file__).resolve().parents[1]
sp=R/'S6_SERIES_PUBLISH_II.tex';s=sp.read_text()
t=s.index(r'\hypertarget{tag-02WT}');a=s.rfind(r'\begin{proposition}',0,t)
p=s.index(r'\end{proof}',t)+len(r'\end{proof}')
left=s.rfind(r'\end{proof}',0,a)+len(r'\end{proof}');right=s.index(r'\begin{proposition}',p)
rows=[r for r in csv.DictReader((R/'CHECK_EVENTS.tsv').open(),delimiter='\t') if r['statement_id']=='night:P4.21']
assert len(rows)==3
d=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),statement_owner='night:P4.21',tag='02WT',
 source_sha256=hashlib.sha256(sp.read_bytes()).hexdigest(),
 ledger_sha256=hashlib.sha256((R/'CHECK_EVENTS.tsv').read_bytes()).hexdigest(),
 adjacent_before=dict(char_start=left,char_end=a,text=s[left:a]),
 adjacent_after=dict(char_start=p,char_end=right,text=s[p:right]),
 exact_owner_rows=rows,
 actual_root_reading_scope='The complete immediately preceding source-location paragraph, the empty following interstatement gap, and all three exact-owner event rows were actually read. This record does not claim root has read the entire WT proof.',
 finding='These adjacent text segments and three exact-owner rows name no computational routine. The checker separately reports reading the entire released WT proof and finding no routine there. No claim of absence elsewhere in the repository or historical source files is made.')
out=R/'records/S6_SERIES_PUBLISH_II_WT_prior_program_scope.json';assert not out.exists();out.write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps(dict(path=str(out.relative_to(R)),sha256=hashlib.sha256(out.read_bytes()).hexdigest(),exact_owner_rows=len(rows))))
