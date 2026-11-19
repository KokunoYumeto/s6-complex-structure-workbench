#!/usr/bin/env python3
"""Validate the assembled artifacts and their recorded evidence before packaging.

This is an artifact-consistency gate, not a mathematical proof checker. The
mathematical arguments are reproduced in the report; finite checks have their
own explicitly limited coverage.
"""
import csv
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    build = json.loads((ROOT/'work/build_final/build_check.json').read_text())
    post = ROOT/'Q03_DEPOSIT_post.tex'
    pdf = ROOT/'work/build_final/Q03_DEPOSIT_post.pdf'
    assert digest(post) == build['source_sha256'], 'PDF built from an earlier source'
    assert digest(pdf) == build['pdf_sha256'], 'PDF changed after build'
    assert build['overfull_count'] == build['overfull_over_2pt'] == 0
    assert not build['undefined_reference_warning']
    shutil.copy2(pdf, ROOT/'Q03_DEPOSIT_post.pdf')
    script_outputs = [
        ('E_check_proof_integration.py','E_check_proof_integration_output.json'),
        ('E_check_final_consistency.py','E_check_final_consistency.out'),
        ('E_build_form_answers.py','E_build_form_answers_output.json'),
    ]
    for script, output in script_outputs:
        completed = subprocess.run(['python3', str(ROOT/'code'/script)],
                                   capture_output=True, text=True, check=True)
        (ROOT/'code'/output).write_text(completed.stdout)
    post_text = post.read_text()
    report = (ROOT/'Q03_DEPOSIT_report.md').read_text()
    assert not report.startswith('INCOMPLETE')
    assert 'VISUAL_QA_PENDING' not in report
    assert len(report.split()) > 12000, 'Full step-by-step report absent'
    # Preserve complete independent derivations, not just a summary or links.
    embedded = ['A_accounting.md','B_foundations.md','B_hard.md',
                'E_provenance.md','E_proof_integration.md','E_final_consistency.md']
    for filename in embedded:
        assert (ROOT/'work'/filename).read_text().strip() in report, filename
    for item in ['A.1','A.2','A.3','B.1','B.2','B.3','C.1','C.2','D.1','E.1','E.2','E.3']:
        assert item in report, item
    assert post_text.count(r'\step{') == 124
    assert len(re.findall(r'\\begin\{proof\}', post_text)) == 43
    rows = list(csv.DictReader((ROOT/'Q03_DEPOSIT_results.csv').open()))
    assert len(rows) == len({r['id'] for r in rows}) == 47
    bib = set(re.findall(r'\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}', post_text))
    cites = set()
    for match in re.finditer(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}',post_text):
        cites.update(match.group(1).split(','))
    assert cites <= bib, ('undefined bibliography', cites-bib)
    for sid in ['P','F','D','N','A','FKN','FKN-e','CG','U','GJ','L','J','G']:
        bibliography_key = 'FKNe' if sid == 'FKN-e' else sid
        assert 'S-'+sid in post_text and bibliography_key in bib, sid
    anc = json.loads((ROOT/'code/E_verify_provenance.out').read_text())
    for row in anc['copy_checks']:
        p = ROOT/row['file']
        assert p.stat().st_size == row['bytes'] and digest(p) == row['sha256']
        assert row['matches_supplied']
    assert anc['observed_private_credentials'] == anc['observed_actual_local_paths'] == 0
    review = json.loads((ROOT/'code/visual_review.json').read_text())
    assert review['pdf_sha256'] == digest(pdf)
    assert review['reviewed_contact_pages'] == list(range(1,build['pages']+1))
    assert review['unresolved_visual_findings'] == []
    assert len(list((ROOT/'work/build_final/pages').glob('page-*.png'))) == build['pages']
    required = ['Q03_DEPOSIT_post.tex','Q03_DEPOSIT_post.pdf','Q03_DEPOSIT_report.md',
                'Q03_DEPOSIT_results.csv','Q03_DEPOSIT_sources.md','Q03_DEPOSIT_literature.md',
                'Q03_DEPOSIT_form_answers.md']
    for name in required:
        assert (ROOT/name).is_file() and (ROOT/name).stat().st_size > 0, name
    result = {
      'verdict':'PASS', 'date':'2026-11-15',
      'scope':'Artifact consistency; human-readable proof derivations and source evidence are in the report and ledgers.',
      'numbered_proof_statements':44, 'all_statement_CSV_rows':47,
      'proof_environments':43, 'numbered_proof_steps':124,
      'full_audit_files_embedded':embedded,
      'report_word_count':len(report.split()),
      'bibliography_items':len(bib), 'source_check_identifiers':13,
      'ancillary_copies_verified':len(anc['copy_checks']),
      'PDF':build, 'visual_review':review,
      'delivered_files':{name:{'bytes':(ROOT/name).stat().st_size,
                               'sha256':digest(ROOT/name)} for name in required},
      'remaining_user_step':'Review and approve the deposit after receiving this package; no remote deposit was performed.',
    }
    (ROOT/'code/final_validation.json').write_text(json.dumps(result,indent=2,ensure_ascii=False))
    print(json.dumps({k:result[k] for k in ['verdict','numbered_proof_statements',
          'all_statement_CSV_rows','proof_environments','numbered_proof_steps',
          'report_word_count','bibliography_items','ancillary_copies_verified']},indent=2))

if __name__ == '__main__':
    main()
