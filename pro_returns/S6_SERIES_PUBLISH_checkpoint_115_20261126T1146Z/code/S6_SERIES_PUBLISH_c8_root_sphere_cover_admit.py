"""Record actual whole-unit sphere/cover rereadings and their open references."""
from __future__ import annotations
from datetime import datetime, timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r

now=datetime.now(timezone.utc).isoformat()
evidence="agents/continuation8_iii_root/S6_SERIES_PUBLISH_III_sphere_cover_units_review.md"
fragment=u.WORK / "root/cyclic_homology.tex"
before=fragment.read_text(encoding="utf-8")
old="For every admissible member $X_p$,\nThe universal cover"
new="For every admissible member $X_p$,\nthe universal cover"
assert before.count(old)==1
after=before.replace(old,new,1)
source=u.repairs.SOURCE.read_text(encoding="utf-8")
assert source.count(before)==1
candidate=source.replace(before,after,1)
u.check_permanent_identifiers(source,candidate)
fields,defects=r.table(r.DEFECTS)
ident="III-C8-CYCLIC-FINAL-CAPITAL"
assert not any(x['change_id']==ident for x in defects)
defects.append(dict(change_id=ident,type="D23",statement_id="maps:src:D.1.1",old_location="final complete cyclic-unit readback",old_page="pending page concordance",new_location="Euler characteristic of cyclic covers",new_page="pending final PDF",old_text=old,new_text=new,reason="Lowercase the continued sentence after the shared-parameter rewrite; the exact resulting sentence is read in this operation's output.",review_status="whole source reviewed; final PDF reading open"))

event_path=u.ROOT / "CHECK_EVENTS.tsv"
event_fields,events=r.table(event_path)
who="GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation eight, root"
outcomes={
 "maps:src:A.2.2":"Complete repaired and publication proofs read against the entire admitted J3 comparison. Supported radial collapse, quaternionic homotopy, based/unbased inverse maps, relative smooth approximation into Q and the lifted-circle contraction retain the complete original scope. No new independent derivation.",
 "mapsIII:rem:cusp-replacement":"Whole new numbered remark compared with its former orphan paragraph and the two closed cached Paper I input statements. Global relative independence is attributed to mapsI:src:A.2.1; the local pi6(T) zero image is not used to prove it. No Paper I proof opened.",
 "mapsIII:def:cyclic-cover":"Whole numbered definition and its before/after source context read. It collects the already used admissible tuple, cover notation and dP6 component surface; K7 still proves the finite covering degree.",
 "maps:src:D.1.1":"Whole current proof before and after publication edits and all169 comparison lines read. Peripheral presentation and inverse cyclic maps, admissibility residues, cusp Euler contributions, cover degree, duality, positive-rank obstruction and complete p=-5 example preserved.",
 "maps:src:D.1.2":"Whole repaired and publication proofs and all234 comparison lines read. Connected covering and branch normalization, ray/blowup maps, integral U/P changes and inverses, Laurent reduction and exact normalization resolution preserved. The duplicated group calculation now cites the preceding complete K7 proof.",
 "maps:src:D.1.3":"Whole repaired and publication proofs and all292 comparison lines read. Exact coefficient/cochain inverses, contraction, finite transfer, complete cusp field and equivariant uniform retraction, character specialization, d=1 and rational component generation preserved. Primary readings are inherited at their explicitly recorded scopes.",
 "mapsIII:def:lifted-fibre":"Whole numbered definition read against the matrices in the replaced KD proof. It preserves both explicit matrices needed later, the map diag(d,1,1,1), its inverse on the covering sublattice, and the conjugation identity.",
 "maps:src:D.1.4":"Whole old6716-character proof, all418 comparison lines, all400 admitted receiving lines and the entire current publication proof read. The separately admitted support guard had been omitted by the required-row selector and is now applied. All covering, finite-fibre, signed attachment, splitting, UCT and exact torsion-obstruction maps are retained; parameter glyphs and the real period inverse are explicit. Existing targeted event is not duplicated.",
}
for label,outcome in outcomes.items():
 eid="publish:c8:III:sphere-cover:"+label
 assert not any(x['event_id']==eid for x in events)
 row={k:"" for k in event_fields}
 row.update(statement_id=label,date="2026-11-25",who=who,type="used and rechecked in this run",outcome=outcome,event_id=eid,phase="continuation8 publication unit comparison",source_file=evidence,source_event_type="used and rechecked in this run",evidence_group="publish:c8:III:sphere-cover",date_utc=now,where=evidence)
 events.append(row)

ppath=u.ROOT / "S6_SERIES_PUBLISH_unit_progress.tsv"
pf,progress=r.table(ppath)
def add_unit(label,title):
 assert not any(x['paper']=='III' and x['unit_id']==label for x in progress)
 for criterion in [f'D{i:02d}' for i in range(1,28)]+['structure']:
  row={k:"" for k in pf}
  row.update(paper="III",unit_id=label,unit_title=title,row_kind="structure" if criterion=='structure' else 'defect',defect_type="" if criterion=='structure' else criterion,status="open",date_utc=now,evidence=evidence,detail="Actual subsection boundary; no completion credit from creating or separating it.")
  progress.append(row)
add_unit("maps:src:A.2.2","Relative realization of sphere maps")
add_unit("maps:src:D.1.5","Characteristic classes and smooth classifications of cyclic covers")
closed=0
for row in progress:
 if row['paper']!='III' or row['unit_id'] not in {'maps:src:A.2.2','maps:src:D.1.1'}: continue
 assert row['status']=='open'
 if row['unit_id']=='maps:src:D.1.1': row['unit_title']='Cyclic covers and integral homology'
 done=row['defect_type'] not in {'D04','D06'}
 row.update(status='done' if done else 'open',date_utc=now,evidence=evidence,
  detail="Whole current canonical unit, complete preceding proofs/comparisons and all28 criterion findings read; final build/page gates separate." if done else "Exact closed series inputs selected and their scope checked; current-edition printed cross-paper expansions await final reference regeneration.")
 closed+=int(done)
assert closed==52
fragment.write_text(after,encoding="utf-8",newline="\n")
u.repairs.SOURCE.write_text(candidate,encoding="utf-8",newline="\n")
r.write_table(r.DEFECTS,fields,defects)
r.write_table(event_path,event_fields,events)
r.write_table(ppath,pf,progress)
print("UTC",now)
print(new+" $\\widetilde X_p$ is a compact complex threefold of Euler characteristic $2d$.")
print("WHOLE_UNIT_CRITERIA_CLOSED",closed)
print("NEW_USED_AND_RECHECKED_EVENTS",len(outcomes))
print("FOUR_CROSS_PAPER_CRITERIA_REMAIN_OPEN")
print("SEPARATED_INVARIANT_UNIT_ALL28_OPEN; LATER_K9_PLACEMENT_STILL_OPEN")
print("III_COMPLETE false")
