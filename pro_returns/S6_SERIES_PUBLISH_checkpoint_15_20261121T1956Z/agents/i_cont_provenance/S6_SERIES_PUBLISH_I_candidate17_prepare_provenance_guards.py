#!/usr/bin/env python3
"""Prepare exact, unapplied candidate17 guards after actual full-block reading."""
from pathlib import Path
from datetime import datetime, timezone
import collections, difflib, hashlib, json, re
from S6_SERIES_PUBLISH_I_cont_recount import proof_end
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
SOURCE_SHA='5b74359a048b1eab3e478a65eab35f35b45474c4c65aadaedd639315c19a9379'
PDF_SHA='3c9f15b28d768f305ab09dfb86ef98365aeb4659329b33e6faedb91864094ab0'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
source=ROOT/'S6_SERIES_PUBLISH_I.tex';assert sha(source)==SOURCE_SHA
text=source.read_text()
def exact(phrase):
    leading=' ' if phrase.startswith(' ') else ''
    pattern=re.escape(leading)+r'\s+'.join(map(re.escape,phrase.strip().split()))
    matches=list(re.finditer(pattern,text));assert len(matches)==1,(phrase,len(matches))
    return matches[0].group(0)
# number,page,type,owner,old,new,scope,we rows,here rows
SPECS=[
(1,324,'D08','push:src:E.2.1',r'It remains to identify the extension at $p_0$ in degree two. We give a fibre-sensitive calculation. The kernel of',r'For the degree-two extension at $p_0$, the kernel of','Replace the announcement with its positive degree-two extension scope. The kernel, conormal gluing, Serre-dual dimension, residue-fibre base change, discrete-valuation-ring freeness and all direct images remain.',[],[]),
(2,327,'D08','night:P5.5','Here is the integral lattice calculation, including torsion.','','The integral cocycle solution, determinant-minus-one matrix, explicit integral inverse and integral H^1 vanishing remain. Delete only the standalone announcement.',[],[19]),
(3,118,'D08','fam:src:B.4.2','We construct an involutive splitting of the group extension.','','The real-member hypothesis, derivative, translation action, square b_0, real representative, correction by -b_0/2, involution and exponential action remain.',[54],[]),
(4,120,'D08','mapsI:src:A.3.2','We next give exact equations for all real fibres.','','The real-part parameter, three branch identifications, involution matrices, affine fixed-point equations, coset counts and offsets remain.',[58],[]),
(5,121,'D08','mapsI:src:A.3.2','We compute the cusp fixed set.','','The complete current-proof review supports deleting this announcement; the cusp matrix values, toric involution, unit signs, orbit equations, edge constants and all fixed-set conclusions remain. This reopens the earlier bounded compute-scan retention of this sentence.',[59],[]),
(6,122,'D08','mapsI:src:A.3.3','We check the intervening torus identification.','','The B_1 and C definitions, involution identities, congruence 2k=1 mod 3, transported cap meridians, determinant-one Heegaard map and Hopf Euler class remain.',[61],[]),
(7,147,'D08','push:src:D.4.5','We first fix its additive normalization exactly.','','The defined Green norm, Jacobi product, horizontal average, zero integral, exact distribution identity and normalization conclusion remain.',[74],[]),
(8,159,'D08','push:src:A.2.2','We give the normalization calculation, including the singular centre.','','The nodal centre, both blow-up charts, conifold small-resolution charts, strict transforms and fibres over smooth and nodal points remain. The theorem states the exact normalization order.',[82],[]),
(9,160,'D08','night:P2.10','We now construct the filling with the untwisted finite fibres.','','The theorem states the untwisted family. The zero winding, two ruled bundles, neck equations, gluing, compact cover, proper modification and finite quotient remain.',[83],[]),
(10,161,'D08','night:P2.10','We identify the compactified generic fibre, including its chosen marked cusp.','','The r-nonzero hypothesis, W=rw and u=r^2 substitutions, cone characters, selected diagonal, exact coordinate comparison, transition AB=1 and cited Engel marking remain.',[84],[]),
(11,166,'D08','push:src:A.2.5','We describe explicitly what the recorded move means geometrically.','','The primitive cone, smooth closed stratum, blow-up coordinates, monomial transitions, exceptional projective bundle, multiplicity and inverse contraction remain.',[85],[]),
(12,171,'D08','push:src:A.4.2','We spell out the rank and saturation assertions.','','The projective-bundle class, exceptional divisor, two restriction maps, primitive rank-twelve image, exact cokernel and remaining Thom maps remain.',[92],[]),
(13,176,'D08','push:src:A.4.8','We classify the connected centres in this chain.','','The codimension, stabilizer, toric-normalization and compact/noncompact centre classification remain, followed by the exact blow-up splitting and all Betti/monodromy formulas.',[95],[]),
(14,181,'D08','push:src:B.1.2',r'This verifies the particular comparison with \cref{fam:src:E.2.1} that we use.',r'These quotient identifications give the comparison with \cref{fam:src:E.2.1}.','Keep the numbered comparison as a positive conclusion of the displayed isogenies, lattice maps and quotient identifications. The exact reference remains.',[96],[]),
(15,186,'D08','push:src:B.3.4','We give the intersection computation needed for the height lattice; this also fixes the component indices used below.','','The affine intersections, infinity coordinates, I_12 component indices, height pairing, determinant, index bounds and trace congruences remain.',[99],[]),
(16,188,'D08','push:src:B.3.6','We next remove all its local ramification without changing this transgression.','','The local norm arguments, localization theorem, exact subtraction xi=xi_0-res eta and conclusion d_2 xi=6P remain; the statement specifies the unramified class and its transgression.',[102],[]),
(17,171,'D02','push:src:A.4.2',', so no integral index is omitted','','Delete the defensive tail after the positively cited surjectivity of the three intersection coordinates. The primitive maps, exact integral sequence, ranks and torsion conclusions remain.',[],[]),
(18,171,'D02','push:src:A.4.2',' without an appeal to a monodromy theorem','','Delete the source-exclusion tail after the explicit tube argument proving (T_u-I)^2=0. The monodromy map and its geometric proof remain.',[],[]),
(19,192,'D08','push:src:B.4.2','For completeness, in a product chart','In a product chart','Remove only the completeness qualifier. The monomial chart, arithmetic--geometric mean bound, common exponent, trajectory length and continuous retraction proof remain.',[104],[6]),
(20,153,'D08','push:src:A.1.2',r'Here is a construction on the whole compact surface $S$. Choose a',r'On the whole compact surface $S$, choose a','Retain the whole compact-surface scope in the actual metric choice. All core/node domains, collar maps, Hausdorff/properness proof, flatness and marked cusp comparison remain.',[],[4]),
(21,207,'D08','push:src:B.4.10','For completeness, the generic Hopf blowdown also has an explicit developing map.','The generic Hopf blowdown also has an explicit\ndeveloping map.','Remove only the completeness qualifier. The developing-map assertion, punctured-parameter hypothesis, entire product, equivariance, charts and exceptional orbit remain.',[],[9]),
(22,221,'D08','push:src:B.4.16',r'For completeness, a compact normal-crossings space $D$ has a natural injection','A compact normal-crossings space $D$\nhas a natural injection','Remove only the completeness qualifier. The hypothesis, exact injection, ordered branch resolution, alternating summand, spectral sequence and surviving integral class argument remain.',[],[11]),
(23,222,'D08','push:src:B.4.17','For completeness the fibre inclusions on fundamental groups are the two quotient maps','The fibre inclusions on fundamental groups\nare the two quotient maps','Remove only the completeness qualifier. Both lattice quotients, van Kampen pushout, signed Mayer--Vietoris matrix, homology tuple and final cohomology calculation remain.',[],[12]),
]
def math_segments(s):
    return re.findall(r'(?s)(?<!\\)\$(?:\\.|[^$\\])*(?<!\\)\$|\\\[(?:.*?)\\\]|\\\((?:.*?)\\\)',s)
def commands(s):return re.findall(r'\\[A-Za-z@]+\*?|\\.',s)
guards=[]
for n,page,kind,sid,phrase,new,reason,we,here in SPECS:
    old=exact(phrase)
    assert math_segments(old)==math_segments(new),(n,'math')
    assert commands(old)==commands(new),(n,'commands')
    guards.append({'id':f'I17-prov-{n:02d}','page':page,'type':kind,'statement_id':sid,
      'line':text.count('\n',0,text.index(old))+1,'before':old,'after':new,'reason':reason,
      'source_sha256':SOURCE_SHA,'pdf_sha256':PDF_SHA,'first_person_row_indices':we,
      'here_row_indices':here,'status':'proposed, not applied','mathematical_events_added':0,
      'full_page_reading_credit_added':0})
archive=OUT/'candidate17_guard_review_blocks';archive.mkdir(exist_ok=True)
groups=collections.defaultdict(list)
for g in guards:groups[g['statement_id']].append(g)
proposed=text;blocks=[]
for i,(sid,members) in enumerate(groups.items(),1):
    pos=text.index('\\label{'+sid+'}',text.index(r'\begin{document}'))
    st=list(re.finditer(r'\\begin\{(proposition|theorem|lemma|remark|definition|cited|maintheorem)\}',text[:pos]))[-1]
    se=text.index('\\end{'+st[1]+'}',pos)+len('\\end{'+st[1]+'}')
    pe=proof_end(text,text.index(r'\begin{proof}',se))
    before=text[st.start():pe];after=before;statement=before[:se-st.start()]
    for g in members:
        assert after.count(g['before'])==1 and g['before'] not in statement
        after=after.replace(g['before'],g['after'],1)
        proposed=proposed.replace(g['before'],g['after'],1)
    assert math_segments(before)==math_segments(after)
    assert commands(before)==commands(after)
    p=archive/f'block_{i:02d}_before.tex';q=archive/f'block_{i:02d}_proposed.tex'
    p.write_text(before+'\n');q.write_text(after+'\n')
    (archive/f'block_{i:02d}.diff').write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='before',tofile='proposed')))
    info={'scope_id':sid,'guards':[g['id'] for g in members],
      'original_full_block':str(p.relative_to(ROOT)),'original_full_block_sha256':sha(p),
      'proposed_full_block':str(q.relative_to(ROOT)),'proposed_full_block_sha256':sha(q),
      'complete_statement_and_proof_actually_read':True,'statement_byte_identical':True,
      'all_mathematical_segments_and_commands_identical':True,'mathematical_assertions_unchanged':True}
    blocks.append(info)
    for g in members:g.update({k:v for k,v in info.items() if k not in ['scope_id','guards']})
# Every exact replacement and every complete affected block has been compared
# above. A whole-document regex can span mixed TeX math delimiters, so it is
# deliberately not used as a substitute for those bounded comparisons.
assert commands(text)==commands(proposed)
dest=OUT/'S6_SERIES_PUBLISH_I_candidate17_provenance_guards.json'
assert not dest.exists(),'Freeze guard batch; do not overwrite'
dest.write_text(json.dumps(guards,ensure_ascii=False,indent=2)+'\n')
reading=OUT/'S6_SERIES_PUBLISH_I_final_candidate17_reading_provenance.json'
assert sha(reading)=='65e544a998acb4810742e3b0c9d4a706d3c76f1166a06069bb33986ba3e4450e'
receipt={'paper':'I','candidate':17,'created_utc':datetime.now(timezone.utc).isoformat(),
 'source_sha256':SOURCE_SHA,'pdf_sha256':PDF_SHA,'guard_file':str(dest.relative_to(ROOT)),
 'guard_sha256':sha(dest),'proposals':len(guards),'counts_by_type':dict(collections.Counter(g['type'] for g in guards)),
 'complete_source_blocks_actually_read':len(blocks),'blocks':blocks,
 'all_statement_bytes_unchanged':True,'all_mathematical_segments_and_commands_identical':True,
 'citation_and_reference_order_identical':True,'mathematical_assertions_unchanged':True,
 'math_preservation_scope':'Every exact replacement and complete affected statement/proof; the whole-source change is precisely those substitutions. Whole-source command order is also identical.',
 'whole_proposed_source_sha256':hashlib.sha256(proposed.encode()).hexdigest(),
 'immutable_reading_record':str(reading.relative_to(ROOT)),'immutable_reading_sha256':sha(reading),
 'first_person_input':{'path':'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate17_all_first_person_contexts.json',
   'sha256':sha(ROOT/'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate17_all_first_person_contexts.json'),
   'assigned_rows_actually_read':list(range(53,105))},
 'here_input':{'path':'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate17_here_contexts.json',
   'sha256':sha(ROOT/'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate17_here_contexts.json'),
   'assigned_rows_actually_read':[4,6,9,11,12,19]},
 'historical_reopening':'The prior bounded compute-scan retention of We compute the cusp fixed set is reopened by full current-proof review (I17-prov-05). Root separately owns context155, We compute all components of the translation group; the immutable page326 observation is left historical.',
 'root_overlap':'Root owns distinct B.2 connecting-map and C.4 translation-group announcements. Merge those substitutions when applying the shared complete blocks.',
 'source_changes_applied':False,'shared_files_modified':False,'mathematical_events_added':0,
 'full_page_reading_credit_added':0,
 'scope':'All 52 assigned first-person contexts, all six assigned Here/For completeness contexts, and all 19 affected full source statements/proofs were actually read before these exact proposals. No source-review image or mathematical event credit is added.'}
rp=OUT/'S6_SERIES_PUBLISH_I_candidate17_provenance_guard_receipt.json'
rp.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
md=['# Candidate17: provenance-agent exact guards','',f'Source: {SOURCE_SHA}. PDF: {PDF_SHA}.','',
 '23 unapplied proposals: 21 D08 and 2 D02. All 19 affected complete statements/proofs were read. Every statement byte, mathematical segment, command, citation and reference order is preserved. No mathematical event is added.','']
for g in guards:
    md.extend([f"## {g['id']} — {g['type']}, page {g['page']}, {g['statement_id']}",'',g['reason'],'','Before:',''])
    md.extend('    '+l for l in g['before'].splitlines())
    md.extend(['','After:',''])
    md.extend('    '+l for l in g['after'].splitlines())
    md.append('')
dest.with_suffix('.md').write_text('\n'.join(md)+'\n')
assert sha(source)==SOURCE_SHA
print(json.dumps({'guard_file':str(dest.relative_to(ROOT)),'guard_sha256':sha(dest),
 'receipt':str(rp.relative_to(ROOT)),'receipt_sha256':sha(rp),'proposals':len(guards),
 'full_source_blocks_read':len(blocks),'counts_by_type':receipt['counts_by_type']},indent=2))

