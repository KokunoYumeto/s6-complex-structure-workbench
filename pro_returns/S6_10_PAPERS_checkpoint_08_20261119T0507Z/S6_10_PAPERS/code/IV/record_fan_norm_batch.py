from pathlib import Path
import csv,datetime,hashlib,json,re
W=Path(__file__).resolve().parents[2];R=W.parents[1];A=W/'analysis/IV'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
checker='GPT-6 Astra Pro (OpenAI, ChatGPT; current writing, 18 November 2026)'
events=json.loads((A/'current_check_events.json').read_text())
idx=json.loads((W/'analysis/inventory_source_index.json').read_text())
blocks={v.get('label'):v for v in idx.values() if isinstance(v,dict)}
body=(W/'papers/IV/body.tex').read_text()
data=[
 ('IV-D-066','night:P3F.30','Full quadratic norm morphism, transverse resolution and retained opposite Hopf factors',
  'Read and rederived the complete proof. The actual line identities N=M tensor T*M=M²(−C0) and T*N=N(−F) use the two exchanged I2 components. The map v→v tensor phi_p^{-1}(v), in coordinates v²/f(p), intertwines the full original suspension with the norm suspension and scalar lambda² by the displayed coefficient identity. The Tate map W=V²/Z has integral matrix[[1,0],[−1,2]], sends both retained period vectors to their exact norm vectors and gives the actual cone invariant rings of the order-two quotient. At the fixed curve the invariants x=a²,z=ab,y=b² satisfy xy=z²; the two displayed resolution charts glue by the original O(−1) transitions and retain the residual tau=delta² action. They give exactly O(−2)_{−1}+O0_{+1} and O0_{−1}+O(−2)_{+1}. The receiving proof now prints the Hermitian conjugate-line duality map and an explicit smooth SU2 disk extension of diag(e^{itheta},e^{−itheta}); factoring the two positive-weight bundles therefore retains base Hopf factors of degree+1 and−1. All maps commute with the given parameter closing. The distinct positive-fan zero and negative-fan−3 applications cite their full actual comparisons; no unproved equality of indices through the auxiliary norm quotient is asserted.'),
 ('IV-D-067','night:P3F.35','Complete one-vertex fan classification, actual periodic flops and prime fixed-set budget',
  'Read and rederived the complete proof. Area one and unimodularity force two triangle and three edge orbits. From triangle(0,a,b), the three actual edge classes force every adjacent triangle and the basis fan T(a,b−a). Replacing its diagonal implements exactly T(v−w,w); reversing the other selected diagonal implements T(v+w,w). Euclid on the primitive first-coordinate row terminates by these individual integral column moves. In each edge orbit the actual curves are disjoint, have no lattice stabilizer and have the conifold relation r0+r2=r1+r3. The common blowup has normal O(−1,−1) on P1xP1, giving the two actual ruling contractions. Its integral cohomology splitting is primitive by exceptional degree−1, and general position plus van Kampen preserve pi1. The already opened Smale/KM63 inputs give the smooth six-sphere from these exact groups. For primitive delta=av+bw, the quotient-lattice maps give isotropy orders |b|,|a|,|a−b|. A prime divides at most one; the determinant-one triangle weights have sum zero and gcd one, so each fixed chart is its origin or one axis. The actual gluings give one complete P1 or exactly two points, each of total mod-prime Betti number two. Regular-fibre primitivity excludes escaping components. A separate nonfree cap contributes an additional compact fixed component and violates the currently opened Floyd Thm4.4 bound. This proves cap freeness for all allowed fans, without asserting global semifreeness for every such fan. Original AC Proposition9.24/Remarks9.25–26 pp82–83 supply the known reference-fan special case and are now expressly credited; no novelty claim is inferred from the bounded search.'),
 ('IV-D-068','night:P3K.19','Primitive effective cap, exact normal-root cancellation and multiplicative source restrictions',
  'Read and rederived the entire proof using the completed K14–16/K18 maps. C-orbits are the components of the finite source quotient and residual H transitivity gives A,B transitivity before quotient. The pulled-back section makes the original multiplicity vector primitive, so every root component has multiplicity one. Centrality gives a common pointwise stabilizer of order h; the faithful normal character and u=z^g yield actual quotient multiplicity g/h. The primitive-meridian theorem forces h=g. At a reduced singular germ, finite averaging linearization cannot fix the whole singular curve unless its derivative and then its full germ are identity, contradicting its root character. At a smooth elliptic germ, the invariant tangent coordinate and the given normal coordinate give exactly(e,z)→(e,zeta_g z), quotient(e,u=z^g); the invariant line frames likewise descend, producing the actual primitive source/line cap with all outer meridians retained. For I_N the Tate-root component group is Z/(Nm), the canonical root deck preserves labels, and translations have labels alpha and mc. The norm identity gives alpha=nc mod N. The actual component orbit count gcd(Nm,alpha,mc) and transitivity imply gcd(N,c)=1. The root line multidegree equation e_{ma[G]}−e0+B_{Nm}d=0, paired with the cyclic labels, gives N|a[G]. The retained F2 generator markings make these gcd(N,b)=1 and N|a. The receiving proof now displays R_N=[[1,N],[0,1]] and its inversion composite−R_N, whose traces prove no marking conjugates them. A node blowup introduces multiplicity two, while a transitive reduced all-minus-one fibre would be a two-sphere tree of arithmetic genus zero. Thus the stated relatively minimal restrictions cannot be evaded by those equivariant blowups. No closed numerical return is claimed from this structural theorem.')]
for eid,label,scope,derivation in data:
 assert not any(e['event_id']==eid for e in events),eid
 b=blocks[label];a=body.index(r'\label{'+label+'}');z=body.index(r'\end{proof}',a)+len(r'\end{proof}')
 events.append(dict(event_id=eid,type='D',labels=[label],verdict='proved',scope=scope,derivation=derivation,checker=checker,recorded_at=now,source_checkpoint=28,
  source_block_sha256={label:hashlib.sha256((R/b['file']).read_text()[b['start']:b['end']].encode()).hexdigest()},
  receiving_block_sha256={label:hashlib.sha256(body[a:z].encode()).hexdigest()},source_file_sha256={label:b['sha256']},
  artifacts=['papers/IV/body.tex','code/IV/fan_norm_repairs.py']))
def tsv(path,rows,cols):
 with path.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=cols,delimiter='\t');w.writeheader()
  for e in rows:w.writerow({k:json.dumps(e[k],ensure_ascii=False) if isinstance(e.get(k),(list,dict)) else e.get(k,'') for k in cols})
(A/'current_check_events.json').write_text(json.dumps(events,indent=2)+'\n')
tsv(A/'current_check_events.tsv',events,['event_id','type','labels','verdict','scope','derivation','checker','recorded_at','artifacts'])
refs=json.loads((A/'reference_checks.json').read_text())
assert not any(x['event_id']=='IV-R-034' for x in refs)
p=R/'sources/original/AC26_original_manuscript.pdf'
keys=['AC26','AC2026','AC26Root','mapsAC26'];bib=W/'S6_10_PAPERS_references.bib'
for key in keys:assert '{'+key+',' in bib.read_text()
refs.append(dict(event_id='IV-R-034',bib_key=keys[0],bib_aliases=keys[1:],author='Claude and Levent Alpöge',
 locator='Attached original108-page manuscript: Proposition9.24 with full proof pp82–83; full Remarks9.25–9.26 p83',
 source='sources/original/AC26_original_manuscript.pdf',
 check='Read the original PDF text and visually inspected both printed pages82–83. Opened the complete Proposition9.24 proof: actual etale quotient, reference-fan cocharacter, full fixed P1, and weights+1,−1. Read the complete finite-subgroup fixed-lattice criterion in Remark9.25 and the alternative two-point computation in Remark9.26. These establish the credited original reference-fan scope. The full arbitrary-basis fan classification, periodic flops and all-fan cap-freeness application are independently proved in the receiving F35. No entire-source or independent-authority credit is inferred. PDF SHA256 '+hashlib.sha256(p.read_bytes()).hexdigest(),
 checker=checker,recorded_at=now,bib_key_sources={key:['work/S6_10_PAPERS/S6_10_PAPERS_references.bib'] for key in keys},
 bib_key_match_scope='Same two authors, exact title, year2026, original URL and attached108-page edition; all aliases share only this bounded opening.',bib_key_matched_at=now))
(A/'reference_checks.json').write_text(json.dumps(refs,indent=2)+'\n')
tsv(A/'reference_checks.tsv',refs,['event_id','bib_key','bib_aliases','author','locator','source','check','checker','recorded_at'])
searches=json.loads((A/'credit_searches.json').read_text())
paths=['work/S6_10_PAPERS/analysis/V/AC26_original_extracted.txt','sources/papers/arXiv_2609.38442_Engel_src/S6.tex','sources/papers/arXiv_2610.00250v1_Du_Guo_Kusakabe_Xie.tex','sources/papers/arXiv_2610.00250v2_Du_Guo_Kusakabe_Xie.tex']
for eid,label,scope,derivation in data:
 terms={'night:P3F.30':['norm','quotient','Hopf'],'night:P3F.35':['triangulation','fixed','flop'],'night:P3K.19':['multiplicit','component','primitive']}[label]
 sources=[]
 for rel in paths:
  p=R/rel;lines=p.read_text().splitlines();hits=[]
  for term in terms:
   found=[dict(line=i,text=x.strip()[:300]) for i,x in enumerate(lines,1) if re.search(term,x,re.I)]
   hits.append(dict(term=term,count=len(found),first_locators=found[:5]))
  sources.append(dict(file=rel,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),hits=hits))
 rec=next(x for x in searches if x['label']==label)
 assessment=('Found exact reference-fan fixed-locus and finite-subgroup results in AC original Proposition9.24/Remarks9.25–26 pp82–83; credited and applied with the actual quotient-lattice maps. No identical all-basis classification/flop/cap-freeness result established by these bounded searches.' if label=='night:P3F.35' else 'Bounded source searches did not establish an identical complete retained-map application. The precise earlier inputs remain cited and the full local map computation is displayed; no novelty claim follows from the unmatched search.')
 rec.update(recorded_at=now,terms=terms,sources=sources,assessment=assessment,related_material_read=scope+'; exact primary-source openings are separately recorded.')
(A/'credit_searches.json').write_text(json.dumps(searches,indent=2)+'\n')
tsv(A/'credit_searches.tsv',searches,['label','paper','event_type','recorded_at','checker','terms','assessment','related_material_read','sources'])
print(json.dumps(dict(recorded_at=now,new_D_events=3,D_labels=len({l for e in events if e['type']=='D' for l in e['labels']}),reference_events=len(refs))))
