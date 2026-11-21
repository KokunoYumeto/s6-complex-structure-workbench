from pathlib import Path
import re,json,hashlib,datetime
root=Path('/workspace/scratch/653608133b22');p=root/'work/S6_SERIES_PUBLISH_references.bib';s=p.read_text();changes=[]
def field(entry,key,value):
 pat=r'(?m)^\s*'+re.escape(key)+r'\s*=\s*\{[^\n]*\},?\s*$'
 new='  '+key+' = {'+value+'},'
 if re.search(pat,entry):return re.sub(pat,lambda m:new,entry,count=1)
 return entry[:-1]+new+'\n}'
for key in ['mapsWhitehead50','mapsMilnor65','IVVOkaOneV5']:
 m=re.search(r'@\w+\{'+key+r',\n.*?\n\}',s,re.S);assert m;old=m.group();new=old
 if key=='mapsWhitehead50':
  new=field(new,'url','https://pmc.ncbi.nlm.nih.gov/articles/PMC1063132/')
  new=field(new,'publication_verification','21 November 2026. Publisher-deposited PMC page images directly read: Theorem 1, p.55 (exact sequence); Section 2 and the preceding infinite-complex discussion, p.57 (quadratic group and weak-direct-sum rule); Theorem 5 and operator naturality, p.58 (quadratic identification and deck-equivariance). This is a locator/scope check of those pages, not a new independent proof check or a claim of a current full-article reading.')
  new=field(new,'publication_verification_record',r'agents/provenance/literature/S6\_SERIES\_PUBLISH\_V\_final\_locator\_addendum\_receipt.json')
 elif key=='mapsMilnor65':
  new=field(new,'url','https://press.princeton.edu/books/paperback/9780691273723/lectures-on-the-h-cobordism-theorem')
  new=field(new,'note','Notes by L. Siebenmann and J. Sondow. Cited page numbers refer to the 1965 edition.')
  new=field(new,'publication_verification','21 November 2026. Analytic agent directly read the original 1965 scan: Theorem 1.4, p.2 with proof pp.25--26; Definition 3.9, p.28; Theorem 3.13, pp.31--32; cutoff vector-field construction, pp.62--63; Theorem 5.8, pp.63--64. The publisher chapter independently confirms Theorem 1.4 on p.2. Theorem 5.8 treats a compact submanifold in a boundaryless ambient manifold; the paper derives its marked relative framed application by the explicit collar/cutoff argument. No full-book reading or new mathematical check event is claimed.')
  new=field(new,'publication_verification_record',r'agents/v\_analytic/literature/S6\_SERIES\_PUBLISH\_V\_Milnor\_locator\_receipt.json')
  new=field(new,'publication_retrieval_url','https://www.math.auckland.ac.nz/~hekmati/Books/Milnor2.pdf')
  new=field(new,'publication_retrieval_sha256','ad179436219871b2cfa8d6026525346ef6c60680e8e761a1b30a730ebd710291')
 else:
  pat=r'(?m)^\s*publication_verification\s*=\s*\{([^\n]*)\},?\s*$';pm=re.search(pat,new);assert pm
  value=pm.group(1)+' Additional locator verification on 21 November 2026: Lemma 5.1 statement, p.14; spray/gluing equations (5.6)--(5.8), pp.16--17; Theorem 6.1 statement, p.17. These primary PDF pages were visually read by the provenance reader. The separate analytic review covers the vertical-spray adaptation; this locator pass adds no mathematical event.'
  new=field(new,'publication_verification',value)
  new=field(new,'publication_verification_record',r'agents/v\_analytic/S6\_SERIES\_PUBLISH\_V\_Oka\_v5\_locator\_receipt.json; agents/provenance/literature/S6\_SERIES\_PUBLISH\_V\_final\_locator\_addendum\_receipt.json')
 changes.append({'id':'final-source-'+key,'bibkey':key,'old':old,'new':new,'reason':'Primary URL and exact current locator/scope; all prior verification history is preserved in nonprinting fields.','mathematical_events_added':0})
 assert s.count(old)==1
q=root/'work/agents/provenance/S6_SERIES_PUBLISH_V_bibliography_final_reading_supplement.json';q.write_text(json.dumps({'source':str(p),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'changes':changes,'scope':'Shared-bibliography guarded changes only; root owns integration and synchronization of inline bibliography.','mathematical_events_added':0},ensure_ascii=False,indent=2)+'\n')
print('guards',len(changes),'path',q)
