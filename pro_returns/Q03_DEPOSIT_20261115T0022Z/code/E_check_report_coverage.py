#!/usr/bin/env python3
"""Final coverage gate for the full Q03 report; reads without editing sources."""
from pathlib import Path
import csv,hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
post=(ROOT/'Q03_DEPOSIT_post.tex').read_text()
report=(ROOT/'Q03_DEPOSIT_report.md').read_text()
pdf=(ROOT/'Q03_DEPOSIT_post.pdf').read_bytes()
expected_source='e497aaa7011dedbbbaa16ff5b67699a6ffdec6bfb4d2f1f473544939def5dbf9'
expected_pdf='d8782e70ae9286badbf36c6ac98247698f7747fa00f1c9733d4a76b1d1c6265a'
assert hashlib.sha256(post.encode()).hexdigest()==expected_source
assert hashlib.sha256(pdf).hexdigest()==expected_pdf
assert not re.search(r'VISUAL_QA_PENDING|INCOMPLETE|IN_PROGRESS|TODO|TBD',report)
assert '**Package state:** Complete; final user approval remains after delivery.' in report
names=['A_accounting.md','B_foundations.md','B_hard.md','E_provenance.md','E_proof_integration.md','E_final_consistency.md']
for name in names:
    body=(ROOT/'work'/name).read_text()
    assert body in report,('audit not embedded completely',name)
marks=list(re.finditer(r'\\begin\{(numbered(?:up)?)\}\{([^{}]+)\}\{([0-9.]+)\}',post))
counts={}
for i,m in enumerate(marks):
    ident=m.group(3)
    end=marks[i+1].start() if i+1<len(marks) else post.index(r'\fixedhead{Limits and open points}',m.start())
    body=post[m.start():end]
    assert re.search(r'^#{2,4} (?:Lemma|Proposition|Theorem|Corollary|Definition) '+re.escape(ident)+r'\b',report,re.M),('audit heading missing',ident)
    counts[ident]=len(re.findall(r'\\step\{',body))
assert len(counts)==44 and sum(counts.values())==124
assert len(re.findall(r'\\begin\{proof\}',post))==43
csvrows=list(csv.DictReader((ROOT/'Q03_DEPOSIT_results.csv').open()))
assert len(csvrows)==47
expected_tasks=['A.1','A.2','A.3','B.1','B.2','B.3','C.1','C.2','D.1','E.1','E.2','E.3']
for task in expected_tasks:assert re.search(r'^\| '+re.escape(task)+r' \|',report,re.M)
checklist=report.split('## Part E — format checklist and delivery state',1)[1].split('### Compilation and visual verification',1)[0]
for k in range(1,11):assert re.search(r'^\| '+str(k)+r' \|',checklist,re.M)
assert '| 10 | User approval remains after delivery |' in checklist
assert '| Final revised build | 38 | 0 | 0 | 0 |' in report
assert expected_pdf in report
assert (ROOT/'work/visual_qa_report.md').read_text() in report
for text in ['Original FKN full text remains unavailable','zero surviving-first initial-pair replacements','50 exact queries','## Per-task completion matrix','### Preservation, supersession and exclusions']:
    assert text in report,text
sections={str(s):{'statements':sum(k.startswith(str(s)+'.') for k in counts),
                  'numbered_steps':sum(v for k,v in counts.items() if k.startswith(str(s)+'.'))} for s in range(2,10)}
print(json.dumps({'date':'2026-11-15','verdict':'PASS','source_sha256':expected_source,'pdf_sha256':expected_pdf,
 'report_sha256':hashlib.sha256(report.encode()).hexdigest(),'report_words':len(report.split()),
 'complete_audits_embedded':names,'proof_statements_with_individual_audit_headings':44,
 'proof_environments':43,'numbered_proof_steps':124,'per_section':sections,
 'CSV_rows':47,'task_rows':expected_tasks,'format_checklist_items':10,
 'pending_markers':0,'final_build_pages':38,'final_overfull_boxes':0,
 'visual_record_embedded_exactly':True,'remaining_step':'User review and approval after delivery.'},indent=2))
