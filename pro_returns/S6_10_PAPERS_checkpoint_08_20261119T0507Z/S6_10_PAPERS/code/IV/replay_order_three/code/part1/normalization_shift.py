"""Certified comparison of the original point-normalized and algebraic splittings."""
from minimum_tools import *
path=[acb(1),acb(1,1),aq(cusp/2)+acb(0,1),aq(cusp/2)]
Y=X*certified_transport(path)
a_split=Y[0,3]*acb(0,-1)*96/(acb.pi()*625)
print('a_split =',a_split.str(100),flush=True)
print('h_original = h_b - Im(a_split)',flush=True)
print('xi_b = xi_original - a_split',flush=True)
print('c_original_min = -h_b_min + Im(a_split)',flush=True)
out={'path':['1','1+i','lambda*/2+i','lambda*/2'],'a_split':a_split.str(100),
     'formula':'sigma_original=sigma_b-a_split alpha e; h_original=h_b-Im(a_split); xi_b=xi_original-a_split',
     'step_bounds':stats}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
