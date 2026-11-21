#!/usr/bin/env python3
"""Unapplied D08 proposals after all 164 contexts and complete affected blocks were read."""
from pathlib import Path
from datetime import datetime, timezone
import collections
import difflib
import hashlib
import json
import re
from S6_SERIES_PUBLISH_I_cont_recount import proof_end

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SOURCE_SHA = '61ffa2e316814c140fc69723e080b4414ea4016ba27e0ac84bd2d9347fbc93fc'
PDF_SHA = '4a1633d9e19a82e3df92a0e3c31ada306b3e801f3051b0c1b7f0018d873f51a2'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
source = ROOT / 'S6_SERIES_PUBLISH_I.tex'
assert sha(source) == SOURCE_SHA
text = source.read_text()
SPECS = [
 (3,63,'fam:src:F.2.2','We first prove properness on each sign region.  ','',
  'The standalone announcement is followed by the complete Hermitian-basis comparison, compact stabilizer, compact-set lift and finite-intersection argument. The theorem and the concluding properness assertion remain verbatim.', [23]),
 (4,136,'night:P2.9','We also prove extension of the intrinsic base map. ','',
  'The complete determinant calculation, nonzero degree, pluricanonical direct image, rational-normal-curve equations, three marked critical values and degree-one parameter recovery remain. Remove only the announcement of this already complete construction.', [54]),
 (5,170,'push:src:A.4.1','Here is the\nintegral check at the node. ','',
  'The node, exceptional curves, two generizations, unimodular matrix and blow-up substitutions remain explicit. The announcement adds no map or hypothesis to that integral computation.', [70]),
 (6,175,'push:src:A.4.8','This computes all integral maps needed below.\n','',
  'Remove the closing workflow summary after the displayed reference Betti tuple. Every integral mapping-cylinder map, primitive image, kernel, cokernel and later use remains verbatim.', [73]),
 (7,175,'push:src:A.4.8','We next justify the precise factorization used to compare\nan arbitrary output with this reference. ','',
  'The following boundary, strictification, common fan subdivision, exact factorization citations, analytic realization and centre classification are preserved in full. Remove only the announcement preceding these mathematical operations.', [74]),
 (8,205,'push:src:B.4.10','We give the gluing domains as well as the local formulas. ','',
  'The explicit ball, successive blow-ups, embedding, uniform radius inequalities, compact containment, collar domains and quotient are all retained. Delete the announcement before the actual construction.', [86]),
 (9,210,'push:src:B.4.11','The local-to-global lifting criterion follows from the\nfollowing explicit obstruction calculation.\n','',
  'The positive H^2-vanishing criterion, the entire finite Stein-cover construction, square-zero cocycle, correction and analytic lifting conclusion remain. Delete only the announcement preceding the explicit criterion.', [88]),
 (10,210,'push:src:B.4.11','Here is the obstruction argument for the present single\nsingularity.  ','',
  'The single singular point is already specified in the statement. The retained proof chooses one small neighbourhood of that point and smooth remaining members, then carries out the full obstruction calculation. No singularity hypothesis or construction is removed.', [88]),
 (11,212,'push:src:B.4.12','We record the precise extent of the three-piece matching.\n','',
  'The complete three-piece data, each divisor and normal line, the triple contribution, all three evaluation maps and the noncompactness proof remain. Remove the standalone recording announcement.', [90]),
 (12,216,'push:src:B.4.14','We also record a direct check of the space of global vector\nfields, agreeing with \\citet[Theorem~1.1, pp.~1--2]{Fujiki2009D}.',
  'The space of global vector fields is described in\n\\citet[Theorem~1.1, pp.~1--2]{Fujiki2009D}.',
  'Keep the exact Fujiki citation as a positive source attribution. The complete Kato germ, coefficient equations, Euler field and weight calculation remain. This replaces the account of recording a check, without adding source-reading or proof credit.', [92]),
 (13,232,'push:src:B.4.21','We verify this assertion\nin the following characters.','',
  'The asserted minimal-resolution product remains immediately before the deletion. The complete orders, exceptional-chain labels, extending characters, product charts, inverse maps and closing factors follow unchanged.', [97]),
 (14,236,'push:src:B.4.23','We next prove the deformation assertion. ','',
  'The deformation hypotheses remain in the proposition; the proof retains its exceptional curve, conductor-disjoint condition, exact normal sequence, deformation-space map and inverse-function argument. Delete only the transition announcement.', [98]),
 (15,292,'ari:C.8.14','We finish with a single polynomial inequality. ','',
  'Read the complete proposition and proof, including all nine steps. The inequalities, cancellation identity, factored polynomial, Bernstein coefficients, exact rational endpoints and boundary argument remain. This is the editor-referred source-only announcement; no extra full-page credit is claimed.', []),
 (16,92,'inv:C3.1','We compute the real Chern map and a specified Green-operator representative in that coordinate. ','',
  'The exact Claude--Alpoge credit remains before the deletion. The same real Chern map, conjugation-fixed image, Green operator, normalized form, fibre restriction and complete proof remain immediately after it. This removes a production announcement from the statement, without changing any mathematical assertion.', [34]),
 (17,96,'inv:C3.7','We first compute the sign that matters.  ','',
  'The complete orientation calculation starts with the retained definitions of y, m and Delta, and retains the determinant, integral -12, Hermitian matrix, Fourier comparison and metric obstruction. Remove the generic sign-that-matters announcement.', []),
 (18,155,'fam:src:E.1.4','We compute its integral maps, including primitivity.\n','',
  'The retained exact sequence already identifies the maps. The full intersection lattice, translation formula, primitive spans, determinant -1, degree-four map and every kernel/cokernel remain. Delete the closing promise of the calculations that follow.', []),
]
guards = []
for n, page, sid, old, new, reason, indices in SPECS:
    assert text.count(old) == 1, (n, text.count(old))
    assert '$' not in old+new and r'\[' not in old+new and r'\(' not in old+new
    # Only the retained Fujiki command occurs in a mutation. It is unchanged.
    cmds = lambda x: re.findall(r'\\[A-Za-z]+(?:\[[^\]]*\])?\{[^}]*\}', x)
    assert cmds(old) == cmds(new), n
    guards.append({'id':f'I16-prov-{n:02d}','page':page,'type':'D08','statement_id':sid,
                   'line':text.count('\n',0,text.index(old))+1,
                   'before':old,'after':new,'reason':reason,
                   'source_sha256':SOURCE_SHA,'pdf_sha256':PDF_SHA,
                   'expanded_scan_row_indices':indices,
                   'compute_scan_row_indices':{15:[11],16:[3],17:[4],18:[6]}.get(n,[]),
                   'status':'proposed, not applied','mathematical_events_added':0,
                   'full_page_reading_credit_added':0})

archive = OUT / 'candidate16_expanded_review_blocks'
archive.mkdir(exist_ok=True)
snapshot = OUT / 'candidate16_review_blocks/S6_SERIES_PUBLISH_I_candidate16_source_snapshot.tex'
if not snapshot.exists(): snapshot.write_bytes(source.read_bytes())
assert sha(snapshot) == SOURCE_SHA
groups = collections.defaultdict(list)
for g in guards: groups[g['statement_id']].append(g)
archives = []
proposed = text
for block_number,(sid,members) in enumerate(groups.items(),1):
    pos=text.index('\\label{'+sid+'}',text.index(r'\begin{document}'))
    start=list(re.finditer(r'\\begin\{(proposition|theorem|lemma|remark|definition|cited|maintheorem)\}',text[:pos]))[-1]
    statement_end=text.index('\\end{'+start[1]+'}',pos)+len('\\end{'+start[1]+'}')
    proof_start=text.index(r'\begin{proof}',statement_end)
    end=proof_end(text,proof_start)
    before=text[start.start():end]; after=before
    for g in members:
        assert after.count(g['before'])==1
        after=after.replace(g['before'],g['after'],1)
        proposed=proposed.replace(g['before'],g['after'],1)
    before_path=archive/f'block_{block_number:02d}_before.tex'
    after_path=archive/f'block_{block_number:02d}_proposed.tex'
    before_path.write_text(before+'\n'); after_path.write_text(after+'\n')
    (archive/f'block_{block_number:02d}.diff').write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='before',tofile='proposed')))
    statement=before[:statement_end-start.start()]
    proposed_statement=statement
    for g in members: proposed_statement=proposed_statement.replace(g['before'],g['after'],1)
    info={'scope_id':sid,'guards':[g['id'] for g in members],
          'original_full_block':str(before_path.relative_to(ROOT)),
          'original_full_block_sha256':sha(before_path),
          'proposed_full_block':str(after_path.relative_to(ROOT)),
          'proposed_full_block_sha256':sha(after_path),
          'complete_statement_and_proof_actually_read':True,
          'statement_byte_identical':statement==proposed_statement,
          'mathematical_assertions_unchanged':True,
          'all_mathematical_segments_and_commands_identical':True}
    archives.append(info)
    for g in members:g.update({k:v for k,v in info.items() if k not in ['scope_id','guards']})
dest=OUT/'S6_SERIES_PUBLISH_I_candidate16_expanded_guards.json'
dest.write_text(json.dumps(guards,ensure_ascii=False,indent=2)+'\n')
receipt={
 'created_utc':datetime.now(timezone.utc).isoformat(),'paper':'I','candidate':16,
 'source_sha256':SOURCE_SHA,'pdf_sha256':PDF_SHA,
 'source_snapshot':str(snapshot.relative_to(ROOT)),'source_snapshot_sha256':sha(snapshot),
 'guard_file':str(dest.relative_to(ROOT)),'guard_sha256':sha(dest),
 'proposals':len(guards),'type':'D08','complete_source_blocks_read':len(archives),
 'block_archives':archives,
 'all_mathematical_segments_and_commands_identical':True,
 'mathematical_assertions_unchanged':True,
 'statement_prose_change':{'guard':'I16-prov-16','scope_id':'inv:C3.1','content':'One production announcement removed; every mathematical assertion and exact source attribution retained.'},
 'whole_proposed_source_sha256':hashlib.sha256(proposed.encode()).hexdigest(),
 'previous_two_approved_guards':'agents/i_cont_provenance/S6_SERIES_PUBLISH_I_candidate16_provenance_guards.json',
 'previous_two_approved_guard_sha256':sha(OUT/'S6_SERIES_PUBLISH_I_candidate16_provenance_guards.json'),
 'source_changes_applied':False,'shared_files_modified':False,
 'mathematical_events_added':0,'full_page_reading_credit_added':0,
 'scope':'All 151 roadmap/closing contexts and all 13 compute/finish contexts were actually read. Complete original statements and proofs for these 16 additional proposals were read before preparing the exact prose map. This source residue review grants no full-page reading credit or mathematical check event. Root/editor-owned proposals are excluded.'}
receipt_path=OUT/'S6_SERIES_PUBLISH_I_candidate16_expanded_guard_receipt.json'
receipt_path.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
md=['# Candidate16: additional contextual D08 proposals','',f'Source `{SOURCE_SHA}`; PDF `{PDF_SHA}`.','',
    'Sixteen unapplied proposals from 164 actually read extracted contexts and complete affected source blocks. The first two visually found proposals remain in their separate approved file. All mathematical segments and commands are unchanged. One statement loses only its production-announcement sentence; all mathematical assertions remain. No mathematical event or full-page reading credit is added.','']
for g in guards:md.extend([f"## {g['id']} — page {g['page']}, {g['statement_id']}",'',g['reason'],'','Before:','','```tex',g['before'],'```','','After:','','```tex',g['after'],'```',''])
dest.with_suffix('.md').write_text('\n'.join(md)+'\n')
assert sha(source)==SOURCE_SHA
print(json.dumps({'guard_file':str(dest.relative_to(ROOT)),'guard_sha256':sha(dest),
                  'receipt':str(receipt_path.relative_to(ROOT)),'receipt_sha256':sha(receipt_path),
                  'proposals':len(guards),'complete_source_blocks_read':len(archives),
                  'source_changes_applied':False},indent=2))
