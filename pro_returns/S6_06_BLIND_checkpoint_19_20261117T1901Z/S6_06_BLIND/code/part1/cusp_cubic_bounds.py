"""Sharp endpoint record for the positive cusp determinant polynomial."""
from pathlib import Path
import contextlib,io,json
with contextlib.redirect_stdout(io.StringIO()):
 exec(Path(__file__).with_name('certified_minimum_cusp_annulus.py').read_text().split('stack=[')[0])
delta=arb('.01');q=acb(arb(0,delta),arb(0,delta));n=160
G=acb_mat(6,3);tt=tail(n,abs(q))
for i in range(6):
 for j in range(3):
    vv=acb_poly([Cs[k][i,j] for k in range(n+1)])(q);eps=tt*hr[i]*fc[j]
    G[i,j]=vv+acb(arb(0,eps),arb(0,eps))
T=acb_mat([[G[i,j] for j in range(3)] for i in range(3)])
DD=acb_mat([[G[i+3,j] for j in range(3)] for i in range(3)])
CC=T*DD.inv();BB=arb_mat([[CC[i,j].imag for j in range(3)] for i in range(3)])
c2=sum(BB[i,i] for i in range(3));c1=sum(BB[i,i]*BB[j,j]-BB[i,j]*BB[j,i] for i in range(3) for j in range(i+1,3));c0=BB.det()
yy=-delta.log()/(2*arb.pi());coeff=[yy*yy*yy+c2*yy*yy+c1*yy+c0,3*yy*yy+2*c2*yy+c1,3*yy+c2,arb(1)]
assert all(x>0 for x in coeff)
out={'radius':'.01','variable':'v=y+log(.01)/(2π)>=0','coefficients_constant_to_cubic':[{'lower':x.lower().str(80),'upper':x.upper().str(80)} for x in coeff]}
print(json.dumps(out,indent=2),flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
