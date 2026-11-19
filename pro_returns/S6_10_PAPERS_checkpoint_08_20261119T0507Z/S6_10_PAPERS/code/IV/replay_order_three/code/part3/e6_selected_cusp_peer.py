#!/usr/bin/env python3
"""Independent selected-cusp source/Cartier/seed checks for the K95 audit."""
from pathlib import Path
import sympy as s,json,hashlib
R=Path(__file__).resolve().parents[2]
w,S,Z,P=s.symbols('w S Z P');v=w*w-1;D=w*w-3
xi,Y,q=s.symbols('xi Y q');T=v+q;checks=[]
def eq(n,e):
 z=s.factor(s.together(e));assert z==0,(n,z);checks.append(n)
eq('full physical height',Y*Y-(xi+v)**3-(3-2*w*w)*(xi+v)**2-D*T*(xi+v)-T*T-(Y*Y-xi*xi*(xi+w*w)-q*(q+v*v+D*xi)))
pg=(1+w)/(1-w);s6=w*(1+pg**6)/(1-pg**6);c6=(1+w)**6/(6+20*w*w+6*w**4)
eq('six-section theta coefficient',c6-(w-s6));Zs=(S-w)/(S+w)
eq('point theta full arrow',S-s6-c6*(1-Zs/pg**6)/(1-Zs))
eq('positive node Miller value',(w+1)**6/(w-s6)-(6+20*w*w+6*w**4))
eq('negative node Miller value',(1-w)**6/(-w-s6)-(6+20*w*w+6*w**4))
eq('six-section even',s6.subs(w,-w)-s6)
eq('reference coefficient reflection',c6.subs(w,-w)-pg**(-6)*c6)
eq('theta reflection factor',(1-P**6/Z)/(1-1/Z)-P**6*(1-Z/P**6)/(1-Z))
r=(3-2*w*w)/D**2
eq('actual four-turn parameter degree',r-s.Rational(1,3)+w**4/(3*D**2))
Gxi=-v;GY=v+w**6*q
eq('formal weighted section parameter',-Gxi/w**2/(GY/w**3)-w*v/GY)
for n in [-1,1]:
 eq('signed cap norm '+str(n),n*n-1)
 eq('source norm scalar '+str(n),2*n*n-2)
for j in range(-20,21):
 k=-6-18*j*(j-1);A=-1-3*j*(j-1)
 eq('physical seed '+str(j),k-6*A)
 eq('reflection seed '+str(j),(-6-18*(1-j)*(-j))-k)
src=R/'notes/part3_e6_selected_cusp_working.md'
out={'status':'PASS','checks':len(checks),'identities':checks,'source':str(src.relative_to(R)),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest()}
(R/'code/part3/e6_selected_cusp_peer.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
