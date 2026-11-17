"""Record the actual complete reading of PUSH E5 and its original inputs."""
from pathlib import Path
import json,hashlib,re
D=Path(__file__).resolve().parents[2];R=D.parent
src=R/'sources/papers/arXiv_2609.33785_Viaclovsky_two_parameter_src/Viaclovsky_S6_September_26_2026.tex'
proof=D/'work/root/push_E5_for_II.tex';s=proof.read_text()
source_record={'keys':['ViaclovskyTwo2026','Viaclovsky2026Two','VTwo26','ViaTwo26push'],
 'source':str(src.relative_to(R)),'sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
 'locator':'Theorem1.1 and fibre table, lines238–283; Proposition4.2 and full proof, lines873–941; Proposition6.1 and full proof, lines1339–1400; Proposition6.4 and full proof, lines1495–1607. Lemma2.1 and Proposition3.1 were previously opened at the retained exact scopes.',
 'verification':'Read every displayed matrix and its geometric determination: d^2=1 follows from the coefficient-one primitive hexagonal periods. Matched ordinary dual homology and all four local types. Read the full canonical-form descent, actual simultaneous line bundle/linearization and root comparison, compact uniform contraction, marked torsion section, proper smooth bidisc, cross-ratio derivative and independent elliptic invariant. The source proves dimension two, not the logarithmic c modulo2Z classification. The latter is independently proved in PUSH E5.3 with all norm and collar conditions.',
 'status':'verified in the specified scope','reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026'}
p=D/'work/root/references_verified.json';refs=json.loads(p.read_text())
if source_record not in refs:refs.append(source_record)
p.write_text(json.dumps(refs,indent=2,ensure_ascii=False)+'\n')
scopes={
 'E.5.1':'Full proof re-derived: inverse coordinate rescaling gives orders(3,6,9), finite discriminant has three simple roots, local period valuations and independent nilpotent ranks are(1,1,2). The false three-rank-one assertion belongs to the input question, not to Viaclovsky.',
 'E.5.2':'Full integral proof re-derived: exact four cohomology matrices and their ordinary inverse-transpose duals; products/order/nilpotence; rational centralizer dimension2; fixed lattice and integral norm columns; all primitive images and integral kernels. The retained exact rerun checks every row reduction, Smith/Hermite form and covariance formula.',
 'E.5.3':'Full proof read and re-derived: uniform contraction on a smaller closed mu-disc and half-plane lift; proper root/rank-one/hexagonal family; anticanonical pencil; cross-ratio derivative and exclusion of rank-one interchange; integral centralizer; order-four norm forcing alpha=1 and even h; actual root and three nodal defects; exact sphere relation; holomorphic remainder conditions; weighted P(1,4) determinant and Laurent H1 calculation; vanishing of the analytic translation torsor; both inverse extensions; injectivity on a single-logarithm bidisc.'}
rows=[]
for sid,scope in scopes.items():
 rows.append({'source_run':'S6_02_PUSH','source_id':sid,'paper':'II','printed_label':'push:src:'+sid,
  'your_check':'GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November 2026, root independent current reading: '+scope,
  'check_outcome':'Passed complete proof and opened-source hypothesis checks; retained exact computation passed.',
  'source_sha256':hashlib.sha256(s.encode()).hexdigest(),
  'audit_notes':'Source-to-print: labels/references/citations normalized; the question-only false configuration is explicitly described. No proof step omitted. Actual rerun: code/push/rerun_manifest.json, e_push_two_parameter.py; full output code/push/logs/e_push_two_parameter.py.txt.'})
(D/'work/root/II_push_E5_full_checks.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n')
sources={'AC26':R/'sources/original/AC26_transcription.tex','E26':R/'sources/papers/arXiv_2609.38442_Engel_src/S6.tex','DGKXv1':R/'sources/papers/arXiv_2610.00250v1_Du_Guo_Kusakabe_Xie_src/v5oka_maps_modifications_deformations.tex','DGKXv2':R/'sources/papers/arXiv_2610.00250v2_Du_Guo_Kusakabe_Xie_src/submited-tams.tex'}
terms=['two-parameter','two parameter','Viaclovsky','III^*','rank-one','cross-ratio']
search=[]
for key,p in sources.items():
 t=p.read_text();search.append({'source':key,'path':str(p.relative_to(R)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'hits':{a:[t[:m.start()].count('\n')+1 for m in re.finditer(re.escape(a),t,re.I)] for a in terms},'scope':'Text locators only; prior opened original AC26 PDF sections2–7 and9–10 control its meaning. No absence inferred from search alone.'})
credits=[]
for sid in scopes:
 credits.append({'source_run':'S6_02_PUSH','source_id':sid,
  'found_in_AC26':'No matching four-fibre theorem in the opened construction/classification scopes, Sections2–7 and9–10. The monodromy, root and cusp construction inputs remain credited. Specific text searches and hit ranges: II_push_E5_source_search.json.',
  'found_in_E26':'No matching four-fibre assertion in the opened construction and Remarks8.1–8.4; two-parameter, Viaclovsky, rank-one and cross-ratio queries in the full supplied text have no such hits. This is a scoped comparison.',
  'found_in_DGKX_v1':'The standard-family Theorem1.4 and Sections6–7 concern different finite multiplicities. No matching four-fibre assertion found in the checked scope. Version2 mentions the Viaclovsky construction as an Oka-property example; it does not supply the present marked logarithmic classification.',
  'found_elsewhere':'Viaclovsky two-parameter paper Theorem1.1, Proposition4.2 and Proposition6.4: actual fibre types, input monodromy and independent two-parameter variation. Full proofs and hypotheses opened. The source does not state classification modulo2Z on the logarithmic lift.',
  'credited_to':{'E.5.1':'Viaclovsky, two-parameter paper, Theorem1.1 and Proposition3.1; correction of the input question only.','E.5.2':'Viaclovsky, two-parameter paper, Proposition4.2 supplies the monodromy matrices; the full centralizer/fixed/norm calculation is retained.','E.5.3':'Viaclovsky, two-parameter paper, Proposition6.4 supplies the local family and independent variation; Proposition6.1 supplies the intrinsic pencil. The integer logarithmic classification has the additional complete norm-and-collar proof printed here.'}[sid]})
(D/'work/root/II_push_E5_source_search.json').write_text(json.dumps(search,indent=2)+'\n')
(D/'work/root/II_push_E5_credit_comparison.json').write_text(json.dumps(credits,indent=2,ensure_ascii=False)+'\n')
print('Recorded full proof and exact source checks for all three PUSH E5 rows.')
