"""Record the root's completed independent reviews without erasing earlier states."""
from pathlib import Path
import hashlib, json, re

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'deliverables/work/maps_audit'
META = dict(reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode)', effort='Pro', date='2026-11-17')
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def read(name): return json.loads((OUT/name).read_text())
def save(name, value): (OUT/name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')

carrier = OUT/'carrier_nullhomotopy_by_extension.tex'
pt = OUT/'pt_relative_bordism_repair.tex'
reviews = [
 dict(event_id='root-independent-carrier-extension-20261117',
      source=str(carrier.relative_to(ROOT)), source_sha256=digest(carrier),
      checking_agent='/root', review_kind='Independent mathematical reading and rederivation by a separate AI agent; not a human review',
      outcome='Passed after making the ambient neighbourhood hypothesis explicit.',
      precise_scope='The based nullhomotopy of both original one-copy angle-forgotten carriers, their smash powers, and the actual local inclusion and affine no-drift source chain. No statement about the retained-angle map or pointwise extension of the flat character.',
      required_correction='N is a closed neighbourhood with int_X(N)=N minus its manifold boundary, so its frontier is exactly that boundary. The actual N0 has this property by the submersion collar.',
      root_source_readings=['cusp_cone_sphere_routes.tex:65–97', 'candidate_geometry.tex:1067–1226', 'integral_leray.tex:878–913 and the earlier Paper I geometric fundamental-group proof', 'cusp_sphere_route_strengthening.tex:267–293,406–417,662–675', 'AC26 original p.30, visually checked by root'],
      provenance='Root collaboration messages received in this turn: independently read/rederived full proof; then independently read full native-alpha/deck/residual/disc/formula chain and confirmed passage after the explicit frontier hypothesis.',
      distinct_proofs_retained='The original framed-torus nullbordism and the original open analysis remain unchanged.', **META),
 dict(event_id='root-independent-pt-relative-bridge-20261117',
      source=str(pt.relative_to(ROOT)), source_sha256=digest(pt),
      checking_agent='/root', review_kind='Independent mathematical reading and rederivation by a separate AI agent; not a human review',
      outcome='Passed, with the opening zero-coordinate wording made precise.',
      precise_scope='Explicit relative embedding, Gram-matrix normal framing and exact boundary match, normal inverse homotopy, all zero-stabilization/block-order comparisons, embedding-family normal frame and abstract tangent-framed Pontryagin–Thom comparison in dimension six.',
      checked_formulas=['RB.1', 'RB.2', 'RB.3', 'RB.4', 'RB.5', 'RB.6', 'normal frame of the embedding-family cylinder'],
      required_correction='Every stabilization of an existing embedding uses identically zero appended coordinates. The g and ge coordinates in the relative extension vanish on its boundary collars, and need not vanish in the interior.',
      subsequent_editorial_change='The already reviewed choice-independence and group-isomorphism argument has been wrapped as an explicitly labelled proposition, without changing its mathematics.',
      provenance='Root collaboration messages received in this turn expressly report a full independent reading/rederivation and passage of every formula and boundary comparison.',
      excluded_scope='This bridge does not compute a stable group and does not promote any Adams/cooperation dependency status.', **META)
]
history=read('check_events.json'); seen={x.get('event_id') for x in history}
history.extend(x for x in reviews if x['event_id'] not in seen);save('check_events.json',history)
save('independent_repair_reviews.json',reviews)

chain=read('carrier_nullhomotopy_source_chain.json')
chain.setdefault('historical_parent_check_status',chain['parent_independent_check'])
chain['parent_independent_check']=reviews[0]
chain['proof_sha256']=digest(carrier)
chain['ambient_hypothesis']='Compact Hausdorff X; compact smooth N is a closed neighbourhood with int_X(N)=N minus boundary(N). The actual cusp N0 is codimension zero with exactly this frontier, by the submersion collar.'
save('carrier_nullhomotopy_source_chain.json',chain)

old=read('pt_relative_bordism_repair_record.json')
old.setdefault('historical_writer_status',old['status'])
old.setdefault('historical_writer_sha256',old['sha256'])
old['status']='Full additional bridge passed root independent mathematical review, after the stated editorial correction.'
old['sha256']=digest(pt);old['independent_check']=reviews[1]
save('pt_relative_bordism_repair_record.json',old)

rows=read('working_carrier_additional_results.json')
for row in rows:
 if row['proof_file']==carrier.name:
  row.setdefault('historical_proof_sha256',row['proof_sha256'])
  row['proof_sha256']=digest(carrier);row['independent_check_event']=reviews[0]['event_id']
  row['current_status']='Passed root independent review at the explicitly angle-forgotten scope; ambient-neighbourhood correction applied.'
save('working_carrier_additional_results.json',rows)

lines=pt.read_text().splitlines(); starts=[]
for i,line in enumerate(lines,1):
 m=re.match(r'\\begin\{(lemma|proposition)\}\[(.*)\]',line)
 if m: starts.append((i,m.group(1),m.group(2)))
ptrows=[]
for j,(start,kind,title) in enumerate(starts):
 end=starts[j+1][0]-1 if j+1<len(starts) else len(lines)
 block='\n'.join(lines[start-1:end])+'\n'
 label=re.search(r'\\label\{([^}]+)\}',block).group(1)
 ptrows.append(dict(source_run='CURRENT_AUDIT_REPAIR',source_id='MAPS-AUDIT-PT-'+str(j+1),
  source_file=str(pt.relative_to(ROOT)),source_sha256=digest(pt),kind=kind,title=title,
  paper='III',printed_label=label,start_line=start,end_line=end,proof_range=[start,end],
  complete_source_text=block,complete_source_text_sha256=hashlib.sha256(block.encode()).hexdigest(),
  producer=META['reader'],producer_effort=META['effort'],producer_date=META['date'],
  current_check_event=reviews[1]['event_id'],full_proof_read=True,
  relationship='Additional complete proof of the precise relative-embedding/tangent-to-normal bridge invoked, but not printed, in the original sphere-twist source. No original result or proof removed.',
  taken_over_by='',duplicate_of_existing_inventory=False,
  scope='Classical Pontryagin–Thom prerequisite; no novelty or stable-group computation claimed.', **META))
save('pt_relative_bordism_repair_inventory.json',ptrows)
save('reviewed_repair_label_recommendations.json',dict(
 rows=[dict(source_id=r['source_id'],printed_label=r['printed_label'],proof_file=r['proof_file'],relationship=r['relationship']) for r in rows if r['proof_file']==carrier.name]+[
 dict(source_id=r['source_id'],printed_label=r['printed_label'],proof_file=pt.name,relationship=r['relationship']) for r in ptrows],
 old_open_analysis='Retain cusp_sphere_route_strengthening.tex:662–675 as the dated source state, and add a forward reference to mapsIII:angle-forgotten-one-copy-null for the newly settled angle-forgotten S2 assertion.',
 distinct_rank_two_proof='Retain the full cusp_s12_carrier_homotopy.tex framed-torus proof alongside the extension homotopy.',
 relative_bridge_insertion='Insert these four complete proof units immediately after embedded normal-framed Pontryagin–Thom and before its application to abstract tangent-framed bordism in the sphere-twist proof.', **META))
print(json.dumps(dict(reviewed_repairs=2,carrier_rows=2,pt_rows=len(ptrows))))
