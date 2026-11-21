from pathlib import Path
import sympy as S,json,hashlib,datetime
r,y,k,w,b,j,x=S.symbols('r y k w b j x',nonzero=True)
# The resolved node is b*w=x*y and z=r*b.
Ua={'b':y*k,'w':w,'x':k*w,'y':y,'z':r*y*k,'r':r}
Ub={'b':b,'w':j*x,'x':x,'y':b*j,'z':r*b,'r':r}
checks={}
for name,c in [('Ua',Ua),('Ub',Ub)]:
 checks[name+'_node']=S.expand(c['b']*c['w']-c['x']*c['y'])
 checks[name+'_original_neck']=S.expand(c['z']*c['w']-r*c['x']*c['y'])
# Transition Ub coordinates (b,x,j)=(k*y,k*w,1/k).
sub={b:k*y,x:k*w,j:1/k}
checks['overlap_all']=[S.simplify(Ub[v].subs(sub,simultaneous=True)-Ua[v]) for v in Ua]
checks['overlap_inverse']=[S.simplify((k*y).subs({y:b*j,k:1/j},simultaneous=True)-b),S.simplify((k*w).subs({w:j*x,k:1/j},simultaneous=True)-x)]
# Exact comparison to corrected A1.2: (X,Y,Z,V,u)=(z,r*w,x,y,r^2).
# A1.2 first chart (V,Y/u,a)=(y,w/r,r*k).
A1=[r*k*y,r*r*(w/r),(r*k)*(w/r),y]
P1=[Ua['z'],r*Ua['w'],Ua['x'],Ua['y']]
checks['A12_chart1']=[S.simplify(a-c) for a,c in zip(A1,P1)]
# A1.2 second chart (X,Z,b_A)=(r*b,x,j/r).
A2=[r*b,r*r*(j/r)*x,x,(j/r)*(r*b)]
P2=[Ub['z'],r*Ub['w'],Ub['x'],Ub['y']]
checks['A12_chart2']=[S.simplify(a-c) for a,c in zip(A2,P2)]
checks['A12_overlap_character']=S.simplify((r*k)*(j/r)).subs(j,1/k)-1
# Involution lifts in the two charts and preserves the mapped old coordinates.
for name,c,change in [('Ua',Ua,{r:-r,k:-k,w:-w}),('Ub',Ub,{r:-r,b:-b,j:-j})]:
 transformed={v:S.simplify(e.subs(change,simultaneous=True)) for v,e in c.items()}
 expected={v:(-e if v in ['r','b','w'] else e) for v,e in c.items()}
 checks[name+'_involution']=[S.simplify(transformed[v]-expected[v]) for v in c]
# q is the product of three chart coordinates; the antidiagonal is a+b=c.
checks['q_chart1']=S.expand(Ua['x']*Ua['y']-k*w*y)
checks['q_chart2']=S.expand(Ub['x']*Ub['y']-x*b*j)
rays=[S.Matrix(v) for v in [(0,0,1),(1,0,1),(0,1,1),(1,1,1)]]
newcones=[(0,1,2),(1,2,3)];oldcones=[(0,1,3),(0,2,3)]
newd=[int(S.Matrix.hstack(*(rays[i] for i in cone)).det()) for cone in newcones]
oldd=[int(S.Matrix.hstack(*(rays[i] for i in cone)).det()) for cone in oldcones]
charnew=S.Matrix([1,1,-1]);charold=S.Matrix([1,-1,0])
newedge=[tuple(map(int,v)) for v in rays if charnew.dot(v)==0]
oldedge=[tuple(map(int,v)) for v in rays if charold.dot(v)==0]
def zero(v):return all(zero(t) for t in v) if isinstance(v,list) else v==0
assert all(zero(v) for v in checks.values())
assert all(abs(d)==1 for d in newd+oldd)
res={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':{q:([str(x) for x in v] if isinstance(v,list) else str(v)) for q,v in checks.items()},'old_diagonal':oldedge,'selected_diagonal':newedge,'new_cone_determinants':newd,'old_cone_determinants':oldd,'old_character':'x/z: a-b','new_character':'z/(r*y): a+b-c','A12_map':'(X,Y,Z,V,u)=(z,r*w,x,y,r^2)','A12_chart_parameters':['(V,Y/u,a)=(y,w/r,r*k)','(X,Z,b_A)=(r*b,x,j/r)'],'scope':'Exact exposed recomputation for P2.10 proof Steps6–8; no targeted-before-proof or whole-theorem independence credit.'}
p=Path(__file__).resolve().parents[1]/'output/S6_SERIES_PUBLISH_I_P210_resolution_exact.json'
p.write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
