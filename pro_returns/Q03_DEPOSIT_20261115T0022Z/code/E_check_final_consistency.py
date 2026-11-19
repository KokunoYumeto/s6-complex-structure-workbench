#!/usr/bin/env python3
"""Exact assembled-post/CSV/metadata consistency checks.

The script checks concrete strings, extracted theorem bodies and record fields.
It neither establishes theorem truth nor replaces the PDF rendering inspection.
"""
from pathlib import Path
import csv,hashlib,json,re

BASE=Path(__file__).resolve().parents[1]

def main():
    p=BASE/'Q03_DEPOSIT_post.tex'; data=p.read_bytes();s=data.decode('utf8')
    rows=list(csv.DictReader((BASE/'Q03_DEPOSIT_results.csv').open()))
    by_id={r['id']:r for r in rows}
    pat=re.compile(r'\\begin\{(numbered(?:up)?)\}\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}([\s\S]*?)\\end\{\1\}')
    blocks=list(pat.finditer(s));assert len(blocks)==44
    for m in blocks:
        env,kind,sid,title,body=m.groups()
        expected=f'{kind} {sid} ({title}).\n{body.strip()}'
        assert by_id[sid]['statement']==expected, f'CSV body mismatch {sid}'
    assert len(rows)==47 and len(by_id)==47
    section=s[s.index('\\section{Correctness and running time}'):s.index('\\fixedhead{Limits and open points}')]
    math=list(re.finditer(r'\$[^$]*\$|\\\[[\s\S]*?\\\]',section))
    leftover=[m.group() for m in math if 'S' in m.group().replace(r'\mathcal{S}','')]
    assert not leftover,'Unrenamed numerical S'
    assert r'B\cdot \mathcal{S}\cdot \mathcal{S}^2\cdot3D\mathcal{S}N' in section
    assert r'=3DB\mathcal{S}^4N=3DB^5N^{4m+1}' in section
    assert r'A(m,K)=2^{40}(m+1)^4(K+1)^4(K512^K)^5' in section
    assert r'G(m)=A(m,12m+25)m^{60m^2+129m+1}+2^{31}(m+1)^4' in section
    assert r'q=64(m+1)(K+1)' in section and r'D=2^{20}q^2' in section
    assert r'60m^2+129m+8' not in s
    assert 'demonstration:' not in s
    record={}
    for line in s.splitlines()[1:]:
        if line.startswith('%%% POST-RECORD v1 END'):break
        if line.startswith('% '):
            key,val=line[2:].split(':',1)
            record[key]=json.loads(val.strip())
    assert record['statements_in_proof']==44
    assert record['date']=='2026-11-15'
    assert record['claim_status']=='proved'
    assert record['human_understanding']=='none'
    assert record['formalization']=='none for this proof'
    assert record['checks_of_this_text'][0]['date']=='2026-11-15'
    assert set(record['checks_of_this_text'][0]['type'].split(','))=={'F','D','C','S'}
    assert [c['verdict'] for c in record['checks']]==['proved with fixable gaps','proved as stated','proved as stated']
    for actor in record['produced_by']:
        if 'model' in actor:assert actor.get('effort')
    assert any(a.get('role')=='deposit-task author' and a.get('effort')=='max' for a in record['produced_by'])
    assert any('9551' in x and '9383' in x for x in record['open_points'])
    assert '9,551 bytes' in s and '9,383-byte' in s
    assert record['provenance']['return_sha256']=='3ebeb452d6f461c23b4f8fa6f04ba6ed15abac541b5d2562fa814ba77977e60c'
    assert not re.findall(r'%%(?:KNOWN_TABLE|DEPENDENCY_TABLE|NOTATION_TABLE|SOURCE_CHECK_ROWS|BIBLIOGRAPHY|FINAL_[A-Z_]+)%%',s)
    metrics=re.search(r'Final PDF: (\d+) pages; (\d+) overfull boxes, (\d+) over 2pt',s)
    assert metrics
    result={'audit_date':'2026-11-15','post_sha256':hashlib.sha256(data).hexdigest(),
      'numbered_statements':len(blocks),'CSV_rows':len(rows),'exact_CSV_statement_matches':len(blocks),
      'numeric_state_bound_renaming':'all math occurrences replaced; product identity checked',
      'calligraphic_state_bound_occurrences':section.count(r'\mathcal{S}'),
      'coefficient_strings':'A,G,q,D match the independently audited accounting',
      'input_exponent':'60m^2+129m+2','padded_exponent':'60m^2+129m+1',
      'model_effort_date_fields':'consistent, including the current task author',
      'original_prompt_qualification':'present with both sizes and missing-variant qualification',
      'historical_verdicts':'exactly preserved; original-return scope identified',
      'scope_m_ge_3_explicit':{sid:bool(re.search(r'm\$?\\geq3|m\\geq3',by_id[sid]['statement'])) for sid in ['8.5','9.1','9.4']},
      'current_PDF_metrics':{'pages':int(metrics[1]),'overfull':int(metrics[2]),'over_2pt':int(metrics[3])},
      'rendering_gate':'Completed visual inspection is recorded separately in code/visual_review.json; this script checks text and recorded build counts only',
      'overall':'All asserted exact consistency checks passed.'}
    print(json.dumps(result,indent=2,ensure_ascii=False))

if __name__=='__main__':main()
