"""Finite discrepancy statistics, exact heights; arithmetic of C0 at 80 digits.
The statistics are numerical descriptions, not bounds for unbounded X.
"""
import numpy as np, mpmath as mp, json, gzip, hashlib
from pathlib import Path
mp.mp.dps=80
base=Path(__file__).resolve().parent
path=base/'A_census_1e9.u32'
x=np.memmap(path,dtype='<u4',mode='r')
h,m=np.unique(x,return_counts=True)
R=np.cumsum(m,dtype=np.int64)
C=mp.mpf(9)/(2*mp.pi**2)*mp.log(2+mp.sqrt(3))*mp.log(3/(2*mp.sqrt(2)))
c=np.longdouble(str(C))
print('C0 (80 decimal-digit working precision):',mp.nstr(C,80))
print('number_of_solutions',len(x),'occupied_heights',len(h),'maximum_multiplicity',int(m.max()),'first_height_with_maximum',int(h[np.argmax(m)]))
for end in [10**7,10**8,10**9]:
 k=np.searchsorted(h,end,side='right');hh=h[:k].astype(np.int64);rr=R[:k]
 ex=rr.astype(np.longdouble)-c*hh
 ib=int(ex.argmax()); z=int(hh[ib]); n=int(rr[ib]); print('range',end,'max_E',mp.nstr(n-C*z,55),'X',z,'R',n)
 zz=hh-1; nn=rr-m[:k]
 ex2=nn.astype(np.longdouble)-c*zz
 valid=zz>=1; ia=int(np.argmin(np.where(valid,ex2,np.inf)));z=int(zz[ia]);n=int(nn[ia]);print('range',end,'min_E',mp.nstr(n-C*z,55),'X',z,'R',n)
 for zz,nn,label in [(hh,rr,'after'),(hh-1,rr-m[:k],'before')]:
  valid=zz>=10000
  ratio=(nn.astype(np.longdouble)-c*zz)/np.sqrt(np.maximum(zz,1).astype(np.longdouble))
  ia=int(np.argmax(np.where(valid,np.abs(ratio),-1)));z=int(zz[ia]);n=int(nn[ia]);print('range',end,'max_abs_ratio_'+label,mp.nstr(abs(n-C*z)/mp.sqrt(z),55),'X',z,'R',n)
 # also check terminal endpoint
 n=k and int(R[k-1]);print('range',end,'endpoint_ratio',mp.nstr((n-C*end)/mp.sqrt(end),55))
# Continuous integral exact for the step count, evaluated with 80-bit long double.
for lo,hi in [(10**4,2*10**4),(10**5,2*10**5),(10**6,2*10**6),(10**7,2*10**7),(10**8,2*10**8),(5*10**8,10**9)]:
 first=np.searchsorted(h,lo,side='right')-1;last=np.searchsorted(h,hi,side='left')
 starts=np.maximum(h[first:last].astype(np.int64),lo).astype(np.longdouble)
 ends=np.r_[h[first+1:last+1],hi] if last==len(h) else h[first+1:last+1]
 stops=np.minimum(ends.astype(np.int64),hi).astype(np.longdouble)
 g=stops-starts;e=R[first:last].astype(np.longdouble)-c*starts
 integ=np.sum(e*e*g-e*c*g*g+c*c*g*g*g/3,dtype=np.longdouble)
 mean=np.sum(e*g-c*g*g/2,dtype=np.longdouble)/(hi-lo)
 print('continuous_block',lo,hi,'integral_E_squared',str(integ),'integral_divided_by_lo_squared',str(integ/np.longdouble(lo)**2),'mean_E',str(mean))
# Uniform integer-height sampling, deterministic spacing 1000.
samples=np.arange(10000,10**9+1,1000,dtype=np.int64)
r=np.searchsorted(x,samples,side='right').astype(np.int64)
e=(r.astype(np.longdouble)-c*samples)/np.sqrt(samples.astype(np.longdouble))
e=e.astype(float);mean=e.mean();std=e.std();q=np.quantile(e,[0,.001,.01,.05,.25,.5,.75,.95,.99,.999,1])
print('sampling_rule: all integer X=10000+1000*k <=1e9; samples=',len(samples))
print('standardized_discrepancy mean',mean,'standard_deviation',std,'skewness',float(np.mean(((e-mean)/std)**3)),'excess_kurtosis',float(np.mean(((e-mean)/std)**4)-3))
print('quantile_probabilities',[0,.001,.01,.05,.25,.5,.75,.95,.99,.999,1]);print('quantiles',q.tolist())
print('lag_one_correlation',float(np.corrcoef(e[:-1],e[1:])[0,1]))
np.savetxt(base/'A_discrepancy_samples.csv',np.c_[samples,r,e],delimiter=',',header='X,R_X,(R_X-C0_X)/sqrt_X',comments='',fmt=['%d','%d','%.17g'])
# Compact exact output: unique heights and multiplicities, little-endian u32 pairs.
# The resulting gzip is a lossless encoding of every solution height.
packed=np.empty((len(h),2),dtype='<u4');packed[:,0]=h;packed[:,1]=m
with gzip.GzipFile(filename=str(base/'A_census_1e9_height_multiplicity.u32.gz'),mode='wb',mtime=0,compresslevel=9) as out:out.write(packed.tobytes())
print('exact_height_receipt',hashlib.sha256(path.read_bytes()).hexdigest())
print('compressed_output: gzip of consecutive (height,multiplicity) pairs, uint32 little endian')
