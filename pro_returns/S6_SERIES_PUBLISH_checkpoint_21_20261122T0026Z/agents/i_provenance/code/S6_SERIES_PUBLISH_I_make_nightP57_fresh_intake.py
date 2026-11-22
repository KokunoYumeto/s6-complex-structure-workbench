from pathlib import Path
from datetime import datetime,timezone
import re,json,hashlib
R=Path('/workspace/scratch/653608133b22');O=R/'work/agents/i_provenance'
p=R/'work/S6_SERIES_PUBLISH_I.tex';s=p.read_text()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def st(s,label):
 pos=s.index('\\label{'+label+'}')
 m=list(re.finditer(r'\\begin\{(theorem|lemma|proposition|corollary|remark|definition|cited)\}',s[:pos]))[-1]
 end=s.index('\\end{'+m[1]+'}',pos)+len('\\end{'+m[1]+'}')
 value=s[m.start():end]
 assert '\\begin{proof}' not in value,label
 return value
def dump(p,j):p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
target=st(s,'night:P5.7')
intake={'created_utc':datetime.now(timezone.utc).isoformat(),'source':str(p),'source_sha256':sha(p),'statement_id':'night:P5.7','statement':target,'target_proof_excluded':True,'warning':'Read this target statement and the separate prerequisite packet only until the independent comparison derivation is frozen. Neither the earlier source-comparison report nor any receiving P5.7 proof is an input.'}
dump(O/'S6_SERIES_PUBLISH_I_nightP57_fresh_statement_intake.json',intake)
defs={}
for label in ['def:common-conventions','I:def:family-parameter','night:P5.3','night:P5.4','night:P5.5','night:P5.6']:
 defs[label]=st(s,label)
oldp=R/'source/S6_SERIES_GRIND_I.tex';olds=oldp.read_text()
primary=R/'source/S6_GRIND_6_literature/papers/arXiv_2610.00250v1_Du_Guo_Kusakabe_Xie_src/v5oka_maps_modifications_deformations.tex'
ps=primary.read_text()
base=st(ps,'prop:period-data-existence')
# The primary's explicit generator laws are supplied as equations, without
# any receiving-paper delta formula, parameter map, or target-proof prose.
equations={}
for label in ['eq:period-generator-laws','eq:mu-generator-laws','eq:beta-generator-laws']:
 pos=ps.index('\\label{'+label+'}')
 start=ps.rfind('\\begin{equation}',0,pos)
 end=ps.index('\\end{equation}',pos)+len('\\end{equation}')
 equations[label]=ps[start:end]
primary_defs={'period_data_statement':base,'generator_equations':equations,'phi_definitions':r'\varphi_1=2-6(1-\mu)^2/\tau,\quad \varphi_2=-3-6\mu^2/\tau','admissible_definition':r'M_0=\sup_{z\in U}(\Im\beta_0(z)-6(\Im\mu(z))^2/\Im\tau(z));\quad\mathcal A=\{a:\Im a<-M_0\}.','primary_asserted_solution_scope':'The primary proof of Proposition period-data-existence cites AC Theorem3.4(i)–(v) for a holomorphic solution beta0 unique up to an additive constant, with the stated cusp behavior and equivariance. The source itself, rather than a receiving comparison formula, supplies this assertion.'}
paths=[R/'work/agents/provenance/literature/S6_SERIES_PUBLISH_DGKX.pdf',O/'literature/S6_SERIES_PUBLISH_I_DGKX_v2.pdf',O/'literature/S6_SERIES_PUBLISH_I_DGKX_v1_abs.html',O/'literature/S6_SERIES_PUBLISH_I_DGKX_v2_abs.html',primary,R/'source/S6_GRIND_6_literature/papers/arXiv_2610.00250v2_Du_Guo_Kusakabe_Xie_src/submited-tams.tex']
files=[{'path':str(x),'sha256':sha(x),'bytes':x.stat().st_size} for x in paths]
images=[]
for v,pages in [(1,[3,81,82,85,95]),(2,[1,2,3])]:
 for page in pages:
  img=O/f'literature/S6_SERIES_PUBLISH_I_DGKX_v{v}_p{page:03d}.png'
  images.append({'version':v,'printed_and_PDF_page':page,'path':str(img),'sha256':sha(img),'scope':'Primary page only; no receiving target-proof content.'})
packet={'created_utc':intake['created_utc'],'source_sha256':intake['source_sha256'],'scope':'Statement and prerequisite definitions plus primary source locators only. No receiving P5.7 proof, earlier comparison report, delta formula or source-to-target parameter map is supplied.','receiving_definitions_and_cited_statements':defs,'primary_DGKX_definitions':primary_defs,'primary_files':files,'primary_pages':images,'locators':{'v1':'Theorems1.3–1.4p3; Theorem6.12pp81–82; Proposition6.16p85; Theorem7.14p95. Direct primary https://arxiv.org/pdf/2610.00250v1','v2':'Front matter pp1–3 and complete primary TeX supplied for a statement inventory. Direct primary https://arxiv.org/pdf/2610.00250v2. No full-version rendered-page read is attributed to the packet author.'},'chronology':{'attached_original_source':str(oldp),'attached_source_sha256':sha(oldp),'verbatim_received_statement_only':st(olds,'night:P5.7'),'September_8_evidence_scope':'The attached original Paper I says public working edition by8September2026. This is an authorial historical assertion in the supplied record. No independently date-authenticated public deposit on8September has been located in this agent’s inspected scope; the later pinned20November repository commit alone cannot establish that earlier public-posting date. The current target says working-edition proof is dated8September.','September_23_primary_scope':'Retained official arXiv v1 HTML explicitly says Submitted on23Sep2026(this version) and Wed,23Sep2026 17:09:17UTC. Its file/hash is listed above.','instruction_scope':'The original user prompt requires retaining the credited appendix and the sole8September/23September comparison. This instruction does not create independent historical evidence.'},'mathematical_check_events_added':0}
dump(O/'S6_SERIES_PUBLISH_I_nightP57_fresh_primary_prerequisites.json',packet)
print(json.dumps({'statement':str(O/'S6_SERIES_PUBLISH_I_nightP57_fresh_statement_intake.json'),'prerequisites':str(O/'S6_SERIES_PUBLISH_I_nightP57_fresh_primary_prerequisites.json'),'source_sha256':intake['source_sha256'],'cited_statements_and_definitions':list(defs),'receiving_target_proof_excluded':True}))

