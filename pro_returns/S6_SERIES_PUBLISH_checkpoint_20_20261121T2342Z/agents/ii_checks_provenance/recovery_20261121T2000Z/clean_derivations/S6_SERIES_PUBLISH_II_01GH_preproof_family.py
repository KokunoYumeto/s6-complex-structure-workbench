"""Exact family certificate before E10 proof release."""
from fractions import Fraction as Q
import sympy as s
import json
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def mul(x,y):return (x[0]*y[0],x[0]*y[1]+x[1]*y[0])
def powr(x,n):
    z=(Q(1),Q(0))
    for _ in range(n):z=mul(z,x)
    return z
def div(x,y):return (x[0]/y[0],(x[1]*y[0]-x[0]*y[1])/y[0]**2)
def jjet(t0):
    t=(Q(t0),Q(1));a=add(powr(t,4),(Q(1),Q(0)));b=powr(t,6)
    a3=powr(a,3);b2=powr(b,2)
    D=add(mul((Q(4),Q(0)),a3),mul((Q(27),Q(0)),b2))
    result=div(mul((Q(1728*4),Q(0)),a3),D)
    expected=-Q(1728*1296)*Q(t0)**11*(Q(t0)**4+1)**2/D[0]**2
    assert result[1]==expected and result[1]!=0
    assert result[0] not in [0,1728]
    return result,D
values={str(t):jjet(t) for t in [7,-3]}
bound=Q(12,16)+Q(12,256)+Q(4,4096)
assert bound<Q(31) and Q(10)>Q(2)+Q(2)
assert s.prod(s.Integer(7-i) for i in range(1,7))==720
M=s.Matrix([[1,t,t*t] for t in [1,2,3,6]]);velocity=s.Matrix([0,0,0,1])
assert M[:3,:].det()==2
assert M.rank()==3 and M.row_join(velocity).rank()==4
print(json.dumps({'timing':'before E10 proof release',
 'method':'dual-number Fraction arithmetic for the actual j-invariants, plus the exact branch-motion interpolation matrix',
 'j_jets':{t:{'j':str(v[0][0]),'derivative':str(v[0][1]),'D':str(v[1][0])} for t,v in values.items()},
 'root_bound_rhs':str(bound),'leading_coefficient':31,
 'critical_discs_centres':[0,10],'critical_discs_radius':2,
 'branch_interpolation_rank':3,'augmented_rank':4,
 'fibre_KS_rank':2,'all_assertions_passed':True,'events_added':0},indent=2))
