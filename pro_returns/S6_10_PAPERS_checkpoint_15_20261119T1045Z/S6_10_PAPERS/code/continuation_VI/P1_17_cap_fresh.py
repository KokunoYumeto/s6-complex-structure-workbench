#!/usr/bin/env python3
"""Exact cap calculation from the statement packet; no inherited code imported."""
from fractions import Fraction
from pathlib import Path
import json

M=[[1,0,0,0,0,0],[0,1,1,2,2,1],[0,-1,0,-1,0,1],[1,-1,-1,-1,-1,-1],[-1,1,0,0,0,0],[1,0,0,1,0,0]]
G=[[1,0,0,0,0,0],[2,0,0,0,-1,0],[-1,0,-1,0,0,0],[-1,0,0,-1,0,0],[2,-1,0,0,0,0],[-1,1,1,1,1,1]]
v=[1,3,-2,-1,2,0]
ell=[1,0,0,0,0,0]
I=[[int(i==j) for j in range(6)] for i in range(6)]
def mm(A,B):return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def mv(A,w):return [sum(a*b for a,b in zip(row,w)) for row in A]
powers=[I]
for _ in range(5):powers.append(mm(powers[-1],M))
assert powers[5]==I and all(powers[j]!=I for j in range(1,5))
assert mv(M,v)==v
assert mm(G,M)==mm(powers[4],G)
assert mm(G,G)==I
assert mm([ell],M)==[ell] and mm([ell],G)==[ell]
a=[Fraction(x,5) for x in v]
obstruction=mv(G,a)[0]+mv(powers[4],a)[0]
assert obstruction==Fraction(2,5) and obstruction.denominator!=1
for k in range(5):
    assert mm([ell],mm(powers[k],G))==[ell]
    assert mm([ell],powers[k])==[ell]
out={'status':'all assertions passed','deck_order':5,'M_fixes_v':True,'G_conjugates_M_to_inverse':True,'obstruction_mod_Z':'2/5','lift_choices_checked':5,'translation_scope':'All translations: the integral covector ell annihilates (M^-1-I)c identically.'}
Path(__file__).with_name('P1_17_cap_fresh.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
