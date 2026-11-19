#!/usr/bin/env python3
"""Exact differential check of the phase-preserving real compression handle."""
from pathlib import Path
import json
import sympy as sp
r,s,C,S,gr,gs,gp=sp.symbols('r s C S g_r g_s g_phi', real=True)
J=sp.Matrix([
    [C,0,-r*S],
    [0,C,-s*S],
    [S,0,r*C],
    [0,-S,-s*C],
    [gr,gs,gp]
])
G=sp.groebner([C*C+S*S-1],C,S,r,s,gr,gs,gp,order='lex')
det=G.reduce(sp.expand((J.T*J).det()))[1]
target=(r*r+s*s)*(1+gr*gr+gs*gs)+gp*gp
assert sp.expand(det-target)==0
x=(r+sp.I*s)*C
y=(r-sp.I*s)*S
assert sp.expand(x*y-(r*r+s*s)*C*S)==0
data={
    'map':['x=z*cos(phi)','y=conj(z)*sin(phi)','gamma=g(z,phi)'],
    'domain_phi':'0<=phi<=pi/2',
    'base_value':'q=|z|^2*cos(phi)*sin(phi)>=0',
    'Gram_determinant':str(target),
    'immersion_off_core':'|z|^2>0',
    'immersion_at_core':'g_phi(0,phi)!=0, since the two center gamma values are separated',
    'injectivity_off_core':'|z|^2=|x|^2+|y|^2; tan(phi)=|y|/|x|; x or conjugate(y) gives the phase of z',
    'injectivity_at_core':'gamma=g(0,phi) is strictly monotone',
    'incoming_boundary':'q=epsilon gives the regular source smoothing annulus, as a gamma graph',
    'outgoing_faces':['phi=0: x=z, y=0','phi=pi/2: x=0, y=conj(z)'],
    'actual_boundary_graph':'f(p,gamma)=r0*exp(2*pi*i*(gamma-g_epsilon(p)))',
    'page_avoidance':'arg(q-epsilon)+2*pi*d*gamma=phase; d=12 in the primitive case, d=4 in the weighted case; choose the fixed gamma arc shorter than 1/(2*d)'
}
out=Path(__file__).resolve().parent
(out/'real_handle.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
