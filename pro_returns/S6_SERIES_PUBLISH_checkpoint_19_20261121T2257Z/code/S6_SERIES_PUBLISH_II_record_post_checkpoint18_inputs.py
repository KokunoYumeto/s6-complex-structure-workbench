"""Preserve the root's bounded readings; this creates no check event."""
from pathlib import Path
import csv, datetime as dt, hashlib, json

R = Path(__file__).resolve().parents[1]
def sha(b):
    return hashlib.sha256(b).hexdigest()
def save(name, data):
    p=R/'records'/name
    assert not p.exists(), str(p)
    p.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({'path':str(p.relative_to(R)),'sha256':sha(p.read_bytes())}))

source=(R/'S6_SERIES_PUBLISH_II.tex').read_bytes()
assert sha(source)=='deed2de0d348b9644cf56307296423d59a62a5947ac7ac0ba9ba41a9ec3e42fc'
text=source.decode(); lines=text.splitlines()
ledger=(R/'CHECK_EVENTS.tsv').read_bytes()
assert sha(ledger)=='b52451e191160bd666dfff6d6ba60162aa223f0d67b8f6d767c2322f625d1d0c'
csv.field_size_limit(100_000_000)
with (R/'CHECK_EVENTS.tsv').open() as f:
    rows=list(csv.DictReader(f,delimiter='\t'))
stamp=dt.datetime.now(dt.timezone.utc).isoformat()
base={'recorded_utc':stamp,'canonical_source_sha256':sha(source),'ledger_sha256':sha(ledger),
      'new_check_credit':False,'root_primary_page_image_credit':0}
def frag(a,b):
    s='\n'.join(lines[a-1:b])+'\n'
    return {'lines':[a,b],'text':s,'sha256':sha(s.encode())}
def pair(label):
    p=text.index('\\label{'+label+'}')
    a=text.rfind('\\begin{',0,p)
    b=text.index('\\end{proof}',p)+len('\\end{proof}')
    s=text[a:b]
    return {'label':label,'text':s,'sha256':sha(s.encode())}

wm=[r for r in rows if r['statement_id']=='night:P4.15']
assert len(wm)==3
table=frag(77902,77928)
save('S6_SERIES_PUBLISH_II_WM_root_program_association_scope.json',{
    **base,'owner':'night:P4.15','tag':'02WM','historical_associations':wm,
    'original_complete_pair':pair('night:P4.15'),
    'bounded_adjacent_tail':frag(15688,15698),
    'programs_table':table,
    'actual_reading':'Root read the complete three exact-owner historical rows, the complete five-item original statement/proof pair, the immediately preceding P4.14 tail, the following P4.16 statement/opening, and all ten current end Programs table rows. The following proof opening has no fresh-check credit.',
    'association_conclusion':'The inspected WM records and target proof name no prior computational routine. The table positively assigns genus_one_conductor.py to P4.14, milnor_intersection.py to P4.16/P4.17 and binomial_milnor.py to P4.18/P4.19. No WM ownership is inferred from adjacency. This bounded inspection does not assert that no other historical routine exists.'})

owners={
 '03IC':'wbII:lem:picard-crossed-defect', '03IE':'wbII:lem:picard-finite-norm',
 '03ID':'wbII:lem:picard-cusp-defect', '03IL':'wbII:prop:direct-boundary-picard',
 '03IN':'wbII:prop:local-cusp-picard-obstruction', '03IH':'wbII:prop:analytic-ah-boundary',
 '03I6':'wbII:lem:analytic-support-specialization', '03IW':'wbII:thm:analytic-all-picard',
 '03IM':'wbII:prop:leray-edge-restriction', '03DR':'wbII:cor:candidate-conductor-actual'}
selected={tag:[r for r in rows if r['statement_id']==label] for tag,label in owners.items()}
assert sum(map(len,selected.values()))==40
save('S6_SERIES_PUBLISH_II_group10_root_historical_program_associations.json',{
    **base,'owners':owners,'associations':selected,
    'actual_reading':'Root read all forty exact-owner historical associations in full before checkpoint18; the exact rows are preserved here. No independent check is awarded for historical import or this inspection.',
    'positive_program_claims':[{'event_id':'ce:1990761c9345c839c9d8','tag':'03IN'},
                               {'event_id':'ce:b92aca063fdfb8162976','tag':'03I6'}],
    'unresolved_named_record':'work/cdp_audit/II_working_credit/working_credit_comparison_30.json',
    'scope':'The two indicated outcomes say program rerun without identifying a source filename. Filename searches and bounded Python-content searches in the attached S6_PUBLISH_programs tree have not yet bound an actual routine to those two claims. The ten current Paper II Programs table rows contain no group10 owner. Related Paper I cusp arithmetic programs have been found by filename but are not assigned to these Paper II owners without a proved content relationship.',
    'programs_table':table})

save('S6_SERIES_PUBLISH_II_F5_root_safe_inputs_and_front_scope.json',{
    **base,'target_owner':'cdp:st:C.3.10','target_tag':'01F5',
    'target_proof_included':False,
    'complete_cited_input':pair('cdp:st:D.1.9'),
    'receivers':[
        {'kind':'backpointer','fragment':frag(5090,5090),'conclusion':'Identifier points to Theorem B outline step3; no theorem domain is asserted in this macro.'},
        {'kind':'tag index','fragment':frag(5592,5592),'conclusion':'Identifier-only statement/tag index row.'},
        {'kind':'main theorem','fragment':frag(5250,5285),'conclusion':'The full main Theorem B expressly begins with a connected smooth compact complex threefold.'},
        {'kind':'outline step3','fragment':frag(5794,5804),'conclusion':'The exclusions are the outline of the exact main Theorem B and inherit its explicitly smooth total-space domain.'}],
    'actual_reading':'Root read the entire D1.9 proposition and all three proof items, the entire main Theorem B, the complete outline step3 and both identifier-only receivers. No F5 target-proof prose is present in this packet.',
    'construction_binding':'D1.9 chooses gamma in H0(P1,R1 f_* Z) with d2(gamma)=d>0, then defines beta as the coherent Leray inverse of the coefficient image of that exact gamma. Naturality gives beta|Y_c=iota_c(gamma_c) on every full fibre. This supplies the cited construction to compare with a separately derived class; equality with any such class is not asserted by this record.',
    'scope_conclusion':'The three frontmatter occurrences inspected do not require a mathematical change when F5 states the smoothness used in its derivation. The agent separately owns the complete body receiver audit.'})
