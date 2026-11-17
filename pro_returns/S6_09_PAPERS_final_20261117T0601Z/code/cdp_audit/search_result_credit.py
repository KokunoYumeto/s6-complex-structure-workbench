"""Execute bounded, result-specific searches of all four required baselines.

Searches are evidence of the stated search scope, not a proof of novelty. The
comparison matrix is written separately after reviewing source contexts.
"""
from pathlib import Path
import json,re,hashlib,subprocess
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'deliverables/work/cdp_audit'
sources={
 'AC26':[
  ROOT/'sources/original/AC26_transcription.tex',
  ROOT/'sources/external/root/AC26_pdf_text.txt'],
 'E26':[ROOT/'sources/papers/arXiv_2609.38442_Engel_src/S6.tex'],
 'DGKX_v1':[ROOT/'sources/papers/arXiv_2610.00250v1_Du_Guo_Kusakabe_Xie_src/v5oka_maps_modifications_deformations.tex'],
 'DGKX_v2':[ROOT/'sources/papers/arXiv_2610.00250v2_Du_Guo_Kusakabe_Xie_src/submited-tams.tex']}
manual={
'A.1.1':['conormal','cotangent','torsion'],
'A.1.2':['normal.crossing','conductor','ambient'],
'A.2.1':['Jacobian','fractional ideal','hypersurface'],
'A.2.2':['normali[sz]ation','conductor','kernel'],
'A.2.3':['Jacobian','normal.crossing','Granger'],
'A.2.4':['pinch','cuspidal edge','Whitney'],
'A.2.5':['tacnod','residue pole','cuspidal'],
'A.2.6':['symbolic square','critical.curve','Hessian'],
'A.3.1':['thicken','nilpotent','lifting'],
'A.3.2':['multiple fibre','multiple fiber','nilpotent'],
'A.3.3':['finite.translation','multiple fibre','Remark 7.4'],
'A.3.4':['smooth.multiple','root cover','unitary'],
'A.3.5':['reducible','ambient','generic'],
'A.4.1':['10.5','torsion.free','normalisation'],
'A.4.2':['genus.*two','Proposition 7.3','constant.family'],
'A.4.3':['genus.one','rank.one','singular fibre'],
'A.4.4':['canonical.*trivial','irreducible','torus fibre'],
'A.4.5':['normal.crossing','cotangent','non.torsion'],
'A.4.6':['normal.crossing','Euler','irreducible'],
'A.4.7':['unitary.flat','holomorphic.*form','Stokes'],
'A.4.8':['singular.support','local.system','Koszul'],
'A.4.9':['Proposition 7.3','Hopf','Inoue','Kodaira'],
'A.5.1':['conductor','normalisation','10.3'],
'A.5.2':['Gorenstein','Chern','minimal.resolution'],
'A.5.3':['effective.conductor','anticanonical','resolution'],
'A.5.4':['persistent','ruled','class VII'],
'A.5.5':['critical.curve','tacnod','ordinary.triple'],
'A.5.6':['Gauduchon','negative.degree','Bochner'],
'A.5.7':['pure.double','derivation','cusp.product'],
'A.5.8':['rational.singularit','irrational.ruled','exceptional'],
'A.5.9':['ruled','conductor','reduced.image'],
'A.5.10':['horizontal.cusp','conductor','minimal.elliptic'],
'A.5.11':['horizontal','conductor','fundamental.group'],
'A.5.12':['conductor','arithmetic.genus','duality'],
'A.5.13':['conductor','arithmetic.genus','geometric.genus'],
'A.5.14':['conductor','arithmetic.genus','complete.intersection'],
'A.5.15':['Hirzebruch','Milnor','suspension'],
'A.5.16':['rational.normali[sz]ation','conductor','singularit'],
'A.5.17':['isolated.hypersurface','suspension','Milnor'],
'A.5.18':['tacnod','double.cover','irrational.ruled'],
'A.5.19':['ordinary.triple','arithmetic.genus','horizontal'],
'A.5.20':['horizontal.cusp','ruled','Euler'],
'A.5.21':['binary.product','nodal.grid','delta'],
'B1':['nodal','endpoint','conductor'],
'B2':['twelve','length.one','rational.elliptic'],
'B3':['Theorem 2.2','Corollary 2.3','10.5'],
'C.1.1':['Riemann.Roch','Picard','index'],
'C.1.2':['effective.divisor','generic','Corollary 1.3'],
'C.1.3':['Riemann.Roch','semi.continu','tangent'],
'C.3.1':['Hopf','very.general','general.fib'],
'C.3.2':['secondary.Kodaira','homology','Kodaira.surface'],
'C.3.3':['secondary.Hopf','Hopf.surface','homology'],
'C.3.4':['reducible','resolution','positivity'],
'C.3.5':['Euler','singular.fib','Hopf'],
'C.3.6':['Hopf','Calabi','Eckmann'],
'C.3.7':['bielliptic','Kawai','nonexist'],
'C.3.8':['Hopf','algebraic.dimension','contraction'],
'C.3.9':['secondary.Kodaira','structure.sheaf','monodromy'],
'C.3.10':['primary.Kodaira','Borcea','period'],
'C.3.11':['cohomological','full.fib','Hopf'],
'C.3.12':['Inoue','ambient','cohomology'],
'C2a':['Euler','critical.value','localization'],
'C2b':['nonnegative','Euler','torus.fib'],
'C2c':['semistable','toric','Mumford'],
'C2d':['normal.jet','tacnod','ordinary.triple'],
'C4a':['geometric.replacement','normalisation','ambient'],
'C4b':['rational.homology','six.sphere','nonvanish'],
'C4c':['singular.fib','normalisation','transgression'],
'C4d':['transgression','Hopf','Kodaira'],
'C4e':['normalisation','Picard','all.twist'],
'C4f':['non.torsion','normalisation','tangent'],
'C4g':['comb','Liu','two.parameter'],
'C5a':['normali[sz]ation','quotient','cohomology.map'],
'C5b':['integral.twist','normalisation','exception'],
'C5c':['nonintegral','resonance','length'],
'D.1.1':['semidirect','co.invariant','10.7'],
'D.1.2':['component.count','co.invariant','torsion'],
'D.1.3':['co.invariant','monodromy','rank.one'],
'D.1.4':['restriction.map','Corollary 5.2','Proposition 5.5'],
'D.1.5':['bielliptic','rational.elliptic','split.extension'],
'D.1.6':['Wang','component.count','second.counterexample'],
'D.1.7':['pluriharmonic','real.cohomology','structure.sheaf'],
'D.1.8':['specialization','punctured','meridian'],
'D.1.9':['irrational','non.torsion','10.8'],
'D.1.10':['invariant.lattice','coherent.restriction','divisor'],
'D.1.11':['dense','Gdelta','non.torsion'],
'D.1.12':['cup.product','Kodaira','base.change'],
'D.1.13':['Wang','nonnegative.splitting','surjectiv'],
'D.1.14':['index.twelve','index.12','stabilizer','Klingler'],
'D.1.15':['twistor','coherent.splitting','constant.monodromy'],
'D.2.1':['trivial.monodromy','reducible','resolution'],
'D.2.2':['trivial.monodromy','Euler','existence'],
'D.2.3':['normal.crossing','geometric.genera','monodromy'],
'D.2.4':['trivial.monodromy','normal.crossing','Euler'],
'D.2.5':['trivial.monodromy','nonpositive','Chern'],
'D.2.6':['period.domain','identity.monodromy','extension'],
'D.2.7':['trivial.monodromy','homology','torus.fibration'],
'D.2.8':['trivial.monodromy','torsion.locus','splitting'],
'E1':['vertical.divisor','meromorphic','factor'],
'E2':['non.holomorphic','meromorphic.map','Lehn'],
'E3':['Moishezon','algebraic.dimension','non.holomorphic'],
'E4':['local.freeness','locally.free','Proposition 5.1'],
'E5':['Leray','cup.product','rank.two'],
'E6':['deformation','fibration','Horikawa'],
'E7':['Kodaira.Spencer','cusp','rank.two'],
'E8':['theta','Weierstrass','determinant'],
'E9':['Kuranishi','tangent.cohomology','miniversal'],
'E10':['positive.genus','fixed.target','Kodaira.Spencer'],
'E11':['coprime','affine.twist','miniversal'],
'E12':['Lemma 1.5','base.change','torsion'],
'E13':['two.parameter','miniversal','tangent.cohomology'],
'E14':['Liu','Rollenske','cusp.splitting'],
'E15':['comb','miniversal','tangent.cohomology'],
'E16':['rank.divisor','Kodaira.Spencer','theta'],
'E17':['embedded.component','Proposition 1.1','higher.image'],
'E18':['theta','square','linearization'],
'E19':['affine.twist','integral.homology','logarithmic.transform']}

keywords=[
 ('Hopf','Hopf'),('Enriques','Enriques'),('Kummer','Kummer'),('K3','K3'),
 ('semicomplete','semicomplete'),('canonical-flat','canonical.flat'),
 ('toric','toric'),('weighted','weighted'),('reflected','reflected'),
 ('rooted','rooted'),('pruning','prun'),('quasi-bundle','quasi.bundle'),
 ('quasibundle','quasi.bundle'),('nonlinear','nonlinear'),('cyclic quotient','cyclic.quotient'),
 ('fundamental group','fundamental.group'),('meridian','meridian'),
 ('elliptic','elliptic'),('Kodaira','Kodaira'),('ruled','ruled'),
 ('triple','triple'),('conductor','conductor'),('tacnode','tacnod'),
 ('cusp','cusp'),('contracted','contract'),('rational','rational'),
 ('Euler','Euler'),('monodromy','monodromy'),('normalization','normali[sz]ation'),
 ('blowup','blow.up'),('normal-crossings','normal.crossing'),('mixed Hodge','mixed.Hodge'),
 ('finite analytic','finite.analytic'),('generation','generation'),
 ('reduction','reduction'),('period','period')]

def queries(row):
 sid=row['source_id']; title=row['source_title']
 if sid in manual:return manual[sid]
 pats=[p for term,p in keywords if term.lower() in title.lower()]
 if sid.startswith('C.2.CR.'):pats=['contracted','horizontal','conductor']+pats
 if sid.startswith('C.2.RAT.'):pats=['rational','conductor','tacnod' if 'tacnode' in title else 'triple']+pats
 if sid.startswith('C.2.D4.'):pats=['ordinary.triple','cubic','conductor']+pats
 if sid.startswith('C.2.NC.'):pats=['normal.crossing','multiplicit','Euler']+pats
 if sid.startswith('C.2.VII.'):pats=['class VII','anticanonical','conductor']+pats
 if sid.startswith('C.2.MH.'):pats=['mixed.Hodge','normali[sz]ation','Euler']+pats
 if sid.startswith('C.2.INT.'):pats=['Hopf','Enoki','elliptic']+pats
 if sid=='C.2.IRR.1':pats=['irrational.ruled','horizontal','conductor']+pats
 for default in ['torus','degeneration','fibre']:
  if len(pats)<3:pats.append(default)
 return list(dict.fromkeys(pats))[:6]

rows=json.loads((OUT/'result_audit.json').read_text())
records=[]
for row in rows:
 pats=queries(row)
 for name,files in sources.items():
  scans=[]
  for p in files:
   command=['rg','-n','-i','--no-heading']
   for pattern in pats:command+=['-e',pattern]
   command += [str(p)]
   result=subprocess.run(command,capture_output=True,text=True)
   assert result.returncode in (0,1),(command,result.stderr)
   matches=[]
   for line in result.stdout.split('\n'):
    if not line:continue
    n,_,text=line.partition(':')
    matches.append({'line':int(n),'text':text})
   scans.append({'file':str(p.relative_to(ROOT)),
    'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
    'command':['rg','-n','-i','--no-heading']+sum((['-e',x] for x in pats),[])+[str(p.relative_to(ROOT))],
    'exit_code':result.returncode,'matches':matches})
  records.append({'source_run':row['source_run'],'source_id':row['source_id'],
   'source_title':row['source_title'],'proof_sha256':row['proof_sha256'],
   'baseline':name,'terms_searched':pats,'scans':scans,
   'scope':'Entire specified source files searched. A keyword search alone does not establish absence from the literature; reviewed context and exact credit are recorded separately.',
   'reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date':'2026-11-17 UTC'})
(OUT/'credit_searches_239.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
(OUT/'credit_search_plan_239.json').write_text(json.dumps([{'source_id':r['source_id'],'title':r['source_title'],'queries':queries(r)} for r in rows],ensure_ascii=False,indent=2)+'\n')
print('Executed',len(records),'result/baseline searches;',sum(len(x['scans']) for x in records),'rg processes.')
for baseline in sources:
 relevant=[r for r in records if r['baseline']==baseline]
 union={}
 for r in relevant:
  for s in r['scans']:
   union.setdefault(s['file'],{}).update({m['line']:m['text'] for m in s['matches']})
 print(baseline,[(p,len(lines)) for p,lines in union.items()])
