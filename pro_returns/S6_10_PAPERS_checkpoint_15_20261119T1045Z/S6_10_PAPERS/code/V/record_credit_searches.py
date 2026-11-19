"""Record actually executed per-result local credit searches, without novelty inference."""
from pathlib import Path
import csv,json,re,datetime,hashlib
R=Path(__file__).resolve().parents[4];W=R/'work/S6_10_PAPERS'
files=[W/'analysis/V/AC26_original_extracted.txt',R/'sources/papers/arXiv_2609.38442_Engel_src/S6.tex',R/'sources/papers/arXiv_2610.00250v1_Du_Guo_Kusakabe_Xie.tex',R/'sources/papers/arXiv_2610.00250v2_Du_Guo_Kusakabe_Xie.tex']
corpus=[(p,p.read_text(errors='replace')) for p in files]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
for paper in ['IV','V']:
 rows=list(csv.DictReader((W/f'analysis/inventory_paper_{paper}_selection.tsv').open(),delimiter='\t'))
 out=[]
 for row in rows:
  label=row['label'];ident=row['source_id']
  if paper=='IV':
   terms=[r'Theta.?7',r'Eells.?Kuiper',r'mapping.tor',r'smooth.monodromy',r'fixed.edge',r'flop']
   if ident.startswith('P3K.') and int(ident.split('.')[-1])>=94:terms=[r'selected.cusp',r'III.star',r'IV.star',r'Miller',r'quaternion',r'unselected']
   related='Engel, Additional remarks, final remark (source lines 1734–1762): the general elliptic-source translation/line construction with logarithmic transforms and the proper Mumford quotient is an antecedent. It does not state the currently calculated Theta7 value. AC Appendix A, Lemmas A.5–A.6 (extracted text lines 6350–6398): peripheral mapping-torus/Wang and cusp retraction calculations. The current parameter-return map retains its separate source, target, cap and orientation comparison.'
  else:
   terms=[r'fourfold',r'rank.six',r'rank.6',r'quaternion',r'genus.two',r'5,.?4']
   if ident.startswith('P1A') or ident=='P1.17':terms += [r'Kuranishi',r'Kodaira.Spencer',r'automorphism']
   if ident.startswith('F.2.') and int(ident.split('.')[-1])>=15:terms += [r'integral.similarity',r'lattice.isomorph',r'unbounded']
   related='The four requested works supply the threefold/construction context. This executed term search did not locate the specified rank-six/fourfold calculation. Relevant positive theorem inputs actually opened in this writing are separately recorded in reference_checks.json, with exact version and page locators.'
  rec={'label':label,'paper':paper,'event_type':'current credit search','recorded_at':now,'checker':'GPT-6 Astra Pro (OpenAI, ChatGPT; current writing)','terms':terms,'sources':[],'assessment':'No identical result has been established by this term search; no novelty classification is inferred from its absence of exact-name hits.','related_material_read':related}
  for p,txt in corpus:
   hits=[]
   for term in terms:
    ms=list(re.finditer(term,txt,re.I))
    hits.append({'term':term,'count':len(ms),'first_locators':[{'line':txt.count('\n',0,m.start())+1,'context':txt[max(0,m.start()-90):m.end()+140].replace('\n',' ')} for m in ms[:3]]})
   rec['sources'].append({'file':str(p.relative_to(R)),'sha256':hashlib.sha256(txt.encode()).hexdigest(),'hits':hits})
  out.append(rec)
 (W/f'analysis/{paper}/credit_searches.json').write_text(json.dumps(out,indent=2,ensure_ascii=False))
 with (W/f'analysis/{paper}/credit_searches.tsv').open('w') as f:
  q=csv.DictWriter(f,fieldnames=['label','paper','event_type','recorded_at','checker','terms','source_files','assessment','related_material_read'],delimiter='\t');q.writeheader()
  for r in out:q.writerow({**{k:r[k] for k in ['label','paper','event_type','recorded_at','checker','assessment','related_material_read']},'terms':'; '.join(r['terms']),'source_files':'; '.join(x['file'] for x in r['sources'])})
 print(paper,len(out),'per-result searches recorded')
