#!/usr/bin/env python3
"""Exact source-coordinate morphism used by the renewed credit comparison."""
from pathlib import Path
import sympy as s
import json
v,t=s.symbols('s t')
T=4*(1-v)/(27*v);S=4/(27*t+4);u=3*v/s.sqrt(2)
checks={
 'base_inverse_t':s.factor(T.subs(v,S)-t),
 'base_inverse_s':s.factor(S.subs(t,T)-v),
 'x_coefficient':s.factor(u**4*T+3*v**3*(v-1)),
 'constant_coefficient':s.factor(u**6*T**2-2*v**4*(v-1)**2),
 'marked_point_y':s.simplify(u**3*T-s.sqrt(2)*v**2*(1-v)),
 'marked_point_on_Engel_curve':s.factor((s.sqrt(2)*v**2*(1-v))**2-2*v**4*(v-1)**2),
 'j_map':s.factor((6912/(27*t+4)).subs(t,T)-1728*v)}
assert all(z==0 for z in checks.values())
out={'all_passed':True,'checks':{k:str(x) for k,x in checks.items()},'check_count':len(checks),
 'map':'s=4/(27t+4), X=(3s/sqrt(2))^2 x, Y=(3s/sqrt(2))^3 y',
 'scope':'Exact invertible generic-fibre/source-coordinate map; no completed threefold or cap identification inferred.'}
p=Path(__file__).resolve().parents[2]/'analysis/continuation_IV/Engel_III_source_map.output.json'
p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
