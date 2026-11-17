"""Perform actual per-result bounded searches for 39 carriers plus two inputs."""
import csv,hashlib,json,re,subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'deliverables/work/cdp_audit/carrier_credit';OUT.mkdir(parents=True,exist_ok=True)
META={'model':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date':'2026-11-17','timezone':'UTC','reader':'/root/cdp_audit'}
SOURCES={
 'AC26':'sources/external/root/AC26_pdf_text.txt',
 'E26':'sources/papers/arXiv_2609.38442_Engel_src/S6.tex',
 'DGKX_v1':'sources/papers/arXiv_2610.00250v1_Du_Guo_Kusakabe_Xie_src/v5oka_maps_modifications_deformations.tex',
 'DGKX_v2':'sources/papers/arXiv_2610.00250v2_Du_Guo_Kusakabe_Xie_src/submited-tams.tex'}
Q={
 'cusp-cover-extension-theorem':['Kummer','toric.*power','quasi.etale','finite.*flat','multiplication.by'],
 'cusp-cover-naive-action-failure':['Kummer','source.action','equivarian','N.th.root'],
 'cusp-cover-global-scope':['sublattice','unspool','Kummer','monodromy.*cover'],
 'cusp-spec-globalization-obstruction':['invariant.*covector','circle.*quotient','Seifert','systol','nonextension'],
 'cusp-cone-native-descent':['vanishing.*cycle','cusp.*quotient','invariant.*quotient','real.*torus'],
 'cusp-cone-S12-route':['S.?12','smash','suspension','cone.*torus'],
 'cusp-cone-S24-local-route':['S.?24','smash','suspension','circle.*quotient'],
 'cusp-cone-S24-route':['S.?24','smash','suspension','Seifert'],
 'cusp-cone-target-slice-embeddings':['slice','smash','radial.*quotient'],
 'cusp-cone-metric-scope':['ambient','intrinsic','systol','Gromov'],
 'cusp-cone-S12-almost-complex-obstruction':['Borel','Serre','almost.complex','S.?12'],
 'cusp-cone-obstructions':['rank.*quotient','finite.cover','almost.complex','S.?24','smash'],
 'cusp-cone-optimal-exponents':['systol','optimal','minimal.*cop','rank.*quotient'],
 'cusp-cone-angle-forgotten-sphere-carriers':['angle','smash','sphere.*carrier','quotient.*length'],
 'cusp-cone-S12-sphere-map-null':['smash','null.homotop','pi.*12','homotopy.*sphere'],
 'cusp-cone-S24-sphere-map-null':['smash','null.homotop','stable.*stem','fourth.*stem'],
 'cusp-cone-literal-R4-open-cells':['open.cell','moving','smash','Euclidean'],
 'cusp-cone-moving-S4-null-homotopy':['suspension','null.homotop','smash','moving.*sphere'],
 'cusp-cone-sphere-map-homotopy-status':['Hurewicz','null.homotop','smash','sphere.*map'],
 'cusp-cone-explicit-carriers':['cone.*tor','local.*homology','conical','smash'],
 'cusp-cone-target-homotopy-types':['suspension','wedge','Whitehead','smash'],
 'cusp-cone-exact-decompactification-space':['decompact','nonproper','non.quotient','Euclidean.*boundary'],
 'cusp-cone-sharp-global-R4-scope':['decompact','noncompact','Euclidean','quotient'],
 'cusp-s12-full-carrier-null':['smash','Barratt','Hilton','stable.*stem','null.homotop'],
 'cusp-s12-all-higher-smashes-null':['smash','suspension','null.homotop','stable.*stem'],
 'cusp-s12-one-copy-invariant':['Pontryagin','Thom','normal.*framing','stable.*stem','Toda'],
 'cusp-s12-nullity-scope':['smash','null.homotop','sphere.*quotient','conical'],
 'cusp-null:thm':['framed.*torus','nullbord','normal.*framing','Pontryagin','Thom'],
 'cusp_s12_carrier_homotopy:L567':['smash','null.homotop','peripheral','stable.*stem'],
 'G2-8':['orientation','octonion','almost.complex','homotop.*structure','structure.*homotop','SO.?6'],
 'carrier-real-periods':['inverse.transpose','realification','period.matrix','dual.lattice'],
 'carrier-native-quotient':['compact.quotient','real.quotient','vanishing.cycles','systol'],
 'sphere-metric-uniform-collapse':['fixed.metric','Hausdorff','diameter','radial.*slice'],
 'sphere-metric-fixed-realization':['cusp.adapted','length.metric','moving.base','ambient.*limit','rescal'],
 'sphere-metric-scaling-trichotomy':['trichotomy','rescal','unroll','ambient.*bubble','intrinsic'],
 'sphere-metric-unit-volume':['unit.volume','volume.normal','square.*torus','rescal'],
 'sphere-metric-tangent-scope':['tangent.cone','asymptotic.cone','local.homology','join','bubble'],
 'h24:ret:chart-lemma':['inverse.image','coordinate.chart','framed.*torus','regular.value','contractible'],
 'h24:ret:orientation-lemma':['normal.frame','orientation.sign','determinant.*frame','regular.value'],
 'h24:ret:framing-proposition':['Lie.fram','tangential.fram','normal.*fram','Pontryagin','Thom'],
 'h24:ret:q2-detected-quotient':['odd.multiple','detected.*quotient','retained.angle','Pontryagin','Thom']}
rows=json.loads((ROOT/'deliverables/work/cdp_audit/carrier_working_inventory_snapshot.json').read_text())
rows+=json.loads((ROOT/'deliverables/work/cdp_audit/carrier_prerequisite_inventory_2.json').read_text())
fixed=ROOT/'sources/overleaf_working_edition/supporting_materials/workbench/research/cusp_sphere_fixed_metric.tex'
ftext=fixed.read_text()
for match in re.finditer(r'\\begin\{(theorem|proposition|corollary)\}',ftext):
 end=ftext.index('\\end{'+match[1]+'}',match.end())+len('\\end{'+match[1]+'}')
 statement=ftext[match.start():end]
 sid=re.search(r'\\label\{([^}]+)\}',statement)[1]
 rows.append({'source_run':'working_edition','source_id':sid,'source_file':str(fixed.relative_to(ROOT)),
              'statement_as_printed':statement,'kind':match[1],
              'source_lines':[ftext[:match.start()].count('\n')+1,ftext[:end].count('\n')+1]})
retained_ids={'h24:ret:chart-lemma','h24:ret:orientation-lemma','h24:ret:framing-proposition','h24:ret:q2-detected-quotient'}
for row in csv.DictReader((ROOT/'deliverables/S6_09_PAPERS_inventory.csv').open()):
 if row['source_run']=='working_edition' and row['source_id'] in retained_ids:rows.append(row)
assert {r['source_id'] for r in rows}==set(Q)
searches=[];plan=[];union={k:{} for k in SOURCES}
for row in rows:
 sid=row['source_id'];term=Q[sid]
 receiving=row['source_file'].split(';',1)[0]
 if not (ROOT/receiving).exists():raise RuntimeError(receiving)
 src=ROOT/receiving
 plan.append({'source_run':row['source_run'],'source_id':sid,'source_file':receiving,
              'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
              'original_statement':row['statement_as_printed'],'queries':term})
 for baseline,rel in SOURCES.items():
  p=ROOT/rel;cmd=['rg','-n','-i','--no-heading']+sum((['-e',x] for x in term),[])+[str(p)]
  r=subprocess.run(cmd,text=True,capture_output=True)
  assert r.returncode in [0,1],r.stderr
  hits=[]
  for line in r.stdout.split('\n'):
   if not line:continue
   n,_,text=line.partition(':');n=int(n);hits.append({'line':n,'text':text});union[baseline][n]=text
  searches.append({'source_run':row['source_run'],'source_id':sid,'baseline':baseline,
     'source':rel,'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
     'command':['rg','-n','-i','--no-heading']+sum((['-e',x] for x in term),[])+[rel],
     'exit_code':r.returncode,'terms_searched':term,'matches':hits,'reader':META,
     'scope':'Entire named file searched with the exact expressions. Matching contexts and positive credit are assessed separately; a negative search is not a worldwide novelty conclusion.'})
for n,d in [('search_plan_41.json',plan),('searches_164.json',searches)]:
 (OUT/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
for k,ls in union.items():(OUT/(k+'_matched_lines.txt')).write_text('\n'.join(f'{i}: {s}' for i,s in sorted(ls.items()))+'\n')
print('Executed',len(searches),'queries for',len(rows),'rows; unique hit counts',{k:len(v) for k,v in union.items()})
