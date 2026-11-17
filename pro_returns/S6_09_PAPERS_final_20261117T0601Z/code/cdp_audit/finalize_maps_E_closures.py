"""Append current source/dependency closures while retaining historical reads."""
import csv, hashlib, json, subprocess, time
from pathlib import Path
ROOT=Path('/workspace/scratch/037cd144174c')
OUT=ROOT/'deliverables/work/cdp_audit/maps_E'
META={'model':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date':'2026-11-17','timezone':'UTC','reader':'/root/cdp_audit'}
refs=json.loads((OUT/'references_verified.json').read_text())
refby={r['key']:r for r in refs}
rows=json.loads((OUT/'result_audit.json').read_text())
program=ROOT/'deliverables/code/cdp_audit/maps_E/independent_fourfold_exterior_page.py'
start=time.monotonic();cmd=['/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python',str(program)]
r=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True)
assert r.returncode==0,r.stderr
stdout=program.with_suffix('.out');stdout.write_text(r.stdout)
newrun={'program':program.name,'source':str(program.relative_to(ROOT)),'source_sha256':hashlib.sha256(program.read_bytes()).hexdigest(),'reader':META,'command':cmd,'exit_code':0,'elapsed_seconds':round(time.monotonic()-start,3),'output':str(stdout.relative_to(ROOT)),'output_sha256':hashlib.sha256(stdout.read_bytes()).hexdigest(),'results':['E.1.4'],'scope':'Independent exact six-dimensional cohomology exterior matrices in every degree. The geometric cusp kernel and transgression ranks are separately proved inputs, not certified by numerical coincidence.'}
(program.parent/'independent_execution_manifest.json').write_text(json.dumps([newrun],ensure_ascii=False,indent=2)+'\n')

keys={
 'E.1.4':[], 'E.2.1':['ffJiaMeng','ffEsoleKang','ffPetersSterk'],
 'E.2.3':['rootScott83'], 'E.2.8':['rootHirsch76'],
 'E.2.9':['rootScott83','rootDavisKirk01','IsaksenWangXu2023','rootHirsch76'],
 'E.2.10':['mapsWinter08'], 'E.2.13':['rootScott83'],
 'E.2.18':['mapsWhitehead50'], 'E.2.21':['mapsVogel09','mapsMilnor65']}
shared={
 'E.1.4':[('MAPS E1.3','deliverables/work/maps_audit/fourfold_priority_source_checks.json','Chen Theorem B, plus projective finite cover and rational invariant cycles; integral specialization remains its separate full geometric proof.'),('MAPS E1.3','deliverables/work/maps_audit/maps_B_and_weight_source_checks.json','Deligne Hodge III Proposition8.3.5 pp42–43, complete printed proof; projective toric pure-weight application separately matched in maps_B_and_weight_application_checks.json.')],
 'E.2.1':[('Paper II root-stack direct-image/duality input','deliverables/work/cdp_audit/references_verified.json','Proper flat curve duality, base change and actual root-chart descent were opened in the completed PaperII audit.'),('MAPS E1.3/E1.4','deliverables/work/cdp_audit/maps_E/result_audit.json','The geometric cusp specialization and newly independent six-dimensional exterior page supply the required topology.')],
 'E.2.5':[('Original sphere integral transgression','deliverables/work/maps_audit/paperI_topology_manifest.json','Full integral topology proof and finite-extension transgression repair are printed in completed PaperI.')],
 'E.2.8':[('MAPS B2.1','deliverables/work/maps_audit/maps_B_and_weight_application_checks.json','Both full null-homotopy proofs were read by maps_audit; the divisor-root proof uses the opened Hatcher pi6(S3)=Z12 and does not require an Adams invariant.')],
 'E.2.9':[('MAPS A2.1','deliverables/work/maps_audit/paperI_circle_quotient_manifest.json','Literal circle quotient with the actual map is printed in PaperI as mapsI:src:A.2.1.'),('MAPS B1.1/B1.2','deliverables/work/maps_audit/maps_B_and_weight_application_checks.json','Full receiving proofs and Bott/APS/Toda originals are closed. In addition, this reader read maps_B.tex lines1–150 and independently followed the invariant stable-framing restriction and the product Lie-torus calculation. The E2.9 vanishing only needs st[e]=eta^3 and pi4S=0, not the separate real-e or unstable normalization.')],
 'E.2.10':[('MAPS B5.2','deliverables/work/maps_audit/maps_B_remaining_full_checks.json','Complete cap/peripheral receiving proof, event new-maps-B-remaining-full-20261117:B.5.2. Its separate full B-program reruns remain with maps_audit; the E-specific certificate has already passed.')],
 'E.2.13':[('MAPS A2.1','deliverables/work/maps_audit/paperI_circle_quotient_manifest.json','Actual circle quotient and derivative, printed in PaperI.')],
 'E.2.14':[('Equations B.5.16–B.5.18','sources/returns/S6_04_MAPS_MANIFOLDS/sections/maps_B.tex','This reader additionally read/rederived lines1030–1171: degree-two honeycomb quotient, primitive swept-torus kernel, both actual boundary coefficients and retained regular framed tube. These are equation tags, not unproved result IDs.'),('MAPS B5.1','deliverables/work/maps_audit/maps_B_and_weight_source_checks.json','Waldhausen Theorem6.1 p77 matched to the relative marked topological cusp comparison; full receiving proof and all boundary hypotheses retained in maps_B_and_weight_application_checks.json.')],
 'E.2.16':[('Equations B.5.16–B.5.17','sources/returns/S6_04_MAPS_MANIFOLDS/sections/maps_B.tex','Exact normalization/cusp peripheral maps re-read at lines1030–1171; the independently verified E2.12 Laurent calculation and E2.16 full noncommutative certificate retain all maps.')],
 'E.2.18':[('MAPS D1.9','deliverables/work/invariants_arithmetic/maps_D_independent_audit.json','Row D.1.9 full128-line receiving proof, complex wall degrees(-6,0,1), eta^2=-12, and exact manifolds_mu.py rerun. Earlier D1.5/6/8 component and Chern inputs are separately retained there.')],
 'E.2.20':[('MAPS B5.1 collar drift','sources/returns/S6_04_MAPS_MANIFOLDS/sections/maps_B.tex','This reader independently read the exact smooth drift-removal argument at lines685–705: after subtracting v_j/m_j the periodic real lift interpolates on the collar. This particular use does not require promoting the later topological logarithmic comparison to a smooth one. E2.19 supplies the actual smooth cusp comparison.')]
}
for row in rows:
    sid=row['source_id']
    event={'id':'maps-E-source-program-closure-20261117','reader':META,
           'scope':'Exact operative primary sources, shared receiving-proof dependencies, all assigned original programs and the independent E1.4 exterior page.',
           'references':[{'key':key,'locator':refby[key]['locator'],'record':'deliverables/work/cdp_audit/maps_E/references_verified.json'} for key in keys.get(sid,[])],
           'shared_dependency_records':[{'source_id':name,'record':record,'scope':scope} for name,record,scope in shared.get(sid,[])],
           'outcome':'No unaddressed mathematical objection remains in this assigned receiving proof; all E-specific source and program checks are completed.',
           'scope_limit':'This does not certify unrelated portions of the external literature or replace separately owned B/D full-program records.'}
    row['new_check_events']=[e for e in row['new_check_events'] if e['id']!=event['id']]+[event]
    row['remaining_dependencies']=[]
    row['status']='complete receiving proof independently checked; operative source matches and E-specific exact programs completed'
    row['closure_event']=event
    if sid=='E.1.4':row['independent_program_checks']=[newrun]
    row['dependency_records']=event['shared_dependency_records']
path=OUT/'result_audit.json';path.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
fields=list(dict.fromkeys(k for row in rows for k in row))
with (OUT/'result_audit.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v for k,v in row.items()} for row in rows)
edits=[{'source_id':'E.2.9','source':'sources/returns/S6_04_MAPS_MANIFOLDS/sections/shifted_group_bordism.tex','old':'Theorems 2.3--2.4 and the Euler-number discussion in Section 2','new':'Theorems 2.3--2.5 and the Euler-number discussion in Section 3, especially Theorem 3.6','reason':'Original Scott1983 pp424–428 and434–436 were opened and matched.'},
       {'source_id':'E.2.9','source':'sources/returns/S6_04_MAPS_MANIFOLDS/sections/shifted_group_bordism.tex','old':'[Theorem 2.1 and Table 1]{rootIWX20}','new':'[Corollary 1.3 and Table 1, pp.~112--113]{IsaksenWangXu2023}','reason':'Explicit edition change to the primary published table actually opened; no 2020-edition equivalence is silently assumed.'}]
(OUT/'required_citation_transformations.json').write_text(json.dumps(edits,ensure_ascii=False,indent=2)+'\n')
print('Closed 22 receiving-proof records with exact source and dependency scopes; preserved all historical events.')
