"""Exact manuscript replacements; source originals are not changed."""
from pathlib import Path
import json,hashlib,re
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'deliverables/work/cdp_audit'
source={r['source_id']:r for r in json.loads((OUT/'source_manifest.json').read_text())}
items=[]
def add(sid,action,reason,file=None,scope=None,edits=None):
 r=source[sid]
 x={'source_id':sid,'action':action,'source_file':'sources/returns/S6_03_CDP/'+r['source_file'].split(';')[0],
 'canonical_file':'sources/'+r['canonical_file'],'canonical_lines':[r['canonical_line_start'],r['canonical_line_end']],
 'original_proof_sha256':r['proof_sha256'],'target_statement_label':'cdp:st:'+sid,'reason':reason}
 if file:
  p=OUT/file;t=p.read_text();x.update(replacement_file=str(p.relative_to(ROOT)),replacement_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),replacement_scope=scope or 'Complete statement and complete proof; preserve all prose before the statement.',
  exact_label_transformations={label:('cdp:'+label if not label.startswith('st:') else 'cdp:'+label) for label in re.findall(r'\\label\{([^}]+)\}',t)})
 if edits:x['exact_text_edits']=edits
 items.append(x)
add('A.1.1','replace full block','Replace the undefined Lead1 pointer by both required H0 vanishings; preserve conormal/torsion notation preceding the theorem.','corrected_A1_1_A2_6_full_proofs.tex','Opening definitions through the end of the A.1.1 proof; the A.2.6 block in this file is a separate replacement.')
add('A.2.6','replace full block','The raw R-module misses orders7 and8; the B-generated normalized module is t^4 B dt. The normalized determinant order remains15.','corrected_A1_1_A2_6_full_proofs.tex','From the A.2.6 statement through its complete proof; do not duplicate A.1.1.')
add('C.3.7','retain full checked source block','The existing CDP proof already repairs Kawai Proposition2 by the finite orbit sum of the divisor after resolution. Preserve this explicit repair and its line-bundle linearization; do not substitute an invariant chosen section or the later multiple-fibre corollary.','extracted/CDP_C_3_7.tex','Complete idstatement and proof; drop only the final next-source comment. The idstatement label st:C.3.7 becomes cdp:st:C.3.7.')
add('C2c','replace full block','Mumford1972 section6 is formal over a complete DVR. The replacement proves the convergent complex-disc quotient, proper discontinuity and properness explicitly.','corrected_C2c_full_proof.tex')
add('C4g','replace full block','For the original affine members H2(Y,Z) in cohomology is torsion Z/d, not zero. Pullback to dP6 is still trivial; use C1.3 under rational Betti vanishings instead of applying integral C4f outside its hypotheses.','corrected_C4g_full_proof.tex')
add('E6','replace full block','Douady section10.2 is fixed-source. The replacement constructs the relative graph germ over the full nonreduced base and retains the complete Artin lifting argument.','corrected_E6_full_proof.tex')
add('E14','typesetting replacement only','Restore the intended epsilon subscripts; no mathematical change.',edits=[{'from':"P'_epsilon",'to':"P'_\\epsilon"},{'from':'f_epsilon','to':'f_\\epsilon'}])
add('E16','typesetting replacement only','Restore the text command after the literal tab in formula(E.16.3).',edits=[{'from':'\text{is represented by}','to':'\\text{is represented by}','from_explanation':'The first character is a literal TAB, followed by ext{is represented by}, not a backslash.'}])
payload={'schema':'paperII-cdp-replacements-v1','checker':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date_utc':'2026-11-17',
 'global_label_rule':{'statement':'Every CDP statement ID receives cdp:st:<exact source ID>.','internal':'Prefix each original internal label and each corresponding ref/eqref target by cdp: once; do not double-prefix. Original manual equation tags can remain until normal renumbering.','cross_paper':'D.1.14 and E9 already belong to Paper I; refer to the existing Paper I theorem labels/numbers rather than recreating them in II.'},
 'replacements':items,
 'open_status_distinctions':[{'source':'INV E2.3','resolved_part':'Comb Kuranishi dimension and smoothness: CDP E15.','remaining_open_part':'The splitting type of K_m is not settled by E15.'}],
 'pending':'The separate WB/CN full supplement and aliases are still being prepared; this manifest does not certify that supplement.'}
(OUT/'paperII_replacements.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
print('Saved',len(items),'exact replacement records')
