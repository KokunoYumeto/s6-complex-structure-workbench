from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, csv, copy

ROOT=Path('/workspace/scratch/653608133b22')
OUT=ROOT/'work/agents/i_provenance'
NOW=datetime.now(timezone.utc).isoformat()
SOURCE=ROOT/'work/S6_SERIES_PUBLISH_I.tex'
data=SOURCE.read_bytes(); text=data.decode(); source_sha=hashlib.sha256(data).hexdigest()
def h(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,j): p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
def bind(p): return {'path':str(p),'sha256':h(p),'bytes':p.stat().st_size}

abstract_tex=re.search(r'\\begin\{abstract\}\s*(.*?)\s*\\end\{abstract\}',text,re.S).group(1)
abstract=' '.join(abstract_tex.split()).replace('Bott--Chern','Bott–Chern')
method=re.search(r'\\subsection\{Methodology\}\s*(.*?)\s*\\subsection\{How the paper is organized\}',text,re.S).group(1)
snapshot=OUT/f'S6_SERIES_PUBLISH_I_provenance_source_{source_sha[:12]}.tex'
snapshot.write_bytes(data)
front_path=ROOT/'work/records/S6_SERIES_PUBLISH_I_front_status_receipt.json'
front=json.loads(front_path.read_text())
status_binding={}
for section in ['mechanisms','statuses','known_new_rows']:
    status_binding[section]={}
    for key,value in front[section].items():
        v=value.replace('\\\\','\\')
        status_binding[section][key]={'text':v,'source_occurrences':text.count(v)}

# Resolve the exact selected-resolution publication gate from the applied
# comparison receipt, without re-performing or re-counting that proof check.
dg_path=OUT/'S6_SERIES_PUBLISH_I_DG_literature_status.json'
dg=json.loads(dg_path.read_text())
old_dg=copy.deepcopy(dg)
prior_dg=OUT/f'S6_SERIES_PUBLISH_I_DG_literature_status_prior_{h(dg_path)[:12]}.json'
if not prior_dg.exists(): dump(prior_dg,old_dg)
applied=ROOT/'work/agents/i_topology/editorial/S6_SERIES_PUBLISH_I_P210_resolution_applied_binding.json'
for row in dg['rows']:
    if row['id']=='I-F-status-02':
        row['records']='The corrected selected-diagonal charts, parameter map and involution lift were applied and compared in the topology receipt listed below. The proper flat untwisted filling and the exact proposed-model Euler comparison remain as stated.'
        row['status']='Selected-diagonal correction applied and bound by its existing evidence group; no new event is added here. The exact proposed-model correction and explicit filling retain their full marked maps.'
        row['applied_resolution_receipt']=bind(applied)
dg['publication_status_binding']=bind(front_path)
dg['source_sha256']=source_sha
dg['recorded_utc']=NOW
dg['remaining_gate']='Final root source/count binding and actual final-PDF reading; no mathematical event is created by this table.'
dump(dg_path,dg)

counts_tokens={'targeted proof check':'{{TARGETED}}','independent re-proof':'{{REPROOF}}','computation or formal certificate':'{{COMPUTATION}}','used and rechecked in this run':'{{USED}}','carried as background without fault found':'{{BACKGROUND}}',"refuted, with the refined statement's id":'{{REFUTED}}'}
method_template=method
patterns=[(r'\d+ examinations of proof steps','{{TARGETED}} examinations of proof steps'),(r'\d+ independent\s+re-derivations','{{REPROOF}} independent\nre-derivations'),(r'\d+ computations or formal certificates','{{COMPUTATION}} computations or formal certificates'),(r'\d+ readings of the proofs and applications','{{USED}} readings of the proofs and applications'),(r'\d+ uses of background results without a fault found','{{BACKGROUND}} uses of background results without a fault found'),(r'\d+ refutations? associated','{{REFUTED}} refutation(s) associated')]
for pattern,replacement in patterns:
    method_template,n=re.subn(pattern,replacement,method_template)
    assert n==1,(pattern,n)
(OUT/'S6_SERIES_PUBLISH_I_methodology_scaffold.tex.in').write_text(method_template+'\n')

pin='83d76022bcd442278b760db9ff438afceed6c6ea'
repo='https://github.com/KokunoYumeto/s6-complex-structure-workbench/tree/'+pin
# Mirror the actual source's scoped production account.  In particular, retain
# the nonexclusive Sol contribution and the pinned account of Astra from 5 Sep,
# without assigning unexamined historical sessions to Paper I statements.
production_tex=method.split('For the statements printed in this paper,')[0]
production_plain=' '.join(production_tex.split()).replace('--','–')
production_plain=production_plain.removeprefix('This text is AI-produced; no part of it was written by a human. ').strip()
provenance=(
'Text: AI-authored; none of it was written by a human. The submitter takes responsibility for the veracity of the text.\n\n'
'How it was produced. '+production_plain+' These historical identities, settings and dates report the documented contributions; the present run does not independently reconstruct a complete historical session inventory. The accompanying provenance receipt records the remaining bounded attribution gap.\n\n'
'How it was checked. The final ledger totals are to be inserted after the root source and CHECK_EVENTS freeze: {{TARGETED}} targeted examinations of proof steps, {{REPROOF}} independent re-derivations, {{COMPUTATION}} computations or formal certificates, {{USED}} uses and proof rereadings, {{BACKGROUND}} background uses without a fault found, and {{REFUTED}} refutations linked to the corrected statement. These are event-to-statement associations. One evidence group may support several statement associations; its reuse does not create another independent derivation. Every event retains its declared mathematical scope, original event identity and evidence group. Derivation before reading the target proof, comparison after exposure, and rereading an edited proof retain those respective descriptions. Metadata scans, bibliography authentication, online literature searches and rendered-page presentation review contribute no mathematical check events. Final statement/environment totals and evidence-group totals remain unbound in this scaffold.\n\n'
'Human understanding. No human has checked the new mathematics of this paper. The submitter directed the research and takes responsibility for the submitted text.\n\n'
'Raw outputs and current records. Historical source outputs, programs and check records are at '+repo+'. That historical commit does not claim to contain the present publication revision or its new checks. The additional publication records and programs accompany the source distribution. The text and accompanying work are dedicated under CC0 1.0 Universal.'
)
deposit={
'title':'The $(3,4,\\infty)$ family of complex six-spheres. I. Periods, moduli and the two ends',
'abstract':abstract,
'comments':'Paper I of the five-paper series “The (3,4,∞) family of complex six-spheres”. This paper determines the marked periods, parameter equivalences, cohomology and deformation data, puncture obstruction, outer boundary and arithmetic norm identities of the displayed family. It studies the constructions of Claude and L. Alpöge (https://alpo.ge/s6.pdf), Engel (https://arxiv.org/abs/2609.38442), and Viaclovsky (https://arxiv.org/abs/2610.39102), with the standard classification and deformation results of Du, Guo, Kusakabe and Xie credited to the separately paginated version 1 (https://arxiv.org/abs/2610.00250v1). Historical series sources, programs and check records are at '+repo+'; the additional publication revision and current check records accompany this source distribution.',
'subject':'math.CV','crossListSubjects':['math.AG','math.GT','math.NT'],
'tags':['complex six-spheres','compact complex threefolds','non-Kähler manifolds','periods and monodromy','complex moduli','Bott–Chern cohomology','Picard twists','analytic degenerations','elliptic heights','AI-authored mathematics'],
'mscCodes':['32J17','32G05','32G20','32Q55','11G50'],
'authorshipMode':'no-human-author-claimed','authors':[{'name':'','affiliation':''}],'submittingContributorIndex':0,'sponsorName':'','submittingOrganizationId':None,'humanUnderstanding':'none','provenance':provenance,
'aiSystems':[{'provider':'OpenAI','model':'GPT-6 Astra (ChatGPT Pro mode; current reasoning effort inherited, no separate numerical setting exposed)','version':None},{'provider':'OpenAI','model':'GPT-5.6 Sol (Codex, reasoning effort ultra; historical record)','version':None},{'provider':'Anthropic','model':'Claude Fable 5.2 (effort high and max; historical record)','version':None},{'provider':'Anthropic','model':'Claude Opus 5.5 (effort max; historical record)','version':None}],
'correctnessConfirmed':None,'communityInterestConfirmed':None,'citationsConfirmed':None,'license':'CC0 1.0','rightsConfirmed':None,'arxivId':None}
deposit_path=OUT/'S6_SERIES_PUBLISH_I_deposit_fields_scaffold.json'
dump(deposit_path,deposit)

prior_path=OUT/'S6_SERIES_PUBLISH_I_three_way_claim_table.json'
prior=json.loads(prior_path.read_text())
claims=copy.deepcopy(prior['claims'])
updates={
'I-P01':('The exact current title and Paper I identity are copied to the deposit scaffold. The common series paragraph still awaits the root series-wide consistency gate.','current source/deposit identity bound'),
'I-P02':('The complete current abstract is copied verbatim apart from line wrapping and the typographic Bott–Chern dash; all seven exact main-status rows are bound below. No Paper V result is imported.','abstract/deposit bound; final PDF gate open'),
'I-P03':('AC Remark3.12 p19 gives the generator and Abel–Jacobi sign. Engel Lemma2.1 proof pp3–4 gives height1/6 and (6P).O=2; Definition2.3p5 gives the quotient input. The exact Weierstrass, differential and lattice transports remain explicit.','precise primary scopes corrected and applied'),
'I-P06':('The assigned third checks and analytic global comparison are supplied in i_analytic records. This table claims no new proof check; root final count/dependency freeze remains controlling.','mathematical records delivered; final gate open'),
'I-P09':('Exact local-height/scaling checks were delivered, including the separately scoped sigma–theta normalization derivation and the corrected lifted branch statement. The current arithmetic clauses are retained at that recorded scope.','mathematical records delivered; final gate open'),
'I-P10':('The standard 2Z classification remains credited to DGKXv1, with the full required credited appendix. The proper-family construction was moved earlier with all labels and exact gluing maps retained.','credit and structural guard applied'),
'I-P12':('The current status row B and known/new table credit the standard equivalence and describe the displayed discrete-data extension with exact affine and cusp maps.','current root status applied and bound'),
'I-P13':('The full real-structure proofs, marked involutions, integral fixed-lift calculations and cap maps were compared in the exposed editorial records. Their operative programs are authenticated at the historical pin.','editorial proof comparison and program scope delivered'),
'I-P17':('The current root D status/table distinguish the evaluated scalar and full algebra from the cited general identities. The root global D/E comparison supplies mathematical review; this source table adds no event.','current root status applied and bound'),
'I-P19':('The exact global coefficient representatives remain in the root proof and D status; no old unresolved-atlas statement is copied into the abstract or deposit.','current scope/abstract bound'),
'I-P22':('The E status and known/new line retain the all-twist and higher-root formulas, exact specialization at k=l=1 and the credited standard untwisted conclusions.','current root status applied and bound'),
'I-P23':('Topology supplied scoped independent and global checks. The current F status keeps the full finite-cover proper Hausdorff obstruction and its exact corner map.','current root status applied and bound'),
'I-P24':('The selected small-resolution diagonal correction is applied, with the topology binding receipt preserved. The Euler comparison concerns exactly Engel’s proposed central model; the explicit untwisted filling remains.','selected-resolution correction applied; final PDF gate open'),
'I-P25':('The topology checks and G status retain the intrinsic Albanese map w→iw/216 and the full continuation scope.','current root status applied and bound'),
'I-P27':('Primary T0,T1, positive circle class and positive-root affine convention were supplied from Engel Theorem5.1p13, equation6.1p16 and Lemma3.6p11. The fresh checker completed inv:B1.0 and night:P5.7; the root completion manifest binds their frozen derivations and comparisons. This agent disclosed earlier Pmark/sign exposure and claims no blind check.','fresh marking and exact-parameter checks completed; this table adds no event'),
'I-P32':('The root applied the exact DGKX/Grauert/Schroeer–Siebert aliases, removed printed verification history, sorted the retained entries and archived unused entries. BM95AB/BM97 remain as separately qualified editions; no unverified edition merge is made. Exact current primary citation receipts and root bibliography-link corrections are retained.','bibliography dispositions applied; final rendered citation reading remains'),
'I-P33':('Deposit mirrors the source’s nonexclusive Sol/ultra contribution and the pinned repository’s Astra/ultra participation from5September. The README also mentions occasional Luna/Terra sessions without individual settings/dates; the provenance receipt records that bounded gap without assigning retained Paper I contributions or check events. No complete historical session inventory is claimed.','documented historical contributions bound; bounded attribution gap disclosed in records'),
'I-P34':('Current methodology already says publication20–21Nov2026 and inherited effort with no separate numerical setting exposed. Deposit uses the same facts and identifies Paper I continuation work on21Nov.','current wording correct and copied; final count fields unbound'),
'I-P35':('Current root count snapshot is preserved only as observed text. Final numeric fields in the scaffold remain tokens; no recomputation occurs here. Evidence reuse and source-only/PDF-only exclusions are explicit.','final root count freeze awaited'),
'I-P36':('The root parser attaches actual immediate and exact deferred proofs plus each main theorem’s own outline, excluding hidden headers and unrelated further results. The initial270/29 figures remain historical intake metadata only. The newly exposed inv:B1.0 and night:P5.7 obligations are completed in the root manifest.','parser correction and exposed obligations completed; final dependency freeze awaited'),
'I-P39':('The root applied the end table of78 unique authenticated raw source links and the34 residual boundary edits. The nine affected full proofs were compared with the originals and bound to their one existing reread evidence group. Four family/maps programs and seven boundary sources retain exact pinned paths and scopes; the diagnostic cusp enumeration remains records-only. Fresh current checks are kept outside old-pin claims.','program table and body scope guards applied; final rendered table reading remains'),
'I-P40':('A–C and D–G bounded online status searches are recorded separately, and the exact root A–G mechanism/status/table strings are bound below. No exhaustive absence or first-priority inference is made.','all seven main-status search scopes recorded'),
'I-P42':('Paper I deposit scaffold uses the actual current abstract, scoped model/date facts and exact status map; final counts and actual final-PDF reading remain open. The attached V form supplies field structure only.','scaffold ready; final source/count/PDF gates open')}
for row in claims:
    if row['id'] in updates: row['disposition'],row['status']=updates[row['id']]
    row['count_comparison']='Not a numerical count claim; consult scoped CHECK_EVENTS for any mathematical-review claim.'
    row['old_HEXAGON_METADATA_V_comparison']='Paper V form supplies field structure and reported shared historical model facts only. No V theorem, count, review episode or numerical certificate is transferred to Paper I.'
    row['deposit_location']='provenance/comments; exact abstract for mathematical scope' if row['id'] not in ['I-P35','I-P42'] else 'provenance; pending final-count binding receipt'
    if row['id']=='I-P35': row['count_comparison']='Final recomputation deliberately deferred to the parent’s frozen root ledger; count tokens remain unbound.'
    if row['id']=='I-P27': row['primary_or_check_evidence']='S6_SERIES_PUBLISH_required_check_completion_manifest.json; agents/i_marking/S6_SERIES_PUBLISH_I_invB10_comparison.md and S6_SERIES_PUBLISH_I_nightP57_comparison.md; this agent supplied primary-only inputs and adds no independent credit.'
    if row['id']=='I-P03': row['primary_or_check_evidence']='AC primary p19, Engelv1 pp3–5; analytic global ABC/source-split receipt confirms the exact generator/sign and height scopes.'
records={}
for p in [ROOT/'work/records/CHECK_EVENTS.tsv',ROOT/'work/records/S6_SERIES_PUBLISH_statement_check_counts.csv']:
    records[str(p)]=bind(p)
scope_records={}
for p in [ROOT/'work/records/S6_SERIES_PUBLISH_required_check_completion_manifest.json',ROOT/'work/records/S6_SERIES_PUBLISH_I_program_table_receipt.json',ROOT/'work/records/S6_SERIES_PUBLISH_I_bibliography_disposition.json',ROOT/'work/records/S6_SERIES_PUBLISH_I_bibliography_link_receipt.json',OUT/'S6_SERIES_PUBLISH_I_boundary_program_applied_binding.json',OUT/'literature/S6_SERIES_PUBLISH_I_CDL_Xiao_locator_receipt.json',OUT/'literature/S6_SERIES_PUBLISH_I_September8_historical_scope_receipt.json',OUT/'literature/S6_SERIES_PUBLISH_I_pinned_README_receipt.json',OUT/'S6_SERIES_PUBLISH_I_historical_model_qualification_guard.json']:
    scope_records[str(p)]=bind(p)
current={'paper':'I','recorded_utc':NOW,'source':str(SOURCE),'source_sha256':source_sha,'source_snapshot':str(snapshot),'abstract_tex_sha256':hashlib.sha256(abstract_tex.encode()).hexdigest(),'deposit_abstract_sha256':hashlib.sha256(abstract.encode()).hexdigest(),'previous_claim_table':bind(prior_path),'claims':claims,'exact_main_status_binding':status_binding,'front_status_receipt':bind(front_path),'records_bound_without_recomputation':records,'counts_recomputed':False,'mathematical_events_added':0,'limitation':'Publication scaffold only. Final source/count freeze, remaining bibliography integration and actual final-PDF reading are not certified here.'}
current['scope_receipts']=scope_records
dump(OUT/'S6_SERIES_PUBLISH_I_three_way_claim_table_current.json',current)
md=['# Paper I: current three-way provenance scaffold','',f'Source SHA-256: `{source_sha}`. Snapshot and records are bound without a count recomputation. No new mathematical event is created.','', '| ID | Claim / location | Records and primary evidence | Current disposition |','|---|---|---|---|']
for row in claims:
    def cell(s): return s.replace('|','\\|').replace('\n',' ')
    md.append('| '+' | '.join(cell(str(x)) for x in [row['id'],row['current_claim_or_issue']+' ('+row['current_location']+')',row['attached_record_comparison']+' '+row['primary_or_check_evidence'],row['disposition']+' '+row['status']])+' |')
(OUT/'S6_SERIES_PUBLISH_I_three_way_claim_table_current.md').write_text('\n'.join(md)+'\n')

msc={'32J17':'Compact complex 3-folds','32G05':'Deformations of complex structures','32G20':'Period matrices, variation of Hodge structure; degenerations','32Q55':'Topological aspects of complex manifolds','11G50':'Heights'}
receipt={'created_utc':NOW,'source':bind(SOURCE),'source_snapshot':bind(snapshot),'deposit':bind(deposit_path),'claim_table':bind(OUT/'S6_SERIES_PUBLISH_I_three_way_claim_table_current.json'),'methodology_observed':method,'methodology_template':bind(OUT/'S6_SERIES_PUBLISH_I_methodology_scaffold.tex.in'),'counts_status':'Unbound. The current printed numbers are an observed interim root snapshot, not final figures or a recomputation by this agent.','count_fields':counts_tokens,'additional_final_fields':['statement_environment_count','subject_ID_count','association_total','declared_evidence_group_count','outline_counts','source_sha256','ledger_sha256','count_report_sha256','final_PDF_sha256','final_reading_receipt'],'main_status_binding':status_binding,'msc_proposal':msc,'msc_source':'Official AMS MSC2020 database and official zbMATH MSC2020 PDF, retrieved search result stored in literature/S6_SERIES_PUBLISH_I_MSC_search_raw.json. Codes are editorial subject choices, not priority claims.','subject_choice_scope':'math.CV primary; math.AG/math.GT/math.NT are proposed cross-lists reflecting the actual algebraic, topological and arithmetic content. They are not copied from the V form.','confirmations':'Null fields are unsubmitted scaffold placeholders. No external deposit or correctness/rights certification was performed.','mathematical_events_added':0}
dump(OUT/'S6_SERIES_PUBLISH_I_deposit_scaffold_receipt.json',receipt)
human=['# Paper I deposit fields — scaffold','', '**This file is ready for the final source/count binding, not for submission.**', '', '## Title','',deposit['title'],'','## Abstract','',abstract,'','## Comments','',deposit['comments'],'','## Provenance','',provenance,'','## Subjects and license','', 'Primary: math.CV. Proposed cross-lists: math.AG, math.GT, math.NT. MSC2020: '+', '.join(msc)+'. CC0 1.0 Universal.','', '## Open binding fields','', 'Final root counts and declared evidence-group totals; exact final source/ledger/PDF hashes; actual final-PDF reading. The inv:B1.0 and night:P5.7 checks are completed in the root manifest. No Paper V review episode or count has been imported.']
(OUT/'S6_SERIES_PUBLISH_I_deposit_fields_scaffold.md').write_text('\n'.join(human)+'\n')
print(json.dumps({'source_sha256':source_sha,'claims':len(claims),'abstract_words':len(abstract.split()),'main_status_occurrences':{k:{a:b['source_occurrences'] for a,b in v.items()} for k,v in status_binding.items()},'counts_recomputed':False,'math_events':0}))
