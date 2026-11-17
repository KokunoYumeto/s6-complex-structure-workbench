"""Bounded, reproducible attached-literature searches for the sixty own III rows."""
from pathlib import Path
import json,re,hashlib
R=Path(__file__).resolve().parents[3];W=R/'deliverables/work/maps_audit'
groups={
 'bubble':(['A.2.2'],[r'bubbl',r'homotop',r'\\pi_?\{?6',r'local modification']),
 'framing':(['B.1.1','B.1.2'],[r'fram',r'Adams',r'Pontryagin',r'\\eta',r'e.invariant']),
 'null_and_cone':(['B.2.1','B.3.2','B.3.3'],[r'null[ -]?homotop',r'homotopically trivial',r'Hopf',r'cofib',r'wedge',r'\\vee']),
 'retained_angle':(['B.3.1'],[r'Arf',r'Pontryagin',r'retained.angle',r'framed.*torus',r'\\eta_?\{?4']),
 'named_families':(['B.4.1'],[r'circle quotient',r'quotient.*circle',r'map.*S\^\{?3',r'Hopf',r'null[ -]?homotop']),
 'cw':(['B.5.1','B.5.2'],[r'mapping[ -]?cylinder',r'\bCW\b',r'cell.*structure',r'tubular',r'homotopy sphere',r'homology sphere']),
 'theta7':(['B.6.1','B.6.2','B.6.21','B.6.24','B.6.25'],[r'smooth monodromy',r'Theta_?\{?7',r'Eells',r'mapping.class',r'Krylov',r'isotop']),
 'smoothing':(['B.6.3','B.6.4','B.6.5','B.6.6'],[r'conifold',r'smooth.*monodromy',r'mapping.tor',r'Torelli',r'Pontryagin',r'Eells']),
 'affine_defect':(['B.6.7','B.6.8'],[r'scalar.shear',r'affine.defect',r'order.six',r'order.6',r'even.shift',r'shear']),
 'spin_c':(['B.6.9','B.6.15','B.6.19'],[r'spin.?c',r'Eells',r'Kuiper',r'free.circle',r'coboundary',r'cobordis']),
 'cover_height':(['B.6.10','B.6.11'],[r'genus.three',r'genus.3',r'height',r'cyclic.cover',r'conductor',r'signature']),
 'norm_torsor':(['B.6.12','B.6.13','B.6.14'],[r'Mordell',r'torsor',r'cyclic.norm',r'conductor',r'genus.one',r'order.two']),
 'fixed_conifold':(['B.6.16','B.6.17','B.6.18','B.6.20','B.6.22','B.6.23'],[r'fixed.circle',r'free.circle',r'Dehn.twist',r'conifold',r'Euler.cube',r'Pontryagin']),
 'kummer':(['C.1.1','C.1.2','C.1.3','C.1.4','C.1.5'],[r'Kummer',r'power.map',r'isogen',r'finite.flat',r'finite.cover',r'cocharacter']),
 'fourfold':(['E.1.1','E.1.2','E.1.3','E.1.5'],[r'fourfold',r'Kuhn',r'eight.dimensional',r'rank.three',r'fibre.product',r'fiber.product']),
 'kuhn_euler':(['F.1.1'],[r'Kuhn',r'tetrahedr',r'n!d',r'n!.*Euler',r'Euler.*n!']),
 'characteristic':(['F.1.2','F.1.3','F.4.1'],[r'quaternion',r'HP\^',r'characteristic.vector',r'Theta_?\{?8',r'inertia',r'c_?\{?2\}?\^2']),
 'linear_obstruction':(['F.1.4','F.2.1'],[r'eigenvalue.one',r'eigenvalue.1',r'free.affine',r'square.zero',r'index.one',r'centralizer']),
 'nonselfdual':(['F.2.5','F.2.6'],[r'non.self.dual',r'three.connected',r'3.connected',r'fourfold',r'Kuhn',r'torsion.*transgress']),
 'polarized_obstruction':(['F.3.4'],[r'polariz',r'polaris',r'semisimpl',r'abelian.surface',r'fixed.part']),
 'explicit_periods':(['F.3.5','F.3.6','F.3.7'],[r'genus.two',r'genus.2',r'exterior.square',r'non.self.dual',r'x\^5',r'rank.six']),
 'oka_periods':(['F.3.8','F.3.9','F.3.10','F.3.11'],[r'LSAP',r'spanning.tube',r'Oka.?1',r'Grassmann',r'period.domain',r'bounded.correction'])
}
base={
 'AC26':'sources/external/maps_audit/AC26_original_search.txt',
 'E26':'sources/papers/arXiv_2609.38442_Engel_src/S6.tex',
 'DGKX_v1':'sources/papers/arXiv_2610.00250v1_Du_Guo_Kusakabe_Xie.tex',
 'DGKX_v2':'sources/papers/arXiv_2610.00250v2_Du_Guo_Kusakabe_Xie.tex'}
old=json.loads((W/'fourfold_priority_credit_search.json').read_text())
sources=[dict(baseline=k,source=p) for k,p in base.items()]
seen={hashlib.sha256((R/p).read_bytes()).hexdigest() for p in base.values()}
for r in old:
 if r['baseline']!='elsewhere':continue
 h=hashlib.sha256((R/r['source']).read_bytes()).hexdigest()
 if h in seen:continue
 sources.append(dict(baseline='elsewhere',source=r['source']));seen.add(h)
logs=[];idx=[]
for group,(ids,queries) in groups.items():
 refs=[]
 for si,source in enumerate(sources):
  p=R/source['source'];text=p.read_text(errors='replace');lines=text.splitlines();hits=[]
  patterns=[re.compile(q,re.I) for q in queries]
  for n,line in enumerate(lines,1):
   found=[queries[j] for j,rx in enumerate(patterns) if rx.search(line)]
   if found:
    hits.append(dict(line=n,queries=found,context='\n'.join(lines[max(0,n-2):min(len(lines),n+1)])))
  sid=f'maps60:{group}:{source["baseline"]}:{si}';refs.append(sid)
  logs.append(dict(search_id=sid,group=group,results=ids,**source,source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),
   queries=queries,search_mode='case-insensitive Python regular expressions, complete attached source file, linewise; exact queries retained',hits=hits,hit_count=len(hits),
   original_control='sources/original/AC26_original_manuscript.pdf' if source['baseline']=='AC26' else source['source'],
   scope='Bounded discovery search, not a whole-source reading or worldwide absence claim. Positive matches and their actual inspected mathematical scope are classified in the per-result matrix.'))
 for sid in ids:idx.append(dict(source_id=sid,group=group,queries=queries,search_ids=refs))
targets=[r['source_id'] for r in json.loads((R/'deliverables/work/root/III_remaining_run_credit_targets.json').read_text()) if r['source_run']=='S6_04_MAPS_MANIFOLDS']
assert sorted(targets)==sorted(r['source_id'] for r in idx)
(W/'maps60_credit_search_log.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2)+'\n')
(W/'maps60_credit_search_index.json').write_text(json.dumps(idx,ensure_ascii=False,indent=2)+'\n')
print('Rows',len(idx),'source files',len(sources),'actual complete-file searches',len(logs))
for group in groups:
 print(group,{r['baseline']:r['hit_count'] for r in logs if r['group']==group and r['baseline']!='elsewhere'})
