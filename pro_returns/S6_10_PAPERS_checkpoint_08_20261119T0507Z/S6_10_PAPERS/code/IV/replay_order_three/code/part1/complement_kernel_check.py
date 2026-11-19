from pathlib import Path
import contextlib,io,json
with contextlib.redirect_stdout(io.StringIO()):
 exec(Path(__file__).with_name('complement_check.py').read_text().split('out={}')[0])
out={}
for k in range(1,4):
 ya=yd(k);yb=yd(k+1);ba=dbdry(0,k);bb=dbdry(0,k+1)
 yz,yp,yr=hpresentation(ya,yb);bz,bp,br=hpresentation(ba,bb)
 assert yr==s.zeros(*yr.shape)
 j=yp*yj(k)*bz
 jd,ju,jv=snf(j);K=jv[:,j.rank():]
 assert all(abs(jd[i,i])==1 for i in range(j.rank())) and j.rank()==j.rows
 rel=K.gauss_jordan_solve(br)[0]
 assert all(x.q==1 for x in rel)
 rd,ru,rv=snf(rel);rr=rel.rank()
 keep=[i for i in range(rel.rows) if i>=rr or abs(rd[i,i])>1]
 KC=bz*K*ru.inv()[:,keep]
 KR=s.zeros(len(keep),len(keep))
 for jj,ii in enumerate(keep):
  if ii<rr:KR[jj,jj]=rd[ii,ii]
 susp=KC[dim(6,k):,:]
 c=maps[k]*ext(S.inv(),k)*KC[:dim(6,k),:]
 if k>=2:assert susp==s.zeros(*susp.shape)
 print('degree',k,'kernel_relation',KR,'suspension',susp,'collapse_on_kernel',c,flush=True)
 print('collapse_on_kernel_smith',snf(c)[0],flush=True)
 if k>=2:
  assert c.rank()==c.rows
  assert all(abs(snf(c)[0][i,i])==1 for i in range(c.rows))
 if k==2:print('H2_kernel_collapse_determinant',c.det(),flush=True);assert abs(c.det())==1
 if k==3:
  freecols=[i for i in range(KR.cols) if KR[i,i]==0]
  print('H3_free_kernel_collapse_determinant',c[:,freecols].det(),flush=True);assert abs(c[:,freecols].det())==1
 out[str(k)]={'Ycycles':yz.tolist(),'Yprojection':yp.tolist(),'Bcycles':bz.tolist(),'Bprojection':bp.tolist(),'Brelations':br.tolist(),'BtoY':j.tolist(),'kernel_cycles':KC.tolist(),'kernel_relations':KR.tolist(),'kernel_suspension':susp.tolist(),'collapse_on_kernel':c.tolist()}
 if k==1:
  wholec=fcusp(k)*bz
  whole=j.col_join(wholec)
  print('H1_combined_map',whole,'det',whole.det(),flush=True);assert abs(whole.det())==1
  out[str(k)]['combined_map']=whole.tolist()
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2,default=int))
