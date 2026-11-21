#!/usr/bin/env python3
"""Prepare reviewed candidate17 prose guards; never mutate canonical files."""
from pathlib import Path
import collections
import datetime
import difflib
import hashlib
import importlib.util
import json
import re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/i_cont_edits'
SOURCE_SHA='5b74359a048b1eab3e478a65eab35f35b45474c4c65aadaedd639315c19a9379'
PDF_SHA='3c9f15b28d768f305ab09dfb86ef98365aeb4659329b33e6faedb91864094ab0'
READING_SHA='ae0903f6015f97d8289cb13e81b397f538a3b23aae211a9dc273deffbfccaa56'
sha=lambda b:hashlib.sha256(b).hexdigest()
spec=importlib.util.spec_from_file_location('previous_guard_helpers',ROOT/'code/S6_SERIES_PUBLISH_I_candidate16_edits_guards.py')
helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
commands=lambda s:re.findall(r'\\[A-Za-z@]+\*?|\\.',s)
refs=lambda s:re.findall(r'\\(?:eqref|ref|cref|Cref|cite|citet|citep|SeriesRef)(?:\[[^\]]*\])?\{[^}]+\}',s)

def block_for(s,p):
    if s.startswith('Use the full real period and the absolute height',p):
        start=s.rfind(r'\subsection{',0,p);h=s.index(r'\begin{proposition}',p)
        end=s.index(r'\end{proof}',h)+len(r'\end{proof}')
        return 'ari:C.6.R5',start,end
    if s.startswith('The known calculations isolate',p):
        start=s.rfind(r'\subsection{',0,p);end=s.index(r'\clearpage',p)
        return 'ari:C.7.4',start,end
    h=list(re.finditer(r'\\begin\{(theorem|proposition|lemma|corollary|remark|definition|cited)\}',s[:p]))[-1]
    end=s.index(r'\end{'+h[1]+'}',h.end())+len(r'\end{'+h[1]+'}')
    if re.match(r'\s*\\begin\{proof\}',s[end:]):end=s.index(r'\end{proof}',end)+len(r'\end{proof}')
    assert h.start()<=p<end
    return re.search(r'\\label\{([^}]+)\}',s[h.start():end])[1],h.start(),end

def main():
    protected={name:ROOT/name for name in ['S6_SERIES_PUBLISH_I.tex','S6_SERIES_PUBLISH_defects_I.tsv','CHECK_EVENTS.tsv']}
    protected['reading']=OUT/'S6_SERIES_PUBLISH_I_final_candidate17_reading_edits.json'
    protected['dossier']=OUT/'S6_SERIES_PUBLISH_I_candidate17_type_closure_preparation.json'
    frozen={k:p.read_bytes() for k,p in protected.items()}
    s=frozen['S6_SERIES_PUBLISH_I.tex'].decode()
    assert sha(s.encode())==SOURCE_SHA and sha(frozen['reading'])==READING_SHA
    assert sha((ROOT/'build/I_candidate17/S6_SERIES_PUBLISH_I.pdf').read_bytes())==PDF_SHA
    start=s.index('Use the full real period and the absolute height')
    st=s.index(r'\begin{proposition}',start)
    body=s.index('For the six rank-one rows',st)
    convention='Use the full real period and the absolute height of\n\\cref{I:def:theta-height}.'
    proposals=[
      (271,'D08/D09'," The proof's error bounds also determine\nthe finer intervals recorded with the verification data.",'',
       'Delete the unspecified verification-data pointer at the end of Proposition 24.11. Every numerical value, the stated absolute error below 10^-8, the Taylor-coefficient relation, and the complete Mellin, kernel, block, period, rounding and rank argument remain. The proof retains its explicit finer error bounds; no new interval or theorem claim is introduced.'),
      (275,'D08/D13',s[start:body],s[st:body]+convention+'\n\n',
       'Move the exact full-real-period and absolute-height convention, with its definition reference, inside Proposition 24.16 after StatementRecord and before its existing first sentence. Delete only the accompanying Gross-Zagier denominator-bound announcement. The full twist maps, Heegner data, height comparison, period products, rational bounds and isolation proof remain. Reference and command order changes precisely because the retained convention crosses the proposition header.'),
      (281,'D08','Every surviving covering has a\ndisplayed point; every excluded covering has a recorded local\nobstruction','Every surviving covering has a\npoint; every excluded covering has a local\nobstruction',
       'Remove the display/record bookkeeping adjectives in the two-isogeny descent. The asserted existence of points and local obstructions, both exact descent indices, both obstruction primes, the quotient formula and the torsion conclusion remain. Surviving describes the coverings left by this mathematical descent and is retained; it is not a label for a draft or research candidate.'),
      (51,'D08',' We have exhibited the respective maps and norm equations for the present matrices.','',
       'Delete the first-person recap in the norm-comparison remark. The exact published comparison, scaling 6/r, order-six norm image, present scaling one, parity calculation, map identification and Kodaira-Spencer citation remain.'),
      (63,'D08','Here is a direct comparison map.  ','',
       'Delete the empty introduction to the comparison map. The transitive action, null-vector construction, Hermitian Gram matrix, symplectic comparison and complete density/maximality argument remain. The separate density-to-maximality reduction carries mathematical content and is retained.'),
      (65,'D08','We derive the required value in the present family.  ','',
       'Delete the announcement. The Engel equation, discriminant, exact j identity, derivative 1728, finite-root descent and proper embedding proof remain.'),
      (77,'D08','We also need its multiplication. ','',
       'Delete the statement of a proof need. The branch-intersection algebra, Alexander-Whitney product, explicit cup pairing, exterior-square isomorphism, base-change and relative-duality proof remain.'),
      (81,'D08','We compute the line bundle $\\OO_X(H)$.\nOn the cover at $p_j$, its sections allow poles','Sections of the line bundle $\\OO_X(H)$\non the cover at $p_j$ allow poles',
       'Replace the announcement with the same positive statement about sections on the finite root cover. The line bundle, base point, pole order, character calculation, modifications, exact direct images and full duality argument remain. Every inline mathematical segment stays in the same order.'),
      (108,'D08','We first give the comparison that turns the local calculation into\na computation of the sheaves. ','',
       'Delete the roadmap before the real-torus comparison. The marking, period matrix, translation lifts, averaging, homotopies, chain isomorphisms, finite invariants and every stalk calculation remain.'),
      (109,'D08','For clarity we evaluate the other coefficients with the original\nWeierstrass normalization.','Use the original Weierstrass normalization.',
       'Retain the Weierstrass convention positively and remove the editorial announcement. Its exact x and y substitutions, invariant identities, elliptic coefficient, K2 calculation and joint transverse coefficient are unchanged.'),
      (110,'D08','We use the following character convention.\n','',
       'Delete the announcement immediately before the complete character definition. The coefficient transformation law, pullback-frame sign, integer cocycle, invariant exponents and nilpotent layers remain.'),
      (117,'D08','We first construct the comparison before returning its affine data to the canonical choice. ','',
       'Delete the roadmap. The complete reflected-cover lift, group involution, period and lattice maps, finite and cusp comparisons, exact target datum, normalization shift and group splitting remain.'),
      (146,'D08','rank is exactly three. This confirms the linear algebra of \\cref{fam:src:C.3.1}, \\cref{fam:src:C.3.2}.','rank is exactly three, as in \\cref{fam:src:C.3.1}, \\cref{fam:src:C.3.2}.',
       'State the rank and its two references directly. Delete only the retrospective confirmation framing; all annihilator, closure, quotient, rational-kernel and Chabauty arguments remain.'),
      (329,'D08','The known calculations isolate the precise issue.\n','',
       'Delete the empty lead-in in the final relative-period discussion. The cited open lower bound, full-period convention, exact isogeny, dimension B_Q=0, central action, positive bracket slope, hyperplane and unresolved step remain. No new question or conditional theorem is added.'),
      (109,'D02',' Thus the contraction need not\ncommute with the base Dolbeault operator.','',
       'Delete the redundant nonrequirement clause after the filtration argument. The relative contractions, associated-graded acyclicity, two-step filtration and resulting full-complex acyclicity remain, together with the finite-equivariant comparison. No commuting property is added to a hypothesis or claimed for a map.'),
      (155,'D08','For clarity, its value on $v_0$','Its value on $v_0$',
       'Remove only the empty editorial qualifier. The exact value on v0, zero O component, intersection equations, integral lattice and all homology maps remain.'),
      (290,'D08','For clarity the respective upper bounds before rounding are','The respective upper bounds before rounding are',
       'Remove only the empty editorial qualifier. The unrounded upper bounds, Lambert-series inputs, rational constants, recurrences, tails and Bernstein positivity proof remain. The substantive introductions of sufficient series and rational enclosures are retained.')
    ]
    blocks={};guards=[]
    for i,(page,typ,before,after,reason) in enumerate(proposals,1):
        assert s.count(before)==1,(i,s.count(before));pos=s.index(before)
        label,a,b=block_for(s,pos);bid=f'I17-edits-{i:02d}'
        row=blocks.setdefault(label,{'start':a,'end':b,'original':s[a:b],'proposed':s[a:b],'guards':[]})
        assert row['proposed'].count(before)==1
        row['proposed']=row['proposed'].replace(before,after,1);row['guards'].append(bid)
        assert helper.math_segments(before)==helper.math_segments(after)
        assert collections.Counter(commands(before))==collections.Counter(commands(after))
        assert collections.Counter(refs(before))==collections.Counter(refs(after))
        guards.append({'id':bid,'page':page,'type':typ,'statement_id':label,'source_line':s[:pos].count('\n')+1,'before':before,'after':after,'reason':reason,'source_sha256':SOURCE_SHA,'pdf_sha256':PDF_SHA,'status':'proposed for root exact review; not applied','all_mathematical_segments_identical':True,'inline_math_mentions_removed':[],'inline_math_mentions_added':[],'tex_command_multiset_identical':True,'tex_command_order_identical':commands(before)==commands(after),'citation_reference_multiset_identical':True,'citation_reference_order_identical':refs(before)==refs(after),'mathematical_events_added':0})
    guards[1].update({'relocated_exact_text':convention,'relocation_from':'Unnumbered preface after subsection 24.2','relocation_to':'Inside ari:C.6.R5 after StatementRecord and before its existing first sentence','reference_order_before':refs(guards[1]['before']),'reference_order_after':refs(guards[1]['after'])})
    archives=[]
    for i,(label,row) in enumerate(blocks.items(),1):
        a,b=row['original'],row['proposed'];assert helper.math_segments(a)==helper.math_segments(b)
        assert collections.Counter(commands(a))==collections.Counter(commands(b))
        assert collections.Counter(refs(a))==collections.Counter(refs(b))
        for p in [r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}']:assert re.findall(p,a)==re.findall(p,b)
        stem=OUT/f'S6_SERIES_PUBLISH_I_candidate17_edits_block_{i:02d}'
        paths=[Path(str(stem)+t) for t in ['_original.tex','_proposed.tex','.diff']]
        paths[0].write_text(a);paths[1].write_text(b);paths[2].write_text(''.join(difflib.unified_diff(a.splitlines(True),b.splitlines(True),fromfile=label+'/candidate17',tofile=label+'/proposed')))
        archive={'statement_id':label,'original':str(paths[0].relative_to(ROOT)),'original_sha256':sha(paths[0].read_bytes()),'proposed':str(paths[1].relative_to(ROOT)),'proposed_sha256':sha(paths[1].read_bytes()),'diff':str(paths[2].relative_to(ROOT)),'diff_sha256':sha(paths[2].read_bytes()),'source_line_start':s[:row['start']].count('\n')+1,'source_line_end':s[:row['end']].count('\n')+1,'guards':row['guards'],'complete_owning_source_block_read':True,'all_mathematical_segments_identical':True,'all_label_target_sequences_identical':True,'command_reference_multisets_identical':True,'command_order_identical':commands(a)==commands(b),'reference_order_identical':refs(a)==refs(b),'all_content_outside_exact_guards_byte_identical':True}
        archives.append(archive)
        for g in guards:
            if g['statement_id']==label:g['full_block_archive']=archive
    proposed=s;maps=[]
    for g in guards:
        p=proposed.index(g['before']);maps.append({'position':p,'before':g['before'],'after':g['after'],'guard_id':g['id']});proposed=proposed[:p]+g['after']+proposed[p+len(g['before']):]
    reverse=proposed
    for m in reversed(maps):
        p=m['position'];assert reverse[p:p+len(m['after'])]==m['after'];reverse=reverse[:p]+m['before']+reverse[p+len(m['after']):]
    assert reverse==s
    for k,p in protected.items():assert p.read_bytes()==frozen[k],k
    result={'paper':'I','candidate':17,'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':SOURCE_SHA,'pdf_sha256':PDF_SHA,'defect_log_sha256':sha(frozen['S6_SERIES_PUBLISH_defects_I.tsv']),'reading_record':'agents/i_cont_edits/S6_SERIES_PUBLISH_I_final_candidate17_reading_edits.json','reading_record_sha256':READING_SHA,'guards':guards,'full_blocks':archives,'guard_count':len(guards),'complete_block_count':len(archives),'exact_inverse_map':maps,'proposed_source_sha256':sha(proposed.encode()),'exact_forward_and_inverse_reconstruction_verified':True,'all_mathematical_segments_identical':True,'all_labels_targets_preserved':True,'all_command_reference_multisets_identical':True,'command_reference_order_qualification':'Only I17-edits-02 moves the retained convention reference across the proposition header and StatementRecord. No claim of unchanged command/reference order is made for that relocation.','source_modified':False,'completed_reading_and_dossier_unchanged':True,'mathematical_events_added':0,'additional_full_page_credit':0,'scope':'17 proposed wording/placement changes in 14 complete owning source blocks read against candidate17. The bounded 52 first-person and six Here/For-clarity contexts, and the current-source verification/data paragraphs, are additional prose checks; they receive no independent mathematical or full-page-reading credit.'}
    p=OUT/'S6_SERIES_PUBLISH_I_candidate17_edits_guards.json';assert not p.exists()
    p.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    md=['# Paper I candidate17 — continuation prose guards','',f'Source: `{SOURCE_SHA}`',f'PDF: `{PDF_SHA}`','', 'Seventeen proposals in fourteen complete owning blocks. No canonical edits or new mathematical events. The exact convention relocation changes reference order only; every mathematical segment, label, target and command/reference multiset is retained.','', '| Guard | Page | Type | Statement | Reason |','|---|---:|---|---|---|']
    for g in guards:md.append(f'| {g["id"]} | {g["page"]} | {g["type"]} | `{g["statement_id"]}` | {g["reason"]} |')
    p.with_suffix('.md').write_text('\n'.join(md)+'\n')
    print(json.dumps({'guard_file':str(p.relative_to(ROOT)),'sha256':sha(p.read_bytes()),'guards':len(guards),'complete_blocks':len(archives),'proposed_source_sha256':sha(proposed.encode()),'source_modified':False,'new_mathematical_events':0},indent=2))

if __name__=='__main__':main()
