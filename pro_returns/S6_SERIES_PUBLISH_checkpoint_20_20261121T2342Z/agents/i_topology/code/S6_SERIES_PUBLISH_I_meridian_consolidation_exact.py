import sympy as S,json
from pathlib import Path
s,v,mu,C,k=S.symbols('s v mu C k');U=-12*k
sigmaP=S.Matrix([6*mu*v,v*U+C*v-6*v*v+6*v]);sigmaB=S.Matrix([6*mu*v,-6*v*v+v*(C-12*k)])
oP=S.Matrix([-mu*s/2,s*s/24-C*s/12+v*(s+U)])
F=S.Matrix([mu*(s+12*v)/2,C*(s+12*v)/12-(s+12*v)**2/24+6*v]);oB=sigmaB-F
assert S.simplify(sigmaP-sigmaB)==S.Matrix([0,6*v]);assert S.simplify(oP-oB)==S.Matrix([0,6*v]);assert S.simplify(sigmaP-oP-F)==S.zeros(2,1)
m,n,ai,bi,aj,bj=S.symbols('m n ai bi aj bj');li=S.Matrix(S.symbols('li0:4'));lj=S.Matrix(S.symbols('lj0:4'));E32=S.zeros(4);E32[2,1]=1;E41=S.zeros(4);E41[3,0]=1
Ai=S.eye(4)-12*m*ai*E32+12*(m*ai+n*bi)*E41;Aj=S.eye(4)-12*m*aj*E32+12*(m*aj+n*bj)*E41
comm=S.simplify(li+Ai*lj-lj-Aj*li)
assert S.expand(comm[3]-12*((m*ai+n*bi)*lj[0]-(m*aj+n*bj)*li[0]))==0
assert (Ai-S.eye(4))*(Aj-S.eye(4))==S.zeros(4)
result={'origin_difference_both':str(S.simplify(oP-oB)),'common_clutching_difference':str(S.simplify(sigmaP-oP)),'commutator_difference':str(comm),'nilpotent_cross_products':'zero','outcome':'all exact assertions passed','scope':'Verification of explicit morphisms in publication proof consolidation; no preread-independent credit.'}
Path(__file__).resolve().parent.parent.joinpath('output/S6_SERIES_PUBLISH_I_meridian_consolidation_exact.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
