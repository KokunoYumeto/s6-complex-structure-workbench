#!/usr/bin/env python3
"""Read-only current-manuscript continuation of the full PUSH C comparison."""
from pathlib import Path
import hashlib, json, re
from datetime import datetime, timezone

D = Path(__file__).resolve().parents[2]
W = D/'work/cdp_audit/push_C_retention'

def sha(s): return hashlib.sha256(s.encode()).hexdigest()

def drop_uses(s):
    chunks=[];last=0
    for m in re.finditer(r'\\Uses\{',s):
        if m.start()<last:continue
        i=m.end();depth=1
        while depth:
            if s[i]=='{' and s[i-1]!='\\':depth+=1
            if s[i]=='}' and s[i-1]!='\\':depth-=1
            i+=1
        chunks.append(s[last:m.start()]);last=i
    chunks.append(s[last:]);return ''.join(chunks)

def canon(s):
    s=re.sub(r'(?<!\\)%[^\n]*','',s)
    s=drop_uses(s)
    s=re.sub(r'\\label\{[^}]+\}','',s)
    s=re.sub(r'\\(?:sub)*section\*?\{[^\n]+\}\s*','',s)
    s=re.sub(r'\\(?:Verified|AuthorSelfCheck|NeedsCheck|Refuted)\b','',s)
    return re.sub(r'\s+',' ',s).strip()

full=json.loads((W/'full_retention_review.json').read_text())
prior=json.loads((W/'final_integrated_retention.json').read_text())
replacements=json.loads((W/'editorial_findings.json').read_text())['replacements']
current=(D/'S6_09_PAPERS_III.tex').read_text();normal=canon(current)
planned=current
regressions=[]
for c in replacements:
    count=planned.count(c['before'])
    if count:
        regressions.append({**c,'current_regressed_before_count':count,
                            'current_after_count':current.count(c['after'])})
        planned=planned.replace(c['before'],c['after'])
planned_normal=canon(planned)
rows=[]
for old in full['rows']:
    if old['paper']!='III':continue
    sid=old['source_id'];path=W/(sid.replace('.','_')+'.printed.tex')
    expected=path.read_text();used=[]
    for change in replacements:
        if change['source_id']!=sid:continue
        n=expected.count(change['before'])
        if n:
            expected=expected.replace(change['before'],change['after'])
            used.append({'before':change['before'],'after':change['after'],'occurrences':n})
    n=canon(expected);found=n in normal
    rows.append({'source_id':sid,'printed_label':old['printed_label'],
      'source_ranges':old['source_ranges'],'source_sha256':old['source_sha256'],
      'preserved_previous_full_printed_block':str(path.relative_to(D)),
      'previous_printed_block_sha256':sha(path.read_text()),
      'exact_documented_replacements_applied_for_comparison':used,
      'expected_current_complete_block_sha256':sha(expected),
      'complete_block_retained_after_only_documented_changes_and_normalization':found,
      'complete_block_matches_after_only_reinstating_regressed_documented_edits':n in planned_normal,
      'complete_argument_route_already_read':old['argument_route_retained'],
      'source_display_count':old['displayed_formulas'],
      'scope':'Complete block-string continuation of the independently read source-to-print comparison; generated Uses, labels, section headings, comments and whitespace are ignored. No new mathematical proof audit is claimed.'})

checks=[]
for c in replacements:
    checks.append({'source_id':c['source_id'],'before':c['before'],'after':c['after'],
                   'before_count_in_current':current.count(c['before']),
                   'after_count_in_current':current.count(c['after'])})
pdf=D/'S6_09_PAPERS_III.pdf'
record={'reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date':'2026-11-17 UTC',
 'timestamp_utc':datetime.now(timezone.utc).isoformat(),
 'III_tex_sha256':sha(current),'III_pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
 'prior_complete_read_record':'work/cdp_audit/push_C_retention/full_retention_review.json',
 'prior_integrated_tex_sha256':prior['III_tex_sha256'],
 'all_34_complete_III_blocks_retained':all(r['complete_block_retained_after_only_documented_changes_and_normalization'] for r in rows),
 'all_34_complete_blocks_match_after_only_reinstating_regressed_documented_edits':all(r['complete_block_matches_after_only_reinstating_regressed_documented_edits'] for r in rows),
 'all_16_documented_replacements_remain_present':all(c['before_count_in_current']==0 and c['after_count_in_current']>0 for c in checks),
 'III_result_blocks':len(rows),'III_source_displays_retained':sum(r['source_display_count'] for r in rows),
 'rows':rows,'exact_editorial_changes':checks,
 'Paper_I_unique_C3_5_scope':'The separate complete source-to-print comparison and all twelve displays remain in full_retention_review.json. This continuation rereads/compares the 34 PaperIII blocks only; final PaperI visual/source hash chain is separately recorded.',
 'paper_mutated':False,'original_source_mutated':False}
(W/'current_final_retention.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
(W/'current_editorial_regressions.json').write_text(json.dumps({'reader':record['reader'],
 'effort':'Pro','date':'2026-11-17 UTC','III_tex_sha256':sha(current),
 'regressed_replacements':regressions,'count':len(regressions),
 'all_complete_source_argument_blocks_match_after_only_these_repairs':record['all_34_complete_blocks_match_after_only_reinstating_regressed_documented_edits'],
 'paper_mutated':False,'scope':'Exact current-source regression in previously approved standalone wording; no new mathematical replacement or general polishing.'},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k not in ['rows','exact_editorial_changes']},indent=2))
if not record['all_34_complete_III_blocks_retained']:
    print('FAILED',[r['source_id'] for r in rows if not r['complete_block_retained_after_only_documented_changes_and_normalization']])
    raise SystemExit(1)
assert record['all_16_documented_replacements_remain_present']
