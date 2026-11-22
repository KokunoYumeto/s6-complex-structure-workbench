from pathlib import Path
import datetime as dt, hashlib, json

R=Path(__file__).resolve().parents[1]
def sha(b):return hashlib.sha256(b).hexdigest()
def bind(p):return dict(path=p,sha256=sha((R/p).read_bytes()))
oldplan='agents/continuation2_root/S6_SERIES_PUBLISH_II_RAT6_restore_plan.json'
plan=json.loads((R/oldplan).read_text())
assert bind(oldplan)['sha256']=='c270fff718c583e235f3fdcdc8ced0bf58fc7955c50b77a2b378d994589684c8'
oldblock=(R/plan['restored_block']['path']).read_text()
newblock=oldblock.replace('and let $X_r$ be the cubic suspension\n','and let $X_r$ be the isolated surface singularity\n').replace('For a finite collection with total delta at most five,','For a collection of these germs with total delta at most five,')
newblock=newblock.replace('modulo one. The bases are','modulo one\n\\cite[\\S1, Theorem~L1 and Example~2.4(a), pp.~1--3]{Nemethi1991Join}.\nThe bases are')
newblockpath='agents/continuation2_root/S6_SERIES_PUBLISH_II_RAT6_v2_proposed.tex'
assert not (R/newblockpath).exists();(R/newblockpath).write_text(newblock)
plan['source_edits'][0]['new']=plan['source_edits'][0]['new'].replace(oldblock,newblock,1)
types=['D06','D12','D09','D18','D18','D18']
for e,t in zip(plan['source_edits'],types):e['type']=t
for e in plan['source_edits']:
 if e['owner']=='Bibliography' and 'Arnold1976NormalForms' in e['new']:
  e['new']=e['new'].replace('\\newblock URL \\url{https://webhomes.maths.ed.ac.uk/~v1ranick/papers/arnold15.pdf}.','\\newblock \\doi{10.1007/BF01390134}.')
  e['reason']+=' Publisher landing page opened and matched the DOI, title, volume, pages and year; the printed citation uses the publisher DOI.'
append=plan['bib_edits'][1]['append']
append=append.replace('  url = {https://webhomes.maths.ed.ac.uk/~v1ranick/papers/arnold15.pdf},','  doi = {10.1007/BF01390134},\n  url = {https://doi.org/10.1007/BF01390134},')
append=append.replace('Published university-hosted scan,','Publisher DOI metadata opened at https://link.springer.com/article/10.1007/BF01390134, confirming title, author, volume, pages and year. Primary text read from https://webhomes.maths.ed.ac.uk/~v1ranick/papers/arnold15.pdf. Published university-hosted scan,')
plan['bib_edits'][1]['append']=append
source=(R/'S6_SERIES_PUBLISH_II.tex').read_text();assert sha(source.encode())==plan['source_before_sha256']
candidate=source
for e in plan['source_edits']:
 assert candidate.count(e['old'])==1
 candidate=candidate.replace(e['old'],e['new'],1)
bib=(R/'S6_SERIES_PUBLISH_references.bib').read_text();assert sha(bib.encode())==plan['bib_before_sha256']
for e in plan['bib_edits']:
 if 'append' in e:bib+=e['append']
 else:
  assert bib.count(e['old'])==1;bib=bib.replace(e['old'],e['new'],1)
plan.update(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),previous_plan=bind(oldplan),restored_block=bind(newblockpath),source_after_sha256=sha(candidate.encode()),bib_after_sha256=sha(bib.encode()),v2_changes='Keep the exact inherited isolated-surface scope; add the already opened Nemethi primary locator; use verified Arnold publisher DOI; align defect classes with the actual register. Mathematical table and BW proposed block unchanged.',online_searches=[dict(query='"Local normal forms of functions" Arnold 1976 35 87 109 doi',engine='system1',scope='Springer and EuDML'),dict(query='"Arnold" "Local normal forms of functions" "10.1007"',engine='system2'),dict(query='"Local normal forms of functions" 87 109 1976',engine='system2')],publisher_page=dict(url='https://link.springer.com/article/10.1007/BF01390134',source_ref='turn665731994view0',actual_reading='Publisher metadata, lines11-24 and98-106; exact title, V.I.Arnold, Inventiones35,87-109,1976, DOI10.1007/BF01390134. No publisher full-text access claimed.'))
out='agents/continuation2_root/S6_SERIES_PUBLISH_II_RAT6_restore_v2_plan.json'
assert not (R/out).exists();(R/out).write_text(json.dumps(plan,indent=2)+'\n')
print(json.dumps(dict(plan=bind(out),restored_block=plan['restored_block'],source_after_sha256=plan['source_after_sha256'],bib_after_sha256=plan['bib_after_sha256']),indent=2))
