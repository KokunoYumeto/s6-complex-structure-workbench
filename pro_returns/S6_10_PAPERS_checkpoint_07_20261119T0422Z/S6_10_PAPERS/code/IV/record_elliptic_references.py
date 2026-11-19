from pathlib import Path
import csv,datetime,hashlib,json,re
root=Path(__file__).resolve().parents[2]
workspace=root.parents[1]
dest=root/'analysis/IV'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
checker='GPT-6 Astra Pro (OpenAI, ChatGPT; current writing, 18 November 2026)'
sources=[workspace/'sources/newer_night/checkpoint27/S6_06_BLIND_references.bib',root/'S6_10_PAPERS_references.bib']
key_sources={}
for p in sources:
 for key in re.findall(r'@\w+\s*\{\s*([^,\s]+)',p.read_text()):
  key_sources.setdefault(key,[]).append(str(p.relative_to(workspace)))
entries=[
 ('IV-R-007','Jin2026',['mapsJin26'],'Huize Jin','arXiv:2608.26698v2, Theorem1.2 and Corollary1.3 p.3; Proposition3.1 pp.10–11; Lemma4.4 and the oriented Poincare-duality proof pp.16–17; Lemma4.8 p.23 and Theorem4.9 p.24','https://arxiv.org/pdf/2608.26698v2','Read the exact statements, g=1 characteristic table, integral basis and adjacent proofs at the listed pages. Checked alpha with p1=4, pairs(1,4),(8,8), A=(4k-ell)/24 and the basis b-8a,a. The earlier Lemma6.2 collar reading remains a separate scope.','analysis/IV/references/Jin2026v2.pdf'),
 ('IV-R-008','OguisoShioda1991',[],'Keiji Oguiso and Tetsuji Shioda','Commentarii Math.Univ.St.Pauli40(1)(1991), Main Theorem table, printed pp.85–86, all rank-one rows43–61','https://rikkyo.repo.nii.ac.jp/record/10006/files/AA00610867_40-01_08.pdf','Downloaded the original Rikkyo scan and visually read both complete pages. Checked every root lattice, free height and torsion entry in rows43–61 against the exact received enumeration program. In particular A7 rows44/45 have different torsion and free heights.','analysis/IV/references/OguisoShioda1991.pdf'),
 ('IV-R-009','Shioda1990',['Shioda90','mapsShioda90'],'Tetsuji Shioda','Original journal edition39(2)(1990), Theorem8.6/eq8.12 p.228; table8.16 p.229; Proposition8.12/eq8.25 p.231','https://rikkyo.repo.nii.ac.jp/record/10027/files/AA00610867_39-02_05.pdf','Downloaded the original Rikkyo scan and visually read printed pp.228–231. Read the complete height-formula proof and the complete degree-of-field-extension proof. Checked local component conventions and the positive correction sign on solving for section intersection. These locators are journal pages, not the separate37-page author-uploaded pagination.','analysis/IV/references/Shioda1990.pdf'),
 ('IV-R-010','Miranda1990',['manMiranda90'],'Rick Miranda','Math.Z.205(1990), Section3 pp.202–205, including Proposition3.4 and its entire proof p.204; Corollary3.5 p.205','https://www.math.colostate.edu/~miranda/preprints/Perssonslist.pdf','Opened the current shared author-PDF copy and read the full j-map pullback, transfer/deflation operations and parity calculation. Visually checked Proposition3.4 p.204. The proof supplies an actual rational elliptic surface with section from the exact prescribed branched map; the permutation genus/transitivity conditions were also opened.','analysis/III_sources/Miranda_1990.pdf'),
 ('IV-R-011','Takase2005',[],'Masamichi Takase','arXiv:math/0506356v1, outward-first orientation p.2; Section2.1, Theorem2.3 and Corollary2.6 p.3','https://arxiv.org/pdf/math/0506356','Downloaded the exact v1 PDF, read pp.2–3 and visually opened p.3. Checked the author correction H=-e^2 and Omega=-(sigma-e^2)/8 for the actual embedded Seifert surface with its cap. No journal pagination is inferred from this preprint.','analysis/IV/references/Takase2005v1.pdf'),
 ('IV-R-012','KervaireMilnor1963',[],'Michel A. Kervaire and John W. Milnor','Ann.Math.77(1963), introductory order table p.504; Smale comparison and connected-sum conventions p.505','https://webhomes.maths.ed.ac.uk/~v1ranick/papers/kervmiln.pdf','Visually opened both original scan pages. The table gives order1 for Theta5; the next page identifies h-cobordism and oriented diffeomorphism classes in dimension5. Corrected F7: the table is p.504, while the comparison is p.505. The two are recorded separately.','analysis/III_sources/Kervaire_Milnor_1963.pdf'),
 ('IV-R-013','HarveyKerinShankar2020',[],'John Harvey, Martin Kerin and Krishnan Shankar','Documenta Math.25(2020), Section2 p.2091; Theorem4.1 pp.2094–2095','https://ems.press/content/serial-article-files/26574?nt=1','Downloaded the journal PDF and read the canonical quotient smooth-structure discussion and the complete statement of Levine classification as given in Theorem4.1. Its hypotheses are codimension4 fixed set and H2(F;Z) without2-torsion; its invariant is the full orbit pair with Euler class. This is supplementary to F7’s explicit equivariant bundle/gauge construction; no proof of Levine’s original theorem is claimed here.','analysis/IV/references/HarveyKerinShankar2020.pdf'),
 ('IV-R-014','Haefliger1966',['Haefliger1966D'],'André Haefliger','Ann.Math.83(1966), Theorem1.2 pp.404–405 and Corollary6.6 p.422, applied with n=2,q=3','https://www.maths.ed.ac.uk/~v1ranick/tda/haefliger.pdf','Applied the already opened exact theorem and corollary to the second required range: n=2,q=3 gives2<2q-3=3. Concordance triviality and Theorem1.2 yield an actual ambient isotopy of the fixed sphere in S5. The earlier n=2,q=4 reading remains a separate scope.','analysis/IV/references/Haefliger1966.pdf'),
]
records=json.loads((dest/'reference_checks.json').read_text());seen={r['event_id'] for r in records}
for event,key,aliases,author,locator,url,check,path in entries:
 assert event not in seen,event
 for k in [key]+aliases:assert k in key_sources,k
 pdf=root/path
 records.append(dict(event_id=event,bib_key=key,bib_aliases=aliases,author=author,locator=locator,source=url,
  check=check+' PDF SHA256 '+hashlib.sha256(pdf.read_bytes()).hexdigest(),checker=checker,recorded_at=now,
  bib_key_sources={k:key_sources[k] for k in [key]+aliases},
  bib_key_match_scope='Author/title and opened edition validated. Verification applies only to these exact locators and edition; no pagination or proof scope transfers to another edition.',
  bib_key_matched_at=now))
(dest/'reference_checks.json').write_text(json.dumps(records,indent=2)+'\n')
cols=['event_id','bib_key','bib_aliases','author','locator','source','check','checker','recorded_at']
with (dest/'reference_checks.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=cols,delimiter='\t');w.writeheader()
 for r in records:w.writerow({k:'; '.join(r[k]) if isinstance(r.get(k),list) else r.get(k,'') for k in cols})
print(json.dumps({'records_added':len(entries),'at':now,'total':len(records)}))
