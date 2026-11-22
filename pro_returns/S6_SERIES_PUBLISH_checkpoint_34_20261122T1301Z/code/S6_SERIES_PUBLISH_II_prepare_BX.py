from pathlib import Path
import datetime as dt,hashlib,json,re

R=Path(__file__).resolve().parents[1]
def bind(p):return dict(path=p,sha256=hashlib.sha256((R/p).read_bytes()).hexdigest())
original='agents/ii_infra/released_proofs/01BX/b168cbeb6186b92e/S6_SERIES_PUBLISH_full_owning_block.tex'
old=(R/original).read_text();new=old;guards=[]
def change(a,b,t,reason,count=1):
 global new
 assert new.count(a)==count,(a,new.count(a),count)
 guards.append(dict(old=a,new=b,type=t,reason=reason,occurrences=count))
 new=new.replace(a,b,count)

change('A rational ordinary-triple image has no positive-genus double branch cover','Double covers over a rational ordinary-triple image','D16','Use a short mathematical title for the same statement.')
record=next(x for x in new.splitlines(True) if x.startswith('\\StatementRecord'))
change(record,'','D10','Remove the machine record; its mathematical dependencies remain in the check inventory and every tag/label remains. The common final statement-header pass supplies uniform printed tags.')
change(r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]',r'\begin{enumerate}[label=\arabic*.,leftmargin=*]','D10','Remove production markers from the thirteen proof item numbers.')
change('Use the actual normal tensor and\nnormal-cone comparison (C.D4.1)--(C.D4.2)',r'Use the normal tensor and'+'\n'+r'normal-cone comparison \eqref{cdp:eq:C.D4.1}--\eqref{cdp:eq:C.D4.2}','D04','Resolve both normal-jet and compact-core comparison equations; mathematical construction unchanged.')
change('into an actual nearby\ntorus.','into a nearby\ntorus.','D08','State the target of the established embedding directly.')
change(r'\SeriesRef{cdp:st:A.5.19}',r'\ref{cdp:st:A.5.19}','D04','Resolve the three uses of the irrational-ruled input by its local statement number.',3)
change('as in (C.RD.2).',r'as in \eqref{cdp:eq:C.RD.2}.','D04','Resolve the integral-closure identification of the complete quadratic root cover.')
change('We record the comparison with relations and disconnected\nboundary retained.','The calculation includes relations among the boundary classes\nand disconnected boundary.','D08','State the precise scope of the same homology calculation directly.')
change('Hodge decomposition on the actual surface $X$.','Hodge decomposition on the projective surface $X$.','D08','Name the geometric hypothesis already stated in the preceding sentence.')
change('(C.D4.9)--(C.D4.10)',r'\eqref{cdp:eq:C.D4.9}--\eqref{cdp:eq:C.D4.10}','D04','Resolve the homology-pair equations, including the relation count.')
change('uses the actual unramified degree-three cover','uses the unramified degree-three cover','D08','Keep the precise cover and degree without a process qualifier.')
change('The local calculation (C.D4.7), or \\CompendiumRef{II}{cdp:st:C.2.RAT.6},','Cited result~\\ref{cdp:st:C.2.RAT.6} and the link comparison\nin \\eqref{cdp:eq:C.D4.7}','D06','Use the restored delta-five result and the exact link-to-exceptional-divisor map; both unchanged bounds apply to these same germs.')
change('Statement \\CompendiumRef{II}{cdp:st:C.2.RAT.6} supplies','Cited result~\\ref{cdp:st:C.2.RAT.6} supplies','D06','Resolve the missing compendium dependency through its restored inherited01CI anchor.')
change('defines an actual map','defines a bundle map','D08','State the already displayed homomorphism between the two specified line bundles directly.')
change('(C.RD.10). Consequently $b_1(X)=0$.','Cited result~\\ref{cdp:st:C.2.RAT.6} and the link comparison\nin \\eqref{cdp:eq:C.D4.7}. Consequently $b_1(X)=0$.','D06','Resolve the A1/A3 rows through the same explicit local table and exceptional homology comparison.')
change('as a sheaf\nidentity, not only over the nonsingular locus.','as an identity of sheaves over all of $E$.','D02','State the proved global sheaf identity positively, preserving the reflexive-extension argument.')
change('We next prove that all singularities of this\nnormalized cover are rational.','The following resolution proves that its singularities are rational.','D08','Connect the conclusion with the explicit resolution already retained below.')
change('\\item For precision, the normalized covers over the','\\item The normalized covers over the','D08','Remove an assurance phrase while retaining the exact proper birational maps.')
change('This is the final contradiction. Every common\ndivisor allowed by \\eqref{cdp:eq:C.DD.4}--\\eqref{cdp:eq:C.DD.5} has now\nbeen treated, proving that $C$ cannot have\npositive genus.','This contradicts the compact-core embedding. Together with\nthe other common divisors allowed by\n\\eqref{cdp:eq:C.DD.4}--\\eqref{cdp:eq:C.DD.5}, it proves $g(C)=0$.','D08','Keep the case exhaustion and conclusion, removing chronological recap.')

assert old.count('\\item')==new.count('\\item')==13
displays=lambda t:re.findall(r'\\\[(.*?)\\\]',t,re.S)
assert displays(old)==displays(new) and len(displays(new))==21
for pattern in [r'\\hypertarget\{([^}]+)\}',r'\\label\{([^}]+)\}']:
 assert re.findall(pattern,old)==re.findall(pattern,new)
proposed='agents/continuation2_root/01BX/S6_SERIES_PUBLISH_II_root_BX_proposed.tex'
assert not (R/proposed).exists();(R/proposed).write_text(new)
now=dt.datetime.now(dt.timezone.utc).isoformat()
freeze='agents/ii_infra/derivation_freezes/01BX/20261122T061218665587Z/S6_SERIES_PUBLISH_derivation_freeze_receipt.json'
release='agents/ii_infra/released_proofs/01BX/b168cbeb6186b92e/S6_SERIES_PUBLISH_release_receipt.json'
frozen=json.loads((R/freeze).read_text())
eventpath='agents/continuation2_root/01BX/S6_SERIES_PUBLISH_II_root_BX_events.json'
events=dict(created_utc=now,events=[
 dict(statement_id='cdp:st:C.2.D4.2',type='targeted proof check',date='2026-11-22',date_utc=frozen['created_utc'],event_id='ce:S6_SERIES_PUBLISH_II_root_BX_target_20261122',evidence_group='S6_SERIES_PUBLISH_II_root_BX_20261122',outcome='Complete seven-section statement-led derivation frozen before release of the target proof. The line-subbundle degree gives all scalar-zero possibilities and the explicit coordinate changes to both splitting charts. The reduced and doubled branch algebras, character sheaf cohomology, local quotient and blowup maps, compact pairing ranks, first Betti bounds and torus obstruction are derived. The full new prerelease program/output was read. Known supporting BW proof and source inputs are disclosed; no fully blind invention claim. The prefreeze connectedness draft correction is recorded and was settled before freeze.'),
 dict(statement_id='cdp:st:C.2.D4.2',type='used and rechecked in this run',date='2026-11-22',date_utc=now,event_id='ce:S6_SERIES_PUBLISH_II_root_BX_reread_20261122',evidence_group='S6_SERIES_PUBLISH_II_root_BX_20261122',outcome='Full original proof and all thirteen proposed items/twenty-one displays compared. Original stronger relation-count and intersection formulas are verified by a fresh closed-cover Euler-strata computation. The original arbitrary-contact normalized blowup resolution is retained, with its exact character transforms, faithful finite pushforward and R1 vanishing. The needed local bound is the restored cited result01CI, with the same link-to-exceptional homology comparison. All original hypotheses, conclusions, mathematical steps and existing labels/tags remain. No mathematical error or extra independent computation group is claimed.')])
assert not (R/eventpath).exists();(R/eventpath).write_text(json.dumps(events,indent=2)+'\n')
programrows=''
for title,filename in [('Double-cover root intersections, normalized character algebras and local exceptional matrices','S6_SERIES_PUBLISH_II_root_BX_prerelease.py'),('Double-cover intersection ranks from Euler strata of the closed cyclic cover','S6_SERIES_PUBLISH_II_root_BX_postrelease.py')]:
 programrows+=title+r' (\cref{cdp:st:C.2.D4.2}) & \href{https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/\SsixRepositoryCommit/code/'+filename+r'}{\nolinkurl{'+filename+r'}} \\[3pt]'+'\n'
orphan='The splitting bounds, all intersection-rank lower\nbounds, the exact scalar-zero coordinate example,\nand the normalized cyclic-cover blowup substitutions\nare retained in \\path{code/E_cubic_double.py} and\nits saved output. The local delta-five table is\nindependently computed in \\path{code/A_cubic_delta5.py}.\n'
plan=dict(created_utc=now,owner='cdp:st:C.2.D4.2',tag='01BX',original=bind(original),proposed=bind(proposed),freeze=bind(freeze),release=bind(release),events=bind(eventpath),guards=guards,proof_item_count=13,display_count=21,program_rows=programrows,orphan_edit=dict(old=orphan,new='',type='D09',owner='cdp:st:C.2.D4.2',location='After the double-cover proof',reason='Move program bookkeeping out of the mathematical text; the new exact programs are cited once in the Programs table. The local suspension table already has its own program citation at01CI.'),comparison_inputs=[bind('records/S6_SERIES_PUBLISH_II_root_BX_pending_review_20261122.json'),bind('code/S6_SERIES_PUBLISH_II_root_BX_prerelease.py'),bind('agents/continuation2_root/01BX/S6_SERIES_PUBLISH_II_root_BX_prerelease.json'),bind('code/S6_SERIES_PUBLISH_II_root_BX_postrelease.py'),bind('code/S6_SERIES_PUBLISH_II_root_BX_postrelease.json'),bind('records/S6_SERIES_PUBLISH_II_RAT6_restore_20261122/manifest.json')],mathematical_errors_found=[],root_proposed_full_reading='Pending actual complete final-block reading; staging alone assigns no reading credit.')
planpath='agents/continuation2_root/01BX/S6_SERIES_PUBLISH_II_root_BX_prepared_plan.json';assert not (R/planpath).exists();(R/planpath).write_text(json.dumps(plan,indent=2)+'\n')
print(json.dumps(dict(plan=bind(planpath),proposed=plan['proposed'],guards=len(guards),proof_items=13,displays=21),indent=2))
