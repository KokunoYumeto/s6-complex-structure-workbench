"""Append only exact editions and locators opened in this current audit."""
from pathlib import Path
import csv,datetime,hashlib,json,re
W=Path(__file__).resolve().parents[2];A=W/'analysis/IV'
base=W.parents[1]
bibs=[W/'S6_10_PAPERS_references.bib',base/'sources/newer_night/checkpoint27/S6_06_BLIND_references.bib']
texts={str(p.relative_to(base)):p.read_text() for p in bibs}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
checker='GPT-6 Astra Pro (OpenAI, ChatGPT; current writing, 18 November 2026)'
rows=[
('IV-R-015','mapsMilnor65',[],'John W. Milnor',
 'Original 1965 Lectures on the h-Cobordism Theorem, Theorem9.1 p.107, adjacent remark/Definition9.2 pp.107–108, PropositionsA–B and their proofs pp.108–110',
 'https://webhomes.maths.ed.ac.uk/~v1ranick/surgery/hcobord.pdf','Milnor1965.pdf',
 'Read the complete four-page locus in text and rendered scan. The product theorem requires a simply connected triad of dimension at least6 with zero relative integral homology. Its proof cancels the extreme Morse indices by Theorem8.1 and invokes Theorem7.8. PropositionsA–B prove the contractible-disc and literal two-disc presentation by excision and the product theorem. Applied those exact hypotheses to the seven-sphere with two coordinate balls removed. This new locus is separate from earlier readings of Theorems1.4,3.13,5.8; it does not claim a current full reading of their entire antecedent handle-cancellation chapters.'),
('IV-R-016','Cerf1970',[],'Jean Cerf',
 'Publications Mathématiques IHÉS39(1970), definitions pp.7–8, Theorem0 and Corollaries1–2 p.8, including the printed corollary proof',
 'https://www.numdam.org/item/PMIHES_1970__39__5_0.pdf','Cerf1970.pdf',
 'Read the definitions of isotopy and pseudo-isotopy and visually read the exact theorem, both corollaries and the shrinking-ball/annulus proof. Applied Corollary2 with n=7: the connected disc diffeomorphism group identifies the isotopy group of S6 with the group of gluing maps modulo disc extension. No claim of a current full reading of the 165-page proof of the pseudo-isotopy theorem.'),
('IV-R-017','Smale1961',['Smale61'],'Stephen Smale',
 'Bulletin AMS67(1961), TheoremJ and its following comparison p.393, definitions and TheoremK p.394',
 'https://math.uchicago.edu/~shmuel/tom-readings/Smale,%20PC.pdf','Smale1961.pdf',
 'Read both pages in text and rendered scan. TheoremJ supplies the oriented h-cobordism/diffeomorphism comparison in dimension7. TheoremK is recorded with its actual parity ranges; its even-dimensional Gamma-to-A surjectivity is not used as an odd-dimensional two-disc theorem. The needed seven-dimensional two-disc map is proved using the separately opened Milnor product theorem.'),
('IV-R-018','EellsKuiper1962',[],'James Eells and Nicolaas H. Kuiper',
 'Publications Mathématiques IHÉS14(1962), Section3 p.96 and Section6 equation(11) with bundle calculations pp.101–103',
 'https://webhomes.maths.ed.ac.uk/~v1ranick/papers/eellskuiper.pdf','EellsKuiper1962.pdf',
 'Read the invariant hypotheses, its exact seven-dimensional denominator896 and the complete Section6 bundle calculation. Visually checked printed96 and101. The rank-four disc bundle with h=2 has Euler1, p1=6 times the generator and signature1, giving mu1/28. The source distinguishes all28 oriented classes. The receiving proof constructs spin fillings by boundary connected sums of this explicit bundle and orientation reversal; relative H4 uniqueness follows from the actual homotopy-sphere boundary.'),
('IV-R-019','Krylov2001',[],'Nikolai A. Krylov',
 'arXiv:math/0107005v1, Section2.1 pp.2–4, especially exact sequences(1)–(2) and the definitions of chi and iota p.3',
 'https://arxiv.org/pdf/math/0107005v1','Krylov2001.pdf',
 'Read the complete section. It reproduces Kreck’s exact sequences under the framed-boundary hypothesis and spells out the normal derivative chi and the actual supported-disc inclusion iota. The stated S3 times S3 case bounds framed S3 times D4, so the inertia quotient is zero. This is an opened reading of Krylov’s reproduction and its explicit maps; no separate current reading of Kreck1979Theorem2 is claimed. Earlier current scopes at equation5p6 and Theorems2–3pp10–13 remain separate.')
]
data=json.loads((A/'reference_checks.json').read_text());seen={r['event_id'] for r in data}
for eid,key,aliases,author,locator,url,file,check in rows:
 assert eid not in seen,eid
 sources={}
 for k in [key]+aliases:
  sources[k]=[p for p,s in texts.items() if re.search(r'@\w+\s*\{\s*'+re.escape(k)+r'\s*,',s)]
  assert sources[k],k
 p=A/'references'/file
 rec=dict(event_id=eid,bib_key=key,bib_aliases=aliases,author=author,locator=locator,source=url,
          check=check+' PDF SHA256 '+hashlib.sha256(p.read_bytes()).hexdigest(),
          checker=checker,recorded_at=now,bib_key_sources=sources,
          bib_key_match_scope='Author/title and opened edition validated. Verification applies only to these exact locators and edition; no pagination or proof scope transfers to another edition.',
          bib_key_matched_at=now)
 data.append(rec)
(A/'reference_checks.json').write_text(json.dumps(data,indent=2)+'\n')
cols=['event_id','bib_key','bib_aliases','author','locator','source','check','checker','recorded_at']
with (A/'reference_checks.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=cols,delimiter='\t');w.writeheader()
 for r in data:w.writerow({k:'; '.join(r[k]) if isinstance(r.get(k),list) else r.get(k,'') for k in cols})
print(json.dumps({'references_added':len(rows),'recorded_at':now}))
