#!/usr/bin/env python3
"""Serialize actual GN comparison/evidence. No canonical source/ledger writes."""
from pathlib import Path
import hashlib,json,re,datetime
B=Path(__file__).resolve().parents[3]; P=Path(__file__).resolve().parent
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bind(p):return {'path':str(p.relative_to(B)),'sha256':h(p),'bytes':p.stat().st_size}
def save(p,x):
    assert not p.exists(),p
    p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
prepared=P/'S6_SERIES_PUBLISH_II_01GN_guards_v2.json'
data=json.loads(prepared.read_text());g=data['guards'][0]
old=g['before'];new=g['after']
fwd=old
for e in g['literal_edits']:
    q=e['sequential_before_offset']; assert fwd[q:q+len(e['before'])]==e['before']
    fwd=fwd[:q]+e['after']+fwd[q+len(e['before']):]
assert fwd==new
inverse=new
for e in reversed(g['literal_edits']):
    q=e['sequential_before_offset'];assert inverse[q:q+len(e['after'])]==e['after']
    inverse=inverse[:q]+e['before']+inverse[q+len(e['after']):]
assert inverse==old
inline=lambda t:re.findall(r'(?<!\\)\$(?!\$)(.*?)(?<!\\)\$',t,re.S)
oi=inline(old);ni=inline(new);oi.remove(r'\langle1\rangle')
q=0
for x in oi:q=ni.index(x,q)+1
od=re.findall(r'\\\[(.*?)\\\]',old,re.S);nd=re.findall(r'\\\[(.*?)\\\]',new,re.S)
q=0
for x in od:q=nd.index(x,q)+1
anchors=lambda t:re.findall(r'\\(?:label|hypertarget)\{[^}]*\}',t)
assert anchors(old)==anchors(new)
refs=lambda t:re.findall(r'\\(?:ref|eqref|SeriesRef|cref|Cref)\{([^}]*)\}',t)
ro=refs(old);rn=refs(new);q=0
for x in ro:q=rn.index(x,q)+1
O=B/g['original_full_block'];N=B/g['proposed_full_block']
assert O.read_text()==old and N.read_text()==new
scope={'created_utc':now,'original_block':bind(O),'proposed_block':bind(N),
 'literal_edit_count':len(g['literal_edits']),'exact_forward_and_inverse':True,
 'original_display_count':len(od),'final_display_count':len(nd),
 'all_original_displayed_math_byte_identical_in_order':True,
 'all_original_inline_math_byte_identical_in_order_except_iteration_marker':True,
 'removed_inline_only':r'\langle1\rangle',
 'all_original_references_retained_in_order':True,
 'added_existing_reference':['cdp:eq:E.16.3'],
 'all_labels_and_hypertargets_identical':True,
 'mathematical_statement_scope_unchanged':True,
 'statement_literal_changes':['Remove actual before Kodaira--Spencer matrix.','Delete redundant clause about an unspecified section; the opening quantifier fixes sigma.'],
 'whole_original_and_final_statement_and_all_five_proof_items_actually_read':True,
 'reading_attestation':'The checker read the complete released original, complete current original, complete v1 proposal, and complete original/v2 proposal together; every item was compared against the frozen derivation. The final v2 block is the only final proposed proof.',
 'events_added':0,'canonical_mutations':0}
validation=P/'S6_SERIES_PUBLISH_II_01GN_full_pair_validation.json';save(validation,scope)

# Source-bound incoming-reference metadata only. No unexposed receiving
# proof text is displayed or used as an independent derivation input.
src=B/'S6_SERIES_PUBLISH_II.tex';s=src.read_text()
labels={'cdp:st:E16','cdp:eq:E.16.1','cdp:eq:E.16.2','cdp:eq:E.16.3'}
owners=[]
for m in re.finditer(r'\\begin\{(proposition|theorem|lemma|corollary|definition|remark)\}',s):
    end=s.find(r'\end{'+m.group(1)+'}',m.end())
    if end<0:continue
    head=s[m.end():end];lab=re.search(r'\\label\{([^}]+)\}',head)
    if lab: owners.append((m.start(),lab.group(1)))
refs_found=[]
for m in re.finditer(r'\\(ref|eqref|SeriesRef|cref|Cref)\{([^}]+)\}',s):
    matches=labels.intersection(x.strip() for x in m.group(2).split(','))
    if not matches:continue
    owner=next((lab for pos,lab in reversed(owners) if pos<m.start()),None)
    region='preamble_or_reference_macro' if m.start()<s.index(r'\begin{document}') else 'document'
    refs_found.append({'target_labels':sorted(matches),'command':m.group(1),'line':s.count('\n',0,m.start())+1,'character_offset':m.start(),'nearest_statement_owner':owner,'region':region})
receiver=P/'S6_SERIES_PUBLISH_II_01GN_receiving_reference_metadata.json'
save(receiver,{'created_utc':now,'source_sha256':hashlib.sha256(s.encode()).hexdigest(),'references':refs_found,
 'scope':'Exact reference labels and nearest owning statement metadata only; no full receiving-proof reading is claimed.',
 'interface_map':'Every target label/hypertarget and mathematical statement is retained by the final guard. The two coefficient corrections alter proof identifications only; ranks, orders and polynomial conclusions received by other statements are unchanged.',
 'canonical_mutations':0,'events_added':0})

freeze=B/'agents/ii_infra/derivation_freezes/01GN/20261121T233516078920Z/S6_SERIES_PUBLISH_derivation_freeze_receipt.json'
release=B/'agents/ii_infra/released_proofs/01GN/0852d8fc0843f270/S6_SERIES_PUBLISH_release_receipt.json'
GL=B/'agents/ii_checks_provenance/recovery_20261121T2000Z/clean_group12/S6_SERIES_PUBLISH_II_01GL_proposed_v2.tex'
public=P/'GN_primary_pdf/S6_SERIES_PUBLISH_Viaclovsky2026Combs_v1_actual_reading_receipt.json'
steps=[
 {'item':1,'printed_step':'Original rank input and higher-root chain rule.',
  'frozen_derivation':'Section2: translations z->z+a, identity differential and real-torus homotopy; explicit [X:Y]->[X^l:Y^k] and local u=s^k,s^l derivative factors.',
  'comparison':'Same ranks and full-cover scope. E8 is a declared cited input, not a new E8 check. No original/affine total-space isomorphism is inferred.'},
 {'item':2,'printed_step':'Weights7,6,6,5; determinant degree12; two nodal zeros and order-four root zero.',
  'frozen_derivation':'Section3: explicit weighted matrix and determinant x^4 Q2(x^4,y), with the two distinct nodal linear factors; exact logarithmic period diag(1,epsilon)/(2 pi i).',
  'comparison':'All zero orders agree. The generic polynomial coefficient certificate checks the weighted multiplication separately from the printed divisor-degree argument. The final proof includes the missing 2 pi i factor.'},
 {'item':3,'printed_step':'LR weights3,2,2,1 and determinant C x^4.',
  'frozen_derivation':'Section4: invertible Weierstrass coordinate map and named primary e/f lattice map; invariant J with determinant4; exact cusp sixfold reduction and coherent frame factors; nonzero determinant c^2/18; weighted C x^4.',
  'comparison':'Same complete rank locus. The original root coordinate and cusp logarithmic conventions agree under the explicit frame maps. The full final GL cited input was read only after GN release and supplies its own logarithmic tangent sequence/pairing extension.'},
 {'item':4,'printed_step':'detV=detG=O(24m-1) and weighted polynomial y^2 P(x^4,y^3).',
  'frozen_derivation':'Section5: actual D_n Psi D_n^-1 root lift, unchanged finite characters, tautological determinant with marked volume, coarse degree2m and pullback O(2m)->O(24m); all-m exponent bijection.',
  'comparison':'All degrees and polynomial claims agree. The final proof adds the root/character transport that identifies the coarse input with these root bundles. Finite enumeration m<=80 is expressly supplemental to the universal congruence proof.'},
 {'item':5,'printed_step':'Four-column determinant E.16.3, frame transformations and cusp leading matrix.',
  'frozen_derivation':'Section1 quotient graph matrix DZ+A21+A22Z-ZA11-ZA12Z; Section5 logarithmic matrix (2 pi i)^-1 I+qHprime.',
  'comparison':'The graph projection equals the printed determinant after the displayed U->U U0^-1 frame map. The postrelease certificate also proves the six two-minor expansion and exact frame factors. Two coefficient-identification statements are repaired; the rank-divisor conclusion is unchanged.'}]
errors=[
 {'type':'D25','location':'E16 proof item5, tangent-frame sentence',
  'old':'Changing a root parameter gives the inverse square of the tangent-frame change.',
  'exact_map':'Dprime=aD sends each differentiated column to a times that column, hence determinant coefficient to a^2. The dual differential frame changes by a^-1, and its square by a^-2.',
  'explicit_test':'For U=(e1,e2), differentiated columns(e3,e4) and Dprime=2D, the coefficient changes from1 to4, whereas the literal inverse-square rule would give1/4.',
  'resolution':'Display coefficient and differential-frame maps and their product. Labels, determinant line, ranks and all statement conclusions are unchanged.',
  'statement_refuted':False},
 {'type':'D25','location':'E16 proof items2 and5, integral leading-matrix wording',
  'old':'The logarithmic derivative is identified literally with an integral monodromy matrix while D=q d/dq is fixed.',
  'exact_map':'In the primary frame e_i=alpha_i+(log q)/(2 pi i) beta_i, nabla e_i=beta_i dq/(2 pi iq). Thus the quotient derivative is (2 pi i)^-1 diag(1,epsilon), and at the comb cusp (2 pi i)^-1 I. With cohomological N=T-I, the source convention gives N e_i=-f_i, so the residue is -N/(2 pi i).',
  'resolution':'Use the exact period derivative and its nonzero scalar; rank and zero orders stay the same.',
  'statement_refuted':False}]
comparison={
 'created_utc':now,'tag':'01GN','statement_id':'cdp:st:E16','checker':'restore_build',
 'status':'Complete fresh target check and complete original/final comparison; root application/admission pending.',
 'derivation':bind(P/'S6_SERIES_PUBLISH_II_01GN_prereading_derivation_v2.md'),
 'freeze_receipt':bind(freeze),'release_receipt':bind(release),
 'input_receipt':bind(P/'S6_SERIES_PUBLISH_II_01GN_prereading_input_receipt_v2.json'),
 'original_full_block':bind(O),'proposed_full_block':bind(N),'prepared_guard':bind(prepared),
 'full_pair_validation':bind(validation),'receiving_reference_metadata':bind(receiver),
 'fresh_program':bind(P/'S6_SERIES_PUBLISH_II_01GN_prereading_certificate_v2.py'),
 'fresh_output':bind(P/'S6_SERIES_PUBLISH_II_01GN_prereading_certificate_output_v2.json'),
 'postrelease_program':bind(P/'S6_SERIES_PUBLISH_II_01GN_postrelease_frame_certificate.py'),
 'postrelease_output':bind(P/'S6_SERIES_PUBLISH_II_01GN_postrelease_frame_certificate_output.json'),
 'program_scope_audit':bind(P/'S6_SERIES_PUBLISH_II_01GN_postrelease_program_scope_audit.json'),
 'program_table_proposal':bind(P/'S6_SERIES_PUBLISH_II_01GN_program_table_proposal_v2.json'),
 'public_primary_reading':bind(public),
 'postrelease_cited_input':{'full_GL_final_block':bind(GL),'actually_read_complete_statement_and_all_12_proof_items':True,'used_for':'Compare the printed E14 dependency and cusp/logarithmic extension after GN freeze; no retroactive prereading claim.'},
 'steps':steps,'proof_errors':errors,
 'all_original_and_final_proof_items_actually_read':True,
 'whole_fresh_and_postrelease_programs_and_outputs_actually_read':True,
 'new_independent_owner_count':1,'actual_comparative_rereading_owner_count':1,
 'additional_independent_credit_for_postrelease_work':0,
 'additional_computation_credit_requested':0,
 'mathematical_statement_unchanged':True,'literal_edits':len(g['literal_edits']),
 'canonical_mutations':0,'events_added':0}
cp=P/'S6_SERIES_PUBLISH_II_01GN_comparison.json';save(cp,comparison)
md='''# E16 complete comparison

The frozen derivation establishes all five parts of the statement from its
declared inputs before the E16 proof or E.16.3 was opened. The original
and final complete statement/proof have now been read and compared. The
final pair preserves the mathematical statement, all labels and targets,
all original displayed mathematics, and every original reference. Its
fifteen literal edits remove publication residue and make the exact
root/period/frame maps explicit. Root review and application remain pending.

## Proof-by-proof comparison

'''
for row in steps:
    md+=f"### Item {row['item']}\n\nPrinted step: {row['printed_step']}\n\nFrozen derivation: {row['frozen_derivation']}\n\nComparison: {row['comparison']}\n\n"
md+='''## Exact coefficient repairs

For the tangent frame D'=aD, each differentiated column in E.16.3 is
multiplied by a, so the coefficient is multiplied by a². The dual
differential frame is multiplied by a⁻¹, and its square by a⁻². Their
product is unchanged. The concrete matrix with U=(e₁,e₂) and derivative
columns(e₃,e₄) has coefficient1; D'=2D gives4. The old literal
inverse-square coefficient rule gives1/4 and is replaced by the full map.

For the primary logarithmic frame, ∇eᵢ=fᵢ dq/(2πiq). The specified
vector q∂q therefore gives (2πi)⁻¹I at the comb cusp. The cohomological
monodromy convention in the opened primary proof is Neᵢ=−fᵢ, so
the connection residue is −N/(2πi). The final text gives the derivative
itself and preserves the nonzero rank conclusion. These are proof-step
coefficient repairs; no theorem statement is refuted or weakened.

## Input and computation boundaries

The original-family calculation uses the supplied E8 result as a cited
input. It gives no second independent credit for E8. Earlier completed
GK and GI comparisons supply their actual bundle and root-coordinate
maps; these exposures are disclosed in the prefreeze input receipt.
The GL statement and three root-isolated construction equations were
available before the GN freeze. The full final GL proof was read only
after the GN target was frozen and released, and is bound separately as
a later cited-input comparison. GN's own independent cusp derivation
already existed before that later reading.

The original E16 owner and current Programs table contain no separate
E16 program association. Root's complete reading of the pinned 104-line
E_checks.py establishes absence of an E16 routine in that file only.
The entire shared file was not opened by this checker. No universal
absence of an E16 program elsewhere is claimed.

The fresh prereading program uses integer/Fraction coefficient
convolution, explicit Leibniz determinants, the named LR lattice map,
and a generic Grassmann quotient projection. It checks weighted matrix
products and finite exponent solutions, with a separate all-m proof.
The postrelease program gives the four-column coefficient through six
two-by-two minors and checks both frame transformations. Both programs
and their complete successful outputs were actually read. The first
program's initial output-serialization failure is preserved; v2 fixes
the reused local name before the successful bound run. The first freeze
attempt failed a literal-owner-name gate; the versioned derivation adds
that name with every mathematical byte preserved before the successful
freeze. Neither failure exposed the target proof.

## Primary edition and source preservation

The supplied comb source matches the existing exact public-v1 source
archive byte for byte. A separately retrieved public v1 PDF is bound;
its complete images11,12,13,14,16,22,23 were actually viewed/read after
the GN freeze. These locate Proposition4.1 pp11–13, Proposition4.3 p14,
equation5.5 p16, and Proposition6.2/equations6.11–6.12 pp22–23. The new
proof locators use that public edition. These primary images add no
Paper II page-reading credit.

The frozen derivation, its original and revised input receipts, v1
proposed proof/guards, and all failed-attempt evidence remain intact.
The final v2 pair has exact sequential forward/inverse maps. All original
displayed expressions and references remain in order. Every original
inline expression also remains in order except the nonmathematical
enumeration iteration marker. Added formulas are the precise maps
described above. The incoming-reference metadata records target labels
and owning statements only; no new full receiving-proof reading is
claimed. Since the complete mathematical statement and all targets
remain unchanged, the receiving interfaces remain identical.

## Event proposal

Propose one targeted proof-check event for E16 and one actual complete
comparative-rereading event for this same printed owner. No separate
independent or computation event is requested for the postrelease
certificate, later GL input, metadata, primary-image reading, or source
application. The proposed JSON does not mutate CHECK_EVENTS. Root must
bind the final applied block and avoid duplicate owner credit.
'''
mp=P/'S6_SERIES_PUBLISH_II_01GN_comparison.md';assert not mp.exists();mp.write_text(md)
final=json.loads(prepared.read_text());final['created_utc']=now
final['supersedes']=[bind(P/'S6_SERIES_PUBLISH_II_01GN_guards_v1.json'),bind(prepared)]
final['comparison']=bind(cp);final['comparison_markdown']=bind(mp)
final['guards'][0]['review_status']='Complete original/final proof actually read and compared; exact forward/inverse verified. Unapplied, awaiting root review.'
final['guards'][0]['comparison_evidence']=bind(cp)
final['guards'][0]['publication_evidence']=[bind(public),bind(P/'S6_SERIES_PUBLISH_II_01GN_prereading_input_receipt_v2.json')]
fg=P/'S6_SERIES_PUBLISH_II_01GN_guards_final.json';save(fg,final)
ep={'created_utc':now,'events':[{'paper':'II','tag':'01GN','statement_id':'cdp:st:E16','date':now[:10],
 'who':'GPT-6 Astra (OpenAI), ChatGPT Pro mode | restore_build | S6_SERIES_PUBLISH continuation',
 'type':'targeted proof check','evidence_group':'S6_SERIES_PUBLISH_II_INFRA_GN',
 'outcome':'Fresh prerelease derivation and complete original/final comparison establish all original/higher, two-parameter, LR and comb rank-divisor conclusions. Two proof coefficient conventions are repaired by exact maps; statement unchanged. Root integration/admission pending.',
 'freeze_receipt':bind(freeze),'release_receipt':bind(release),'comparison_receipt':bind(cp),
 'proposed_full_block':bind(N),'guard_receipt':bind(fg),'proposal_only':True,
 'one_event_for_this_printed_owner':True,'required_final_applied_block_binding':True,'do_not_duplicate_any_accepted_owner_event':True}],
 'actual_full_comparative_rereading_owners':['cdp:st:E16'],'rereading_evidence':bind(cp),
 'events_added':0,'canonical_ledger_modified':False}
ev=P/'S6_SERIES_PUBLISH_II_01GN_event_proposals.json';save(ev,ep)
print(json.dumps({'guard':bind(fg),'comparison':bind(cp),'comparison_md':bind(mp),'events':bind(ev),
 'full_pair_validation':bind(validation),'receiver_metadata':bind(receiver),
 'final_block':bind(N),'literal_edit_count':len(g['literal_edits']),
 'program_table':bind(P/'S6_SERIES_PUBLISH_II_01GN_program_table_proposal_v2.json')},indent=2))
