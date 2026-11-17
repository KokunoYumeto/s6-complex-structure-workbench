#!/usr/bin/env python3
"""Record six independent receiving-proof checks; do not rerun root-owned jobs."""
from pathlib import Path
import csv, hashlib, json, re

ROOT=Path(__file__).resolve().parents[3]
WORK=ROOT/'deliverables/work/invariants_arithmetic'
SRC=ROOT/'sources/returns/S6_04_MAPS_MANIFOLDS'
META=dict(checker='GPT-6 Astra (OpenAI, ChatGPT Pro mode)',effort='Pro',date='2026-11-17 UTC')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(n,x): (WORK/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')

ao=dict(**META,citation_key='ffAchingerOgus20',author='Piotr Achinger and Arthur Ogus',
 title='Monodromy and log geometry',year=2020,journal='Tunisian Journal of Mathematics',volume='2',issue='3',pages='455–534',
 doi='10.2140/tunis.2020.2.455',url='https://msp.org/tunis/2020/2-3/tunis-v2-n3-p01-p.pdf',
 local_source='sources/audit_cache/inv_ari/maps_literature/Achinger_Ogus_2020.pdf',
 source_sha256='c650c81b537d94b6d9113c4dd7e07e57853eb1aed760b558db0fb516979988b1',
 status='verified_for_stated_use',verified=True,
 opened_locator='Published original §3.1 p474 (verticality); Theorem4.1.1 p480, Lemmas4.1.2–3 and complete proof pp481–482. Original printed pp480–481 visually checked; text lines1110–1145 and1400–1535 read in full.',
 actual_use='The semistable Kuhn cap and boundary inclusion are modelled by the logarithmic-collapse mapping cylinder.',
 hypotheses_and_normalization_check='Fine saturated log analytic spaces; proper, log smooth, vertical over a log disc. The monomial chart N→N^(k+1),1↦(1,...,1), has these properties. Exactness is automatic over that base. The theorem gives a noncanonical homeomorphism; its proof fixes the logarithmic central fibre. The selected radial identification and the explicit cusp marking are retained.',
 extent='Operative statement, definitions and complete proof opened. This is not a claim to have independently reproved the cited log-fibration theorem of Nakayama–Ogus or all80 pages.',
 web_refs=['turn310search12','turn312search6','turn312search7','turn314view1','turn316view1'],
 version_note='The author2018 preprint was also opened: Proposition4.1.1 pp25–26 assumes exactness explicitly. The published2020 theorem and original publisher PDF govern this check.')
assert sha(ROOT/ao['local_source'])==ao['source_sha256']
dump('maps_F_references_verified.json',[ao])
(WORK/'maps_F_checked_references.bib').write_text('''@article{ffAchingerOgus20,
  author = {Achinger, Piotr and Ogus, Arthur},
  title = {Monodromy and log geometry},
  journal = {Tunisian Journal of Mathematics},
  volume = {2}, number = {3}, pages = {455--534}, year = {2020},
  doi = {10.2140/tunis.2020.2.455},
  url = {https://msp.org/tunis/2020/2-3/tunis-v2-n3-p01-p.pdf},
  note = {Verified original: Theorem 4.1.1 and complete proof, pp. 480--482; precise use is the logarithmic mapping-cylinder model}
}
''')

spec={
33:('fourfolds_cap_chains.tex',3,162),34:('fourfolds_cap_chains.tex',163,305),
35:('fourfolds_global_chains.tex',1,344),37:('fourfolds_tuple_classification.tex',1,145),
38:('fourfolds_involution_classes.tex',1,169),39:('fourfolds_classification_synthesis.tex',1,133)}
details={
33:'Read the complete statement, entire recursive proof and every implementation/scope paragraph. Independently verified the Laurent Koszul contraction in all signs, the recursive bar comparison and its side identities, and the strict orbit-groupoid action including nonfixed numerators and integer offsets. The groupoid orbit has m distinct objects by freeness; its strict mth action is identity because the integral power offset cancels at both endpoints. Re-derived both finite homological perturbation series: the first lowers group degree at each step, and every higher term followed by the periodic homotopy lowers it again. Supplied explicit all-degree inclusion and carry-formula projection for the cyclic periodic resolution, with pi=1 and ph=hi=h²=0. Checked radial retraction, equivariant projection from the boundary action diag(1,M), transfer of its map, and the mapping cone. The finite degree prefixes and2^r/2^(r+1) bounds follow from the displayed basis. No equivariant replacement by homology is made without the retained corrections.',
34:'Read the complete theorem, all toric/logarithmic geometry, the full diagram and every chain-comparison step. Checked that the translated face category retains multiple incidences; Q_sigma R_tau composes because the smaller face lattice is killed, and the shear diagrams compose additively. Since normalized tau contains0, the translation label w is a vertex of sigma, so Q_sigma w=0 proves naturality of the collapse. Re-derived the angular quotient and boundary shear from the unimodular monomial charts, and the primitive cusp group relation with its sign. Opened the exact published Achinger–Ogus theorem and full proof, including the explicit noncanonical-trivialization caveat; matched every hypothesis. The finite simplicial replacement has flag length≤3, so its transferred chains and full collapse map terminate after at most four terms. Unit cancellation is integral and preserves the cone. Read root’s complete fresh Kuhn output: all matrices, ranks,2063/4988/7087 cancellations and the unique order-two boundary torsion agree. Independently checked Poincare–Lefschetz ranks and Euler6 as consequences, not replacements for the integral matrix calculation.',
35:'Read all344 source lines, including every map formula and the three complete integration reports. Re-derived the signed Fox contraction and semidirect Alexander–Whitney map; in degree2 the mixed term exactly cancels the difference between y and M(w)y. The inverse matrices act on the right, with rho(wu)=rho(u)rho(w), so the noncommuting horizontal differential squares to zero. Checked the natural-transformation prism including integer offsets, tau=g^-1 x^a, its complement value−e+M^-1a, and recovery of the positive root as+e. The mth relation retains the full integral affine numerator. Verified the optional bounded mapping-torus cap only under its unimodular normal-form hypothesis. Re-derived c=(s1...sk)^-1 x^-kappa and the exact cusp shuffle identity; filling gives precisely s1...sk x^kappa=1. Asphericity fixes the marked homotopy class of each boundary map. The Mayer–Vietoris cone is the homotopy-pushout chain model. Recomputed the rank expression and finite prefix bound, and read root’s completed fresh survivor output through every boundary degree and final Smith groups. No saturation or spectral-sequence extension is substituted. Root owns the remaining exact integration executions.',
37:'Read the whole145-line source, including implementation and marking transport beyond the extracted theorem proof. Re-derived free affine lift existence from a primitive fixed vector and translationu/d²; every prime stabilizer subgroup is a nontrivial pure translation. Enumerated the permitted cyclotomic degree budgets≤5 beside the fixed vector, giving exactly1,2,3,4,5,6,8,10,12 as linear orders. The height/lexicographic well-order gives a per-input finite box containing its own least conjugacy representative, conditional only on the separately proved F2.36 decision procedure. Characteristic polynomial and order rejections preserve every equivalent tuple. Identity insertion and the involution branch are conjugacy-invariant sectors, so their separate canonical choices are consistent. The unbounded trace argument rules out a fixed finite box. The general height-box branch is proved terminating but is explicitly not claimed executed. Affine vectors, clutch and cusp marking are all transported by the same returned conjugator.',
38:'Read all169 source lines and independently re-derived the full integral classification. The primitive cusp basis gives M1=[A,B;0,−A], M2=[A,B−A;0,−A], A²=1 and AB=BA. The integral involution lattice is recovered from primitive plus/minus eigensublattices and a binary graph of glue, giving exactly six types in rank3. Computed every mixed and swap norm block integrally; the quotient is Mat_p(F2)⊕Mat_q(F2), with no saturated substitute. Its algebra quotient shows that the centralizer action is exactly independent similarity. Re-derived the Hadamard determinant bound for binary3×3 lifts and the final full integral norm equation, including the sign of shear conjugation. The finite-field orbit counts1,2,6,14 give14+12+12+14+2+2=56. The fixed vectors yield free order-four affine lifts, while all possible actual orders are even, so the cyclic orbifold quotient obstructs simple connectivity. Root’s completed output independently supplies112 exact conjugators and112 free affine actions; no new run is claimed by this reader.',
39:'Read all133 source lines, including the unified-driver tests and nonzero order-one numerator example. Checked the synthesis against each operative predecessor rather than treating it as an additional classification theorem. The conjugator sends every matrix, numerator, clutch and supplied cusp marking by the same integral map; (RP)^-1(Rx)=P^-1x gives identical marked toric charts. Thus the claimed comparison is an actual diffeomorphism of the fully marked gluing. Re-derived deletion of an actual order-one site: moving x^vi across the suffix adds (M_(i+1)...M_k)^-1 vi to kappa. At most one such site is possible. The group and chain algorithms therefore cover every stated genuine two- or three-point datum. The survivor implication retains all of F2.7–30 and F4.1, whose receiving checks belong to root/maps. Complete effective per-input classification is distinguished from an unexecuted infinite global table and from the enormous noninvolution fallback.'}
deps={33:['F.2.31'],34:['F.2.33','ffAchingerOgus20','fixed primitive Kuhn toric construction'],
35:['F.2.31','F.2.33','F.2.34'],37:['F.2.16','F.2.36','F.2.38'],
38:['F.2.1','F.2.31'],39:['F.2.7–30','F.2.31','F.2.33–38','F.4.1']}

# Only completed root outputs actually opened by this receiving reader enter here.
root_manifests=[]
for n in ['execution_manifest.json','cli_execution_manifest.json']:
 p=ROOT/'deliverables/code/root_maps_F'/n
 for rec in json.loads(p.read_text()):
  rec={**rec,'execution_manifest':'code/root_maps_F/'+n}
  root_manifests.append(rec)
outputs={
33:['fourfolds_bar_koszul.py.rerun.txt','fourfolds_affine_cap_chains.py.rerun.txt'],
34:['fourfolds_kuhn_cap_chains.py.rerun.txt'],
35:['fourfolds_global_chains.py.rerun.txt','fourfolds_peripheral_signs.py.rerun.txt','cli_05_fourfolds_total_homology.py_--fresh.rerun.txt'],
37:['cli_03_test_fourfolds_tuple_classification.py.rerun.txt'],
38:['cli_02_fourfolds_involution_classes.py.rerun.txt'],39:[]}
prior_paths=[SRC/'records/root_audit_checkpoint08_progress.json',SRC/'records/root_audit_checkpoint09_progress.json',SRC/'records/root_f2_completion_audit.json']
prior_data=[json.loads(p.read_text()) for p in prior_paths]
rows=[]
outdir=WORK/'maps_F_receiving_extracted';outdir.mkdir(exist_ok=True)
for n,(name,lo,hi) in spec.items():
 path=SRC/'sections'/name
 text=''.join(path.read_text().splitlines(keepends=True)[lo-1:hi])
 target=outdir/f'F_2_{n}.tex';target.write_text(text)
 program=[]
 for out in outputs[n]:
  matching=[r for r in root_manifests if Path(r['output']).name==out]
  assert len(matching)==1,(out,matching)
  rec=matching[0];assert rec['exit_code']==0
  assert sha(ROOT/'deliverables'/rec['output'])==rec['output_sha256']
  program.append({**rec,'receiving_check':'Full recorded output opened and matched to its exact stated role; executed by root, not repeated by this reader.'})
 prior=[]
 for p,d in zip(prior_paths,prior_data):
  if n in [33,34,37,38] and 'checkpoint08' in p.name:
   key='F.2.33--34' if n in [33,34] else 'F.2.37--38'
   record=d['statements'][key];locator='/statements/'+key
  elif n in [35,39] and 'checkpoint09' in p.name:
   key='F.2.35;F.2.39';record=d['statements'][key];locator='/statements/'+key
  elif 'root_f2' in p.name:
   record={k:d[k] for k in ['root_proof_review','root_code_review','exact_scope','computational_limit','marking_limit']};locator='/root_proof_review,/root_code_review,/exact_scope,/computational_limit,/marking_limit'
  else:continue
  prior.append(dict(reviewer='GPT-6 Astra (OpenAI, ChatGPT Pro mode), source-run root',effort='Pro mode; no finer parameter recorded',date=d.get('recorded_utc',d.get('updated_utc')),source_file=str(p.relative_to(ROOT)),source_sha256=sha(p),locator=locator,scope=record,provenance='Within the15–16 November producing run; not human or external review.'))
 row=dict(**META,source_run='S6_04_MAPS_MANIFOLDS',source_id=f'F.2.{n}',printed_label=f'maps:F.2.{n}',paper='III',
  source_blocks=[dict(file=str(path.relative_to(ROOT)),start_line=lo,end_line=hi,sha256=hashlib.sha256(text.encode()).hexdigest())],
  complete_proof_file=str(target.relative_to(ROOT/'deliverables')),complete_proof_sha256=sha(target),
  own_check=dict(**META,proof_read='Whole statement, complete proof, and all ensuing implementation/scope/marking paragraphs',details=details[n],outcome='Complete independent receiving proof rederived; no mathematical gap found at the stated scope'),
  check_outcome='receiving proof verified; parent-owned numerical/dependency closure remains separately recorded',
  depends_on=deps[n],recorded_checks=prior,program_runs=program,
  unresolved_mathematical_claims=[],
  program_ownership='Root owns and is executing the remaining F commands; this reader has not duplicated them.',
  prerequisite_evidence=dict(root_full_proof_check='work/root/maps_F_proof_audit.md',root_BHJ_original_check='work/root/BHJ22_source_check.json' if n in [37,39] else None,logarithmic_cylinder='work/invariants_arithmetic/maps_F_references_verified.json' if n in [34,35,39] else None),
  source_candidate_comparison='Every source mathematical paragraph retained in the complete extracted copy; optional additions are separate and introduce no weaker hypotheses.')
 if n==33: row['optional_proof_addition']='work/invariants_arithmetic/maps_F_cyclic_bar_inclusion.tex'
 if n==34: row['optional_proof_addition']='work/invariants_arithmetic/maps_F_log_cylinder_scope.tex'
 if n in [37,39]: row['explicit_computational_limit']='The general noninvolution height-box algorithm is not claimed exhaustively executed; this is a proved finite algorithm, not a missing mathematical case.'
 rows.append(row)
dump('maps_F_receiving_audit.json',rows)
with (WORK/'maps_F_receiving_audit.csv').open('w',newline='') as f:
 cols=['source_id','printed_label','source_blocks','own_check','check_outcome','depends_on','recorded_checks','program_runs','prerequisite_evidence','optional_proof_addition','explicit_computational_limit']
 w=csv.DictWriter(f,fieldnames=cols);w.writeheader()
 for r in rows:w.writerow({k:json.dumps(r[k],ensure_ascii=False) if isinstance(r.get(k),(list,dict)) else r.get(k,'') for k in cols})
dump('maps_F_proof_insertions.json',[
 dict(source_id='F.2.33',source='sections/fourfolds_cap_chains.tex',insertion_file='work/invariants_arithmetic/maps_F_cyclic_bar_inclusion.tex',placement='After the periodic contraction/comparison paragraph (source lines111–126); before Borel/radial comparison',reason='Make the cyclic comparison inclusion and all-degree retraction identities explicit.'),
 dict(source_id='F.2.34',source='sections/fourfolds_cap_chains.tex',insertion_file='work/invariants_arithmetic/maps_F_log_cylinder_scope.tex',placement='After the logarithmic mapping-cylinder appeal, source lines238–250',reason='Match all published theorem hypotheses and retain its noncanonical radial marking.')])
print('Saved six complete receiving-proof records; original Achinger–Ogus source check; two optional full proof additions.')
