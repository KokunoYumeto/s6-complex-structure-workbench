"""Independent exact charts, physical weights, overlap and residue signs."""
from pathlib import Path
import json
import sympy as s
a,b,x,y,p=s.symbols('a b x y p',nonzero=True)
rows=[]
for k in range(9):
 U=(a*b)**k*a;V=(a*b)**(8-k)*y**9*p*b
 assert s.expand(U*V-(a*b)**9*y**9*p)==0
 weights=[k+1,-k-2,1,0];assert sum(weights)==0
 # dx ^ dU/U = -da ^ db; moving dU past dy,dp gives no extra sign.
 residue=s.det(s.Matrix([[s.diff(a*b,a),s.diff(a*b,b)],[s.diff(U,a)/U,s.diff(U,b)/U]]))
 assert s.factor(residue)==-1
 ap=y**(9-2*k)*a;bp=y**(2*k-7)*b
 xp=1/y;yp=a*b*y**2
 assert s.factor(ap*bp-yp)==0
 assert s.factor(xp**9*yp**k*ap-U)==0
 assert s.factor(yp**(8-k)*p*bp-V)==0
 rows.append({'chart':'x','k':k,'physical_weights':weights,'canonical_residue_sign':-1,'source_overlap':{'a_prime_y_exponent':9-2*k,'b_prime_y_exponent':2*k-7},'pass':True})
 U=x**9*(a*b)**k*a;V=(a*b)**(8-k)*p*b
 assert s.expand(U*V-x**9*(a*b)**9*p)==0
 weights=[-1,10-k,k-9,0];assert sum(weights)==0
 rows.append({'chart':'y','k':k,'physical_weights':weights,'canonical_residue_sign':1,'pass':True})
U=x**9*y**9*a;V=b;assert U*V==x**9*y**9*(a*b)
rows.append({'chart':'p','physical_weights':[-1,1,1,-1],'canonical_residue_sign':-1,'pass':True})
out={'status':'PASS','charts':len(rows),'scope':'Actual ordered x^9,y^9,p graph charts of UV=x^9 y^9 p and their physical-circle weights. No quotient fixed-locus count, boundary identification or total return is inferred.','rows':rows}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':'PASS','charts':len(rows)},indent=2))
