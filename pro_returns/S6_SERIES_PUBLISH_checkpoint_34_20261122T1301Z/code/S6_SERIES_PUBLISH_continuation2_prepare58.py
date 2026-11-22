from pathlib import Path
import csv,datetime as dt,hashlib,json,re,sys
R=Path(__file__).resolve().parents[1]
def bind(p):return dict(path=p,sha256=hashlib.sha256((R/p).read_bytes()).hexdigest())
def read(p):return json.loads((R/p).read_text())
def verify(o):
 if isinstance(o,dict):
  if 'path' in o and 'sha256' in o:assert bind(o['path'])['sha256']==o['sha256'],o['path']
  for v in o.values():verify(v)
 elif isinstance(o,list):
  for v in o:verify(v)

pre='agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_02XR_'
ip=pre+'final_v1_index.json';idx=read(ip)
assert bind(ip)['sha256']=='82ea667149cb3defafd2f1b2ebc527b4cb77484334127abec5a94f3cce7f49e8';verify(idx)
pp=pre+'final_v1_proposals.json';p=read(pp);verify(p);t=p['blocks'][0]
sp='agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_WY_XR_scope_chronology_20261122.json';sc=read(sp)
assert bind(sp)['sha256']=='5977511da1b39e8b2de2ba2e9c3c45e34cbf6e2666e774df026ac55ed0ec3ce4';verify(sc)
assert sc['exposure_and_credit']['XR_target_proof_ever_opened_by_this_checker'] is False
assert sc['exposure_and_credit']['C_XR_derivation_or_comparison_opened'] is False
guards=[dict(old=g['old'],new=g['new'],type=g['defect_type'],reason=g['reason']) for g in t['guards']]
guards.extend([
 dict(old='\\begin{proposition}[P4.52]',new='\\begin{proposition}[Multiplicity of contracted horizontal pole sections]',type='D04,D16',reason='Replace the production identifier in the title by the mathematical assertion.'),
 dict(old='In the remaining positive ruled support of Part~4.2,',new='In the remaining positive ruled support of \\cref{sec:II:night-sign},',type='D04',reason='Resolve the standing section reference without changing the positive ruled-support domain.')])
old=(R/t['original_full_block']['path']).read_text();new=old
for g in guards:
 assert new.count(g['old'])==1;new=new.replace(g['old'],g['new'],1)
assert old.count('\\item')==new.count('\\item')==9
assert re.findall(r'\\\[(.*?)\\\]',old,re.S)==re.findall(r'\\\[(.*?)\\\]',new,re.S)
for pat in [r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}']:assert re.findall(pat,old)==re.findall(pat,new)
np='agents/continuation2_root/S6_SERIES_PUBLISH_II_root_XR_v2_proposed.tex'
if (R/np).exists():assert (R/np).read_text()==new
else:(R/np).write_text(new)
if '--reviewed' not in sys.argv:
 print(json.dumps(dict(proposed=bind(np),full_final_reading_pending=True)));sys.exit(0)
now=dt.datetime.now(dt.timezone.utc).isoformat()
review='records/S6_SERIES_PUBLISH_II_root_continuation2_batch58_review.json';assert not (R/review).exists()
evb=read(pre+'final_v1_evidence_bindings.json');verify(evb)
review_data=dict(created_utc=now,checker='GPT-6 Astra (OpenAI), ChatGPT Pro mode, root, second continuation; reasoning effort not separately exposed',
 actual_reading='Root read the complete frozen XR derivation and its postrelease completion before opening the original target. Root then read the full separate WY-to-XR scope receipt, the exact R6/R15 statements, and historical WY Sections0/1 before opening XR. All nine original proof items, all nine agent-final-v1 items and all nine root-final-v2 items, all eleven original displays, the full comparison, both full program sources and outputs, all guards and event/source/computation receipts were read. The source-image openings are credited exactly to C receipts; no new root primary-source opening is claimed.',
 required_check_disposition='One composite independent checking group. C independently wrote the main residue/transverse-spectrum/trace route before XR release, but its last R15 application lacked a written critical-curve justification. That omission remains visible in the immutable freeze and every event. A had independently proved the full strict-conductor image assertion in WY Section1 at 06:33:54.058752, before C opened XR at 06:39:19.258256. A then verified the exact domain and contracted-H specialization in a separately dated receipt, without ever opening XR target proof or C derivation/comparison. This supplies the outstanding applicability step independently of the printed target. The required row is closed on those combined records and the full comparison, not on a false assertion that C alone froze every justification. There is no second independent event for A, root or the postrelease completion.',
 mathematical_review=[
 'The standing Y,f,S and finite normalization nu:N->S are identical in WY and XR, with the same minimal resolution pi:T->N and composite rho. Finiteness of nu and contraction of connected H by rho force pi(H) to be one point. R6 makes its exceptional configuration meet a noncontracted strict conductor component, whose image is a curve through rho(H). For a reduced germ g, each germ component of V(dg) through that point has constant g=0, so V(dg)_red=V(g,dg)_red. Thus R15 applies at multiplicity two. Its even product branches and odd finite birational parametrization have smooth normalization, excluding a contracted curve in the minimal resolution. This reproduces exactly the independently written WY fact; it does not backdate the later application receipt.',
 'The ambient blowup chart (r,ru,rv) has Jacobian r^2 and transforms the residue by r^(2-d), giving 2=(d-2)n+a. The new normalization resolution maps through the old minimal resolution and has the same positive-genus strict transform. Finite duality gives effective strict conductor. On its exceptional configuration Q=-intersection is positive definite with nonpositive off-diagonal entries, and Q a=K.C_i+Cstrict.C_i>=0. Splitting a into its positive and negative parts proves a>=0; the positive-genus equation has positive right side and forces a_i>0. Hence d<=4 and d=4 implies n=1,a=0. H is then generically outside both exceptional and conductor loci and maps birationally to a multiplicity-one positive-genus component of the quartic. Its degree is3 or4, forcing the full quartic reduced.',
 'The frozen alternative treats the actual germ. Positive-genus irreducible quartics have total delta<=2 and only A_j singularities of total j<=4; a smooth cubic plus line has contact budget3 and total j<=5. Parametric splitting and Weierstrass give the actual transverse Milnor budget<=5. The Siersma equivariant maps j2(M-I)=VARII j and vertical mapping-torus invariants contain every nonunit eigenvalue in transverse H1; the n=2 H1 containment is read at its exact source locus. The A_j lattice spectra and all19 budget partitions have full-column-rank first-three-trace matrices. The analytic A Campo trace formula gives zero first three Lefschetz traces and positive fourth trace at the first multiplicity-four exceptional plane, contradicting those matrices. The printed homogeneous proof is separately preserved and compared through the same j/j2, transverse monodromy and virtual homology objects.',
 'For the printed compact transport, the nonzero homogeneous fibre has nonvanishing differential by Euler identity. The scaled analytic family and its gradient vector field on a compact neighborhood transport any finite cycle collection and intersections into the actual local fibre. The proper semialgebraic radius has finitely many critical values and an invariant product end, producing the required compact core. Scalar monodromy acts freely away from identity. The covering to P2 minus the reduced quartic has degree4 and Euler4(7-M), so Fourier inversion gives virtual multiplicity7-M for each C4 character. Nontrivial H2 multiplicities are at least these virtual multiplicities. Thus rank(T-I)>=3(7-M), while the boundary Wang sequence and exact variation identity give rank(T-I)<=M. For M<=5 the exact gap21-4M>=1 excludes the quartic.',
 'The original isolated-point Morse step remains: an isolated hypersurface critical point has positive Milnor number; a small morsification and the smooth transverse Milnor boundary permit path transport to the original nonzero fibre. The sphere has square-2, contradicting P4.51. This is compared after release as the printed alternative to the independently supplied conductor-image argument. The even normalization graphs and odd parametrization (Y,X,Z)=(u^2,i u^m,Z) are finite birational maps from smooth charts; multiplicity one is smooth. All cases give the stated exact multiplicity three.',
 'Both complete programs and exact outputs were read. The prerelease program constructs minus cyclic permutation on the integral augmentation lattice and checks all19 transverse partitions. The postrelease program derives the printed normalization Euler identity, C4 rational idempotents/ranks, all integer gaps and blowup Jacobian by a different exact method. The named old quartic_tangent.py remains unavailable under its recorded file-list and404 search; no method, read or replay is attributed to it.'
 ],
 editorial_disposition='All nine original steps and eleven displays are preserved. Root v2 adds only a mathematical title and resolving standing-section reference to immutable agent v1. The local matrix expansion specifies the original argument. Only the program verifying the printed homogeneous calculation is cited in Programs; the alternative transverse-trace program stays in the check evidence and delivered code. Global small-tag, equation-number and residual style passes remain open.',
 mathematical_errors_in_printed_statement=[],original_proof_items_preserved=9,original_displays_preserved=11,new_required_owners=1,independent_groups=1,events_proposed=3,publication_page_reading_credit=0,
 evidence=[bind(ip),bind(sp),idx['frozen_derivation'],idx['comparison'],bind(pre+'final_v1_postrelease_completion.md'),bind(np),*evb['bindings']])
(R/review).write_text(json.dumps(review_data,indent=2)+'\n')
with (R.parent/'S6_SERIES_GRIND_tags.tsv').open() as f:pages={x['tag']:x['page'] for x in csv.DictReader(f,delimiter='\t')}
note='Required-row admission uses the composite proof described in '+review+'. A independently wrote the R6 strict-conductor image fact in the WY freeze at 06:33:54.058752 UTC, before XR release, and supplied the exact contracted-H specialization without opening XR or C proof/comparison; separate receipt '+sp+'. C own omission/completion timing remains unchanged. No additional evidence group or event is awarded. Root full finalv2 reading completed at '+now+'.'
target=dict(owner='night:P4.52',tag='02XR',old_page=pages['02XR'],original=t['original_full_block'],proposed=bind(np),freeze=idx['freeze_receipt'],release=idx['release_receipt'],events=bind(pre+'final_v1_event_proposals.json'),guards=guards,who=review_data['checker'],scope='Multiplicity exactly three for the image of the contracted horizontal pole section in the specified positive ruled support; independent applicability supplied by the separately written conductor-image argument, with all chronology preserved.',event_note=note)
pr=read(pre+'final_v1_programs_table_proposal.json');g=pr['guards'][0]
added=g['new'][len(g['old']):];rows=''.join(line+'\n' for line in added.splitlines() if 'final_v1_printed_certificate.py' in line);assert rows and 'trace_certificate' not in rows
s=(R/'S6_SERIES_PUBLISH_II.tex').read_text();start=s.index('\\section*{Programs}');end=s.index('\\end{longtable}',start);last=s[s.rfind('\n',start,end-1)+1:end];assert last.strip()
extra=[dict(old=last,new=last+rows,type='D09,D18',owner='Programs',location='Programs',reason='Cite the exact program checking the printed homogeneous Euler/character/residue calculation once; preserve the alternative trace program in check evidence only.')]
copies=[]
for cp in pr['program_copy_proposals']:
 copies.extend([dict(**{'from':dict(path=cp['from'],sha256=cp['sha256'])},to=cp['to']),dict(**{'from':dict(path=cp['output_from'],sha256=cp['output_sha256'])},to=cp['output_to'])])
cfg=dict(batch=58,root_review_complete=True,source_before_sha256=bind('S6_SERIES_PUBLISH_II.tex')['sha256'],ledger_before_sha256=bind('CHECK_EVENTS.tsv')['sha256'],review_evidence=[bind(review),bind(ip),bind(sp),bind(pp),idx['comparison'],idx['frozen_derivation'],*evb['bindings']],targets=[target],additional_source_edits=extra,code_copies=copies,mathematical_repairs=[],scope='02XR admitted on one composite independent checking group with the critical-curve step supplied by the separately frozen WY conductor-image argument and a target-unexposed exact scope application. C own postrelease omission/completion is retained, never backdated. All nine original items and eleven displays remain;15 target guards and one program reference. Three events within one group; no global defect-class or page-reading closure.')
assert cfg['source_before_sha256']=='c920ca31e439809154a6e95ac40d9f1eda21cc8f1074a92a7fecac1a576bf0a0'
assert cfg['ledger_before_sha256']=='6704bd335a470ed37627c3c14acfc9609499a4b45e5b16efa348ad9db7afeba1'
out='records/S6_SERIES_PUBLISH_II_continuation2_batch58_config.json';assert not (R/out).exists();(R/out).write_text(json.dumps(cfg,indent=2)+'\n');print(json.dumps(bind(out)))
