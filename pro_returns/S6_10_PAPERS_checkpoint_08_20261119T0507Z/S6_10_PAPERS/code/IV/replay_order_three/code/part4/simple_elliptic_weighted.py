from pathlib import Path
import json
import sympy as s

def monomials(weights,n):
 if n<0:return []
 return [(i,j,k) for i in range(n//weights[0]+1) for j in range(n//weights[1]+1) for k in range(n//weights[2]+1) if sum(a*b for a,b in zip(weights,(i,j,k)))==n]
rows=[]
for r in (1,2,3):
 chiB=3*(2-r);chiF=18-chiB
 mult=[s.Rational(chiF+chiB*((-1)**j),6) for j in range(6)]
 assert sum(mult)==chiF and mult[0]==3
 lower=sum(mult[1:]);M=3-r
 assert lower==9+3*r and lower>M
 rows.append({'intersection_points':r,'fixed_curve_Euler':chiB,'Milnor_Euler':chiF,'virtual_character_multiplicities':[int(v) for v in mult],'nontrivial_H2_rank_lower':int(lower),'transverse_Milnor_sum':M})
pa={}
for weights,D in [((1,2,3),7),((1,3,4),9)]:
 vals={str(e):len(monomials(weights,e-sum(weights))) for e in range(1,D+1)}
 assert vals[str(D)]==1 and vals[str(D-1)]==1
 assert all(vals[str(e)]==0 for e in range(1,D-1))
 pa[str(weights)]=vals
# Quadratic characters at the order-four vertex cannot equal the equation character1.
quad=sorted(set((a+b)%4 for a in (1,3) for b in (1,3)))
assert quad==[0,2]
# Explicit E6 warning example has smooth cubic tangent on the first blowup.
X,Y,Z=s.symbols('X Y Z');G=X*Y**2+X**2*Z+Z**3
partials=[s.diff(G,q) for q in (X,Y,Z)]
chart_units={}
for q in (X,Y,Z):
 B=s.groebner(partials+[q-1],X,Y,Z)
 assert B.contains(s.Integer(1))
 chart_units[str(q)]=True
out={'status':'PASS','degree_six_character_bounds':rows,'weighted_arithmetic_genera':pa,'order_four_quadratic_characters':quad,'explicit_smooth_cubic_chart_checks':chart_units,'degree_seven_rank_bounds':[{'Euler_complement':3,'H2_nontrivial_lower':18,'M':0},{'Euler_complement':2,'H2_nontrivial_lower':12,'M':1}]}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('Reduced simple-elliptic weighted models: PASS')
for row in rows: print(row)
print('Weighted arithmetic genera:',pa)
print('Order-four quadratic characters:',quad)
