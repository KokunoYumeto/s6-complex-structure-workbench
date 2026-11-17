"""Record full receiving reads without conflating them with unread prerequisites."""
from pathlib import Path
import csv
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'deliverables/work/maps_audit'
COURSE=ROOT/'sources/codex_workspace/courses/CG-S6/src'
ACTOR=dict(reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode)',effort='Pro',date='2026-11-17')
working=json.loads((OUT/'working_results_inventory.json').read_text())
events=json.loads((OUT/'check_events.json').read_text())
new=[]

def add(key, ids, scope, outcome, locator, remaining=()):
    event=dict(event_id=key,results=['WORK:'+x for x in ids],scope=scope,
        outcome=outcome,locator=locator,remaining_dependencies=list(remaining),**ACTOR)
    if not any(e['event_id']==key for e in events):events.append(event)
    new.append(event)
    return event

def ids(name):
    return [x['source_id'] for x in working if Path(x['source_file']).name==name]

twist_dependencies=[
 dict(source='the-original-six-dimensional-framing-invariant.md',scope='Sections 7–9: embedded representatives, bordism invariance, two-connected preparation, actual index reduction and framed nullbordism.',status='not yet fully read in current audit'),
 dict(source='the-original-integral-stable-group-and-its-completion-maps.md',scope='Sections 5–7 and their Adams/cooperation prerequisites: complete independent course proof of the sixth stable stem.',status='not yet fully read; classical numerical stem is known, but this does not certify the course rederivation'),
 dict(source='higher-index-framed-slides-and-chain-maps.md',scope='Sections 3–6: actual framed slides and both adjacent chain comparisons.',status='not yet fully read'),
 dict(source='whitney-moves-in-the-receiving-dimensions.md',scope='Sections 1–4: complement, complete Whitney disk and framing, supported flow in (6,3,3).',status='not yet fully read'),
 dict(source='realizing-framed-handles-and-middle-cancellation.md',scope='Sections 2–6: actual Morse realization, trajectory correspondence, cancellation and product map.',status='not yet fully read'),
 dict(source='spin-six-and-the-framing-comparison.md',scope='Sections 5–6: pi5 SO7, the given stable framing and rank-six comparison.',status='not yet fully read'),
 dict(source='framed-manifolds-and-the-pontryagin-thom-map.md',scope='Exact normal/tangent framing and Pontryagin–Thom comparison used by the geometric framing construction.',status='not yet fully read'),
]
twist=add('new-course-sphere-twist-receiving-full-20261117',
 ids('sphere-twists-and-the-original-smooth-six-sphere-comparison.md'),
 'Read and rederived the entire 836-line receiving chapter: the exact radius-dependent smooth tube map and inverse; signed relative degree; full integral symplectic operations and Lagrangian algorithm; actual middle-level identifications; interior regluing with its unremoved frame defect; signed new incidence and prescribed handle comparisons; final degree-one and tangent-bundle comparison; complete general stable-framing homotopy; both worked examples. The final source/provenance section was also read. All 433 mathematical checks and all nine source-text checks passed on an independent rerun of the unchanged mathematics.',
 'The receiving calculations are internally consistent. This event does not certify the entire course proof of Theta6=0: the separately listed geometric and stable-homotopy provider proofs still require full independent audit. No old filling is identified with the new filling, and no preservation of the old stable framing is assumed.',
 'sources/codex_workspace/courses/CG-S6/src/sphere-twists-and-the-original-smooth-six-sphere-comparison.md:1–836; deliverables/code/maps_audit/course/SPHERE_TWIST_CHECKS.with_source.json',
 twist_dependencies)
smooth=add('new-course-smooth-receiving-full-20261117',['CG-S6-07-SMOOTH'],
 'Read and rederived the full receiving smooth-recognition section, lines 954–1088, and the four subsequent solved exercises through line 1185. Checked the two punctures, relative H6 diagonal, boundary H5 generators, fundamental group, actual h-cobordism maps, and the exact references to the sphere-twist construction. The two copies of the lesson in sources/course and sources/codex_workspace have identical SHA256.',
 'The local h-cobordism and comparison arguments are checked; the distinct long sphere-twist proof is retained. The geometric provider dependencies listed for that proof remain open in this audit, so this is not blanket certification of its smooth-recognition derivation.',
 'sources/codex_workspace/courses/CG-S6/src/integral-homology-and-sphere-recognition.md:954–1185',twist_dependencies)
almost=add('new-course-almost-complex-full-20261117',ids('almost-complex-structures-and-integrability.md'),
 'Read and rederived all 1250 lines: tensor conventions and bar-partial-square identity; the exact octonion algebra comparison; cross-product, Nijenhuis and associator formulas with norms, ranks, inverses and orientations; diffeomorphism transport and the non-Kahler obstruction; complete nonlinear coordinate transformation; periodic Sobolev gauge construction and its negative Laplacian linearization; elliptic smoothing and the full factorial analytic induction; commuting holomorphic flows and the smooth Newlander–Nirenberg conclusion; polynomial clutching linearization, Riesz splitting, integral K-basis on products of two-spheres, factorial Chern obstruction and conjugate parity; all six complete exercises. Also read and rederived all three receiving characteristic-class providers (350+114+103 lines), including every proof and exact integral comparison. All 80 finite exact algebra checks passed independently.',
 'Full internal proofs checked, including the supplied analytic estimates and the independent polynomial generation proof. Classical almost-complex-sphere and smooth integrability claims must be credited as classical. Original Baez, Hill–Taylor, Newlander–Nirenberg and characteristic-class source comparisons are recorded separately and remain pending where not yet opened; finite checks do not prove convergence. The source discussion of another author’s formula is not to be promoted into a standalone new theorem.',
 'sources/codex_workspace/courses/CG-S6/src/almost-complex-structures-and-integrability.md:1–1250; thom-euler-for-lesson11.md:1–350; projective-splitting-for-lesson11.md:1–114; integral-chern-classes-for-lesson11.md:1–103; deliverables/code/maps_audit/course/ALMOST_COMPLEX_CHECKS.with_source.json',
 [dict(kind='source_credit',scope='Original Baez §2.2, Hill–Taylor §§2–4 and Newlander–Nirenberg source comparisons pending. These are distinct from the complete printed independent argument.'),dict(kind='source_credit',scope='Milnor–Stasheff characteristic-class source comparisons pending; complete receiving proofs read.')])

for row in working:
    # These full-read events predate the explicit boolean field. Normalize the
    # field from the existing named evidence, without inventing a new reading.
    previous_full={'new-foundation-full-20261117','new-working-kummer-full-20261117','new-course-homology-homotopy-full-20261117'}
    if previous_full.intersection(row.get('check_event_ids',[])):
        row['full_proof_read']=True
        row['full_proof_read_evidence']=sorted(previous_full.intersection(row['check_event_ids']))
    chosen=[e for e in new if 'WORK:'+row['source_id'] in e['results']]
    if not chosen:continue
    old=row.get('your_check','')
    extra=' | '.join(e['event_id']+': '+e['scope'] for e in chosen)
    row['your_check']=' | '.join(x for x in [old,extra] if x and extra not in old) if extra not in old else old
    row['full_proof_read']=True
    row['current_reader']=ACTOR
    row['check_event_ids']=list(dict.fromkeys(row.get('check_event_ids',[])+[e['event_id'] for e in chosen]))
    row['check_outcome']=' | '.join(e['outcome'] for e in chosen)
    row['current_unresolved_proof_gaps']=[]
    row['remaining_dependency_checks']=[d for e in chosen for d in e['remaining_dependencies']]
    row['proof_audit_scope']='Complete receiving proof read; separately listed imported prerequisites are not thereby certified.'
    if row['source_id'].startswith('twist-') or row['source_id']=='CG-S6-07-SMOOTH':
        standalone={'twist-actual-tube','twist-signed-action','twist-integral-lagrangians','twist-general-stable-framing','twist-worked-exercises'}
        row['dependency_audit_completion']='complete for displayed standalone algebra/map, source credit pending' if row['source_id'] in standalone else 'receiving proof complete; imported geometric proof reads pending'
        row['raw_producer_header']=(COURSE/'sphere-twists-and-the-original-smooth-six-sphere-comparison.md').read_text().splitlines()[2]
        row['raw_producer_date']='11 October 2026'
    else:
        row['dependency_audit_completion']='complete internal proof and characteristic-class providers; original-source credit checks pending'
    if not row.get('proof_end_line'):
        lines=(ROOT/row['source_file']).read_text().splitlines()
        start=int(row['start_line'])
        next_heading=next((i for i in range(start,len(lines)) if lines[i].startswith('## ')),len(lines))
        row['proof_end_line']=next_heading
        row['end_line']=next_heading

def write_inventory(path, rows):
    path.with_suffix('.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
    keys=list(dict.fromkeys(k for row in rows for k in row))
    with path.with_suffix('.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=keys);writer.writeheader()
        for row in rows:writer.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in row.items()})

write_inventory(OUT/'working_results_inventory',working)
(OUT/'check_events.json').write_text(json.dumps(events,ensure_ascii=False,indent=2)+'\n')
(OUT/'course_remaining_full_checks.json').write_text(json.dumps(new,ensure_ascii=False,indent=2)+'\n')
(OUT/'course_geometric_dependencies_pending.json').write_text(json.dumps(dict(checked_receiving_chapters=[twist['locator'],smooth['locator']],pending=twist_dependencies,**ACTOR),ensure_ascii=False,indent=2)+'\n')

additional=[]
thom=COURSE/'thom-euler-for-lesson11.md'
lines=thom.read_text().splitlines()
for i,line in enumerate(lines,1):
    m=re.match(r'\*\*(Lemma|Theorem|Proposition|Corollary) ([0-9.]+)',line)
    if not m:continue
    kind,num=m.groups();num=num.rstrip('.')
    end=next((j for j in range(i,len(lines)) if lines[j].startswith('## ') or re.match(r'\*\*(Lemma|Theorem|Proposition|Corollary) ',lines[j])),len(lines))
    prior='CG-S6-CHAIN-'+kind.upper()+'-'+num
    duplicate=num in {'1.1','2.1','2.2','4.1'}
    additional.append(dict(source_id=prior,source_file=str(thom.relative_to(ROOT)),start_line=i,end_line=end,
        kind=kind,title=line.split('**',2)[1],full_proof_read=True,paper='I' if duplicate else 'III classical appendix',
        taken_over_by=prior if duplicate else '',duplicate_of_existing_inventory=duplicate,
        credit='Classical singular topology, Thom and Euler classes; GPT-6.1 Sol (OpenAI), Ultra, October 2026 source; GPT-6 Astra (OpenAI), Ultra receiving editing, date not explicitly recorded in this provider header.',
        source_sha256=hashlib.sha256(thom.read_bytes()).hexdigest(),**ACTOR))
for filename,prefix in [('projective-splitting-for-lesson11.md','PROJECTIVE'),('integral-chern-classes-for-lesson11.md','CHERN')]:
    p=COURSE/filename;lines=p.read_text().splitlines()
    heads=[(i,line) for i,line in enumerate(lines,1) if re.match(r'## [0-9]+\.',line)]
    for pos,(i,line) in enumerate(heads):
        end=heads[pos+1][0]-1 if pos+1<len(heads) else next((j for j in range(i,len(lines)) if lines[j].startswith('## Human')),len(lines))
        m=re.match(r'## (\d+)\. (.*?)(?: \{#([^}]+)\})?$',line)
        additional.append(dict(source_id='CG-S6-'+prefix+'-'+m.group(1),source_file=str(p.relative_to(ROOT)),start_line=i,end_line=end,
            kind='Labelled complete classical derivation',title=m.group(2),source_label=m.group(3),full_proof_read=True,paper='III classical appendix',
            taken_over_by='',duplicate_of_existing_inventory=False,
            credit='Classical characteristic classes; exact raw CC0 source and receiving headers retained.',raw_producer_header=lines[2],
            source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),**ACTOR))
write_inventory(OUT/'course_characteristic_provider_inventory',additional)
print(json.dumps(dict(working_rows=len(working),full_receiving_proof_reads=sum(bool(r.get('full_proof_read')) for r in working),new_receiving_rows=sum(len(e['results']) for e in new),provider_rows=len(additional),provider_duplicates=sum(r['duplicate_of_existing_inventory'] for r in additional),unread_geometric_dependency_files=len(twist_dependencies)),indent=2))
