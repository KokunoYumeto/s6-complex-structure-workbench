from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,csv
R=Path('/workspace/scratch/653608133b22');O=R/'work/agents/i_provenance'
now=datetime.now(timezone.utc).isoformat()
p=O/'S6_SERIES_PUBLISH_I_boundary_program_comparison.json';j=json.loads(p.read_text())
scopes={
'push:src:B.1.1':'Reread the complete four-step finite-root plumbing proof: the exact exponential bundle/period morphism, xy=u to xy=r^12 and its unit-compatible toric charts, the ruled-bundle triviality criterion and finite-isogeny norm argument, and the discrete torsion loci. The positive model statement retains all morphisms and all quantified nontriviality conclusions; the Engel height locator is the actually read pp3–4.',
'push:src:B.1.2':'Reread all four steps: covariance/invariant vectors; affine maps and unit descent; free component/node actions, flatness/multiplicity; marked isogenies and the punctured c-shift gauge. Every map and its r!=0 domain is retained.',
'push:src:B.2.1':'Reread all five steps: base-change lattice, forced rays and bridge, cone intersections/volume, quotient/flatness/properness, star/gluing and component monodromy. General-n proof unchanged; program scope exactly n=2,12.',
'push:src:B.3.1':'Reread all four steps: top-fan overlap, proper component cover, dihedral/peripheral conventions and four residues. Obstruction remains exactly for the prescribed finite and plain cusp models.',
'push:src:B.3.3':'Reread both steps: dZ² lattice, translation order d/gcd(d,a,b), point-isotropy normal coordinate s^h0, multiplicity d/h0, and order-n lower bound. Removed script prose was finite d<=60 diagnostic evidence; no general independent credit.',
'push:src:B.3.4':'Reread all nine steps: curve/surface substitutions, section orbit/line, affine and I12 intersections, height matrix, torsion exclusion, NS index, half-integral trace contradiction and exact trace image. Equations and geometric inputs unchanged. Symbolic code scope is only identities/matrices/series/residue arithmetic; external source-page authentication remains separate.',
'push:src:B.3.5':'Reread pole-order basis, coefficient equations, lower height bound and exclusion of three nonzero half-classes. Integral saturation and determinant conclusions unchanged.',
'push:src:B.3.6':'Reread all seven steps: continuous five-term sequence, trace quotient, local norms, localization/ramification correction, regular torsor model, affine extension/twelfth-power adjustment, and remaining line/cusp/family data. Finite program scope is cochains/components; it is not credited with torsor existence.',
'push:src:B.3.7':'Reread all eight steps: relative Picard lift/square, normal-line degree, explicit Pic0 inverse, exact collars/plumbing, two small resolutions, both Euler calculations and valuation divisibility. Geometric multiplicity proof retained; code scope limited to polynomial/Euler arithmetic.'
}
group='eg:publish-iprovenance-boundary-program-editorial-'+j['source_sha256'][:16]
j.update(actual_reread_completed_utc=now,reading_method='Each full original proof and each full proposed proof were read in tool output. Every changed passage was compared with its archived original. The final parent-requested deletions remove only the already compared program-bookkeeping sentences. Labels/tags and displayed equations were additionally checked for exact equality.',evidence_group=group,exposure='All target proofs exposed; no derivation-before-target-proof or new computational credit.',new_used_and_rechecked_associations=9)
for row in j['proofs']:row['reread_scope']=scopes[row['statement_id']]
p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
md=O/'S6_SERIES_PUBLISH_I_boundary_program_comparison.md'
lines=['# Paper I: boundary program and prose comparison','',f'Completed {now}. Source SHA-256: '+j['source_sha256']+'.','',f'Evidence group: {group}. Nine exposed proof-reread associations; zero independent or computational events. Authentication adds no mathematical events.','', 'The full original and proposed proof blocks were actually read. All labels, tags and displayed equations remain unchanged. All seven complete primary code sources were read and their raw bytes authenticated against exact pinned Git blobs; none was executed. The final six deleted certificate sentences repeat no mathematical input, calculation or result: each is already explicit in its proof. The statement-to-program map now appears in the end-table row.','']
for row in j['proofs']:lines+=['## '+row['statement_id'],'',scopes[row['statement_id']],'','Original: '+row['original'],'Proposed: '+row['proposed'],'']
lines+=['## Program scope','', 'Six operative programs have exact raw pinned URLs and receiving statement IDs. The cusp-root residue script covers root degrees1–60 and remains a diagnostic record. The auxiliary script verifies characteristic-polynomial and Euler arithmetic; the printed valuation argument proves geometric cusp multiplicity. No finite script is credited with analytic gluing or torsor existence.','', '## Bibliography boundary','', 'Shioda90, CDL24 and Xiao91 exact primary-page authentication is not claimed by this reread record. Their named inputs and receiving maps remain unchanged; locator work is separate.']
md.write_text('\n'.join(lines)+'\n')
fields=['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group']
who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited (no separate numeric setting exposed), S6_SERIES_PUBLISH/provenance_inventory'
out=O/'S6_SERIES_PUBLISH_I_boundary_program_CHECK_EVENTS.tsv'
with out.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader()
 for i,row in enumerate(j['proofs'],1):
  sid=row['statement_id'];typ='used and rechecked in this run'
  w.writerow(dict(statement_id=sid,date=now[:10],who=who,type=typ,outcome=scopes[sid]+' Exposed editorial comparison only; no independent or computational credit.',event_id='ce:publish-iprovenance-boundary-program-'+sid.replace(':','-').replace('.',''),phase='S6_SERIES_PUBLISH_I_editorial_reread',source_file=str(md),source_row=i,source_event_type=typ,evidence_group=group))
s=(R/'work/S6_SERIES_PUBLISH_I.tex').read_text()
a=s.index('We use the Claude--Alp');b=s.index('\\hypertarget{main-I-A}',a)
primary=R/'source/S6_GRIND_6_literature/papers/arXiv_2610.00250v1_Du_Guo_Kusakabe_Xie_src/v5oka_maps_modifications_deformations.tex'
ps=primary.read_text();a2=ps.index(r'\label{eq:cusp-decomposition}');b2=ps.index('We recall the toric notation',a2)
supp={'created_utc':now,'scope':'Primary facts and receiving definitions only; no target P5.7 proof or parameter-map conclusion.','receiving_intro_adoption_and_definitions':s[a:b],'AC_primary':{'pdf':str(O/'literature/S6_SERIES_PUBLISH_I_AC26_primary.pdf'),'sha256':'283bba102dd1d5dc346af81b28145bdaaea6654398d5032e76e97bafb9a858f2','locator':'Definition3.1p14 and Theorem3.4(i)–(iii)pp14–15','images':[str(O/'literature/S6_SERIES_PUBLISH_I_AC26_p014.png'),str(O/'literature/S6_SERIES_PUBLISH_I_AC26_p015.png')],'facts':'Theorem3.4(i) uniquely specifies tau by j(tau)=1728t and the two generator laws. Theorem3.4(ii) uniquely specifies mu by its affine laws and boundedness on the distinguished g0-invariant cusp component U_r. Theorem3.4(iii) makes the holomorphic beta solutions with the affine laws and beta+tau bounded on that same component a nonempty affine line under constants; beta+tau descends and extends holomorphically at the cusp. These are primary input assertions, not a receiving-paper comparison derivation.'},'DGKX_primary_adoption':'The proof of Proposition period-data-existence, attached source lines681–715, explicitly applies AC Theorem3.4(i)–(v) in the ordered (gammahat,uhat,what,deltahat) basis, names the unique-up-to-constant beta0 solution, and prints the generator laws.','DGKX_primary_cusp_excerpt':ps[a2:b2],'no_new_check_event':True}
supppath=O/'S6_SERIES_PUBLISH_I_nightP57_fresh_primary_supplement.json';supppath.write_text(json.dumps(supp,ensure_ascii=False,indent=2)+'\n')
guard=O/'S6_SERIES_PUBLISH_I_boundary_program_guards.json'
print(json.dumps({'events':str(out),'rows':9,'group':group,'guard_sha256':hashlib.sha256(guard.read_bytes()).hexdigest(),'supplement':str(supppath)}))

