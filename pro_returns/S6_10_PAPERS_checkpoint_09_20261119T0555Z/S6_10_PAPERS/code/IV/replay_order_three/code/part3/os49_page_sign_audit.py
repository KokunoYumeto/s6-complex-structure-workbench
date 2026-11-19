"""Fresh reconstruction certificate, not byte replay of the lost audit."""
from pathlib import Path
import sympy as S,json
checks=[]
def ck(name,v):
 assert bool(v),name
 checks.append(name)
x,y,g,th=S.symbols("x y g th", real=True)
for e in (-1,1):
 beta=-e*y
 h=2*x-3*y
 theta=-e*(x-y-g)
 M=S.Matrix([[2,3*e],[-e,-1]])
 ck(f"det_{e}",M.det()==1)
 ck(f"matrix_{e}",M*S.Matrix([x,beta])+S.Matrix([0,e*g])==S.Matrix([h,theta]))
 ck(f"binding_{e}",S.expand(beta-2*theta-e*(h-2*g))==0)
 T=S.diag(1,1,-e)
 ck(f"signed_normal_{e}",((-e)*T).det()==1)
a,t=S.symbols("a t", real=True)
G=S.Matrix([[-S.sin(a),S.cos(t)*S.cos(a),S.sin(t)*S.cos(a)],[S.cos(a),S.cos(t)*S.sin(a),S.sin(t)*S.sin(a)],[0,S.sin(t),-S.cos(t)]])
R=S.Matrix([[S.cos(a),-S.sin(a),0],[S.sin(a),S.cos(a),0],[0,0,1]])
ck("clutch_factorization",all(S.trigsimp(z)==0 for z in G-R*G.subs(a,0)))
ck("clutch_SO3",S.trigsimp(G.det())==1)
for k in range(1,8):
 for l in range(0,8):
  m=3*k;h=6*l+1
  pair=(6*k*h,24*k*(3*l+1))
  ck(f"physical_pair_{k}_{l}",pair==(2*m*h,4*m*(h+1)))
  ck(f"index_{k}_{l}",S.Rational(pair[0],6)-S.Rational(pair[1],24)==3*k*l)
out={"status":"PASS","provenance":"new exact certificate for reconstructed PSA, not original 46-check byte stream","count":len(checks),"checks":checks}
p=Path(__file__).with_suffix(".json");p.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"status":"PASS","count":len(checks)}))
