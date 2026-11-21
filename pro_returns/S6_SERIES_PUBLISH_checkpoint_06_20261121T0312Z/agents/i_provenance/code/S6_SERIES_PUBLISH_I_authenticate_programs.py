from pathlib import Path
import json,csv,urllib.request,hashlib,datetime,concurrent.futures

ROOT=Path('/workspace/scratch/653608133b22');B=ROOT/'work/agents/i_provenance';P=B/'programs';P.mkdir(exist_ok=True)
commit='83d76022bcd442278b760db9ff438afceed6c6ea'
repo='KokunoYumeto/s6-complex-structure-workbench'
cp15='pro_returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z/S6_10_PAPERS/code/I/'
cp10='pro_returns/S6_SERIES_GRIND_checkpoint_10_20261120T0211Z/'
treefile=ROOT/'work/agents/i_analytic/S6_SERIES_PUBLISH_I_program_tree_receipt.json'
tree=json.loads(treefile.read_text())['tree']['tree']
configs=[
 ('cd_torsion_independent.py','fam:src:D.1.1;fam:src:D.1.3','Exact sixth- and fourth-division expressions used for the exceptional-fibre lists','replay_family_applications/cd_torsion_independent.py'),
 ('real_involutions.py','mapsI:src:A.3.2','Integral and affine fixed-set Smith/Hermite computations for the three real parameter arcs','replay_maps/real_involutions.py'),
 ('real_finite_four.py','mapsI:src:A.3.2','Denominator-24 finite-root fixed sets and deck permutations','replay_maps/real_finite_four.py'),
 ('cusp_hexagon_exact.py','fam:src:C.4.1','Thirty-six primitive-ray pairs, twelve fan maps and six curve actions','code/current_audits/audit_paper_i/code/cusp_hexagon_exact.py')
]
manifest=list(csv.DictReader((ROOT/'source/S6_SERIES_GRIND_filelist.tsv').open(),delimiter='\t'))
def download(cfg):
 name,ids,scope,rel=cfg
 iscusp=name=='cusp_hexagon_exact.py';prefix=cp10 if iscusp else cp15
 rp=prefix+rel;url=f'https://raw.githubusercontent.com/{repo}/{commit}/{rp}'
 with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=45) as r:b=r.read();status=r.status
 sha=hashlib.sha256(b).hexdigest();blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
 local=P/('S6_SERIES_PUBLISH_I_primary_'+name);local.write_bytes(b)
 if iscusp:
  ms=[x for x in manifest if x['path']==rel];assert len(ms)==1
  expected=ms[0];attached=ROOT/'source/S6_PUBLISH_programs'/rel
  assert len(b)==int(expected['size']) and sha==expected['sha256'] and b==attached.read_bytes()
  basis='Pinned primary raw bytes equal attached file and exact attached manifest SHA256/size'
  exp=dict(manifest_path=rel,sha256=expected['sha256'],bytes=int(expected['size']))
 else:
  es=[x for x in tree if x['path']==rel];assert len(es)==1
  expected=es[0];assert blob==expected['sha'] and len(b)==expected['size']
  basis='Pinned primary raw bytes equal authenticated cp15 I-tree Git blob and size'
  exp=dict(tree_path=rel,git_blob_sha1=expected['sha'],bytes=expected['size'],tree_receipt=str(treefile))
 return dict(filename=name,statement_ids=ids,mathematical_scope=scope,commit=commit,path=rp,url=url,http_status=status,retrieved_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),bytes=len(b),sha256=sha,git_blob_sha1=blob,verification_basis=basis,expected=exp,local_path=str(local),executed=False)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:rows=list(ex.map(download,configs))
receipt=dict(recorded_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),mathematical_check_events=0,programs=rows,scope='Authentication only: these historical files were downloaded and their bytes identified; none was executed. Current-run checks are not asserted to exist at this historical commit.')
(B/'S6_SERIES_PUBLISH_I_family_program_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
fields=['filename','statement_ids','commit','path','bytes','sha256','verification_basis','url']
with (B/'S6_SERIES_PUBLISH_I_family_program_map.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows([{k:r[k] for k in fields} for r in rows])
tex=[]
for r in rows:
 label=r['filename'].replace('_',r'\_')
 href='https://github.com/'+repo+'/blob/\SsixRepositoryCommit/'+r['path']
 tex.append(r['mathematical_scope']+' & '+r'\href{'+href+'}{'+r'\texttt{'+label+'}}'+r' \\')
(B/'S6_SERIES_PUBLISH_I_family_program_rows.tex').write_text('\n'.join(tex)+'\n')
print(json.dumps([dict(filename=r['filename'],bytes=r['bytes'],sha256=r['sha256'],http_status=r['http_status']) for r in rows],indent=2))
