from pathlib import Path
import json,re,hashlib,collections
R=Path(__file__).resolve().parents[3];W=R/'deliverables/work/maps_audit'
units=json.loads((W/'III_course_retention_units.json').read_text());old=json.loads((W/'maps60_credit_search_log.json').read_text())
sources=[];seen=set()
for r in old:
 if r['source'] not in seen:sources.append({k:r[k] for k in ['source','source_sha256','baseline']});seen.add(r['source'])
loaded={r['source']:(R/r['source']).read_text(errors='replace').splitlines() for r in sources}
groups={
'framing':(r'Arf|Kervaire|stable fram|normal fram|framed bord|framing invariant',['the-original-six-dimensional-framing-invariant.md']),
'whitney':(r'Whitney|belt sphere|normal frame|Whitney disk|Whitney disc',['whitney-moves-in-the-receiving-dimensions.md','whitney-move-with-controlled-support.md','belt-sphere-complements-and-the-whitney-disk.md']),
'handles':(r'handle slide|handle chain|attaching sphere|belt sphere|handle decomposition|signed incidenc',['integral-handle-chains-and-signed-incidences.md','higher-index-framed-slides-and-chain-maps.md','framed-handle-slides-and-index-one-removal.md','rearranging-the-original-framed-handles.md','realizing-framed-handles-and-middle-cancellation.md']),
'morse':(r'Morse|cancelling handle|canceling handle|critical value|pseudogradient|pseudo.gradient',['morse-cancellation-with-controlled-support.md','morse-trajectories-and-critical-value-lowering.md','relative-morse-functions-and-original-handles.md','removing-the-original-zero-and-top-handles.md','creating-an-original-cancelling-handle-pair.md']),
'pt':(r'Pontr[jy]agin|Thom|framed bord|collapse map',['framed-manifolds-and-the-pontryagin-thom-map.md']),
'spin':(r'Spin\(?6|SU\(?4|clutch|Euler class|normal fram',['spin-six-and-the-framing-comparison.md']),
'stable':(r'Adams|cobar|cooperat|Milnor basis|stable stem|stable homotopy|completion map|derived limit',['the-original-integral-stable-group-and-its-completion-maps.md','the-original-adams-tower-and-arithmetic-completion.md','the-adams-tower-and-exact-inverse-limits.md','the-exact-characteristic-two-coordinate-calculation.md','the-original-projective-coordinate-and-actual-cooperations.md','the-actual-mod-two-cooperation-comparison-through-degree-eight.md','the-actual-mod-two-adams-resolution-and-cooperation-maps.md','the-degree-six-milnor-cobar-calculation.md','the-original-odd-prime-cooperations-and-degree-six-adams-calculation.md','coefficient-rings-and-the-original-degree-six-class.md']),
'duality':(r'Poincar|diagonal|Euler class|Thom class|compact.support|tubular',['manifold-duality-the-diagonal-and-wu-classes.source.txt','thom-euler-for-lesson11.md']),
'chern':(r'Chern|projective bundle|splitting principle|flag bundle|Thom',['integral-chern-classes-for-lesson11.md','projective-splitting-for-lesson11.md']),
'sphere':(r'Theta|homotopy sphere|smooth sphere|sphere recognition|h.cobordism',['integral-homology-and-sphere-recognition.md']),
'twist':(r'Dehn twist|Lagrangian sphere|symplectic transvection|sphere twist',['sphere-twists-and-the-original-smooth-six-sphere-comparison.md']),
'integrability':(r'Newlander|Nirenberg|Nijenhuis|octonion|Cayley|integrability|almost.complex',['almost-complex-structures-and-integrability.md'])}
byfile={f:(g,q) for g,(q,fs) in groups.items() for f in fs}
assert all(Path(u['source']).name in byfile for u in units)
rows=[]
for group,(q,files) in groups.items():
 rx=re.compile(q,re.I)
 for i,s in enumerate(sources):
  ls=loaded[s['source']];hits=[]
  for n,line in enumerate(ls):
   if rx.search(line):hits.append(dict(line=n+1,context='\n'.join(ls[max(0,n-1):min(len(ls),n+2)])))
  rows.append(dict(search_id=f'course249:{group}:{s["baseline"]}:{i}',group=group,chapter_files=files,queries=[q],hit_count=len(hits),hits=hits,search_scope='Complete attached file searched with the recorded case-insensitive regular expression; search is not a claim to have read every hit or every complete source proof.',**s))
# Exact per-unit title search in every baseline, separately from the broader thematic scan.
inv={}
for file in ['course_geometric_provider_inventory.json','course_characteristic_provider_inventory.json','course_duality_euler_provider_inventory.json','working_results_inventory.json']:
 for r in json.loads((W/file).read_text()):inv[r['source_id']]=r
ix=[]
for u in units:
 a=inv[u['source_id']];title=a.get('title',a.get('source_heading',a.get('statement','')));title=re.sub(r'^\s*(?:#+\s*)?\d+(?:\.\d+)*[.\s]*','',title);title=re.sub(r'\{#[^}]*\}','',title).strip();group,q=byfile[Path(u['source']).name]
 exact=[]
 if title:
  for i,s in enumerate(sources[:4]):
   hits=[dict(line=n+1,context=line) for n,line in enumerate(loaded[s['source']]) if title.casefold() in line.casefold()]
   e=dict(search_id=f'course249:unit:{u["source_id"]}:{s["baseline"]}',group=group,source_id=u['source_id'],queries=[title],hit_count=len(hits),hits=hits,search_scope='Complete attached file searched for the exact unit title, case-insensitively; supplementary localization only, not theorem-equivalence evidence.',**s);rows.append(e);exact.append(e['search_id'])
 ix.append(dict(source_id=u['source_id'],source=u['source'],source_unit_range=u['source_unit_range'],title=title,group=group,search_ids=[e['search_id'] for e in rows if e.get('group')==group and 'source_id' not in e]+exact))
(W/'course249_credit_search_log.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');(W/'course249_credit_search_index.json').write_text(json.dumps(ix,ensure_ascii=False,indent=2)+'\n')
print('Actual full-file searches',len(rows),'rows',len(ix),'groups',len(groups),'sources',len(sources))
for g in groups:
 print(g,{r['baseline']:r['hit_count'] for r in rows if r['group']==g and 'source_id' not in r and r['baseline']!='elsewhere'})
