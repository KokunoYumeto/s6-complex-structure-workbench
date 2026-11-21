#!/usr/bin/env python3
"""Versioned six-guard candidate18 proposal; preserve initial four-guard history."""
from pathlib import Path
import collections
import datetime
import difflib
import hashlib
import json
import re
from S6_SERIES_PUBLISH_I_candidate17_combined import block, math, displays, refs, write_stable
from S6_SERIES_PUBLISH_I_candidate18_edits_guards import PROPOSALS, SOURCE, PDF, READING
from S6_SERIES_PUBLISH_synctex_batch import Scanner

R=Path(__file__).resolve().parents[1]
O=R/'agents/i_cont_edits'
sha=lambda b:hashlib.sha256(b).hexdigest()
commands=lambda s:re.findall(r'\\[A-Za-z@]+\*?|\\.',s)
INITIAL='df139808a042e1234e92757f2183e55e27b910a626942c01b78e008624517798'
EXTRA=[
 (240,(239,240),'D08',
  'The displayed coherent direct-image exact sequence proves the\nrequired local constancy on the punctured disc.\n','',[],
  'Delete the recap after the exact direct-image calculation. The complete exact sequence, its vanishing last term, h^0 equal to rank M for every sufficiently small nonzero parameter, and contradiction with the accumulating resonances remain. No map, quantity, hypothesis, reference or mathematical segment is removed.',
  ['The last term vanishes. Therefore\n$h^0(H_a,K_{H_a}^{-1})=\\operatorname{rank}M$ for\n\\emph{every} sufficiently small $a\\ne0$. This\ncontradicts \\eqref{pub:I:eq:B-4-25-5} and the accumulating resonances.']),
 (214,(213,215),'D11',
  ' The original finite-support argument\nalso covers modifications where that normal-degree test alone\nwould give no information.','',[],
  'Delete the repeated scope comparison at the end of the normal-degree step. The initial statement already gives the finite-modification assertion and the nonzero-normal-degree assertion with their exact hypotheses. The full finite-image/equivariance/orbit proof in steps1–3 and the derivative/Abel–Jacobi normal-line proof in step4 remain. The removed sentence adds no map, formula or case definition; no new comparison of the two methods is asserted.',
  ['Suppose $p:Y\\to H$ is a finite composition of point blow-ups,\nallowing infinitely near centres, and at least one point of $E$\nis an image of its exceptional locus.',
   'More generally, if a compact smooth surface contains a preserved\nmarked elliptic curve $E$ of nonzero normal degree $d$, every\nholomorphic automorphism restricting to translation by $b$ on $E$\nmust satisfy $d\\,b=0$ in $E$.',
   'Thus preservation of $N$ forces $d b=0$.'])
]


def main():
 sp=R/'S6_SERIES_PUBLISH_I.tex'; pp=R/'build/I_candidate18/S6_SERIES_PUBLISH_I.pdf'
 rp=O/'S6_SERIES_PUBLISH_I_final_candidate18_reading_edits.json'
 ip=O/'S6_SERIES_PUBLISH_I_candidate18_edits_guards.json'
 paths={sp,R/'S6_SERIES_PUBLISH_defects_I.tsv',R/'CHECK_EVENTS.tsv',rp,ip}
 for pattern in ['S6_SERIES_PUBLISH_I_final_candidate*_reading_edits.json','S6_SERIES_PUBLISH_I_candidate*_type_closure_preparation.json','S6_SERIES_PUBLISH_I_candidate18_edits_block_*']:
  paths.update(O.glob(pattern))
 protected={p:p.read_bytes() for p in paths}
 source=protected[sp].decode();initial=json.loads(protected[ip])
 assert sha(protected[sp])==SOURCE and sha(pp.read_bytes())==PDF
 assert sha(protected[rp])==READING and sha(protected[ip])==INITIAL
 guards=[];blocks={};proposed=source;maps=[]
 with Scanner(pp) as scanner:
  for i,(page,page_bounds,typ,old,new,removed,reason,witnesses) in enumerate(PROPOSALS+EXTRA,1):
   gid=f'I18-edits-{i:02d}';assert source.count(old)==1
   pos=source.index(old);label,a,b,kind=block(source,pos)
   row=blocks.setdefault(label,{'start':a,'end':b,'original':source[a:b],'proposed':source[a:b],'guards':[],'page_bounds':page_bounds,'removed':[]})
   assert row['proposed'].count(old)==1
   row['proposed']=row['proposed'].replace(old,new,1)
   row['guards'].append(gid);row['removed']+=removed
   assert collections.Counter(math(old))-collections.Counter(math(new))==collections.Counter(removed)
   assert not(collections.Counter(math(new))-collections.Counter(math(old)))
   assert displays(old)==displays(new) and commands(old)==commands(new) and refs(old)==refs(new)
   ws=[]
   for w in witnesses:
    assert row['original'].count(w)==row['proposed'].count(w)==1,(gid,w)
    ws.append({'exact_text':w,'sha256':sha(w.encode()),'source_line':source[:a+row['original'].index(w)].count('\n')+1,'preserved_byte_identically':True})
   line=source[:pos].count('\n')+1
   pages=sorted({p for ln in range(line,line+old.count('\n')+1) for p in scanner.pages(sp,ln)})
   assert page in pages,(gid,page,pages)
   guards.append({'id':gid,'page':page,'type':typ,'statement_id':label,'source_line':line,'before':old,'after':new,'reason':reason,'source_sha256':SOURCE,'pdf_sha256':PDF,'candidate18_synctex_pages':pages,'retained_witnesses':ws,'inline_math_mentions_removed':removed,'inline_math_mentions_added':[],'all_mathematical_segments_identical':not bool(removed),'all_display_mathematical_segments_identical':True,'all_remaining_inline_math_in_identical_order':True,'tex_command_sequence_identical':True,'citation_reference_sequence_identical':True,'all_labels_targets_preserved':True,'status':'proposed for root exact review; not applied','mathematical_events_added':0})
   q=proposed.index(old);maps.append({'guard_id':gid,'position':q,'before':old,'after':new});proposed=proposed[:q]+new+proposed[q+len(old):]
 archives=[]
 for i,(label,row) in enumerate(blocks.items(),1):
  original,replacement=row['original'],row['proposed']
  assert displays(original)==displays(replacement) and commands(original)==commands(replacement) and refs(original)==refs(replacement)
  assert collections.Counter(math(original))-collections.Counter(math(replacement))==collections.Counter(row['removed'])
  assert not(collections.Counter(math(replacement))-collections.Counter(math(original)))
  expected=original
  for g in guards:
   if g['id'] in row['guards']:expected=expected.replace(g['before'],g['after'],1)
  assert expected==replacement and math(expected)==math(replacement)
  assert re.findall(r'\\(?:label|hypertarget)\{[^}]+\}',original)==re.findall(r'\\(?:label|hypertarget)\{[^}]+\}',replacement)
  end=original.index(r'\end{proposition}')+len(r'\end{proposition}')
  assert replacement.startswith(original[:end])
  stem=O/f'S6_SERIES_PUBLISH_I_candidate18_edits_v2_block_{i:02d}'
  pa,pb,pd=[Path(str(stem)+x) for x in ['_original.tex','_proposed.tex','.diff']]
  write_stable(pa,original);write_stable(pb,replacement)
  write_stable(pd,''.join(difflib.unified_diff(original.splitlines(True),replacement.splitlines(True),fromfile=label+'/candidate18',tofile=label+'/six-guard-proposal')))
  arc={'statement_id':label,'original':str(pa.relative_to(R)),'original_sha256':sha(pa.read_bytes()),'proposed':str(pb.relative_to(R)),'proposed_sha256':sha(pb.read_bytes()),'diff':str(pd.relative_to(R)),'diff_sha256':sha(pd.read_bytes()),'source_line_start':source[:row['start']].count('\n')+1,'source_line_end':source[:row['end']].count('\n')+1,'printed_page_start':row['page_bounds'][0],'printed_page_end':row['page_bounds'][1],'kind':'complete statement and attached proof','guards':row['guards'],'complete_original_statement_and_proof_read':True,'full_statement_byte_identical':True,'all_display_mathematical_segments_identical':True,'all_inline_mathematical_segments_identical':not bool(row['removed']),'removed_repeated_inline_mentions':row['removed'],'all_remaining_inline_math_in_identical_order':True,'all_command_reference_label_target_sequences_identical':True,'all_content_outside_exact_guards_byte_identical':True}
  archives.append(arc)
  for g in guards:
   if g['id'] in row['guards']:g['full_block_archive']=arc
 reverse=proposed
 for m in reversed(maps):
  q=m['position'];assert reverse[q:q+len(m['after'])]==m['after'];reverse=reverse[:q]+m['before']+reverse[q+len(m['after']):]
 assert reverse==source and displays(source)==displays(proposed) and refs(source)==refs(proposed) and commands(source)==commands(proposed)
 permitted=source
 for g in guards:
  if g['inline_math_mentions_removed']:permitted=permitted.replace(g['before'],g['after'],1)
 assert math(permitted)==math(proposed)
 for g in guards:
  for w in g['retained_witnesses']:assert proposed.count(w['exact_text'])==1
 for old,g in zip(initial['guards'],guards[:4]):
  for key in ['id','before','after','type','reason','inline_math_mentions_removed']:
   assert old[key]==g[key],(g['id'],key)
 for p,raw in protected.items():assert p.read_bytes()==raw,p
 result={'paper':'I','candidate':18,'version':2,'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':SOURCE,'pdf_sha256':PDF,'defect_log_sha256':sha(protected[R/'S6_SERIES_PUBLISH_defects_I.tsv']),'check_ledger_sha256':sha(protected[R/'CHECK_EVENTS.tsv']),'reading_record':str(rp.relative_to(R)),'reading_record_sha256':READING,'guards':guards,'full_blocks':archives,'guard_count':len(guards),'complete_block_count':len(archives),'supersedes':{'path':str(ip.relative_to(R)),'sha256':INITIAL,'meaning':'Use this six-guard batch in place of the initial four-guard batch. IDs01–04 and their literal substitutions/reasons are identical; IDs05–06 extend the two existing owning-proof pairs. The historical four-guard file and all of its archives remain unchanged.'},'exact_inverse_map':maps,'proposed_source_sha256':sha(proposed.encode()),'exact_forward_and_inverse_reconstruction_verified':True,'all_display_mathematical_segments_identical':True,'all_inline_mathematical_segments_identical':False,'inline_math_qualification':'Only repeated $E$ in I18-edits-01 and repeated $Y$ in I18-edits-03 are removed with redundant prose; every other inline segment remains in identical order. Exact unchanged definitions and operative witnesses are bound. No reference or TeX command is removed.','all_command_reference_label_target_sequences_identical':True,'all_statements_byte_identical':True,'source_modified':False,'canonical_status_modified':False,'completed_reading_and_dossier_unchanged':True,'mathematical_events_added':0,'additional_full_page_credit':0,'retained_contextual_dispositions':initial['retained_contextual_dispositions'],'scope':'Six guarded wording deletions in four complete statements/proofs, following the33 actual full-page readings. All complete original blocks were read. Exact merged proposed blocks, retained witnesses and reversible literal maps are saved for final full-pair review. Root approval/application and later rendered bindings remain separate.'}
 out=O/'S6_SERIES_PUBLISH_I_candidate18_edits_guards_v2.json';assert not out.exists()
 out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 md=['# Paper I candidate18 — six guarded prose proposals','',f'Source: `{SOURCE}`',f'PDF: `{PDF}`',f'Immutable actual reading: `{READING}`','',f'This version supersedes the initial four-guard batch `{INITIAL}` without modifying that historical record. The four original substitutions are identical. Two further complete-context deletions are added in the existing B.4.13 and B.4.25 blocks.','', 'Six proposals: three D02, two D08 and one D11. All statements, displayed mathematics, labels, targets, TeX commands and references remain byte-identical. Two repeated inline symbol mentions, E and Y, are explicitly removed with their clauses and mapped to unchanged definitions and operative uses.','', '| Guard | Page | Type | Owning statement | Reason |','|---|---:|---|---|---|']
 for g in guards:md.append(f"| {g['id']} | {g['page']} | {g['type']} | `{g['statement_id']}` | {g['reason']} |")
 out.with_suffix('.md').write_text('\n'.join(md)+'\n')
 print(json.dumps({'guard_file':str(out.relative_to(R)),'sha256':sha(out.read_bytes()),'guards':len(guards),'complete_blocks':len(archives),'proposed_source_sha256':sha(proposed.encode()),'source_modified':False,'mathematical_events_added':0},indent=2))


if __name__=='__main__':main()
