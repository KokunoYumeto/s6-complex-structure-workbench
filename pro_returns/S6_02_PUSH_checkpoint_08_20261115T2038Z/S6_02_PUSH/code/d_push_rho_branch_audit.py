"""Independent audit of the unsuccessful one-square rho contraction.
Its derivative bound remains useful for uniqueness of all refined roots.
"""
from d_root_gradient_certificate import *

rho=acb(rat('1/2'),arb(3).sqrt()/2)
zc=(2-rho)/3
q=(2*P*I*(rho+square(rat('1/50')))).exp()
A=(1/series(zc,(2*P*I*rho).exp())[1]).mid()
for r in ['13/1000','7/500','3/200','1/64','2/125','17/1000','9/500','1/50','1/40']:
    z,d=contraction(zc.mid(),q,A,r)
    print(r,json.dumps(d))
