#!/usr/bin/env python3
"""Repair two exact unresolved-reference tokens observed in the full II build."""
from pathlib import Path
import csv,datetime as dt,difflib,hashlib,io,json,re
from S6_SERIES_PUBLISH_II_title_census import fingerprint as titlefp
from S6_SERIES_PUBLISH_II_D10_census import fingerprint as apparatusfp
R=Path(__file__).resolve().parents[1];O=R/'records/S6_SERIES_PUBLISH_II_build_reference_fixes_01'
sha=lambda b:hashlib.sha256(b).hexdigest()
def enc(x):return (json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode()
def bind(p):
 b=p.read_bytes();return dict(path=str(p.relative_to(R)),bytes=len(b),sha256=sha(b))
def tab(rows,fields):
 o=io.StringIO(newline='');w=csv.DictWriter(o,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writerows(rows);return o.getvalue().encode()
assert not O.exists();p=R/'S6_SERIES_PUBLISH_II.tex';b=p.read_bytes();s=b.decode();assert sha(b)=='6ebaca4da9c7533800d8054bb63d8b4521c11e59b401c8ec02a425a34cd3d181'
guards=[dict(id='section-key-leading-whitespace',type='D23',old='\\cref{sec:II:06,sec:II:07,sec:II:all:08,sec:II:09,sec:II:10,\nsec:II:11,sec:II:all:12}',new='\\cref{sec:II:06,sec:II:07,sec:II:all:08,sec:II:09,sec:II:10,sec:II:11,sec:II:all:12}',location='How the paper is organized, sign-theorem section list',reason='The TeX newline becomes a leading space in the sixth reference key. Removing that separator joins the exact same seven existing labels. No destination identity changes.'),dict(id='Stacks-citation-key',type='D18',old=r'\cite[Tag~031S, Lemma~10.157.4]{Stacks}',new=r'\cite[Tag~031S, Lemma~10.157.4]{StacksProject}',location='Normality criterion in conductor-branch proof',reason='The intended existing bibliography entry is StacksProject. The exact official Tag031S page was opened and its full Lemma10.157.4 statement/proof read; the cited locus is unchanged.')]
assert all(s.count(r'\label{'+k+'}')==1 for k in ['sec:II:06','sec:II:07','sec:II:all:08','sec:II:09','sec:II:10','sec:II:11','sec:II:all:12'])
assert s.count(r'\bibitem[{The Stacks Project Authors}(2026)]{StacksProject}')==1
new=s;inverse=[]
for g in guards:
 assert new.count(g['old'])==1 and new.count(g['new'])==0,g['id'];a=new.index(g['old']);inverse.append(dict(offset=a,old=g['old'],new=g['new']));new=new[:a]+g['new']+new[a+len(g['old']):]
back=new
for g in reversed(inverse):a=g['offset'];assert back[a:a+len(g['new'])]==g['new'];back=back[:a]+g['old']+back[a+len(g['new']):]
assert back==s and titlefp(s)==titlefp(new) and apparatusfp(s)==apparatusfp(new)
csv.field_size_limit(100_000_000);dp=R/'S6_SERIES_PUBLISH_defects_II.tsv';db=dp.read_bytes();rd=csv.DictReader(io.StringIO(db.decode()),delimiter='\t');oldrows=list(rd);fields=rd.fieldnames;rows=[]
for i,g in enumerate(guards,1):
 r={k:'' for k in fields};r.update(change_id=f'II-BUILDREF-01-{i:03}',type=g['type'],statement_id='',old_location=g['location'],old_page='temporary D19 build: observed warning',new_location=g['location'],new_page='pending repeated build',old_text=g['old'],new_text=g['new'],reason=g['reason'],review_status='Exact reference-identity repair; no proof wording, mathematical statement or displayed formula changed.');rows.append(r)
now=dt.datetime.now(dt.timezone.utc).isoformat();O.mkdir();(O/'guards_and_inverse.json').write_bytes(enc(dict(guards=guards,inverse=inverse)));(O/'defect_rows.tsv').write_bytes(tab(rows,fields));(O/'source.diff').write_text(''.join(difflib.unified_diff(s.splitlines(True),new.splitlines(True),fromfile='II before reference fixes',tofile='II after reference fixes')))
record=dict(created_utc=now,source_before_sha256=sha(b),source_after_sha256=sha(new.encode()),exact_inverse=True,primary_source=dict(url='https://stacks.math.columbia.edu/tag/031S',web_ref='turn186285053view0',read='Complete Lemma10.157.4 statement and proof, website lines27–37',scope='The Noetherian R1/S2 normality criterion named in the existing citation; no new whole receiving-proof check.'),build_findings=['LaTeX Warning: Reference ` sec:II:11` undefined','Package natbib Warning: Citation `Stacks` undefined'],verifier_finding='The earlier citation-warning regex recognized LaTeX Warning only; the next verifier must also recognize Package natbib Warning and the final undefined-citations summary.',defect_rows_added=2,defect_rows_after=len(oldrows)+2,source_guard_count=2,mathematical_events_added=0,classes_closed=0,final_pdf_page_credit=0,D10_fingerprint_unchanged=apparatusfp(new),D16_fingerprint_unchanged=titlefp(new),code=bind(Path(__file__)),evidence=[bind(x) for x in sorted(O.iterdir())])
(O/'manifest.json').write_bytes(enc(record));assert p.read_bytes()==b and dp.read_bytes()==db;p.write_text(new);dp.write_bytes(db+tab(rows,fields))
note=f'\n\n## Paper II: two compiled-reference repairs — {now}\n\nThe full temporary numbering build exposed a leading-space section key and the unmatched Stacks citation key. Both are repaired through their exact existing target identities; official Tag031S was additionally opened at Lemma10.157.4. The initial verifier failed honestly, and its natbib-warning coverage is being strengthened before a fresh build. Source `{sha(new.encode())}`. Evidence `records/S6_SERIES_PUBLISH_II_build_reference_fixes_01/manifest.json`. Two individual defect records, no mathematical event or class/page credit.\n'
for n in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
 with (R/n).open('ab') as f:f.write(note.encode())
print(json.dumps(record,indent=2))
